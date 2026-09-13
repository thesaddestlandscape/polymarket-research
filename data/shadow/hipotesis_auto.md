# Hipótesis automáticas — 2026-09-13 09:59 UTC
_Generado por shadow_postmortem.py sobre 418078 resoluciones (PNL=+44163.37€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.385` → IC=-0.150 (n=195)

  - _Acción_: SKIP cuando `py_entrada` < 0.385
  - _Potencial_: sin este filtro IC_bueno=+0.242 (n=398)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=398)

- **PATRÓN** `py_entrada` > `0.385` → IC=+0.242 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.385 (IC base=+0.113)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.206 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.113)

- **PATRÓN** `banda_hit_calibrado` > `0.8059` → IC=+0.266 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8059 (IC base=+0.113)

- **PATRÓN** `banda_z` > `10.736` → IC=+0.222 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.736 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.130 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 11.0 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=469)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.113)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=398)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.131 (n=128)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 98.0 (IC base=+0.037)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.375` → IC=-0.129 (n=141)

  - _Acción_: SKIP cuando `py_entrada` < 0.375
  - _Potencial_: sin este filtro IC_bueno=+0.232 (n=315)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=288)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=313)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.232 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.120)

- **PATRÓN** `n_total_lado` > `58.0` → IC=+0.192 (n=232)

  - _Acción_: Kelly boost +0.96€ cuando `n_total_lado` > 58.0 (IC base=+0.120)

- **PATRÓN** `banda_hit_calibrado` > `0.8049` → IC=+0.265 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8049 (IC base=+0.120)

- **PATRÓN** `banda_z` > `11.589` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.589 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=385)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 87.0 (IC base=+0.032)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.335` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` < 0.335
  - _Potencial_: sin este filtro IC_bueno=+0.207 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=101)

- **FILTRO** `py_entrada` > `0.845` → IC=-0.393 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.845
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=80)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=90)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.132 (n=74)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.495 (IC base=-0.018)

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
- **FILTRO** `restante_s_al_confirmar` < `146.32` → IC=-0.262 (n=5328)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.32
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=15988)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `n_ballenas` < `4.0` → IC=-0.126 (n=1842)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=1143)

- **FILTRO** `restante_s_al_confirmar` < `141.13` → IC=-0.281 (n=746)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.13
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=2239)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `133.27` → IC=-0.288 (n=678)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.27
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2034)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `144.43` → IC=-0.161 (n=1377)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 144.43
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=4132)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `157.46` → IC=-0.254 (n=1225)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.46
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3677)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `156.1` → IC=-0.347 (n=1342)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.1
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=2727)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.31` → IC=-0.295 (n=42)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=137)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.167 (n=79)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=83)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=85)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` > 0.52 (IC base=+0.025)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

- **FILTRO** `py_entrada` > `0.3` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=27)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.7` → IC=+0.199 (n=9929)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=2694)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `11005.6828` → IC=+0.194 (n=861)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 11005.6828 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=8111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=9809)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.246 (n=7261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.174 (n=5323)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `6971.4958` → IC=+0.176 (n=1689)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 6971.4958 (IC base=+0.137)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1256)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.355 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=1548)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `14487.9883` → IC=+0.212 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14487.9883 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=1140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.214 (n=1255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.270 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1609)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `12668.1396` → IC=+0.207 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12668.1396 (IC base=+0.205)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.178 (n=265)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.615 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=280)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `4690.1012` → IC=+0.152 (n=225)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4690.1012 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.165 (n=539)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.425 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=535)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3857.7273` → IC=+0.163 (n=413)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3857.7273 (IC base=+0.136)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=2173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=1849)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.135)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.330 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=494)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` < `0.305` → IC=+0.329 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.305 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.239 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `4382.6662` → IC=+0.245 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4382.6662 (IC base=+0.239)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.137 (n=452)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.225 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=596)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `1512.3969` → IC=+0.149 (n=448)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1512.3969 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=146)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.085)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.213 (n=489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.197 (n=1013)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 12.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.426 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.187 (n=465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.279 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.187 (n=1056)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.03 (IC base=+0.182)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.325 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.191 (n=176)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3435.4625` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 3435.4625 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.224 (n=241)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=8340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=7089)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.218 (n=3015)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `5363.4643` → IC=+0.345 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5363.4643 (IC base=+0.196)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.178 (n=2014)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.180 (n=2107)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.377 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.335)

- **PATRÓN** `py_entrada` > `0.845` → IC=+0.392 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.845 (IC base=+0.335)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=2091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=1764)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=2009)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.184 (n=1332)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.72 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=1862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.238 (n=1589)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.325 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.237)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=2015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1731)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.7` → IC=+0.190 (n=1057)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.7 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.190 (n=856)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.73 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.445 (n=346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.449 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `9523.4542` → IC=+0.461 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9523.4542 (IC base=+0.443)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.442 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.458 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `11651.323` → IC=+0.460 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11651.323 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.454 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.443)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.460 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.442 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.443)

- **PATRÓN** `libro_liquidez` > `3923.6329` → IC=+0.455 (n=65)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.195 (n=24629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.236 (n=9486)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=5062)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.169 (n=4292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4518)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.165)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=4366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=4363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=1586)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=1838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=4517)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.167)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=2209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=1689)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.268 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.206 (n=1517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.251 (n=2079)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.191 (n=3322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.246 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.188)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.202 (n=3743)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.125)

- **PATRÓN** `restante_min` < `4.05` → IC=+0.136 (n=3417)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` < 4.05 (IC base=+0.125)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.147 (n=3736)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.94 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=4528)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `lag_apertura_s` < `3.4` → IC=+0.151 (n=3419)

  - _Acción_: Kelly boost +0.76€ cuando `lag_apertura_s` < 3.4 (IC base=+0.125)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.207 (n=1875)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.131)

- **PATRÓN** `restante_min` < `3.99` → IC=+0.142 (n=1696)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` < 3.99 (IC base=+0.131)

- **PATRÓN** `restante_min` > `4.89` → IC=+0.145 (n=2350)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.89 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.150 (n=2519)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 8.0 (IC base=+0.131)

- **PATRÓN** `lag_apertura_s` < `6.49` → IC=+0.147 (n=2232)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 6.49 (IC base=+0.131)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=1868)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.47` → IC=+0.127 (n=2279)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.47 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.150 (n=1882)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=2299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.92` → IC=+0.148 (n=1723)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 2.92 (IC base=+0.119)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.317 (n=617)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `1640.8166` → IC=+0.298 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1640.8166 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.301 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.328 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `5124.6271` → IC=+0.295 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5124.6271 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.329 (n=290)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.382 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1497.524` → IC=+0.311 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1497.524 (IC base=+0.291)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.436 (n=344)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.432 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.430 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `1890.5013` → IC=+0.437 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1890.5013 (IC base=+0.429)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.433 (n=163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.440 (n=181)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.434 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `5265.735` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5265.735 (IC base=+0.429)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.262)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.399 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.274 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1386.3493` → IC=+0.288 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1386.3493 (IC base=+0.262)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.262)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.399 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.274 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1386.3493` → IC=+0.288 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1386.3493 (IC base=+0.262)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9742` → IC=+0.228 (n=1853)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9742 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.2046` → IC=+0.242 (n=1142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2046 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.83` → IC=+0.166 (n=2142)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.83 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.613` → IC=+0.255 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.613 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `1.0681` → IC=+0.241 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0681 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` < `0.0812` → IC=+0.190 (n=3236)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0812 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.11` → IC=+0.193 (n=1392)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.11 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `2.8516` → IC=+0.190 (n=3589)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.8516 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `1.472` → IC=+0.193 (n=3589)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.472 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.5741` → IC=+0.125 (n=6841)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.5741 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.1299` → IC=+0.164 (n=2040)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1299 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `1.2072` → IC=+0.162 (n=2126)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2072 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` > `0.8704` → IC=+0.165 (n=1417)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.8704 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.1694` → IC=+0.223 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1694 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.4644` → IC=+0.194 (n=3540)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.4644 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.204 (n=3306)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 165.0 (IC base=+0.056)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.188 (n=415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.185 (n=566)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.007 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3264` → IC=+0.170 (n=1246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3264 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.186 (n=833)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 11.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.032` → IC=+0.284 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.032 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.193 (n=161)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.6357` → IC=+0.156 (n=1139)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.6357 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.162 (n=1139)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.182 (n=1325)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.06 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.188 (n=906)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 64.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.238 (n=819)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.253 (n=832)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1923` → IC=+0.280 (n=620)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1923 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.253 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0621` → IC=+0.286 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0621 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.363` → IC=+0.250 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.363 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0688` → IC=+0.234 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0688 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2878` → IC=+0.288 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2878 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.7352` → IC=+0.263 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7352 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1576.48` → IC=+0.249 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1576.48 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.231 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.238)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.235 (n=417)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.236 (n=415)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9251` → IC=+0.254 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9251 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1954` → IC=+0.217 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1954 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.91` → IC=+0.231 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.91 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `1.2629` → IC=+0.223 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2629 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `0.8783` → IC=+0.213 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8783 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.212 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4925` → IC=+0.227 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4925 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.4178` → IC=+0.217 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4178 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `11847.0948` → IC=+0.228 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11847.0948 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.161 (n=889)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0048 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3201` → IC=+0.147 (n=1008)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3201 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.160 (n=339)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.175 (n=1008)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6789 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.426` → IC=+0.180 (n=176)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.426 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.149 (n=1008)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2035 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.197 (n=269)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4143` → IC=+0.155 (n=899)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4143 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4133` → IC=+0.151 (n=900)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4133 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `12777.1965` → IC=+0.151 (n=672)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 12777.1965 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.167 (n=274)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 220.0 (IC base=+0.139)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.189 (n=1216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0058 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.178 (n=1215)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.255 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.358` → IC=+0.229 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.358 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.183 (n=1018)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.3774` → IC=+0.177 (n=159)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.3774 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.6649` → IC=+0.183 (n=1128)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.6649 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.191 (n=1367)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.195 (n=316)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 16.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.219 (n=1049)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.1472` → IC=+0.215 (n=462)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1472 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=494)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.3911` → IC=+0.230 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3911 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.635` → IC=+0.238 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.635 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.394` → IC=+0.212 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.394 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3649` → IC=+0.270 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3649 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.8451` → IC=+0.201 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8451 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.3036` → IC=+0.218 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3036 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.222 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1892.2584` → IC=+0.227 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1892.2584 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.211 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.212)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=87)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1539)

- **PATRÓN** `ibs_20min` > `0.9296` → IC=+0.158 (n=261)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.9296 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` < `0.1735` → IC=+0.337 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1735 (IC base=+0.007)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.23` → IC=+0.128 (n=484)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 4.23 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `0.6044` → IC=+0.409 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6044 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `1.1897` → IC=+0.348 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1897 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `2.4241` → IC=+0.337 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4241 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.1031` → IC=+0.335 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1031 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `163.0` → IC=+0.339 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 163.0 (IC base=+0.007)

- **PATRÓN** `dist_vwap_pct` > `0.1494` → IC=+0.182 (n=149)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1494 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `1.0358` → IC=+0.148 (n=410)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0358 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` > `0.6171` → IC=+0.137 (n=466)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6171 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2145` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2145 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `1.4999` → IC=+0.168 (n=372)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.4999 (IC base=-0.007)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=220)

- **FILTRO** `ibs_20min` < `0.2424` → IC=-0.176 (n=66)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2424
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=200)

