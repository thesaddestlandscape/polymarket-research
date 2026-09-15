# Hipótesis automáticas — 2026-09-15 00:05 UTC
_Generado por shadow_postmortem.py sobre 443028 resoluciones (PNL=+47443.51€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` < `0.465` → IC=-0.148 (n=200)

  - _Acción_: SKIP cuando `py_entrada` < 0.465
  - _Potencial_: sin este filtro IC_bueno=+0.246 (n=412)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=403)

- **PATRÓN** `py_entrada` > `0.465` → IC=+0.246 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.465 (IC base=+0.117)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.204 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.117)

- **PATRÓN** `banda_hit_calibrado` > `0.8049` → IC=+0.257 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8049 (IC base=+0.117)

- **PATRÓN** `banda_z` > `9.058` → IC=+0.206 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.058 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.136 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=487)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.140 (n=134)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 100.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=403)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.129 (n=130)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 97.0 (IC base=+0.038)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.385` → IC=-0.131 (n=155)

  - _Acción_: SKIP cuando `py_entrada` < 0.385
  - _Potencial_: sin este filtro IC_bueno=+0.248 (n=320)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=289)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=314)

- **PATRÓN** `py_entrada` > `0.385` → IC=+0.248 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.385 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.210 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8036` → IC=+0.267 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8036 (IC base=+0.125)

- **PATRÓN** `banda_z` > `11.481` → IC=+0.269 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 11.481 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=403)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.125)

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
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=83)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=93)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.133 (n=77)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.495 (IC base=-0.013)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.174)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `145.96` → IC=-0.260 (n=5557)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.96
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=16676)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `n_ballenas` < `4.0` → IC=-0.133 (n=1960)

  - _Acción_: SKIP cuando `n_ballenas` < 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=1162)

- **FILTRO** `restante_s_al_confirmar` < `138.77` → IC=-0.289 (n=780)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.77
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=2342)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `483.07` → IC=-0.161 (n=296)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 483.07
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=891)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `135.32` → IC=-0.288 (n=696)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 135.32
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=2088)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `141.54` → IC=-0.162 (n=1437)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.54
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=4315)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `158.17` → IC=-0.256 (n=1298)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 158.17
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=3897)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `157.23` → IC=-0.338 (n=1383)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 157.23
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=2810)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.33` → IC=-0.305 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=306)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.151 (n=104)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=255)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.155 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=274)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.308 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=166)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=158)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.261 (n=65)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.156 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=70)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.194 (n=47)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=53)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.196 (n=11375)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.69 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=2806)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `11046.4721` → IC=+0.196 (n=895)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 11046.4721 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.145 (n=8671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=10144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.246 (n=7619)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=5561)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7106.825` → IC=+0.176 (n=1759)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7106.825 (IC base=+0.136)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.209 (n=1262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.353 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1627)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `14522.6972` → IC=+0.216 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14522.6972 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.209 (n=1206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.208 (n=1316)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.300 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `12841.4798` → IC=+0.212 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12841.4798 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.184 (n=267)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.62 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=281)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `4643.6334` → IC=+0.153 (n=226)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 4643.6334 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.183 (n=276)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.164 (n=555)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.425 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=542)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3846.6396` → IC=+0.158 (n=419)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3846.6396 (IC base=+0.132)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=2271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.140 (n=1921)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.330 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1015)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` < `0.305` → IC=+0.330 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.305 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.240 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `3755.7636` → IC=+0.237 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3755.7636 (IC base=+0.236)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.132 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 11.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.135 (n=527)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.223 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=623)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `1950.0111` → IC=+0.160 (n=351)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 1950.0111 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.171 (n=147)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.081)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.218 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.194 (n=1040)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 12.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.85` → IC=+0.423 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.85 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=948)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.270 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.355 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.182 (n=1088)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.03 (IC base=+0.177)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.184 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` > `0.743` → IC=+0.345 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.743 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=177)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3428.6555` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3428.6555 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.143 (n=667)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.230 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=321)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `9.0` → IC=-0.298 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=104)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=8806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=8389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.220 (n=3142)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `5339.6996` → IC=+0.342 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5339.6996 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.178 (n=2099)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.180 (n=2192)

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

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.330 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.333 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.314)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.366 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.314)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.182 (n=2065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2073)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=1859)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=1950)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=1651)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.238)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.323 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.320 (n=48)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=1799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.194 (n=1511)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.443 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.444 (n=358)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.450 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.441 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `9523.4542` → IC=+0.462 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9523.4542 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.444 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.459 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `11651.323` → IC=+0.461 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11651.323 (IC base=+0.441)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.452 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.446)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.462 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.446)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.445 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.446)

- **PATRÓN** `libro_liquidez` > `3860.0656` → IC=+0.457 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3860.0656 (IC base=+0.446)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.415)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.429 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.415)

- **PATRÓN** `py_entrada` < `0.932` → IC=+0.411 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.932 (IC base=+0.415)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.421 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.415)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` < `0.795` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=18)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=26125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.237 (n=9971)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.194)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=5335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=4475)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=4765)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.167)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=4637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.226 (n=4826)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.273 (n=1669)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.173 (n=4498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4781)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.168)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=2348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.219 (n=1748)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=1657)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=4322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=4227)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.256 (n=2187)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=4385)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 8.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.192 (n=3465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 12.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.247 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.190)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.202 (n=3939)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.125)

- **PATRÓN** `restante_min` < `4.06` → IC=+0.135 (n=3602)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` < 4.06 (IC base=+0.125)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.146 (n=3984)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.94 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=5279)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.125)

- **PATRÓN** `lag_apertura_s` < `3.35` → IC=+0.151 (n=3593)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 3.35 (IC base=+0.125)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.209 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.131)

- **PATRÓN** `restante_min` < `3.99` → IC=+0.138 (n=1781)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 3.99 (IC base=+0.131)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.147 (n=1888)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.93 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.148 (n=2607)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.131)

- **PATRÓN** `lag_apertura_s` < `4.24` → IC=+0.149 (n=1784)

  - _Acción_: Kelly boost +0.75€ cuando `lag_apertura_s` < 4.24 (IC base=+0.131)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=1959)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.48` → IC=+0.128 (n=2412)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.48 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.147 (n=1815)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.128 (n=2672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 8.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `4.45` → IC=+0.144 (n=2392)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 4.45 (IC base=+0.119)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1614.3793` → IC=+0.297 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1614.3793 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.301 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.275)

- **PATRÓN** `py_entrada` > `0.785` → IC=+0.325 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.785 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `3348.9607` → IC=+0.279 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3348.9607 (IC base=+0.275)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.325 (n=307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.291 (n=438)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.382 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1492.929` → IC=+0.314 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1492.929 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.338 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.332)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.359 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.332)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.375 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.332)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.332)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.370 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.332)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.436 (n=358)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.435 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.433 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.431 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `1854.0504` → IC=+0.437 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1854.0504 (IC base=+0.430)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.436 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.429)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.435 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.437 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.447 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.433 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `2127.0131` → IC=+0.454 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2127.0131 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.375 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.378)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.300 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.289 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.303 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.300 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1367.7996` → IC=+0.289 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.7996 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `ibs_20min` > `0.9773` → IC=+0.231 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9773 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.1504` → IC=+0.248 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1504 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.711` → IC=+0.153 (n=3217)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.711 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.2306` → IC=+0.246 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2306 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `1.0731` → IC=+0.249 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0731 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` < `0.176` → IC=+0.193 (n=3967)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.176 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.3107` → IC=+0.201 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3107 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `1.4704` → IC=+0.197 (n=3831)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4704 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.5721` → IC=+0.128 (n=7231)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.5721 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.5603` → IC=+0.180 (n=455)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.5603 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.3387` → IC=+0.165 (n=2402)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.3387 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.167 (n=1014)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6973 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `0.8696` → IC=+0.171 (n=1537)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.8696 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.2459` → IC=+0.223 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2459 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `1.464` → IC=+0.198 (n=3837)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.464 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.206 (n=3608)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.057)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.191 (n=444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0049 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.183 (n=600)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.007 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.3233` → IC=+0.166 (n=1316)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3233 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.189 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 8.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.067` → IC=+0.278 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.067 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.202 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.166 (n=1210)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.190 (n=1192)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `62.0` → IC=+0.185 (n=970)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 62.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.253 (n=885)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.278 (n=659)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.252 (n=678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.0603` → IC=+0.287 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0603 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.353` → IC=+0.248 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.353 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0691` → IC=+0.235 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0691 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.270 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.7311` → IC=+0.265 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7311 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1733.26` → IC=+0.247 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1733.26 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.232 (n=442)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.240 (n=440)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=1000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.9263` → IC=+0.254 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9263 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.2115` → IC=+0.220 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2115 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.375` → IC=+0.215 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.375 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.865` → IC=+0.236 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.865 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.2653` → IC=+0.226 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2653 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.8751` → IC=+0.216 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8751 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.217 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4881` → IC=+0.226 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4881 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.397` → IC=+0.218 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.397 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `11865.8018` → IC=+0.228 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11865.8018 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.161 (n=941)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0048 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.168 (n=356)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.170 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 18.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.6744` → IC=+0.179 (n=1068)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6744 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1316` → IC=+0.156 (n=949)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1316 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.446` → IC=+0.179 (n=185)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.446 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.150 (n=1068)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.204 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` > `0.615` → IC=+0.143 (n=1068)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.615 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1561` → IC=+0.200 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1561 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4384` → IC=+0.152 (n=959)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4384 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.415` → IC=+0.152 (n=959)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.415 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `12873.5877` → IC=+0.155 (n=712)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 12873.5877 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `310.0` → IC=+0.158 (n=583)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 310.0 (IC base=+0.141)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.191 (n=1289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0057 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.44` → IC=+0.231 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.44 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` < `0.1065` → IC=+0.186 (n=1085)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.1065 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.3792` → IC=+0.176 (n=168)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.3792 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.6649` → IC=+0.182 (n=1202)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.6649 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.192 (n=1464)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.04 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.220 (n=1113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.214 (n=994)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.249 (n=377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` < `0.3878` → IC=+0.232 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3878 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.626` → IC=+0.235 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.626 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.389` → IC=+0.215 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.389 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3647` → IC=+0.261 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3647 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.2947` → IC=+0.221 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2947 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.228 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1888.9584` → IC=+0.232 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1888.9584 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.204 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.213)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.152 (n=90)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1630)

- **PATRÓN** `ibs_20min` > `0.9309` → IC=+0.172 (n=275)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.9309 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` > `0.3321` → IC=+0.337 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3321 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.4846` → IC=+0.340 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4846 (IC base=+0.011)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.256` → IC=+0.137 (n=511)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 4.256 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `0.6001` → IC=+0.389 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6001 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `1.1929` → IC=+0.373 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1929 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.377 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4916` → IC=+0.356 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4916 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `1.8203` → IC=+0.352 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8203 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.353 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 165.0 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` > `0.1626` → IC=+0.192 (n=186)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1626 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `0.8572` → IC=+0.150 (n=344)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8572 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `1.1639` → IC=+0.144 (n=172)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.1639 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2157` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2157 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.5033` → IC=+0.179 (n=416)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.5033 (IC base=-0.003)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.140 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=234)

- **FILTRO** `ibs_20min` < `0.3636` → IC=-0.174 (n=93)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3636
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=189)

- **FILTRO** `ibs_20min` > `0.2778` → IC=-0.128 (n=1676)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2778
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=831)

- **FILTRO** `sigma_ewma_delta_pct` > `8.613` → IC=-0.198 (n=273)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.613
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2234)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `1.1883` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1883 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4558` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4558 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.5788` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5788 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `0.7744` → IC=+0.343 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7744 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` < `0.1442` → IC=+0.319 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1442 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.9536` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.9536 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` > `0.6886` → IC=+0.321 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6886 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` < `0.6485` → IC=+0.201 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6485 (IC base=-0.048)

