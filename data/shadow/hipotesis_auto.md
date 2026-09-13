# Hipótesis automáticas — 2026-09-13 14:24 UTC
_Generado por shadow_postmortem.py sobre 420866 resoluciones (PNL=+44653.78€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.385` → IC=-0.150 (n=195)

  - _Acción_: SKIP cuando `py_entrada` < 0.385
  - _Potencial_: sin este filtro IC_bueno=+0.243 (n=399)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=400)

- **PATRÓN** `py_entrada` > `0.385` → IC=+0.243 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.385 (IC base=+0.114)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.206 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.114)

- **PATRÓN** `banda_hit_calibrado` > `0.8059` → IC=+0.266 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8059 (IC base=+0.114)

- **PATRÓN** `banda_z` > `10.736` → IC=+0.222 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.736 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.131 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 11.0 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=470)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.114)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=400)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.136 (n=130)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 98.0 (IC base=+0.039)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.375` → IC=-0.129 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=316)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=314)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.233 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.121)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.192 (n=232)

  - _Acción_: Kelly boost +0.96€ cuando `n_total_lado` > 58.0 (IC base=+0.121)

- **PATRÓN** `banda_hit_calibrado` > `0.8048` → IC=+0.262 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8048 (IC base=+0.121)

- **PATRÓN** `banda_z` > `11.557` → IC=+0.271 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.557 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=242)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=386)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.121)

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
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=81)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=91)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.136 (n=75)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=-0.014)

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
- **FILTRO** `restante_s_al_confirmar` < `146.19` → IC=-0.262 (n=5352)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.19
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=16058)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `n_ballenas` < `4.0` → IC=-0.128 (n=1860)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=1147)

- **FILTRO** `restante_s_al_confirmar` < `140.4` → IC=-0.283 (n=751)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 140.4
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=2256)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `133.42` → IC=-0.288 (n=679)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.42
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2039)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `144.37` → IC=-0.158 (n=1381)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.37
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4147)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `157.46` → IC=-0.255 (n=1234)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.46
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3702)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.16` → IC=-0.346 (n=1345)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.16
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=2732)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.31` → IC=-0.300 (n=43)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=160)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.135 (n=83)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=100)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.274 (n=29)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=89)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=26)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.695` → IC=+0.200 (n=10034)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.695 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=2710)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `10994.9669` → IC=+0.194 (n=866)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 10994.9669 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=8111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=9809)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.246 (n=7298)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.173 (n=5347)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4704.409` → IC=+0.174 (n=2307)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 4704.409 (IC base=+0.137)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.354 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=1560)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `13129.2094` → IC=+0.208 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13129.2094 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.208 (n=1150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.213 (n=1265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.270 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `12625.2295` → IC=+0.206 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12625.2295 (IC base=+0.204)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.178 (n=259)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.62 (IC base=+0.104)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=280)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `4690.1012` → IC=+0.152 (n=225)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4690.1012 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.164 (n=542)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.425 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=537)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3855.969` → IC=+0.160 (n=415)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3855.969 (IC base=+0.136)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=1864)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.328 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` < `0.305` → IC=+0.328 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.305 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.238 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `4371.3668` → IC=+0.244 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4371.3668 (IC base=+0.238)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.127 (n=529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.134 (n=457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 15.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.226 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.134 (n=601)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `1512.3969` → IC=+0.147 (n=451)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1512.3969 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=146)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.085)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.213 (n=489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.196 (n=1016)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 12.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.425 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.279 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.186 (n=1058)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.03 (IC base=+0.181)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.184 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.333 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `3435.4625` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3435.4625 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.140 (n=651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.225 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=316)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=104)

- **FILTRO** `py_entrada` > `0.8` → IC=-0.344 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=8412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=7161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.218 (n=3036)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `5363.4643` → IC=+0.345 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5363.4643 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.178 (n=2029)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.180 (n=2121)

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

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.364 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.328)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.328 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.328)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.365 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.328)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=1991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=1779)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=2020)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=1805)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=1875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.236)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.238 (n=1602)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.324 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.236)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=1745)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.192 (n=1062)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.7 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.446 (n=349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.450 (n=336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `9670.6919` → IC=+0.461 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9670.6919 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.436 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.442 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.458 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `11651.323` → IC=+0.460 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11651.323 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.449 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.460 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.442 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `3923.6329` → IC=+0.456 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3923.6329 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.422 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.433 (n=87)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.429 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.429 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` < `12.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `libro_liquidez` < `5005.2013` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 5005.2013
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=24851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.236 (n=9552)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=5101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.168 (n=4859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 17.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4547)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.165)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=4405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=4402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=1838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4547)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.167)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=2209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=1689)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.203 (n=4119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=4085)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.252 (n=2092)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=1791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.191 (n=3349)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.245 (n=1703)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.189)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=3770)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.125)

- **PATRÓN** `restante_min` < `4.05` → IC=+0.136 (n=3437)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.05 (IC base=+0.125)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.148 (n=3760)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.94 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.139 (n=5109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 8.0 (IC base=+0.125)

- **PATRÓN** `lag_apertura_s` < `3.4` → IC=+0.152 (n=3442)

  - _Acción_: Kelly boost +0.76€ cuando `lag_apertura_s` < 3.4 (IC base=+0.125)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=1892)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.131)

- **PATRÓN** `restante_min` < `3.99` → IC=+0.141 (n=1709)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` < 3.99 (IC base=+0.131)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.149 (n=1786)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.93 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.150 (n=2519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.131)

- **PATRÓN** `lag_apertura_s` < `4.31` → IC=+0.150 (n=1706)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 4.31 (IC base=+0.131)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=1878)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.47` → IC=+0.126 (n=2291)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.47 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.151 (n=1894)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=2299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.92` → IC=+0.149 (n=1734)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 2.92 (IC base=+0.119)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1637.5719` → IC=+0.297 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1637.5719 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.298 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.275)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.329 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `5124.6271` → IC=+0.295 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5124.6271 (IC base=+0.275)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.329 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.382 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1496.7246` → IC=+0.312 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1496.7246 (IC base=+0.291)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.437 (n=346)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.433 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.431 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `1890.5013` → IC=+0.437 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1890.5013 (IC base=+0.429)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.434 (n=165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.435 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.435 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.446 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.431 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `2133.31` → IC=+0.452 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2133.31 (IC base=+0.430)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.372)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.372)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.263)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.399 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.274 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `1382.8486` → IC=+0.288 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1382.8486 (IC base=+0.263)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.263)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.399 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.274 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `1382.8486` → IC=+0.288 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1382.8486 (IC base=+0.263)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9742` → IC=+0.229 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9742 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.2069` → IC=+0.244 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2069 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.83` → IC=+0.165 (n=2155)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.83 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6121` → IC=+0.254 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6121 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `1.0681` → IC=+0.242 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0681 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.0811` → IC=+0.191 (n=3261)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0811 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.11` → IC=+0.192 (n=1403)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.11 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `2.8592` → IC=+0.191 (n=3616)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.8592 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.472` → IC=+0.194 (n=3616)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.472 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.5745` → IC=+0.125 (n=6882)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.5745 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.1312` → IC=+0.163 (n=2065)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1312 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.161 (n=2144)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2035 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` > `0.8688` → IC=+0.164 (n=1429)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.8688 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.1694` → IC=+0.225 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1694 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.4641` → IC=+0.195 (n=3568)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4641 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.204 (n=3331)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.056)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.185 (n=420)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.187 (n=570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.007 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3242` → IC=+0.169 (n=1254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3242 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.191 (n=620)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 8.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.032` → IC=+0.283 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.032 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.193 (n=161)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.6362` → IC=+0.156 (n=1148)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.6362 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.162 (n=1148)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.182 (n=1337)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.06 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `63.0` → IC=+0.188 (n=904)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 63.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.238 (n=822)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.253 (n=835)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1923` → IC=+0.279 (n=623)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1923 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.252 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0621` → IC=+0.285 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0621 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.363` → IC=+0.249 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.363 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0688` → IC=+0.234 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0688 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2878` → IC=+0.290 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2878 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.7352` → IC=+0.264 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7352 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1576.58` → IC=+0.249 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1576.58 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.231 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.238)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.233 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.1116` → IC=+0.236 (n=418)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1116 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9251` → IC=+0.252 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9251 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.217 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.921` → IC=+0.229 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.921 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.2629` → IC=+0.223 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2629 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.8783` → IC=+0.214 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8783 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.212 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4924` → IC=+0.228 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4924 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.4076` → IC=+0.216 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4076 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `11865.8018` → IC=+0.228 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11865.8018 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.161 (n=894)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0048 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.166 (n=339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.160 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.5415` → IC=+0.178 (n=893)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5415 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.703` → IC=+0.170 (n=337)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 6.703 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.149 (n=1015)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2025 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1561` → IC=+0.200 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1561 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4183` → IC=+0.154 (n=906)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4183 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4138` → IC=+0.149 (n=906)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4138 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `12755.4107` → IC=+0.152 (n=676)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 12755.4107 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `219.0` → IC=+0.164 (n=275)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 219.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.191 (n=1225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0058 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=1229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.258 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.369` → IC=+0.229 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.369 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.186 (n=1027)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.3789` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.3789 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.664` → IC=+0.184 (n=1139)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.664 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.192 (n=1380)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.199 (n=330)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 16.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.221 (n=1055)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.1453` → IC=+0.215 (n=464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1453 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.232 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3902 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.704` → IC=+0.237 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.704 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.388` → IC=+0.213 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.388 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.271 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.8456` → IC=+0.202 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8456 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.3057` → IC=+0.218 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3057 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1892.3232` → IC=+0.229 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1892.3232 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.214 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.213)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=87)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1553)