- **FILTRO** `ibs_20min` > `0.2857` → IC=-0.126 (n=1588)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=796)

- **FILTRO** `sigma_ewma_delta_pct` > `8.607` → IC=-0.198 (n=263)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.607
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2121)

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

- **PATRÓN** `dist_vwap_pct` > `0.6537` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6537 (IC base=-0.047)

- **PATRÓN** `volumen_regimen` < `1.1392` → IC=+0.169 (n=170)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1392 (IC base=-0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.0872` → IC=+0.202 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0872 (IC base=-0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.4885` → IC=+0.208 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4885 (IC base=-0.047)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.241 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=-0.047)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6317` → IC=-0.191 (n=390)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6317
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1174)

- **FILTRO** `ibs_20min` < `0.641` → IC=-0.159 (n=1032)

  - _Acción_: SKIP cuando `ibs_20min` < 0.641
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=532)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.190 (n=324)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=1240)

- **FILTRO** `ibs_20min` > `0.7778` → IC=-0.195 (n=591)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7778
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1783)

- **PATRÓN** `dist_vwap_pct` > `0.8527` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8527 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.290 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2396 (IC base=-0.089)

- **PATRÓN** `volumen_regimen` > `0.6107` → IC=+0.275 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6107 (IC base=-0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.289 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.089)

- **PATRÓN** `volumen_spike_ratio` < `2.5191` → IC=+0.256 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5191 (IC base=-0.089)

- **PATRÓN** `volumen_spike_ratio` > `1.8262` → IC=+0.276 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8262 (IC base=-0.089)

- **PATRÓN** `dist_vwap_pct` > `0.6943` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6943 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` < `0.2353` → IC=+0.232 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2353 (IC base=-0.030)

- **PATRÓN** `volumen_regimen` > `1.0829` → IC=+0.291 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0829 (IC base=-0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.250 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.224` → IC=+0.248 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.224 (IC base=-0.030)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.229 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=-0.030)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.158 (n=3137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0076 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.4545` → IC=+0.170 (n=6184)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.4545 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.6935` → IC=+0.273 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6935 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.483` → IC=+0.136 (n=3282)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.483 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` > `0.6744` → IC=+0.225 (n=2074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6744 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2492` → IC=+0.250 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2492 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` < `1.4807` → IC=+0.234 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4807 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` > `2.8037` → IC=+0.229 (n=1226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8037 (IC base=+0.083)

- **PATRÓN** `ballena_activa_n` < `104.0` → IC=+0.274 (n=3162)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 104.0 (IC base=+0.083)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.136 (n=2385)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0084 (IC base=+0.065)

- **PATRÓN** `ibs_20min` < `0.5613` → IC=+0.147 (n=6289)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5613 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.6554` → IC=+0.241 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6554 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` > `1.2001` → IC=+0.254 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2001 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.2507` → IC=+0.320 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2507 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.6193` → IC=+0.251 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6193 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` > `2.3777` → IC=+0.256 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3777 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.255 (n=2253)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.065)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2298` → IC=-0.143 (n=468)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2298
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=1405)

- **FILTRO** `sigma_ewma_delta_pct` > `4.322` → IC=-0.158 (n=363)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.322
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1197)

- **PATRÓN** `ibs_20min` > `0.8553` → IC=+0.252 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8553 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.017` → IC=+0.160 (n=492)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 5.017 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.292 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.8775` → IC=+0.197 (n=308)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.8775 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` > `2.6757` → IC=+0.186 (n=154)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6757 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.217 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 61.0 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1791` → IC=+0.470 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1791 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.4617` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4617 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `2.3568` → IC=+0.444 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3568 (IC base=-0.017)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8342` → IC=-0.150 (n=530)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8342
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=1594)

- **PATRÓN** `dist_vwap_pct` > `0.1104` → IC=+0.123 (n=311)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1104 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `0.6545` → IC=+0.126 (n=532)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.6545 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.4168` → IC=+0.155 (n=192)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4168 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 236.0 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.1352` → IC=+0.230 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1352 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.341 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.7706` → IC=+0.227 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7706 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.209 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4316 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `515.0` → IC=+0.211 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 515.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.268 (n=988)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.244 (n=369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.252 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.57` → IC=+0.277 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.57 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1116` → IC=+0.256 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1116 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.6876` → IC=+0.241 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6876 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1910.4284` → IC=+0.238 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.4284 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.297 (n=878)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0055 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.315 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.3357` → IC=+0.286 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3357 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.886` → IC=+0.301 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.886 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.3459` → IC=+0.309 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3459 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `3.3742` → IC=+0.273 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 3.3742 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.228` → IC=+0.284 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.228 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.286 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `1882.4784` → IC=+0.296 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1882.4784 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.275 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.280)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2234` → IC=-0.211 (n=303)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2234
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=911)

- **FILTRO** `ibs_20min` > `0.8276` → IC=-0.177 (n=413)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1243)

- **PATRÓN** `ibs_20min` > `0.7998` → IC=+0.129 (n=413)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.7998 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.4514` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4514 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` < `0.9328` → IC=+0.199 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9328 (IC base=-0.026)

- **PATRÓN** `volumen_regimen` > `0.6044` → IC=+0.170 (n=219)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6044 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.2693` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2693 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.2948` → IC=+0.225 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2948 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `175.0` → IC=+0.223 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 175.0 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.103` → IC=+0.157 (n=68)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.103 (IC base=-0.027)

- **PATRÓN** `volumen_regimen` < `1.0948` → IC=+0.159 (n=168)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0948 (IC base=-0.027)

- **PATRÓN** `volumen_regimen` > `0.6889` → IC=+0.153 (n=168)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6889 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.1443` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1443 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.7112` → IC=+0.236 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7112 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` > `2.2216` → IC=+0.256 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2216 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.229 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6579` → IC=-0.196 (n=754)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6579
  - _Potencial_: sin este filtro IC_bueno=+0.243 (n=757)

- **FILTRO** `ibs_20min` > `0.7241` → IC=-0.234 (n=401)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7241
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=1210)

- **FILTRO** `sigma_ewma_delta_pct` > `4.726` → IC=-0.161 (n=387)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.726
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=1224)

- **PATRÓN** `ibs_20min` > `0.6579` → IC=+0.243 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6579 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1794` → IC=+0.308 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1794 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `0.8622` → IC=+0.275 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8622 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.634` → IC=+0.264 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.634 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1058` → IC=+0.268 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1058 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.4432` → IC=+0.316 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4432 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.310 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.2022` → IC=+0.167 (n=532)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.2022 (IC base=-0.002)

- **PATRÓN** `dist_vwap_pct` > `0.6691` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.6691 (IC base=-0.002)

- **PATRÓN** `dist_vwap_pct` < `0.1563` → IC=+0.180 (n=267)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1563 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.2143` → IC=+0.189 (n=297)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.2143 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.187 (n=257)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.22` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.22 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `2.6418` → IC=+0.203 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6418 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `1.526` → IC=+0.180 (n=267)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.526 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.209 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0145` → IC=+0.319 (n=646)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0145 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.276 (n=458)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` > `0.8982` → IC=+0.329 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8982 (IC base=+0.260)