- **PATRÓN** `volumen_regimen` > `0.9175` → IC=+0.187 (n=148)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.9175 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.1972` → IC=+0.193 (n=177)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1972 (IC base=-0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.1481` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1481 (IC base=-0.048)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.223 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4963 (IC base=-0.048)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6568` → IC=-0.191 (n=412)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=1240)

- **FILTRO** `ibs_20min` < `0.65` → IC=-0.162 (n=1088)

  - _Acción_: SKIP cuando `ibs_20min` < 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=564)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.200 (n=361)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1291)

- **FILTRO** `ibs_20min` > `0.775` → IC=-0.200 (n=625)

  - _Acción_: SKIP cuando `ibs_20min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1879)

- **PATRÓN** `dist_vwap_pct` > `0.9637` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9637 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` < `0.2465` → IC=+0.300 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2465 (IC base=-0.087)

- **PATRÓN** `volumen_regimen` > `0.616` → IC=+0.292 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.616 (IC base=-0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.297 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.087)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.283 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=-0.087)

- **PATRÓN** `dist_vwap_pct` > `0.7589` → IC=+0.269 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7589 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.2521` → IC=+0.239 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2521 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` < `0.728` → IC=+0.239 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.728 (IC base=-0.031)

- **PATRÓN** `volumen_regimen` > `1.0842` → IC=+0.299 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0842 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2549` → IC=+0.265 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2549 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.2413` → IC=+0.256 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2413 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.4817` → IC=+0.234 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4817 (IC base=-0.031)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.236 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=-0.031)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.009` → IC=+0.174 (n=2452)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.009 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8824` → IC=+0.264 (n=3336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8824 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.7125` → IC=+0.280 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7125 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.494` → IC=+0.142 (n=3483)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 3.494 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6774` → IC=+0.235 (n=2227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6774 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.249` → IC=+0.257 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.249 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `1.478` → IC=+0.237 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.478 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.7899` → IC=+0.237 (n=1320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7899 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.278 (n=3445)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.137 (n=2515)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0084 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.5588` → IC=+0.147 (n=6637)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.5588 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.6776` → IC=+0.247 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6776 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.1628` → IC=+0.229 (n=1816)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1628 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.227 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7144 (IC base=+0.066)

- **PATRÓN** `volumen_regimen` > `1.199` → IC=+0.257 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.199 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.2521` → IC=+0.323 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2521 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.6229` → IC=+0.252 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6229 (IC base=+0.066)

- **PATRÓN** `volumen_spike_ratio` > `2.3762` → IC=+0.255 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3762 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.253 (n=2465)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.066)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2353` → IC=-0.141 (n=497)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2353
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1492)

- **FILTRO** `sigma_ewma_delta_pct` > `2.61` → IC=-0.148 (n=509)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.61
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=1151)

- **PATRÓN** `ibs_20min` > `0.864` → IC=+0.252 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.864 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.275` → IC=+0.152 (n=673)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.275 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.302 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.8494` → IC=+0.195 (n=342)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.8494 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.6525` → IC=+0.194 (n=171)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6525 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.209 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` < `0.1791` → IC=+0.472 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1791 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=-0.020)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.467 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **FILTRO** `ibs_20min` > `0.8319` → IC=-0.150 (n=556)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8319
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1670)

- **PATRÓN** `dist_vwap_pct` > `0.3011` → IC=+0.140 (n=248)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.3011 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6498` → IC=+0.132 (n=571)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6498 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.167 (n=82)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4206` → IC=+0.160 (n=207)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4206 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.181 (n=202)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 235.0 (IC base=+0.010)

- **PATRÓN** `dist_vwap_pct` < `0.1009` → IC=+0.215 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1009 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `1.1336` → IC=+0.232 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1336 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.344 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.7997` → IC=+0.220 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7997 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1626` → IC=+0.233 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1626 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `508.0` → IC=+0.210 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 508.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.267 (n=1046)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0953` → IC=+0.247 (n=390)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0953 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.259 (n=433)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.291 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.758` → IC=+0.270 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.758 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.1111` → IC=+0.257 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1111 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `2.3526` → IC=+0.239 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3526 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `3.0923` → IC=+0.249 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.0923 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.256 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.262 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.299 (n=833)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.321 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.3333` → IC=+0.286 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3333 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.885` → IC=+0.298 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.885 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.3448` → IC=+0.301 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3448 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.6193` → IC=+0.280 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6193 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.2115` → IC=+0.282 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2115 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.287 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `1880.9161` → IC=+0.299 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1880.9161 (IC base=+0.278)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.277 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.278)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2414` → IC=-0.209 (n=331)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2414
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=993)

- **FILTRO** `ibs_20min` > `0.8182` → IC=-0.182 (n=438)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8182
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1316)

- **PATRÓN** `ibs_20min` > `0.8031` → IC=+0.142 (n=451)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.8031 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.3052` → IC=+0.226 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3052 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` < `0.9592` → IC=+0.215 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9592 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` > `0.6162` → IC=+0.192 (n=258)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` > 0.6162 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.306 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.4915` → IC=+0.273 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4915 (IC base=-0.017)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.244 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 171.0 (IC base=-0.017)

- **PATRÓN** `dist_vwap_pct` > `0.122` → IC=+0.177 (n=97)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.122 (IC base=-0.023)

- **PATRÓN** `dist_vwap_pct` < `0.4439` → IC=+0.156 (n=222)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.4439 (IC base=-0.023)

- **PATRÓN** `volumen_regimen` < `0.9634` → IC=+0.154 (n=180)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.9634 (IC base=-0.023)

- **PATRÓN** `volumen_regimen` > `0.7109` → IC=+0.165 (n=183)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.7109 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.787` → IC=+0.241 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.787 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.4157` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4157 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.224 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 151.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.6667` → IC=-0.203 (n=793)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=809)

- **FILTRO** `ibs_20min` > `0.7188` → IC=-0.235 (n=425)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7188
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=1279)

- **FILTRO** `sigma_ewma_delta_pct` > `4.704` → IC=-0.168 (n=402)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.704
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=1302)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.252 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.782` → IC=+0.339 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.782 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.289 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` > `0.636` → IC=+0.276 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.636 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.1084` → IC=+0.278 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1084 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.327 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4442` → IC=+0.311 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4442 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.323 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.027)