- **PATRÓN** `ibs_20min` > `0.9296` → IC=+0.159 (n=262)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.9296 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` < `0.1735` → IC=+0.338 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1735 (IC base=+0.007)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.23` → IC=+0.128 (n=485)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 4.23 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.6001` → IC=+0.409 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6001 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.1897` → IC=+0.348 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1897 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `2.4241` → IC=+0.338 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4241 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.1031` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1031 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.340 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.187 (n=148)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1525 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.0344` → IC=+0.145 (n=415)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0344 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` > `0.6129` → IC=+0.136 (n=471)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6129 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2145` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2145 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.4999` → IC=+0.168 (n=377)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4999 (IC base=-0.007)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=220)

- **FILTRO** `ibs_20min` < `0.2424` → IC=-0.176 (n=66)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2424
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=200)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.126 (n=1596)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=800)

- **FILTRO** `sigma_ewma_delta_pct` > `8.602` → IC=-0.198 (n=263)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.602
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2133)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.202 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` > `1.1487` → IC=+0.380 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1487 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.338 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `3.0656` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.0656 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.1948` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1948 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` < `1.1373` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.1373 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.0872` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0872 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.7423` → IC=+0.242 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7423 (IC base=-0.048)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.246 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=-0.048)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.627` → IC=-0.191 (n=393)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.627
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=1181)

- **FILTRO** `ibs_20min` < `0.641` → IC=-0.159 (n=1038)

  - _Acción_: SKIP cuando `ibs_20min` < 0.641
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=536)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.193 (n=330)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=1244)

- **FILTRO** `ibs_20min` > `0.7761` → IC=-0.197 (n=596)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7761
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1792)

- **PATRÓN** `dist_vwap_pct` > `0.8711` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8711 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.292 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.089)

- **PATRÓN** `volumen_regimen` > `0.6107` → IC=+0.277 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6107 (IC base=-0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.289 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=-0.089)

- **PATRÓN** `volumen_spike_ratio` < `2.5191` → IC=+0.259 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5191 (IC base=-0.089)

- **PATRÓN** `volumen_spike_ratio` > `1.8262` → IC=+0.278 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8262 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` > `0.7074` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7074 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` < `0.242` → IC=+0.232 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.242 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` > `1.0828` → IC=+0.289 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0828 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1054` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1054 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.24` → IC=+0.245 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.24 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.4747` → IC=+0.226 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4747 (IC base=-0.030)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.227 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=-0.030)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.170 (n=2326)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0091 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.4552` → IC=+0.171 (n=6225)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4552 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.6984` → IC=+0.270 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6984 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.487` → IC=+0.138 (n=3301)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 3.487 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` > `0.6736` → IC=+0.228 (n=2095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6736 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` < `0.1147` → IC=+0.221 (n=3529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1147 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2498` → IC=+0.251 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2498 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.4809` → IC=+0.234 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4809 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` > `2.8039` → IC=+0.232 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8039 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.276 (n=3192)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.5615` → IC=+0.147 (n=6322)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5615 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.6628` → IC=+0.242 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6628 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` > `1.1988` → IC=+0.253 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1988 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.251` → IC=+0.323 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.251 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.62` → IC=+0.249 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.62 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` > `2.3762` → IC=+0.256 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3762 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.254 (n=2275)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.065)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3469` → IC=-0.123 (n=622)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3469
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=1265)

- **FILTRO** `sigma_ewma_delta_pct` > `4.322` → IC=-0.159 (n=364)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.322
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1203)

- **PATRÓN** `ibs_20min` > `0.8553` → IC=+0.253 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8553 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.0` → IC=+0.162 (n=495)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 5.0 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.294 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.8706` → IC=+0.193 (n=311)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.8706 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` > `2.6821` → IC=+0.190 (n=156)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6821 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.217 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.019)

- **PATRÓN** `volumen_spike_ratio` < `1.4617` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4617 (IC base=-0.019)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.463 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=-0.019)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8333` → IC=-0.149 (n=533)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8333
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=1600)

- **PATRÓN** `dist_vwap_pct` > `0.2959` → IC=+0.124 (n=219)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.2959 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `0.6566` → IC=+0.127 (n=534)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6566 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.4168` → IC=+0.156 (n=193)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4168 (IC base=+0.006)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.186 (n=189)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 235.0 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.1352` → IC=+0.224 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1352 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.341 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.7707` → IC=+0.226 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7707 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4386` → IC=+0.209 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4386 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `514.0` → IC=+0.210 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 514.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.268 (n=996)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0944` → IC=+0.247 (n=373)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0944 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.252 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.293 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.58` → IC=+0.278 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.58 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.1117` → IC=+0.258 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1117 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `1.6845` → IC=+0.243 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6845 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1910.8884` → IC=+0.243 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.8884 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.296 (n=882)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.315 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.287 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.885` → IC=+0.304 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.885 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.3459` → IC=+0.310 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3459 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `3.38` → IC=+0.273 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.38 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.228` → IC=+0.286 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.228 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.287 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `1882.9554` → IC=+0.297 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.9554 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.280 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.280)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2268` → IC=-0.205 (n=307)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2268
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=921)

- **FILTRO** `ibs_20min` > `0.8269` → IC=-0.177 (n=416)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8269
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1254)

- **PATRÓN** `ibs_20min` > `0.7971` → IC=+0.131 (n=418)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.7971 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.3041` → IC=+0.216 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3041 (IC base=-0.024)

- **PATRÓN** `volumen_regimen` < `0.9231` → IC=+0.196 (n=222)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.9231 (IC base=-0.024)

- **PATRÓN** `volumen_regimen` > `0.6044` → IC=+0.180 (n=226)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6044 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2693` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2693 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4982` → IC=+0.265 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4982 (IC base=-0.024)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.225 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 175.0 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1051 (IC base=-0.027)

- **PATRÓN** `volumen_regimen` < `1.0948` → IC=+0.151 (n=173)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0948 (IC base=-0.027)

- **PATRÓN** `volumen_regimen` > `0.6828` → IC=+0.140 (n=173)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6828 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.7656` → IC=+0.236 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7656 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` > `2.2356` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2356 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.216 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6667` → IC=-0.196 (n=758)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.245 (n=759)

- **FILTRO** `ibs_20min` > `0.7222` → IC=-0.235 (n=405)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7222
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1216)

- **FILTRO** `sigma_ewma_delta_pct` > `4.71` → IC=-0.162 (n=389)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.71
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1232)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.245 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1797` → IC=+0.307 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1797 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.8622` → IC=+0.276 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8622 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6344` → IC=+0.265 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6344 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` < `0.1058` → IC=+0.269 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1058 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4442` → IC=+0.317 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4442 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.311 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.025)

- **PATRÓN** `ibs_20min` < `0.2022` → IC=+0.167 (n=535)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.2022 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` > `0.5417` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.5417 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.241 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7144 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.186 (n=262)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2188` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2188 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.629` → IC=+0.201 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.629 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.5131` → IC=+0.179 (n=272)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.5131 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.212 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0145` → IC=+0.321 (n=651)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0145 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.276 (n=458)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` > `0.9` → IC=+0.332 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9 (IC base=+0.262)

- **PATRÓN** `dist_vwap_pct` > `0.1804` → IC=+0.307 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1804 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.341` → IC=+0.289 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.341 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.752` → IC=+0.262 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.752 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` > `0.8501` → IC=+0.287 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8501 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.1112` → IC=+0.266 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1112 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.297 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.5522` → IC=+0.274 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5522 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.267 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `2572.0774` → IC=+0.267 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2572.0774 (IC base=+0.262)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.278 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.292 (n=706)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.302 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3902 (IC base=+0.268)

