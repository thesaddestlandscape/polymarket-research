# Hipótesis automáticas — 2026-09-14 06:15 UTC
_Generado por shadow_postmortem.py sobre 431295 resoluciones (PNL=+45795.35€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.385` → IC=-0.150 (n=195)

  - _Acción_: SKIP cuando `py_entrada` < 0.385
  - _Potencial_: sin este filtro IC_bueno=+0.243 (n=407)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=401)

- **PATRÓN** `py_entrada` > `0.385` → IC=+0.243 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.385 (IC base=+0.116)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.205 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.116)

- **PATRÓN** `banda_hit_calibrado` > `0.8056` → IC=+0.260 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8056 (IC base=+0.116)

- **PATRÓN** `banda_z` > `10.65` → IC=+0.212 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.65 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.133 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 11.0 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=478)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.123 (n=401)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.132 (n=131)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 98.0 (IC base=+0.038)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.375` → IC=-0.129 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=324)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=314)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.233 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.213 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.804` → IC=+0.263 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.804 (IC base=+0.123)

- **PATRÓN** `banda_z` > `11.552` → IC=+0.273 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.552 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=394)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 88.0 (IC base=+0.034)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.207 (n=97)

- **FILTRO** `banda_hit_calibrado` < `0.6329` → IC=-0.198 (n=41)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6329
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=84)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=82)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=92)

- **PATRÓN** `py_entrada` > `0.56` → IC=+0.244 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.56 (IC base=+0.098)

- **PATRÓN** `banda_hit_calibrado` > `0.6329` → IC=+0.244 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6329 (IC base=+0.098)

- **PATRÓN** `banda_z` > `6.173` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `banda_z` > 6.173 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=101)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `1149.6186` → IC=+0.146 (n=63)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1149.6186 (IC base=+0.098)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.128 (n=76)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=-0.018)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.191)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.382 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.191)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `146.18` → IC=-0.260 (n=5433)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.18
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=16307)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `n_ballenas` < `4.0` → IC=-0.132 (n=1906)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=1157)

- **FILTRO** `restante_s_al_confirmar` < `139.02` → IC=-0.285 (n=765)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.02
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=2298)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `134.36` → IC=-0.290 (n=687)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 134.36
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2062)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `144.23` → IC=-0.150 (n=1401)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.23
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4207)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `157.24` → IC=-0.254 (n=1264)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.24
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3794)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.46` → IC=-0.345 (n=1355)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.46
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=2753)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.48` → IC=-0.233 (n=148)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=148)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.191 (n=82)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=169)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.291 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=130)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=118)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.236 (n=51)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `py_entrada` > `0.3` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=28)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.196 (n=11177)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.69 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=2751)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `10962.1513` → IC=+0.196 (n=879)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 10962.1513 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.143 (n=8364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=10071)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.245 (n=7437)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.169 (n=5456)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7054.2523` → IC=+0.172 (n=1728)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7054.2523 (IC base=+0.135)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.355 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `13070.3814` → IC=+0.213 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13070.3814 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.207 (n=1174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.297 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=1658)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `12625.2295` → IC=+0.203 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12625.2295 (IC base=+0.200)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.179 (n=263)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.62 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=280)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `4690.1012` → IC=+0.152 (n=225)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4690.1012 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.185 (n=274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.164 (n=548)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.425 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=541)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `3846.6396` → IC=+0.159 (n=417)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3846.6396 (IC base=+0.135)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=2221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=1889)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.329 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.233)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.297 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `4381.435` → IC=+0.236 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4381.435 (IC base=+0.233)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.132 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 11.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.137 (n=516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.225 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=610)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `1984.6996` → IC=+0.161 (n=343)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1984.6996 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=146)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.082)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.217 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.195 (n=1028)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 12.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.424 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.181 (n=936)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.277 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.180 (n=1077)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.03 (IC base=+0.176)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.184 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.335 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3435.4625` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3435.4625 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.143 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.228 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=318)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=104)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=8570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=7284)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.219 (n=3087)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `5363.4643` → IC=+0.345 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5363.4643 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.179 (n=2060)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.181 (n=2158)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.74 (IC base=+0.168)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.342 (n=137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.321)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.332 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.321)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.364 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.321)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=2136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=1805)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=2064)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=1830)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.249 (n=1907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=1625)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.326 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.316 (n=47)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=1770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.193 (n=1477)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.444 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.447 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.443 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `9410.7841` → IC=+0.462 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9410.7841 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.443 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.458 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `11570.9911` → IC=+0.461 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11570.9911 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.451 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.445)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.445)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.461 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.445)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.444 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.445)

- **PATRÓN** `libro_liquidez` > `3810.0701` → IC=+0.457 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3810.0701 (IC base=+0.445)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.433 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.422)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.430 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.422)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.420 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.422)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` < `12.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=18)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **FILTRO** `libro_liquidez` < `5005.2013` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 5005.2013
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=29821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.230 (n=14061)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=5193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=4395)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4649)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.166)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=4487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=4481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=1898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4655)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.168)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=2283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=1742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.208 (n=1563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.254 (n=2141)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=5013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.193 (n=3401)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.245 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.190)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.200 (n=3843)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.124)

- **PATRÓN** `restante_min` < `4.05` → IC=+0.134 (n=3513)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.05 (IC base=+0.124)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.145 (n=3852)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.94 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=4642)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `lag_apertura_s` < `3.39` → IC=+0.150 (n=3515)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.39 (IC base=+0.124)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=1931)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.130)

- **PATRÓN** `restante_min` < `3.99` → IC=+0.138 (n=1750)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 3.99 (IC base=+0.130)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.145 (n=1823)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.93 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.147 (n=2579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.130)

- **PATRÓN** `lag_apertura_s` < `4.31` → IC=+0.146 (n=1743)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 4.31 (IC base=+0.130)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=1912)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.47` → IC=+0.126 (n=2338)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.47 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.149 (n=1936)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.95 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=2353)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.83` → IC=+0.146 (n=1771)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.83 (IC base=+0.118)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1617.6179` → IC=+0.296 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1617.6179 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.300 (n=278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.274)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.330 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.274)

- **PATRÓN** `libro_liquidez` > `5090.6456` → IC=+0.293 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5090.6456 (IC base=+0.274)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.329 (n=297)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.293 (n=429)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.383 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1492.929` → IC=+0.312 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1492.929 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.335 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.330)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.359 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.330)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.330)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.368 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.330)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.438 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.434 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.432 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `1860.5823` → IC=+0.438 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1860.5823 (IC base=+0.430)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.440 (n=165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.436 (n=185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.446 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.432 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `2127.0131` → IC=+0.454 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2127.0131 (IC base=+0.431)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.281 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.260)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.319 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.281 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1367.6878` → IC=+0.292 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.6878 (IC base=+0.260)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.281 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.260)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.319 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.281 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1367.6878` → IC=+0.292 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.6878 (IC base=+0.260)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9758` → IC=+0.230 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9758 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` < `0.2097` → IC=+0.247 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2097 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.842` → IC=+0.166 (n=2220)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.842 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `1.2291` → IC=+0.245 (n=1428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2291 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `1.0676` → IC=+0.245 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0676 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` < `0.1761` → IC=+0.193 (n=3860)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1761 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2534` → IC=+0.195 (n=749)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2534 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.8612` → IC=+0.192 (n=3724)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.8612 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `1.472` → IC=+0.196 (n=3723)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.472 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.575` → IC=+0.125 (n=7035)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.575 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.165 (n=2100)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` > `0.8706` → IC=+0.168 (n=1476)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.8706 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.1691` → IC=+0.223 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1691 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.4654` → IC=+0.194 (n=3686)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4654 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.204 (n=3453)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.056)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.186 (n=431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.185 (n=585)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.007 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3242` → IC=+0.169 (n=1284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3242 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.193 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 8.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.044` → IC=+0.283 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.044 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.201 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.6362` → IC=+0.156 (n=1178)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.6362 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.442` → IC=+0.164 (n=1178)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.442 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.182 (n=1377)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.06 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.188 (n=944)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 63.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.236 (n=844)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.252 (n=857)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.1914` → IC=+0.278 (n=638)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1914 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.251 (n=649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.062` → IC=+0.287 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.062 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.34` → IC=+0.247 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.34 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.235 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.281 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.7379` → IC=+0.267 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7379 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1578.46` → IC=+0.249 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1578.46 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.233 (n=428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.1107` → IC=+0.237 (n=428)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1107 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=1013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9278` → IC=+0.252 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9278 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.1993` → IC=+0.220 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1993 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.1319` → IC=+0.215 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1319 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.902` → IC=+0.232 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.902 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2661` → IC=+0.226 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2661 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.8755` → IC=+0.215 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8755 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.213 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.0749` → IC=+0.214 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0749 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.4925` → IC=+0.228 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4925 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.4189` → IC=+0.219 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4189 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `11835.8417` → IC=+0.230 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11835.8417 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.159 (n=914)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0048 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0744` → IC=+0.161 (n=346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0744 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6814` → IC=+0.176 (n=1038)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6814 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.48` → IC=+0.181 (n=180)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 11.48 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2044` → IC=+0.147 (n=1038)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2044 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.6119` → IC=+0.139 (n=1038)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6119 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1536` → IC=+0.201 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1536 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4311` → IC=+0.152 (n=929)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4311 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4146` → IC=+0.148 (n=929)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4146 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `12617.1565` → IC=+0.150 (n=692)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 12617.1565 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `314.0` → IC=+0.152 (n=567)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 314.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.192 (n=1260)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0057 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=1326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.194 (n=628)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 8.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.256 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.394` → IC=+0.229 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.394 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` < `0.107` → IC=+0.189 (n=1058)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.107 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.3774` → IC=+0.175 (n=164)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.3774 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.664` → IC=+0.184 (n=1173)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.664 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.193 (n=1425)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.196 (n=632)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 30.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.220 (n=1082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1461` → IC=+0.213 (n=476)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1461 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=510)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.231 (n=952)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3902 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.68` → IC=+0.232 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.68 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.378` → IC=+0.212 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.378 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.266 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.3036` → IC=+0.223 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3036 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1890.8984` → IC=+0.230 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1890.8984 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.199 (n=888)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 51.0 (IC base=+0.211)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.156 (n=88)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1585)

- **PATRÓN** `ibs_20min` > `0.9299` → IC=+0.164 (n=269)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.9299 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.4759` → IC=+0.340 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4759 (IC base=+0.010)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.255` → IC=+0.136 (n=498)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 4.255 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` < `0.5993` → IC=+0.399 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5993 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `1.1808` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1808 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2246` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2246 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `2.4621` → IC=+0.340 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4621 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `1.8189` → IC=+0.346 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8189 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.347 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` > `0.1574` → IC=+0.183 (n=165)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1574 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `1.0419` → IC=+0.140 (n=431)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.0419 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `0.6129` → IC=+0.138 (n=489)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6129 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2145` → IC=+0.216 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2145 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4984` → IC=+0.168 (n=393)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4984 (IC base=-0.006)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.140 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=226)

- **FILTRO** `ibs_20min` < `0.3636` → IC=-0.163 (n=90)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3636
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=184)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.128 (n=1623)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=823)

- **FILTRO** `sigma_ewma_delta_pct` > `8.602` → IC=-0.199 (n=267)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.602
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2179)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.148 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0049 (IC base=+0.040)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.198 (n=94)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.75 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `1.1052` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1052 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.5788` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5788 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `0.7744` → IC=+0.340 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7744 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1442` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1442 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.9536` → IC=+0.267 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9536 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` > `0.6573` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6573 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` < `0.6535` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6535 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` > `0.9321` → IC=+0.171 (n=138)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.9321 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.1972` → IC=+0.181 (n=158)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1972 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.0856` → IC=+0.217 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0856 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.209 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4963 (IC base=-0.048)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.227 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=-0.048)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.627` → IC=-0.191 (n=402)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.627
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=1210)

- **FILTRO** `ibs_20min` < `0.6452` → IC=-0.159 (n=1063)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6452
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=549)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.197 (n=344)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1268)

- **FILTRO** `ibs_20min` > `0.775` → IC=-0.197 (n=609)

  - _Acción_: SKIP cuando `ibs_20min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1830)