- **PATRÓN** `ibs_20min` < `0.1154` → IC=+0.188 (n=427)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.1154 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` > `0.5672` → IC=+0.205 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5672 (IC base=+0.001)

- **PATRÓN** `dist_vwap_pct` < `0.3844` → IC=+0.179 (n=341)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.3844 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` < `0.7154` → IC=+0.250 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7154 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.0994` → IC=+0.174 (n=299)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.0994 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2178` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2178 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `2.6339` → IC=+0.200 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6339 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `1.5131` → IC=+0.174 (n=308)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.5131 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.206 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0149` → IC=+0.323 (n=677)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0149 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.283 (n=473)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.341 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.1852` → IC=+0.313 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1852 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.383` → IC=+0.296 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.383 (IC base=+0.267)

- **PATRÓN** `volumen_regimen` > `0.8551` → IC=+0.294 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8551 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.11` → IC=+0.269 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.11 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2365` → IC=+0.297 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2365 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5515` → IC=+0.274 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5515 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.2134` → IC=+0.271 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2134 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.270 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `2574.954` → IC=+0.273 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2574.954 (IC base=+0.267)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.276 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0203` → IC=+0.295 (n=500)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0203 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.282 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.3853` → IC=+0.304 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3853 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.5389` → IC=+0.285 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5389 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.406` → IC=+0.286 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.406 (IC base=+0.267)

- **PATRÓN** `volumen_regimen` > `1.2464` → IC=+0.310 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2464 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.243` → IC=+0.358 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.243 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `2.5563` → IC=+0.264 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5563 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `1.4364` → IC=+0.259 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4364 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.268 (n=803)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `2550.1344` → IC=+0.276 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2550.1344 (IC base=+0.267)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.181 (n=1951)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0047 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.201 (n=1949)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3346` → IC=+0.175 (n=5143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3346 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=6118)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.697` → IC=+0.231 (n=5224)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.697 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1647` → IC=+0.199 (n=2585)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1647 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.234` → IC=+0.249 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.234 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.166 (n=3905)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2177 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6232` → IC=+0.162 (n=3903)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6232 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1071` → IC=+0.186 (n=2288)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1071 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `2.311` → IC=+0.170 (n=4880)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.311 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6793` → IC=+0.168 (n=1849)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.6793 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3825.7125` → IC=+0.175 (n=1948)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3825.7125 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.185 (n=4755)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 124.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.186 (n=3755)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0063 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0785` → IC=+0.206 (n=1874)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0785 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=2736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.4585` → IC=+0.227 (n=5616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4585 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.2222` → IC=+0.161 (n=4128)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2222 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.28` → IC=+0.195 (n=979)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.28 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.1842` → IC=+0.154 (n=4105)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1842 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6245` → IC=+0.150 (n=4104)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6245 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2926` → IC=+0.227 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2926 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5744` → IC=+0.169 (n=2185)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5744 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.283` → IC=+0.177 (n=2251)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.283 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.171 (n=4575)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 126.0 (IC base=+0.170)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.221 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.205 (n=445)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3159` → IC=+0.204 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3159 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.218 (n=484)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.073` → IC=+0.308 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.073 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.238 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `2.5605` → IC=+0.183 (n=887)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.5605 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.184 (n=887)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.241 (n=623)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.248 (n=708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0042 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.297 (n=472)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.246 (n=746)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.1059` → IC=+0.268 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1059 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.024` → IC=+0.253 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.024 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0703` → IC=+0.238 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0703 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.260 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.8801` → IC=+0.249 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8801 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.6473` → IC=+0.238 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6473 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1904.7343` → IC=+0.261 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.7343 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.241 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.243 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.359` → IC=+0.177 (n=847)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.359 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.200 (n=588)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.4506` → IC=+0.224 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4506 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.2181` → IC=+0.214 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2181 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.578` → IC=+0.234 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.578 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.268` → IC=+0.178 (n=847)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 1.268 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.192 (n=186)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.4115` → IC=+0.201 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4115 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `9645.5725` → IC=+0.185 (n=847)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 9645.5725 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `408.0` → IC=+0.166 (n=677)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 408.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.178 (n=841)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.2863` → IC=+0.166 (n=955)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2863 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.167 (n=885)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.5219` → IC=+0.194 (n=955)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5219 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1347` → IC=+0.167 (n=957)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.1347 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.047` → IC=+0.216 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.047 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.1987` → IC=+0.164 (n=955)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1987 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.193 (n=291)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.159 (n=846)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.4146` → IC=+0.153 (n=846)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4146 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.160 (n=254)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 231.0 (IC base=+0.149)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.198 (n=962)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0058 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.1968` → IC=+0.197 (n=642)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1968 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.283 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.578` → IC=+0.262 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.578 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.1074` → IC=+0.188 (n=790)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.1074 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.6803` → IC=+0.184 (n=299)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.6803 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `3.6551` → IC=+0.204 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.6551 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.204 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.236 (n=805)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.0894` → IC=+0.242 (n=269)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0894 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.271 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.3478` → IC=+0.251 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3478 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.269 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.274 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `3.5248` → IC=+0.246 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.5248 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1889.461` → IC=+0.244 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1889.461 (IC base=+0.222)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.185 (n=811)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0065 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.4224` → IC=+0.171 (n=922)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.4224 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.167 (n=929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.4125` → IC=+0.207 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4125 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1337` → IC=+0.196 (n=617)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1337 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.198` → IC=+0.246 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.198 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.8636` → IC=+0.166 (n=615)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8636 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `1.1989` → IC=+0.176 (n=307)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.1989 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.228 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.4065` → IC=+0.175 (n=300)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4065 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.5456` → IC=+0.185 (n=300)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.5456 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `7297.5544` → IC=+0.195 (n=614)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7297.5544 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.168 (n=758)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 155.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.159 (n=863)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.006 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.3739` → IC=+0.142 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3739 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` < `0.6008` → IC=+0.178 (n=979)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6008 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.3348` → IC=+0.136 (n=1061)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.3348 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.142` → IC=+0.187 (n=193)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 12.142 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.138 (n=653)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.856 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` > `0.6086` → IC=+0.128 (n=979)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.6086 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.199 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.128 (n=578)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.7982 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.4806` → IC=+0.149 (n=289)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.4806 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `9930.9704` → IC=+0.150 (n=444)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 9930.9704 (IC base=+0.125)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.149 (n=727)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0077 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=1123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.52` → IC=+0.196 (n=1091)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.52 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `1.0154` → IC=+0.231 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0154 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.399` → IC=+0.251 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.399 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2184` → IC=+0.125 (n=1091)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.2184 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` < `0.1686` → IC=+0.128 (n=1091)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1686 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.8034` → IC=+0.129 (n=699)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.8034 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1120)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2897.8254` → IC=+0.194 (n=495)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2897.8254 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.138 (n=791)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 49.0 (IC base=+0.113)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.140 (n=717)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0072 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.173 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 15.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.537` → IC=+0.207 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.537 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.6893` → IC=+0.144 (n=200)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.6893 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.191` → IC=+0.136 (n=981)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.191 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.336` → IC=+0.152 (n=231)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 7.336 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.0388` → IC=+0.126 (n=946)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.0388 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.179 (n=129)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4623` → IC=+0.129 (n=311)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4623 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` > `2.1743` → IC=+0.142 (n=423)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1743 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `3071.3046` → IC=+0.157 (n=359)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3071.3046 (IC base=+0.113)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` < `0.0271` → IC=+0.202 (n=1045)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0271 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0177` → IC=+0.211 (n=697)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0177 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.1651` → IC=+0.219 (n=460)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1651 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1087)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.7209` → IC=+0.254 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7209 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `1.2325` → IC=+0.232 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2325 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.342` → IC=+0.243 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.342 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.206 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.6086` → IC=+0.211 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6086 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2414` → IC=+0.261 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2414 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1918` → IC=+0.214 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1918 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.8159` → IC=+0.205 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8159 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.202 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `2554.0958` → IC=+0.201 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2554.0958 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.239 (n=366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0161` → IC=+0.208 (n=731)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0161 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.224 (n=367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.218 (n=547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` < `0.4309` → IC=+0.240 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4309 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `1.1261` → IC=+0.219 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1261 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.304` → IC=+0.237 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.304 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6302` → IC=+0.217 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6302 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.279 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.2458` → IC=+0.198 (n=846)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.2458 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4624` → IC=+0.191 (n=961)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4624 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2510.618` → IC=+0.211 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2510.618 (IC base=+0.203)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.150 (n=466)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.152 (n=464)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0087 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.149 (n=465)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=702)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.4019` → IC=+0.170 (n=1392)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.4019 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.8234` → IC=+0.167 (n=202)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.8234 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.713` → IC=+0.168 (n=631)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.713 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.159 (n=798)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8646 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.162 (n=382)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.4361` → IC=+0.161 (n=444)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4361 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.5988` → IC=+0.157 (n=444)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5988 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.146 (n=1535)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `8121.9037` → IC=+0.169 (n=632)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 8121.9037 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.162 (n=1174)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 156.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.156 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0037 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=1471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.6278` → IC=+0.144 (n=1450)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6278 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.836` → IC=+0.132 (n=571)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 3.836 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.139 (n=372)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.167 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` < `2.2445` → IC=+0.128 (n=1218)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.2445 (IC base=+0.108)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3354` → IC=+0.128 (n=310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3354 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.155 (n=285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 10.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.3102` → IC=+0.146 (n=309)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.3102 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.6913` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6913 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.333` → IC=+0.169 (n=146)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.333 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.174 (n=136)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6895 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.0648` → IC=+0.124 (n=131)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0648 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `9462.325` → IC=+0.149 (n=309)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 9462.325 (IC base=+0.111)

- **PATRÓN** `ballena_activa_n` < `148.0` → IC=+0.170 (n=95)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 148.0 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.209 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.336` → IC=+0.143 (n=457)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.336 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.142 (n=412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 7.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.3583` → IC=+0.194 (n=305)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3583 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.384` → IC=+0.133 (n=186)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 4.384 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.7044` → IC=+0.140 (n=409)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.7044 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.205 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.4163` → IC=+0.144 (n=448)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4163 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `1.4203` → IC=+0.128 (n=447)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4203 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.153 (n=145)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 159.0 (IC base=+0.120)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.254 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.210 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.217 (n=143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.239 (n=293)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.2721` → IC=+0.239 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2721 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.3803` → IC=+0.222 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3803 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.116` → IC=+0.239 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.116 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.8293` → IC=+0.208 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8293 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.1573` → IC=+0.224 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1573 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.252` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.252 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.3711` → IC=+0.227 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3711 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.0515` → IC=+0.241 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0515 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=466)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `12421.138` → IC=+0.231 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12421.138 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.122 (n=366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0066 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.134 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 11.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` < `0.3044` → IC=+0.154 (n=244)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.3044 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.514` → IC=+0.150 (n=98)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.514 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2187` → IC=+0.167 (n=61)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2187 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `1.5498` → IC=+0.121 (n=309)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_spike_ratio` > 1.5498 (IC base=+0.097)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3485` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3485
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=322)

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
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 14.0 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.4524` → IC=+0.159 (n=259)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.4524 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` < `0.7183` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.7183 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `2.513` → IC=+0.126 (n=236)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.513 (IC base=+0.078)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.131 (n=204)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 45.0 (IC base=+0.078)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0234` → IC=+0.161 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0234 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.172 (n=117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.177 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 16.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.203 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.76 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `1.0795` → IC=+0.155 (n=198)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 1.0795 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.8813` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.8813 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.164 (n=138)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.174 (n=179)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2497.2192` → IC=+0.152 (n=116)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2497.2192 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0171` → IC=+0.157 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0171 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.0773` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.0773 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.1805` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1805 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.064` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 5.064 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6529` → IC=+0.133 (n=194)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6529 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1201` → IC=+0.126 (n=169)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1201 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.0168` → IC=+0.131 (n=120)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.0168 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.141 (n=154)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 17.0 (IC base=+0.119)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.194 (n=3337)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0085 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=7709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.4768` → IC=+0.213 (n=7348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4768 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.8989` → IC=+0.202 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8989 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.221 (n=3612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.8829` → IC=+0.166 (n=3310)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8829 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.186 (n=1409)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.6486` → IC=+0.182 (n=2329)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.6486 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.172 (n=8773)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.04 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `3787.3248` → IC=+0.172 (n=2450)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3787.3248 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.196 (n=5257)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 95.0 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.195 (n=4512)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0067 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.4738` → IC=+0.184 (n=6760)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4738 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=2619)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5581` → IC=+0.238 (n=6761)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5581 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2328` → IC=+0.164 (n=4200)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2328 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.844` → IC=+0.199 (n=978)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.844 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7023` → IC=+0.158 (n=2054)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.7023 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.2013` → IC=+0.163 (n=1556)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.2013 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2903` → IC=+0.253 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2903 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.304` → IC=+0.191 (n=2734)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.304 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `127.0` → IC=+0.176 (n=5637)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 127.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.224 (n=415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.229 (n=562)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.207 (n=822)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.321 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.362` → IC=+0.292 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.362 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2779` → IC=+0.245 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2779 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.5616` → IC=+0.191 (n=503)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.5616 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.5941` → IC=+0.195 (n=381)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.5941 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `64.0` → IC=+0.220 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 64.0 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.261 (n=857)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.270 (n=870)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.2023` → IC=+0.282 (n=650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2023 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=887)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.256 (n=888)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.288 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.636` → IC=+0.265 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.636 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.301 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.705` → IC=+0.294 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.705 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1735.1348` → IC=+0.267 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1735.1348 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.255 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.256)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.191 (n=389)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0027 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1812` → IC=+0.159 (n=777)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1812 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.6972` → IC=+0.245 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6972 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.3442` → IC=+0.202 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3442 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.88` → IC=+0.162 (n=273)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.88 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.396` → IC=+0.155 (n=1031)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.396 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.2804` → IC=+0.162 (n=1165)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2804 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1544` → IC=+0.181 (n=324)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1544 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.4449` → IC=+0.160 (n=1111)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4449 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7617` → IC=+0.158 (n=741)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7617 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `10658.416` → IC=+0.170 (n=1040)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10658.416 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `496.0` → IC=+0.166 (n=1042)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 496.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.171 (n=913)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0049 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.3218` → IC=+0.170 (n=1038)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3218 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.181 (n=355)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 18.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.6377` → IC=+0.209 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6377 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.7019` → IC=+0.159 (n=168)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.7019 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.1302` → IC=+0.169 (n=935)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1302 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.305` → IC=+0.178 (n=513)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 3.305 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.167 (n=1038)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1888 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1504` → IC=+0.220 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1504 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `2.4236` → IC=+0.171 (n=940)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.4236 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.5148` → IC=+0.165 (n=840)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5148 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `314.0` → IC=+0.171 (n=372)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 314.0 (IC base=+0.157)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.227 (n=1157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.214 (n=1158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=563)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.6777` → IC=+0.249 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6777 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.468` → IC=+0.295 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.468 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.2179` → IC=+0.220 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2179 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `1.6743` → IC=+0.220 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6743 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.231 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 59.0 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.243 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.230)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.231 (n=508)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.257 (n=373)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.269 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.72` → IC=+0.273 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.72 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.3592` → IC=+0.295 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3592 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.7875` → IC=+0.225 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7875 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.2483` → IC=+0.228 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2483 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.242 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `1892.3232` → IC=+0.233 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1892.3232 (IC base=+0.230)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.237 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.230)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.173 (n=549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0038 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4291` → IC=+0.139 (n=1246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4291 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=618)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.7124` → IC=+0.237 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7124 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.5571` → IC=+0.183 (n=355)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.5571 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.295` → IC=+0.169 (n=535)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.295 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8808` → IC=+0.162 (n=831)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8808 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2746` → IC=+0.228 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2746 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.502` → IC=+0.150 (n=527)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.502 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.4658` → IC=+0.161 (n=399)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4658 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8843.5076` → IC=+0.232 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8843.5076 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.149 (n=992)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 167.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.156 (n=879)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0065 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.4315` → IC=+0.152 (n=999)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4315 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.147 (n=499)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 8.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.6877` → IC=+0.187 (n=999)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6877 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.2043` → IC=+0.140 (n=917)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2043 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.14` → IC=+0.191 (n=147)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.14 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8555` → IC=+0.141 (n=666)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8555 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.1764` → IC=+0.157 (n=333)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.1764 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2776` → IC=+0.263 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2776 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.5573` → IC=+0.143 (n=410)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5573 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.4671` → IC=+0.171 (n=311)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.4671 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `11059.2821` → IC=+0.184 (n=333)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 11059.2821 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `196.0` → IC=+0.141 (n=925)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 196.0 (IC base=+0.135)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.178 (n=1274)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.4667 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `1.0059` → IC=+0.193 (n=226)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 1.0059 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.408` → IC=+0.217 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.408 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=884)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2911.4143` → IC=+0.244 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.4143 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.128 (n=933)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 53.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.171 (n=539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0061 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1231` → IC=+0.149 (n=406)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1231 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.153 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 15.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.625` → IC=+0.209 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.625 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.4697` → IC=+0.132 (n=1184)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.4697 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.506` → IC=+0.126 (n=1117)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 2.506 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.7154` → IC=+0.160 (n=536)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7154 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2176` → IC=+0.177 (n=187)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2176 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4615` → IC=+0.140 (n=354)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4615 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.5629` → IC=+0.129 (n=354)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.5629 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2928.3958` → IC=+0.162 (n=406)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2928.3958 (IC base=+0.115)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.217 (n=582)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.205 (n=1139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1854` → IC=+0.235 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1854 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.544` → IC=+0.243 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.544 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `1.2457` → IC=+0.206 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2457 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `0.6263` → IC=+0.209 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6263 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.602` → IC=+0.235 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.602 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.212 (n=1292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2555.945` → IC=+0.212 (n=856)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2555.945 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.242 (n=474)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.219 (n=472)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.204 (n=1332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.199 (n=1491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 18.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.505` → IC=+0.254 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.505 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.8499` → IC=+0.202 (n=1582)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8499 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.973` → IC=+0.264 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.973 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.238 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.253 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.2324` → IC=+0.191 (n=1088)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.2324 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `1.4468` → IC=+0.196 (n=1236)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4468 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=977)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=2493)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.152 (n=2135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0096 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.5322` → IC=+0.153 (n=2423)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.5322 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.160 (n=841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.153 (n=936)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 5.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` > `0.9395` → IC=+0.210 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9395 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1905` → IC=+0.155 (n=818)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1905 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.161 (n=773)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` > `0.9047` → IC=+0.148 (n=994)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.9047 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.1739` → IC=+0.172 (n=663)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1739 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.4594` → IC=+0.162 (n=800)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4594 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.9054` → IC=+0.158 (n=1600)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.9054 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `3470.6302` → IC=+0.148 (n=1615)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3470.6302 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.194 (n=628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.487` → IC=+0.158 (n=1882)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.487 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=721)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.158 (n=703)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.1814` → IC=+0.165 (n=828)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1814 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.7081` → IC=+0.147 (n=344)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.7081 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.241` → IC=+0.149 (n=1862)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.241 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.255` → IC=+0.146 (n=1787)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.255 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0717` → IC=+0.155 (n=891)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0717 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.5707` → IC=+0.146 (n=1863)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.5707 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.8237` → IC=+0.150 (n=1242)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8237 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=2493)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7614.1842` → IC=+0.153 (n=1681)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7614.1842 (IC base=+0.140)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.161 (n=275)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0034 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0921` → IC=+0.186 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0921 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.159 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 6.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.5204` → IC=+0.196 (n=205)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5204 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.2354` → IC=+0.176 (n=140)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2354 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.25` → IC=+0.164 (n=391)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 8.25 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2549` → IC=+0.157 (n=307)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2549 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.8157` → IC=+0.184 (n=204)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.8157 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2313` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2313 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.214 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.3963` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.3963 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `12593.9941` → IC=+0.199 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12593.9941 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.203 (n=378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3655` → IC=+0.149 (n=856)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3655 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.174 (n=311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.1518` → IC=+0.168 (n=377)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.1518 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.6044` → IC=+0.151 (n=388)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6044 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6031` → IC=+0.158 (n=115)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6031 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.225` → IC=+0.161 (n=836)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.225 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8855` → IC=+0.182 (n=571)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8855 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.163 (n=408)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.5773` → IC=+0.146 (n=853)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.5773 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.150 (n=569)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `12053.6057` → IC=+0.149 (n=765)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 12053.6057 (IC base=+0.137)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.197 (n=259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0068 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.191 (n=267)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0101 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.5864` → IC=+0.176 (n=588)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.5864 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.240 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.703` → IC=+0.229 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.703 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2095` → IC=+0.203 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2095 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.3086` → IC=+0.177 (n=391)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.3086 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `2531.8684` → IC=+0.237 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2531.8684 (IC base=+0.169)

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
- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.149 (n=708)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0088 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.143 (n=707)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0045 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.5025` → IC=+0.149 (n=707)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.5025 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.165 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.141 (n=249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 4.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.188` → IC=+0.152 (n=707)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.188 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `1.0099` → IC=+0.177 (n=159)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 1.0099 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.4248` → IC=+0.147 (n=658)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.4248 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.818` → IC=+0.148 (n=709)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 6.818 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.1122` → IC=+0.146 (n=622)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1122 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.6442` → IC=+0.142 (n=707)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.6442 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1777` → IC=+0.161 (n=213)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1777 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.4409` → IC=+0.162 (n=232)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4409 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=657)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `8830.4497` → IC=+0.150 (n=632)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8830.4497 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.168 (n=504)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0071 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.5171` → IC=+0.187 (n=573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.5171 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.205 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.165 (n=386)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 11.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.1001` → IC=+0.166 (n=573)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.1001 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.154` → IC=+0.172 (n=275)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.154 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.3867` → IC=+0.157 (n=575)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.3867 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.041` → IC=+0.168 (n=269)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.041 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6434` → IC=+0.189 (n=191)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6434 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `0.7326` → IC=+0.158 (n=512)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 0.7326 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.184 (n=248)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.1885` → IC=+0.172 (n=495)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.1885 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.4487` → IC=+0.170 (n=562)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4487 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `8151.1111` → IC=+0.171 (n=573)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 8151.1111 (IC base=+0.155)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.150 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=137)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=160)

- **PATRÓN** `ibs_20min` > `0.9848` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.9848 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.125` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 7.125 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.156` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.156 (IC base=+0.025)

- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0138 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.6223` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6223 (IC base=+0.065)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.257` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 4.257 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.128 (n=92)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 68.0 (IC base=+0.065)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0084` → IC=-0.253 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=265)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.223 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=271)

- **FILTRO** `dist_vwap_pct` > `0.1598` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1598
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=193)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.186 (n=415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0051 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.6404` → IC=+0.214 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6404 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.1318` → IC=+0.168 (n=284)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1318 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.216 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `0.6313` → IC=+0.136 (n=234)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6313 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.2901` → IC=+0.229 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2901 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `2.5266` → IC=+0.153 (n=425)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.5266 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=426)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2444.1883` → IC=+0.168 (n=230)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2444.1883 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.0714` → IC=+0.288 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0714 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.131 (n=193)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1598 (IC base=-0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.902` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.902 (IC base=-0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0818` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0818 (IC base=-0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.181 (n=114)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.3987 (IC base=-0.031)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=-0.031)

- **PATRÓN** `libro_liquidez` > `2874.2912` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2874.2912 (IC base=-0.031)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.209 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.111)

- **PATRÓN** `ibs_20min` > `0.5857` → IC=+0.212 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5857 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.192 (n=92)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.739` → IC=+0.136 (n=116)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.739 (IC base=+0.111)

- **PATRÓN** `volumen_regimen` < `1.0552` → IC=+0.142 (n=160)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.0552 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` < `0.0759` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0759 (IC base=+0.111)

- **PATRÓN** `volumen_pendiente_norm` > `0.2692` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2692 (IC base=+0.111)

- **PATRÓN** `volumen_spike_ratio` < `2.0198` → IC=+0.190 (n=127)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.0198 (IC base=+0.111)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=184)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `2938.2254` → IC=+0.141 (n=151)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2938.2254 (IC base=+0.111)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=81)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=72)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.171 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0049 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.141 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.6407` → IC=+0.242 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6407 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.4992` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.4992 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.954` → IC=+0.315 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.954 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.789` → IC=+0.164 (n=123)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.789 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.9231` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.9231 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.3101` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3101 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.7588` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.7588 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `1.3908` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.3908 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.155 (n=192)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `1055.8208` → IC=+0.187 (n=161)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1055.8208 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1021` → IC=+0.188 (n=30)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1021 (IC base=-0.060)

- **PATRÓN** `ibs_20min` < `0.1926` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1926 (IC base=-0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.924` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.924 (IC base=-0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.0562` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0562 (IC base=-0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.7615` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.7615 (IC base=-0.060)

- **PATRÓN** `volumen_spike_ratio` > `1.4506` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4506 (IC base=-0.060)

- **PATRÓN** `libro_liquidez` > `1059.8551` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1059.8551 (IC base=-0.060)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` < `0.6667` → IC=-0.191 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=166)

- **FILTRO** `sigma_h` > `0.0119` → IC=-0.281 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0119
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=76)

- **FILTRO** `ibs_20min` > `0.1176` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1176
  - _Potencial_: sin este filtro IC_bueno=+0.275 (n=38)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.171 (n=86)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.075)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.137 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 14.0 (IC base=+0.075)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.191 (n=166)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.6667 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.8682` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.8682 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.655` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 3.655 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.062` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.062 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `2.5513` → IC=+0.162 (n=146)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.5513 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `397.132` → IC=+0.146 (n=142)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 397.132 (IC base=+0.075)

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

- **FILTRO** `hora_utc` > `10.0` → IC=-0.341 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=72)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=120)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.395 (n=17)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=39)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `drift_60min` |x|> `0.1067` → IC=-0.237 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1067
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

- **FILTRO** `volumen_regimen` < `0.892` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.892
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

- **FILTRO** `sigma_h` < `0.0018` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=38)

- **FILTRO** `ibs_20min` > `0.4141` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4141
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `volumen_regimen` > `0.9045` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9045
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=25)

- **FILTRO** `volumen_regimen` > `0.5996` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.5996
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `volumen_regimen` < `1.0824` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.0824
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.450 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=20)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=18)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.3387` → IC=-0.162 (n=69)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3387
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=210)