- **PATRÓN** `dist_vwap_pct` > `0.1796` → IC=+0.307 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1796 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.339` → IC=+0.287 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.339 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.737` → IC=+0.260 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.737 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `0.85` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.85 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` < `0.1112` → IC=+0.264 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1112 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.296 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.552` → IC=+0.273 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.552 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.266 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `2426.1788` → IC=+0.264 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2426.1788 (IC base=+0.260)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.278 (n=353)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.292 (n=705)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.275 (n=1007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.3875` → IC=+0.302 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3875 (IC base=+0.268)

- **PATRÓN** `dist_vwap_pct` > `0.5156` → IC=+0.291 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5156 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.406` → IC=+0.282 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.406 (IC base=+0.268)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.311 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2407` → IC=+0.349 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2407 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `2.5387` → IC=+0.264 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5387 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.1688` → IC=+0.268 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1688 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.268 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `2550.1344` → IC=+0.279 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2550.1344 (IC base=+0.268)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.177 (n=1848)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0047 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.201 (n=1846)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3326` → IC=+0.174 (n=4872)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3326 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=5783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.6943` → IC=+0.229 (n=4946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6943 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1595` → IC=+0.196 (n=2418)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1595 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.216` → IC=+0.250 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.216 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2184` → IC=+0.161 (n=3703)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2184 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6228` → IC=+0.158 (n=3703)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.6228 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.1068` → IC=+0.187 (n=2162)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1068 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `2.3122` → IC=+0.168 (n=4611)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.3122 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `3825.7125` → IC=+0.173 (n=1846)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3825.7125 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.184 (n=4454)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 127.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.188 (n=3570)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0063 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0787` → IC=+0.205 (n=1784)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0787 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=2583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4508` → IC=+0.225 (n=5351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4508 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.747` → IC=+0.190 (n=2228)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.747 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1902` → IC=+0.156 (n=3918)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1902 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6257` → IC=+0.153 (n=3919)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6257 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.229 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.8815` → IC=+0.169 (n=3137)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.8815 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6394` → IC=+0.177 (n=1569)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6394 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.171 (n=4312)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 130.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.220 (n=309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.204 (n=421)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.3182` → IC=+0.208 (n=927)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3182 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=408)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.190)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.044` → IC=+0.309 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.044 (IC base=+0.190)

- **PATRÓN** `volumen_pendiente_norm` > `0.2282` → IC=+0.236 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2282 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` < `2.2555` → IC=+0.180 (n=735)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.2555 (IC base=+0.190)

- **PATRÓN** `volumen_spike_ratio` > `1.4401` → IC=+0.181 (n=835)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4401 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.205 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.190)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.246 (n=588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.246 (n=668)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1821` → IC=+0.296 (n=445)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1821 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.243 (n=670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.1074` → IC=+0.267 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1074 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.964` → IC=+0.250 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.964 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0688` → IC=+0.234 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0688 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.256 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.8747` → IC=+0.252 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8747 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6473` → IC=+0.231 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6473 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1582.26` → IC=+0.251 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1582.26 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.235 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.247 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.3591` → IC=+0.175 (n=799)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3591 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.45` → IC=+0.222 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.45 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.2079` → IC=+0.213 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2079 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.237 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `1.2757` → IC=+0.177 (n=799)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.2757 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2392` → IC=+0.191 (n=173)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2392 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.205 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `11191.459` → IC=+0.190 (n=714)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 11191.459 (IC base=+0.165)

- **PATRÓN** `ballena_activa_n` < `412.0` → IC=+0.162 (n=634)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 412.0 (IC base=+0.165)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.180 (n=804)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0049 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.287` → IC=+0.170 (n=913)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.287 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.168 (n=841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5076` → IC=+0.194 (n=913)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5076 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.089` → IC=+0.221 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.089 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.168 (n=913)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2025 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1586` → IC=+0.198 (n=276)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1586 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.163 (n=805)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.4146` → IC=+0.155 (n=804)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4146 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `237.0` → IC=+0.158 (n=241)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 237.0 (IC base=+0.151)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.199 (n=907)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0058 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1929` → IC=+0.197 (n=605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1929 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.219 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.189 (n=426)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.541` → IC=+0.271 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.541 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.1074` → IC=+0.185 (n=738)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1074 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.1357` → IC=+0.184 (n=352)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1357 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `3.6503` → IC=+0.200 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6503 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.204 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.205 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.235 (n=767)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.221 (n=349)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0885` → IC=+0.244 (n=256)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0885 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.265 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` < `0.3521` → IC=+0.249 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3521 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.268 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.3595` → IC=+0.269 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3595 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.8282` → IC=+0.211 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8282 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.2531` → IC=+0.229 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2531 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1889.7284` → IC=+0.240 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1889.7284 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.202 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.220)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.184 (n=766)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0065 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.4224` → IC=+0.169 (n=868)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4224 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.168 (n=872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.4125` → IC=+0.206 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4125 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.1317` → IC=+0.189 (n=574)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1317 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.201` → IC=+0.247 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.201 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8679` → IC=+0.166 (n=579)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8679 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.2029` → IC=+0.181 (n=290)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.2029 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.236 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.172 (n=282)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4142 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `2.5308` → IC=+0.183 (n=282)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5308 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7528.5122` → IC=+0.194 (n=579)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7528.5122 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.165 (n=708)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 158.0 (IC base=+0.156)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.160 (n=822)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.006 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.372` → IC=+0.148 (n=933)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.372 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.185 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 18.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.5944` → IC=+0.178 (n=933)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.5944 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` < `0.146` → IC=+0.141 (n=933)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.146 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.147` → IC=+0.197 (n=183)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 12.147 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.139 (n=622)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8646 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.6144` → IC=+0.135 (n=933)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6144 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.0738` → IC=+0.170 (n=371)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0738 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.7863` → IC=+0.132 (n=547)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.7863 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `9896.1185` → IC=+0.152 (n=423)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 9896.1185 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `187.0` → IC=+0.120 (n=749)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 187.0 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.147 (n=698)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0077 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=1076)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5098` → IC=+0.195 (n=1045)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5098 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `1.0126` → IC=+0.227 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0126 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.352` → IC=+0.256 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.352 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.2233` → IC=+0.121 (n=1045)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.2233 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `1.7948` → IC=+0.123 (n=669)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.7948 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=1062)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `3131.3446` → IC=+0.212 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3131.3446 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.136 (n=748)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 49.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.142 (n=683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0073 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.097` → IC=+0.142 (n=339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.097 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.525` → IC=+0.204 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.525 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.6832` → IC=+0.130 (n=187)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.6832 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.335` → IC=+0.159 (n=215)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 7.335 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.0504` → IC=+0.128 (n=896)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0504 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.185 (n=122)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.5717` → IC=+0.127 (n=387)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5717 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.1727` → IC=+0.147 (n=397)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.1727 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `3086.6566` → IC=+0.157 (n=339)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3086.6566 (IC base=+0.116)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.209 (n=661)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.1645` → IC=+0.213 (n=437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1645 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=1030)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.250 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.72 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `1.2054` → IC=+0.239 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2054 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.289` → IC=+0.234 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.289 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `1.2034` → IC=+0.200 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2034 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` > `0.8476` → IC=+0.215 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8476 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.169` → IC=+0.254 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.169 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `2.2071` → IC=+0.214 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2071 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.4272` → IC=+0.203 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4272 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.199 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.241 (n=353)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0074 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.022` → IC=+0.205 (n=480)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.022 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.218 (n=353)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.211 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=490)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.4305` → IC=+0.236 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4305 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `1.1079` → IC=+0.208 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1079 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.713` → IC=+0.224 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.713 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.6282` → IC=+0.214 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6282 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.287 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2526` → IC=+0.195 (n=813)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.2526 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4604` → IC=+0.187 (n=924)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4604 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2511.48` → IC=+0.210 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2511.48 (IC base=+0.200)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.146 (n=430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0038 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.154 (n=587)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0071 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0941` → IC=+0.153 (n=430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0941 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=653)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.4079` → IC=+0.169 (n=1290)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.4079 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.7813` → IC=+0.190 (n=172)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.7813 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.713` → IC=+0.177 (n=583)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 3.713 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8639` → IC=+0.161 (n=735)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8639 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1672` → IC=+0.166 (n=354)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1672 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.4377` → IC=+0.148 (n=410)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4377 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.153 (n=819)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.147 (n=1424)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `8121.9037` → IC=+0.175 (n=585)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 8121.9037 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.164 (n=364)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 20.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.144 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0036 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.4887` → IC=+0.143 (n=1176)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.4887 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.807` → IC=+0.125 (n=531)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 3.807 (IC base=+0.103)

- **PATRÓN** `volumen_pendiente_norm` > `0.1662` → IC=+0.144 (n=344)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.1662 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `2.2321` → IC=+0.126 (n=1118)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.2321 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.137 (n=400)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 20.0 (IC base=+0.103)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.142 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0037 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1037` → IC=+0.169 (n=128)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1037 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.159 (n=291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 8.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.9057` → IC=+0.189 (n=130)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.9057 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.2999` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2999 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.328` → IC=+0.186 (n=135)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.328 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.5894` → IC=+0.204 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5894 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.0648` → IC=+0.126 (n=121)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.0648 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `1.5129` → IC=+0.129 (n=246)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.5129 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `9633.8027` → IC=+0.157 (n=287)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9633.8027 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 150.0 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.204 (n=194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.2739` → IC=+0.138 (n=387)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.2739 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.3747` → IC=+0.186 (n=294)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.3747 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.279` → IC=+0.130 (n=182)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 4.279 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` > `0.7151` → IC=+0.133 (n=393)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.7151 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.1552` → IC=+0.196 (n=123)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1552 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` < `2.0997` → IC=+0.143 (n=379)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.0997 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.155 (n=137)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 156.0 (IC base=+0.112)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.256 (n=174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.224 (n=132)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.239 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.2763` → IC=+0.248 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2763 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.3645` → IC=+0.246 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3645 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.252 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.602` → IC=+0.231 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.602 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.168` → IC=+0.246 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.168 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2451` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2451 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.3686` → IC=+0.220 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3686 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.0245` → IC=+0.264 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0245 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `12476.4494` → IC=+0.231 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12476.4494 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.132 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0047 (IC base=+0.084)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.155 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.3235` → IC=+0.137 (n=221)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.3235 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.48` → IC=+0.137 (n=89)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 6.48 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.084)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.9091` → IC=+0.207 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9091 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.328` → IC=+0.146 (n=125)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 5.328 (IC base=+0.067)

- **PATRÓN** `libro_liquidez` > `2944.1737` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2944.1737 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.4524` → IC=+0.155 (n=253)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.4524 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7227` → IC=+0.146 (n=111)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.7227 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `2.5969` → IC=+0.123 (n=229)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5969 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.129 (n=195)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 45.0 (IC base=+0.074)

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
- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.191 (n=3155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0086 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=7271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.4738` → IC=+0.211 (n=6955)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4738 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.8871` → IC=+0.199 (n=920)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.8871 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.579` → IC=+0.220 (n=3416)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.579 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8833` → IC=+0.163 (n=3142)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8833 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1697` → IC=+0.183 (n=1914)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1697 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.6484` → IC=+0.177 (n=2199)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6484 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.170 (n=8260)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.04 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3788.7148` → IC=+0.171 (n=2319)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3788.7148 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.191 (n=4920)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 98.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.198 (n=4263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0067 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.4745` → IC=+0.185 (n=6385)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4745 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.200 (n=2432)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=2956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5584` → IC=+0.237 (n=6385)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5584 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.771` → IC=+0.203 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.771 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.689` → IC=+0.182 (n=6157)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.689 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.059` → IC=+0.156 (n=3879)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.059 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `1.201` → IC=+0.160 (n=1470)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.201 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2366` → IC=+0.248 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2366 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.2953` → IC=+0.190 (n=2566)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.2953 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.178 (n=5262)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 130.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.222 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.232 (n=527)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=784)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.796` → IC=+0.325 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.796 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.094` → IC=+0.225 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.094 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `1.559` → IC=+0.199 (n=473)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.559 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.589` → IC=+0.189 (n=358)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.589 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.05` → IC=+0.224 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.05 (IC base=+0.196)

- **PATRÓN** `ballena_activa_n` < `80.0` → IC=+0.230 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 80.0 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.266 (n=807)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.269 (n=919)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.2039` → IC=+0.288 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2039 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=843)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.0669` → IC=+0.310 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0669 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.636` → IC=+0.270 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.636 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2279` → IC=+0.319 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2279 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `1.9123` → IC=+0.281 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9123 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1578.46` → IC=+0.269 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1578.46 (IC base=+0.260)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.260 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.187 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0027 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.1824` → IC=+0.153 (n=735)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1824 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.6923` → IC=+0.242 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6923 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.3341` → IC=+0.199 (n=423)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3341 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.901` → IC=+0.169 (n=258)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.901 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.384` → IC=+0.154 (n=977)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.384 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `1.2804` → IC=+0.161 (n=1101)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2804 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1561` → IC=+0.181 (n=305)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1561 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `2.4502` → IC=+0.160 (n=1048)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4502 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `1.7711` → IC=+0.160 (n=698)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7711 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `10640.5814` → IC=+0.171 (n=983)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 10640.5814 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `498.0` → IC=+0.164 (n=976)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 498.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.188 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0024 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.3247` → IC=+0.173 (n=982)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3247 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.172 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.6433` → IC=+0.206 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6433 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.581` → IC=+0.187 (n=180)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.581 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.186` → IC=+0.168 (n=982)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.186 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1498` → IC=+0.223 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1498 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.4046` → IC=+0.172 (n=885)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.4046 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `322.0` → IC=+0.170 (n=349)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 322.0 (IC base=+0.157)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.226 (n=1088)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=1142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.217 (n=973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.6713` → IC=+0.249 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6713 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.413` → IC=+0.285 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.413 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.2192` → IC=+0.219 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2192 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.6898` → IC=+0.219 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6898 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.235 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 62.0 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.232 (n=1060)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.231 (n=948)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.1472` → IC=+0.229 (n=467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1472 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.236 (n=505)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.267 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.693` → IC=+0.276 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.693 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.3607` → IC=+0.290 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3607 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.7875` → IC=+0.220 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7875 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.2501` → IC=+0.227 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2501 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.237 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `1894.26` → IC=+0.230 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1894.26 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.220 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.228)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.169 (n=518)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0038 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4291` → IC=+0.136 (n=1174)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.4291 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=1228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.7132` → IC=+0.235 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7132 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.3355` → IC=+0.179 (n=450)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3355 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.356` → IC=+0.171 (n=511)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 4.356 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8828` → IC=+0.159 (n=783)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8828 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.1997` → IC=+0.137 (n=392)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.1997 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.233 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.4563` → IC=+0.163 (n=375)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4563 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=1273)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `9026.9243` → IC=+0.235 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9026.9243 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.144 (n=925)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 169.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.191 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0031 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4242` → IC=+0.150 (n=942)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4242 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=425)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6906` → IC=+0.184 (n=942)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6906 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1944` → IC=+0.138 (n=872)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1944 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.13` → IC=+0.192 (n=141)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.13 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.140 (n=628)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8546 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `0.6137` → IC=+0.136 (n=943)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6137 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2758` → IC=+0.261 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2758 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.557` → IC=+0.142 (n=386)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.557 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `2.1299` → IC=+0.162 (n=397)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.1299 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `11093.2268` → IC=+0.177 (n=314)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 11093.2268 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `198.0` → IC=+0.137 (n=863)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 198.0 (IC base=+0.133)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=460)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.4583` → IC=+0.175 (n=1214)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4583 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `1.0026` → IC=+0.174 (n=213)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 1.0026 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.403` → IC=+0.214 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.403 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=833)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `2933.8625` → IC=+0.249 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2933.8625 (IC base=+0.094)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.173 (n=500)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0061 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1205` → IC=+0.151 (n=379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1205 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.156 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.619` → IC=+0.208 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.619 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.1894` → IC=+0.138 (n=931)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1894 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.344` → IC=+0.127 (n=1091)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.344 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.7148` → IC=+0.153 (n=500)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7148 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2176` → IC=+0.182 (n=177)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2176 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4671` → IC=+0.150 (n=327)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4671 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.2089` → IC=+0.138 (n=445)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.2089 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2953.4428` → IC=+0.159 (n=379)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2953.4428 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.027` → IC=+0.217 (n=408)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.027 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=1277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=1090)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.237 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.1738` → IC=+0.235 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1738 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.534` → IC=+0.235 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.534 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2397` → IC=+0.204 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2397 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.204 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6199 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2373` → IC=+0.230 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2373 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.6094` → IC=+0.227 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6094 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.209 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2556.6049` → IC=+0.207 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2556.6049 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.248 (n=451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0252` → IC=+0.224 (n=450)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0252 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.203 (n=1432)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.251 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.4786` → IC=+0.204 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4786 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.1798` → IC=+0.203 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1798 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.941` → IC=+0.262 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.941 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.239 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.257 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.2259` → IC=+0.192 (n=1033)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2259 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.4453` → IC=+0.197 (n=1173)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4453 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2530.3534` → IC=+0.204 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2530.3534 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.182 (n=1077)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 37.0 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=2345)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.146 (n=719)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0051 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4192` → IC=+0.140 (n=1886)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4192 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.155 (n=745)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.139 (n=720)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 4.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.200 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1845` → IC=+0.126 (n=723)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.1845 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.188` → IC=+0.147 (n=344)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 10.188 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` > `0.8969` → IC=+0.130 (n=921)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 0.8969 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.1731` → IC=+0.156 (n=594)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1731 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `1.4515` → IC=+0.152 (n=707)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4515 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.8861` → IC=+0.144 (n=1413)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.8861 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `8788.3223` → IC=+0.147 (n=972)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8788.3223 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.199 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0037 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4768` → IC=+0.163 (n=1771)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4768 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1843` → IC=+0.156 (n=779)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.1843 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6915` → IC=+0.155 (n=291)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6915 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.241` → IC=+0.148 (n=1750)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.241 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.9013` → IC=+0.154 (n=1120)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.9013 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0721` → IC=+0.154 (n=834)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0721 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.5699` → IC=+0.145 (n=1753)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.5699 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8164` → IC=+0.151 (n=1168)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.8164 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=2345)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `12051.5949` → IC=+0.158 (n=803)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12051.5949 (IC base=+0.139)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_ewma_delta_pct` > `4.934` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.934
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=344)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.160 (n=239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0058 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.160 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0035 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0941` → IC=+0.188 (n=91)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0941 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.174 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 19.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.516` → IC=+0.194 (n=181)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.516 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.2289` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.2289 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.934` → IC=+0.159 (n=344)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.934 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.1969` → IC=+0.148 (n=271)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1969 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.8077` → IC=+0.178 (n=181)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8077 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.1087` → IC=+0.148 (n=302)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.1087 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2272` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2272 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.4169` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4169 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.6272` → IC=+0.167 (n=91)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.6272 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `12645.8095` → IC=+0.193 (n=242)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 12645.8095 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.200 (n=364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.3662` → IC=+0.147 (n=828)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3662 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.168 (n=296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.1546` → IC=+0.164 (n=364)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1546 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.6071` → IC=+0.145 (n=376)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6071 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.6069` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6069 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.225` → IC=+0.158 (n=808)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 6.225 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.8812` → IC=+0.177 (n=552)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.8812 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.0691` → IC=+0.160 (n=392)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0691 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.5652` → IC=+0.141 (n=825)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.5652 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.8071` → IC=+0.149 (n=550)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.8071 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `12051.5949` → IC=+0.148 (n=740)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 12051.5949 (IC base=+0.134)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.212 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.191 (n=205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0104 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.2953` → IC=+0.168 (n=302)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2953 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.237 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.9863` → IC=+0.226 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9863 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.281` → IC=+0.210 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.281 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.0959` → IC=+0.175 (n=195)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0959 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `3.4649` → IC=+0.167 (n=451)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.4649 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.8314` → IC=+0.161 (n=402)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.8314 (IC base=+0.156)

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
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.145 (n=694)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0088 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.139 (n=693)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0045 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4977` → IC=+0.144 (n=694)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.4977 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.164 (n=236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.140 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 4.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.7971` → IC=+0.159 (n=315)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.7971 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.9872` → IC=+0.182 (n=152)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.9872 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4203` → IC=+0.144 (n=650)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4203 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.807` → IC=+0.145 (n=692)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.807 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.1119` → IC=+0.144 (n=610)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.1119 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.6457` → IC=+0.136 (n=693)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 0.6457 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1754` → IC=+0.156 (n=210)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1754 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.161 (n=228)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=640)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8862.571` → IC=+0.154 (n=620)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8862.571 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.173 (n=488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0071 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.5081` → IC=+0.194 (n=553)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.5081 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.171 (n=378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.103` → IC=+0.169 (n=553)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.103 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.168 (n=254)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.3657` → IC=+0.160 (n=563)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.3657 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.089` → IC=+0.168 (n=263)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.089 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6473` → IC=+0.184 (n=185)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6473 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.7334` → IC=+0.159 (n=494)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.7334 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.184 (n=242)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.183` → IC=+0.169 (n=478)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.183 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.170 (n=543)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `8201.961` → IC=+0.169 (n=553)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 8201.961 (IC base=+0.155)

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
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=260)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=265)

- **FILTRO** `dist_vwap_pct` > `0.1599` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1599
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=187)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.184 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.005 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.162 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6404` → IC=+0.201 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6404 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1296` → IC=+0.148 (n=251)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1296 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.218` → IC=+0.210 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.218 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.231 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `2.5266` → IC=+0.142 (n=384)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.5266 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=392)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2445.5482` → IC=+0.162 (n=211)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2445.5482 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=-0.035)

- **PATRÓN** `dist_vwap_pct` < `0.1599` → IC=+0.130 (n=187)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1599 (IC base=-0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.931` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.931 (IC base=-0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=-0.035)

- **PATRÓN** `volumen_spike_ratio` < `2.4111` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.4111 (IC base=-0.035)

- **PATRÓN** `volumen_spike_ratio` > `1.3879` → IC=+0.146 (n=125)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.3879 (IC base=-0.035)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=133)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=-0.035)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.206 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.201 (n=75)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.5781` → IC=+0.200 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5781 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.739` → IC=+0.127 (n=108)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 3.739 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `1.0527` → IC=+0.127 (n=148)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0527 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` < `0.0763` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0763 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.2602` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2602 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `2.0198` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.0198 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2846.2218` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2846.2218 (IC base=+0.102)

- **PATRÓN** `drift_60min` |x|≤ `0.0401` → IC=+0.239 (n=21)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0401 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.7` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.7 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.699` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.699 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.9643` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.9643 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.245 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.035)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6404` → IC=-0.161 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6404
  - _Potencial_: sin este filtro IC_bueno=+0.224 (n=172)

- **FILTRO** `sigma_h` > `0.0066` → IC=-0.321 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=79)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=70)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.159 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0048 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.130 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.107)

- **PATRÓN** `ibs_20min` > `0.6404` → IC=+0.224 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6404 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` > `0.1209` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1209 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.109` → IC=+0.320 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.109 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` < `0.7859` → IC=+0.141 (n=115)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.7859 (IC base=+0.107)

- **PATRÓN** `volumen_regimen` > `0.6191` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.6191 (IC base=+0.107)

- **PATRÓN** `volumen_pendiente_norm` > `0.3066` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3066 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` < `1.7387` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7387 (IC base=+0.107)

- **PATRÓN** `volumen_spike_ratio` > `1.4015` → IC=+0.140 (n=123)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4015 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=179)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `1343.31` → IC=+0.202 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1343.31 (IC base=+0.107)

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