- **PATRÓN** `dist_vwap_pct` > `0.8853` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8853 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` < `0.2397` → IC=+0.302 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2397 (IC base=-0.086)

- **PATRÓN** `volumen_regimen` > `0.6119` → IC=+0.282 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6119 (IC base=-0.086)

- **PATRÓN** `volumen_pendiente_norm` < `0.1542` → IC=+0.263 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1542 (IC base=-0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.0729` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0729 (IC base=-0.086)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.265 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=-0.086)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.272 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` > `0.4431` → IC=+0.250 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4431 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.2364` → IC=+0.237 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2364 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `1.094` → IC=+0.295 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.094 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.1062` → IC=+0.252 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1062 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.2413` → IC=+0.255 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2413 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5844` → IC=+0.232 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5844 (IC base=-0.031)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.232 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=-0.031)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.009` → IC=+0.174 (n=2385)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.009 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.4583` → IC=+0.175 (n=6380)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4583 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.6892` → IC=+0.276 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6892 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.481` → IC=+0.141 (n=3387)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 3.481 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6734` → IC=+0.231 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6734 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` < `0.114` → IC=+0.224 (n=3652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.114 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2481` → IC=+0.255 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2481 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `1.4784` → IC=+0.235 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4784 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.7883` → IC=+0.235 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7883 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.278 (n=3318)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.562` → IC=+0.147 (n=6476)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.562 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.6563` → IC=+0.238 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6563 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.159` → IC=+0.229 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.159 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` > `1.2024` → IC=+0.253 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2024 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.2527` → IC=+0.322 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2527 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `1.6267` → IC=+0.247 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6267 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` > `2.3812` → IC=+0.254 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3812 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.250 (n=2364)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.064)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3548` → IC=-0.125 (n=635)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3548
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=1292)

- **FILTRO** `sigma_ewma_delta_pct` > `4.369` → IC=-0.160 (n=377)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.369
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1250)

- **PATRÓN** `ibs_20min` > `0.8636` → IC=+0.258 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8636 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.963` → IC=+0.167 (n=506)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.963 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.302 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.8723` → IC=+0.193 (n=330)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.8723 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `2.6662` → IC=+0.201 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6662 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.214 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4617` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4617 (IC base=-0.020)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.463 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8333` → IC=-0.151 (n=543)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8333
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=1633)

- **PATRÓN** `volumen_regimen` > `0.6498` → IC=+0.129 (n=551)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6498 (IC base=+0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.2213` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2213 (IC base=+0.008)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.147 (n=199)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.008)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 235.0 (IC base=+0.008)

- **PATRÓN** `volumen_regimen` > `1.1352` → IC=+0.231 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1352 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.341 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.777` → IC=+0.228 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.777 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.4319` → IC=+0.211 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4319 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `513.0` → IC=+0.208 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 513.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.270 (n=1021)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.0948` → IC=+0.247 (n=381)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0948 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.258 (n=432)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.471` → IC=+0.273 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.471 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` < `0.1113` → IC=+0.259 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1113 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `2.3483` → IC=+0.241 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3483 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.6757` → IC=+0.243 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6757 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.272 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.316 (n=411)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.316 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` < `0.3388` → IC=+0.285 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3388 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.883` → IC=+0.301 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.883 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.3458` → IC=+0.308 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3458 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` < `1.6224` → IC=+0.273 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6224 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `2.2257` → IC=+0.284 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2257 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.285 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `1881.2284` → IC=+0.296 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1881.2284 (IC base=+0.277)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.270 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.277)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2323` → IC=-0.209 (n=318)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2323
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=957)

- **FILTRO** `ibs_20min` > `0.8229` → IC=-0.180 (n=426)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8229
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1280)

- **PATRÓN** `ibs_20min` > `0.8027` → IC=+0.140 (n=434)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.8027 (IC base=-0.018)

- **PATRÓN** `dist_vwap_pct` > `0.3046` → IC=+0.221 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3046 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` < `0.9335` → IC=+0.211 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9335 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` > `0.6044` → IC=+0.184 (n=242)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6044 (IC base=-0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.2672` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2672 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4915` → IC=+0.273 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4915 (IC base=-0.018)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.239 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 119.0 (IC base=-0.018)

- **PATRÓN** `dist_vwap_pct` > `0.1085` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1085 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.2648` → IC=+0.146 (n=193)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2648 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.9603` → IC=+0.139 (n=167)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.9603 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `0.7237` → IC=+0.155 (n=169)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7237 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.333 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.783` → IC=+0.235 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.783 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `2.2837` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2837 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.208 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6667` → IC=-0.198 (n=773)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.249 (n=783)

- **FILTRO** `ibs_20min` > `0.7213` → IC=-0.236 (n=415)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7213
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=1246)

- **FILTRO** `sigma_ewma_delta_pct` > `4.704` → IC=-0.166 (n=393)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.704
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1268)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.249 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1799` → IC=+0.308 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1799 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.283 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` > `0.7198` → IC=+0.273 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7198 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.1055` → IC=+0.274 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1055 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.318 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.317 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.318 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.027)

- **PATRÓN** `ibs_20min` < `0.4118` → IC=+0.122 (n=831)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.4118 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` > `0.5424` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.5424 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` < `0.1676` → IC=+0.188 (n=286)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1676 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.243 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7144 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2178` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2178 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.6339` → IC=+0.197 (n=292)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.6339 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.5315` → IC=+0.172 (n=291)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.5315 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.202 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0146` → IC=+0.323 (n=663)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0146 (IC base=+0.265)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.281 (n=469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.265)

- **PATRÓN** `ibs_20min` > `0.9` → IC=+0.335 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9 (IC base=+0.265)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.314 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.265)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.355` → IC=+0.292 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.355 (IC base=+0.265)

- **PATRÓN** `volumen_regimen` > `0.68` → IC=+0.281 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.68 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` < `0.1098` → IC=+0.269 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1098 (IC base=+0.265)

- **PATRÓN** `volumen_pendiente_norm` > `0.2387` → IC=+0.297 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2387 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` < `1.5517` → IC=+0.276 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5517 (IC base=+0.265)

- **PATRÓN** `volumen_spike_ratio` > `2.2147` → IC=+0.268 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2147 (IC base=+0.265)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.269 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.265)