- **FILTRO** `dist_vwap_pct` > `0.4212` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4212
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=245)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.152 (n=205)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6522 (IC base=+0.064)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.133 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.041)

- **PATRÓN** `ibs_20min` < `0.234` → IC=+0.126 (n=185)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.234 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.105` → IC=+0.134 (n=91)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 6.105 (IC base=+0.041)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=71)

- **FILTRO** `ibs_20min` < `0.4975` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4975
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=66)

- **FILTRO** `volumen_regimen` < `0.8072` → IC=-0.167 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8072
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=59)

- **PATRÓN** `ibs_20min` > `0.6382` → IC=+0.123 (n=59)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.6382 (IC base=-0.028)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.230 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.1524` → IC=+0.171 (n=80)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1524 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` < `1.0441` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0441 (IC base=+0.090)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=57)

- **FILTRO** `ibs_20min` < `0.7272` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7272
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=57)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=52)

- **FILTRO** `ibs_20min` > `0.3298` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3298
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=71)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.144 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0042 (IC base=+0.058)

- **PATRÓN** `drift_60min` |x|≤ `0.2768` → IC=+0.127 (n=57)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.2768 (IC base=+0.058)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.7272` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.7272 (IC base=+0.058)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `1549.4073` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1549.4073 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.321` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.321 (IC base=+0.021)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2121` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2121
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=33)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.233 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.137)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.155 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0056 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3838` → IC=+0.140 (n=84)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3838 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.159 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 6.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.7143` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.7143 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.6353` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6353 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1961` → IC=+0.153 (n=70)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1961 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.5494` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5494 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `507.9911` → IC=+0.140 (n=84)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 507.9911 (IC base=+0.137)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=434)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2813.2668` → IC=+0.160 (n=154)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2813.2668 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.122 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.090)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=434)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2813.2668` → IC=+0.160 (n=154)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2813.2668 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.122 (n=345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 11.0 (IC base=+0.090)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `11.0` → IC=-0.198 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=73)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=118)

- **FILTRO** `libro_liquidez` < `2359.8786` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `libro_liquidez` < 2359.8786
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=101)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=186)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=172)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1287)

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
- **FILTRO** `liq_usd_total` < `32944.1` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `liq_usd_total` < 32944.1
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=88)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `libro_liquidez` < `15405.8709` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 15405.8709
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `liq_usd_total` > `55522.43` → IC=+0.132 (n=66)

  - _Acción_: Kelly boost +0.66€ cuando `liq_usd_total` > 55522.43 (IC base=+0.011)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `hora_utc` > `13.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=73)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=541)

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
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=427)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=238)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=238)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.996` → IC=-0.131 (n=63)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.996
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=190)

- **FILTRO** `py_entrada` > `0.555` → IC=-0.188 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.555
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=207)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=154)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=154)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=127)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.132 (n=74)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=95)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=71)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=155)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=54)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=40)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=211)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=211)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=79)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=6004)

### MOMENTUM_IBS_15M#BNB#15min
- **FILTRO** `libro_liquidez` < `2151.302` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 2151.302
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=143)

### MOMENTUM_IBS_15M#BTC#15min
- **FILTRO** `ibs_20min` < `0.7683` → IC=-0.154 (n=255)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7683
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=775)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1265)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.177 (n=2509)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=7672)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.172 (n=2623)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=7933)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.216 (n=410)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=1292)

- **FILTRO** `ibs_20min` < `0.7482` → IC=-0.177 (n=425)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7482
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=1277)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.158 (n=433)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=1451)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.194 (n=436)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=1325)

- **FILTRO** `py_entrada` > `0.63` → IC=-0.218 (n=442)

  - _Acción_: SKIP cuando `py_entrada` > 0.63
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=1408)

- **FILTRO** `ibs_20min` > `0.287` → IC=-0.175 (n=462)

  - _Acción_: SKIP cuando `ibs_20min` > 0.287
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=1388)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.200 (n=404)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=1270)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.193 (n=461)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1399)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2308)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2265)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2271)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=264)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `ibs_20min` < `0.7049` → IC=-0.204 (n=113)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7049
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=114)

- **FILTRO** `py_entrada` > `0.635` → IC=-0.348 (n=44)

  - _Acción_: SKIP cuando `py_entrada` > 0.635
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=149)

- **FILTRO** `libro_liquidez` < `2918.5053` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `libro_liquidez` < 2918.5053
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=145)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=592)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.126 (n=7236)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=16745)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.273 (n=5964)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=18017)

- **FILTRO** `ibs_7min` < `0.7088` → IC=-0.235 (n=5995)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7088
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=17986)

- **FILTRO** `ballena_activa_n` > `16.0` → IC=-0.160 (n=8001)

  - _Acción_: SKIP cuando `ballena_activa_n` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=15980)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.223 (n=7475)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=22472)

- **FILTRO** `ibs_7min` > `0.2982` → IC=-0.177 (n=7481)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2982
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=22466)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=897)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2909)

- **FILTRO** `ibs_7min` < `0.7099` → IC=-0.259 (n=1254)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7099
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2552)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.194 (n=942)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=2864)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.147 (n=3518)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1701)

- **FILTRO** `drift_7min_pct` |x|> `0.1081` → IC=-0.121 (n=1773)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1081
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=3446)

- **FILTRO** `ibs_7min` > `0.8` → IC=-0.204 (n=1300)

  - _Acción_: SKIP cuando `ibs_7min` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3919)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.141 (n=956)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=3253)

- **FILTRO** `py_entrada` < `0.36` → IC=-0.252 (n=1051)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=3158)

- **FILTRO** `ibs_7min` < `0.7611` → IC=-0.186 (n=1052)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7611
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=3157)

- **FILTRO** `ballena_activa_n` > `160.0` → IC=-0.171 (n=1051)

  - _Acción_: SKIP cuando `ballena_activa_n` > 160.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=3158)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.257 (n=987)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3255)

- **FILTRO** `ibs_7min` > `0.2504` → IC=-0.171 (n=1060)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2504
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3182)

- **FILTRO** `ballena_activa_n` > `113.0` → IC=-0.161 (n=1438)

  - _Acción_: SKIP cuando `ballena_activa_n` > 113.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=2804)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.182 (n=859)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=2726)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.320 (n=844)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=2741)

- **FILTRO** `drift_7min_pct` |x|> `0.1836` → IC=-0.131 (n=1217)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1836
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=2368)

- **FILTRO** `ibs_7min` < `0.2045` → IC=-0.272 (n=896)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2045
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=2689)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.216 (n=878)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=2707)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.235 (n=1283)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=4189)

- **FILTRO** `ibs_7min` > `0.2654` → IC=-0.157 (n=1860)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2654
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=3612)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.168 (n=2600)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1345)

- **FILTRO** `ibs_7min` < `0.7475` → IC=-0.189 (n=986)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7475
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=2959)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.185 (n=969)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=2976)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.258 (n=987)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3040)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.174 (n=1006)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3021)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.178 (n=987)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=3040)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.238 (n=1060)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=3313)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.205 (n=1082)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3291)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.176 (n=1375)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=4286)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.277 (n=963)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3100)

- **FILTRO** `ibs_7min` < `0.7353` → IC=-0.224 (n=1014)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7353
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3049)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.200 (n=998)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=3065)

- **FILTRO** `py_entrada` > `0.68` → IC=-0.202 (n=1281)

  - _Acción_: SKIP cuando `py_entrada` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=4045)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=938)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.122 (n=43)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=479)

- **FILTRO** `libro_liquidez` < `10498.4421` → IC=-0.159 (n=130)

  - _Acción_: SKIP cuando `libro_liquidez` < 10498.4421
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=392)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=568)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.157 (n=97)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=312)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=523)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=436)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.138 (n=683)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.138 (n=547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `474.7871` → IC=+0.156 (n=219)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 474.7871 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.123 (n=258)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 28.0 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.132)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.199 (n=81)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.134 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 4.0 (IC base=+0.107)

- **PATRÓN** `total_vol_5m` < `384.339` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.339 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `7735.3085` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 7735.3085 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 81.0 (IC base=+0.107)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3998` → IC=+0.188 (n=110)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio` |x|> 0.3998 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.196 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.155)

- **PATRÓN** `total_vol_5m` < `7212.57` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 7212.57 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 37.0 (IC base=+0.155)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.161 (n=107)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.139 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 13.0 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 36.0 (IC base=+0.115)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0057` → IC=-0.302 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=156)

