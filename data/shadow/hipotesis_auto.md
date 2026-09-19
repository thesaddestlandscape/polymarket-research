# Hipótesis automáticas — 2026-09-19 05:36 UTC
_Generado por shadow_postmortem.py sobre 507450 resoluciones (PNL=+55274.98€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.152 (n=202)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=450)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=431)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.250 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `77.0` → IC=+0.215 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 77.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8033` → IC=+0.259 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8033 (IC base=+0.125)

- **PATRÓN** `banda_z` > `10.168` → IC=+0.227 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.168 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.141 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 11.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=520)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2833.2535` → IC=+0.137 (n=326)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2833.2535 (IC base=+0.125)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=349)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=304)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=329)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.258 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.134)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.223 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.134)

- **PATRÓN** `banda_hit_calibrado` > `0.7991` → IC=+0.275 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7991 (IC base=+0.134)

- **PATRÓN** `banda_z` > `11.336` → IC=+0.238 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.336 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.155 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=435)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `88.0` → IC=+0.136 (n=75)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 88.0 (IC base=+0.028)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=87)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=87)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=86)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=97)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.253 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.103)

- **PATRÓN** `banda_hit_calibrado` > `0.6284` → IC=+0.230 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6284 (IC base=+0.103)

- **PATRÓN** `banda_z` > `6.043` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `banda_z` > 6.043 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `1185.8848` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1185.8848 (IC base=+0.103)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.154)

- **PATRÓN** `banda_z` > `3.13` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 3.13 (IC base=+0.154)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.705` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `ballenas_wallet_edge_medio` > 0.705 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2518.5859` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2518.5859 (IC base=+0.154)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `144.49` → IC=-0.243 (n=6213)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.49
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=18643)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `141.1` → IC=-0.251 (n=854)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.1
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2564)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `132.9` → IC=-0.280 (n=760)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.9
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=2282)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `158.92` → IC=-0.235 (n=1467)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.92
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=4402)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `120.59` → IC=-0.367 (n=1210)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 120.59
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=3632)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.243 (n=309)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=354)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.158 (n=191)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=433)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.260 (n=156)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=169)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.180 (n=73)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=222)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.250 (n=98)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.151 (n=61)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=121)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.174 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=141)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.199 (n=12453)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3120)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `5408.9119` → IC=+0.173 (n=1986)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5408.9119 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=9863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=11862)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.237 (n=9442)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=5130)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `1657.3138` → IC=+0.161 (n=5779)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1657.3138 (IC base=+0.132)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.206 (n=1470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `15582.9488` → IC=+0.233 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15582.9488 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=1337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.205 (n=1478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=1894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `13674.9234` → IC=+0.211 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13674.9234 (IC base=+0.200)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.178 (n=290)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.62 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `4628.5254` → IC=+0.150 (n=232)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4628.5254 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.161 (n=311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.150 (n=764)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.44 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=551)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `5871.1399` → IC=+0.167 (n=217)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5871.1399 (IC base=+0.124)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=2493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.142 (n=2133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.339 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.247 (n=1133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.240)

- **PATRÓN** `py_entrada` < `0.305` → IC=+0.328 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.305 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.247 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `3179.2134` → IC=+0.241 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3179.2134 (IC base=+0.240)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.134 (n=405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 11.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.140 (n=582)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.227 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=486)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `1297.6972` → IC=+0.144 (n=580)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 1297.6972 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.162 (n=149)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4420.281 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.430 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=1000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.266 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.173 (n=1160)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.03 (IC base=+0.171)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.168 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 13.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.360 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=183)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `1309.2371` → IC=+0.164 (n=218)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 1309.2371 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=279)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.218 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=339)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.113)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=9886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=9504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.225 (n=3443)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.341 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.175 (n=2339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.178 (n=2448)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.168)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.296 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.272 (n=244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.270)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.341 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.270)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=2398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2297)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=2026)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=2144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=1829)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.326 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.321 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.239)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=2252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.194 (n=1692)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.192 (n=942)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.73 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.437)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=404)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `2048.1399` → IC=+0.445 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2048.1399 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.443 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.458 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `13089.4142` → IC=+0.448 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13089.4142 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.455 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.467 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.442 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `3299.2146` → IC=+0.440 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3299.2146 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.420 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.413)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.414 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.413)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.411 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.413)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.418 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.413)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

- **FILTRO** `libro_liquidez` < `6836.9618` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 6836.9618
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.199 (n=29353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.240 (n=11079)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=5984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=5071)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=5469)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=5235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.225 (n=5242)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=1876)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=2838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=5442)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=2637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=2014)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=1853)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=4859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.254 (n=2462)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=2126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.195 (n=1849)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 5.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=1948)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.201 (n=4513)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` < `4.09` → IC=+0.134 (n=4107)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.09 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.146 (n=4218)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.95 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.123 (n=4777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=5429)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.24` → IC=+0.146 (n=4115)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.24 (IC base=+0.122)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.204 (n=2274)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.126)

- **PATRÓN** `restante_min` < `4.03` → IC=+0.137 (n=2047)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.03 (IC base=+0.126)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.142 (n=2071)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.94 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.139 (n=3018)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 8.0 (IC base=+0.126)

- **PATRÓN** `lag_apertura_s` < `3.74` → IC=+0.145 (n=2038)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 3.74 (IC base=+0.126)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=2239)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.49` → IC=+0.125 (n=2763)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.49 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=2157)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.41` → IC=+0.145 (n=2071)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.41 (IC base=+0.118)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.298 (n=1045)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.383 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1594.2001` → IC=+0.294 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1594.2001 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.291 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.270)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.337 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `4209.1188` → IC=+0.289 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4209.1188 (IC base=+0.270)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.326 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.292 (n=475)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.394 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1485.7226` → IC=+0.314 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1485.7226 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.343 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.337)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.361 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.337)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.377 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.337)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.345 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.337)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.373 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.337)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.443 (n=456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.441 (n=389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.436 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `1843.456` → IC=+0.441 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1843.456 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.435 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.435 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `2081.2854` → IC=+0.457 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2081.2854 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.381)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.298 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.298 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.268 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1376.3842` → IC=+0.285 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1376.3842 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.3527` → IC=+0.124 (n=5991)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.3527 (IC base=+0.101)

- **PATRÓN** `ibs_20min` > `0.9798` → IC=+0.238 (n=2270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9798 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` < `0.6061` → IC=+0.246 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6061 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.862` → IC=+0.172 (n=2633)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 5.862 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `1.2124` → IC=+0.246 (n=1772)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2124 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` > `1.0555` → IC=+0.246 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0555 (IC base=+0.101)

- **PATRÓN** `volumen_pendiente_norm` > `0.3074` → IC=+0.212 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3074 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` > `1.9108` → IC=+0.204 (n=3035)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9108 (IC base=+0.101)

- **PATRÓN** `ibs_20min` < `0.5703` → IC=+0.131 (n=8266)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5703 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.5678` → IC=+0.186 (n=556)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.5678 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` < `0.1383` → IC=+0.168 (n=2528)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1383 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` < `1.1978` → IC=+0.168 (n=2775)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1978 (IC base=+0.059)

- **PATRÓN** `volumen_regimen` > `0.8699` → IC=+0.172 (n=1850)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 0.8699 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.223 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.167 (IC base=+0.059)

- **PATRÓN** `volumen_spike_ratio` > `1.5824` → IC=+0.199 (n=4114)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.5824 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.215 (n=3855)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 85.0 (IC base=+0.059)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.180 (n=514)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.005 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.177 (n=515)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0081 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.3326` → IC=+0.168 (n=1538)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3326 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.168 (n=752)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.186 (n=584)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.032` → IC=+0.276 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.032 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.202 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.166 (n=1424)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.182 (n=1480)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.249 (n=1012)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.088` → IC=+0.292 (n=378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.088 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.249 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0583` → IC=+0.294 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0583 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.373` → IC=+0.249 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.373 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0914` → IC=+0.230 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0914 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2284` → IC=+0.262 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2284 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.248 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1609.04` → IC=+0.250 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1609.04 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.234 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.1164` → IC=+0.246 (n=513)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1164 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=1215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.9138` → IC=+0.257 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9138 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.1922` → IC=+0.213 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1922 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` < `0.3703` → IC=+0.216 (n=1089)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3703 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.874` → IC=+0.233 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.874 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.2501` → IC=+0.221 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2501 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.8746` → IC=+0.215 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8746 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.159` → IC=+0.212 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.159 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.220 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.4994` → IC=+0.220 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4994 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.3766` → IC=+0.228 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3766 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `11104.1249` → IC=+0.224 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11104.1249 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.156 (n=827)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0767` → IC=+0.155 (n=413)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0767 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.162 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.170 (n=1239)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6789 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1259` → IC=+0.150 (n=1107)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1259 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.547` → IC=+0.159 (n=405)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.547 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.2046` → IC=+0.144 (n=1239)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2046 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.137 (n=1239)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6201 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.175 (n=333)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4311` → IC=+0.146 (n=1129)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4311 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.7651` → IC=+0.141 (n=753)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7651 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `13672.3135` → IC=+0.139 (n=826)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 13672.3135 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `416.0` → IC=+0.143 (n=1045)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 416.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.199 (n=1499)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0059 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=1572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=1001)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.261 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.865` → IC=+0.236 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.865 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` < `0.2131` → IC=+0.188 (n=1477)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2131 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.3716` → IC=+0.192 (n=196)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.3716 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.9287` → IC=+0.206 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9287 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=1741)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.228 (n=1275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.219)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.220 (n=1138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.3808` → IC=+0.236 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3808 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.703` → IC=+0.239 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.703 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3635` → IC=+0.268 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3635 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.2814` → IC=+0.229 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2814 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.235 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1907.76` → IC=+0.247 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1907.76 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.231 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.219)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1906)

- **PATRÓN** `ibs_20min` > `0.94` → IC=+0.200 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.94 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` > `0.3371` → IC=+0.342 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3371 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` < `0.6795` → IC=+0.329 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6795 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.461` → IC=+0.144 (n=599)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 4.461 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` < `0.5964` → IC=+0.343 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5964 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` > `1.1897` → IC=+0.352 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1897 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.373 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` < `1.4779` → IC=+0.348 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4779 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` > `1.7863` → IC=+0.340 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7863 (IC base=+0.016)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.343 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 169.0 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` > `0.1738` → IC=+0.164 (n=263)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1738 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `1.0271` → IC=+0.147 (n=581)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.0271 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2693` → IC=+0.233 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2693 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.5018` → IC=+0.177 (n=543)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.5018 (IC base=+0.004)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.149 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=272)

- **FILTRO** `ibs_20min` < `0.375` → IC=-0.176 (n=106)

  - _Acción_: SKIP cuando `ibs_20min` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=221)

- **FILTRO** `ibs_20min` > `0.2692` → IC=-0.132 (n=1888)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2692
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=932)

- **FILTRO** `sigma_ewma_delta_pct` > `8.618` → IC=-0.217 (n=312)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.618
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2508)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.9864` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9864 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` < `0.5354` → IC=+0.289 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5354 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.5788` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5788 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `0.7836` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7836 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.064` → IC=+0.326 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.064 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.7895` → IC=+0.312 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7895 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `1.5176` → IC=+0.286 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5176 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.326 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` > `0.6118` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6118 (IC base=-0.049)

- **PATRÓN** `volumen_regimen` < `1.0699` → IC=+0.216 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0699 (IC base=-0.049)

- **PATRÓN** `volumen_pendiente_norm` < `0.102` → IC=+0.220 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.102 (IC base=-0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.1481` → IC=+0.240 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1481 (IC base=-0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.4205` → IC=+0.256 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4205 (IC base=-0.049)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.250 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=-0.049)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6568` → IC=-0.195 (n=476)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=1430)

- **FILTRO** `ibs_20min` < `0.6821` → IC=-0.159 (n=1257)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6821
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=649)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.196 (n=389)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=1517)

- **FILTRO** `ibs_20min` > `0.775` → IC=-0.204 (n=711)

  - _Acción_: SKIP cuando `ibs_20min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2140)

- **PATRÓN** `dist_vwap_pct` > `0.9664` → IC=+0.291 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9664 (IC base=-0.079)

- **PATRÓN** `dist_vwap_pct` < `0.2456` → IC=+0.316 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2456 (IC base=-0.079)