- **PATRÓN** `libro_liquidez` > `2570.3048` → IC=+0.271 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2570.3048 (IC base=+0.265)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.273 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0202` → IC=+0.297 (n=490)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0202 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.272 (n=1025)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.266 (n=1143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.303 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3902 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` > `0.5156` → IC=+0.288 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5156 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.415` → IC=+0.285 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.415 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` > `1.2502` → IC=+0.309 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2502 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2431` → IC=+0.356 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2431 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `2.5563` → IC=+0.261 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5563 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.1751` → IC=+0.264 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1751 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.267 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `2546.904` → IC=+0.279 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2546.904 (IC base=+0.266)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.180 (n=1904)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0047 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.203 (n=1907)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3331` → IC=+0.175 (n=5021)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3331 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=5935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.6957` → IC=+0.231 (n=5098)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6957 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1614` → IC=+0.198 (n=2491)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1614 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.216` → IC=+0.249 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.216 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2153` → IC=+0.165 (n=3813)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2153 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.161 (n=3813)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6211 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.107` → IC=+0.186 (n=2226)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.107 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `2.3099` → IC=+0.170 (n=4759)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.3099 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.679` → IC=+0.167 (n=1803)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.679 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3813.5418` → IC=+0.174 (n=1902)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3813.5418 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.186 (n=4615)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 124.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.185 (n=3660)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0063 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.204 (n=1829)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=2652)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.4578` → IC=+0.225 (n=5482)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4578 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.265` → IC=+0.193 (n=957)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.265 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.1885` → IC=+0.152 (n=4012)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1885 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6252` → IC=+0.150 (n=4013)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6252 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2918` → IC=+0.232 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2918 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.574` → IC=+0.167 (n=2127)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.574 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6473` → IC=+0.176 (n=1611)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6473 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.169 (n=4447)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 128.0 (IC base=+0.169)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.216 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.208 (n=433)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3176` → IC=+0.206 (n=955)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3176 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.226 (n=421)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.049` → IC=+0.310 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.049 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.237 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.5605` → IC=+0.184 (n=863)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.5605 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `1.4412` → IC=+0.183 (n=863)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4412 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.243 (n=605)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.248 (n=613)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.297 (n=456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.242 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.1074` → IC=+0.265 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1074 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.936` → IC=+0.249 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.936 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0697` → IC=+0.234 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0697 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.273 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8823` → IC=+0.246 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8823 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6706` → IC=+0.243 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6706 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.239 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1903.8` → IC=+0.261 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.8 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.235 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.247 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3628` → IC=+0.176 (n=823)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3628 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=869)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.4506` → IC=+0.224 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4506 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.211` → IC=+0.217 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.211 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.669` → IC=+0.229 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.669 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `1.2757` → IC=+0.179 (n=823)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.2757 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2363` → IC=+0.194 (n=178)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2363 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.4117` → IC=+0.203 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4117 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `11188.0133` → IC=+0.193 (n=735)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 11188.0133 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `409.0` → IC=+0.165 (n=655)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 409.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.177 (n=822)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.286` → IC=+0.168 (n=934)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.286 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.167 (n=858)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.5155` → IC=+0.193 (n=934)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5155 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.047` → IC=+0.220 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.047 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.164 (n=934)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.204 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.158` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.158 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.4386` → IC=+0.159 (n=825)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4386 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4133` → IC=+0.154 (n=825)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4133 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.156 (n=248)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 233.0 (IC base=+0.149)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.201 (n=940)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.1945` → IC=+0.200 (n=627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1945 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.219 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=442)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.286 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.573` → IC=+0.271 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.573 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.1074` → IC=+0.191 (n=768)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1074 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `3.6503` → IC=+0.201 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6503 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.206 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.233 (n=788)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.219 (n=358)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.2234` → IC=+0.231 (n=525)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2234 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.265 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.248 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.666` → IC=+0.269 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.666 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.274 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `3.5171` → IC=+0.244 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5171 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1889.461` → IC=+0.242 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1889.461 (IC base=+0.218)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.189 (n=789)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0065 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.4224` → IC=+0.173 (n=897)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4224 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=897)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.4158` → IC=+0.210 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4158 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.1332` → IC=+0.196 (n=594)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1332 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.201` → IC=+0.242 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.201 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.8639` → IC=+0.168 (n=598)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8639 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.1981` → IC=+0.181 (n=299)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.1981 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.2879` → IC=+0.229 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2879 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4062` → IC=+0.177 (n=292)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4062 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.5456` → IC=+0.186 (n=291)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.5456 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `7316.3109` → IC=+0.195 (n=598)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7316.3109 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.170 (n=734)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 156.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.155 (n=842)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.006 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.372` → IC=+0.144 (n=955)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.372 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.596` → IC=+0.177 (n=955)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.596 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.141 (n=950)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.181` → IC=+0.196 (n=189)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 12.181 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8624` → IC=+0.136 (n=638)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8624 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6135` → IC=+0.130 (n=954)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.6135 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.7906` → IC=+0.127 (n=561)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.7906 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `9896.1185` → IC=+0.151 (n=433)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 9896.1185 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.147 (n=714)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0077 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=1097)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` > `0.5156` → IC=+0.196 (n=1071)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5156 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `1.0126` → IC=+0.222 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0126 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.371` → IC=+0.249 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.371 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `1.2184` → IC=+0.122 (n=1073)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2184 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` < `0.1682` → IC=+0.128 (n=1071)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1682 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `2.1617` → IC=+0.123 (n=906)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.1617 (IC base=+0.112)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1096)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2897.8254` → IC=+0.199 (n=486)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2897.8254 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.137 (n=769)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 49.0 (IC base=+0.112)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.149 (n=462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0058 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5366` → IC=+0.206 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5366 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.135 (n=973)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.335` → IC=+0.153 (n=223)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 7.335 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `1.0447` → IC=+0.124 (n=924)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.0447 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2729` → IC=+0.182 (n=124)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2729 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `1.573` → IC=+0.129 (n=400)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.573 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `2.1727` → IC=+0.140 (n=412)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.1727 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `3082.2041` → IC=+0.156 (n=350)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3082.2041 (IC base=+0.112)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0177` → IC=+0.210 (n=682)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0177 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.1642` → IC=+0.217 (n=450)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1642 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1057)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.205 (n=469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.250 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.72 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `1.1774` → IC=+0.234 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1774 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.339` → IC=+0.239 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.339 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.2022` → IC=+0.204 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2022 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.6887` → IC=+0.212 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6887 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2414` → IC=+0.260 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2414 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2067` → IC=+0.216 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2067 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4285` → IC=+0.205 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4285 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.202 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.240 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.208 (n=488)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.022 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.223 (n=359)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.213 (n=535)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=497)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.4309` → IC=+0.238 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4309 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.4931` → IC=+0.206 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4931 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.3` → IC=+0.232 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.3 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.6289` → IC=+0.215 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6289 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.292 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.2526` → IC=+0.195 (n=828)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.2526 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.4611` → IC=+0.189 (n=941)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4611 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2506.382` → IC=+0.211 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2506.382 (IC base=+0.202)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.152 (n=593)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0043 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.160 (n=612)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0071 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0942` → IC=+0.156 (n=449)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0942 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.4079` → IC=+0.173 (n=1347)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.4079 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.7813` → IC=+0.196 (n=179)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7813 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.692` → IC=+0.178 (n=609)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 3.692 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8615` → IC=+0.165 (n=770)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8615 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.170 (n=371)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4339` → IC=+0.161 (n=429)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4339 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.8216` → IC=+0.158 (n=857)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.8216 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.152 (n=1490)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `11786.9126` → IC=+0.181 (n=449)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 11786.9126 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.172 (n=385)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 20.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.151 (n=465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0036 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.124 (n=931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 11.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.635` → IC=+0.138 (n=1393)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.635 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.836` → IC=+0.127 (n=547)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 3.836 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.1669` → IC=+0.138 (n=357)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1669 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.2358` → IC=+0.122 (n=1167)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.2358 (IC base=+0.103)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.155 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0037 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.0997` → IC=+0.167 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0997 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.161 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 8.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.9034` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.9034 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.6865` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6865 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.192 (n=144)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.5894` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.5894 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.0645` → IC=+0.136 (n=127)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.0645 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.2054` → IC=+0.134 (n=255)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.2054 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.5129` → IC=+0.135 (n=258)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.5129 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `9457.747` → IC=+0.168 (n=302)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 9457.747 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.163 (n=93)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 147.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.202 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.3358` → IC=+0.136 (n=448)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3358 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.6102` → IC=+0.172 (n=395)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.6102 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` > `0.7151` → IC=+0.134 (n=400)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.7151 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1556` → IC=+0.201 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1556 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `2.4163` → IC=+0.137 (n=439)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.4163 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.160 (n=139)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 156.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.253 (n=184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.229 (n=138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.0948` → IC=+0.231 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0948 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.2795` → IC=+0.245 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2795 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.3742` → IC=+0.239 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3742 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.085` → IC=+0.252 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.085 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.221 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8331 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.156` → IC=+0.243 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.156 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2439` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2439 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.368` → IC=+0.232 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.368 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.0232` → IC=+0.265 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0232 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `12429.5841` → IC=+0.229 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12429.5841 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.137 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0047 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.3318` → IC=+0.141 (n=235)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.3318 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.514` → IC=+0.142 (n=93)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.514 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.143 (n=82)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.089)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3485` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3485
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=321)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.208 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.297` → IC=+0.143 (n=127)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 5.297 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `2940.9508` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2940.9508 (IC base=+0.071)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.124 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 14.0 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.4524` → IC=+0.158 (n=258)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.4524 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.7183` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.7183 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `2.513` → IC=+0.124 (n=235)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.513 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.131 (n=201)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 44.0 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.160 (n=154)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0232 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0189` → IC=+0.167 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0189 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3227` → IC=+0.172 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3227 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.191 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 16.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.193 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.7425` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.7425 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.2105` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2105 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.931` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.931 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.182 (n=130)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.9878` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.9878 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.3079` → IC=+0.173 (n=154)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.3079 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.5702` → IC=+0.212 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5702 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=162)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.226 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.188 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.022 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.126 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.619` → IC=+0.127 (n=164)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.619 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.998` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.998 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.079` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.079 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `0.889` → IC=+0.122 (n=109)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` > 0.889 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.5879` → IC=+0.162 (n=69)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5879 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 16.0 (IC base=+0.114)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.194 (n=3255)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0085 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=7473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.4763` → IC=+0.214 (n=7171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4763 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.883` → IC=+0.200 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.883 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.566` → IC=+0.222 (n=3518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.566 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.882` → IC=+0.165 (n=3231)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.882 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.186 (n=1368)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.6455` → IC=+0.181 (n=2271)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.6455 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.172 (n=8544)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `3752.6696` → IC=+0.173 (n=2391)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3752.6696 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.196 (n=5111)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 96.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.194 (n=4386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0066 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.4734` → IC=+0.183 (n=6574)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.4734 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=2517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.56` → IC=+0.237 (n=6578)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.56 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.228` → IC=+0.164 (n=4168)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.228 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.811` → IC=+0.203 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.811 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.6239` → IC=+0.156 (n=1514)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6239 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `1.2015` → IC=+0.162 (n=1514)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.2015 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.254 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.3025` → IC=+0.189 (n=2651)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.3025 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.175 (n=5449)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 128.0 (IC base=+0.180)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.220 (n=402)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.232 (n=547)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.211 (n=810)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.322 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.814` → IC=+0.320 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.814 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2282` → IC=+0.239 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2282 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.5664` → IC=+0.195 (n=490)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5664 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.5899` → IC=+0.192 (n=371)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5899 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.213 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.223 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.263 (n=829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.269 (n=842)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.2026` → IC=+0.284 (n=629)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2026 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=865)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.3529` → IC=+0.288 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3529 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.536` → IC=+0.259 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.536 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.62` → IC=+0.265 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.62 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.311 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.7096` → IC=+0.294 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7096 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1579.5248` → IC=+0.268 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1579.5248 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.253 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.190 (n=379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1817` → IC=+0.159 (n=754)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1817 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.4595` → IC=+0.213 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4595 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1241` → IC=+0.194 (n=632)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1241 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.852` → IC=+0.164 (n=266)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.852 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.374` → IC=+0.156 (n=1002)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.374 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.2802` → IC=+0.164 (n=1131)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2802 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1542` → IC=+0.181 (n=312)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1542 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.4502` → IC=+0.161 (n=1078)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4502 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7674` → IC=+0.160 (n=718)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7674 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `10605.0228` → IC=+0.173 (n=1010)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 10605.0228 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `497.0` → IC=+0.166 (n=1009)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 497.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.196 (n=337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0024 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.3196` → IC=+0.168 (n=1011)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3196 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.174 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 18.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.6443` → IC=+0.207 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6443 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.618` → IC=+0.188 (n=184)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 11.618 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.164 (n=1011)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1888 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.1495` → IC=+0.220 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1495 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.409` → IC=+0.169 (n=913)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.409 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `456.0` → IC=+0.158 (n=717)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 456.0 (IC base=+0.155)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.228 (n=1128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=1183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.220 (n=1008)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.6739` → IC=+0.252 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6739 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.426` → IC=+0.292 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.426 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.1413` → IC=+0.222 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1413 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.6784` → IC=+0.221 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6784 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.236 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 60.0 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.231 (n=1090)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.231 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1472` → IC=+0.228 (n=480)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1472 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.251 (n=412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.230 (n=520)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` < `0.3774` → IC=+0.267 (n=959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3774 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.708` → IC=+0.276 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.708 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.3607` → IC=+0.291 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3607 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.7916` → IC=+0.214 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7916 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.2531` → IC=+0.229 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2531 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `1893.9584` → IC=+0.230 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1893.9584 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.218 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.227)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.172 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0038 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4291` → IC=+0.141 (n=1213)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4291 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=1266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.7151` → IC=+0.240 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7151 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.5564` → IC=+0.184 (n=337)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.5564 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.295` → IC=+0.173 (n=521)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 4.295 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.165 (n=809)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8812 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.227 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7416` → IC=+0.162 (n=776)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7416 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `8939.3872` → IC=+0.232 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8939.3872 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.150 (n=957)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 167.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.185 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0032 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4263` → IC=+0.150 (n=972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4263 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.6897` → IC=+0.185 (n=972)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6897 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.2016` → IC=+0.137 (n=901)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2016 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.137` → IC=+0.196 (n=146)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.137 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8591` → IC=+0.135 (n=648)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8591 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `1.1737` → IC=+0.150 (n=324)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.1737 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.261 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.276 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `2.1354` → IC=+0.161 (n=411)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.1354 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `11059.7035` → IC=+0.184 (n=324)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 11059.7035 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.136 (n=893)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 196.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.463` → IC=+0.178 (n=1245)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.463 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `1.0011` → IC=+0.174 (n=216)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 1.0011 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.373` → IC=+0.211 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.373 (IC base=+0.097)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=864)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `2917.745` → IC=+0.248 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2917.745 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.126 (n=905)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 53.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.172 (n=520)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0061 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1197` → IC=+0.148 (n=393)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1197 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.625` → IC=+0.208 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.625 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.1913` → IC=+0.137 (n=966)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1913 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.379` → IC=+0.123 (n=1134)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 3.379 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.7146` → IC=+0.158 (n=519)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7146 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.2169` → IC=+0.183 (n=181)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2169 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4645` → IC=+0.148 (n=342)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4645 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `2.2251` → IC=+0.124 (n=464)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.2251 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2938.2572` → IC=+0.163 (n=393)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2938.2572 (IC base=+0.114)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.217 (n=570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.205 (n=1119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.311 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.1781` → IC=+0.237 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1781 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.539` → IC=+0.241 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.539 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.2398` → IC=+0.207 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2398 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.208 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.236 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.6032` → IC=+0.233 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6032 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2550.7164` → IC=+0.207 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2550.7164 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.246 (n=462)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.224 (n=462)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.201 (n=1461)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.505` → IC=+0.251 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.505 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.2617` → IC=+0.204 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2617 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.954` → IC=+0.264 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.954 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2333` → IC=+0.239 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2333 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.260 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.2322` → IC=+0.190 (n=1060)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.2322 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.443` → IC=+0.196 (n=1205)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.443 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2526.0585` → IC=+0.202 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2526.0585 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.179 (n=1114)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 37.0 (IC base=+0.199)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=2424)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.149 (n=2015)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0096 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.531` → IC=+0.147 (n=2290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.531 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.156 (n=791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.156 (n=798)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 4.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.9311` → IC=+0.204 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9311 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1866` → IC=+0.145 (n=771)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1866 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.694` → IC=+0.150 (n=724)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 5.694 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.7085` → IC=+0.129 (n=639)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.7085 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.902` → IC=+0.139 (n=967)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.902 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1739` → IC=+0.163 (n=627)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1739 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.4563` → IC=+0.153 (n=756)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4563 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.8986` → IC=+0.154 (n=1510)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.8986 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `8642.3169` → IC=+0.145 (n=1039)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8642.3169 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.198 (n=613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0037 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.4775` → IC=+0.163 (n=1830)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4775 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.165 (n=619)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 4.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.1825` → IC=+0.163 (n=805)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1825 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.6851` → IC=+0.157 (n=304)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6851 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.225` → IC=+0.149 (n=1808)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.225 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2492` → IC=+0.145 (n=1739)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2492 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.156 (n=867)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.5773` → IC=+0.147 (n=1812)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.5773 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.154 (n=1208)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=2424)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `12048.7616` → IC=+0.162 (n=830)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 12048.7616 (IC base=+0.141)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.159 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.176 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0066 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0919` → IC=+0.183 (n=102)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0919 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.8759` → IC=+0.174 (n=305)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.8759 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.2308` → IC=+0.174 (n=139)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.2308 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.25` → IC=+0.162 (n=389)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 8.25 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.2448` → IC=+0.155 (n=305)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.2448 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.8157` → IC=+0.183 (n=203)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.8157 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.149 (n=340)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.7022` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.7022 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `12593.964` → IC=+0.195 (n=273)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 12593.964 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.203 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3657` → IC=+0.151 (n=851)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3657 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.174 (n=311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.1485` → IC=+0.171 (n=375)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1485 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.6044` → IC=+0.149 (n=386)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6044 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.6011` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6011 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.225` → IC=+0.164 (n=830)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.225 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8855` → IC=+0.182 (n=568)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8855 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0691` → IC=+0.162 (n=406)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0691 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.5736` → IC=+0.147 (n=848)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.5736 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.153 (n=565)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `12064.8695` → IC=+0.150 (n=760)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 12064.8695 (IC base=+0.138)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.194 (n=233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0068 (IC base=+0.162)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.198 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0102 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.432` → IC=+0.171 (n=466)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.432 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.9885` → IC=+0.232 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9885 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.366` → IC=+0.218 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.366 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2095` → IC=+0.187 (n=148)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2095 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `3.4677` → IC=+0.166 (n=528)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.4677 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.8234` → IC=+0.171 (n=472)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8234 (IC base=+0.162)

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

- **PATRÓN** `libro_liquidez` > `2463.7708` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2463.7708 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.148 (n=696)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0088 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.140 (n=696)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0045 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4959` → IC=+0.146 (n=696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4959 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.165 (n=237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.141 (n=249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 4.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.7971` → IC=+0.160 (n=316)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.7971 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.9851` → IC=+0.182 (n=152)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.9851 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.4234` → IC=+0.144 (n=652)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4234 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.796` → IC=+0.147 (n=693)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.796 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1117` → IC=+0.145 (n=612)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1117 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6442` → IC=+0.138 (n=696)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.6442 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.175` → IC=+0.153 (n=211)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.175 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.161 (n=228)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=643)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `8854.7868` → IC=+0.154 (n=622)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8854.7868 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.169 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0071 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.5081` → IC=+0.191 (n=557)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.5081 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.168 (n=381)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 11.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.1015` → IC=+0.164 (n=557)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.1015 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.160 (n=257)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.3694` → IC=+0.159 (n=567)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.3694 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.058` → IC=+0.167 (n=265)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.058 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6473` → IC=+0.181 (n=186)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6473 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.7334` → IC=+0.156 (n=498)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7334 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.186 (n=243)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.165 (n=482)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.447` → IC=+0.169 (n=547)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.447 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `8160.4392` → IC=+0.166 (n=557)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 8160.4392 (IC base=+0.152)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=157)

- **PATRÓN** `ibs_20min` > `0.9848` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.9848 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.803` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 8.803 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.156` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.156 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.5986` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.5986 (IC base=+0.050)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0084` → IC=-0.253 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=264)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=270)

- **FILTRO** `dist_vwap_pct` > `0.1598` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1598
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=192)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.190 (n=401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.005 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.168 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 18.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.6383` → IC=+0.209 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6383 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.160 (n=263)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.185` → IC=+0.185 (n=287)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 4.185 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `0.6219` → IC=+0.134 (n=225)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6219 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2898` → IC=+0.231 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2898 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `2.5476` → IC=+0.146 (n=405)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.5476 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.139 (n=411)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `2468.387` → IC=+0.167 (n=220)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2468.387 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.288 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.129 (n=192)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1598 (IC base=-0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.931` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.931 (IC base=-0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.0826` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0826 (IC base=-0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.178 (n=113)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.3987 (IC base=-0.033)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=137)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=-0.033)

- **PATRÓN** `libro_liquidez` > `2874.2912` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2874.2912 (IC base=-0.033)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.212 (n=182)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.5781` → IC=+0.208 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5781 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.182 (n=86)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.739` → IC=+0.134 (n=110)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 3.739 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `1.0554` → IC=+0.131 (n=155)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0554 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` < `0.0763` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.0763 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `2.0205` → IC=+0.177 (n=122)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.0205 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=180)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2929.9152` → IC=+0.140 (n=145)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2929.9152 (IC base=+0.106)

- **PATRÓN** `drift_60min` |x|≤ `0.0909` → IC=+0.189 (n=43)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0909 (IC base=+0.038)

- **PATRÓN** `ibs_20min` < `0.4723` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4723 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.876` → IC=+0.192 (n=63)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.876 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.9643` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.9643 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0796` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0796 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.038)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.321 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=80)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=71)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.169 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0047 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.6407` → IC=+0.239 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6407 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.1209` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1209 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.109` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.109 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.7864` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.7864 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `0.9231` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.9231 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.7434` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.7434 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `1.3908` → IC=+0.157 (n=129)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.3908 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.154 (n=186)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `1064.9876` → IC=+0.188 (n=155)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1064.9876 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.1021` → IC=+0.188 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1021 (IC base=-0.065)

- **PATRÓN** `ibs_20min` < `0.1926` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1926 (IC base=-0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.069` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.069 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0649` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0649 (IC base=-0.065)

- **PATRÓN** `libro_liquidez` > `1059.8551` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1059.8551 (IC base=-0.065)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` < `0.6744` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6744
  - _Potencial_: sin este filtro IC_bueno=+0.196 (n=156)

- **FILTRO** `sigma_h` > `0.0119` → IC=-0.281 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0119
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=76)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.275 (n=38)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.171 (n=83)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.072)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.131 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 14.0 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.6744` → IC=+0.196 (n=156)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.6744 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.8682` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.8682 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.655` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 3.655 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` > `1.062` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.062 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.0854` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.0854 (IC base=+0.072)

- **PATRÓN** `volumen_spike_ratio` < `2.5681` → IC=+0.164 (n=138)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.5681 (IC base=+0.072)

- **PATRÓN** `libro_liquidez` > `392.9095` → IC=+0.154 (n=134)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 392.9095 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=-0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.25` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.25 (IC base=-0.081)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1546` → IC=-0.365 (n=35)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1546
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=107)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.419 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `dist_vwap_pct` > `0.2306` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2306
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=128)

- **FILTRO** `volumen_pendiente_norm` > `0.082` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.082
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=48)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=109)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=37)

- **FILTRO** `volumen_spike_ratio` > `1.5066` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5066
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=28)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.6687` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.6687
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `dist_vwap_pct` < `0.1009` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1009
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=25)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=25)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.357 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=25)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `volumen_regimen` < `1.0824` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0824
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `sigma_h` > `0.0073` → IC=-0.350 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=20)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.450 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2374` → IC=-0.138 (n=92)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2374
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=179)

- **PATRÓN** `ibs_20min` > `0.6438` → IC=+0.142 (n=199)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6438 (IC base=+0.054)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.133 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.2374` → IC=+0.141 (n=179)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.2374 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.0` → IC=+0.148 (n=86)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 6.0 (IC base=+0.046)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=68)

- **FILTRO** `ibs_20min` < `0.4975` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4975
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=63)

- **FILTRO** `volumen_regimen` < `0.7993` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7993
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=57)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1361 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `1.021` → IC=+0.120 (n=77)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.021 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` > `1.5991` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.5991 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.140 (n=87)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.102)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=55)