- **PATRÓN** `dist_vwap_pct` > `0.5158` → IC=+0.291 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5158 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.415` → IC=+0.282 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.415 (IC base=+0.268)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.311 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.349 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `2.5387` → IC=+0.264 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5387 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.1688` → IC=+0.269 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1688 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `2549.3704` → IC=+0.280 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2549.3704 (IC base=+0.268)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.176 (n=1865)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0047 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.201 (n=1859)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.174 (n=4898)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=5823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6949` → IC=+0.229 (n=4973)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6949 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1604` → IC=+0.196 (n=2415)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1604 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.217` → IC=+0.250 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.217 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.162 (n=3722)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2177 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6215` → IC=+0.159 (n=3721)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6215 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1068` → IC=+0.186 (n=2170)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1068 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.3124` → IC=+0.168 (n=4638)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.3124 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.68` → IC=+0.164 (n=1758)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.68 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3822.4537` → IC=+0.173 (n=1856)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3822.4537 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.184 (n=4479)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 126.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.188 (n=3592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0063 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.205 (n=1797)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=2583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4552` → IC=+0.226 (n=5386)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4552 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.732` → IC=+0.190 (n=2241)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.732 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1874` → IC=+0.156 (n=3944)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1874 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.152 (n=3944)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6248 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.231 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.8815` → IC=+0.168 (n=3160)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.8815 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.641` → IC=+0.177 (n=1580)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.641 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.171 (n=4345)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 129.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.219 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.207 (n=424)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3176` → IC=+0.208 (n=932)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3176 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.220 (n=466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.044` → IC=+0.310 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.044 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.235 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.5798` → IC=+0.184 (n=841)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.5798 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `1.4401` → IC=+0.182 (n=840)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4401 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.246 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.247 (n=670)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1823` → IC=+0.297 (n=447)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1823 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.243 (n=674)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.1074` → IC=+0.266 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1074 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.936` → IC=+0.249 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.936 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.069` → IC=+0.233 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.069 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2343` → IC=+0.256 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2343 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8745` → IC=+0.251 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8745 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6455` → IC=+0.233 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6455 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1583.66` → IC=+0.250 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1583.66 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.235 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.244 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.359` → IC=+0.177 (n=802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.359 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4506` → IC=+0.221 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4506 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.2079` → IC=+0.213 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2079 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.697` → IC=+0.235 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.697 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.2719` → IC=+0.177 (n=802)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.2719 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.191 (n=173)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.4089` → IC=+0.203 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4089 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `11189.3992` → IC=+0.190 (n=717)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 11189.3992 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `412.0` → IC=+0.163 (n=638)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 412.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.180 (n=808)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0049 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.287` → IC=+0.171 (n=919)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.287 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.168 (n=848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.5135` → IC=+0.194 (n=919)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5135 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.118` → IC=+0.216 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.118 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.169 (n=919)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.204 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1586` → IC=+0.196 (n=278)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1586 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4386` → IC=+0.163 (n=810)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4386 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.4146` → IC=+0.155 (n=810)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4146 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.154 (n=244)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 235.0 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.200 (n=915)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1928` → IC=+0.198 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1928 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.219 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=426)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.541` → IC=+0.270 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.541 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.1074` → IC=+0.188 (n=745)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1074 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.6731` → IC=+0.184 (n=283)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.6731 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `3.6503` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 3.6503 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.205 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.235 (n=772)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.0885` → IC=+0.243 (n=259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0885 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.265 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.252 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.270 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3595` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3595 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.8345` → IC=+0.211 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8345 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.2644` → IC=+0.231 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2644 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1890.8984` → IC=+0.242 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1890.8984 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.206 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.221)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.186 (n=768)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0065 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.4222` → IC=+0.169 (n=873)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4222 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.168 (n=878)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.4158` → IC=+0.206 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4158 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1317` → IC=+0.189 (n=574)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1317 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.201` → IC=+0.242 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.201 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8656` → IC=+0.164 (n=582)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8656 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.2004` → IC=+0.183 (n=291)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.2004 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.236 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.178 (n=284)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.5331` → IC=+0.184 (n=283)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5331 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7528.5122` → IC=+0.192 (n=582)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7528.5122 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.165 (n=714)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 158.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.159 (n=829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.006 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.372` → IC=+0.148 (n=940)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.372 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.5954` → IC=+0.179 (n=940)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.5954 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.142 (n=945)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.147` → IC=+0.202 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.147 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8624` → IC=+0.141 (n=628)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8624 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `0.6135` → IC=+0.134 (n=940)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.6135 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2871` → IC=+0.193 (n=138)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2871 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.7867` → IC=+0.134 (n=552)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7867 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4566` → IC=+0.144 (n=276)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.4566 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `9896.1185` → IC=+0.150 (n=427)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 9896.1185 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `186.0` → IC=+0.122 (n=753)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 186.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.129 (n=1049)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` > 0.0054 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=1081)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5111` → IC=+0.196 (n=1049)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5111 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0166` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0166 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.371` → IC=+0.254 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.371 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.121 (n=1050)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2233 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.7951` → IC=+0.123 (n=672)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7951 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=1067)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2907.8423` → IC=+0.199 (n=476)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2907.8423 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.135 (n=752)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 49.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.153 (n=451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0058 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.140 (n=342)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.5294` → IC=+0.204 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5294 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.305` → IC=+0.150 (n=218)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 7.305 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `1.0503` → IC=+0.127 (n=902)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0503 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2729` → IC=+0.185 (n=122)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2729 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.5717` → IC=+0.126 (n=391)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.5717 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.1616` → IC=+0.143 (n=401)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1616 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `3085.1851` → IC=+0.157 (n=342)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3085.1851 (IC base=+0.115)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.208 (n=666)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.1642` → IC=+0.217 (n=440)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1642 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=1039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.250 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.72 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `1.2037` → IC=+0.240 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2037 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.294` → IC=+0.236 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.294 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `1.2022` → IC=+0.200 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2022 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `0.6862` → IC=+0.209 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6862 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.259 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.2072` → IC=+0.213 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2072 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.4285` → IC=+0.203 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4285 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.200 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.242 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0219` → IC=+0.204 (n=482)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0219 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.223 (n=355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.211 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=490)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.431` → IC=+0.237 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.431 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `1.1079` → IC=+0.208 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1079 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.713` → IC=+0.224 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.713 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.6258` → IC=+0.213 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6258 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.289 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2559` → IC=+0.194 (n=817)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2559 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4604` → IC=+0.188 (n=928)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4604 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2507.0024` → IC=+0.211 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2507.0024 (IC base=+0.200)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.148 (n=577)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0043 (IC base=+0.141)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.156 (n=434)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0085 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0941` → IC=+0.154 (n=434)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0941 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.164 (n=1216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` > `0.4087` → IC=+0.169 (n=1302)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.4087 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` > `0.784` → IC=+0.186 (n=170)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.784 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.699` → IC=+0.176 (n=587)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.699 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `0.8626` → IC=+0.162 (n=743)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8626 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1671` → IC=+0.166 (n=357)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1671 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `1.4377` → IC=+0.149 (n=414)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4377 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.8231` → IC=+0.155 (n=827)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.8231 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=1438)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `8223.8718` → IC=+0.174 (n=590)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 8223.8718 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.164 (n=367)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 20.0 (IC base=+0.141)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.146 (n=450)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0036 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.4899` → IC=+0.142 (n=1187)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.4899 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.824` → IC=+0.126 (n=535)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 3.824 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.1661` → IC=+0.147 (n=346)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1661 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.2286` → IC=+0.125 (n=1128)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.2286 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.136 (n=407)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 20.0 (IC base=+0.103)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.148 (n=194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0037 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1037` → IC=+0.172 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1037 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.164 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.9042` → IC=+0.194 (n=132)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.9042 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.2999` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2999 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.31` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.31 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.5894` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5894 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.0645` → IC=+0.129 (n=122)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.0645 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `2.2024` → IC=+0.136 (n=245)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.2024 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `1.5129` → IC=+0.134 (n=249)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.5129 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `9627.5275` → IC=+0.159 (n=291)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9627.5275 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 147.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.206 (n=195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.2739` → IC=+0.139 (n=389)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2739 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.3747` → IC=+0.187 (n=295)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.3747 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` > `0.7151` → IC=+0.134 (n=394)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.7151 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.1556` → IC=+0.204 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1556 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `2.4163` → IC=+0.138 (n=432)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.4163 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.157 (n=138)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 156.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.253 (n=176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.217 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.241 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.225 (n=416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.277` → IC=+0.246 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.277 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.367` → IC=+0.244 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.367 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.247 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.221 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8331 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.248 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1605 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.3686` → IC=+0.214 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3686 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.0232` → IC=+0.267 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0232 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `12476.0568` → IC=+0.233 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12476.0568 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.133 (n=224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0047 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.3259` → IC=+0.133 (n=224)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.3259 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.48` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.48 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.142 (n=79)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.084)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3477` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3477
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=318)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.237 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.143 (n=127)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `2928.3958` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2928.3958 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.4524` → IC=+0.155 (n=256)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.4524 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7183` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.7183 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `2.513` → IC=+0.123 (n=234)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.513 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.127 (n=199)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 44.0 (IC base=+0.074)

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
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.192 (n=3181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0085 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=7332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.4748` → IC=+0.212 (n=7001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4748 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.8904` → IC=+0.198 (n=917)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.8904 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.221 (n=3437)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8827` → IC=+0.163 (n=3160)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8827 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.17` → IC=+0.183 (n=1919)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.17 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.6497` → IC=+0.179 (n=2215)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6497 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.171 (n=8320)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.04 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3771.8767` → IC=+0.172 (n=2334)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3771.8767 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.193 (n=4953)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 97.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.197 (n=4285)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0067 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.4734` → IC=+0.184 (n=6424)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4734 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=2432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=2956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.237 (n=6426)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5588 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.775` → IC=+0.203 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.775 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.6238` → IC=+0.158 (n=1481)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6238 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.1986` → IC=+0.158 (n=1481)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1986 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.252 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.2962` → IC=+0.190 (n=2583)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.2962 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.177 (n=5303)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 130.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.220 (n=391)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.234 (n=531)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.814` → IC=+0.322 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.814 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2282` → IC=+0.232 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2282 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `1.5616` → IC=+0.197 (n=477)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5616 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.5899` → IC=+0.192 (n=361)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5899 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.215 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.229 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.266 (n=810)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.269 (n=921)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.2035` → IC=+0.287 (n=614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2035 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.259 (n=848)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.0662` → IC=+0.308 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0662 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.621` → IC=+0.269 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.621 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.226` → IC=+0.321 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.226 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `1.9089` → IC=+0.282 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9089 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1578.46` → IC=+0.269 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1578.46 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.259 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.187 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0027 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1824` → IC=+0.154 (n=738)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1824 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.6943` → IC=+0.243 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6943 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.124` → IC=+0.191 (n=609)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.124 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.887` → IC=+0.167 (n=259)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.887 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.396` → IC=+0.155 (n=981)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.396 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2802` → IC=+0.162 (n=1105)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2802 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.155` → IC=+0.179 (n=306)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.155 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.161 (n=1052)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.160 (n=701)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `10634.3743` → IC=+0.171 (n=987)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 10634.3743 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `498.0` → IC=+0.165 (n=982)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 498.0 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.194 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0024 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.3225` → IC=+0.172 (n=988)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3225 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.172 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.157 (n=659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 11.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.6443` → IC=+0.206 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6443 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.3` → IC=+0.177 (n=491)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 3.3 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.168 (n=988)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1856 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.1498` → IC=+0.224 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1498 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.4071` → IC=+0.170 (n=890)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.4071 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.169 (n=264)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 288.0 (IC base=+0.156)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.228 (n=1096)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.216 (n=1095)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=540)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.82` → IC=+0.295 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.82 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.2193` → IC=+0.222 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2193 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `1.6811` → IC=+0.222 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6811 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.238 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.243 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.232 (n=483)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1455` → IC=+0.228 (n=469)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1455 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.236 (n=505)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.268 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.278 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.3607` → IC=+0.291 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3607 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` < `1.7916` → IC=+0.219 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7916 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.2531` → IC=+0.228 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2531 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `1894.7532` → IC=+0.231 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1894.7532 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.221 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.229)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.170 (n=522)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0038 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.424` → IC=+0.139 (n=1183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.424 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=1240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.7101` → IC=+0.234 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7101 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.5499` → IC=+0.183 (n=323)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.5499 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.327` → IC=+0.171 (n=511)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 4.327 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.160 (n=789)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8812 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2746` → IC=+0.228 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2746 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.4628` → IC=+0.163 (n=378)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4628 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=1285)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `9007.4868` → IC=+0.231 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9007.4868 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `168.0` → IC=+0.144 (n=929)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 168.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.190 (n=317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0031 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.424` → IC=+0.152 (n=951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.424 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6885` → IC=+0.184 (n=951)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6885 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1977` → IC=+0.138 (n=887)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1977 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.14` → IC=+0.192 (n=141)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.14 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.8533` → IC=+0.140 (n=634)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8533 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.1715` → IC=+0.143 (n=317)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1715 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2758` → IC=+0.263 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2758 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.5573` → IC=+0.142 (n=389)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5573 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `2.1354` → IC=+0.160 (n=401)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.1354 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `11076.5036` → IC=+0.177 (n=317)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 11076.5036 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `198.0` → IC=+0.137 (n=873)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 198.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.176 (n=1219)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4615 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `1.0085` → IC=+0.174 (n=210)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 1.0085 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.403` → IC=+0.214 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.403 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=837)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2925.9204` → IC=+0.251 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2925.9204 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.175 (n=505)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0061 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1197` → IC=+0.147 (n=383)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1197 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.156 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.625` → IC=+0.208 (n=1150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.625 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.344` → IC=+0.126 (n=1101)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.344 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.153 (n=506)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7144 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2161` → IC=+0.182 (n=177)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2161 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.581` → IC=+0.144 (n=436)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.581 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.2078` → IC=+0.133 (n=450)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.2078 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2943.5324` → IC=+0.159 (n=382)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2943.5324 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.213 (n=559)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=1102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1751` → IC=+0.236 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1751 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.534` → IC=+0.237 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.534 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.243` → IC=+0.204 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.243 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.6191` → IC=+0.205 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6191 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.235 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.229 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.210 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2555.3558` → IC=+0.207 (n=821)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2555.3558 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.249 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0252` → IC=+0.223 (n=452)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0252 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.203 (n=1438)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.251 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.4811` → IC=+0.204 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4811 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.1806` → IC=+0.202 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1806 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.945` → IC=+0.262 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.945 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.238 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.260 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2259` → IC=+0.191 (n=1037)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2259 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.443` → IC=+0.197 (n=1178)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.443 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2528.1128` → IC=+0.205 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2528.1128 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.182 (n=1083)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 37.0 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=2350)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.146 (n=725)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0051 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.2729` → IC=+0.144 (n=1445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.2729 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.155 (n=745)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.137 (n=850)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 5.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` > `0.9291` → IC=+0.199 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9291 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1852` → IC=+0.126 (n=723)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.1852 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.152` → IC=+0.144 (n=346)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.152 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `0.8969` → IC=+0.130 (n=926)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.8969 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.1737` → IC=+0.157 (n=598)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1737 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.4536` → IC=+0.150 (n=715)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4536 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.8927` → IC=+0.147 (n=1430)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8927 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `8774.5433` → IC=+0.146 (n=983)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8774.5433 (IC base=+0.132)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.198 (n=594)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0036 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.476` → IC=+0.162 (n=1774)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.476 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1843` → IC=+0.156 (n=781)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1843 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6916` → IC=+0.155 (n=291)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6916 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.241` → IC=+0.148 (n=1753)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.241 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2455` → IC=+0.142 (n=1684)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2455 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0721` → IC=+0.154 (n=836)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0721 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.5706` → IC=+0.145 (n=1756)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.5706 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8194` → IC=+0.151 (n=1171)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.8194 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=2350)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `12053.6057` → IC=+0.157 (n=805)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 12053.6057 (IC base=+0.139)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.160 (n=245)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.160 (n=248)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0034 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0941` → IC=+0.184 (n=93)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0941 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.174 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 19.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.5194` → IC=+0.192 (n=186)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5194 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.2407` → IC=+0.156 (n=120)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.2407 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.996` → IC=+0.158 (n=352)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.996 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.231` → IC=+0.146 (n=278)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.231 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.8151` → IC=+0.179 (n=185)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.8151 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.1087` → IC=+0.149 (n=311)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.1087 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.229` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.229 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.4213` → IC=+0.205 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4213 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.6405` → IC=+0.174 (n=93)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6405 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `12660.8481` → IC=+0.188 (n=248)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 12660.8481 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.198 (n=366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0033 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.3661` → IC=+0.147 (n=831)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3661 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.168 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.1568` → IC=+0.163 (n=366)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1568 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.6044` → IC=+0.146 (n=377)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6044 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.607` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.607 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.225` → IC=+0.159 (n=810)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.225 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.176 (n=554)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8812 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0691` → IC=+0.159 (n=394)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0691 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.5675` → IC=+0.141 (n=828)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5675 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.8118` → IC=+0.146 (n=552)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8118 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `12053.6057` → IC=+0.146 (n=742)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 12053.6057 (IC base=+0.134)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.208 (n=207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.193 (n=213)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0104 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.2768` → IC=+0.167 (n=313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2768 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.9885` → IC=+0.223 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9885 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.335` → IC=+0.212 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.335 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.0931` → IC=+0.176 (n=202)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0931 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `3.5044` → IC=+0.168 (n=468)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 3.5044 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.8346` → IC=+0.167 (n=418)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8346 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.254)

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
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.147 (n=694)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0088 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.140 (n=695)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0045 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.4959` → IC=+0.145 (n=694)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4959 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.164 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.140 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 4.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.7971` → IC=+0.159 (n=315)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.7971 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.9851` → IC=+0.182 (n=152)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.9851 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.4203` → IC=+0.145 (n=651)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4203 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.796` → IC=+0.147 (n=692)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.796 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1119` → IC=+0.144 (n=611)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1119 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.6454` → IC=+0.137 (n=694)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6454 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1754` → IC=+0.156 (n=210)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1754 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.161 (n=228)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=641)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `8862.571` → IC=+0.154 (n=620)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8862.571 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.174 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0071 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.5081` → IC=+0.194 (n=554)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.5081 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.172 (n=379)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.1015` → IC=+0.167 (n=554)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.1015 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.168 (n=254)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.3663` → IC=+0.161 (n=565)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.3663 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.058` → IC=+0.169 (n=264)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.058 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6473` → IC=+0.184 (n=185)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6473 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.7334` → IC=+0.160 (n=495)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.7334 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.184 (n=242)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.169 (n=479)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.170 (n=544)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `8178.431` → IC=+0.169 (n=554)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 8178.431 (IC base=+0.155)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=129)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` > `0.6396` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6396 (IC base=+0.026)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0084` → IC=-0.250 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=262)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=267)

- **FILTRO** `dist_vwap_pct` > `0.1608` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1608
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=189)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.184 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.005 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.162 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6404` → IC=+0.203 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6404 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.151 (n=250)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.131` → IC=+0.205 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.131 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2899` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2899 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.5476` → IC=+0.141 (n=388)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.5476 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=396)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2468.387` → IC=+0.165 (n=213)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2468.387 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.0688` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0688 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.1608` → IC=+0.134 (n=189)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1608 (IC base=-0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.981` → IC=+0.162 (n=66)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.981 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4035` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.4035 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.376` → IC=+0.148 (n=126)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.376 (IC base=-0.031)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=134)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=-0.031)

- **PATRÓN** `libro_liquidez` > `2856.428` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2856.428 (IC base=-0.031)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.209 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.5781` → IC=+0.203 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5781 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.739` → IC=+0.131 (n=109)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.739 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `1.0552` → IC=+0.132 (n=150)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0552 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` < `0.0763` → IC=+0.150 (n=118)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0763 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `2.0198` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.0198 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2938.2254` → IC=+0.134 (n=140)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2938.2254 (IC base=+0.102)

- **PATRÓN** `drift_60min` |x|≤ `0.0401` → IC=+0.239 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0401 (IC base=+0.038)

- **PATRÓN** `ibs_20min` < `0.7` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.7 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.876` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.876 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.8132` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8132 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `2526.1581` → IC=+0.141 (n=62)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2526.1581 (IC base=+0.038)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6404` → IC=-0.161 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6404
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=173)

- **FILTRO** `sigma_h` > `0.0066` → IC=-0.321 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=79)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=70)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.186 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0029 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.132 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.6404` → IC=+0.226 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6404 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.1209` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1209 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.109` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.109 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `0.7864` → IC=+0.144 (n=116)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.7864 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` > `0.6191` → IC=+0.137 (n=155)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6191 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `1.7387` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7387 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` > `1.4015` → IC=+0.143 (n=124)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4015 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.148 (n=180)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `1348.1352` → IC=+0.202 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1348.1352 (IC base=+0.108)

- **PATRÓN** `drift_60min` |x|≤ `0.1021` → IC=+0.210 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1021 (IC base=-0.061)

- **PATRÓN** `ibs_20min` < `0.1926` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1926 (IC base=-0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.069` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 6.069 (IC base=-0.061)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.412` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.412 (IC base=-0.061)

- **PATRÓN** `volumen_pendiente_norm` > `0.0562` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0562 (IC base=-0.061)

- **PATRÓN** `volumen_spike_ratio` > `1.3921` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.3921 (IC base=-0.061)

- **PATRÓN** `libro_liquidez` > `1059.8551` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1059.8551 (IC base=-0.061)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0119` → IC=-0.281 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0119
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=76)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.275 (n=38)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.171 (n=80)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.127 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 14.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.193 (n=151)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.6757 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.8747` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.8747 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.5745` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.5745 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `385.351` → IC=+0.151 (n=130)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 385.351 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=-0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.25` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.25 (IC base=-0.081)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1621` → IC=-0.389 (n=34)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1621
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=106)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.419 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=107)

- **FILTRO** `dist_vwap_pct` > `0.2306` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2306
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=126)

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
- **FILTRO** `volumen_regimen` < `1.6316` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.6316
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `sigma_h` < `0.0018` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=37)

- **FILTRO** `ibs_20min` > `0.4197` → IC=-0.289 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4197
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

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
- **FILTRO** `ibs_20min` > `0.2413` → IC=-0.130 (n=90)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2413
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=176)

- **PATRÓN** `ibs_20min` > `0.6438` → IC=+0.143 (n=194)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6438 (IC base=+0.054)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.149 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.2413` → IC=+0.146 (n=176)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2413 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.944` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 5.944 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `3751.1947` → IC=+0.145 (n=91)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3751.1947 (IC base=+0.052)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=65)

- **FILTRO** `ibs_20min` < `0.4049` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4049
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=61)