- **FILTRO** `T_h` > `52.6662` → IC=-0.250 (n=182)

  - _Acción_: SKIP cuando `T_h` > 52.6662
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=91)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.225 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=-0.110)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.279 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=34)

- **FILTRO** `T_h` > `57.4676` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `T_h` > 57.4676
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=-0.088)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `267.9719` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `T_h` < 267.9719
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.200 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0091` → IC=-0.217 (n=210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=71)

- **FILTRO** `pct_vs_K` |x|> `2.9509` → IC=-0.422 (n=114)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9509
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=115)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0036` → IC=-0.278 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=78)

- **FILTRO** `pct_vs_K` |x|> `2.7217` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7217
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=68)

- **FILTRO** `T_h` > `144.6177` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `T_h` > 144.6177
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=61)

- **FILTRO** `pct_vs_K` |x|> `3.3729` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3729
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.986` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `T_h` > 135.986
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=57)

- **FILTRO** `pct_vs_K` |x|> `4.2825` → IC=-0.450 (n=18)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2825
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=57)

- **FILTRO** `sigma_h` > `0.01` → IC=-0.250 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=60)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.385 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **FILTRO** `T_h` > `71.0631` → IC=-0.333 (n=58)

  - _Acción_: SKIP cuando `T_h` > 71.0631
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0143` → IC=-0.147 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0143
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=46)

- **FILTRO** `sigma_h` < `0.0068` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=41)

- **FILTRO** `T_h` > `135.9709` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `T_h` > 135.9709
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.357 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.312 (n=14)

- **FILTRO** `T_h` > `87.2992` → IC=-0.403 (n=29)

  - _Acción_: SKIP cuando `T_h` > 87.2992
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.2005` → IC=+0.462 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.462 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.364)

- **PATRÓN** `T_h` > `0.8157` → IC=+0.471 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8157 (IC base=+0.364)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.463 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.458 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.364)

- **PATRÓN** `edge` > `0.1035` → IC=+0.447 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1035 (IC base=+0.403)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.461 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.403)

- **PATRÓN** `T_h` < `0.6781` → IC=+0.426 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6781 (IC base=+0.403)

- **PATRÓN** `T_h` > `0.8294` → IC=+0.426 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8294 (IC base=+0.403)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.485 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.403)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.414 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.403)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.432 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.403)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.472)

- **PATRÓN** `edge` > `0.2135` → IC=+0.471 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2135 (IC base=+0.475)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.473 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.475)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.462 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.475)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.462 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.475)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.475)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.461 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.475)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.466 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.475)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=115)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=217)

- **FILTRO** `streak_estiramiento` > `0.8581` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8581
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=133)

- **PATRÓN** `streak_estiramiento` < `0.4382` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `streak_estiramiento` < 0.4382 (IC base=+0.008)

- **PATRÓN** `streak_estiramiento` < `0.5577` → IC=+0.159 (n=89)

  - _Acción_: Kelly boost +0.80€ cuando `streak_estiramiento` < 0.5577 (IC base=+0.033)

### STREAK_FADE_15M#XRP#15min
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
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=32)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=479)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=485)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=298)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=434)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=879)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=509)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=545)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2272)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1167)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=1175)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.193 (n=343)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0039 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.196 (n=343)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.009 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.0554` → IC=+0.175 (n=343)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0554 (IC base=+0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0589` → IC=+0.176 (n=1027)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.0589 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.341` → IC=+0.211 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.341 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.173 (n=1080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 4.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.194 (n=485)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.617` → IC=+0.242 (n=1027)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.617 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.1084` → IC=+0.173 (n=668)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1084 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.845` → IC=+0.251 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.845 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `5120.698` → IC=+0.188 (n=466)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 5120.698 (IC base=+0.172)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=309)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.216 (n=174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.0624` → IC=+0.253 (n=87)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0624 (IC base=+0.199)

- **PATRÓN** `drift_15min` |x|≤ `0.3748` → IC=+0.208 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3748 (IC base=+0.199)

- **PATRÓN** `delta_ratio_macro` |x|> `0.25` → IC=+0.219 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.25 (IC base=+0.199)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3848` → IC=+0.235 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3848 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.214 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_15` > `0.7746` → IC=+0.266 (n=233)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7746 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.3946` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3946 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.1092` → IC=+0.209 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1092 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.491` → IC=+0.252 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.491 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `13760.2251` → IC=+0.250 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13760.2251 (IC base=+0.199)

### UPDOWN_GBM#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `19.688` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 19.688 (IC base=+0.006)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.154 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0061 (IC base=+0.139)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.146 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0055 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.154 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.139)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1408` → IC=+0.173 (n=163)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.1408 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2698` → IC=+0.173 (n=154)

  - _Acción_: Kelly boost +0.87€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2698 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=254)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.6537` → IC=+0.229 (n=245)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6537 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.5309` → IC=+0.150 (n=275)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.5309 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.996` → IC=+0.212 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.996 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `10076.1613` → IC=+0.155 (n=111)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10076.1613 (IC base=+0.139)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `ibs_15` > `0.2226` → IC=-0.227 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2226
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=41)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.140 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0047 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.172 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0076 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.1727` → IC=+0.160 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1727 (IC base=+0.134)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0638` → IC=+0.162 (n=128)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.0638 (IC base=+0.134)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3249` → IC=+0.197 (n=97)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3249 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.164 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.134)

- **PATRÓN** `ibs_15` > `0.587` → IC=+0.236 (n=142)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.587 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.4283` → IC=+0.144 (n=158)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4283 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=118)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2978.7992` → IC=+0.231 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2978.7992 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.194 (n=70)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 35.0 (IC base=+0.134)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5773` → IC=-0.144 (n=116)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5773
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=532)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `ibs_15` < `0.5` → IC=-0.142 (n=65)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=143)