- **PATRÓN** `volumen_regimen` < `0.9967` → IC=+0.281 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9967 (IC base=-0.079)

- **PATRÓN** `volumen_regimen` > `0.6141` → IC=+0.298 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6141 (IC base=-0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.0764` → IC=+0.306 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0764 (IC base=-0.079)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.287 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=-0.079)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.283 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=-0.079)

- **PATRÓN** `dist_vwap_pct` > `1.0191` → IC=+0.281 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0191 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.26` → IC=+0.246 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.26 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.7364` → IC=+0.253 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7364 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.290 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1058` → IC=+0.278 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1058 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.1777` → IC=+0.257 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1777 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.5844` → IC=+0.243 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5844 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.193 (n=2827)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0094 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.4655` → IC=+0.185 (n=7574)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.4655 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `1.0273` → IC=+0.293 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0273 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.509` → IC=+0.152 (n=4021)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.509 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` > `0.6787` → IC=+0.246 (n=2613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6787 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2452` → IC=+0.263 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2452 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `1.4735` → IC=+0.247 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4735 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` > `2.7185` → IC=+0.246 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7185 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.278 (n=4215)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.093)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.141 (n=2862)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0088 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.5534` → IC=+0.150 (n=7549)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5534 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.6844` → IC=+0.236 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6844 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2317` → IC=+0.232 (n=2283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2317 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `0.7154` → IC=+0.232 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7154 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` > `1.199` → IC=+0.245 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.199 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.2476` → IC=+0.316 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2476 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.6166` → IC=+0.250 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6166 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` > `2.3469` → IC=+0.256 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3469 (IC base=+0.069)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.259 (n=3006)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.069)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2507` → IC=-0.147 (n=578)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2507
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=1737)

- **FILTRO** `sigma_ewma_delta_pct` > `4.399` → IC=-0.167 (n=442)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.399
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1493)

- **PATRÓN** `ibs_20min` > `0.8861` → IC=+0.273 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8861 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.283` → IC=+0.158 (n=794)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.283 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.277` → IC=+0.292 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.277 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.4428` → IC=+0.203 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4428 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` > `2.5703` → IC=+0.207 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5703 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.194 (n=214)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 13.0 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` < `0.1845` → IC=+0.475 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1845 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.2378` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2378 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8196` → IC=-0.149 (n=627)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8196
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1884)

- **PATRÓN** `dist_vwap_pct` > `0.3003` → IC=+0.160 (n=301)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3003 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` < `1.1921` → IC=+0.142 (n=757)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1921 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` > `0.6566` → IC=+0.149 (n=677)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6566 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.197 (n=97)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.190 (n=246)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` > `2.3568` → IC=+0.141 (n=246)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.3568 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `254.0` → IC=+0.190 (n=321)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 254.0 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` > `0.6419` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6419 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.211 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `0.5945` → IC=+0.204 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5945 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.276` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.276 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1737` → IC=+0.230 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1737 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `485.0` → IC=+0.207 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 485.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.292 (n=903)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.1` → IC=+0.248 (n=451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.258 (n=511)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.758` → IC=+0.282 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.758 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.260 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.8634` → IC=+0.247 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8634 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `2.9826` → IC=+0.258 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9826 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=1551)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `1919.501` → IC=+0.254 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.501 (IC base=+0.244)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.267 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.244)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.303 (n=1067)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.323 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.288 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.884` → IC=+0.303 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.884 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.304 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.6234` → IC=+0.291 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6234 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.8751` → IC=+0.285 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8751 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `1900.7432` → IC=+0.318 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1900.7432 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.289 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.283)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2556` → IC=-0.206 (n=399)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2556
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=1200)

- **FILTRO** `ibs_20min` > `0.7967` → IC=-0.184 (n=507)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7967
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=1522)

- **PATRÓN** `ibs_20min` > `0.8036` → IC=+0.163 (n=544)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8036 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` > `0.4516` → IC=+0.233 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4516 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` < `0.9674` → IC=+0.226 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9674 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `0.6394` → IC=+0.216 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6394 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2647` → IC=+0.326 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2647 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `2.0676` → IC=+0.248 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0676 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `1.3727` → IC=+0.238 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.3727 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.257 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 160.0 (IC base=+0.000)

- **PATRÓN** `dist_vwap_pct` > `0.1281` → IC=+0.200 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1281 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` < `0.4847` → IC=+0.184 (n=318)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.4847 (IC base=-0.012)

- **PATRÓN** `volumen_regimen` < `1.0026` → IC=+0.188 (n=261)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0026 (IC base=-0.012)

- **PATRÓN** `volumen_regimen` > `0.7266` → IC=+0.185 (n=265)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.7266 (IC base=-0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.1562` → IC=+0.279 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1562 (IC base=-0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.7947` → IC=+0.238 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7947 (IC base=-0.012)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.243 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5154 (IC base=-0.012)

- **PATRÓN** `ballena_activa_n` < `145.0` → IC=+0.246 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 145.0 (IC base=-0.012)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6909` → IC=-0.211 (n=911)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6909
  - _Potencial_: sin este filtro IC_bueno=+0.271 (n=911)

- **FILTRO** `ibs_20min` > `0.7049` → IC=-0.229 (n=474)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7049
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=1426)

- **FILTRO** `sigma_ewma_delta_pct` > `4.627` → IC=-0.177 (n=434)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.627
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=1466)

- **PATRÓN** `ibs_20min` > `0.6909` → IC=+0.271 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6909 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.2796` → IC=+0.325 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2796 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.469` → IC=+0.154 (n=284)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.469 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.299 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.6354` → IC=+0.285 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6354 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.287 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.335 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.4456` → IC=+0.324 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4456 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.318 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.030)