- **FILTRO** `volumen_regimen` < `0.7924` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7924
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.138 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0028 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1524 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.217` → IC=+0.130 (n=90)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 14.217 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.0206` → IC=+0.145 (n=74)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.0206 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `3.503` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 3.503 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` > `1.6024` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.6024 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3644.5187` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3644.5187 (IC base=+0.114)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0033` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=+0.173 (n=47)

- **FILTRO** `ibs_20min` < `0.6645` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6645
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=53)

- **FILTRO** `ibs_20min` > `0.3559` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3559
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=68)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.173 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0033 (IC base=+0.056)

- **PATRÓN** `drift_60min` |x|≤ `0.1059` → IC=+0.184 (n=36)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1059 (IC base=+0.056)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.214 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.056)

- **PATRÓN** `ibs_20min` > `0.8265` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8265 (IC base=+0.056)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `1620.5728` → IC=+0.133 (n=47)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1620.5728 (IC base=+0.056)

- **PATRÓN** `ibs_20min` < `0.2114` → IC=+0.129 (n=60)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.2114 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.26` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.26 (IC base=+0.033)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.5556` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5556
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=49)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=43)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3593` → IC=+0.139 (n=81)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3593 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.125 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.7692` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7692 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.5856` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.5856 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.1848` → IC=+0.148 (n=69)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1848 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.132 (n=55)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.04 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `507.9911` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 507.9911 (IC base=+0.124)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2805.4316` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2805.4316 (IC base=+0.104)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2805.4316` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2805.4316 (IC base=+0.104)

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
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=181)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=167)

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

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1253)

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
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=510)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.425` → IC=-0.140 (n=145)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=458)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=218)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=218)

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
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=64)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=49)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=208)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=208)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=73)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=5754)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=987)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=1131)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.176 (n=2389)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=7180)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.167 (n=2466)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=7500)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.212 (n=384)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=1203)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.200 (n=401)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=1256)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.221 (n=414)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1325)