- **FILTRO** `ibs_20min` < `0.7272` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7272
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=55)

- **FILTRO** `ibs_20min` > `0.3559` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3559
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=69)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.149 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0042 (IC base=+0.060)

- **PATRÓN** `drift_60min` |x|≤ `0.2768` → IC=+0.132 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.2768 (IC base=+0.060)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.060)

- **PATRÓN** `ibs_20min` > `0.7272` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.7272 (IC base=+0.060)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `1604.9934` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1604.9934 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.26` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.26 (IC base=+0.027)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.5556` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5556
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=49)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=43)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.233 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3593` → IC=+0.143 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3593 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.130 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.7143 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.5856` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.5856 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.1848` → IC=+0.148 (n=69)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1848 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.04 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `514.5372` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 514.5372 (IC base=+0.127)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=415)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2811.7744` → IC=+0.173 (n=148)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2811.7744 (IC base=+0.107)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=415)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2811.7744` → IC=+0.173 (n=148)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2811.7744 (IC base=+0.107)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `11.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=72)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=117)

- **FILTRO** `libro_liquidez` < `2359.8786` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `libro_liquidez` < 2359.8786
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=100)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=181)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=167)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=24)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `libro_liquidez` < `14445.5423` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 14445.5423
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1270)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=49)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=81)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=60)

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
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=526)

- **FILTRO** `liq_usd_total` < `9664.41` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 9664.41
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9593` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9593
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=419)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.435` → IC=-0.132 (n=188)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=420)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=227)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=227)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.188 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=196)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=152)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=152)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.151 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=126)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.140 (n=73)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=94)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=51)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=67)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=151)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=49)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=210)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=210)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=75)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=5866)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=996)

- **FILTRO** `libro_liquidez` < `15830.8412` → IC=-0.153 (n=252)

  - _Acción_: SKIP cuando `libro_liquidez` < 15830.8412
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=759)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=1194)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.176 (n=2447)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=7408)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.170 (n=2536)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=7674)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.215 (n=395)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=1245)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.156 (n=419)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1404)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.196 (n=426)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=1280)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.221 (n=424)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=1361)

- **FILTRO** `ibs_20min` > `0.2865` → IC=-0.176 (n=446)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2865
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=1339)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.201 (n=396)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=1222)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.190 (n=443)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=1358)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2175)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2119)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2125)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.129 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=214)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.147 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=160)

- **FILTRO** `ibs_20min` < `0.2609` → IC=-0.217 (n=104)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2609
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=105)

- **FILTRO** `py_entrada` > `0.635` → IC=-0.348 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.635
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=142)

- **FILTRO** `ibs_20min` > `0.9763` → IC=-0.208 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9763
  - _Potencial_: sin este filtro IC_bueno=-0.127 (n=140)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=569)

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

- **FILTRO** `drift_7min_pct` |x|> `0.0331` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0331
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.126 (n=7175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=16195)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.274 (n=5792)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=17578)

- **FILTRO** `ibs_7min` < `0.7102` → IC=-0.235 (n=5841)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7102
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=17529)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.161 (n=7832)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=15538)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.222 (n=7248)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=21858)

- **FILTRO** `ibs_7min` > `0.2976` → IC=-0.176 (n=7275)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2976
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=21831)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=872)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2810)

- **FILTRO** `ibs_7min` < `0.7099` → IC=-0.260 (n=1214)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7099
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2468)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.205 (n=860)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=2822)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.146 (n=3424)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1653)