- **PATRÓN** `ibs_20min` < `0.1071` → IC=+0.199 (n=476)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1071 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` > `0.8343` → IC=+0.192 (n=76)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.8343 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` < `0.1847` → IC=+0.199 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1847 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `0.7129` → IC=+0.257 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7129 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.189 (n=390)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2643` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2643 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.5589` → IC=+0.210 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5589 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.225 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0161` → IC=+0.320 (n=747)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0161 (IC base=+0.275)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.295 (n=529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.275)

- **PATRÓN** `ibs_20min` > `0.9064` → IC=+0.348 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9064 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2708` → IC=+0.320 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2708 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.436` → IC=+0.303 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.436 (IC base=+0.275)

- **PATRÓN** `volumen_regimen` > `1.0357` → IC=+0.310 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0357 (IC base=+0.275)

- **PATRÓN** `volumen_pendiente_norm` > `0.2844` → IC=+0.305 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2844 (IC base=+0.275)

- **PATRÓN** `volumen_spike_ratio` < `1.5398` → IC=+0.281 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5398 (IC base=+0.275)

- **PATRÓN** `volumen_spike_ratio` > `2.5479` → IC=+0.288 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5479 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.279 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `2448.2154` → IC=+0.284 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2448.2154 (IC base=+0.275)

- **PATRÓN** `sigma_h` > `0.0147` → IC=+0.294 (n=822)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0147 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.284 (n=622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.3966` → IC=+0.305 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3966 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.5389` → IC=+0.285 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5389 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.438` → IC=+0.292 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.438 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.306 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2407` → IC=+0.354 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2407 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.5298` → IC=+0.265 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5298 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.167` → IC=+0.275 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.167 (IC base=+0.269)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.271 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `2367.1745` → IC=+0.273 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2367.1745 (IC base=+0.269)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.174 (n=2244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0049 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.205 (n=2235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3454` → IC=+0.176 (n=5894)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3454 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=6948)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.6943` → IC=+0.234 (n=5983)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6943 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.165` → IC=+0.197 (n=2959)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.165 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.206` → IC=+0.253 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.206 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.163 (n=4440)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2145 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6251` → IC=+0.161 (n=4440)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6251 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2464` → IC=+0.194 (n=1350)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2464 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5623` → IC=+0.176 (n=2810)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5623 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6486` → IC=+0.178 (n=2129)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6486 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3852.6349` → IC=+0.171 (n=2233)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3852.6349 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.183 (n=5606)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 120.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.184 (n=4272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0065 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.204 (n=2136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.207 (n=2169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.4737` → IC=+0.227 (n=6406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4737 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.2221` → IC=+0.160 (n=4692)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2221 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.135` → IC=+0.195 (n=1092)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.135 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `1.1795` → IC=+0.151 (n=4681)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1795 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` > `0.6253` → IC=+0.145 (n=4680)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6253 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.291` → IC=+0.227 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.291 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.5717` → IC=+0.167 (n=2528)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5717 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `2.6369` → IC=+0.174 (n=1915)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6369 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.171 (n=5373)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 122.0 (IC base=+0.168)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.223 (n=381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.197 (n=381)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0082 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.3311` → IC=+0.207 (n=1142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3311 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.186 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.034` → IC=+0.309 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.034 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.234 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.429` → IC=+0.183 (n=1044)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.429 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.205 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.243 (n=717)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.252 (n=725)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1803` → IC=+0.292 (n=542)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1803 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.239 (n=814)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.1059` → IC=+0.274 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1059 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.044` → IC=+0.255 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.044 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0946` → IC=+0.235 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0946 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.258 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4211` → IC=+0.255 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4211 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.631` → IC=+0.235 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.631 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1611.8061` → IC=+0.259 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1611.8061 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.251 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.0764` → IC=+0.199 (n=330)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0764 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=1032)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4268` → IC=+0.231 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4268 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.2063` → IC=+0.213 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2063 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.482` → IC=+0.226 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.482 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.2485` → IC=+0.173 (n=986)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.2485 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.0774` → IC=+0.166 (n=821)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.0774 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2311` → IC=+0.186 (n=218)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2311 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.4139` → IC=+0.203 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4139 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.4599` → IC=+0.165 (n=317)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4599 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `11701.6956` → IC=+0.181 (n=881)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 11701.6956 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.158 (n=1097)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.293` → IC=+0.157 (n=1098)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.293 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.157 (n=1011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.5447` → IC=+0.186 (n=1097)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.5447 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.133` → IC=+0.162 (n=1103)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.133 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.882` → IC=+0.208 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.882 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.155 (n=1097)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2089 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1575` → IC=+0.166 (n=336)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1575 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4292` → IC=+0.147 (n=987)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4292 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.148 (n=305)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 223.0 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.206 (n=1116)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.2014` → IC=+0.212 (n=745)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2014 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.289 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.673` → IC=+0.273 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.673 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.2129` → IC=+0.194 (n=1073)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.2129 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.6516` → IC=+0.200 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6516 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.2884` → IC=+0.204 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2884 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.208 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `1924.4094` → IC=+0.201 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1924.4094 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.240 (n=914)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.224 (n=817)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0898` → IC=+0.246 (n=305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0898 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.275 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` < `0.3478` → IC=+0.254 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3478 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.704` → IC=+0.277 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.704 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.272 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.8365` → IC=+0.219 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8365 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `3.4953` → IC=+0.240 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4953 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1904.2616` → IC=+0.246 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.2616 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.229 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.224)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.172 (n=1060)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0077 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4373` → IC=+0.165 (n=1061)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4373 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=1107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.4076` → IC=+0.206 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4076 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1422` → IC=+0.191 (n=712)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1422 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.003` → IC=+0.247 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.003 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.05` → IC=+0.157 (n=932)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.05 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `1.1917` → IC=+0.162 (n=353)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1917 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2885` → IC=+0.227 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2885 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4065` → IC=+0.169 (n=345)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4065 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5102` → IC=+0.180 (n=345)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.5102 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `7052.6142` → IC=+0.188 (n=706)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7052.6142 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.153 (n=995)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 171.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.161 (n=1126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0072 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.144 (n=1126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.187 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6096` → IC=+0.178 (n=1126)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6096 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.3367` → IC=+0.140 (n=1215)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.3367 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.618` → IC=+0.186 (n=218)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.618 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.141 (n=751)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8554 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2871` → IC=+0.212 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2871 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4695` → IC=+0.142 (n=336)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4695 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `10007.3401` → IC=+0.162 (n=510)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 10007.3401 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.124 (n=938)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 173.0 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.164 (n=558)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.01 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=1258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.5192` → IC=+0.203 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5192 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `1.0671` → IC=+0.220 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0671 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.458` → IC=+0.258 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.458 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.2243` → IC=+0.126 (n=1229)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2243 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` < `0.1676` → IC=+0.130 (n=1226)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1676 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.121 (n=518)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.8114` → IC=+0.132 (n=788)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8114 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1276)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2903.4322` → IC=+0.191 (n=557)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2903.4322 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.134 (n=908)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 49.0 (IC base=+0.116)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.149 (n=545)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.006 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.1` → IC=+0.150 (n=412)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.5625` → IC=+0.204 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5625 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.9525` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.9525 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.133 (n=1103)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.383` → IC=+0.150 (n=261)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 7.383 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.6337` → IC=+0.130 (n=412)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.6337 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.167 (n=148)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `1.4585` → IC=+0.139 (n=364)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4585 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `2.1742` → IC=+0.123 (n=494)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 2.1742 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `3081.0348` → IC=+0.159 (n=412)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3081.0348 (IC base=+0.109)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0185` → IC=+0.208 (n=778)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0185 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.1696` → IC=+0.209 (n=514)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1696 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=535)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.73` → IC=+0.258 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.73 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `1.2313` → IC=+0.222 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2313 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.403` → IC=+0.246 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.403 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.209` → IC=+0.205 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.209 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.6942` → IC=+0.210 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6942 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2387` → IC=+0.276 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2387 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1696` → IC=+0.215 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1696 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.202 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2587.3393` → IC=+0.200 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2587.3393 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.237 (n=409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0169` → IC=+0.210 (n=816)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0169 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.089` → IC=+0.216 (n=410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.089 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.221 (n=607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=562)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.029` → IC=+0.308 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.029 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.1476` → IC=+0.219 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1476 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.305` → IC=+0.233 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.305 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6271` → IC=+0.216 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6271 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.283 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.2351` → IC=+0.192 (n=956)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2351 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4604` → IC=+0.194 (n=1086)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4604 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2561.1058` → IC=+0.209 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2561.1058 (IC base=+0.203)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.157 (n=540)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0039 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.169 (n=538)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.009 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1349` → IC=+0.153 (n=710)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1349 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.3963` → IC=+0.176 (n=1611)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.3963 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.8398` → IC=+0.180 (n=239)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.8398 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.673` → IC=+0.172 (n=744)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 3.673 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.8703` → IC=+0.160 (n=926)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8703 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.6964` → IC=+0.146 (n=1240)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6964 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1633` → IC=+0.170 (n=444)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1633 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.4361` → IC=+0.158 (n=515)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4361 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.5596` → IC=+0.175 (n=515)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.5596 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=1802)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `8727.5698` → IC=+0.158 (n=731)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8727.5698 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.163 (n=1222)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 105.0 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.146 (n=566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0038 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=1704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` < `0.6416` → IC=+0.141 (n=1693)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.6416 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.134 (n=430)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `2.2349` → IC=+0.126 (n=1429)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.2349 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.121 (n=518)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 18.0 (IC base=+0.107)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3479` → IC=+0.135 (n=387)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.3479 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.148 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 9.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.6822` → IC=+0.181 (n=258)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6822 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.5223` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.5223 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.291` → IC=+0.148 (n=177)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.291 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6135` → IC=+0.157 (n=129)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6135 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `10528.8173` → IC=+0.138 (n=387)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 10528.8173 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.147 (n=120)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 156.0 (IC base=+0.113)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.209 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3387` → IC=+0.143 (n=530)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3387 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.3458` → IC=+0.199 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3458 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1732` → IC=+0.148 (n=530)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1732 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.437` → IC=+0.140 (n=209)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 4.437 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.869` → IC=+0.126 (n=552)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 6.869 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` > `1.0613` → IC=+0.163 (n=241)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.0613 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.1567` → IC=+0.209 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1567 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `2.1023` → IC=+0.150 (n=458)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1023 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4106` → IC=+0.138 (n=520)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4106 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 152.0 (IC base=+0.126)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.264 (n=210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.208 (n=214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.0948` → IC=+0.217 (n=157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0948 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.248 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.4001` → IC=+0.242 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4001 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.233 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.047` → IC=+0.235 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.047 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.209 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8331 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.223 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1605 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2464` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2464 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `1.3759` → IC=+0.226 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3759 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.0509` → IC=+0.245 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0509 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `12296.651` → IC=+0.211 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12296.651 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.3254` → IC=+0.150 (n=287)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.3254 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.1653` → IC=+0.138 (n=103)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1653 (IC base=+0.089)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3265` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3265
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=423)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.130 (n=317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0053 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.136 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 8.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.8889` → IC=+0.207 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8889 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.8449` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.8449 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.1` → IC=+0.179 (n=163)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 5.1 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.0562` → IC=+0.121 (n=312)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0562 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.192 (n=50)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `2.2114` → IC=+0.136 (n=152)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.2114 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `3078.7088` → IC=+0.217 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3078.7088 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 21.0 (IC base=+0.099)

- **PATRÓN** `ibs_20min` < `0.5152` → IC=+0.145 (n=345)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5152 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.6051` → IC=+0.178 (n=141)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.6051 (IC base=+0.075)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.191 (n=160)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.56 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2468` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2468 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.175 (n=152)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.8803` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8803 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.1233` → IC=+0.169 (n=140)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.1233 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2727.8122` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2727.8122 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.177 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.022 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.08` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.08 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.53` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.53 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.0734` → IC=+0.126 (n=177)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0734 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.6508` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.6508 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1187` → IC=+0.133 (n=178)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1187 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.6702` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.6702 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.0068` → IC=+0.127 (n=124)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.0068 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.146 (n=162)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 17.0 (IC base=+0.124)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.201 (n=2833)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=8833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.4727` → IC=+0.217 (n=8496)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4727 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.9144` → IC=+0.197 (n=1158)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.9144 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.559` → IC=+0.227 (n=4158)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.559 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.8814` → IC=+0.166 (n=3797)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8814 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.196 (n=1599)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.623` → IC=+0.190 (n=2706)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.623 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3802.1817` → IC=+0.170 (n=2832)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3802.1817 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.195 (n=6269)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 91.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.192 (n=5168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0069 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1439` → IC=+0.186 (n=3410)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1439 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=2971)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.5633` → IC=+0.237 (n=7749)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5633 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.2341` → IC=+0.160 (n=4815)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2341 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.826` → IC=+0.196 (n=1099)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.826 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.684` → IC=+0.181 (n=7508)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.684 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.6291` → IC=+0.154 (n=1789)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6291 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `1.2029` → IC=+0.152 (n=1789)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.2029 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.245 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.284` → IC=+0.188 (n=3179)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.284 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.193 (n=2263)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 25.0 (IC base=+0.179)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.208 (n=481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.211 (n=962)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.199 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.200 (n=972)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.324 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.348` → IC=+0.292 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.348 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.243 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `2.561` → IC=+0.206 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.561 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.259 (n=1111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.266 (n=1113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.1255` → IC=+0.290 (n=488)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1255 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=1001)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.255 (n=1015)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.3451` → IC=+0.287 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3451 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.427` → IC=+0.265 (n=1171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.427 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.296 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `1.8725` → IC=+0.275 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8725 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1608.68` → IC=+0.270 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1608.68 (IC base=+0.255)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.200 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0845` → IC=+0.165 (n=452)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0845 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3136` → IC=+0.203 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3136 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1244` → IC=+0.183 (n=771)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1244 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.756` → IC=+0.163 (n=315)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.756 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.279` → IC=+0.152 (n=1209)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.279 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.626` → IC=+0.183 (n=452)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.626 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.0738` → IC=+0.158 (n=1181)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.0738 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2654` → IC=+0.182 (n=196)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2654 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1195` → IC=+0.156 (n=1144)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1195 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7597` → IC=+0.161 (n=867)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7597 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11084.2751` → IC=+0.168 (n=1211)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 11084.2751 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `485.0` → IC=+0.160 (n=1232)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 485.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.2566` → IC=+0.165 (n=1053)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2566 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.158 (n=1120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` < `0.6379` → IC=+0.196 (n=1197)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6379 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6965` → IC=+0.149 (n=192)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6965 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1286` → IC=+0.163 (n=1086)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1286 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.493` → IC=+0.164 (n=209)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.493 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.158 (n=1197)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1913 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1504` → IC=+0.194 (n=328)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1504 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.159 (n=1099)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4232 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7499` → IC=+0.156 (n=733)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7499 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `365.0` → IC=+0.160 (n=668)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 365.0 (IC base=+0.147)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.006` → IC=+0.233 (n=1361)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.221 (n=1419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.221 (n=1379)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.6739` → IC=+0.256 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6739 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.576` → IC=+0.298 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.576 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.2136` → IC=+0.223 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2136 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.9235` → IC=+0.243 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.9235 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `1920.181` → IC=+0.221 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1920.181 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.243 (n=1275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.241 (n=849)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=485)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.3621` → IC=+0.271 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3621 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.741` → IC=+0.277 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.741 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.3562` → IC=+0.293 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3562 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.7875` → IC=+0.234 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7875 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.2286` → IC=+0.234 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2286 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.252 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1908.1032` → IC=+0.259 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.1032 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.264 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.236)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.184 (n=483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0035 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.4373` → IC=+0.142 (n=1444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.4373 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.148 (n=1504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.7002` → IC=+0.235 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7002 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.3544` → IC=+0.176 (n=566)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3544 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.385` → IC=+0.172 (n=242)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.385 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8781` → IC=+0.158 (n=963)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8781 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.239 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5111` → IC=+0.151 (n=612)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5111 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.4493` → IC=+0.157 (n=464)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.4493 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `8422.3422` → IC=+0.234 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8422.3422 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.167 (n=446)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 85.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.157 (n=1174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0076 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4443` → IC=+0.153 (n=1174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4443 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=534)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6883` → IC=+0.192 (n=1174)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.6883 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.2059` → IC=+0.142 (n=1063)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2059 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.936` → IC=+0.191 (n=173)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.936 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6962` → IC=+0.143 (n=517)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6962 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1764` → IC=+0.146 (n=391)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.1764 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.273 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4416` → IC=+0.152 (n=1103)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4416 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `11047.6745` → IC=+0.207 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11047.6745 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `188.0` → IC=+0.146 (n=1097)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 188.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_20min` > `0.6364` → IC=-0.175 (n=469)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6364
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=1408)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.133 (n=964)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0079 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.187 (n=1448)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4706 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `1.0481` → IC=+0.195 (n=277)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 1.0481 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.363` → IC=+0.231 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.363 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=1003)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `2913.9614` → IC=+0.244 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2913.9614 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.128 (n=1091)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 54.0 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.181 (n=471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0057 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.1276` → IC=+0.158 (n=471)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1276 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.151 (n=660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 15.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.204 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` < `0.4821` → IC=+0.122 (n=1349)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.4821 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.43` → IC=+0.123 (n=1356)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 3.43 (IC base=+0.109)

- **PATRÓN** `volumen_regimen` < `0.7154` → IC=+0.151 (n=620)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.7154 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.179 (n=216)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` < `1.461` → IC=+0.142 (n=417)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.461 (IC base=+0.109)

- **PATRÓN** `volumen_spike_ratio` > `2.2089` → IC=+0.122 (n=567)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 2.2089 (IC base=+0.109)

- **PATRÓN** `libro_liquidez` > `2867.96` → IC=+0.159 (n=470)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2867.96 (IC base=+0.109)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0245` → IC=+0.218 (n=658)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0245 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.205 (n=1295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` > `0.5143` → IC=+0.247 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5143 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.186` → IC=+0.230 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.186 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.415` → IC=+0.252 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.415 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.8796` → IC=+0.208 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8796 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.6326` → IC=+0.211 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6326 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.241 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.5489` → IC=+0.239 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5489 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.213 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2598.9768` → IC=+0.212 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2598.9768 (IC base=+0.206)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.231 (n=530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.017` → IC=+0.210 (n=1062)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.017 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.209 (n=1121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.198 (n=1679)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 18.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.5207` → IC=+0.252 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5207 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.4999` → IC=+0.198 (n=481)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.4999 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.2673` → IC=+0.202 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2673 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.724` → IC=+0.257 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.724 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.233` → IC=+0.235 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.233 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.262 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `2.2192` → IC=+0.192 (n=1240)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2192 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4427` → IC=+0.197 (n=1408)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4427 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.209 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2569.9973` → IC=+0.199 (n=1060)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2569.9973 (IC base=+0.198)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=2688)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.155 (n=2317)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0093 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.5234` → IC=+0.157 (n=2632)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.5234 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.156 (n=881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.169 (n=935)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.9395` → IC=+0.209 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9395 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1868` → IC=+0.156 (n=904)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1868 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.192` → IC=+0.177 (n=431)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.192 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.9028` → IC=+0.159 (n=1083)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.9028 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1725` → IC=+0.176 (n=712)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1725 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4575` → IC=+0.159 (n=868)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4575 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.8964` → IC=+0.160 (n=1735)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8964 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `8270.0397` → IC=+0.154 (n=1194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8270.0397 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.191 (n=677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0037 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4827` → IC=+0.151 (n=2028)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4827 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.165 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.159 (n=699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 4.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.1823` → IC=+0.158 (n=892)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1823 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.735` → IC=+0.132 (n=677)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.735 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.922` → IC=+0.134 (n=296)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.922 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.2418` → IC=+0.124 (n=1814)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.2418 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.309` → IC=+0.141 (n=2009)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 6.309 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.109` → IC=+0.138 (n=1695)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.109 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.147 (n=952)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.5352` → IC=+0.139 (n=884)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5352 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.8175` → IC=+0.140 (n=1338)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.8175 (IC base=+0.131)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=2688)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `7593.8032` → IC=+0.146 (n=1812)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 7593.8032 (IC base=+0.131)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.173 (n=295)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0034 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.0921` → IC=+0.188 (n=110)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0921 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.5544` → IC=+0.189 (n=220)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5544 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.2265` → IC=+0.186 (n=154)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.2265 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.282` → IC=+0.163 (n=413)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 8.282 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.8282` → IC=+0.198 (n=220)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.8282 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.3102` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3102 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4394` → IC=+0.188 (n=110)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4394 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.7705` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7705 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `12645.8095` → IC=+0.204 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12645.8095 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.209 (n=393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.169 (n=297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.165 (n=332)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.1527` → IC=+0.157 (n=392)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.1527 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.6117` → IC=+0.143 (n=404)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6117 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.7065` → IC=+0.143 (n=82)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.7065 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.2247` → IC=+0.133 (n=913)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2247 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.06` → IC=+0.148 (n=972)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 9.06 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8811` → IC=+0.176 (n=594)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8811 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.162 (n=421)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.5736` → IC=+0.138 (n=888)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5736 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.8153` → IC=+0.141 (n=592)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.8153 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `11387.9096` → IC=+0.145 (n=891)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 11387.9096 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `714.0` → IC=+0.137 (n=847)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 714.0 (IC base=+0.131)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.180 (n=282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.4174` → IC=+0.173 (n=548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.4174 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.9934` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9934 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.404` → IC=+0.217 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.404 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `3.3904` → IC=+0.166 (n=621)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3904 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2425.929` → IC=+0.197 (n=282)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2425.929 (IC base=+0.164)

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
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.152 (n=357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.005 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.156 (n=808)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0045 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4977` → IC=+0.154 (n=808)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.4977 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.169 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 4.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.5451` → IC=+0.151 (n=539)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.5451 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.1862` → IC=+0.156 (n=808)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.1862 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `1.0356` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 1.0356 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.4283` → IC=+0.160 (n=751)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.4283 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.735` → IC=+0.157 (n=808)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.735 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.0977` → IC=+0.151 (n=711)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0977 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `0.7182` → IC=+0.153 (n=722)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.7182 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.1126` → IC=+0.149 (n=745)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.1126 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1724` → IC=+0.163 (n=238)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1724 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.5252` → IC=+0.155 (n=793)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5252 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=785)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.160 (n=662)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0084 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.5056` → IC=+0.172 (n=662)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.5056 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.148 (n=464)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.103` → IC=+0.157 (n=662)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.103 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.153 (n=318)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.4003` → IC=+0.146 (n=665)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.4003 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.675` → IC=+0.158 (n=109)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.675 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.266` → IC=+0.143 (n=598)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.266 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.0958` → IC=+0.156 (n=583)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0958 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.7257` → IC=+0.146 (n=591)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7257 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.174 (n=283)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.160 (n=572)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7831` → IC=+0.155 (n=433)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7831 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `7781.1736` → IC=+0.164 (n=662)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 7781.1736 (IC base=+0.142)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=166)

- **PATRÓN** `ibs_20min` > `0.9706` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.9706 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.165` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 7.165 (IC base=+0.025)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.248 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=305)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.235 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=310)

- **FILTRO** `dist_vwap_pct` > `0.1599` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1599
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=240)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.209 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.6061` → IC=+0.207 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6061 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.175 (n=358)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.791` → IC=+0.214 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.791 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `0.8014` → IC=+0.136 (n=429)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8014 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `0.9761` → IC=+0.129 (n=292)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.9761 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.204 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `2.1116` → IC=+0.167 (n=470)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.1116 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=524)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `2468.387` → IC=+0.150 (n=281)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2468.387 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.277 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=-0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0643` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0643 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` < `2.3013` → IC=+0.125 (n=150)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.3013 (IC base=-0.025)

- **PATRÓN** `volumen_spike_ratio` > `1.4422` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4422 (IC base=-0.025)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.171 (n=253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0061 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.592` → IC=+0.201 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.592 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.181 (n=114)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.791` → IC=+0.121 (n=138)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` > 3.791 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.0527` → IC=+0.131 (n=196)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0527 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.152 (n=162)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `2.0129` → IC=+0.189 (n=162)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.0129 (IC base=+0.105)

- **PATRÓN** `drift_60min` |x|≤ `0.0437` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0437 (IC base=+0.049)

- **PATRÓN** `ibs_20min` < `0.739` → IC=+0.187 (n=97)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.739 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` < `0.0573` → IC=+0.126 (n=97)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.0573 (IC base=+0.049)

- **PATRÓN** `volumen_regimen` < `0.6802` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6802 (IC base=+0.049)

- **PATRÓN** `volumen_pendiente_norm` > `0.0849` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0849 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` < `2.0636` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.0636 (IC base=+0.049)

- **PATRÓN** `volumen_spike_ratio` > `1.4201` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4201 (IC base=+0.049)

- **PATRÓN** `libro_liquidez` > `3269.2861` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3269.2861 (IC base=+0.049)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.288 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=94)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.174 (n=170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.005 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.5986` → IC=+0.233 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5986 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.182 (n=124)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.616` → IC=+0.328 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.616 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.0679` → IC=+0.149 (n=223)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0679 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6313` → IC=+0.152 (n=199)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6313 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3002` → IC=+0.274 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3002 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.7434` → IC=+0.178 (n=116)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.7434 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.3908` → IC=+0.163 (n=173)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.3908 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=233)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `1101.9191` → IC=+0.180 (n=195)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1101.9191 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.159 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.108 (IC base=-0.067)

- **PATRÓN** `ibs_20min` < `0.1926` → IC=+0.206 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1926 (IC base=-0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.067)

- **PATRÓN** `volumen_spike_ratio` > `2.637` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.637 (IC base=-0.067)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=82)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.171 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0054 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.6324` → IC=+0.185 (n=198)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.6324 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.184` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.184 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.626` → IC=+0.221 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.626 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` > `0.6582` → IC=+0.126 (n=177)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6582 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.0894` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0894 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `2.1768` → IC=+0.169 (n=158)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.1768 (IC base=+0.088)

- **PATRÓN** `libro_spread` < `0.08` → IC=+0.123 (n=181)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.08 (IC base=+0.088)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.143 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.006 (IC base=-0.077)

- **PATRÓN** `ibs_20min` < `0.1154` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1154 (IC base=-0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.966` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.966 (IC base=-0.077)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `11.0` → IC=-0.429 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=126)

- **FILTRO** `dist_vwap_pct` > `0.2226` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2226
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=149)

- **FILTRO** `volumen_spike_ratio` > `3.4505` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.4505
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=70)

- **FILTRO** `volumen_spike_ratio` < `1.6757` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.6757
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=62)

- **FILTRO** `drift_60min` |x|> `0.2212` → IC=-0.338 (n=35)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2212
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=109)

- **FILTRO** `dist_vwap_pct` > `0.3412` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3412
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=121)

- **FILTRO** `sigma_ewma_delta_pct` > `8.432` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.432
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=121)

- **FILTRO** `volumen_pendiente_norm` > `0.074` → IC=-0.400 (n=18)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.074
  - _Potencial_: sin este filtro IC_bueno=-0.280 (n=48)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.210 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

- **FILTRO** `volumen_regimen` < `0.892` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.892
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=38)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=42)

- **FILTRO** `dist_vwap_pct` < `0.0874` → IC=-0.284 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0874
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=27)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=41)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.8218` → IC=-0.450 (n=38)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8218
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.340 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

- **FILTRO** `dist_vwap_pct` > `0.0486` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0486
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=35)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=20)

- **FILTRO** `volumen_regimen` < `1.0683` → IC=-0.431 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0683
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.234` → IC=-0.140 (n=109)

  - _Acción_: SKIP cuando `ibs_20min` > 0.234
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=214)

- **FILTRO** `dist_vwap_pct` > `0.6344` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6344
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=297)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.126 (n=105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 15.0 (IC base=+0.080)

- **PATRÓN** `ibs_20min` > `0.6592` → IC=+0.161 (n=225)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6592 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.4724` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.4724 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.234` → IC=+0.125 (n=214)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.234 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.13` → IC=+0.138 (n=103)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 6.13 (IC base=+0.035)

- **PATRÓN** `libro_liquidez` > `3837.0322` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3837.0322 (IC base=+0.035)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=83)

- **FILTRO** `ibs_20min` < `0.5548` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5548
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=75)

- **FILTRO** `volumen_regimen` < `0.7777` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7777
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=75)

- **PATRÓN** `ibs_20min` > `0.6466` → IC=+0.123 (n=67)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.6466 (IC base=-0.025)

- **PATRÓN** `ibs_20min` < `0.1381` → IC=+0.183 (n=99)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1381 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.1746` → IC=+0.131 (n=82)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1746 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `2.8706` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.8706 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `3574.4675` → IC=+0.149 (n=112)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3574.4675 (IC base=+0.096)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=61)

- **FILTRO** `ibs_20min` < `0.8361` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8361
  - _Potencial_: sin este filtro IC_bueno=+0.196 (n=54)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=77)

- **FILTRO** `ibs_20min` > `0.3236` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3236
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=77)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.167 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0042 (IC base=+0.073)

- **PATRÓN** `drift_60min` |x|≤ `0.2855` → IC=+0.135 (n=61)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.2855 (IC base=+0.073)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.073)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.121 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 7.0 (IC base=+0.073)

- **PATRÓN** `ibs_20min` > `0.8361` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.8361 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.0901` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.0901 (IC base=+0.073)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `1555.6741` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1555.6741 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.000)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.55` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ibs_20min` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=56)

- **FILTRO** `volumen_regimen` < `1.0339` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0339
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=36)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.197 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0047 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.182 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0058 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.170 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` < `0.7619` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7619 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.7619 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.6434` → IC=+0.283 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6434 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` < `0.2073` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2073 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.246 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.0991` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0991 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5494` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5494 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.03 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `523.3443` → IC=+0.167 (n=91)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 523.3443 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.0808` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0808 (IC base=-0.041)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `4.0` → IC=+0.125 (n=606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 4.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.130 (n=549)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.5 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2855.9096` → IC=+0.175 (n=189)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2855.9096 (IC base=+0.114)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `4.0` → IC=+0.125 (n=606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 4.0 (IC base=+0.114)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.130 (n=549)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` > 0.5 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2855.9096` → IC=+0.175 (n=189)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2855.9096 (IC base=+0.114)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=76)

- **FILTRO** `py_entrada` < `0.435` → IC=-0.176 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=110)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=129)

- **FILTRO** `libro_liquidez` < `2453.3967` → IC=-0.263 (n=36)

  - _Acción_: SKIP cuando `libro_liquidez` < 2453.3967
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=109)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=196)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=182)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4919.88` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `liq_usd_total` < 4919.88
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=16)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1409)

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
- **FILTRO** `liq_usd_total` < `35093.65` → IC=-0.160 (n=45)

  - _Acción_: SKIP cuando `liq_usd_total` < 35093.65
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=94)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `liq_usd_total` > `61042.02` → IC=+0.167 (n=70)

  - _Acción_: Kelly boost +0.83€ cuando `liq_usd_total` > 61042.02 (IC base=+0.018)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=74)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=642)

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
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=422)

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
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=77)

### LIQUIDACIONES_60M
- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=445)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=284)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=284)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=166)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=166)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=78)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=103)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=66)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=82)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=171)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=72)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=221)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=221)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=100)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=6968)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=1058)