- **FILTRO** `sigma_ewma_delta_pct` < `8.524` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 8.524
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=24)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.491` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 24.491 (IC base=+0.000)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.524` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 8.524 (IC base=+0.008)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0223` → IC=+0.250 (n=98)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0223 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.202 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.176)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.189 (n=262)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=+0.176)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.279 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.229 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.176)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.267 (n=294)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1729` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1729 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.796` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.796 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `2710.8057` → IC=+0.226 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2710.8057 (IC base=+0.176)

- **PATRÓN** `ibs_15` < `0.1053` → IC=+0.175 (n=318)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.88€ cuando `ibs_15` < 0.1053 (IC base=+0.046)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.391 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.1546` → IC=+0.340 (n=261)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1546 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.345 (n=198)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2954` → IC=+0.369 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2954 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.353 (n=317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.391 (n=265)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` > `0.4172` → IC=+0.372 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4172 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.219` → IC=+0.344 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.219 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.018` → IC=+0.335 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.018 (IC base=+0.336)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.343 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `3940.6708` → IC=+0.350 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3940.6708 (IC base=+0.336)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1204` → IC=+0.342 (n=74)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1204 (IC base=+0.336)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.333 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.336)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.362 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.336)

- **PATRÓN** `drift_60min` |x|≤ `0.1544` → IC=+0.340 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1544 (IC base=+0.336)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1021` → IC=+0.342 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1021 (IC base=+0.336)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1224` → IC=+0.404 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1224 (IC base=+0.336)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.353 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.336)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.336 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.336)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.371 (n=168)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.336)

- **PATRÓN** `dist_vwap_pct` > `0.2515` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2515 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.345 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.336)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.344 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.336)

- **PATRÓN** `libro_liquidez` > `9041.1491` → IC=+0.360 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9041.1491 (IC base=+0.336)

- **PATRÓN** `ballena_activa_n` < `611.0` → IC=+0.401 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 611.0 (IC base=+0.336)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.331 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.347 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.347 (n=57)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.347 (n=129)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.347 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.7601` → IC=+0.393 (n=129)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7601 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.1433` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1433 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.338 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.368 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.024` → IC=+0.331 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.024 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.348 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `2980.3742` → IC=+0.339 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2980.3742 (IC base=+0.333)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.336 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.333)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.198 (n=518)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1557)

- **FILTRO** `ibs_15` < `0.6009` → IC=-0.186 (n=173)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6009
  - _Potencial_: sin este filtro IC_bueno=+0.252 (n=519)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.169 (n=653)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1422)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2866` → IC=+0.219 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2866 (IC base=-0.056)

- **PATRÓN** `ibs_15` > `0.6009` → IC=+0.252 (n=519)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6009 (IC base=-0.056)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.172 (n=401)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.056)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1193` → IC=+0.234 (n=697)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1193 (IC base=-0.050)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1822` → IC=+0.234 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1822 (IC base=-0.050)

- **PATRÓN** `ibs_15` < `0.3557` → IC=+0.274 (n=1046)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3557 (IC base=-0.050)

- **PATRÓN** `dist_vwap_pct` > `0.6425` → IC=+0.262 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6425 (IC base=-0.050)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.007` → IC=-0.205 (n=307)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=925)

- **FILTRO** `sigma_h` < `0.0032` → IC=-0.235 (n=308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0032
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=924)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.214 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=445)

- **FILTRO** `sigma_ewma_delta_pct` > `19.843` → IC=-0.242 (n=223)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.843
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=1009)

- **PATRÓN** `sigma_h` < `0.003` → IC=+0.157 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.003 (IC base=+0.079)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1967` → IC=+0.259 (n=52)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1967 (IC base=+0.079)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.079)

- **PATRÓN** `ibs_15` > `0.7946` → IC=+0.346 (n=102)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7946 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.354` → IC=+0.272 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.354 (IC base=+0.079)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6466` → IC=-0.229 (n=83)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6466
  - _Potencial_: sin este filtro IC_bueno=+0.248 (n=252)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=318)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.138 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0064 (IC base=+0.129)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.152 (n=225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0039 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0771` → IC=+0.217 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0771 (IC base=+0.129)

- **PATRÓN** `drift_15min` |x|≤ `0.4157` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `drift_15min` |x|≤ 0.4157 (IC base=+0.129)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0557` → IC=+0.130 (n=252)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio_macro` |x|> 0.0557 (IC base=+0.129)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.217 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.135 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_15` > `0.6466` → IC=+0.248 (n=252)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6466 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1025` → IC=+0.172 (n=178)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1025 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `18.902` → IC=+0.138 (n=269)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 18.902 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=318)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `10550.3134` → IC=+0.207 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10550.3134 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.231 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.3518` → IC=+0.227 (n=386)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3518 (IC base=+0.219)

- **PATRÓN** `drift_15min` |x|≤ `0.7631` → IC=+0.221 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7631 (IC base=+0.219)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2028` → IC=+0.245 (n=198)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2028 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.250 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.229 (n=153)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.219)

- **PATRÓN** `ibs_15` < `0.361` → IC=+0.263 (n=437)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.361 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.729` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.729 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.327` → IC=+0.239 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.327 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `3628.461` → IC=+0.220 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3628.461 (IC base=+0.219)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0509` → IC=-0.147 (n=381)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0509
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=128)

- **FILTRO** `drift_60min` |x|> `0.1649` → IC=-0.214 (n=173)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1649
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=336)

- **FILTRO** `drift_15min` |x|> `0.8398` → IC=-0.229 (n=127)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8398
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=382)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0711` → IC=+0.202 (n=199)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0711 (IC base=-0.045)

- **PATRÓN** `ibs_15` < `0.3667` → IC=+0.238 (n=223)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3667 (IC base=-0.045)

- **PATRÓN** `dist_vwap_pct` < `0.1586` → IC=+0.194 (n=197)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1586 (IC base=-0.045)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0188` → IC=-0.239 (n=309)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0188
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=310)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.252 (n=167)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=452)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1093` → IC=+0.350 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1093 (IC base=-0.050)

- **PATRÓN** `ibs_15` < `0.3273` → IC=+0.297 (n=304)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3273 (IC base=-0.050)

- **PATRÓN** `dist_vwap_pct` > `1.0781` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0781 (IC base=-0.050)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.200 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.062)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.200 (n=18)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.1159` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1159 (IC base=+0.062)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.062)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.200 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.062)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.200 (n=18)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` > `0.1159` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1159 (IC base=+0.062)

- **PATRÓN** `libro_liquidez` > `13398.7443` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13398.7443 (IC base=+0.062)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.294 (n=338)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.289 (n=230)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.313 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1409` → IC=+0.305 (n=337)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1409 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1083` → IC=+0.322 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1083 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.303 (n=526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.329 (n=506)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2735` → IC=+0.325 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2735 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.312 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `12383.1611` → IC=+0.315 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12383.1611 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.295 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.282 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0025 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0604` → IC=+0.304 (n=95)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0604 (IC base=+0.281)

- **PATRÓN** `drift_15min` |x|≤ `0.3845` → IC=+0.283 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3845 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2454` → IC=+0.314 (n=95)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2454 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3622` → IC=+0.297 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3622 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.331 (n=134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.8593` → IC=+0.308 (n=253)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8593 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.332 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.976` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.976 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `11986.1796` → IC=+0.311 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11986.1796 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.304 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.296)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.300 (n=223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.308 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1901` → IC=+0.325 (n=101)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1901 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.328 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.319 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.340 (n=223)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.2764` → IC=+0.311 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2764 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` < `0.4471` → IC=+0.302 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4471 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.334` → IC=+0.311 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.334 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.308 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `10425.7161` → IC=+0.306 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10425.7161 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.301 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0852` → IC=-0.269 (n=63)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0852
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=191)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.250 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=168)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=73)

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
- **PATRÓN** `T_h` > `87.9712` → IC=+0.147 (n=185)

  - _Acción_: Kelly boost +0.74€ cuando `T_h` > 87.9712 (IC base=+0.135)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.328 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.135)

- **PATRÓN** `T_h` > `145.8502` → IC=+0.409 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8502 (IC base=+0.347)

- **PATRÓN** `ratio` > `1.0088` → IC=+0.359 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0088 (IC base=+0.347)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.5528` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `T_h` > 144.5528 (IC base=+0.095)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.286 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.095)

- **PATRÓN** `T_h` > `87.9936` → IC=+0.303 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9936 (IC base=+0.300)

- **PATRÓN** `ratio` > `1.0368` → IC=+0.472 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0368 (IC base=+0.300)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `63.9918` → IC=+0.222 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 63.9918 (IC base=+0.195)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.415 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.195)