- **FILTRO** `ibs_20min` > `0.2875` → IC=-0.179 (n=434)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2875
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=1305)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.199 (n=386)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=1175)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.186 (n=431)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=1324)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2046)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=1970)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1976)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=200)

- **FILTRO** `ibs_20min` > `0.1507` → IC=-0.125 (n=94)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1507
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=189)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=175)

- **FILTRO** `py_entrada` > `0.635` → IC=-0.348 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.635
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=136)

- **FILTRO** `ibs_20min` > `0.9803` → IC=-0.217 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9803
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=136)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=539)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=6976)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=15838)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.275 (n=5614)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=17200)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.235 (n=5702)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=17112)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.162 (n=7685)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=15129)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.220 (n=7019)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=21351)

- **FILTRO** `ibs_7min` > `0.2969` → IC=-0.173 (n=7090)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2969
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=21280)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=837)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2746)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.257 (n=1181)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2402)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.203 (n=853)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=2730)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.145 (n=3326)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=1618)

- **FILTRO** `drift_7min_pct` |x|> `0.1354` → IC=-0.131 (n=1235)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1354
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=3709)

- **FILTRO** `ibs_7min` > `0.7992` → IC=-0.202 (n=1235)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7992
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3709)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.147 (n=917)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=3099)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.254 (n=997)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=3019)

- **FILTRO** `ibs_7min` < `0.7628` → IC=-0.184 (n=1004)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7628
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3012)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.171 (n=998)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3018)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.258 (n=929)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3103)

- **FILTRO** `ibs_7min` > `0.2497` → IC=-0.171 (n=1007)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2497
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3025)

- **FILTRO** `ballena_activa_n` > `113.0` → IC=-0.162 (n=1363)

  - _Acción_: SKIP cuando `ballena_activa_n` > 113.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=2669)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.180 (n=823)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=2568)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.323 (n=793)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=2598)

- **FILTRO** `ibs_7min` < `0.2083` → IC=-0.272 (n=847)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2083
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=2544)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.215 (n=776)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=2615)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.232 (n=1202)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=3976)

- **FILTRO** `ibs_7min` > `0.2661` → IC=-0.151 (n=1760)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2661
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=3418)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.170 (n=2483)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1282)

- **FILTRO** `ibs_7min` < `0.749` → IC=-0.191 (n=941)

  - _Acción_: SKIP cuando `ibs_7min` < 0.749
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=2824)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.185 (n=932)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=2833)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.258 (n=928)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2874)

- **FILTRO** `ibs_7min` > `0.2744` → IC=-0.172 (n=949)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2744
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2853)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.175 (n=944)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=2858)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.234 (n=1050)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3154)

- **FILTRO** `ibs_7min` < `0.7353` → IC=-0.201 (n=1051)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7353
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=3153)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.169 (n=1286)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=4076)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.282 (n=908)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2947)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.225 (n=962)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=2893)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.209 (n=886)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2969)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.195 (n=1202)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=3850)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=923)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=475)

- **FILTRO** `libro_liquidez` < `10498.4421` → IC=-0.157 (n=129)

  - _Acción_: SKIP cuando `libro_liquidez` < 10498.4421
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=389)

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
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=517)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3986` → IC=+0.137 (n=657)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3986 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.131 (n=527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `486.9033` → IC=+0.149 (n=212)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 486.9033 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=312)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.140 (n=265)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.196 (n=77)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.109)

- **PATRÓN** `total_vol_5m` < `495.741` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 495.741 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `7829.679` → IC=+0.141 (n=104)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7829.679 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 70.0 (IC base=+0.109)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.204 (n=106)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.199 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.164)

- **PATRÓN** `total_vol_5m` < `5917.212` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 5917.212 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3155.1686` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3155.1686 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 37.0 (IC base=+0.164)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.164 (n=105)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.136 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 13.0 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.180 (n=73)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 36.0 (IC base=+0.114)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.275` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.275
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=68)

- **FILTRO** `T_h` > `50.8821` → IC=-0.265 (n=168)

  - _Acción_: SKIP cuando `T_h` > 50.8821
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=84)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.207 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=-0.120)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.281 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.265 (n=32)

- **FILTRO** `T_h` > `56.3892` → IC=-0.402 (n=39)

  - _Acción_: SKIP cuando `T_h` > 56.3892
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=40)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.265 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.094)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0087` → IC=-0.152 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0087
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `T_h` < `291.9853` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `T_h` < 291.9853
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0057` → IC=-0.184 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.7615` → IC=-0.244 (n=88)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7615
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=171)

- **FILTRO** `T_h` > `144.6658` → IC=-0.363 (n=71)

  - _Acción_: SKIP cuando `T_h` > 144.6658
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=142)

- **FILTRO** `pct_vs_K` |x|> `4.555` → IC=-0.446 (n=53)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.555
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=160)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0036` → IC=-0.269 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=73)

- **FILTRO** `T_h` > `63.9918` → IC=-0.176 (n=72)

  - _Acción_: SKIP cuando `T_h` > 63.9918
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `T_h` > `144.5878` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `T_h` > 144.5878
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=51)

- **FILTRO** `pct_vs_K` |x|> `2.3742` → IC=-0.423 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.3742
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=39)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.260 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

- **FILTRO** `T_h` > `135.986` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 135.986
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=53)

- **FILTRO** `pct_vs_K` |x|> `4.5225` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.5225
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `sigma_h` > `0.0085` → IC=-0.300 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.385 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=50)

- **FILTRO** `T_h` > `71.0631` → IC=-0.325 (n=55)

  - _Acción_: SKIP cuando `T_h` > 71.0631
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `T_h` > `63.6677` → IC=-0.136 (n=42)

  - _Acción_: SKIP cuando `T_h` > 63.6677
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `sigma_h` > `0.0063` → IC=-0.357 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=10)

- **FILTRO** `T_h` > `95.1632` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### RESOLUTION_SNIPER
- **PATRÓN** `dist_50` > `0.4444` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4444 (IC base=+0.343)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.447 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.343)

- **PATRÓN** `edge` > `0.1072` → IC=+0.441 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.404)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.478 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.404)

- **PATRÓN** `T_h` > `0.7616` → IC=+0.441 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7616 (IC base=+0.404)

- **PATRÓN** `dist_50` > `0.3885` → IC=+0.485 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3885 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.440 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.404)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.2065` → IC=+0.470 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2065 (IC base=+0.487)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.477 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.487)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.477 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.487)

- **PATRÓN** `T_h` > `0.9332` → IC=+0.479 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9332 (IC base=+0.487)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.477 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.487)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.478 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.487)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=112)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=209)

- **FILTRO** `streak_estiramiento` > `0.7274` → IC=-0.127 (n=57)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.7274
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=111)

- **PATRÓN** `streak_estiramiento` < `0.4382` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.4382 (IC base=+0.019)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.034)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `991078.0` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `volumen_racha` > 991078.0
  - _Potencial_: sin este filtro IC_bueno=+0.180 (n=23)

- **FILTRO** `libro_liquidez` < `2208.5143` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 2208.5143
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=70)

- **PATRÓN** `volumen_racha` < `991078.0` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_racha` < 991078.0 (IC base=-0.011)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 45.0 (IC base=+0.047)

- **PATRÓN** `libro_liquidez` > `2208.5143` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2208.5143 (IC base=+0.047)

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
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=445)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=451)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=286)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=412)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=834)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=472)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=526)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2158)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1130)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1138)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.186 (n=326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0038 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.183 (n=326)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0087 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.171 (n=326)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.168)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0587` → IC=+0.172 (n=976)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.0587 (IC base=+0.168)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.225 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.168 (n=1020)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 4.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.189 (n=467)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.168)

- **PATRÓN** `ibs_15` > `0.619` → IC=+0.240 (n=976)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.619 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.1038` → IC=+0.173 (n=647)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1038 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.71` → IC=+0.243 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.71 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=864)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `2972.5116` → IC=+0.178 (n=651)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2972.5116 (IC base=+0.168)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=278)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.5859` → IC=-0.122 (n=125)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.5859
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=244)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.213 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0023` → IC=+0.194 (n=246)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0023 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.0624` → IC=+0.250 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0624 (IC base=+0.193)

- **PATRÓN** `drift_15min` |x|≤ `0.374` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.374 (IC base=+0.193)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2433` → IC=+0.214 (n=82)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2433 (IC base=+0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1124` → IC=+0.233 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1124 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.210 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=254)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_15` > `0.7746` → IC=+0.261 (n=220)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7746 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.099` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.099 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.624` → IC=+0.253 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.624 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `13580.5333` → IC=+0.254 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13580.5333 (IC base=+0.193)

### UPDOWN_GBM#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `20.331` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 20.331 (IC base=+0.001)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.154 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0061 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.151 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0055 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.160 (n=101)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.137)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.169 (n=152)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.137)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2725` → IC=+0.169 (n=140)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2725 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.138 (n=172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 11.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.151 (n=239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_15` > `0.6992` → IC=+0.262 (n=204)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6992 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.3919` → IC=+0.156 (n=242)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.3919 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.024` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.024 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=269)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.141 (n=104)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.137)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.1832` → IC=-0.190 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1832
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=29)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.167 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0047 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.172 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0076 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.1368` → IC=+0.172 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1368 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0657` → IC=+0.161 (n=122)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.0657 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3249` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3249 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.246 (n=136)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.2071` → IC=+0.159 (n=136)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2071 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.367` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.367 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `3092.4545` → IC=+0.250 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3092.4545 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.139)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.6204` → IC=-0.149 (n=112)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6204
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=497)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `8.191` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 8.191
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=22)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.892` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 12.892 (IC base=-0.017)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.223 (n=186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.087` → IC=+0.180 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.087 (IC base=+0.162)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0459` → IC=+0.176 (n=279)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.0459 (IC base=+0.162)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0926` → IC=+0.278 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0926 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.217 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_15` > `0.5075` → IC=+0.251 (n=279)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5075 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.1654` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1654 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` < `0.3009` → IC=+0.165 (n=261)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3009 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.796` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.796 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.247` → IC=+0.161 (n=252)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 7.247 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `2697.3044` → IC=+0.205 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2697.3044 (IC base=+0.162)

- **PATRÓN** `ibs_15` < `0.1034` → IC=+0.174 (n=296)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.87€ cuando `ibs_15` < 0.1034 (IC base=+0.044)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.397 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.338 (n=251)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0679` → IC=+0.336 (n=285)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0679 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.367 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.350 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.378 (n=285)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.362 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.963` → IC=+0.353 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.963 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3940.6708` → IC=+0.344 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3940.6708 (IC base=+0.333)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1228` → IC=+0.336 (n=71)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1228 (IC base=+0.330)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.357 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.330)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.333 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.330)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1017` → IC=+0.337 (n=145)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1017 (IC base=+0.330)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.330)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.359 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.330)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.330 (n=169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.330)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.366 (n=162)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.330)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.330)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.330)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.296` → IC=+0.343 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.296 (IC base=+0.330)

- **PATRÓN** `libro_liquidez` > `8959.7753` → IC=+0.354 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8959.7753 (IC base=+0.330)

- **PATRÓN** `ballena_activa_n` < `611.0` → IC=+0.396 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 611.0 (IC base=+0.330)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.381 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.360 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.332)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.349 (n=124)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.332)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2364` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2364 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.349 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.332)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.397 (n=124)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.332)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.342 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.433` → IC=+0.381 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.433 (IC base=+0.332)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.348 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `3566.5529` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3566.5529 (IC base=+0.332)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.343 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=+0.332)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.194 (n=498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=1497)

- **FILTRO** `ibs_15` < `0.5856` → IC=-0.184 (n=166)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5856
  - _Potencial_: sin este filtro IC_bueno=+0.246 (n=498)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=617)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1378)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.218 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=-0.056)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.246 (n=498)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` < `0.2628` → IC=+0.173 (n=392)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2628 (IC base=-0.056)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1194` → IC=+0.232 (n=646)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1194 (IC base=-0.051)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1833` → IC=+0.233 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1833 (IC base=-0.051)