- **FILTRO** `libro_liquidez` < `15906.9303` → IC=-0.152 (n=268)

  - _Acción_: SKIP cuando `libro_liquidez` < 15906.9303
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=805)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.178 (n=2899)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=8991)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.174 (n=2995)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=9315)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.215 (n=499)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1530)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.170 (n=510)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=1690)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=1214)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.021)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.208 (n=509)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1561)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.223 (n=511)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=1668)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.169 (n=532)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=1647)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.197 (n=476)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=1531)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.192 (n=524)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1656)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=2526)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=2662)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=2668)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=325)

- **FILTRO** `ibs_20min` > `0.1405` → IC=-0.121 (n=138)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1405
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=270)

- **FILTRO** `libro_liquidez` < `16719.5604` → IC=-0.149 (n=203)

  - _Acción_: SKIP cuando `libro_liquidez` < 16719.5604
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=612)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=205)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.346 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=192)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=673)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.136 (n=42)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.032)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=8516)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=18996)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.280 (n=6587)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=20925)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.241 (n=6857)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=20655)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.162 (n=9117)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=18395)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.229 (n=8133)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=26441)

- **FILTRO** `ibs_7min` > `0.2955` → IC=-0.177 (n=8637)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2955
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=25937)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=1071)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=3398)

- **FILTRO** `ibs_7min` < `0.7073` → IC=-0.260 (n=1474)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7073
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2995)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.178 (n=1116)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=3353)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.150 (n=4032)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=1963)