- **PATRÓN** `libro_liquidez` > `1059.8551` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1059.8551 (IC base=-0.061)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=76)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=37)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.167 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0059 (IC base=+0.069)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.127 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 14.0 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.191 (n=150)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.6757 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.8439` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.8439 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.59` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.59 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.0854` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.0854 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.5681` → IC=+0.162 (n=131)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.5681 (IC base=+0.069)

- **PATRÓN** `libro_liquidez` > `385.351` → IC=+0.154 (n=128)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 385.351 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.25` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.25 (IC base=-0.086)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1621` → IC=-0.389 (n=34)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1621
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=105)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.419 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `dist_vwap_pct` > `0.2306` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2306
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=125)

- **FILTRO** `volumen_pendiente_norm` > `0.1113` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1113
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=48)

- **FILTRO** `dist_vwap_pct` > `0.3468` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3468
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=111)

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
- **FILTRO** `ibs_20min` < `0.6783` → IC=-0.470 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6783
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.357 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=25)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `volumen_regimen` < `1.0152` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0152
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
- **FILTRO** `ibs_20min` > `0.25` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=172)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.155 (n=192)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.6429 (IC base=+0.060)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.149 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 15.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.144 (n=172)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.25 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.866` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 5.866 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.0649` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.0649 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `3703.4476` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3703.4476 (IC base=+0.053)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=64)