- **PATRÓN** `ibs_15` < `0.3557` → IC=+0.271 (n=969)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3557 (IC base=-0.051)

- **PATRÓN** `dist_vwap_pct` > `0.628` → IC=+0.256 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.628 (IC base=-0.051)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.213 (n=294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=886)

- **FILTRO** `sigma_h` < `0.0031` → IC=-0.237 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0031
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=885)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.216 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=425)

- **FILTRO** `sigma_ewma_delta_pct` > `19.975` → IC=-0.243 (n=216)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.975
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=964)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.167 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.003 (IC base=+0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2339` → IC=+0.257 (n=35)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2339 (IC base=+0.068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1145` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1145 (IC base=+0.068)

- **PATRÓN** `ibs_15` > `0.7944` → IC=+0.351 (n=92)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7944 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.1422` → IC=+0.253 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1422 (IC base=+0.068)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6395` → IC=-0.244 (n=80)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6395
  - _Potencial_: sin este filtro IC_bueno=+0.254 (n=242)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=305)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.156 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0039 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.216 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.130)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0557` → IC=+0.131 (n=242)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.0557 (IC base=+0.130)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.228 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.144 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 5.0 (IC base=+0.130)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.254 (n=242)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.167 (n=175)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.838` → IC=+0.139 (n=258)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 18.838 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=305)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.225 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3466` → IC=+0.225 (n=354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3466 (IC base=+0.213)

- **PATRÓN** `drift_15min` |x|≤ `0.7445` → IC=+0.216 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7445 (IC base=+0.213)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1994` → IC=+0.234 (n=182)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1994 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.214 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.226 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.213)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.260 (n=402)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.729` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.729 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.252` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.252 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.957` → IC=+0.216 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.957 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `3672.3796` → IC=+0.215 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3672.3796 (IC base=+0.213)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.8298` → IC=-0.242 (n=122)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8298
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=369)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.210 (n=181)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=310)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0711` → IC=+0.204 (n=187)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0711 (IC base=-0.045)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.194` → IC=+0.184 (n=134)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.194 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.249 (n=209)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` < `0.1449` → IC=+0.197 (n=193)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.1449 (IC base=-0.045)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0188` → IC=-0.241 (n=295)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0188
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=297)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.239 (n=155)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=437)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.103` → IC=+0.368 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.103 (IC base=-0.051)

- **PATRÓN** `ibs_15` < `0.3273` → IC=+0.288 (n=277)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3273 (IC base=-0.051)

- **PATRÓN** `dist_vwap_pct` > `0.4309` → IC=+0.393 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4309 (IC base=-0.051)

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
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.293 (n=215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.286)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.295 (n=222)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.324 (n=163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2316` → IC=+0.317 (n=162)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2316 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1083` → IC=+0.320 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1083 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.302 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.330 (n=486)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2631` → IC=+0.321 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2631 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.306 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.286)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.290 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `12344.7964` → IC=+0.312 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12344.7964 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.295 (n=120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.285 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.0602` → IC=+0.317 (n=91)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0602 (IC base=+0.277)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2427` → IC=+0.328 (n=91)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2427 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3724` → IC=+0.290 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3724 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.330 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.8595` → IC=+0.311 (n=242)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8595 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.335 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.276` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.276 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `14264.9886` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14264.9886 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.302 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.303 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.325 (n=95)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1466` → IC=+0.315 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1466 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.333 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.317 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.344 (n=216)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.2764` → IC=+0.312 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2764 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.299 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.398` → IC=+0.324 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.398 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.309 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.300 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.305 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0857` → IC=-0.278 (n=61)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0857
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=187)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.244 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=164)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.161 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=321)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2171` → IC=-0.167 (n=64)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2171
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=65)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1771` → IC=-0.148 (n=69)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1771
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=69)

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

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1979` → IC=-0.382 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1979
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.214 (n=19)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.239 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `83.3501` → IC=+0.126 (n=172)

  - _Acción_: Kelly boost +0.63€ cuando `T_h` > 83.3501 (IC base=+0.121)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.326 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.121)

- **PATRÓN** `T_h` > `145.8875` → IC=+0.411 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8875 (IC base=+0.348)

- **PATRÓN** `ratio` > `1.012` → IC=+0.360 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.012 (IC base=+0.348)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9922` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.083)

- **PATRÓN** `T_h` > `111.89` → IC=+0.299 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.89 (IC base=+0.297)

- **PATRÓN** `ratio` > `1.0047` → IC=+0.350 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0047 (IC base=+0.297)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9922` → IC=+0.207 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9922 (IC base=+0.181)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.357 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.181)