- **FILTRO** `drift_7min_pct` |x|> `0.1117` → IC=-0.125 (n=2031)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1117
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=3964)

- **FILTRO** `ibs_7min` > `0.7987` → IC=-0.205 (n=1498)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7987
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=4497)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=3672)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.257 (n=1146)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3656)

- **FILTRO** `ibs_7min` < `0.7534` → IC=-0.187 (n=1200)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7534
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3602)

- **FILTRO** `ballena_activa_n` > `162.0` → IC=-0.176 (n=1197)

  - _Acción_: SKIP cuando `ballena_activa_n` > 162.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=3605)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.252 (n=1181)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=3681)

- **FILTRO** `ibs_7min` > `0.2571` → IC=-0.170 (n=1215)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2571
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3647)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.181 (n=1212)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3650)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.168 (n=1201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=2989)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.313 (n=1014)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=3176)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.245 (n=1382)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=2808)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.225 (n=954)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=3236)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.234 (n=1487)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=4841)

- **FILTRO** `ibs_7min` > `0.7633` → IC=-0.173 (n=1581)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7633
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=4747)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.127 (n=1460)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=3079)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.239 (n=1342)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3197)

- **FILTRO** `ibs_7min` < `0.742` → IC=-0.187 (n=1133)

  - _Acción_: SKIP cuando `ibs_7min` < 0.742
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3406)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.182 (n=1121)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=3418)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1159)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3493)

- **FILTRO** `ibs_7min` > `0.2744` → IC=-0.175 (n=1160)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2744
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=3492)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.185 (n=1140)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3512)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.260 (n=1206)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3681)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.229 (n=1218)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3669)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.173 (n=1606)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4941)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.281 (n=1063)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3562)

- **FILTRO** `ibs_7min` < `0.7156` → IC=-0.231 (n=1156)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7156
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3469)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.211 (n=1119)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=3506)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.206 (n=1462)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=4728)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1004)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=500)

- **FILTRO** `libro_liquidez` < `10515.1773` → IC=-0.159 (n=136)

  - _Acción_: SKIP cuando `libro_liquidez` < 10515.1773
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=410)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=317)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=539)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.153 (n=448)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.133 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.159 (n=224)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 459.6089 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `3728.089` → IC=+0.129 (n=305)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3728.089 (IC base=+0.121)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4377` → IC=+0.167 (n=52)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4377 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.138)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.188 (n=91)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.104)

- **PATRÓN** `total_vol_5m` < `394.3776` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.3776 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 70.0 (IC base=+0.104)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.192 (n=118)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.208 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.148)

- **PATRÓN** `total_vol_5m` < `7671.127` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 7671.127 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `3221.1629` → IC=+0.157 (n=106)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3221.1629 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.192 (n=50)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 37.0 (IC base=+0.148)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.167 (n=115)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.143 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 12.0 (IC base=+0.118)

- **PATRÓN** `total_vol_5m` < `358653.4` → IC=+0.143 (n=113)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 358653.4 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.244 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.118)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.315 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=156)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.163 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0039 (IC base=-0.133)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.360 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=50)

- **FILTRO** `T_h` > `54.3209` → IC=-0.360 (n=48)

  - _Acción_: SKIP cuando `T_h` > 54.3209
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=50)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.130)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `T_h` < `267.9719` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `T_h` < 267.9719
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0142` → IC=-0.206 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0142
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `T_h` < `90.336` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `T_h` < 90.336
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.6696` → IC=-0.271 (n=107)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.6696
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=213)

- **FILTRO** `pct_vs_K` |x|> `2.6757` → IC=-0.424 (n=130)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6757
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=131)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `63.9952` → IC=-0.193 (n=86)

  - _Acción_: SKIP cuando `T_h` > 63.9952
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **FILTRO** `pct_vs_K` |x|> `2.7902` → IC=-0.375 (n=38)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7902
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=78)

- **FILTRO** `T_h` > `144.6172` → IC=-0.318 (n=20)

  - _Acción_: SKIP cuando `T_h` > 144.6172
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=72)

- **FILTRO** `pct_vs_K` |x|> `3.0008` → IC=-0.439 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0008
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=61)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `3.386` → IC=-0.403 (n=29)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.386
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=60)

- **FILTRO** `sigma_h` > `0.0095` → IC=-0.292 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=67)

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.375 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=67)

- **FILTRO** `T_h` > `61.3303` → IC=-0.324 (n=66)

  - _Acción_: SKIP cuando `T_h` > 61.3303
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=23)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `T_h` > `135.6166` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `T_h` > 135.6166
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=49)

- **FILTRO** `pct_vs_K` |x|> `5.0364` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.0364
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=55)

- **FILTRO** `sigma_h` < `0.0129` → IC=-0.353 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **FILTRO** `T_h` > `74.8972` → IC=-0.368 (n=36)

  - _Acción_: SKIP cuando `T_h` > 74.8972
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=13)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.377)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.470 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.377)

- **PATRÓN** `T_h` > `0.8592` → IC=+0.470 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8592 (IC base=+0.377)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.470 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.377)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.463 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.377)

- **PATRÓN** `edge` > `0.1023` → IC=+0.447 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.406)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.441 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.406)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.439 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.406)

- **PATRÓN** `dist_50` > `0.4085` → IC=+0.476 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4085 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.432 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.406)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.478)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.460 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.478)

- **PATRÓN** `sigma_h` < `0.0148` → IC=+0.468 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0148 (IC base=+0.468)

- **PATRÓN** `T_h` > `0.958` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.958 (IC base=+0.468)

- **PATRÓN** `dist_50` > `0.4658` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4658 (IC base=+0.468)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.457 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.468)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.457 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.468)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=144)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=250)

- **FILTRO** `streak_estiramiento` > `0.8382` → IC=-0.185 (n=52)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8382
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=157)

- **PATRÓN** `streak_estiramiento` < `0.4763` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `streak_estiramiento` < 0.4763 (IC base=+0.022)

- **PATRÓN** `streak_estiramiento` < `0.5654` → IC=+0.154 (n=105)

  - _Acción_: Kelly boost +0.77€ cuando `streak_estiramiento` < 0.5654 (IC base=+0.027)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `991078.0` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_racha` > 991078.0
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=26)

- **PATRÓN** `volumen_racha` < `991078.0` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_racha` < 991078.0 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=80)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=86)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=34)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=642)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=648)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=338)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `libro_liquidez` < `2389.5844` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2389.5844
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=505)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1023)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=615)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=623)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=2549)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1321)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1329)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.230 (n=571)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.1641` → IC=+0.192 (n=1109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1641 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.057` → IC=+0.188 (n=1260)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.057 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1354` → IC=+0.245 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1354 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.194 (n=886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 11.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.201 (n=607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.6192` → IC=+0.265 (n=1260)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6192 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.4411` → IC=+0.187 (n=305)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.4411 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.5591` → IC=+0.179 (n=1268)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.5591 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.367` → IC=+0.269 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.367 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `9139.2638` → IC=+0.192 (n=420)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 9139.2638 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.213 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.188)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=418)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.220 (n=205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.281 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2012` → IC=+0.211 (n=140)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2012 (IC base=+0.206)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2203` → IC=+0.266 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2203 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.257 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.267 (n=307)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.4073` → IC=+0.273 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4073 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.583` → IC=+0.256 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.583 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `15869.2533` → IC=+0.262 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15869.2533 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.173 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0034 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.150 (n=198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.005 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.151 (n=130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2358` → IC=+0.183 (n=99)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio_macro` |x|> 0.2358 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.266` → IC=+0.172 (n=199)

  - _Acción_: Kelly boost +0.86€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.266 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.162 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.157 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 6.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.6381` → IC=+0.234 (n=295)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6381 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1005` → IC=+0.170 (n=204)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1005 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.223 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `9475.4181` → IC=+0.147 (n=134)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 9475.4181 (IC base=+0.143)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `drift_15min` |x|> `0.6221` → IC=-0.156 (n=30)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.6221
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=59)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=64)

- **FILTRO** `ibs_15` > `0.2226` → IC=-0.227 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2226
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=64)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.232 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1785` → IC=+0.177 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1785 (IC base=+0.150)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0638` → IC=+0.180 (n=145)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.0638 (IC base=+0.150)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2704` → IC=+0.202 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2704 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.182 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.245 (n=163)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1134` → IC=+0.150 (n=98)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1134 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.5918` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.5918 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.026` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.026 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=130)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3004.732` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3004.732 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.213 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.150)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.556` → IC=-0.137 (n=122)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.556
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=638)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `14.795` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.795 (IC base=-0.006)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0166` → IC=+0.240 (n=233)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0166 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.205 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.190)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0407` → IC=+0.198 (n=349)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio_macro` |x|> 0.0407 (IC base=+0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1004` → IC=+0.293 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1004 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.244 (n=174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.190)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.283 (n=349)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.1199` → IC=+0.205 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1199 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` < `0.606` → IC=+0.198 (n=408)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.606 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.726` → IC=+0.238 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.726 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.191 (n=389)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.03 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `2861.0808` → IC=+0.265 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2861.0808 (IC base=+0.190)

- **PATRÓN** `ibs_15` < `0.1154` → IC=+0.168 (n=389)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.84€ cuando `ibs_15` < 0.1154 (IC base=+0.042)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.387 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.342)

- **PATRÓN** `drift_60min` |x|≤ `0.1519` → IC=+0.350 (n=305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1519 (IC base=+0.342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.358 (n=231)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.342)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1316` → IC=+0.390 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1316 (IC base=+0.342)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.357 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.342)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.382 (n=346)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` > `0.4267` → IC=+0.385 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4267 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.354 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.342)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.349 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.342)

- **PATRÓN** `libro_liquidez` > `3525.4286` → IC=+0.359 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3525.4286 (IC base=+0.342)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.345 (n=172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.347)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.396 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.347)