- **PATRÓN** `T_h` > `87.9957` → IC=+0.344 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9957 (IC base=+0.326)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.362 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.326)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1131` → IC=+0.457 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1131 (IC base=+0.406)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.617 sube el IC de +0.172 a +0.242 en UPDOWN_GBM#15min (n=1027). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7746 sube el IC de +0.199 a +0.266 en UPDOWN_GBM#BTC#15min (n=233). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6537 sube el IC de +0.139 a +0.229 en UPDOWN_GBM#ETH#15min (n=245). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.587 sube el IC de +0.134 a +0.236 en UPDOWN_GBM#SOL#15min (n=142). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.176 a +0.267 en UPDOWN_GBM#XRP#15min (n=294). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1053 sube el IC de +0.046 a +0.175 en UPDOWN_GBM#XRP#15min (n=318). Ya aplicado como kelly_boost=+0.88€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6009 sube el IC de -0.056 a +0.252 en UPDOWN_GBM_15M_TARDIO (n=519). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3557 sube el IC de -0.050 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=1046). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7946 sube el IC de +0.079 a +0.346 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=102). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6466 sube el IC de +0.129 a +0.248 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=252). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.361 sube el IC de +0.219 a +0.263 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=437). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.146 a +0.342 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3667 sube el IC de -0.045 a +0.238 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=223). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3273 sube el IC de -0.050 a +0.297 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=304). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.288 a +0.329 en UPDOWN_GBM_IBS_ALTO (n=506). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8593 sube el IC de +0.281 a +0.308 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=253). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.296 a +0.340 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=223). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.336 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=265). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.336 a +0.371 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=168). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7601 sube el IC de +0.333 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=129). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL` — IC=+0.378 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1127 | +0.081 | +122.57€ | 2 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1127 | +0.081 | +122.57€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 816 | +0.087 | +100.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 816 | +0.087 | +100.54€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 234 | +0.047 | +5.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 234 | +0.047 | +5.08€ | 4 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 51 | +0.160 | +18.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 51 | +0.160 | +18.45€ | 0 | 2 |
| ✅ BALLENAS_TARDIAS | 19823 | -0.107 | -2900.01€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1187 | -0.036 | -203.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 18636 | -0.111 | -2696.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3122 | -0.123 | -567.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3122 | -0.123 | -567.75€ | 2 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1187 | -0.036 | -203.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1187 | -0.036 | -203.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 374 | -0.136 | -161.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 374 | -0.136 | -161.05€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 5752 | -0.056 | -585.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 5752 | -0.056 | -585.01€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 5195 | -0.115 | -412.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 5195 | -0.115 | -412.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 4193 | -0.172 | -970.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 4193 | -0.172 | -970.36€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 11303 | -0.044 | +4269.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 3056 | -0.008 | +1845.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 8247 | -0.058 | +2424.06€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 11303 | -0.044 | +4269.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 3056 | -0.008 | +1845.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 8247 | -0.058 | +2424.06€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 750 | -0.106 | -123.08€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 36 | -0.132 | -11.07€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 714 | -0.105 | -112.01€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 21 | -0.109 | +1.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 21 | -0.109 | +1.43€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 436 | -0.082 | -68.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 24 | -0.154 | -8.48€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 412 | -0.077 | -59.66€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 200 | -0.168 | -48.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 12 | -0.043 | -2.59€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 188 | -0.174 | -45.86€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 56 | -0.035 | -5.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 56 | -0.035 | -5.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 37 | -0.141 | -2.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 37 | -0.141 | -2.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 71625 | +0.114 | -3728.82€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 11276 | +0.183 | -353.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 273 | -0.118 | -49.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 55070 | +0.100 | -3225.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 5006 | +0.116 | -100.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 9179 | +0.096 | -868.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 36 | -0.158 | -1.29€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 9128 | +0.098 | -855.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 14484 | +0.132 | -272.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 3430 | +0.203 | -101.19€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 9126 | +0.110 | -169.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 1886 | +0.117 | +20.59€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 9221 | +0.089 | -912.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 43 | -0.056 | -3.06€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 9163 | +0.091 | -898.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 15348 | +0.125 | -293.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 4343 | +0.171 | -81.29€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 9194 | +0.109 | -157.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 1799 | +0.099 | -46.36€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 14197 | +0.117 | -808.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 3388 | +0.186 | -171.01€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 176 | -0.073 | +4.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 9312 | +0.092 | -566.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1321 | +0.137 | -74.81€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 9196 | +0.102 | -572.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 36 | -0.026 | +4.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 9147 | +0.103 | -577.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 11326 | +0.189 | -771.66€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 11326 | +0.189 | -771.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 2795 | +0.168 | -300.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 2795 | +0.168 | -300.47€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 540 | +0.190 | +19.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 540 | +0.190 | +19.14€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 2748 | +0.177 | -256.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 2748 | +0.177 | -256.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 2471 | +0.238 | -68.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 2471 | +0.238 | -68.72€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 2693 | +0.191 | -179.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 2693 | +0.191 | -179.32€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 524 | +0.441 | -1.78€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 524 | +0.441 | -1.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 202 | +0.441 | +0.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 202 | +0.441 | +0.20€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 200 | +0.446 | +2.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 200 | +0.446 | +2.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 116 | +0.415 | -5.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 116 | +0.415 | -5.05€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 38670 | +0.194 | -3291.14€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 38670 | +0.194 | -3291.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 6746 | +0.167 | -884.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 6746 | +0.167 | -884.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 6114 | +0.223 | -230.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 6114 | +0.223 | -230.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 6703 | +0.168 | -862.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 6703 | +0.168 | -862.25€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 6212 | +0.218 | -261.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 6212 | +0.218 | -261.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 6387 | +0.202 | -442.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 6387 | +0.202 | -442.86€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 6508 | +0.190 | -609.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 6508 | +0.190 | -609.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 14368 | +0.125 | +289.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 14368 | +0.125 | +289.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 7121 | +0.131 | +212.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 7121 | +0.131 | +212.93€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 7247 | +0.119 | +76.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 7247 | +0.119 | +76.55€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1220 | +0.288 | -23.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1220 | +0.288 | -23.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 539 | +0.275 | -17.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 539 | +0.275 | -17.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 582 | +0.291 | -4.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 582 | +0.291 | -4.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 99 | +0.332 | -1.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 99 | +0.332 | -1.14€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 539 | +0.430 | -8.77€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 539 | +0.430 | -8.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 251 | +0.429 | -4.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 251 | +0.429 | -4.69€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 249 | +0.432 | -3.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 249 | +0.432 | -3.80€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 39 | +0.378 | -0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 39 | +0.378 | -0.28€ | 0 | 1 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 812 | +0.071 | -38.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 285 | +0.068 | -19.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 527 | +0.073 | -19.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 51 | +0.123 | +2.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 51 | +0.123 | +2.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 634 | +0.079 | -17.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 107 | +0.105 | +1.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 527 | +0.073 | -19.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 127 | +0.012 | -23.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 127 | +0.012 | -23.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 25157 | +0.099 | -769.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 2126 | +0.093 | +24.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 23031 | +0.099 | -793.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 14395 | +0.102 | -221.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 2126 | +0.093 | +24.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 12269 | +0.104 | -246.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 4296 | +0.115 | +36.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 4296 | +0.115 | +36.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 6466 | +0.078 | -583.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 6466 | +0.078 | -583.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 707 | +0.257 | -91.26€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 707 | +0.257 | -91.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 707 | +0.257 | -91.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 707 | +0.257 | -91.26€ | 0 | 4 |
| ✅ GBM_LATE_15M | 18787 | +0.074 | +8432.87€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 18787 | +0.074 | +8432.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 3071 | +0.196 | +2264.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 3071 | +0.196 | +2264.66€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 2754 | +0.177 | +1860.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2754 | +0.177 | +1860.58€ | 0 | 26 |
| ✅ GBM_LATE_15M#DOGE | 3200 | +0.195 | +2330.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 3200 | +0.195 | +2330.58€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 2817 | +0.002 | +421.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2817 | +0.002 | +421.85€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 2789 | -0.039 | +609.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2789 | -0.039 | +609.81€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 4156 | -0.053 | +945.39€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 4156 | -0.053 | +945.39€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 19851 | +0.076 | +9870.34€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 19851 | +0.076 | +9870.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 3649 | +0.012 | +1938.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 3649 | +0.012 | +1938.13€ | 2 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 4195 | +0.004 | +777.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 4195 | +0.004 | +777.05€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 2802 | +0.256 | +2753.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 2802 | +0.256 | +2753.53€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 3078 | -0.020 | +340.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 3078 | -0.020 | +340.33€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 3306 | +0.013 | +1155.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 3306 | +0.013 | +1155.05€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2821 | +0.267 | +2906.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2821 | +0.267 | +2906.25€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 15277 | +0.170 | +11150.24€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 15277 | +0.170 | +11150.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 2247 | +0.210 | +1811.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 2247 | +0.210 | +1811.54€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 2402 | +0.157 | +1701.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 2402 | +0.157 | +1701.55€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 2354 | +0.204 | +1836.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 2354 | +0.204 | +1836.31€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 2533 | +0.141 | +1696.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 2533 | +0.141 | +1696.36€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 2887 | +0.113 | +1859.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 2887 | +0.113 | +1859.78€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 2854 | +0.202 | +2244.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 2854 | +0.202 | +2244.70€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 3789 | +0.124 | +1506.19€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 3789 | +0.124 | +1506.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 129 | +0.111 | +49.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 129 | +0.111 | +49.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1021 | +0.117 | +400.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1021 | +0.117 | +400.44€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 368 | +0.149 | +182.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1057 | +0.152 | +493.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1057 | +0.152 | +493.73€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 724 | +0.074 | +174.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 724 | +0.074 | +174.16€ | 1 | 9 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 490 | +0.132 | +205.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 490 | +0.132 | +205.15€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO | 18809 | +0.173 | +13532.40€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 18809 | +0.173 | +13532.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 2936 | +0.222 | +2486.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 2936 | +0.222 | +2486.99€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 2935 | +0.153 | +1921.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 2935 | +0.153 | +1921.77€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 3032 | +0.221 | +2553.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 3032 | +0.221 | +2553.27€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 2992 | +0.136 | +1933.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 2992 | +0.136 | +1933.63€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 3318 | +0.106 | +1860.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 3318 | +0.106 | +1860.12€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 3596 | +0.202 | +2776.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 3596 | +0.202 | +2776.63€ | 0 | 24 |
| ✅ GBM_LATE_5M | 5738 | +0.142 | +3139.12€ | 1 | 25 |
| ✅ GBM_LATE_5M#5min | 5738 | +0.142 | +3139.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 526 | +0.178 | +351.31€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 526 | +0.178 | +351.31€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1549 | +0.141 | +953.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1549 | +0.141 | +953.78€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 842 | +0.175 | +550.00€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 842 | +0.175 | +550.00€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 1705 | +0.147 | +936.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 1705 | +0.147 | +936.84€ | 0 | 29 |
| ✅ GBM_LATE_5M#SOL | 311 | +0.043 | +49.44€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 311 | +0.043 | +49.44€ | 2 | 7 |
| ✅ GBM_LATE_5M#XRP | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 805 | +0.111 | +297.75€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1180 | +0.063 | +429.75€ | 3 | 17 |
| ✅ GBM_LATE_60M#60min | 1180 | +0.063 | +429.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 413 | +0.088 | +149.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 413 | +0.088 | +149.83€ | 0 | 17 |
| ✅ GBM_LATE_60M#ETH | 393 | +0.070 | +180.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 393 | +0.070 | +180.38€ | 2 | 19 |
| ✅ GBM_LATE_60M#SOL | 374 | +0.027 | +99.54€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 374 | +0.027 | +99.54€ | 3 | 10 |
| 🚫 GBM_LATE_60M_FADE | 283 | -0.279 | -33.56€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 283 | -0.279 | -33.56€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 108 | -0.227 | -8.73€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 108 | -0.227 | -8.73€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 94 | -0.323 | -18.43€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 94 | -0.323 | -18.43€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 81 | -0.283 | -6.40€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 81 | -0.283 | -6.40€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 552 | +0.052 | +85.47€ | 2 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 552 | +0.052 | +85.47€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 207 | +0.041 | +21.45€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 207 | +0.041 | +21.45€ | 3 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 169 | +0.038 | -1.81€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 169 | +0.038 | -1.81€ | 4 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 176 | +0.079 | +65.84€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 176 | +0.079 | +65.84€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN | 56 | +0.241 | +31.18€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 56 | +0.241 | +31.18€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 56 | +0.241 | +31.18€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 56 | +0.241 | +31.18€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 1290 | +0.100 | +349.85€ | 0 | 4 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1290 | +0.100 | +349.85€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1290 | +0.100 | +349.85€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1290 | +0.100 | +349.85€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M | 341 | -0.086 | -34.53€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 341 | -0.086 | -34.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 80 | -0.085 | -7.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 80 | -0.085 | -7.38€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 66 | -0.073 | -6.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 66 | -0.073 | -6.94€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 114 | -0.017 | -3.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 114 | -0.017 | -3.34€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 1485 | -0.004 | -9.83€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 1485 | -0.004 | -9.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 75 | -0.033 | -5.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 75 | -0.033 | -5.22€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 165 | -0.027 | -1.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 165 | -0.027 | -1.96€ | 3 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 101 | -0.053 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 101 | -0.053 | -6.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 588 | +0.029 | +19.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 588 | +0.029 | +19.02€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 459 | -0.008 | -8.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 459 | -0.008 | -8.73€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 97 | -0.066 | -6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 97 | -0.066 | -6.47€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M | 868 | -0.049 | -28.63€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 868 | -0.049 | -28.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 255 | -0.060 | -16.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 255 | -0.060 | -16.48€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 278 | -0.036 | -4.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 278 | -0.036 | -4.33€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 335 | -0.052 | -7.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 335 | -0.052 | -7.82€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 12541 | -0.012 | -186.55€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 12541 | -0.012 | -186.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 2231 | -0.024 | -52.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 2231 | -0.024 | -52.90€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2560 | +0.007 | -18.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2560 | +0.007 | -18.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 2516 | -0.016 | -20.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 2516 | -0.016 | -20.01€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 2977 | -0.018 | -61.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 2977 | -0.018 | -61.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1679 | -0.006 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 20737 | -0.013 | +928.26€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 20737 | -0.013 | +928.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 3586 | +0.009 | +484.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 3586 | +0.009 | +484.27€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 3368 | -0.025 | -24.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 3368 | -0.025 | -24.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 3611 | +0.002 | +299.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 3611 | +0.002 | +299.80€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 3163 | -0.044 | -68.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 3163 | -0.044 | -68.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 3475 | -0.018 | +132.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 3475 | -0.018 | +132.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 3534 | -0.006 | +104.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 3534 | -0.006 | +104.73€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 4674 | -0.034 | -108.38€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 4674 | -0.034 | -108.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1149 | +0.000 | -16.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1149 | +0.000 | -16.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 937 | -0.040 | -27.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 937 | -0.040 | -27.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 41 | -0.128 | -5.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 41 | -0.128 | -5.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 420 | -0.114 | -14.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 420 | -0.114 | -14.21€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1281 | -0.043 | -19.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1281 | -0.043 | -19.00€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 53928 | -0.073 | +1058.53€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 53928 | -0.073 | +1058.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 9025 | -0.082 | +514.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 9025 | -0.082 | +514.53€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 8451 | -0.087 | -292.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 8451 | -0.087 | -292.08€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 9057 | -0.073 | +417.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 9057 | -0.073 | +417.40€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 7972 | -0.094 | -225.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 7972 | -0.094 | -225.19€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 10034 | -0.048 | +268.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 10034 | -0.048 | +268.94€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 9389 | -0.064 | +374.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 9389 | -0.064 | +374.93€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 6665 | -0.021 | -114.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 6665 | -0.021 | -114.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1475 | -0.021 | -16.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1475 | -0.021 | -16.26€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1002 | -0.020 | -30.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1002 | -0.020 | -30.79€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 1469 | -0.013 | -10.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 1469 | -0.013 | -10.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 986 | -0.035 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 986 | -0.035 | -13.75€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 737 | -0.021 | -24.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 737 | -0.021 | -24.17€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 944 | +0.112 | +325.83€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 808 | +0.121 | +313.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 183 | +0.132 | +86.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 183 | +0.132 | +86.57€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 159 | +0.090 | +34.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 159 | +0.090 | +34.51€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 161 | +0.107 | +58.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 161 | +0.107 | +58.69€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 146 | +0.155 | +79.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 146 | +0.155 | +79.67€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 159 | +0.115 | +53.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 159 | +0.115 | +53.80€ | 0 | 4 |
| ✅ PRICE_TARGET_GBM | 451 | -0.094 | -15.12€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 200 | -0.134 | -34.68€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 158 | -0.175 | -37.31€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 42 | +0.023 | +2.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 161 | -0.083 | +3.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 119 | -0.095 | -3.55€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 42 | -0.045 | +6.56€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 90 | -0.022 | +16.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 70 | -0.042 | +10.45€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 20 | +0.045 | +6.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 347 | -0.122 | -30.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 104 | +0.000 | +15.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 510 | -0.221 | -40.74€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 215 | -0.205 | -33.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 183 | -0.197 | -30.77€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 32 | -0.235 | -2.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 180 | -0.242 | -21.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 153 | -0.255 | -25.30€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 27 | -0.155 | +4.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 115 | -0.209 | +13.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 101 | -0.209 | +10.46€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 14 | -0.131 | +3.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 437 | -0.222 | -45.60€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#reach | 73 | -0.207 | +4.86€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 179 | +0.395 | +129.86€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 23 | +0.020 | -2.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 23 | +0.020 | -2.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 43 | +0.344 | +36.85€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 43 | +0.344 | +36.85€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 113 | +0.483 | +95.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 113 | +0.483 | +95.37€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#sniper | 179 | +0.395 | +129.86€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 370 | +0.024 | +5.94€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 370 | +0.024 | +5.94€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 164 | +0.030 | +1.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 164 | +0.030 | +1.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 24 | +0.077 | +2.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 24 | +0.077 | +2.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 40 | -0.048 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 40 | -0.048 | -5.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 142 | +0.028 | +7.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 142 | +0.028 | +7.02€ | 0 | 1 |
| ✅ STREAK_FADE_5M | 2353 | -0.023 | -99.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2353 | -0.023 | -99.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 804 | -0.019 | -26.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 561 | -0.022 | -22.88€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 561 | -0.022 | -22.88€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 151 | -0.043 | -13.92€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 151 | -0.043 | -13.92€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 837 | -0.023 | -36.23€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 837 | -0.023 | -36.23€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 55 | -0.026 | -2.48€ | 1 | 0 |
| ✅ STREAK_FADE_60M#60min | 55 | -0.026 | -2.48€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 35 | -0.095 | -3.94€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 20 | +0.091 | +1.47€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 20 | +0.091 | +1.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 6113 | +0.024 | +97.44€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 6113 | +0.024 | +97.44€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 1962 | +0.023 | +22.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 1962 | +0.023 | +22.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1269 | +0.033 | +37.58€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1269 | +0.033 | +37.58€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 1786 | +0.014 | +4.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 1786 | +0.014 | +4.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1096 | +0.031 | +31.96€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1096 | +0.031 | +31.96€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 5794 | +0.012 | -34.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 5794 | +0.012 | -34.90€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2291 | +0.018 | -0.78€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2291 | +0.018 | -0.78€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2304 | +0.014 | -8.36€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2304 | +0.014 | -8.36€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1199 | -0.006 | -25.77€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1199 | -0.006 | -25.77€ | 2 | 0 |
| ✅ UPDOWN_GBM | 23502 | +0.029 | +1320.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 6371 | +0.056 | +1016.49€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 885 | +0.004 | +8.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 14752 | +0.023 | +297.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 1396 | +0.000 | -4.73€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 2018 | +0.077 | +211.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 269 | +0.127 | +86.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 19 | -0.023 | -0.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 1730 | +0.070 | +125.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 4208 | +0.031 | +281.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 758 | +0.083 | +183.82€ | 0 | 12 |
| ✅ UPDOWN_GBM#BTC#240min | 253 | +0.025 | +7.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 2544 | +0.025 | +86.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 616 | +0.002 | +2.07€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#daily | 37 | -0.115 | +1.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 2809 | +0.033 | +92.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 229 | +0.106 | +55.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 16 | +0.000 | -0.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 2564 | +0.026 | +37.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 4695 | +0.017 | +207.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1744 | +0.042 | +192.97€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 240 | +0.008 | +8.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 2176 | +0.005 | +6.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 503 | -0.003 | -3.92€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 32 | -0.147 | +4.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 6190 | +0.015 | +133.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 1712 | +0.021 | +95.55€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 234 | -0.009 | -2.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 3940 | +0.015 | +43.59€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 277 | +0.002 | -2.88€ | 2 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 27 | -0.155 | -0.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 3580 | +0.039 | +395.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 1659 | +0.077 | +402.73€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 123 | -0.020 | -4.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 1798 | +0.009 | -3.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 96 | -0.143 | +5.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 395 | +0.336 | +108.54€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 395 | +0.336 | +108.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 223 | +0.336 | +55.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 223 | +0.336 | +55.56€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 172 | +0.333 | +52.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 172 | +0.333 | +52.98€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 8634 | -0.051 | +1782.61€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 8634 | -0.051 | +1782.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 401 | -0.051 | +347.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 401 | -0.051 | +347.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 1657 | -0.130 | -15.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 1657 | -0.130 | -15.92€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 139 | +0.117 | +54.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 917 | +0.187 | +507.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 917 | +0.187 | +507.11€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 2782 | -0.064 | +441.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 2782 | -0.064 | +441.62€ | 3 | 4 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 2738 | -0.079 | +447.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 2738 | -0.079 | +447.87€ | 2 | 3 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 92 | +0.043 | +3.89€ | 0 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 92 | +0.043 | +3.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 92 | +0.043 | +3.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 92 | +0.043 | +3.89€ | 0 | 4 |
| ✅ UPDOWN_GBM_IBS_ALTO | 674 | +0.288 | +551.25€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 674 | +0.288 | +551.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 377 | +0.281 | +293.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 377 | +0.281 | +293.72€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 297 | +0.296 | +257.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 297 | +0.296 | +257.53€ | 0 | 13 |
| ✅ UPDOWN_OU_5M | 683 | -0.109 | -79.87€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 683 | -0.109 | -79.87€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 181 | -0.068 | -11.67€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 181 | -0.068 | -11.67€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 66 | -0.176 | -10.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 66 | -0.176 | -10.12€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 58 | -0.200 | -8.54€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 58 | -0.200 | -8.54€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 33 | -0.186 | -6.80€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 1852 | +0.303 | +939.40€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 616 | +0.244 | +99.15€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 655 | +0.291 | +255.97€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 581 | +0.375 | +584.28€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.033 n=347 — no justifica filtro, seguir monitorizando
  - _Datos_: n=347 IC=+0.033 PNL=+24.30€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 441 celda(s) pasan gate riguroso completo de 2010 evaluadas (n>=40) y 2980 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.021 < 0.08 — monitorear
  - _Datos_: n=1709 IC=+0.021 PNL=+95.06€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=655/15 IC=+0.291 PNL=+255.97€ | BTC: n=616/15 IC=+0.244 PNL=+99.15€ | SOL: n=581/15 IC=+0.375 PNL=+584.28€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.084 n=171/60 | contraria IC=+0.119 n=153 | gap=-0.036 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=226, boost estimado=+0.001. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=503/40 IC=-0.003 PNL=-3.92€ | BTC#60min: n=615/40 IC=+0.002 PNL=+2.58€ | SOL#60min: n=277/40 IC=+0.002 PNL=-2.88€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.054 n=248070 | tras_1loss IC=+0.070 n=194141 | tras_2loss IC=+0.037 n=83484/40 | gap=+0.017 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.08 con n=189 PNL=+145.36€
  - _Datos_: n=189 IC=+0.207 PNL=+145.36€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.08 con n=254 PNL=+157.57€
  - _Datos_: n=254 IC=+0.191 PNL=+157.57€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.341 > 0.1 con n=1553 PNL=+929.02€
  - _Datos_: n=1553 IC=+0.341 PNL=+929.02€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=179 IC=+0.058 PNL=+20.88€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=179 IC=+0.058 PNL=+20.88€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=43 IC=+0.189 PNL=+28.53€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=43 IC=+0.189 PNL=+28.53€

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
  - _Estado_: n=1032 IC=+0.003 PNL=-7.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1032 IC=+0.003 PNL=-7.66€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=363 IC=-0.007 PNL=+3.44€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=363 IC=-0.007 PNL=+3.44€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=347 IC=+0.033 PNL=+24.30€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=347 IC=+0.033 PNL=+24.30€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.1 con n=1369 PNL=+778.66€
  - _Datos_: n=1369 IC=+0.172 PNL=+778.66€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=758 IC=+0.083 PNL=+183.82€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=758 IC=+0.083 PNL=+183.82€

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
  - _Estado_: n=354 IC=+0.017 PNL=+25.00€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=354 IC=+0.017 PNL=+25.00€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=24 IC=+0.038 PNL=+0.44€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=24 IC=+0.038 PNL=+0.44€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.241 n=56) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=56 IC=+0.241 PNL=+31.18€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.02 con n=541 PNL=+211.63€
  - _Datos_: n=541 IC=+0.126 PNL=+211.63€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=140 IC=-0.056 PNL=+31.39€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=140 IC=-0.056 PNL=+31.39€

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
  - _Estado_: n=7537 IC=+0.053 PNL=+905.41€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=7537 IC=+0.053 PNL=+905.41€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.151 < -0.1 con n=144 PNL=+13.36€
  - _Datos_: n=144 IC=-0.151 PNL=+13.36€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1266 IC=+0.045 PNL=+146.05€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1266 IC=+0.045 PNL=+146.05€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=53 IC=-0.118 PNL=+6.20€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=53 IC=-0.118 PNL=+6.20€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.131 > 0.1 con n=242 PNL=+75.92€
  - _Datos_: n=242 IC=+0.131 PNL=+75.92€

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
  - _Estado_: n=12859 IC=-0.142 PNL=+656.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=12859 IC=-0.142 PNL=+656.12€

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
  - _Estado_: n=1420 IC=+0.140 PNL=+751.03€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1420 IC=+0.140 PNL=+751.03€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.239 < -0.1 con n=1306 PNL=-177.60€
  - _Datos_: n=1306 IC=-0.239 PNL=-177.60€

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
  - _Estado_: 26/40 ops en el filtro definido (IC actual=+0.036 PNL=+7.17€)
  - _Datos_: n=26 IC=+0.036 PNL=+7.17€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.089 n=675) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=675 IC=+0.089 PNL=+158.31€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=372) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=372 IC=+0.414 PNL=+520.78€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=6741 IC=+0.167 PNL=-884.43€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=6741 IC=+0.167 PNL=-884.43€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.213 > 0.1 con n=99 PNL=+62.52€
  - _Datos_: n=99 IC=+0.213 PNL=+62.52€