- **PATRÓN** `T_h` > `87.9957` → IC=+0.345 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9957 (IC base=+0.326)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.326)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.406)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.619 sube el IC de +0.168 a +0.240 en UPDOWN_GBM#15min (n=976). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7746 sube el IC de +0.193 a +0.261 en UPDOWN_GBM#BTC#15min (n=220). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6992 sube el IC de +0.137 a +0.262 en UPDOWN_GBM#ETH#15min (n=204). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.139 a +0.246 en UPDOWN_GBM#SOL#15min (n=136). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5075 sube el IC de +0.162 a +0.251 en UPDOWN_GBM#XRP#15min (n=279). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1034 sube el IC de +0.044 a +0.174 en UPDOWN_GBM#XRP#15min (n=296). Ya aplicado como kelly_boost=+0.87€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.056 a +0.246 en UPDOWN_GBM_15M_TARDIO (n=498). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3557 sube el IC de -0.051 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=969). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7944 sube el IC de +0.068 a +0.351 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=92). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6395 sube el IC de +0.130 a +0.254 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=242). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3605 sube el IC de +0.213 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=402). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.145 a +0.333 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de -0.045 a +0.249 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=209). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3273 sube el IC de -0.051 a +0.288 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=277). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.286 a +0.330 en UPDOWN_GBM_IBS_ALTO (n=486). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8595 sube el IC de +0.277 a +0.311 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=242). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.296 a +0.344 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=216). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.333 a +0.378 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=285). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.330 a +0.366 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=162). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.332 a +0.397 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=124). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH#sniper` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1106 | +0.079 | +111.29€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1106 | +0.079 | +111.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 798 | +0.084 | +86.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 798 | +0.084 | +86.90€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 232 | +0.047 | +5.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 232 | +0.047 | +5.39€ | 4 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 50 | +0.173 | +20.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 50 | +0.173 | +20.49€ | 0 | 4 |
| ✅ BALLENAS_TARDIAS | 19066 | -0.108 | -2783.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1144 | -0.026 | -191.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 17922 | -0.114 | -2591.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3007 | -0.119 | -562.35€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3007 | -0.119 | -562.35€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1144 | -0.026 | -191.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1144 | -0.026 | -191.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5528 | -0.060 | -518.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5528 | -0.060 | -518.98€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 4936 | -0.110 | -384.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 4936 | -0.110 | -384.25€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4077 | -0.183 | -964.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4077 | -0.183 | -964.98€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 10322 | -0.048 | +4324.71€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 2823 | -0.009 | +1859.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 7499 | -0.063 | +2465.18€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 10322 | -0.048 | +4324.71€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 2823 | -0.009 | +1859.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 7499 | -0.063 | +2465.18€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 386 | -0.090 | -56.96€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 10 | +0.000 | -0.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 376 | -0.093 | -56.52€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 16 | -0.089 | -0.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 16 | -0.089 | -0.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 232 | -0.034 | -17.18€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 228 | -0.035 | -17.06€ | 1 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 105 | -0.192 | -33.90€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 6 | +0.000 | -0.33€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#ETH#5min | 99 | -0.203 | -33.57€ | 2 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#SOL | 15 | -0.199 | -9.93€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#SOL#5min | 15 | -0.199 | -9.93€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 18 | +0.000 | +4.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 18 | +0.000 | +4.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 68594 | +0.113 | -3700.53€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 10868 | +0.182 | -330.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 263 | -0.111 | -45.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 52596 | +0.100 | -3225.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 4867 | +0.117 | -98.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 8774 | +0.095 | -872.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 36 | -0.158 | -1.29€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 8723 | +0.097 | -859.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 13874 | +0.132 | -276.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3286 | +0.202 | -96.20€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 8717 | +0.109 | -177.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1829 | +0.118 | +20.10€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 8812 | +0.089 | -890.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 42 | -0.045 | -1.79€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 8755 | +0.090 | -877.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 14700 | +0.125 | -297.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4169 | +0.170 | -77.76€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 8777 | +0.109 | -167.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1742 | +0.100 | -43.17€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 13646 | +0.117 | -807.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3299 | +0.187 | -157.88€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 166 | -0.059 | +7.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 8885 | +0.091 | -582.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1296 | +0.136 | -75.55€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 8788 | +0.102 | -556.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 36 | -0.026 | +4.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 8739 | +0.103 | -561.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 10847 | +0.188 | -757.85€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 10847 | +0.188 | -757.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2694 | +0.168 | -290.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2694 | +0.168 | -290.06€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 447 | +0.175 | +15.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 447 | +0.175 | +15.60€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2653 | +0.177 | -247.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2653 | +0.177 | -247.94€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2381 | +0.236 | -69.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2381 | +0.236 | -69.63€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2593 | +0.189 | -179.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2593 | +0.189 | -179.57€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 506 | +0.443 | +0.33€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 506 | +0.443 | +0.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 198 | +0.440 | -0.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 198 | +0.440 | -0.29€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 192 | +0.443 | +1.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 192 | +0.443 | +1.70€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 110 | +0.429 | -1.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 110 | +0.429 | -1.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 36984 | +0.193 | -3223.53€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 36984 | +0.193 | -3223.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 6469 | +0.165 | -868.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 6469 | +0.165 | -868.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 5834 | +0.224 | -219.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 5834 | +0.224 | -219.86€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 6412 | +0.167 | -833.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 6412 | +0.167 | -833.89€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 5935 | +0.217 | -259.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 5935 | +0.217 | -259.11€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6115 | +0.199 | -444.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6115 | +0.199 | -444.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 6219 | +0.189 | -597.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 6219 | +0.189 | -597.07€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 13727 | +0.125 | +277.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 13727 | +0.125 | +277.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 6799 | +0.131 | +203.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 6799 | +0.131 | +203.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 6928 | +0.119 | +73.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 6928 | +0.119 | +73.91€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1175 | +0.288 | -20.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1175 | +0.288 | -20.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 519 | +0.275 | -15.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 519 | +0.275 | -15.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 559 | +0.291 | -3.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 559 | +0.291 | -3.80€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 97 | +0.328 | -1.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 97 | +0.328 | -1.32€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 518 | +0.429 | -8.87€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 518 | +0.429 | -8.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 241 | +0.430 | -3.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 241 | +0.430 | -3.62€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 240 | +0.430 | -4.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 240 | +0.430 | -4.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 37 | +0.372 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 37 | +0.372 | -0.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 768 | +0.064 | -47.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 268 | +0.056 | -23.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 500 | +0.068 | -23.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 48 | +0.100 | +0.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 48 | +0.100 | +0.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 600 | +0.073 | -22.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 100 | +0.098 | +0.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 500 | +0.068 | -23.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 120 | +0.000 | -25.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 120 | +0.000 | -25.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 23719 | +0.098 | -747.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2012 | +0.095 | +32.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 21707 | +0.098 | -780.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 13622 | +0.102 | -212.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2012 | +0.095 | +32.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 11610 | +0.104 | -245.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 3969 | +0.116 | +36.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 3969 | +0.116 | +36.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 6128 | +0.077 | -572.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 6128 | +0.077 | -572.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 685 | +0.263 | -77.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 685 | +0.263 | -77.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 685 | +0.263 | -77.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 685 | +0.263 | -77.86€ | 0 | 4 |
| ✅ GBM_LATE_15M | 17878 | +0.073 | +8008.00€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 17878 | +0.073 | +8008.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 2915 | +0.197 | +2154.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 2915 | +0.197 | +2154.46€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 2616 | +0.174 | +1759.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2616 | +0.174 | +1759.64€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 3038 | +0.194 | +2205.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3038 | +0.194 | +2205.74€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 2685 | -0.002 | +386.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2685 | -0.002 | +386.91€ | 1 | 14 |
| ✅ GBM_LATE_15M#SOL | 2662 | -0.038 | +593.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2662 | -0.038 | +593.42€ | 4 | 10 |
| ✅ GBM_LATE_15M#XRP | 3962 | -0.054 | +907.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 3962 | -0.054 | +907.83€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 18869 | +0.075 | +9435.61€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 18869 | +0.075 | +9435.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3454 | +0.012 | +1923.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3454 | +0.012 | +1923.86€ | 2 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4006 | +0.001 | +731.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4006 | +0.001 | +731.80€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2659 | +0.257 | +2621.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2659 | +0.257 | +2621.97€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2898 | -0.026 | +269.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2898 | -0.026 | +269.18€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3138 | +0.011 | +1108.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3138 | +0.011 | +1108.54€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2714 | +0.266 | +2780.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2714 | +0.266 | +2780.27€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 14601 | +0.169 | +10557.62€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 14601 | +0.169 | +10557.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2135 | +0.210 | +1719.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2135 | +0.210 | +1719.43€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2293 | +0.158 | +1616.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2293 | +0.158 | +1616.61€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2247 | +0.204 | +1750.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2247 | +0.204 | +1750.92€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2416 | +0.141 | +1589.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2416 | +0.141 | +1589.12€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2764 | +0.113 | +1757.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2764 | +0.113 | +1757.18€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2746 | +0.199 | +2124.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2746 | +0.199 | +2124.37€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 3532 | +0.122 | +1353.01€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 3532 | +0.122 | +1353.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 105 | +0.107 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 105 | +0.107 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 975 | +0.117 | +379.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 975 | +0.117 | +379.43€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 978 | +0.151 | +431.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 978 | +0.151 | +431.62€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 719 | +0.071 | +167.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 719 | +0.071 | +167.92€ | 1 | 8 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 387 | +0.130 | +151.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 387 | +0.130 | +151.73€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO | 17898 | +0.173 | +12830.48€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 17898 | +0.173 | +12830.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 2785 | +0.224 | +2378.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 2785 | +0.224 | +2378.59€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2789 | +0.152 | +1835.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2789 | +0.152 | +1835.20€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 2879 | +0.221 | +2418.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 2879 | +0.221 | +2418.06€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 2844 | +0.134 | +1804.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 2844 | +0.134 | +1804.98€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3153 | +0.105 | +1739.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3153 | +0.105 | +1739.43€ | 0 | 16 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3448 | +0.201 | +2654.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3448 | +0.201 | +2654.22€ | 0 | 27 |
| ✅ GBM_LATE_5M | 5254 | +0.135 | +2718.16€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5254 | +0.135 | +2718.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 475 | +0.177 | +315.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 475 | +0.177 | +315.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1477 | +0.136 | +860.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1477 | +0.136 | +860.45€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 684 | +0.168 | +424.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 684 | +0.168 | +424.40€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 1663 | +0.145 | +885.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1663 | +0.145 | +885.97€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 278 | +0.011 | +21.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 278 | +0.011 | +21.30€ | 2 | 2 |
| ✅ GBM_LATE_5M#XRP | 677 | +0.097 | +210.54€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 677 | +0.097 | +210.54€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1127 | +0.055 | +376.16€ | 3 | 17 |
| ✅ GBM_LATE_60M#60min | 1127 | +0.055 | +376.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 395 | +0.082 | +137.49€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 395 | +0.082 | +137.49€ | 0 | 17 |
| ✅ GBM_LATE_60M#ETH | 376 | +0.061 | +141.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 376 | +0.061 | +141.01€ | 3 | 19 |
| ✅ GBM_LATE_60M#SOL | 356 | +0.020 | +97.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 356 | +0.020 | +97.66€ | 2 | 10 |
| 🚫 GBM_LATE_60M_FADE | 279 | -0.283 | -37.41€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 279 | -0.283 | -37.41€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 106 | -0.222 | -7.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 106 | -0.222 | -7.71€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 92 | -0.340 | -23.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 92 | -0.340 | -23.29€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 81 | -0.283 | -6.40€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 81 | -0.283 | -6.40€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 524 | +0.053 | +86.34€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 524 | +0.053 | +86.34€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 193 | +0.049 | +24.68€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 193 | +0.049 | +24.68€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 160 | +0.043 | +1.94€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 160 | +0.043 | +1.94€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 171 | +0.067 | +59.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 171 | +0.067 | +59.73€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1201 | +0.098 | +318.55€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1201 | +0.098 | +318.55€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1201 | +0.098 | +318.55€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1201 | +0.098 | +318.55€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 334 | -0.092 | -36.68€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 334 | -0.092 | -36.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 78 | -0.100 | -9.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 78 | -0.100 | -9.01€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 109 | -0.022 | -3.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 109 | -0.022 | -3.88€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1451 | -0.005 | -10.07€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1451 | -0.005 | -10.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 163 | -0.021 | +0.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 163 | -0.021 | +0.58€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 101 | -0.053 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 101 | -0.053 | -6.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 557 | +0.024 | +15.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 557 | +0.024 | +15.74€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 458 | -0.006 | -8.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 458 | -0.006 | -8.22€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 97 | -0.066 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 97 | -0.066 | -6.47€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 836 | -0.042 | -21.14€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 836 | -0.042 | -21.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 246 | -0.057 | -15.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 246 | -0.057 | -15.11€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 264 | -0.023 | -0.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 264 | -0.023 | -0.56€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 326 | -0.046 | -5.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 326 | -0.046 | -5.47€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 12054 | -0.011 | -171.92€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 12054 | -0.011 | -171.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2084 | -0.022 | -42.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2084 | -0.022 | -42.43€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2559 | +0.008 | -17.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2559 | +0.008 | -17.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2251 | -0.018 | -18.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2251 | -0.018 | -18.06€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 2903 | -0.016 | -59.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 2903 | -0.016 | -59.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 19535 | -0.014 | +919.90€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 19535 | -0.014 | +919.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3360 | +0.008 | +475.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3360 | +0.008 | +475.92€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3173 | -0.026 | -15.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3173 | -0.026 | -15.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3396 | -0.001 | +280.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3396 | -0.001 | +280.03€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3011 | -0.045 | -64.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3011 | -0.045 | -64.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3279 | -0.017 | +149.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3279 | -0.017 | +149.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3316 | -0.009 | +94.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3316 | -0.009 | +94.31€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 4117 | -0.031 | -97.00€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 4117 | -0.031 | -97.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 914 | +0.000 | -15.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 914 | +0.000 | -15.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 760 | -0.037 | -20.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 760 | -0.037 | -20.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 41 | -0.128 | -5.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 41 | -0.128 | -5.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 374 | -0.117 | -12.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 374 | -0.117 | -12.56€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1182 | -0.033 | -18.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1182 | -0.033 | -18.18€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 51184 | -0.073 | +1063.13€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 51184 | -0.073 | +1063.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 8527 | -0.081 | +493.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 8527 | -0.081 | +493.19€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 8048 | -0.087 | -284.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 8048 | -0.087 | -284.37€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 8569 | -0.072 | +425.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 8569 | -0.072 | +425.03€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 7567 | -0.096 | -242.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 7567 | -0.096 | -242.18€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 9566 | -0.046 | +310.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 9566 | -0.046 | +310.42€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 8907 | -0.063 | +361.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 8907 | -0.063 | +361.03€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6625 | -0.020 | -119.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6625 | -0.020 | -119.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1456 | -0.021 | -19.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1456 | -0.021 | -19.30€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1457 | -0.011 | -9.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1457 | -0.011 | -9.08€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 977 | -0.035 | -16.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 977 | -0.035 | -16.77€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 913 | +0.111 | +307.83€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 777 | +0.120 | +295.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 174 | +0.119 | +72.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 174 | +0.119 | +72.95€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 152 | +0.091 | +32.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 152 | +0.091 | +32.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 154 | +0.109 | +56.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 154 | +0.109 | +56.62€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 141 | +0.164 | +80.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 141 | +0.164 | +80.80€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#XRP | 156 | +0.114 | +51.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 156 | +0.114 | +51.92€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 421 | -0.098 | -14.07€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 185 | -0.147 | -36.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 151 | -0.186 | -37.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 34 | +0.028 | +0.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 151 | -0.088 | +3.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 113 | -0.100 | -2.79€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 38 | -0.050 | +6.62€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 85 | -0.006 | +18.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 66 | -0.029 | +11.86€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 19 | +0.068 | +6.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 330 | -0.127 | -28.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 91 | +0.005 | +14.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 472 | -0.219 | -34.47€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 199 | -0.202 | -29.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 173 | -0.191 | -26.93€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 26 | -0.250 | -2.30€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 166 | -0.244 | -20.73€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 143 | -0.252 | -24.60€ | 6 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 23 | -0.180 | +3.88€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 107 | -0.206 | +15.48€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 93 | -0.205 | +12.42€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 409 | -0.218 | -39.11€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 63 | -0.223 | +4.64€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 161 | +0.390 | +110.48€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#BTC | 21 | -0.022 | -5.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 21 | -0.022 | -5.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 37 | +0.321 | +34.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 37 | +0.321 | +34.38€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 103 | +0.490 | +81.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 103 | +0.490 | +81.46€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#sniper | 161 | +0.390 | +110.48€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 359 | +0.029 | +7.85€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 359 | +0.029 | +7.85€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 157 | +0.041 | +3.38€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 157 | +0.041 | +3.38€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 24 | +0.077 | +2.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 24 | +0.077 | +2.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 40 | -0.048 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 40 | -0.048 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 138 | +0.029 | +7.12€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 138 | +0.029 | +7.12€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2305 | -0.022 | -96.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2305 | -0.022 | -96.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 560 | -0.023 | -23.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 560 | -0.023 | -23.43€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 150 | -0.040 | -13.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 150 | -0.040 | -13.41€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 791 | -0.021 | -32.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 791 | -0.021 | -32.63€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 48 | +0.020 | +0.80€ | 1 | 0 |
| ✅ STREAK_FADE_60M#60min | 48 | +0.020 | +0.80€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 29 | -0.048 | -1.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 29 | -0.048 | -1.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 5810 | +0.023 | +86.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 5810 | +0.023 | +86.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1882 | +0.024 | +23.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1882 | +0.024 | +23.75€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1195 | +0.034 | +36.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1195 | +0.034 | +36.14€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1693 | +0.011 | -0.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1693 | +0.011 | -0.71€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1040 | +0.028 | +27.52€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1040 | +0.028 | +27.52€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 5546 | +0.013 | -23.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 5546 | +0.013 | -23.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2177 | +0.022 | +7.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2177 | +0.022 | +7.21€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2207 | +0.016 | -4.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2207 | +0.016 | -4.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1162 | -0.008 | -26.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1162 | -0.008 | -26.70€ | 2 | 0 |
| ✅ UPDOWN_GBM | 21752 | +0.028 | +1156.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 5987 | +0.054 | +913.13€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 824 | +0.004 | +8.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 13572 | +0.022 | +249.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1281 | -0.008 | -18.45€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 1823 | +0.078 | +194.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 267 | +0.128 | +86.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1537 | +0.070 | +108.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 3859 | +0.028 | +243.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 696 | +0.080 | +161.24€ | 1 | 13 |
| ✅ UPDOWN_GBM#BTC#240min | 237 | +0.027 | +7.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2332 | +0.023 | +75.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 561 | -0.003 | -2.57€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 33 | -0.129 | +1.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 2585 | +0.032 | +85.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 228 | +0.109 | +55.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2341 | +0.025 | +29.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 4386 | +0.015 | +162.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1634 | +0.040 | +160.16€ | 0 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 224 | +0.009 | +8.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2032 | +0.004 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 467 | -0.014 | -8.74€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 29 | -0.145 | +4.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 5777 | +0.014 | +126.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1612 | +0.020 | +92.94€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 219 | -0.007 | -1.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 3669 | +0.016 | +43.11€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 253 | -0.010 | -7.14€ | 1 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 24 | -0.154 | -0.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3320 | +0.037 | +345.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1550 | +0.073 | +356.38€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 109 | -0.032 | -4.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1661 | +0.007 | -5.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 86 | -0.148 | +5.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 380 | +0.333 | +100.16€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 380 | +0.333 | +100.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 215 | +0.330 | +50.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 215 | +0.330 | +50.87€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 165 | +0.332 | +49.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 165 | +0.332 | +49.30€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 8238 | -0.052 | +1716.96€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 8238 | -0.052 | +1716.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 397 | -0.049 | +350.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 397 | -0.049 | +350.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1583 | -0.133 | -15.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1583 | -0.133 | -15.66€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 857 | +0.182 | +469.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 857 | +0.182 | +469.99€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2663 | -0.064 | +419.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2663 | -0.064 | +419.09€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2599 | -0.078 | +438.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2599 | -0.078 | +438.46€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 86 | +0.057 | +7.70€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 86 | +0.057 | +7.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 86 | +0.057 | +7.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 86 | +0.057 | +7.70€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 648 | +0.286 | +520.89€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 648 | +0.286 | +520.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 361 | +0.277 | +270.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 361 | +0.277 | +270.97€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 287 | +0.296 | +249.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 287 | +0.296 | +249.91€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 676 | -0.108 | -79.03€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 676 | -0.108 | -79.03€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 176 | -0.067 | -11.84€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 176 | -0.067 | -11.84€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 65 | -0.172 | -9.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 65 | -0.172 | -9.61€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 57 | -0.195 | -8.03€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 57 | -0.195 | -8.03€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1737 | +0.300 | +866.50€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 573 | +0.237 | +76.19€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 601 | +0.289 | +231.63€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 563 | +0.374 | +558.68€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.034 n=318 — no justifica filtro, seguir monitorizando
  - _Datos_: n=318 IC=+0.034 PNL=+22.09€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 415 celda(s) pasan gate riguroso completo de 1975 evaluadas (n>=40) y 2935 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.020 < 0.08 — monitorear
  - _Datos_: n=1612 IC=+0.020 PNL=+92.94€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=601/15 IC=+0.289 PNL=+231.63€ | BTC: n=573/15 IC=+0.237 PNL=+76.19€ | SOL: n=563/15 IC=+0.374 PNL=+558.68€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 29 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: 40
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Solo 0 ops con ibs_15 (feature añadida 2026-06-27). Esperar n≥40.

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: 20
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: Solo 0 ops GBM con hora_utc en features. Esperar n≥20 para patrones.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.070 n=156/60 | contraria IC=+0.140 n=145 | gap=-0.070 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=215, boost estimado=+0.006. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=467/40 IC=-0.014 PNL=-8.74€ | BTC#60min: n=561/40 IC=-0.003 PNL=-2.57€ | SOL#60min: n=253/40 IC=-0.010 PNL=-7.14€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.055 n=235676 | tras_1loss IC=+0.068 n=184780 | tras_2loss IC=+0.036 n=79814/40 | gap=+0.019 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.000 n=0 | contrario_BTC IC=+0.000 n=0/40 | gap=+0.000 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.08 con n=180 PNL=+119.73€
  - _Datos_: n=180 IC=+0.198 PNL=+119.73€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.08 con n=237 PNL=+135.23€
  - _Datos_: n=237 IC=+0.182 PNL=+135.23€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.341 > 0.1 con n=1459 PNL=+861.32€
  - _Datos_: n=1459 IC=+0.341 PNL=+861.32€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=153 IC=+0.055 PNL=+17.52€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=153 IC=+0.055 PNL=+17.52€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=41 IC=+0.198 PNL=+28.61€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=41 IC=+0.198 PNL=+28.61€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=949 IC=-0.007 PNL=-17.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=949 IC=-0.007 PNL=-17.59€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=332 IC=-0.012 PNL=-0.86€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=332 IC=-0.012 PNL=-0.86€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=318 IC=+0.034 PNL=+22.09€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=318 IC=+0.034 PNL=+22.09€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.168 > 0.1 con n=1301 PNL=+694.98€
  - _Datos_: n=1301 IC=+0.168 PNL=+694.98€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=695 IC=+0.081 PNL=+161.75€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=695 IC=+0.081 PNL=+161.75€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**⏳ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: 40
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: 20
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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