- **PATRÓN** `drift_60min` |x|≤ `0.1514` → IC=+0.356 (n=172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1514 (IC base=+0.347)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.356 (n=130)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.347)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1177` → IC=+0.422 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1177 (IC base=+0.347)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.367 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.347)

- **PATRÓN** `ibs_15` > `0.8166` → IC=+0.378 (n=195)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8166 (IC base=+0.347)

- **PATRÓN** `dist_vwap_pct` > `0.2515` → IC=+0.406 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2515 (IC base=+0.347)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.381` → IC=+0.355 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.381 (IC base=+0.347)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.472` → IC=+0.358 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.472 (IC base=+0.347)

- **PATRÓN** `libro_liquidez` > `10218.4138` → IC=+0.386 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10218.4138 (IC base=+0.347)

- **PATRÓN** `ballena_activa_n` < `585.0` → IC=+0.406 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 585.0 (IC base=+0.347)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.330 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.374 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.338 (n=134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0624` → IC=+0.343 (n=151)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0624 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2262` → IC=+0.371 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2262 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.349 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.389 (n=151)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.337 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` < `0.1075` → IC=+0.351 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1075 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.361 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3553.0968` → IC=+0.354 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3553.0968 (IC base=+0.333)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.013` → IC=-0.209 (n=572)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=1719)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.181 (n=735)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1556)

- **FILTRO** `libro_liquidez` < `3852.5505` → IC=-0.126 (n=1512)

  - _Acción_: SKIP cuando `libro_liquidez` < 3852.5505
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=779)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.264 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.057)

- **PATRÓN** `ibs_15` > `0.6235` → IC=+0.269 (n=565)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6235 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.176 (n=140)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.4333 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` < `0.1109` → IC=+0.185 (n=344)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1109 (IC base=-0.057)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1167` → IC=+0.235 (n=889)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1167 (IC base=-0.043)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1825` → IC=+0.245 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1825 (IC base=-0.043)

- **PATRÓN** `ibs_15` < `0.3571` → IC=+0.281 (n=1334)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3571 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` > `0.6509` → IC=+0.265 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6509 (IC base=-0.043)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.213 (n=347)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=1044)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.231 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=932)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.209 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=511)

- **FILTRO** `sigma_ewma_delta_pct` > `19.873` → IC=-0.244 (n=248)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.873
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=1143)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.164 (n=126)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0028 (IC base=+0.082)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.370 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.082)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.336 (n=138)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1073` → IC=+0.286 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1073 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.5498` → IC=+0.288 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5498 (IC base=+0.082)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6556` → IC=-0.206 (n=90)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6556
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=271)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=344)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.145 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0067 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.172 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0041 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0768` → IC=+0.221 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0768 (IC base=+0.142)

- **PATRÓN** `drift_15min` |x|≤ `0.4631` → IC=+0.156 (n=120)

  - _Acción_: Kelly boost +0.78€ cuando `drift_15min` |x|≤ 0.4631 (IC base=+0.142)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3059` → IC=+0.243 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3059 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.190 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.142)

- **PATRÓN** `ibs_15` > `0.6556` → IC=+0.258 (n=271)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6556 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1047` → IC=+0.177 (n=193)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1047 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.902` → IC=+0.153 (n=292)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 18.902 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=344)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.196 (n=123)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.244 (n=549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.226)

- **PATRÓN** `drift_15min` |x|≤ `0.7722` → IC=+0.236 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7722 (IC base=+0.226)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1963` → IC=+0.249 (n=249)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1963 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.233 (n=372)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.226)

- **PATRÓN** `ibs_15` < `0.2722` → IC=+0.286 (n=483)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2722 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.7494` → IC=+0.273 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7494 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.065` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.065 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.254` → IC=+0.228 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.254 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `3546.5572` → IC=+0.228 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3546.5572 (IC base=+0.226)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.227 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 157.0 (IC base=+0.226)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0501` → IC=-0.159 (n=412)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0501
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=138)

- **FILTRO** `drift_60min` |x|> `0.1657` → IC=-0.218 (n=186)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1657
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=364)

- **FILTRO** `drift_15min` |x|> `0.8849` → IC=-0.248 (n=137)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8849
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=413)

- **FILTRO** `sigma_ewma_delta_pct` > `18.09` → IC=-0.137 (n=287)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.09
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2295)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.156)

- **PATRÓN** `dist_vwap_pct` < `0.1511` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.1511 (IC base=-0.156)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1148` → IC=+0.220 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1148 (IC base=-0.046)

- **PATRÓN** `ibs_15` < `0.3659` → IC=+0.252 (n=260)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3659 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` > `0.6912` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6912 (IC base=-0.046)

- **PATRÓN** `dist_vwap_pct` < `0.1738` → IC=+0.206 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1738 (IC base=-0.046)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.263 (n=344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=345)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=178)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=511)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1081` → IC=+0.343 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1081 (IC base=-0.047)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.308 (n=379)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.047)

- **PATRÓN** `dist_vwap_pct` > `1.0781` → IC=+0.391 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0781 (IC base=-0.047)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.8434` → IC=-0.167 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8434
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.139 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0065 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.260 (n=23)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.1457` → IC=+0.123 (n=59)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` > 0.1457 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.100)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.8434` → IC=-0.167 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8434
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.139 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0065 (IC base=+0.100)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.260 (n=23)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.5868` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `drift_15min` |x|≤ 0.5868 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.1457` → IC=+0.123 (n=59)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` > 0.1457 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1511` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1511 (IC base=+0.100)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.292 (n=383)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.302 (n=261)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.320 (n=192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1425` → IC=+0.297 (n=383)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1425 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1083` → IC=+0.348 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1083 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.312 (n=595)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8378` → IC=+0.330 (n=574)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8378 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2738` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2738 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.332 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `14264.9886` → IC=+0.309 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14264.9886 (IC base=+0.293)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.297 (n=215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.304 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.327 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.246` → IC=+0.291 (n=108)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.246 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1424` → IC=+0.325 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1424 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.304 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8255` → IC=+0.306 (n=322)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8255 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2631` → IC=+0.350 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2631 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.353 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `15946.6772` → IC=+0.327 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15946.6772 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.308 (n=253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.302)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.303 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.314 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.302)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1466` → IC=+0.318 (n=168)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1466 (IC base=+0.302)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.347 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.329 (n=244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.302)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.346 (n=252)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.302)

- **PATRÓN** `dist_vwap_pct` > `0.6145` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6145 (IC base=+0.302)

- **PATRÓN** `dist_vwap_pct` < `0.454` → IC=+0.302 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.454 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.619` → IC=+0.331 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.619 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` < `19.173` → IC=+0.302 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 19.173 (IC base=+0.302)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.310 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.302)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.302 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.302)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0841` → IC=-0.276 (n=65)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0841
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=197)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.247 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=173)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1869` → IC=-0.123 (n=75)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1869
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=75)

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
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

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

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.239 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `76.962` → IC=+0.151 (n=239)

  - _Acción_: Kelly boost +0.76€ cuando `T_h` > 76.962 (IC base=+0.147)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.327 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.147)

- **PATRÓN** `T_h` > `145.8408` → IC=+0.407 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8408 (IC base=+0.349)

- **PATRÓN** `ratio` > `1.0104` → IC=+0.386 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0104 (IC base=+0.349)

### WEEKLY_PRICE#BTC
- **FILTRO** `ratio` > `0.9933` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `ratio` > 0.9933
  - _Potencial_: sin este filtro IC_bueno=+0.290 (n=79)

- **PATRÓN** `T_h` > `144.522` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `T_h` > 144.522 (IC base=+0.110)

- **PATRÓN** `ratio` < `0.9933` → IC=+0.290 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.110)

- **PATRÓN** `T_h` > `87.9969` → IC=+0.311 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9969 (IC base=+0.304)

- **PATRÓN** `ratio` > `1.0057` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0057 (IC base=+0.304)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `87.9936` → IC=+0.217 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9936 (IC base=+0.199)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.395 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.199)