- **FILTRO** `ibs_20min` < `0.4049` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4049
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=60)

- **FILTRO** `volumen_regimen` < `0.7924` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7924
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=54)

- **PATRÓN** `sigma_h` > `0.0019` → IC=+0.128 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` > 0.0019 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.2127` → IC=+0.153 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.2127 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1622 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.217` → IC=+0.137 (n=89)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 14.217 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1293` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1293 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `3.3907` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 3.3907 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `1.6024` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.6024 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `3644.5187` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3644.5187 (IC base=+0.119)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=52)

- **FILTRO** `ibs_20min` < `0.6645` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6645
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=51)

- **FILTRO** `ibs_20min` > `0.3626` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3626
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=64)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.167 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0046 (IC base=+0.071)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.160 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.071)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.8265` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.8265 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.0901` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.0901 (IC base=+0.071)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `1624.9844` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1624.9844 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.26` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.26 (IC base=+0.029)

- **PATRÓN** `libro_liquidez` > `1570.5288` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1570.5288 (IC base=+0.029)

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
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.122 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2811.7744` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2811.7744 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2370.2342` → IC=+0.122 (n=416)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2370.2342 (IC base=+0.095)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.122 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 10.0 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2811.7744` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2811.7744 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `2370.2342` → IC=+0.122 (n=416)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2370.2342 (IC base=+0.095)

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
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=180)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=166)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1250)

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
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=507)

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
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=455)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=215)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=215)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.167 (n=43)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=187)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=151)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=151)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=91)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.151 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=125)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=47)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=147)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=208)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=208)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=72)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=5718)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=979)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=1113)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.465` → IC=-0.177 (n=2355)

  - _Acción_: SKIP cuando `py_entrada` < 0.465
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=7131)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.166 (n=2450)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=7434)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.212 (n=383)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=1189)

- **FILTRO** `ibs_20min` < `0.748` → IC=-0.175 (n=392)

  - _Acción_: SKIP cuando `ibs_20min` < 0.748
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1180)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.199 (n=400)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=1243)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.218 (n=410)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1314)

- **FILTRO** `ibs_20min` > `0.2873` → IC=-0.178 (n=430)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2873
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=1294)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.196 (n=383)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=1161)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.184 (n=428)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1311)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2030)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=1930)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=1936)

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
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=133)

- **FILTRO** `ibs_20min` > `0.9803` → IC=-0.217 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9803
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=133)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=537)

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
- **FILTRO** `py_entrada` < `0.35` → IC=-0.275 (n=5583)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=17049)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.235 (n=5657)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=16975)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.162 (n=7641)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=14991)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.220 (n=6964)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=21211)

- **FILTRO** `ibs_7min` > `0.2969` → IC=-0.173 (n=7042)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2969
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=21133)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.317 (n=833)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2715)

- **FILTRO** `ibs_7min` < `0.7105` → IC=-0.259 (n=1170)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7105
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=2378)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.203 (n=853)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=2695)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.145 (n=3301)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1605)

- **FILTRO** `drift_7min_pct` |x|> `0.1087` → IC=-0.123 (n=1668)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1087
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=3238)

- **FILTRO** `ibs_7min` > `0.7992` → IC=-0.202 (n=1225)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7992
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=3681)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.147 (n=917)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=3071)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.254 (n=993)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=2995)

- **FILTRO** `ibs_7min` < `0.7628` → IC=-0.184 (n=997)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7628
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=2991)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.171 (n=995)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=2993)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.260 (n=921)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=3087)

- **FILTRO** `ibs_7min` > `0.2498` → IC=-0.170 (n=1001)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2498
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=3007)

- **FILTRO** `ballena_activa_n` > `113.0` → IC=-0.162 (n=1354)

  - _Acción_: SKIP cuando `ballena_activa_n` > 113.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2654)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.180 (n=823)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=2533)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.322 (n=791)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=2565)

- **FILTRO** `ibs_7min` < `0.2069` → IC=-0.272 (n=839)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2069
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=2517)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.215 (n=776)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=2580)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.231 (n=1189)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=3949)

- **FILTRO** `ibs_7min` > `0.2666` → IC=-0.151 (n=1746)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2666
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=3392)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=1184)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=2552)

- **FILTRO** `ibs_7min` < `0.7492` → IC=-0.190 (n=934)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=2802)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.185 (n=929)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=2807)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.259 (n=924)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2853)

- **FILTRO** `ibs_7min` > `0.2744` → IC=-0.174 (n=943)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2744
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2834)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.176 (n=940)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=2837)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.234 (n=1045)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3139)

- **FILTRO** `ibs_7min` < `0.7353` → IC=-0.202 (n=1046)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7353
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=3138)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.168 (n=1270)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=4057)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.281 (n=904)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2916)

- **FILTRO** `ibs_7min` < `0.7368` → IC=-0.224 (n=955)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7368
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=2865)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.210 (n=884)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2936)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.195 (n=1196)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=3823)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=920)

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
- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=515)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3984` → IC=+0.136 (n=651)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3984 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.130 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `total_vol_5m` < `314679.3` → IC=+0.135 (n=628)

  - _Acción_: Kelly boost +0.67€ cuando `total_vol_5m` < 314679.3 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=309)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.140 (n=262)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.123)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.205 (n=76)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.110)

- **PATRÓN** `total_vol_5m` < `495.741` → IC=+0.196 (n=77)

  - _Acción_: Kelly boost +0.98€ cuando `total_vol_5m` < 495.741 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `9761.0798` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 9761.0798 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `70.0` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 70.0 (IC base=+0.110)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3997` → IC=+0.207 (n=104)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.3997 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.164)

- **PATRÓN** `total_vol_5m` < `7212.57` → IC=+0.170 (n=104)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 7212.57 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3632.1507` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3632.1507 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.179 (n=82)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 69.0 (IC base=+0.164)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.160 (n=104)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.109)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.129 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 13.0 (IC base=+0.109)

- **PATRÓN** `total_vol_5m` < `353208.2` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `total_vol_5m` < 353208.2 (IC base=+0.109)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.243 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 37.0 (IC base=+0.109)

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
- **FILTRO** `T_h` < `87.9936` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `T_h` < 87.9936
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=24)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0076` → IC=-0.203 (n=170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0076
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=89)

- **FILTRO** `T_h` > `69.913` → IC=-0.168 (n=194)

  - _Acción_: SKIP cuando `T_h` > 69.913
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=65)

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
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=207)

- **FILTRO** `streak_estiramiento` > `0.7313` → IC=-0.138 (n=56)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.7313
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=110)

- **PATRÓN** `streak_estiramiento` < `0.4382` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `streak_estiramiento` < 0.4382 (IC base=+0.019)

- **PATRÓN** `streak_estiramiento` < `0.4095` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4095 (IC base=+0.030)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `991078.0` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `volumen_racha` > 991078.0
  - _Potencial_: sin este filtro IC_bueno=+0.180 (n=23)

- **FILTRO** `libro_liquidez` < `2208.5143` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 2208.5143
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=69)

- **PATRÓN** `volumen_racha` < `991078.0` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_racha` < 991078.0 (IC base=-0.011)

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
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=440)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=446)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=283)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=410)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=828)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=467)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=523)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2149)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1128)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1136)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.187 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0038 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.178 (n=324)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0086 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.169 (n=324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.166)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0589` → IC=+0.171 (n=970)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio_macro` |x|> 0.0589 (IC base=+0.166)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3447` → IC=+0.207 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3447 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.167 (n=1012)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 4.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.189 (n=467)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.166)

- **PATRÓN** `ibs_15` > `0.6176` → IC=+0.239 (n=970)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6176 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` < `0.102` → IC=+0.171 (n=639)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.102 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.699` → IC=+0.242 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.699 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=861)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2975.1342` → IC=+0.178 (n=647)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2975.1342 (IC base=+0.166)

### UPDOWN_GBM#60min
- **FILTRO** `sigma_ewma_delta_pct` > `26.924` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 26.924
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=276)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=275)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.5868` → IC=-0.127 (n=124)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.5868
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=243)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.215 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0023` → IC=+0.195 (n=244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0023 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.0624` → IC=+0.250 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0624 (IC base=+0.194)

- **PATRÓN** `drift_15min` |x|≤ `0.374` → IC=+0.214 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.374 (IC base=+0.194)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2384` → IC=+0.202 (n=82)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2384 (IC base=+0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3853` → IC=+0.227 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3853 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.211 (n=251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `ibs_15` > `0.8791` → IC=+0.294 (n=163)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8791 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.3722` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3722 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` < `0.099` → IC=+0.207 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.099 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.624` → IC=+0.257 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.624 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `13595.2872` → IC=+0.252 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13595.2872 (IC base=+0.194)

### UPDOWN_GBM#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `20.351` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 20.351 (IC base=+0.000)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.698` → IC=-0.124 (n=99)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.698
  - _Potencial_: sin este filtro IC_bueno=+0.262 (n=204)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.152 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0061 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.141 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0055 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0756` → IC=+0.157 (n=100)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0756 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2488` → IC=+0.179 (n=76)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.2488 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2712` → IC=+0.167 (n=139)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2712 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.136 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 11.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=238)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.698` → IC=+0.262 (n=204)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.698 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.3911` → IC=+0.153 (n=240)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.3911 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.024` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.024 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=268)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.141 (n=104)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.136)

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
- **FILTRO** `dist_vwap_pct` > `0.5798` → IC=-0.143 (n=113)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5798
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=483)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `8.191` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 8.191
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=22)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.892` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 12.892 (IC base=-0.017)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.219 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0133 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.087` → IC=+0.175 (n=121)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.087 (IC base=+0.158)