- **FILTRO** `drift_7min_pct` |x|> `0.108` → IC=-0.124 (n=1726)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.108
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=3351)

- **FILTRO** `ibs_7min` > `0.8` → IC=-0.203 (n=1267)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3810)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.141 (n=956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=3157)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.254 (n=1025)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=3088)

- **FILTRO** `ibs_7min` < `0.7615` → IC=-0.184 (n=1026)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7615
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3087)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.171 (n=1027)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3086)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.261 (n=954)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3170)

- **FILTRO** `ibs_7min` > `0.2497` → IC=-0.171 (n=1029)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2497
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3095)

- **FILTRO** `ballena_activa_n` > `112.0` → IC=-0.161 (n=1401)

  - _Acción_: SKIP cuando `ballena_activa_n` > 112.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2723)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.181 (n=854)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=2632)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.323 (n=816)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=2670)

- **FILTRO** `drift_7min_pct` |x|> `0.1842` → IC=-0.129 (n=1185)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1842
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=2301)

- **FILTRO** `ibs_7min` < `0.208` → IC=-0.272 (n=871)

  - _Acción_: SKIP cuando `ibs_7min` < 0.208
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=2615)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.217 (n=871)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=2615)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.232 (n=1242)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=4071)

- **FILTRO** `ibs_7min` > `0.2655` → IC=-0.155 (n=1806)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2655
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=3507)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=1219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=2635)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.249 (n=921)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=2933)

- **FILTRO** `ibs_7min` < `0.7486` → IC=-0.189 (n=963)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7486
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=2891)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.184 (n=957)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=2897)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=963)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2940)

- **FILTRO** `ibs_7min` > `0.2762` → IC=-0.173 (n=975)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2762
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2928)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.180 (n=967)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=2936)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.236 (n=1025)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=3258)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.205 (n=1051)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3232)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.174 (n=1332)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=4175)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.280 (n=931)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3021)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.223 (n=986)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=2966)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.199 (n=975)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=2977)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.199 (n=1243)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=3939)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=930)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=477)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.153 (n=96)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=310)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=519)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3986` → IC=+0.135 (n=667)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3986 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.134 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `314679.3` → IC=+0.133 (n=644)

  - _Acción_: Kelly boost +0.67€ cuando `total_vol_5m` < 314679.3 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.116)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4131` → IC=+0.179 (n=79)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio` |x|> 0.4131 (IC base=+0.098)

- **PATRÓN** `total_vol_5m` < `498.2784` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `total_vol_5m` < 498.2784 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `7735.3085` → IC=+0.130 (n=106)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 7735.3085 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 80.0 (IC base=+0.098)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.200 (n=108)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.193 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 10.0 (IC base=+0.164)

- **PATRÓN** `total_vol_5m` < `5874.669` → IC=+0.163 (n=96)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 5874.669 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3632.1507` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 3632.1507 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 37.0 (IC base=+0.164)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.167 (n=106)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.136 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 13.0 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 36.0 (IC base=+0.116)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0057` → IC=-0.304 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=152)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.218 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=-0.110)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.273 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.271 (n=33)

- **FILTRO** `T_h` > `56.3892` → IC=-0.405 (n=40)

  - _Acción_: SKIP cuando `T_h` > 56.3892
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=-0.086)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `T_h` < `267.9719` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `T_h` < 267.9719
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=37)

- **FILTRO** `T_h` < `87.9936` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `T_h` < 87.9936
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `4.605` → IC=-0.243 (n=68)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.605
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=205)

- **FILTRO** `T_h` > `87.9668` → IC=-0.305 (n=167)

  - _Acción_: SKIP cuando `T_h` > 87.9668
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=56)

- **FILTRO** `pct_vs_K` |x|> `4.5067` → IC=-0.447 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.5067
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=168)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0036` → IC=-0.278 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=75)

- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.357 (n=33)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=67)

- **FILTRO** `T_h` > `144.5878` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `T_h` > 144.5878
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=53)

- **FILTRO** `pct_vs_K` |x|> `2.3742` → IC=-0.425 (n=38)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3742
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=40)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.986` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` > 135.986
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=55)

- **FILTRO** `pct_vs_K` |x|> `4.5225` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.5225
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.385 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `T_h` > `71.0631` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `T_h` > 71.0631
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0101` → IC=-0.210 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0101
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=30)

- **FILTRO** `T_h` > `135.6166` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `T_h` > 135.6166
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=39)

- **FILTRO** `T_h` > `87.8021` → IC=-0.400 (n=28)

  - _Acción_: SKIP cuando `T_h` > 87.8021
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.2005` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.458 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.354)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.354)

- **PATRÓN** `dist_50` > `0.4444` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.354)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.457 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.354)

- **PATRÓN** `edge` > `0.1072` → IC=+0.444 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.408)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.480 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.408)

- **PATRÓN** `T_h` > `0.8587` → IC=+0.439 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8587 (IC base=+0.408)

- **PATRÓN** `dist_50` > `0.4092` → IC=+0.485 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4092 (IC base=+0.408)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.421 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.408)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.444 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.408)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.21` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.21 (IC base=+0.487)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.471 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.487)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.480 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.487)

- **PATRÓN** `T_h` > `1.1323` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1323 (IC base=+0.487)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.487)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.479 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.487)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=113)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=213)

- **FILTRO** `streak_estiramiento` > `0.7259` → IC=-0.133 (n=58)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.7259
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=114)

- **PATRÓN** `streak_estiramiento` < `0.4382` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.4382 (IC base=+0.015)

- **PATRÓN** `streak_estiramiento` < `0.5597` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.5597 (IC base=+0.034)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `991078.0` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `volumen_racha` > 991078.0
  - _Potencial_: sin este filtro IC_bueno=+0.180 (n=23)

- **PATRÓN** `volumen_racha` < `991078.0` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_racha` < 991078.0 (IC base=-0.011)

- **PATRÓN** `libro_liquidez` > `2208.5143` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2208.5143 (IC base=+0.046)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=81)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=83)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=32)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=456)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=462)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=295)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=420)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=850)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=492)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=535)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2211)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1145)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1153)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.189 (n=332)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0038 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.192 (n=332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.009 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0578` → IC=+0.174 (n=332)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0578 (IC base=+0.170)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0587` → IC=+0.174 (n=995)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.0587 (IC base=+0.170)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0963` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0963 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.170)

- **PATRÓN** `ibs_15` > `0.619` → IC=+0.243 (n=995)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.619 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.1038` → IC=+0.176 (n=659)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1038 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.72` → IC=+0.251 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.72 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `2977.0871` → IC=+0.180 (n=663)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2977.0871 (IC base=+0.170)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=292)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.5859` → IC=-0.121 (n=130)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.5859
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=255)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.212 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0023` → IC=+0.197 (n=252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0023 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.0623` → IC=+0.256 (n=84)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0623 (IC base=+0.197)

- **PATRÓN** `drift_15min` |x|≤ `0.374` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.374 (IC base=+0.197)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2433` → IC=+0.221 (n=84)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2433 (IC base=+0.197)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3853` → IC=+0.228 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3853 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.213 (n=259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.199 (n=260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_15` > `0.7732` → IC=+0.267 (n=225)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7732 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3789` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3789 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.209 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.624` → IC=+0.253 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.624 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `14769.4491` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14769.4491 (IC base=+0.197)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.151 (n=233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0061 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.157 (n=106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0055 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.1177` → IC=+0.146 (n=156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1177 (IC base=+0.138)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2435` → IC=+0.188 (n=78)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.2435 (IC base=+0.138)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2712` → IC=+0.171 (n=144)

  - _Acción_: Kelly boost +0.86€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2712 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.138 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.153 (n=243)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_15` > `0.6992` → IC=+0.262 (n=208)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6992 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.4027` → IC=+0.160 (n=245)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.4027 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.996` → IC=+0.217 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.996 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=274)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `10110.2635` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 10110.2635 (IC base=+0.138)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2345` → IC=-0.214 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2345
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=39)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.167 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0047 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.172 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1419` → IC=+0.175 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.1419 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0657` → IC=+0.161 (n=122)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.0657 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1283` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1283 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.241 (n=137)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2071` → IC=+0.155 (n=137)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.2071 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.367` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.367 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3092.4545` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3092.4545 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.136)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5854` → IC=-0.147 (n=114)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5854
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=523)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `8.524` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 8.524
  - _Potencial_: sin este filtro IC_bueno=+0.180 (n=23)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.955` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 14.955 (IC base=-0.005)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.245 (n=96)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0859` → IC=+0.188 (n=126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0859 (IC base=+0.168)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0451` → IC=+0.181 (n=286)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.0451 (IC base=+0.168)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0926` → IC=+0.273 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0926 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.227 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.168)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.260 (n=286)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.1654` → IC=+0.184 (n=153)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1654 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.3009` → IC=+0.170 (n=268)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.3009 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.35` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.35 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.092` → IC=+0.168 (n=257)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 7.092 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2703.9992` → IC=+0.212 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2703.9992 (IC base=+0.168)

- **PATRÓN** `ibs_15` < `0.1053` → IC=+0.168 (n=308)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.84€ cuando `ibs_15` < 0.1053 (IC base=+0.044)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.399 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.341 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.335)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.339 (n=290)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.335)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.370 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.352 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.335)

- **PATRÓN** `ibs_15` > `0.8365` → IC=+0.393 (n=259)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8365 (IC base=+0.335)

- **PATRÓN** `dist_vwap_pct` > `0.4169` → IC=+0.367 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4169 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.335)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.341 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `3925.9545` → IC=+0.347 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3925.9545 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `499.0` → IC=+0.364 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 499.0 (IC base=+0.335)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1204` → IC=+0.338 (n=72)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1204 (IC base=+0.332)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.360 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.336 (n=144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.332)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1017` → IC=+0.339 (n=147)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1017 (IC base=+0.332)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.400 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.362 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.332)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.331 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.332)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.367 (n=164)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.332)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.386 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.472` → IC=+0.346 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.472 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `8959.7753` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8959.7753 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `609.0` → IC=+0.397 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 609.0 (IC base=+0.332)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.372 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.335)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.362 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.335)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.352 (n=126)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.335)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.354 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.335)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.350 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.335)

- **PATRÓN** `ibs_15` > `0.7574` → IC=+0.398 (n=126)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7574 (IC base=+0.335)

- **PATRÓN** `dist_vwap_pct` < `0.2966` → IC=+0.344 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2966 (IC base=+0.335)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.86` → IC=+0.381 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.86 (IC base=+0.335)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.351 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.335)

- **PATRÓN** `libro_liquidez` > `3566.5529` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3566.5529 (IC base=+0.335)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 150.0 (IC base=+0.335)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.194 (n=507)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1523)

- **FILTRO** `ibs_15` < `0.5867` → IC=-0.186 (n=167)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5867
  - _Potencial_: sin este filtro IC_bueno=+0.248 (n=507)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.166 (n=635)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1395)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2875` → IC=+0.218 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2875 (IC base=-0.056)

- **PATRÓN** `ibs_15` > `0.5867` → IC=+0.248 (n=507)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5867 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` < `0.2631` → IC=+0.174 (n=397)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.2631 (IC base=-0.056)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1198` → IC=+0.232 (n=670)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1198 (IC base=-0.052)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1839` → IC=+0.235 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1839 (IC base=-0.052)

- **PATRÓN** `ibs_15` < `0.3561` → IC=+0.275 (n=1005)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3561 (IC base=-0.052)

- **PATRÓN** `dist_vwap_pct` > `0.8488` → IC=+0.253 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8488 (IC base=-0.052)