- **PATRÓN** `T_h` > `97.926` → IC=+0.354 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 97.926 (IC base=+0.331)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.389 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.331)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1062` → IC=+0.450 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1062 (IC base=+0.404)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6192 sube el IC de +0.188 a +0.265 en UPDOWN_GBM#15min (n=1260). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.206 a +0.267 en UPDOWN_GBM#BTC#15min (n=307). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6381 sube el IC de +0.143 a +0.234 en UPDOWN_GBM#ETH#15min (n=295). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.150 a +0.245 en UPDOWN_GBM#SOL#15min (n=163). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.190 a +0.283 en UPDOWN_GBM#XRP#15min (n=349). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1154 sube el IC de +0.042 a +0.168 en UPDOWN_GBM#XRP#15min (n=389). Ya aplicado como kelly_boost=+0.84€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6235 sube el IC de -0.057 a +0.269 en UPDOWN_GBM_15M_TARDIO (n=565). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3571 sube el IC de -0.043 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1334). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.082 a +0.336 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=138). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6556 sube el IC de +0.142 a +0.258 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=271). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2722 sube el IC de +0.226 a +0.286 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=483). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.156 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3659 sube el IC de -0.046 a +0.252 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=260). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.047 a +0.308 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=379). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8378 sube el IC de +0.293 a +0.330 en UPDOWN_GBM_IBS_ALTO (n=574). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8255 sube el IC de +0.284 a +0.306 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=322). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.302 a +0.346 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=252). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.342 a +0.382 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=346). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8166 sube el IC de +0.347 a +0.378 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=195). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.333 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=151). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1195 | +0.083 | +140.26€ | 2 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1195 | +0.083 | +140.26€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 867 | +0.090 | +116.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 867 | +0.090 | +116.91€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 242 | +0.045 | +4.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 242 | +0.045 | +4.70€ | 4 | 5 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 22188 | -0.093 | -3099.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1328 | -0.041 | -195.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 20860 | -0.097 | -2904.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3418 | -0.091 | -569.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3418 | -0.091 | -569.07€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1328 | -0.041 | -195.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1328 | -0.041 | -195.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 6357 | -0.040 | -613.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 6357 | -0.040 | -613.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5869 | -0.094 | -468.12€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5869 | -0.094 | -468.12€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4842 | -0.175 | -1093.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4842 | -0.175 | -1093.00€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 14296 | -0.036 | +4172.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3789 | -0.003 | +1833.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 10507 | -0.048 | +2338.40€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 14296 | -0.036 | +4172.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3789 | -0.003 | +1833.66€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 10507 | -0.048 | +2338.40€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1287 | -0.097 | -161.11€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 129 | -0.042 | -12.47€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1158 | -0.103 | -148.64€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 725 | -0.086 | -84.87€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 105 | -0.033 | -7.25€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 620 | -0.095 | -77.63€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 372 | -0.126 | -64.15€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 348 | -0.129 | -58.92€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 49 | -0.147 | -2.57€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 49 | -0.147 | -2.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 80745 | +0.113 | -4111.25€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 12478 | +0.185 | -347.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 313 | -0.113 | -47.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 62504 | +0.100 | -3535.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5450 | +0.111 | -180.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 10408 | +0.097 | -941.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 41 | -0.151 | -1.09€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 10352 | +0.099 | -929.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 16332 | +0.132 | -309.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3860 | +0.203 | -106.70€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 10358 | +0.111 | -171.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2072 | +0.111 | -8.85€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 10448 | +0.088 | -1015.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 48 | -0.060 | -2.83€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 10385 | +0.089 | -1001.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 17253 | +0.124 | -338.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4823 | +0.175 | -60.58€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 10457 | +0.106 | -215.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1961 | +0.098 | -53.97€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 15879 | +0.116 | -902.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3664 | +0.188 | -185.90€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 216 | -0.073 | +6.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 10582 | +0.093 | -605.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1417 | +0.129 | -117.62€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#XRP | 10425 | +0.103 | -603.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 42 | -0.023 | +9.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 10370 | +0.103 | -612.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 12771 | +0.192 | -833.37€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 12771 | +0.192 | -833.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3106 | +0.168 | -332.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3106 | +0.168 | -332.13€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 833 | +0.196 | +8.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 833 | +0.196 | +8.37€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3037 | +0.182 | -258.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3037 | +0.182 | -258.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2729 | +0.239 | -77.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2729 | +0.239 | -77.90€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2987 | +0.192 | -186.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2987 | +0.192 | -186.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 598 | +0.437 | -7.33€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 598 | +0.437 | -7.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 227 | +0.439 | -1.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 227 | +0.439 | -1.24€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 227 | +0.443 | +1.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 227 | +0.443 | +1.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 136 | +0.413 | -6.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 136 | +0.413 | -6.56€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 43756 | +0.196 | -3539.62€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 43756 | +0.196 | -3539.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 7607 | +0.172 | -933.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 7607 | +0.172 | -933.44€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6958 | +0.224 | -252.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6958 | +0.224 | -252.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 7571 | +0.172 | -929.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 7571 | +0.172 | -929.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 7049 | +0.218 | -284.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 7049 | +0.218 | -284.46€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 7227 | +0.204 | -479.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 7227 | +0.204 | -479.03€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 7344 | +0.192 | -660.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 7344 | +0.192 | -660.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 16417 | +0.122 | +245.78€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 16417 | +0.122 | +245.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 8145 | +0.126 | +174.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 8145 | +0.126 | +174.13€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 8272 | +0.118 | +71.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 8272 | +0.118 | +71.64€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1317 | +0.287 | -25.89€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1317 | +0.287 | -25.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 584 | +0.270 | -26.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 584 | +0.270 | -26.82€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 631 | +0.293 | +0.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 631 | +0.293 | +0.32€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 102 | +0.337 | +0.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 102 | +0.337 | +0.62€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 577 | +0.434 | -3.96€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 577 | +0.434 | -3.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 270 | +0.434 | -2.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 270 | +0.434 | -2.39€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 267 | +0.437 | -1.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 267 | +0.437 | -1.45€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 40 | +0.381 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 40 | +0.381 | -0.11€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 937 | +0.075 | -37.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 326 | +0.064 | -24.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 611 | +0.081 | -13.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 55 | +0.132 | +4.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 736 | +0.083 | -14.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 125 | +0.091 | -1.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 611 | +0.081 | -13.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 146 | +0.013 | -27.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 146 | +0.013 | -27.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 29555 | +0.099 | -866.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2472 | +0.090 | +19.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 27083 | +0.099 | -886.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 16744 | +0.103 | -245.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2472 | +0.090 | +19.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 14272 | +0.105 | -265.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 5316 | +0.113 | +18.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 5316 | +0.113 | +18.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 7495 | +0.080 | -640.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 7495 | +0.080 | -640.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 752 | +0.235 | -90.03€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 752 | +0.235 | -90.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 752 | +0.235 | -90.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 752 | +0.235 | -90.03€ | 1 | 4 |
| ✅ GBM_LATE_15M | 21601 | +0.077 | +9797.63€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 21601 | +0.077 | +9797.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3558 | +0.193 | +2584.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3558 | +0.193 | +2584.90€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 3205 | +0.172 | +2120.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3205 | +0.172 | +2120.67€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 3696 | +0.200 | +2779.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3696 | +0.200 | +2779.87€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 3238 | +0.009 | +529.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3238 | +0.009 | +529.86€ | 1 | 14 |
| ✅ GBM_LATE_15M#SOL | 3147 | -0.039 | +655.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3147 | -0.039 | +655.75€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 4757 | -0.047 | +1126.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4757 | -0.047 | +1126.57€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 22741 | +0.081 | +11354.86€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 22741 | +0.081 | +11354.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 4250 | +0.014 | +2024.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 4250 | +0.014 | +2024.24€ | 2 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4787 | +0.008 | +913.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4787 | +0.008 | +913.34€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3217 | +0.262 | +3232.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3217 | +0.262 | +3232.01€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3628 | -0.007 | +551.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3628 | -0.007 | +551.22€ | 2 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3722 | +0.017 | +1330.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3722 | +0.017 | +1330.98€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3137 | +0.272 | +3303.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3137 | +0.272 | +3303.07€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 17469 | +0.168 | +12816.88€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 17469 | +0.168 | +12816.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2604 | +0.208 | +2080.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2604 | +0.208 | +2080.19€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2776 | +0.151 | +1954.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2776 | +0.151 | +1954.12€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2706 | +0.208 | +2151.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2706 | +0.208 | +2151.23€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2912 | +0.138 | +1967.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2912 | +0.138 | +1967.30€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3284 | +0.113 | +2169.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3284 | +0.113 | +2169.35€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3187 | +0.202 | +2494.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3187 | +0.202 | +2494.70€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 4405 | +0.125 | +1799.66€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 4405 | +0.125 | +1799.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 183 | +0.122 | +78.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 183 | +0.122 | +78.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1221 | +0.121 | +517.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1221 | +0.121 | +517.21€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1199 | +0.146 | +547.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1199 | +0.146 | +547.66€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 931 | +0.087 | +255.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 931 | +0.087 | +255.14€ | 1 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 503 | +0.136 | +218.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 503 | +0.136 | +218.58€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 21658 | +0.173 | +15754.54€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 21658 | +0.173 | +15754.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 3400 | +0.219 | +2843.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 3400 | +0.219 | +2843.78€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 3401 | +0.148 | +2191.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 3401 | +0.148 | +2191.87€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3510 | +0.226 | +3033.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3510 | +0.226 | +3033.56€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 3489 | +0.137 | +2268.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 3489 | +0.137 | +2268.08€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3805 | +0.107 | +2279.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3805 | +0.107 | +2279.56€ | 1 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4053 | +0.202 | +3137.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4053 | +0.202 | +3137.67€ | 0 | 26 |
| ✅ GBM_LATE_5M | 6212 | +0.140 | +3374.60€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 6212 | +0.140 | +3374.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 589 | +0.185 | +410.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 589 | +0.185 | +410.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1626 | +0.138 | +1000.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1626 | +0.138 | +1000.11€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 888 | +0.171 | +564.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 888 | +0.171 | +564.16€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 1959 | +0.146 | +1059.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1959 | +0.146 | +1059.38€ | 0 | 31 |
| ✅ GBM_LATE_5M#SOL | 335 | +0.019 | +31.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 335 | +0.019 | +31.23€ | 1 | 2 |
| ✅ GBM_LATE_5M#XRP | 815 | +0.113 | +308.96€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 815 | +0.113 | +308.96€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1385 | +0.068 | +637.09€ | 3 | 15 |
| ✅ GBM_LATE_60M#60min | 1385 | +0.068 | +637.09€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 497 | +0.087 | +215.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 497 | +0.087 | +215.11€ | 0 | 16 |
| ✅ GBM_LATE_60M#ETH | 463 | +0.072 | +250.54€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 463 | +0.072 | +250.54€ | 1 | 16 |
| ✅ GBM_LATE_60M#SOL | 425 | +0.041 | +171.43€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 425 | +0.041 | +171.43€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 316 | -0.261 | -21.93€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 316 | -0.261 | -21.93€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 118 | -0.217 | -7.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 118 | -0.217 | -7.46€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 106 | -0.278 | -9.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 106 | -0.278 | -9.71€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 92 | -0.287 | -4.76€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 92 | -0.287 | -4.76€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 623 | +0.057 | +120.38€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 623 | +0.057 | +120.38€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 248 | +0.048 | +40.26€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 248 | +0.048 | +40.26€ | 3 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 182 | +0.033 | +1.45€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 182 | +0.033 | +1.45€ | 4 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 193 | +0.090 | +78.66€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 193 | +0.090 | +78.66€ | 2 | 15 |
| ✅ LATE_WINDOW_5MIN | 75 | +0.253 | +53.23€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 75 | +0.253 | +53.23€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 75 | +0.253 | +53.23€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 75 | +0.253 | +53.23€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1572 | +0.104 | +451.12€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1572 | +0.104 | +451.12€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1572 | +0.104 | +451.12€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1572 | +0.104 | +451.12€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 362 | -0.082 | -34.11€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 362 | -0.082 | -34.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 93 | -0.068 | -5.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 93 | -0.068 | -5.97€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 121 | -0.020 | -3.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 121 | -0.020 | -3.83€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1607 | -0.002 | -5.83€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1607 | -0.002 | -5.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 173 | -0.020 | +1.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 173 | -0.020 | +1.17€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 102 | -0.048 | -5.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 102 | -0.048 | -5.98€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 689 | +0.024 | +18.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 689 | +0.024 | +18.45€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 462 | -0.006 | -8.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 462 | -0.006 | -8.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 106 | -0.056 | -6.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 106 | -0.056 | -6.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M | 952 | -0.048 | -29.26€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 952 | -0.048 | -29.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 278 | -0.050 | -14.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 278 | -0.050 | -14.25€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 308 | -0.035 | -4.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 308 | -0.035 | -4.35€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 366 | -0.057 | -10.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 366 | -0.057 | -10.67€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 13832 | -0.012 | -208.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 13832 | -0.012 | -208.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2652 | -0.025 | -62.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2652 | -0.025 | -62.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2972 | -0.016 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2972 | -0.016 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 24200 | -0.009 | +1072.33€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 24200 | -0.009 | +1072.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 4229 | +0.013 | +542.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 4229 | +0.013 | +542.48€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3852 | -0.026 | -28.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3852 | -0.026 | -28.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 4249 | +0.008 | +331.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 4249 | +0.008 | +331.91€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3631 | -0.047 | -98.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3631 | -0.047 | -98.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4052 | -0.012 | +166.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4052 | -0.012 | +166.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 4187 | +0.002 | +158.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 4187 | +0.002 | +158.84€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5289 | -0.050 | -134.13€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5289 | -0.050 | -134.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1202 | +0.001 | -15.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1202 | +0.001 | -15.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1223 | -0.069 | -33.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1223 | -0.069 | -33.21€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 43 | -0.122 | -5.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 515 | -0.133 | -30.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 515 | -0.133 | -30.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1460 | -0.064 | -24.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1460 | -0.064 | -24.81€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 846 | -0.015 | -25.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 846 | -0.015 | -25.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3340 | +0.004 | -3.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3340 | +0.004 | -3.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 187 | +0.008 | -2.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 187 | +0.008 | -2.15€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 136 | +0.000 | -1.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 136 | +0.000 | -1.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1314 | +0.007 | +7.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1314 | +0.007 | +7.09€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 187 | -0.008 | -5.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 62086 | -0.074 | +1365.86€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 62086 | -0.074 | +1365.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 10464 | -0.081 | +608.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 10464 | -0.081 | +608.67€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 9664 | -0.091 | -386.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 9664 | -0.091 | -386.15€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 10518 | -0.070 | +561.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 10518 | -0.070 | +561.62€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 9191 | -0.094 | -252.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 9191 | -0.094 | -252.69€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 11434 | -0.049 | +341.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 11434 | -0.049 | +341.01€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 10815 | -0.063 | +493.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 10815 | -0.063 | +493.40€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6832 | -0.023 | -102.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6832 | -0.023 | -102.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1565 | -0.023 | -5.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1565 | -0.023 | -5.29€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1519 | -0.017 | -5.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1519 | -0.017 | -5.07€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1013 | -0.040 | -17.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1013 | -0.040 | -17.42€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1031 | +0.113 | +361.80€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 895 | +0.121 | +349.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 208 | +0.138 | +103.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 208 | +0.138 | +103.81€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#DOGE | 179 | +0.091 | +39.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 179 | +0.091 | +39.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 180 | +0.104 | +63.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 180 | +0.104 | +63.57€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 157 | +0.148 | +81.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 157 | +0.148 | +81.19€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 171 | +0.118 | +60.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 171 | +0.118 | +60.79€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 489 | -0.085 | -13.99€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 216 | -0.128 | -36.99€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 174 | -0.165 | -39.62€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 174 | -0.074 | +5.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 132 | -0.082 | -1.42€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 99 | -0.005 | +17.86€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 79 | -0.018 | +11.76€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 385 | -0.107 | -29.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 581 | -0.217 | -47.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 240 | -0.198 | -33.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 208 | -0.191 | -31.31€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 205 | -0.239 | -24.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 178 | -0.250 | -29.07€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 136 | -0.210 | +11.34€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 122 | -0.210 | +8.28€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 508 | -0.218 | -52.10€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 218 | +0.400 | +164.89€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#BTC | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 28 | +0.033 | -4.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 54 | +0.375 | +44.07€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 54 | +0.375 | +44.07€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 136 | +0.478 | +125.57€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 136 | +0.478 | +125.57€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#sniper | 218 | +0.400 | +164.89€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 432 | +0.025 | +11.01€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 432 | +0.025 | +11.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 203 | +0.022 | +2.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 203 | +0.022 | +2.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 26 | +0.107 | +4.41€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 47 | -0.031 | -4.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 47 | -0.031 | -4.66€ | 1 | 0 |
| ✅ STREAK_FADE_15M#XRP | 156 | +0.032 | +8.49€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 156 | +0.032 | +8.49€ | 1 | 2 |
| ✅ STREAK_FADE_5M | 2561 | -0.025 | -112.66€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2561 | -0.025 | -112.66€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 564 | -0.023 | -23.35€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 564 | -0.023 | -23.35€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 153 | -0.042 | -13.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 153 | -0.042 | -13.91€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1040 | -0.028 | -48.45€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1040 | -0.028 | -48.45€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 65 | -0.037 | -4.30€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 65 | -0.037 | -4.30€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 37 | -0.090 | -3.93€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 37 | -0.090 | -3.93€ | 1 | 0 |
| ✅ STREAK_FADE_60M#SOL | 28 | +0.033 | -0.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 28 | +0.033 | -0.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6943 | +0.025 | +115.05€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6943 | +0.025 | +115.05€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2121 | +0.021 | +20.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1474 | +0.034 | +43.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1474 | +0.034 | +43.42€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2068 | +0.016 | +10.70€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2068 | +0.016 | +10.70€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1280 | +0.034 | +40.02€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1280 | +0.034 | +40.02€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 6472 | +0.010 | -51.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 6472 | +0.010 | -51.79€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2568 | +0.017 | -5.19€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2568 | +0.017 | -5.19€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2551 | +0.011 | -17.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2551 | +0.011 | -17.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1353 | -0.006 | -29.06€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1353 | -0.006 | -29.06€ | 2 | 0 |
| ✅ UPDOWN_GBM | 28939 | +0.030 | +1707.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 7876 | +0.060 | +1336.40€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1083 | +0.005 | +8.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 18103 | +0.022 | +349.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1762 | +0.004 | +9.92€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2649 | +0.076 | +303.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 391 | +0.151 | +155.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 2239 | +0.064 | +148.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 5306 | +0.032 | +354.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 974 | +0.077 | +219.22€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 304 | +0.023 | +7.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 3202 | +0.029 | +115.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 782 | +0.000 | +10.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 44 | -0.109 | +1.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 3438 | +0.035 | +163.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 345 | +0.143 | +127.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3077 | +0.023 | +36.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 6085 | +0.018 | +244.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2104 | +0.045 | +232.40€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 292 | +0.007 | +7.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 3035 | +0.004 | +2.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 617 | +0.002 | -2.62€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 37 | -0.141 | +4.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 7187 | +0.015 | +166.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2043 | +0.019 | +110.88€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 286 | -0.007 | -2.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 4463 | +0.016 | +57.50€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 363 | +0.015 | +1.86€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 32 | -0.147 | -1.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 4272 | +0.038 | +476.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2019 | +0.076 | +490.53€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 166 | -0.006 | -2.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2087 | +0.005 | -11.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 113 | -0.135 | +4.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 461 | +0.342 | +144.20€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 461 | +0.342 | +144.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 260 | +0.347 | +79.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 260 | +0.347 | +79.85€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 201 | +0.333 | +64.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 201 | +0.333 | +64.35€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 9994 | -0.046 | +2056.97€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 9994 | -0.046 | +2056.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 546 | -0.044 | +339.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 546 | -0.044 | +339.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1891 | -0.126 | +37.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1891 | -0.126 | +37.63€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 209 | +0.159 | +119.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 209 | +0.159 | +119.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1092 | +0.198 | +621.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1092 | +0.198 | +621.33€ | 2 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3132 | -0.065 | +446.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3132 | -0.065 | +446.55€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3124 | -0.078 | +492.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3124 | -0.078 | +492.35€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 114 | +0.069 | +16.41€ | 1 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 114 | +0.069 | +16.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 114 | +0.069 | +16.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 114 | +0.069 | +16.41€ | 1 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 765 | +0.293 | +627.67€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 765 | +0.293 | +627.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 429 | +0.284 | +328.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 429 | +0.284 | +328.78€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 336 | +0.302 | +298.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 336 | +0.302 | +298.89€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 691 | -0.107 | -79.24€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 691 | -0.107 | -79.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 188 | -0.068 | -12.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 188 | -0.068 | -12.06€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 67 | -0.167 | -9.09€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 67 | -0.167 | -9.09€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 58 | -0.200 | -8.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 58 | -0.200 | -8.54€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2049 | +0.305 | +1065.34€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 687 | +0.252 | +108.95€ | 1 | 4 |
| ✅ WEEKLY_PRICE#ETH | 746 | +0.295 | +321.14€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 616 | +0.375 | +635.25€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.059) — sin ventaja clara. oversold(IBS<0.3): IC=+0.049 n=10145 | neutral: IC=+0.027 n=10951 | overbought(IBS>0.7): IC=+0.086 n=10402
  - _Datos_: n=32649 IC=+0.054 PNL=+3973.91€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 484 celda(s) pasan gate riguroso completo de 2093 evaluadas (n>=40) y 3080 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.019 < 0.08 — monitorear
  - _Datos_: n=2038 IC=+0.019 PNL=+110.37€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=746/15 IC=+0.295 PNL=+321.14€ | BTC: n=687/15 IC=+0.252 PNL=+108.95€ | SOL: n=616/15 IC=+0.375 PNL=+635.25€

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
  - _Estado_: 28794 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.099 n=220/60 | contraria IC=+0.140 n=212 | gap=-0.041 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=252, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 156 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=616/40 IC=+0.003 PNL=-2.11€ | BTC#60min: n=780/40 IC=+0.000 PNL=+10.01€ | SOL#60min: n=361/40 IC=+0.015 PNL=+1.84€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.053 n=284539 | tras_1loss IC=+0.073 n=221912 | tras_2loss IC=+0.042 n=94628/40 | gap=+0.011 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.015 n=3161 | contrario_BTC IC=+0.017 n=2789/40 | gap=+0.002 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.209 > 0.08 con n=242 PNL=+185.12€
  - _Datos_: n=242 IC=+0.209 PNL=+185.12€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.215 > 0.08 con n=307 PNL=+221.41€
  - _Datos_: n=307 IC=+0.215 PNL=+221.41€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.243 > 0.08 con n=33 PNL=+24.82€
  - _Datos_: n=33 IC=+0.243 PNL=+24.82€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.343 > 0.1 con n=1707 PNL=+1047.44€
  - _Datos_: n=1707 IC=+0.343 PNL=+1047.44€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=221 IC=+0.079 PNL=+29.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=221 IC=+0.079 PNL=+29.84€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=46 IC=+0.188 PNL=+30.45€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=46 IC=+0.188 PNL=+30.45€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=27653 IC=+0.029 PNL=+1607.79€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=27653 IC=+0.029 PNL=+1607.79€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 3/15 ops en el filtro definido (IC actual=+0.045 PNL=+5.14€)
  - _Datos_: n=3 IC=+0.045 PNL=+5.14€

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
  - _Estado_: n=1287 IC=+0.011 PNL=+2.67€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1287 IC=+0.011 PNL=+2.67€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=470 IC=-0.013 PNL=+7.08€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=470 IC=-0.013 PNL=+7.08€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=404 IC=+0.020 PNL=+22.97€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=404 IC=+0.020 PNL=+22.97€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.187 > 0.1 con n=1674 PNL=+1040.26€
  - _Datos_: n=1674 IC=+0.187 PNL=+1040.26€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=872 IC=+0.047 PNL=+67.72€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=872 IC=+0.047 PNL=+67.72€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=972 IC=+0.077 PNL=+219.28€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=972 IC=+0.077 PNL=+219.28€

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
  - _Estado_: n=4521 IC=+0.064 PNL=+926.50€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4521 IC=+0.064 PNL=+926.50€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=125 IC=-0.232 PNL=-3.43€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=125 IC=-0.232 PNL=-3.43€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=209 IC=-0.012 PNL=+13.39€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=209 IC=-0.012 PNL=+13.39€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=424 IC=+0.019 PNL=+36.65€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=424 IC=+0.019 PNL=+36.65€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=35 IC=+0.013 PNL=-0.13€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=35 IC=+0.013 PNL=-0.13€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=3829 IC=-0.007 PNL=-24.25€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3829 IC=-0.007 PNL=-24.25€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.176 > 0.08 con n=66 PNL=+18.24€
  - _Datos_: n=66 IC=+0.176 PNL=+18.24€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.253 n=75) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=75 IC=+0.253 PNL=+53.23€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=5619 IC=+0.027 PNL=+280.37€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=5619 IC=+0.027 PNL=+280.37€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=1804 IC=+0.049 PNL=+212.62€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1804 IC=+0.049 PNL=+212.62€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=315 PNL=+96.86€
  - _Datos_: n=315 IC=+0.112 PNL=+96.86€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.138 > 0.08 con n=484 PNL=+117.73€
  - _Datos_: n=484 IC=+0.138 PNL=+117.73€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.08 con n=369 PNL=+182.73€
  - _Datos_: n=369 IC=+0.125 PNL=+182.73€

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
  - _Estado_: n=4060 IC=+0.035 PNL=+275.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4060 IC=+0.035 PNL=+275.44€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.02 con n=586 PNL=+243.67€
  - _Datos_: n=586 IC=+0.131 PNL=+243.67€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.453 > 0.1 con n=1014 PNL=+1032.88€
  - _Datos_: n=1014 IC=+0.453 PNL=+1032.88€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=9745 IC=+0.053 PNL=+1201.73€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=9745 IC=+0.053 PNL=+1201.73€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.200 > 0.1 con n=2660 PNL=+1438.63€
  - _Datos_: n=2660 IC=+0.200 PNL=+1438.63€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.181 < -0.1 con n=186 PNL=+8.71€
  - _Datos_: n=186 IC=-0.181 PNL=+8.71€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1551 IC=+0.042 PNL=+161.18€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1551 IC=+0.042 PNL=+161.18€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=61 IC=-0.119 PNL=+5.27€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=61 IC=-0.119 PNL=+5.27€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.140 > 0.1 con n=312 PNL=+102.24€
  - _Datos_: n=312 IC=+0.140 PNL=+102.24€

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
  - _Estado_: n=14849 IC=-0.140 PNL=+874.04€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=14849 IC=-0.140 PNL=+874.04€

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
  - _Estado_: n=1647 IC=+0.134 PNL=+846.36€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1647 IC=+0.134 PNL=+846.36€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.190 > 0.08 con n=1635 PNL=+1027.63€
  - _Datos_: n=1635 IC=+0.190 PNL=+1027.63€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=2967 IC=+0.016 PNL=+91.27€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2967 IC=+0.016 PNL=+91.27€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.082 > 0.08 con n=1722 PNL=+877.25€
  - _Datos_: n=1722 IC=+0.082 PNL=+877.25€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.205 > 0.08 con n=408 PNL=+204.31€
  - _Datos_: n=408 IC=+0.205 PNL=+204.31€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.239 < -0.1 con n=1490 PNL=-187.40€
  - _Datos_: n=1490 IC=-0.239 PNL=-187.40€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=4341 IC=+0.154 PNL=+2694.74€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=4341 IC=+0.154 PNL=+2694.74€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.08 con n=70 PNL=+31.20€
  - _Datos_: n=70 IC=+0.125 PNL=+31.20€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=1701 IC=+0.052 PNL=+382.72€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1701 IC=+0.052 PNL=+382.72€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=1538 PNL=+996.10€
  - _Datos_: n=1538 IC=+0.175 PNL=+996.10€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=2501 IC=-0.037 PNL=+588.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2501 IC=-0.037 PNL=+588.11€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.084 > 0.08 con n=491 PNL=-54.26€
  - _Datos_: n=491 IC=+0.084 PNL=-54.26€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.233 > 0.08 con n=2930 PNL=-276.12€
  - _Datos_: n=2930 IC=+0.233 PNL=-276.12€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 32/40 ops en el filtro definido (IC actual=-0.029 PNL=+3.53€)
  - _Datos_: n=32 IC=-0.029 PNL=+3.53€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.094 n=815) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=815 IC=+0.094 PNL=+201.27€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.346 > 0.08 con n=213 PNL=+85.07€
  - _Datos_: n=213 IC=+0.346 PNL=+85.07€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=406) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=406 IC=+0.412 PNL=+570.24€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=7597 IC=+0.172 PNL=-931.41€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=7597 IC=+0.172 PNL=-931.41€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.219 > 0.1 con n=112 PNL=+72.18€
  - _Datos_: n=112 IC=+0.219 PNL=+72.18€