- **PATRÓN** `delta_ratio_macro` |x|> `0.047` → IC=+0.179 (n=275)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.047 (IC base=+0.158)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.217 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_15` > `0.5075` → IC=+0.247 (n=275)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5075 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1137` → IC=+0.175 (n=167)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1137 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.232` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.232 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.092` → IC=+0.159 (n=250)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 7.092 (IC base=+0.158)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.158 (n=296)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.03 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `2708.1108` → IC=+0.201 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2708.1108 (IC base=+0.158)

- **PATRÓN** `ibs_15` < `0.103` → IC=+0.172 (n=294)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.86€ cuando `ibs_15` < 0.103 (IC base=+0.046)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.397 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.332)

- **PATRÓN** `drift_60min` |x|≤ `0.1549` → IC=+0.337 (n=250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1549 (IC base=+0.332)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.338 (n=189)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.332)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2203` → IC=+0.369 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2203 (IC base=+0.332)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.356 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.332)

- **PATRÓN** `ibs_15` > `0.8365` → IC=+0.391 (n=254)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8365 (IC base=+0.332)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.362 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.332)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.332)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `3925.9545` → IC=+0.344 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3925.9545 (IC base=+0.332)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1885` → IC=+0.326 (n=142)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1885 (IC base=+0.329)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.326 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.329)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.357 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.329)

- **PATRÓN** `drift_60min` |x|≤ `0.1544` → IC=+0.333 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1544 (IC base=+0.329)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1017` → IC=+0.336 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1017 (IC base=+0.329)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1236` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1236 (IC base=+0.329)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.358 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.329)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.329 (n=168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.329)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.365 (n=161)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.329)

- **PATRÓN** `dist_vwap_pct` > `0.4001` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4001 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.561` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.561 (IC base=+0.329)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.296` → IC=+0.343 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.296 (IC base=+0.329)

- **PATRÓN** `libro_liquidez` > `8997.0825` → IC=+0.353 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8997.0825 (IC base=+0.329)

- **PATRÓN** `ballena_activa_n` < `611.0` → IC=+0.395 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 611.0 (IC base=+0.329)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.379 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.360 (n=55)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.331)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.348 (n=123)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.331)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.349 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.331)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.348 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.331)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.396 (n=123)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.331)

- **PATRÓN** `dist_vwap_pct` < `0.2797` → IC=+0.341 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2797 (IC base=+0.331)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.734` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.734 (IC base=+0.331)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.331)

- **PATRÓN** `libro_liquidez` > `3566.5529` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3566.5529 (IC base=+0.331)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.341 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=+0.331)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0122` → IC=-0.197 (n=496)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0122
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1491)

- **FILTRO** `ibs_15` < `0.5837` → IC=-0.183 (n=165)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5837
  - _Potencial_: sin este filtro IC_bueno=+0.243 (n=497)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=613)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1374)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.217 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=-0.056)

- **PATRÓN** `ibs_15` > `0.5837` → IC=+0.243 (n=497)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5837 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` < `0.262` → IC=+0.170 (n=389)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.262 (IC base=-0.056)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1192` → IC=+0.231 (n=642)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1192 (IC base=-0.050)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1825` → IC=+0.233 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1825 (IC base=-0.050)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.272 (n=963)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.050)

- **PATRÓN** `dist_vwap_pct` > `0.3804` → IC=+0.252 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3804 (IC base=-0.050)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.212 (n=293)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=881)

- **FILTRO** `sigma_h` < `0.0032` → IC=-0.229 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0032
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=881)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.214 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=425)

- **FILTRO** `sigma_ewma_delta_pct` > `20.169` → IC=-0.246 (n=215)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.169
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=959)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.167 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.003 (IC base=+0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2339` → IC=+0.250 (n=34)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2339 (IC base=+0.068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1145` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1145 (IC base=+0.068)

- **PATRÓN** `ibs_15` > `0.7695` → IC=+0.340 (n=92)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7695 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.1418` → IC=+0.260 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1418 (IC base=+0.068)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6395` → IC=-0.244 (n=80)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6395
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=241)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=304)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.156 (n=216)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0039 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0772` → IC=+0.213 (n=106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0772 (IC base=+0.129)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.129)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1291` → IC=+0.132 (n=161)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio_macro` |x|> 0.1291 (IC base=+0.129)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.226 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.161 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.144 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.253 (n=241)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.165 (n=174)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.838` → IC=+0.137 (n=257)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 18.838 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=304)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.227 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3466` → IC=+0.227 (n=350)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3466 (IC base=+0.214)

- **PATRÓN** `drift_15min` |x|≤ `0.7427` → IC=+0.216 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7427 (IC base=+0.214)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1958` → IC=+0.234 (n=182)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1958 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.241 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.214)

- **PATRÓN** `ibs_15` < `0.3584` → IC=+0.260 (n=398)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3584 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.7113` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7113 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.251` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.251 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.945` → IC=+0.219 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 11.945 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `3672.3796` → IC=+0.215 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3672.3796 (IC base=+0.214)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1644` → IC=-0.208 (n=166)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1644
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=323)

- **FILTRO** `drift_15min` |x|> `0.8298` → IC=-0.242 (n=122)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8298
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=367)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0711` → IC=+0.202 (n=186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0711 (IC base=-0.044)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.194` → IC=+0.184 (n=134)

  - _Acción_: Kelly boost +0.92€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.194 (IC base=-0.044)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.248 (n=208)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.044)

- **PATRÓN** `dist_vwap_pct` < `0.1449` → IC=+0.196 (n=192)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.1449 (IC base=-0.044)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0188` → IC=-0.240 (n=294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0188
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=295)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.237 (n=154)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=435)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1035` → IC=+0.375 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1035 (IC base=-0.049)

- **PATRÓN** `ibs_15` < `0.3256` → IC=+0.287 (n=275)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3256 (IC base=-0.049)

- **PATRÓN** `dist_vwap_pct` > `0.4287` → IC=+0.393 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4287 (IC base=-0.049)

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
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.291 (n=323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.294 (n=221)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.329 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2314` → IC=+0.317 (n=162)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2314 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1083` → IC=+0.320 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1083 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.303 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.329 (n=484)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2628` → IC=+0.323 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2628 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.491` → IC=+0.304 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.491 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.291 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `12357.9012` → IC=+0.315 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12357.9012 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.293 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.278)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.283 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.0602` → IC=+0.326 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0602 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `0.3839` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3839 (IC base=+0.278)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2389` → IC=+0.326 (n=90)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2389 (IC base=+0.278)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3796` → IC=+0.294 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3796 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.330 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.278)