- **PATRÓN** `dist_vwap_pct` < `0.2198` → IC=+0.221 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2198 (IC base=-0.052)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.216 (n=301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=905)

- **FILTRO** `sigma_h` < `0.0031` → IC=-0.239 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0031
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=905)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.218 (n=764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=442)

- **FILTRO** `sigma_ewma_delta_pct` > `19.843` → IC=-0.247 (n=219)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.843
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=987)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.167 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.003 (IC base=+0.074)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2377` → IC=+0.289 (n=36)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2377 (IC base=+0.074)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2964` → IC=+0.264 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2964 (IC base=+0.074)

- **PATRÓN** `ibs_15` > `0.7695` → IC=+0.347 (n=96)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7695 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2294` → IC=+0.273 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2294 (IC base=+0.074)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6448` → IC=-0.235 (n=81)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6448
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=246)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=310)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.153 (n=220)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0039 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0771` → IC=+0.218 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0771 (IC base=+0.129)

- **PATRÓN** `drift_15min` |x|≤ `0.4157` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.4157 (IC base=+0.129)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0547` → IC=+0.133 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0547 (IC base=+0.129)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.221 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 4.0 (IC base=+0.129)

- **PATRÓN** `ibs_15` > `0.6448` → IC=+0.250 (n=246)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6448 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.169 (n=176)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.822` → IC=+0.136 (n=262)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 18.822 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=310)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.202 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.232 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.3488` → IC=+0.226 (n=366)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3488 (IC base=+0.216)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2028` → IC=+0.238 (n=189)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2028 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.245 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=280)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.216)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.263 (n=416)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.727` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.727 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.2198` → IC=+0.215 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2198 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.608` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.608 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `3672.3796` → IC=+0.220 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3672.3796 (IC base=+0.216)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0492` → IC=-0.151 (n=373)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0492
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=125)

- **FILTRO** `drift_60min` |x|> `0.1649` → IC=-0.213 (n=169)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1649
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=329)

- **FILTRO** `drift_15min` |x|> `0.8243` → IC=-0.246 (n=124)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8243
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=374)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1156` → IC=+0.212 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1156 (IC base=-0.046)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1944` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1944 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.248 (n=216)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` < `0.1472` → IC=+0.194 (n=197)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1472 (IC base=-0.046)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0188` → IC=-0.238 (n=303)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0188
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=304)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.244 (n=162)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=445)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1081` → IC=+0.350 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1081 (IC base=-0.051)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.296 (n=292)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.051)

- **PATRÓN** `dist_vwap_pct` > `0.7735` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7735 (IC base=-0.051)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.148 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0071 (IC base=+0.086)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.250 (n=18)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.086)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.1423` → IC=+0.125 (n=46)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.62€ cuando `ibs_15` > 0.1423 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1159` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1159 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.086)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.148 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0071 (IC base=+0.086)

- **PATRÓN** `drift_60min` |x|≤ `0.0856` → IC=+0.250 (n=18)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0856 (IC base=+0.086)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.086)

- **PATRÓN** `ibs_15` > `0.1423` → IC=+0.125 (n=46)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.62€ cuando `ibs_15` > 0.1423 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1159` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1159 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.086)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.295 (n=218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.292 (n=224)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.320 (n=165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2315` → IC=+0.320 (n=165)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2315 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1084` → IC=+0.324 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1084 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.331 (n=494)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2663` → IC=+0.322 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2663 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.316` → IC=+0.304 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.316 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `12383.1611` → IC=+0.319 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12383.1611 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.298 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.287 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0602` → IC=+0.319 (n=92)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0602 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `0.3839` → IC=+0.287 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3839 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2433` → IC=+0.330 (n=92)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2433 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3724` → IC=+0.295 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3724 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.333 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.8593` → IC=+0.310 (n=246)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8593 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2565` → IC=+0.341 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2565 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.471` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.471 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `14273.3051` → IC=+0.327 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14273.3051 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.300 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.301 (n=219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.318 (n=97)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2249` → IC=+0.327 (n=73)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2249 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.330 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.319 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.342 (n=219)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2764` → IC=+0.306 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2764 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` < `0.4406` → IC=+0.303 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4406 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.398` → IC=+0.324 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.398 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.308 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.302 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.295)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.301 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0857` → IC=-0.278 (n=61)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0857
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=191)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.247 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=167)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.161 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=322)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2171` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2171
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=66)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1774` → IC=-0.139 (n=70)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1774
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=71)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2503` → IC=-0.127 (n=65)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2503
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2312` → IC=-0.204 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2312
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2179` → IC=-0.155 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2179
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `sigma_h` < `0.0039` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2099` → IC=-0.389 (n=16)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2099
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1066` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1066
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.239 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `83.3501` → IC=+0.132 (n=180)

  - _Acción_: Kelly boost +0.66€ cuando `T_h` > 83.3501 (IC base=+0.126)

- **PATRÓN** `ratio` < `0.9775` → IC=+0.458 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.126)

- **PATRÓN** `T_h` > `145.8743` → IC=+0.409 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8743 (IC base=+0.347)

- **PATRÓN** `ratio` > `1.0083` → IC=+0.359 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0083 (IC base=+0.347)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9956` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9956 (IC base=+0.085)

- **PATRÓN** `T_h` > `87.9922` → IC=+0.302 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9922 (IC base=+0.299)