**⏳ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: 40
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: 30
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.227 n=53) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=53 IC=+0.227 PNL=+25.89€

**⏳ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: 40
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: 40
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: 40
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: 40
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: 200
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: 100
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: 40
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=517 PNL=+194.96€
  - _Datos_: n=517 IC=+0.124 PNL=+194.96€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=131 IC=-0.049 PNL=+33.33€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=131 IC=-0.049 PNL=+33.33€

**⏳ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: 25
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: 0/25 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=6843 IC=+0.050 PNL=+785.29€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=6843 IC=+0.050 PNL=+785.29€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.126 < -0.1 con n=129 PNL=+17.86€
  - _Datos_: n=129 IC=-0.126 PNL=+17.86€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1179 IC=+0.044 PNL=+135.49€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1179 IC=+0.044 PNL=+135.49€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.1 con n=221 PNL=+63.89€
  - _Datos_: n=221 IC=+0.119 PNL=+63.89€

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
  - _Estado_: n=12235 IC=-0.142 PNL=+582.33€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12235 IC=-0.142 PNL=+582.33€

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
  - _Estado_: n=1352 IC=+0.139 PNL=+726.43€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1352 IC=+0.139 PNL=+726.43€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=2250 IC=+0.018 PNL=+57.31€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2250 IC=+0.018 PNL=+57.31€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=1431 PNL=+774.42€
  - _Datos_: n=1431 IC=+0.084 PNL=+774.42€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.238 < -0.1 con n=1244 PNL=-172.02€
  - _Datos_: n=1244 IC=-0.238 PNL=-172.02€

**⏳ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: 100
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: 0/100 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: 40
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: 40
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.092 n=623) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=623 IC=+0.092 PNL=+154.97€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.416 n=355) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=355 IC=+0.416 PNL=+496.74€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=6466 IC=+0.165 PNL=-869.87€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=6466 IC=+0.165 PNL=-869.87€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.1 con n=93 PNL=+59.67€
  - _Datos_: n=93 IC=+0.216 PNL=+59.67€