- **PATRÓN** `ibs_15` > `0.8595` → IC=+0.311 (n=241)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8595 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.335 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.471` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.471 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `14264.9886` → IC=+0.316 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14264.9886 (IC base=+0.278)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.301 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.302 (n=215)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0716` → IC=+0.325 (n=95)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0716 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2251` → IC=+0.324 (n=72)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2251 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.333 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.316 (n=205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.343 (n=215)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2764` → IC=+0.312 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2764 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.297 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.547` → IC=+0.324 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.547 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.308 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `10575.7678` → IC=+0.300 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10575.7678 (IC base=+0.295)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.304 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 164.0 (IC base=+0.295)

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

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6176 sube el IC de +0.166 a +0.239 en UPDOWN_GBM#15min (n=970). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.8791 sube el IC de +0.194 a +0.294 en UPDOWN_GBM#BTC#15min (n=163). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.698 sube el IC de +0.136 a +0.262 en UPDOWN_GBM#ETH#15min (n=204). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.139 a +0.246 en UPDOWN_GBM#SOL#15min (n=136). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5075 sube el IC de +0.158 a +0.247 en UPDOWN_GBM#XRP#15min (n=275). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.103 sube el IC de +0.046 a +0.172 en UPDOWN_GBM#XRP#15min (n=294). Ya aplicado como kelly_boost=+0.86€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5837 sube el IC de -0.056 a +0.243 en UPDOWN_GBM_15M_TARDIO (n=497). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.050 a +0.272 en UPDOWN_GBM_15M_TARDIO (n=963). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7695 sube el IC de +0.068 a +0.340 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=92). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6395 sube el IC de +0.129 a +0.253 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=241). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3584 sube el IC de +0.214 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=398). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.144 a +0.333 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.044 a +0.248 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=208). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3256 sube el IC de -0.049 a +0.287 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=275). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.287 a +0.329 en UPDOWN_GBM_IBS_ALTO (n=484). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8595 sube el IC de +0.278 a +0.311 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=241). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.295 a +0.343 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=215). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8365 sube el IC de +0.332 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=254). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.329 a +0.365 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=161). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.331 a +0.396 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=123). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH#sniper` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#ETH` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.372 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1103 | +0.078 | +107.57€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1103 | +0.078 | +107.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 796 | +0.083 | +84.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 796 | +0.083 | +84.19€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 231 | +0.045 | +4.38€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 231 | +0.045 | +4.38€ | 4 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 50 | +0.173 | +20.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 50 | +0.173 | +20.49€ | 0 | 4 |
| ✅ BALLENAS_TARDIAS | 21316 | -0.105 | -3216.50€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1139 | -0.028 | -192.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 20177 | -0.110 | -3023.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 2985 | -0.117 | -555.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 2985 | -0.117 | -555.43€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1139 | -0.028 | -192.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1139 | -0.028 | -192.99€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 2712 | -0.088 | -612.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 2712 | -0.088 | -612.51€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5509 | -0.061 | -517.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5509 | -0.061 | -517.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 4902 | -0.110 | -374.50€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 4902 | -0.110 | -374.50€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4069 | -0.183 | -963.60€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4069 | -0.183 | -963.60€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 10202 | -0.049 | +4338.05€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 2795 | -0.009 | +1860.84€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 7407 | -0.064 | +2477.21€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 10202 | -0.049 | +4338.05€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 2795 | -0.009 | +1860.84€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 7407 | -0.064 | +2477.21€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 341 | -0.101 | -62.09€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 8 | +0.000 | -0.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 333 | -0.103 | -61.76€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 16 | -0.089 | -0.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 16 | -0.089 | -0.58€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 207 | -0.041 | -20.91€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 205 | -0.041 | -20.91€ | 1 | 1 |
| 🚫 CANDIDATA9_BOT_CONSENSO#ETH | 94 | -0.208 | -35.30€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 6 | +0.000 | -0.33€ | 0 | 0 |
| 🚫 CANDIDATA9_BOT_CONSENSO#ETH#5min | 88 | -0.222 | -34.97€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 8 | -0.160 | -8.57€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 8 | -0.160 | -8.57€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 16 | +0.000 | +3.27€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 16 | +0.000 | +3.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 67807 | +0.113 | -3664.72€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 10817 | +0.183 | -309.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 261 | -0.112 | -45.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 52257 | +0.100 | -3227.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 4472 | +0.117 | -82.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 8717 | +0.094 | -874.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 36 | -0.158 | -1.29€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 8666 | +0.096 | -861.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 13415 | +0.132 | -255.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3264 | +0.202 | -89.90€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 8660 | +0.109 | -176.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1449 | +0.117 | +33.80€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 8756 | +0.088 | -895.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 41 | -0.035 | -1.28€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 8700 | +0.089 | -882.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 14611 | +0.125 | -280.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4148 | +0.170 | -69.98€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 8719 | +0.109 | -162.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1732 | +0.101 | -39.38€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 13573 | +0.117 | -794.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3292 | +0.188 | -151.73€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 164 | -0.060 | +8.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 8826 | +0.091 | -574.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1291 | +0.136 | -76.43€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 8735 | +0.101 | -565.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 36 | -0.026 | +4.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 8686 | +0.102 | -570.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 10492 | +0.183 | -776.80€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 10492 | +0.183 | -776.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2679 | +0.168 | -290.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2679 | +0.168 | -290.02€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 149 | -0.136 | -0.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 149 | -0.136 | -0.83€ | 4 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2638 | +0.176 | -249.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2638 | +0.176 | -249.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2368 | +0.237 | -68.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2368 | +0.237 | -68.02€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2579 | +0.189 | -182.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2579 | +0.189 | -182.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 503 | +0.443 | +0.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 503 | +0.443 | +0.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 196 | +0.439 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 196 | +0.439 | -0.46€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 191 | +0.443 | +1.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 191 | +0.443 | +1.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 110 | +0.429 | -1.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 110 | +0.429 | -1.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 36762 | +0.192 | -3220.74€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 36762 | +0.192 | -3220.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 6430 | +0.165 | -864.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 6430 | +0.165 | -864.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 5795 | +0.224 | -218.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 5795 | +0.224 | -218.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 6374 | +0.167 | -830.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 6374 | +0.167 | -830.45€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 5899 | +0.217 | -258.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 5899 | +0.217 | -258.28€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6081 | +0.198 | -450.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6081 | +0.198 | -450.27€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 6183 | +0.188 | -598.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 6183 | +0.188 | -598.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 13650 | +0.125 | +270.63€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 13650 | +0.125 | +270.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 6759 | +0.131 | +200.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 6759 | +0.131 | +200.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 6891 | +0.119 | +70.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 6891 | +0.119 | +70.41€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1172 | +0.289 | -19.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1172 | +0.289 | -19.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 517 | +0.277 | -13.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 517 | +0.277 | -13.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 558 | +0.291 | -4.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 558 | +0.291 | -4.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 97 | +0.328 | -1.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 97 | +0.328 | -1.32€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 516 | +0.429 | -9.17€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 516 | +0.429 | -9.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 239 | +0.429 | -3.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 239 | +0.429 | -3.92€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 240 | +0.430 | -4.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 240 | +0.430 | -4.79€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 37 | +0.372 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 37 | +0.372 | -0.46€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 761 | +0.066 | -43.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 266 | +0.060 | -21.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 495 | +0.069 | -21.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 48 | +0.100 | +0.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 48 | +0.100 | +0.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 594 | +0.075 | -20.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 99 | +0.104 | +1.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 495 | +0.069 | -21.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 119 | +0.004 | -24.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 119 | +0.004 | -24.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 23535 | +0.098 | -757.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2001 | +0.095 | +31.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 21534 | +0.098 | -788.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 13527 | +0.102 | -217.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2001 | +0.095 | +31.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 11526 | +0.103 | -249.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 3926 | +0.116 | +34.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 3926 | +0.116 | +34.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 6082 | +0.076 | -573.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 6082 | +0.076 | -573.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 683 | +0.262 | -79.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 683 | +0.262 | -79.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 683 | +0.262 | -79.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 683 | +0.262 | -79.15€ | 0 | 4 |
| ✅ GBM_LATE_15M | 17771 | +0.073 | +7940.26€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 17771 | +0.073 | +7940.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 2898 | +0.197 | +2145.14€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 2898 | +0.197 | +2145.14€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 2600 | +0.174 | +1737.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2600 | +0.174 | +1737.84€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 3017 | +0.193 | +2180.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3017 | +0.193 | +2180.70€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 2668 | -0.002 | +377.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2668 | -0.002 | +377.18€ | 1 | 14 |
| ✅ GBM_LATE_15M#SOL | 2650 | -0.038 | +591.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2650 | -0.038 | +591.11€ | 4 | 10 |
| ✅ GBM_LATE_15M#XRP | 3938 | -0.054 | +908.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 3938 | -0.054 | +908.31€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 18754 | +0.074 | +9333.38€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 18754 | +0.074 | +9333.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3433 | +0.012 | +1926.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3433 | +0.012 | +1926.84€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 3987 | +0.000 | +716.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 3987 | +0.000 | +716.09€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2641 | +0.256 | +2590.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2641 | +0.256 | +2590.80€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2870 | -0.027 | +242.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2870 | -0.027 | +242.39€ | 2 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3122 | +0.011 | +1098.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3122 | +0.011 | +1098.43€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2701 | +0.265 | +2758.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2701 | +0.265 | +2758.83€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 14515 | +0.169 | +10444.94€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 14515 | +0.169 | +10444.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2124 | +0.210 | +1709.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2124 | +0.210 | +1709.87€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2282 | +0.158 | +1594.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2282 | +0.158 | +1594.82€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2231 | +0.203 | +1731.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2231 | +0.203 | +1731.64€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2400 | +0.141 | +1547.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2400 | +0.141 | +1547.61€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2747 | +0.113 | +1750.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2747 | +0.113 | +1750.01€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2731 | +0.199 | +2111.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2731 | +0.199 | +2111.00€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 3500 | +0.121 | +1323.08€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 3500 | +0.121 | +1323.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 105 | +0.107 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 105 | +0.107 | +39.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 968 | +0.114 | +366.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 968 | +0.114 | +366.93€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 966 | +0.152 | +418.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 966 | +0.152 | +418.38€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 706 | +0.071 | +163.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 706 | +0.071 | +163.72€ | 0 | 8 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 387 | +0.130 | +151.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 387 | +0.130 | +151.73€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO | 17785 | +0.172 | +12695.90€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 17785 | +0.172 | +12695.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 2768 | +0.224 | +2369.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 2768 | +0.224 | +2369.27€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2775 | +0.152 | +1819.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2775 | +0.152 | +1819.40€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 2860 | +0.219 | +2388.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 2860 | +0.219 | +2388.94€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 2820 | +0.134 | +1758.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 2820 | +0.134 | +1758.11€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3132 | +0.105 | +1725.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3132 | +0.105 | +1725.19€ | 0 | 17 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3430 | +0.201 | +2634.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3430 | +0.201 | +2634.98€ | 0 | 27 |
| ✅ GBM_LATE_5M | 5216 | +0.135 | +2686.50€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5216 | +0.135 | +2686.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 475 | +0.177 | +315.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 475 | +0.177 | +315.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1464 | +0.136 | +856.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1464 | +0.136 | +856.21€ | 1 | 27 |
| ✅ GBM_LATE_5M#DOGE | 661 | +0.165 | +403.32€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 661 | +0.165 | +403.32€ | 0 | 18 |
| ✅ GBM_LATE_5M#ETH | 1661 | +0.145 | +879.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1661 | +0.145 | +879.62€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 278 | +0.011 | +21.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 278 | +0.011 | +21.30€ | 2 | 2 |
| ✅ GBM_LATE_5M#XRP | 677 | +0.097 | +210.54€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 677 | +0.097 | +210.54€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1119 | +0.054 | +356.72€ | 3 | 16 |
| ✅ GBM_LATE_60M#60min | 1119 | +0.054 | +356.72€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 391 | +0.080 | +129.40€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 391 | +0.080 | +129.40€ | 0 | 16 |
| ✅ GBM_LATE_60M#ETH | 375 | +0.060 | +130.92€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 375 | +0.060 | +130.92€ | 3 | 18 |
| ✅ GBM_LATE_60M#SOL | 353 | +0.018 | +96.39€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 353 | +0.018 | +96.39€ | 2 | 9 |
| 🚫 GBM_LATE_60M_FADE | 278 | -0.282 | -36.90€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 278 | -0.282 | -36.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 106 | -0.222 | -7.71€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 106 | -0.222 | -7.71€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 92 | -0.340 | -23.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 92 | -0.340 | -23.29€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 80 | -0.281 | -5.89€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 80 | -0.281 | -5.89€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 515 | +0.057 | +91.58€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 515 | +0.057 | +91.58€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 191 | +0.054 | +28.01€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 191 | +0.054 | +28.01€ | 3 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 153 | +0.048 | +3.84€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 153 | +0.048 | +3.84€ | 3 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 171 | +0.067 | +59.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 171 | +0.067 | +59.73€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 53 | +0.227 | +25.89€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1186 | +0.098 | +312.65€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1186 | +0.098 | +312.65€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1186 | +0.098 | +312.65€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1186 | +0.098 | +312.65€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 333 | -0.094 | -37.20€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 333 | -0.094 | -37.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 78 | -0.100 | -9.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 78 | -0.100 | -9.01€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 108 | -0.027 | -4.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 108 | -0.027 | -4.40€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1448 | -0.006 | -11.53€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1448 | -0.006 | -11.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 163 | -0.021 | +0.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 163 | -0.021 | +0.58€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 101 | -0.053 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 101 | -0.053 | -6.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 554 | +0.022 | +14.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 554 | +0.022 | +14.28€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 458 | -0.006 | -8.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 458 | -0.006 | -8.22€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 97 | -0.066 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 97 | -0.066 | -6.47€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 830 | -0.043 | -22.45€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 830 | -0.043 | -22.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 244 | -0.061 | -16.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 244 | -0.061 | -16.27€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 261 | -0.021 | -0.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 261 | -0.021 | -0.15€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 325 | -0.047 | -6.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 325 | -0.047 | -6.03€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 11986 | -0.011 | -170.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 11986 | -0.011 | -170.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2058 | -0.020 | -39.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2058 | -0.020 | -39.86€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2559 | +0.008 | -17.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2559 | +0.008 | -17.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2215 | -0.019 | -17.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2215 | -0.019 | -17.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 2897 | -0.016 | -61.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 2897 | -0.016 | -61.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 19370 | -0.015 | +918.90€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 19370 | -0.015 | +918.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3330 | +0.008 | +480.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3330 | +0.008 | +480.14€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3150 | -0.026 | -19.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3150 | -0.026 | -19.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3367 | -0.002 | +280.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3367 | -0.002 | +280.15€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 2990 | -0.045 | -64.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 2990 | -0.045 | -64.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3250 | -0.018 | +144.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3250 | -0.018 | +144.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3283 | -0.009 | +98.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3283 | -0.009 | +98.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 4061 | -0.031 | -92.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 4061 | -0.031 | -92.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 885 | +0.001 | -14.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 885 | +0.001 | -14.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 743 | -0.034 | -17.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 743 | -0.034 | -17.57€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 41 | -0.128 | -5.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 41 | -0.128 | -5.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 371 | -0.119 | -13.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 371 | -0.119 | -13.44€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1175 | -0.031 | -15.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1175 | -0.031 | -15.89€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 50807 | -0.073 | +1047.59€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 50807 | -0.073 | +1047.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 8454 | -0.082 | +476.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 8454 | -0.082 | +476.15€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 7996 | -0.086 | -279.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 7996 | -0.086 | -279.42€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 8494 | -0.072 | +420.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 8494 | -0.072 | +420.14€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 7513 | -0.096 | -247.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 7513 | -0.096 | -247.05€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 9511 | -0.046 | +310.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 9511 | -0.046 | +310.89€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 8839 | -0.063 | +366.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 8839 | -0.063 | +366.89€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6616 | -0.020 | -116.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6616 | -0.020 | -116.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1453 | -0.020 | -17.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1453 | -0.020 | -17.77€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1454 | -0.011 | -8.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1454 | -0.011 | -8.75€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 974 | -0.034 | -15.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 974 | -0.034 | -15.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 905 | +0.110 | +300.94€ | 1 | 5 |
| ✅ ORDER_FLOW_5M#5min | 769 | +0.119 | +288.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 174 | +0.119 | +72.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 174 | +0.119 | +72.95€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 151 | +0.088 | +31.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 151 | +0.088 | +31.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 152 | +0.110 | +56.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 152 | +0.110 | +56.66€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 138 | +0.164 | +79.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 138 | +0.164 | +79.32€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#XRP | 154 | +0.109 | +48.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 154 | +0.109 | +48.00€ | 0 | 5 |
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
| 🚫 PRICE_TARGET_GBM_FADE | 472 | -0.219 | -34.47€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 199 | -0.202 | -29.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 173 | -0.191 | -26.93€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 26 | -0.250 | -2.30€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 166 | -0.244 | -20.73€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 143 | -0.252 | -24.60€ | 5 | 0 |
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
| ✅ STREAK_FADE_15M | 357 | +0.026 | +4.94€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 357 | +0.026 | +4.94€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 156 | +0.038 | +1.94€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 156 | +0.038 | +1.94€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 24 | +0.077 | +2.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 24 | +0.077 | +2.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 40 | -0.048 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 40 | -0.048 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 137 | +0.025 | +5.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 137 | +0.025 | +5.65€ | 2 | 1 |
| ✅ STREAK_FADE_5M | 2297 | -0.022 | -97.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2297 | -0.022 | -97.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 560 | -0.023 | -23.43€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 560 | -0.023 | -23.43€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 150 | -0.040 | -13.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 150 | -0.040 | -13.41€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 783 | -0.022 | -33.51€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 783 | -0.022 | -33.51€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 48 | +0.020 | +0.80€ | 1 | 0 |
| ✅ STREAK_FADE_60M#60min | 48 | +0.020 | +0.80€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 29 | -0.048 | -1.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 29 | -0.048 | -1.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 19 | +0.113 | +2.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 5768 | +0.023 | +88.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 5768 | +0.023 | +88.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1870 | +0.025 | +24.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1870 | +0.025 | +24.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1185 | +0.034 | +36.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1185 | +0.034 | +36.22€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1681 | +0.011 | -0.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1681 | +0.011 | -0.60€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1032 | +0.028 | +27.61€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1032 | +0.028 | +27.61€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 5527 | +0.014 | -21.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 5527 | +0.014 | -21.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2168 | +0.023 | +7.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2168 | +0.023 | +7.84€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2199 | +0.017 | -2.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2199 | +0.017 | -2.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1160 | -0.008 | -26.67€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1160 | -0.008 | -26.67€ | 2 | 0 |
| ✅ UPDOWN_GBM | 21548 | +0.027 | +1130.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 5954 | +0.055 | +908.04€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 817 | +0.003 | +8.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 13419 | +0.021 | +231.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1270 | -0.009 | -20.80€ | 2 | 0 |
| ✅ UPDOWN_GBM#BNB | 1801 | +0.075 | +185.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 267 | +0.128 | +86.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1515 | +0.067 | +99.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 3811 | +0.027 | +238.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 692 | +0.081 | +162.08€ | 1 | 13 |
| ✅ UPDOWN_GBM#BTC#240min | 235 | +0.027 | +7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2296 | +0.021 | +71.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 555 | -0.004 | -4.46€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 33 | -0.129 | +1.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 2566 | +0.031 | +81.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 228 | +0.109 | +55.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2322 | +0.023 | +26.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 4370 | +0.015 | +162.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1625 | +0.040 | +160.20€ | 1 | 12 |
| ✅ UPDOWN_GBM#ETH#240min | 222 | +0.009 | +8.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2029 | +0.004 | -2.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 465 | -0.014 | -8.71€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 29 | -0.145 | +4.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 5716 | +0.014 | +125.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1602 | +0.021 | +95.09€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 217 | -0.007 | -1.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 3623 | +0.015 | +40.50€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 250 | -0.012 | -7.62€ | 1 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 24 | -0.154 | -0.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3282 | +0.037 | +338.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1540 | +0.073 | +348.26€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 108 | -0.036 | -5.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1634 | +0.009 | -3.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 86 | -0.148 | +5.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 378 | +0.332 | +98.27€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 378 | +0.332 | +98.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 214 | +0.329 | +49.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 214 | +0.329 | +49.94€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 164 | +0.331 | +48.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 164 | +0.331 | +48.33€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO | 8198 | -0.051 | +1735.27€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 8198 | -0.051 | +1735.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 397 | -0.049 | +350.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 397 | -0.049 | +350.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1575 | -0.132 | -9.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1575 | -0.132 | -9.01€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 851 | +0.182 | +467.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 851 | +0.182 | +467.00€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2650 | -0.063 | +426.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2650 | -0.063 | +426.86€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2586 | -0.077 | +445.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2586 | -0.077 | +445.35€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 86 | +0.057 | +7.70€ | 0 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 86 | +0.057 | +7.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 86 | +0.057 | +7.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 86 | +0.057 | +7.70€ | 0 | 6 |
| ✅ UPDOWN_GBM_IBS_ALTO | 645 | +0.287 | +520.73€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 645 | +0.287 | +520.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 359 | +0.278 | +271.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 359 | +0.278 | +271.79€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 286 | +0.295 | +248.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 286 | +0.295 | +248.95€ | 0 | 13 |
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
  - _Estado_: 409 celda(s) pasan gate riguroso completo de 1963 evaluadas (n>=40) y 2922 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.021 < 0.08 — monitorear
  - _Datos_: n=1602 IC=+0.021 PNL=+95.09€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.070 n=156/60 | contraria IC=+0.141 n=143 | gap=-0.072 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

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
  - _Estado_: ETH#60min: n=465/40 IC=-0.014 PNL=-8.71€ | BTC#60min: n=555/40 IC=-0.004 PNL=-4.46€ | SOL#60min: n=250/40 IC=-0.012 PNL=-7.62€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.055 n=234114 | tras_1loss IC=+0.067 n=183569 | tras_2loss IC=+0.035 n=79348/40 | gap=+0.020 (umbral 0.05)

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
  - _Estado_: n=941 IC=-0.008 PNL=-18.73€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=941 IC=-0.008 PNL=-18.73€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=329 IC=-0.014 PNL=-2.07€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=329 IC=-0.014 PNL=-2.07€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.166 > 0.1 con n=1293 PNL=+685.10€
  - _Datos_: n=1293 IC=+0.166 PNL=+685.10€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=692 IC=+0.081 PNL=+162.08€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=692 IC=+0.081 PNL=+162.08€

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
  - _Estado_: n=20 IC=-0.045 PNL=-1.64€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=20 IC=-0.045 PNL=-1.64€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.02 con n=513 PNL=+191.50€
  - _Datos_: n=513 IC=+0.123 PNL=+191.50€

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
  - _Estado_: n=6755 IC=+0.049 PNL=+761.74€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=6755 IC=+0.049 PNL=+761.74€

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
  - _Estado_: n=1174 IC=+0.046 PNL=+137.09€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1174 IC=+0.046 PNL=+137.09€

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
  - _Estado_: n=12165 IC=-0.143 PNL=+571.09€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12165 IC=-0.143 PNL=+571.09€

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
  - _Estado_: n=1342 IC=+0.140 PNL=+714.45€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1342 IC=+0.140 PNL=+714.45€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.238 < -0.1 con n=1237 PNL=-170.31€
  - _Datos_: n=1237 IC=-0.238 PNL=-170.31€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.095 n=620) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=620 IC=+0.095 PNL=+159.08€

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
  - _Estado_: n=6429 IC=+0.165 PNL=-865.09€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=6429 IC=+0.165 PNL=-865.09€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.1 con n=93 PNL=+59.67€
  - _Datos_: n=93 IC=+0.216 PNL=+59.67€