- **PATRÓN** `ratio` > `1.0357` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0357 (IC base=+0.299)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9957` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9957 (IC base=+0.186)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.355 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.186)

- **PATRÓN** `T_h` > `87.9956` → IC=+0.344 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9956 (IC base=+0.324)

- **PATRÓN** `ratio` > `1.012` → IC=+0.342 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.324)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1131` → IC=+0.457 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1131 (IC base=+0.406)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.619 sube el IC de +0.170 a +0.243 en UPDOWN_GBM#15min (n=995). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7732 sube el IC de +0.197 a +0.267 en UPDOWN_GBM#BTC#15min (n=225). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6992 sube el IC de +0.138 a +0.262 en UPDOWN_GBM#ETH#15min (n=208). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.136 a +0.241 en UPDOWN_GBM#SOL#15min (n=137). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.168 a +0.260 en UPDOWN_GBM#XRP#15min (n=286). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1053 sube el IC de +0.044 a +0.168 en UPDOWN_GBM#XRP#15min (n=308). Ya aplicado como kelly_boost=+0.84€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5867 sube el IC de -0.056 a +0.248 en UPDOWN_GBM_15M_TARDIO (n=507). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3561 sube el IC de -0.052 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=1005). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7695 sube el IC de +0.074 a +0.347 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=96). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6448 sube el IC de +0.129 a +0.250 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3605 sube el IC de +0.216 a +0.263 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=416). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.148 a +0.333 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de -0.046 a +0.248 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=216). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.051 a +0.296 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=292). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.288 a +0.331 en UPDOWN_GBM_IBS_ALTO (n=494). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8593 sube el IC de +0.281 a +0.310 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=246). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.295 a +0.342 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=219). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8365 sube el IC de +0.335 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=259). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.332 a +0.367 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=164). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7574 sube el IC de +0.335 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=126). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH#sniper` — IC=+0.329 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH` — IC=+0.329 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.375 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.375 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1115 | +0.080 | +116.86€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1115 | +0.080 | +116.86€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 806 | +0.085 | +93.67€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 806 | +0.085 | +93.67€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 233 | +0.045 | +4.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 233 | +0.045 | +4.19€ | 4 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 50 | +0.173 | +20.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 50 | +0.173 | +20.49€ | 0 | 4 |
| ✅ BALLENAS_TARDIAS | 19365 | -0.107 | -2784.40€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1154 | -0.025 | -185.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 18211 | -0.112 | -2598.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3063 | -0.122 | -558.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3063 | -0.122 | -558.69€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1154 | -0.025 | -185.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1154 | -0.025 | -185.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5608 | -0.055 | -517.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5608 | -0.055 | -517.61€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5058 | -0.112 | -394.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5058 | -0.112 | -394.03€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4108 | -0.180 | -967.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4108 | -0.180 | -967.10€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 10784 | -0.046 | +4308.40€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 2932 | -0.008 | +1854.67€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 7852 | -0.061 | +2453.73€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 10784 | -0.046 | +4308.40€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 2932 | -0.008 | +1854.67€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 7852 | -0.061 | +2453.73€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 547 | -0.108 | -102.38€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 19 | -0.023 | -1.66€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 528 | -0.111 | -100.71€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 17 | -0.112 | -1.65€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 17 | -0.112 | -1.65€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 326 | -0.064 | -41.10€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 11 | -0.064 | -3.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 315 | -0.061 | -37.74€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 145 | -0.194 | -49.16€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 8 | +0.040 | +1.69€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#ETH#5min | 137 | -0.212 | -50.85€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 34 | -0.139 | -10.99€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 34 | -0.139 | -10.99€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 25 | -0.093 | +0.52€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 25 | -0.093 | +0.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 70026 | +0.113 | -3773.03€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 11076 | +0.181 | -370.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 268 | -0.115 | -47.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 53752 | +0.100 | -3260.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 4930 | +0.117 | -95.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 8964 | +0.095 | -877.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 36 | -0.158 | -1.29€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 8913 | +0.097 | -864.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 14164 | +0.132 | -281.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3360 | +0.201 | -110.71€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 8907 | +0.110 | -166.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1855 | +0.118 | +18.11€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 9003 | +0.088 | -916.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 43 | -0.056 | -3.06€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 8945 | +0.089 | -902.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 15005 | +0.125 | -302.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4254 | +0.170 | -85.38€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 8971 | +0.109 | -168.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1768 | +0.100 | -40.23€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 13912 | +0.116 | -831.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3347 | +0.186 | -174.42€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 171 | -0.067 | +6.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 9087 | +0.091 | -590.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1307 | +0.137 | -73.60€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 8978 | +0.102 | -563.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 36 | -0.026 | +4.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 8929 | +0.102 | -568.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 11090 | +0.189 | -755.45€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 11090 | +0.189 | -755.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2744 | +0.168 | -294.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2744 | +0.168 | -294.60€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 495 | +0.184 | +17.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 495 | +0.184 | +17.44€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2701 | +0.178 | -248.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2701 | +0.178 | -248.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2428 | +0.238 | -65.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2428 | +0.238 | -65.25€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2643 | +0.190 | -178.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2643 | +0.190 | -178.78€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 518 | +0.442 | -0.34€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 518 | +0.442 | -0.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 200 | +0.441 | -0.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 200 | +0.441 | -0.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 198 | +0.445 | +2.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 198 | +0.445 | +2.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 114 | +0.422 | -3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 114 | +0.422 | -3.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 37799 | +0.194 | -3236.99€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 37799 | +0.194 | -3236.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 6604 | +0.166 | -880.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 6604 | +0.166 | -880.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 5964 | +0.224 | -216.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 5964 | +0.224 | -216.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 6551 | +0.168 | -844.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 6551 | +0.168 | -844.08€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6072 | +0.218 | -253.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6072 | +0.218 | -253.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6250 | +0.200 | -445.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6250 | +0.200 | -445.76€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 6358 | +0.190 | -596.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 6358 | +0.190 | -596.86€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 14027 | +0.124 | +268.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 14027 | +0.124 | +268.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 6950 | +0.130 | +201.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 6950 | +0.130 | +201.33€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 7077 | +0.118 | +66.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 7077 | +0.118 | +66.70€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1196 | +0.289 | -19.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1196 | +0.289 | -19.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 529 | +0.274 | -17.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 529 | +0.274 | -17.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 569 | +0.293 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 569 | +0.293 | -0.46€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 98 | +0.330 | -1.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 98 | +0.330 | -1.23€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 529 | +0.430 | -7.68€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 529 | +0.430 | -7.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 246 | +0.431 | -3.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 246 | +0.431 | -3.14€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 245 | +0.431 | -4.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 245 | +0.431 | -4.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 38 | +0.375 | -0.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 38 | +0.375 | -0.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 789 | +0.070 | -39.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 278 | +0.064 | -20.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 511 | +0.073 | -18.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 50 | +0.115 | +2.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 50 | +0.115 | +2.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 615 | +0.079 | -17.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 104 | +0.104 | +1.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 511 | +0.073 | -18.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 124 | +0.008 | -24.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 124 | +0.008 | -24.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 24387 | +0.098 | -768.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2065 | +0.092 | +22.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 22322 | +0.099 | -791.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 13979 | +0.102 | -219.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2065 | +0.092 | +22.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 11914 | +0.104 | -242.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 4121 | +0.114 | +20.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 4121 | +0.114 | +20.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 6287 | +0.078 | -569.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 6287 | +0.078 | -569.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 698 | +0.260 | -84.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 698 | +0.260 | -84.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 698 | +0.260 | -84.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 698 | +0.260 | -84.89€ | 0 | 4 |
| ✅ GBM_LATE_15M | 18298 | +0.073 | +8188.54€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 18298 | +0.073 | +8188.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 2986 | +0.197 | +2205.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 2986 | +0.197 | +2205.80€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 2678 | +0.175 | +1790.27€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2678 | +0.175 | +1790.27€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 3119 | +0.194 | +2263.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3119 | +0.194 | +2263.96€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 2744 | +0.000 | +405.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2744 | +0.000 | +405.88€ | 1 | 14 |
| ✅ GBM_LATE_15M#SOL | 2720 | -0.039 | +595.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2720 | -0.039 | +595.19€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 4051 | -0.053 | +927.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4051 | -0.053 | +927.42€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 19334 | +0.076 | +9626.98€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 19334 | +0.076 | +9626.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3554 | +0.013 | +1933.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3554 | +0.013 | +1933.71€ | 2 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4092 | +0.002 | +739.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4092 | +0.002 | +739.25€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2730 | +0.256 | +2680.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2730 | +0.256 | +2680.59€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2981 | -0.023 | +307.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2981 | -0.023 | +307.96€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3217 | +0.013 | +1135.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3217 | +0.013 | +1135.10€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2760 | +0.266 | +2830.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2760 | +0.266 | +2830.36€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 14915 | +0.169 | +10795.08€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 14915 | +0.169 | +10795.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2183 | +0.210 | +1757.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2183 | +0.210 | +1757.89€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2342 | +0.157 | +1639.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2342 | +0.157 | +1639.10€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2300 | +0.203 | +1786.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2300 | +0.203 | +1786.42€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2467 | +0.141 | +1628.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2467 | +0.141 | +1628.32€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2827 | +0.112 | +1796.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2827 | +0.112 | +1796.75€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2796 | +0.201 | +2186.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2796 | +0.201 | +2186.61€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 3651 | +0.124 | +1458.35€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 3651 | +0.124 | +1458.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 119 | +0.112 | +45.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 119 | +0.112 | +45.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 999 | +0.117 | +402.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 999 | +0.117 | +402.51€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1020 | +0.155 | +480.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1020 | +0.155 | +480.50€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 723 | +0.074 | +174.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 723 | +0.074 | +174.13€ | 1 | 9 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 422 | +0.132 | +172.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 422 | +0.132 | +172.39€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 18325 | +0.173 | +13118.61€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 18325 | +0.173 | +13118.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 2854 | +0.222 | +2422.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 2854 | +0.222 | +2422.01€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2854 | +0.152 | +1860.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2854 | +0.152 | +1860.06€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 2956 | +0.220 | +2476.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 2956 | +0.220 | +2476.45€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 2912 | +0.135 | +1856.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 2912 | +0.135 | +1856.40€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3231 | +0.105 | +1788.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3231 | +0.105 | +1788.23€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3518 | +0.201 | +2715.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3518 | +0.201 | +2715.47€ | 0 | 26 |
| ✅ GBM_LATE_5M | 5492 | +0.139 | +2907.17€ | 1 | 26 |
| ✅ GBM_LATE_5M#5min | 5492 | +0.139 | +2907.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 475 | +0.177 | +315.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 475 | +0.177 | +315.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1540 | +0.141 | +925.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1540 | +0.141 | +925.60€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 764 | +0.170 | +481.20€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 764 | +0.170 | +481.20€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 1669 | +0.144 | +878.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1669 | +0.144 | +878.99€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 299 | +0.035 | +42.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 299 | +0.035 | +42.23€ | 1 | 4 |
| ✅ GBM_LATE_5M#XRP | 745 | +0.108 | +263.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 745 | +0.108 | +263.65€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1152 | +0.059 | +405.50€ | 3 | 17 |
| ✅ GBM_LATE_60M#60min | 1152 | +0.059 | +405.50€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 405 | +0.085 | +139.35€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 405 | +0.085 | +139.35€ | 0 | 17 |
| ✅ GBM_LATE_60M#ETH | 384 | +0.065 | +168.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 384 | +0.065 | +168.00€ | 2 | 17 |
| ✅ GBM_LATE_60M#SOL | 363 | +0.023 | +98.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 363 | +0.023 | +98.16€ | 3 | 11 |
| 🚫 GBM_LATE_60M_FADE | 281 | -0.281 | -33.67€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 281 | -0.281 | -33.67€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 107 | -0.225 | -8.22€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 107 | -0.225 | -8.22€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 93 | -0.332 | -19.04€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 93 | -0.332 | -19.04€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 81 | -0.283 | -6.40€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 81 | -0.283 | -6.40€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 536 | +0.050 | +83.19€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 536 | +0.050 | +83.19€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 200 | +0.040 | +21.78€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 200 | +0.040 | +21.78€ | 3 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 164 | +0.042 | +0.97€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 164 | +0.042 | +0.97€ | 3 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 172 | +0.069 | +60.44€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 172 | +0.069 | +60.44€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1247 | +0.096 | +325.83€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1247 | +0.096 | +325.83€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1247 | +0.096 | +325.83€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1247 | +0.096 | +325.83€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 335 | -0.090 | -35.93€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 335 | -0.090 | -35.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 79 | -0.093 | -8.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 79 | -0.093 | -8.25€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 109 | -0.022 | -3.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 109 | -0.022 | -3.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1468 | -0.003 | -6.61€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1468 | -0.003 | -6.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 163 | -0.021 | +0.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 163 | -0.021 | +0.58€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 101 | -0.053 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 101 | -0.053 | -6.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 573 | +0.030 | +19.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 573 | +0.030 | +19.70€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 459 | -0.008 | -8.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 459 | -0.008 | -8.73€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 97 | -0.066 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 97 | -0.066 | -6.47€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 850 | -0.046 | -25.08€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 850 | -0.046 | -25.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 249 | -0.054 | -14.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 249 | -0.054 | -14.56€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 271 | -0.031 | -3.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 271 | -0.031 | -3.01€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 330 | -0.051 | -7.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 330 | -0.051 | -7.51€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 12281 | -0.011 | -170.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 12281 | -0.011 | -170.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2146 | -0.023 | -46.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2146 | -0.023 | -46.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2559 | +0.008 | -17.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2559 | +0.008 | -17.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2373 | -0.017 | -18.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2373 | -0.017 | -18.23€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 2946 | -0.016 | -53.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 2946 | -0.016 | -53.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 20065 | -0.014 | +918.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 20065 | -0.014 | +918.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3463 | +0.009 | +477.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3463 | +0.009 | +477.15€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3245 | -0.025 | -19.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3245 | -0.025 | -19.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3491 | -0.000 | +286.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3491 | -0.000 | +286.04€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3081 | -0.044 | -67.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3081 | -0.044 | -67.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3366 | -0.017 | +145.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3366 | -0.017 | +145.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3419 | -0.008 | +96.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3419 | -0.008 | +96.06€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 4395 | -0.032 | -97.13€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 4395 | -0.032 | -97.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1023 | +0.002 | -13.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1023 | +0.002 | -13.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 852 | -0.040 | -26.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 852 | -0.040 | -26.56€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 41 | -0.128 | -5.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 41 | -0.128 | -5.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 395 | -0.110 | -10.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 395 | -0.110 | -10.37€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1238 | -0.038 | -15.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1238 | -0.038 | -15.87€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 846 | -0.015 | -25.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 846 | -0.015 | -25.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3186 | +0.004 | -3.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3186 | +0.004 | -3.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 185 | +0.008 | -2.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 185 | +0.008 | -2.27€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1163 | +0.008 | +8.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1163 | +0.008 | +8.30€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1387 | +0.007 | -0.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1387 | +0.007 | -0.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 52476 | -0.073 | +1014.03€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 52476 | -0.073 | +1014.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 8759 | -0.082 | +491.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 8759 | -0.082 | +491.26€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 8237 | -0.087 | -294.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 8237 | -0.087 | -294.26€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 8799 | -0.073 | +420.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 8799 | -0.073 | +420.24€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 7757 | -0.095 | -243.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 7757 | -0.095 | -243.08€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 9790 | -0.047 | +283.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 9790 | -0.047 | +283.85€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 9134 | -0.064 | +356.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 9134 | -0.064 | +356.02€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6641 | -0.020 | -116.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6641 | -0.020 | -116.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1465 | -0.021 | -18.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1465 | -0.021 | -18.79€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1462 | -0.012 | -7.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1462 | -0.012 | -7.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 979 | -0.034 | -15.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 979 | -0.034 | -15.47€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 927 | +0.109 | +308.16€ | 1 | 3 |
| ✅ ORDER_FLOW_5M#5min | 791 | +0.118 | +295.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 175 | +0.116 | +71.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 175 | +0.116 | +71.04€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 158 | +0.094 | +36.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 158 | +0.094 | +36.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 157 | +0.098 | +50.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 157 | +0.098 | +50.73€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 144 | +0.164 | +83.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 144 | +0.164 | +83.75€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#XRP | 157 | +0.116 | +53.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 157 | +0.116 | +53.88€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 443 | -0.093 | -13.26€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 197 | -0.133 | -34.03€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 155 | -0.175 | -36.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 158 | -0.081 | +3.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 116 | -0.093 | -2.72€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 88 | -0.022 | +16.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 68 | -0.043 | +10.84€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 339 | -0.122 | -28.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 496 | -0.219 | -37.63€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 210 | -0.203 | -32.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 178 | -0.194 | -30.17€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 175 | -0.240 | -19.74€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 148 | -0.253 | -23.82€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 111 | -0.208 | +14.56€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 97 | -0.207 | +11.50€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 423 | -0.220 | -42.48€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 170 | +0.395 | +124.43€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 23 | +0.020 | -2.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 23 | +0.020 | -2.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 39 | +0.329 | +35.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 39 | +0.329 | +35.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 108 | +0.491 | +91.33€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 108 | +0.491 | +91.33€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#sniper | 170 | +0.395 | +124.43€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 364 | +0.027 | +7.17€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 364 | +0.027 | +7.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 160 | +0.037 | +2.75€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 160 | +0.037 | +2.75€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 24 | +0.077 | +2.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 24 | +0.077 | +2.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 40 | -0.048 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 40 | -0.048 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 140 | +0.028 | +7.07€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 140 | +0.028 | +7.07€ | 1 | 2 |
| ✅ STREAK_FADE_5M | 2327 | -0.022 | -97.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2327 | -0.022 | -97.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 561 | -0.022 | -22.88€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 561 | -0.022 | -22.88€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 151 | -0.043 | -13.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 151 | -0.043 | -13.92€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 811 | -0.021 | -33.90€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 811 | -0.021 | -33.90€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 51 | -0.009 | -0.73€ | 1 | 0 |
| ✅ STREAK_FADE_60M#60min | 51 | -0.009 | -0.73€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 32 | -0.088 | -3.42€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 32 | -0.088 | -3.42€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 5949 | +0.025 | +98.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 5949 | +0.025 | +98.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1915 | +0.024 | +24.92€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1915 | +0.024 | +24.92€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1233 | +0.036 | +39.89€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1233 | +0.036 | +39.89€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1732 | +0.013 | +3.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1732 | +0.013 | +3.40€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1069 | +0.030 | +30.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1069 | +0.030 | +30.71€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 5665 | +0.011 | -36.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 5665 | +0.011 | -36.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2230 | +0.019 | -0.23€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2230 | +0.019 | -0.23€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2258 | +0.014 | -9.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2258 | +0.014 | -9.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1177 | -0.007 | -26.43€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1177 | -0.007 | -26.43€ | 2 | 0 |
| ✅ UPDOWN_GBM | 22604 | +0.028 | +1217.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 6152 | +0.054 | +940.86€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 855 | +0.003 | +7.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 14165 | +0.023 | +275.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1340 | -0.004 | -8.98€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 1932 | +0.078 | +205.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 268 | +0.130 | +87.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1645 | +0.071 | +119.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 4040 | +0.029 | +260.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 720 | +0.076 | +167.98€ | 1 | 13 |
| ✅ UPDOWN_GBM#BTC#240min | 245 | +0.026 | +7.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2453 | +0.024 | +82.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 587 | -0.001 | +1.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 35 | -0.122 | +1.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 2714 | +0.032 | +88.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 228 | +0.109 | +55.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2470 | +0.025 | +32.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 4468 | +0.015 | +173.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1676 | +0.039 | +166.13€ | 0 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 232 | +0.009 | +8.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2045 | +0.004 | +0.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 485 | -0.007 | -6.02€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 30 | -0.156 | +3.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6008 | +0.014 | +126.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1657 | +0.018 | +89.53€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 226 | -0.009 | -1.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 3832 | +0.016 | +44.29€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 268 | -0.004 | -4.41€ | 1 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 25 | -0.167 | -1.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3440 | +0.038 | +365.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1603 | +0.074 | +374.03€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 117 | -0.029 | -5.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1720 | +0.009 | -3.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 90 | -0.152 | +4.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 386 | +0.335 | +104.64€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 386 | +0.335 | +104.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 218 | +0.332 | +52.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 218 | +0.332 | +52.40€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 168 | +0.335 | +52.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 168 | +0.335 | +52.24€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 8428 | -0.053 | +1716.94€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 8428 | -0.053 | +1716.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 400 | -0.050 | +348.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 400 | -0.050 | +348.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1617 | -0.134 | -25.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1617 | -0.134 | -25.97€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 881 | +0.184 | +481.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 881 | +0.184 | +481.59€ | 2 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2722 | -0.065 | +421.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2722 | -0.065 | +421.11€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2669 | -0.079 | +437.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2669 | -0.079 | +437.22€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 86 | +0.057 | +7.70€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 86 | +0.057 | +7.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 86 | +0.057 | +7.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 86 | +0.057 | +7.70€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 658 | +0.288 | +535.40€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 658 | +0.288 | +535.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 367 | +0.281 | +282.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 367 | +0.281 | +282.79€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 291 | +0.295 | +252.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 291 | +0.295 | +252.61€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 681 | -0.109 | -80.55€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 681 | -0.109 | -80.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 179 | -0.069 | -12.34€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 179 | -0.069 | -12.34€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 66 | -0.176 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 66 | -0.176 | -10.12€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 58 | -0.200 | -8.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 58 | -0.200 | -8.54€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1805 | +0.301 | +905.28€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 600 | +0.241 | +90.71€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 633 | +0.289 | +243.37€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 572 | +0.375 | +571.19€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.058) — sin ventaja clara. oversold(IBS<0.3): IC=+0.044 n=7802 | neutral: IC=+0.027 n=8637 | overbought(IBS>0.7): IC=+0.085 n=8331
  - _Datos_: n=25683 IC=+0.052 PNL=+2985.06€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 419 celda(s) pasan gate riguroso completo de 1985 evaluadas (n>=40) y 2953 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.018 < 0.08 — monitorear
  - _Datos_: n=1657 IC=+0.018 PNL=+89.53€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=633/15 IC=+0.289 PNL=+243.37€ | BTC: n=600/15 IC=+0.241 PNL=+90.71€ | SOL: n=572/15 IC=+0.375 PNL=+571.19€

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
  - _Estado_: 22542 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.077 n=166/60 | contraria IC=+0.123 n=152 | gap=-0.046 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=221, boost estimado=+0.003. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 144 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=485/40 IC=-0.007 PNL=-6.02€ | BTC#60min: n=587/40 IC=-0.001 PNL=+1.45€ | SOL#60min: n=268/40 IC=-0.004 PNL=-4.41€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.055 n=241717 | tras_1loss IC=+0.069 n=189301 | tras_2loss IC=+0.036 n=81620/40 | gap=+0.019 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.011 n=2223 | contrario_BTC IC=+0.008 n=2032/40 | gap=-0.003 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.200 > 0.08 con n=181 PNL=+121.90€
  - _Datos_: n=181 IC=+0.200 PNL=+121.90€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.08 con n=243 PNL=+142.45€
  - _Datos_: n=243 IC=+0.186 PNL=+142.45€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.08 con n=31 PNL=+21.19€
  - _Datos_: n=31 IC=+0.227 PNL=+21.19€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.341 > 0.1 con n=1516 PNL=+899.96€
  - _Datos_: n=1516 IC=+0.341 PNL=+899.96€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=166 IC=+0.054 PNL=+18.35€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=166 IC=+0.054 PNL=+18.35€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=43 IC=+0.189 PNL=+28.53€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=43 IC=+0.189 PNL=+28.53€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=21444 IC=+0.027 PNL=+1119.78€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=21444 IC=+0.027 PNL=+1119.78€

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
  - _Estado_: 1/20 ops en el filtro definido (IC actual=+0.008 PNL=+1.96€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.96€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=994 IC=-0.001 PNL=-11.89€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=994 IC=-0.001 PNL=-11.89€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=346 IC=-0.011 PNL=+2.91€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=346 IC=-0.011 PNL=+2.91€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=333 IC=+0.025 PNL=+19.31€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=333 IC=+0.025 PNL=+19.31€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.170 > 0.1 con n=1326 PNL=+726.67€
  - _Datos_: n=1326 IC=+0.170 PNL=+726.67€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=850 IC=+0.049 PNL=+68.83€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=850 IC=+0.049 PNL=+68.83€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=720 IC=+0.076 PNL=+167.98€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=720 IC=+0.076 PNL=+167.98€

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
  - _Estado_: n=3534 IC=+0.053 PNL=+626.68€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3534 IC=+0.053 PNL=+626.68€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=94 IC=-0.198 PNL=+0.82€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=94 IC=-0.198 PNL=+0.82€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=167 IC=-0.009 PNL=+15.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=167 IC=-0.009 PNL=+15.94€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=333 IC=+0.019 PNL=+25.30€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=333 IC=+0.019 PNL=+25.30€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=21 IC=-0.022 PNL=-1.10€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=21 IC=-0.022 PNL=-1.10€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=2979 IC=-0.008 PNL=-26.07€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2979 IC=-0.008 PNL=-26.07€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.161 > 0.08 con n=60 PNL=+13.41€
  - _Datos_: n=60 IC=+0.161 PNL=+13.41€

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
  - _Estado_: n=4333 IC=+0.023 PNL=+208.89€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4333 IC=+0.023 PNL=+208.89€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=1478 IC=+0.042 PNL=+136.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1478 IC=+0.042 PNL=+136.83€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.114 > 0.08 con n=280 PNL=+86.26€
  - _Datos_: n=280 IC=+0.114 PNL=+86.26€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.144 > 0.08 con n=369 PNL=+75.98€
  - _Datos_: n=369 IC=+0.144 PNL=+75.98€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.129 > 0.08 con n=300 PNL=+156.96€
  - _Datos_: n=300 IC=+0.129 PNL=+156.96€

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
  - _Estado_: n=3177 IC=+0.032 PNL=+197.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3177 IC=+0.032 PNL=+197.01€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.02 con n=528 PNL=+197.60€
  - _Datos_: n=528 IC=+0.123 PNL=+197.60€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=140 IC=-0.056 PNL=+31.39€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=140 IC=-0.056 PNL=+31.39€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.451 > 0.1 con n=913 PNL=+902.84€
  - _Datos_: n=913 IC=+0.451 PNL=+902.84€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=7224 IC=+0.052 PNL=+839.15€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=7224 IC=+0.052 PNL=+839.15€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.1 con n=2087 PNL=+1049.31€
  - _Datos_: n=2087 IC=+0.189 PNL=+1049.31€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.143 < -0.1 con n=138 PNL=+14.97€
  - _Datos_: n=138 IC=-0.143 PNL=+14.97€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1222 IC=+0.044 PNL=+137.50€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1222 IC=+0.044 PNL=+137.50€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=50 IC=-0.096 PNL=+7.73€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=50 IC=-0.096 PNL=+7.73€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.1 con n=228 PNL=+66.55€
  - _Datos_: n=228 IC=+0.117 PNL=+66.55€

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
  - _Estado_: n=12539 IC=-0.141 PNL=+654.50€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12539 IC=-0.141 PNL=+654.50€

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
  - _Estado_: n=1383 IC=+0.138 PNL=+721.00€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1383 IC=+0.138 PNL=+721.00€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.173 > 0.08 con n=1287 PNL=+714.03€
  - _Datos_: n=1287 IC=+0.173 PNL=+714.03€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=2369 IC=+0.017 PNL=+63.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2369 IC=+0.017 PNL=+63.12€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.083 > 0.08 con n=1491 PNL=+791.04€
  - _Datos_: n=1491 IC=+0.083 PNL=+791.04€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.196 > 0.08 con n=334 PNL=+161.31€
  - _Datos_: n=334 IC=+0.196 PNL=+161.31€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.238 < -0.1 con n=1272 PNL=-175.45€
  - _Datos_: n=1272 IC=-0.238 PNL=-175.45€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=3533 IC=+0.145 PNL=+2110.69€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=3533 IC=+0.145 PNL=+2110.69€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.08 con n=66 PNL=+27.32€
  - _Datos_: n=66 IC=+0.118 PNL=+27.32€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=1430 IC=+0.045 PNL=+312.64€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1430 IC=+0.045 PNL=+312.64€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.08 con n=1290 PNL=+876.00€
  - _Datos_: n=1290 IC=+0.186 PNL=+876.00€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=2124 IC=-0.043 PNL=+480.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2124 IC=-0.043 PNL=+480.76€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=443 PNL=-39.76€
  - _Datos_: n=443 IC=+0.098 PNL=-39.76€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.230 > 0.08 con n=2617 PNL=-259.01€
  - _Datos_: n=2617 IC=+0.230 PNL=-259.01€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 25/40 ops en el filtro definido (IC actual=+0.056 PNL=+7.73€)
  - _Datos_: n=25 IC=+0.056 PNL=+7.73€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.085 n=656) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=656 IC=+0.085 PNL=+150.95€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.330 > 0.08 con n=174 PNL=+72.04€
  - _Datos_: n=174 IC=+0.330 PNL=+72.04€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.415 n=363) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=363 IC=+0.415 PNL=+507.69€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=6604 IC=+0.166 PNL=-880.27€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=6604 IC=+0.166 PNL=-880.27€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.1 con n=97 PNL=+59.53€
  - _Datos_: n=97 IC=+0.207 PNL=+59.53€
