# Hipótesis automáticas — 2026-09-25 17:33 UTC
_Generado por shadow_postmortem.py sobre 607936 resoluciones (PNL=+68702.09€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=500)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.236 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.209 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.8026` → IC=+0.257 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8026 (IC base=+0.140)

- **PATRÓN** `banda_z` > `4.083` → IC=+0.164 (n=546)

  - _Acción_: Kelly boost +0.82€ cuando `banda_z` > 4.083 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=585)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3000.2192` → IC=+0.150 (n=364)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3000.2192 (IC base=+0.140)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.123 (n=500)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.143 (n=180)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 94.0 (IC base=+0.052)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.134 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=420)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=366)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.258 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.149)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.210 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.149)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.265 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.149)

- **PATRÓN** `banda_z` > `4.287` → IC=+0.177 (n=438)

  - _Acción_: Kelly boost +0.89€ cuando `banda_z` > 4.287 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=496)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `4494.3377` → IC=+0.150 (n=198)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4494.3377 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11781.953` → IC=+0.121 (n=143)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 11781.953 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.155 (n=140)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 95.0 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.214 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=101)

- **FILTRO** `banda_hit_calibrado` < `0.6297` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6297
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=90)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=107)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=91)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=91)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=104)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.55 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1356.6996` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1356.6996 (IC base=+0.110)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=88)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=-0.008)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `n_ballena_banda` > 26.0 (IC base=+0.154)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.154)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.154)

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
- **FILTRO** `restante_s_al_confirmar` < `146.3` → IC=-0.228 (n=7176)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.3
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=21531)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `137.45` → IC=-0.250 (n=943)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.45
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=2830)

### BALLENAS_TARDIAS#BTC#15min
- **FILTRO** `restante_s_al_confirmar` < `500.82` → IC=-0.146 (n=371)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 500.82
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=1114)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.44` → IC=-0.307 (n=870)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.44
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=2612)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `165.89` → IC=-0.214 (n=1741)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 165.89
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=5224)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.5` → IC=-0.351 (n=1411)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.5
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=4235)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.47` → IC=-0.230 (n=357)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=408)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=174)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=539)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=563)

### CANDIDATA9_BOT_CONSENSO#BTC#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.259 (n=164)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=169)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.218 (n=69)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=234)

### CANDIDATA9_BOT_CONSENSO#ETH#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.270 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=156)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.175 (n=78)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=161)

- **FILTRO** `py_entrada` < `0.47` → IC=-0.167 (n=70)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=169)

### FAVORITO_CONFIRMADO
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.205 (n=14035)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=3540)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5652.3116` → IC=+0.179 (n=2254)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5652.3116 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.138 (n=11579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=14118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=11058)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=5736)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7856.7501` → IC=+0.174 (n=2166)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7856.7501 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1716)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.353 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=2155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `16028.7692` → IC=+0.242 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16028.7692 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.205 (n=1552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.263 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `15869.986` → IC=+0.214 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15869.986 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.171 (n=329)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.615 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `4614.6151` → IC=+0.144 (n=237)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4614.6151 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=828)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=558)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `5859.5725` → IC=+0.162 (n=220)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5859.5725 (IC base=+0.107)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2855)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=2438)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.344 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` < `0.26` → IC=+0.358 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.26 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `3725.7914` → IC=+0.233 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3725.7914 (IC base=+0.232)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.157 (n=467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=608)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 15.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.239 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=553)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `1313.0714` → IC=+0.150 (n=669)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1313.0714 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.434 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.165 (n=592)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 7.0 (IC base=+0.159)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.316 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=734)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.159)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.174 (n=308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 7.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.365 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=188)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `1244.5613` → IC=+0.152 (n=228)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1244.5613 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.146 (n=312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.355` → IC=+0.198 (n=392)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.355 (IC base=+0.111)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.8` → IC=-0.333 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.8
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=11700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=11219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.226 (n=3842)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.339 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `8491.3442` → IC=+0.342 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8491.3442 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=2827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.173 (n=2692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=2681)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.167)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=884)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.245 (n=885)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.354 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.242)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=2638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=2668)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2280)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.249 (n=2461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.326 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.239)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.199 (n=2699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2606)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.197 (n=2008)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.433 (n=539)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.428)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.427 (n=481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `11185.2288` → IC=+0.456 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11185.2288 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.439 (n=212)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.452 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `14347.2058` → IC=+0.443 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14347.2058 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.441 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.458 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `3369.9988` → IC=+0.441 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3369.9988 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.407 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.406)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.407 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.406)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.406)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.408 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.406)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.775` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=34810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.235 (n=15463)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=7074)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=4833)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.190 (n=6498)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.176)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=6246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=6249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.264 (n=3545)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.175 (n=6341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=6326)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.172)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=2362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.210 (n=5768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=2311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=5819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=5823)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.251 (n=2190)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5287)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.126 (n=4900)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.16 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.139 (n=5345)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=6469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.75` → IC=+0.140 (n=4882)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.75 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.198 (n=2664)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.122)

- **PATRÓN** `restante_min` < `4.12` → IC=+0.128 (n=2439)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.12 (IC base=+0.122)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.141 (n=2655)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.138 (n=2799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `lag_apertura_s` < `3.35` → IC=+0.144 (n=2425)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.35 (IC base=+0.122)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=2623)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.126 (n=2460)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=2698)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.27` → IC=+0.140 (n=2464)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.27 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.318 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.289)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `4103.1582` → IC=+0.306 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4103.1582 (IC base=+0.289)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.297 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.275)

- **PATRÓN** `py_entrada` > `0.805` → IC=+0.327 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.805 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `4262.2927` → IC=+0.297 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4262.2927 (IC base=+0.275)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.332 (n=378)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.291)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.394 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `1450.7635` → IC=+0.305 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1450.7635 (IC base=+0.291)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.346 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.341)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.368 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.341)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.384 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.344 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.370 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.341)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.442 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=439)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.437 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.438 (n=240)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.451 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.451 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `1987.6172` → IC=+0.462 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1987.6172 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.389 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.391)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.391)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.305 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.313 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1367.6878` → IC=+0.287 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.6878 (IC base=+0.257)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=54)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=54)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.305 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.257)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.313 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.275 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1367.6878` → IC=+0.287 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1367.6878 (IC base=+0.257)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4866` → IC=+0.123 (n=8236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.4866 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.9822` → IC=+0.244 (n=2745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9822 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.8405` → IC=+0.251 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8405 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.6334` → IC=+0.250 (n=2337)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6334 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.342` → IC=+0.187 (n=2174)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 8.342 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.248 (n=2240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `1.045` → IC=+0.261 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.045 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.3036` → IC=+0.223 (n=826)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3036 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` > `1.4622` → IC=+0.203 (n=5658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4622 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.133 (n=9947)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5714 (IC base=+0.065)

- **PATRÓN** `dist_vwap_pct` > `0.6154` → IC=+0.202 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6154 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` < `0.6983` → IC=+0.185 (n=1536)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6983 (IC base=+0.065)

- **PATRÓN** `volumen_regimen` > `1.0526` → IC=+0.176 (n=1583)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.0526 (IC base=+0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.1671` → IC=+0.227 (n=1667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1671 (IC base=+0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.5684` → IC=+0.200 (n=5261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5684 (IC base=+0.065)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.210 (n=5681)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=+0.065)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.175 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.005 (IC base=+0.160)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.176 (n=622)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0082 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.166 (n=1855)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.167 (n=1248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 11.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.266 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.211 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.164 (n=1737)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.160)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.244 (n=1260)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0931` → IC=+0.270 (n=471)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0931 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.245 (n=966)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0549` → IC=+0.294 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0549 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.240 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.244 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.259 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4285` → IC=+0.234 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4285 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.238 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.229 (n=950)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.0863` → IC=+0.246 (n=475)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0863 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=1495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.217 (n=1452)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9034` → IC=+0.265 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9034 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.5738` → IC=+0.222 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5738 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.688` → IC=+0.260 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.688 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` < `1.2525` → IC=+0.219 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2525 (IC base=+0.217)

- **PATRÓN** `volumen_regimen` > `1.0799` → IC=+0.228 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0799 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.247 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.3766` → IC=+0.234 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3766 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `12550.7458` → IC=+0.221 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12550.7458 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.168 (n=992)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0775` → IC=+0.168 (n=495)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0775 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.7006` → IC=+0.174 (n=1484)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.7006 (IC base=+0.141)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.157 (n=1324)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.254` → IC=+0.161 (n=237)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.254 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.274` → IC=+0.144 (n=1354)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.274 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.2035` → IC=+0.152 (n=1484)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2035 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.178 (n=393)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4267` → IC=+0.154 (n=1374)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4267 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.4185` → IC=+0.149 (n=1374)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4185 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `235.0` → IC=+0.165 (n=571)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 235.0 (IC base=+0.141)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.206 (n=611)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=1925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.224` → IC=+0.251 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.224 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.2093` → IC=+0.187 (n=1834)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.2093 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.3578` → IC=+0.200 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3578 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.819` → IC=+0.204 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.819 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.193 (n=1299)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.220 (n=1388)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6121` → IC=+0.211 (n=1577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6121 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=735)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.247 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.729` → IC=+0.234 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.729 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.534` → IC=+0.210 (n=1712)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.534 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3526` → IC=+0.274 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3526 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7646` → IC=+0.203 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7646 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.19` → IC=+0.217 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.19 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.215 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1903.1828` → IC=+0.215 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1903.1828 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.214 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.144 (n=102)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2258)

- **PATRÓN** `ibs_20min` > `0.9449` → IC=+0.212 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9449 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1604` → IC=+0.321 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1604 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.7929` → IC=+0.335 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7929 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.739` → IC=+0.160 (n=728)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.739 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.328 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `1.2039` → IC=+0.342 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2039 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.349 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4107` → IC=+0.347 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4107 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.2012` → IC=+0.332 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2012 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.332 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 160.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.68` → IC=+0.207 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.68 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` < `0.8486` → IC=+0.164 (n=572)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8486 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` > `1.1597` → IC=+0.153 (n=286)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1597 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.221 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` > `1.5219` → IC=+0.176 (n=718)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5219 (IC base=+0.018)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.177 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=329)

- **FILTRO** `ibs_20min` < `0.28` → IC=-0.207 (n=97)

  - _Acción_: SKIP cuando `ibs_20min` < 0.28
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=292)

- **FILTRO** `ibs_20min` > `0.25` → IC=-0.125 (n=2230)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=1099)

- **FILTRO** `sigma_ewma_delta_pct` > `8.691` → IC=-0.209 (n=355)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.691
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2974)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.185 (n=195)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.6 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `1.8814` → IC=+0.340 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.8814 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.5952` → IC=+0.274 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5952 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.7776` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7776 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.7487` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7487 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.302 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.125 (n=1099)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.25 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` > `0.7124` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7124 (IC base=-0.043)

- **PATRÓN** `dist_vwap_pct` < `0.9295` → IC=+0.216 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9295 (IC base=-0.043)

- **PATRÓN** `volumen_regimen` < `1.0952` → IC=+0.229 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0952 (IC base=-0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.157` → IC=+0.261 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.157 (IC base=-0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.4205` → IC=+0.268 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4205 (IC base=-0.043)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6568` → IC=-0.185 (n=579)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=1741)

- **FILTRO** `ibs_20min` < `0.7179` → IC=-0.153 (n=1531)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7179
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=789)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.197 (n=424)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1896)

- **FILTRO** `ibs_20min` > `0.77` → IC=-0.203 (n=850)

  - _Acción_: SKIP cuando `ibs_20min` > 0.77
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=2557)

- **PATRÓN** `dist_vwap_pct` > `0.4614` → IC=+0.317 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4614 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.279` → IC=+0.311 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.279 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` < `0.9775` → IC=+0.286 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9775 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.304 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.295 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` < `2.1377` → IC=+0.295 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1377 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.290 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.9063` → IC=+0.273 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9063 (IC base=-0.023)

- **PATRÓN** `volumen_regimen` < `0.7347` → IC=+0.249 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7347 (IC base=-0.023)

- **PATRÓN** `volumen_regimen` > `1.2624` → IC=+0.284 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2624 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.1027` → IC=+0.276 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1027 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.1434` → IC=+0.255 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1434 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5236` → IC=+0.248 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5236 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.242 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.198 (n=3454)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0098 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4762` → IC=+0.188 (n=9251)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4762 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.7682` → IC=+0.285 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7682 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.612` → IC=+0.156 (n=4859)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.612 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6905` → IC=+0.249 (n=3300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6905 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.270 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.4647` → IC=+0.237 (n=1999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4647 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6562` → IC=+0.244 (n=1998)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6562 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.267 (n=5516)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 97.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.159 (n=3429)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0092 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5488` → IC=+0.155 (n=9054)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5488 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7295` → IC=+0.243 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7295 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2531` → IC=+0.240 (n=2877)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2531 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7092` → IC=+0.242 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7092 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.2053` → IC=+0.248 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2053 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2436` → IC=+0.304 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2436 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.6007` → IC=+0.261 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6007 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.3028` → IC=+0.258 (n=1826)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3028 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `84.0` → IC=+0.265 (n=3905)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 84.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2584` → IC=-0.146 (n=712)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2584
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2140)

- **FILTRO** `sigma_ewma_delta_pct` > `4.548` → IC=-0.156 (n=542)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.548
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1831)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.266 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.851` → IC=+0.206 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.851 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2224` → IC=+0.271 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2224 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4309` → IC=+0.168 (n=302)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.4309 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1445` → IC=+0.197 (n=411)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.1445 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.181 (n=409)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 14.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1673` → IC=+0.457 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1673 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.4828` → IC=+0.446 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4828 (IC base=-0.015)

- **PATRÓN** `volumen_spike_ratio` > `1.7555` → IC=+0.440 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7555 (IC base=-0.015)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.474 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.015)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8636` → IC=+0.159 (n=693)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.8636 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.3154` → IC=+0.175 (n=380)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.3154 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6744` → IC=+0.169 (n=854)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6744 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.232 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.194 (n=312)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.3807` → IC=+0.156 (n=312)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.3807 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `243.0` → IC=+0.196 (n=409)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 243.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1623` → IC=+0.223 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1623 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `0.6101` → IC=+0.219 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6101 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.317 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.220 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1553` → IC=+0.241 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1553 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `462.0` → IC=+0.220 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 462.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.285 (n=543)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=1630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.248 (n=1646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.691` → IC=+0.282 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.691 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.1039` → IC=+0.258 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1039 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `3.4099` → IC=+0.264 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.4099 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.254 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1803.227` → IC=+0.249 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1803.227 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.315 (n=592)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.6177` → IC=+0.283 (n=1306)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6177 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.330 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` < `0.0909` → IC=+0.289 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0909 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.812` → IC=+0.294 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.812 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.75` → IC=+0.281 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.75 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` > `0.3403` → IC=+0.309 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3403 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` < `1.7408` → IC=+0.283 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7408 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `2.7242` → IC=+0.288 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7242 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.285 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `1892.3107` → IC=+0.296 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1892.3107 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.286 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.281)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.2958` → IC=-0.184 (n=507)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2958
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=1523)

- **FILTRO** `ibs_20min` > `0.7745` → IC=-0.187 (n=609)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7745
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1831)

- **PATRÓN** `ibs_20min` > `0.8229` → IC=+0.161 (n=691)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.8229 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` > `0.4473` → IC=+0.221 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4473 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.6974` → IC=+0.217 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6974 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.9969` → IC=+0.236 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9969 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` > `0.5902` → IC=+0.216 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5902 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.269 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `1.3994` → IC=+0.266 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3994 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.246 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` > `0.1559` → IC=+0.213 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1559 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` < `0.6853` → IC=+0.200 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6853 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1677` → IC=+0.211 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1677 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.8285` → IC=+0.262 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8285 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.1499` → IC=+0.235 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1499 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.249 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 139.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7273` → IC=-0.193 (n=1094)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=+0.277 (n=1101)

- **FILTRO** `ibs_20min` > `0.6875` → IC=-0.236 (n=562)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6875
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1704)

- **FILTRO** `sigma_ewma_delta_pct` > `4.709` → IC=-0.185 (n=494)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.709
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=1772)

- **PATRÓN** `ibs_20min` > `0.7273` → IC=+0.277 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7273 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.315 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.635` → IC=+0.171 (n=344)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.635 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8684` → IC=+0.303 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8684 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.7306` → IC=+0.296 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7306 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1016` → IC=+0.292 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1016 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2243` → IC=+0.305 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2243 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.421` → IC=+0.323 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.421 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.315 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.582` → IC=+0.120 (n=1496)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.582 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` > `0.7308` → IC=+0.202 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7308 (IC base=+0.014)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.221 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.014)

- **PATRÓN** `volumen_regimen` < `0.7115` → IC=+0.248 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7115 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.212 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.014)

- **PATRÓN** `volumen_pendiente_norm` > `0.0689` → IC=+0.211 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0689 (IC base=+0.014)

- **PATRÓN** `volumen_spike_ratio` < `2.4641` → IC=+0.222 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4641 (IC base=+0.014)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.232 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.014)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.316 (n=894)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.292 (n=632)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.277)

- **PATRÓN** `ibs_20min` > `0.7419` → IC=+0.322 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7419 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2114` → IC=+0.315 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2114 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.301 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.277)

- **PATRÓN** `volumen_regimen` > `0.6233` → IC=+0.289 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6233 (IC base=+0.277)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.326 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.277)

- **PATRÓN** `volumen_spike_ratio` > `2.1481` → IC=+0.296 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1481 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.282 (n=1435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `2637.4126` → IC=+0.293 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2637.4126 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.302 (n=961)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.273)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.284 (n=493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.273)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.277 (n=715)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.273)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.305 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3902 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` > `0.3099` → IC=+0.282 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3099 (IC base=+0.273)

- **PATRÓN** `dist_vwap_pct` < `0.228` → IC=+0.273 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.228 (IC base=+0.273)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.462` → IC=+0.290 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.462 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` < `0.6391` → IC=+0.276 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6391 (IC base=+0.273)

- **PATRÓN** `volumen_regimen` > `1.2435` → IC=+0.307 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2435 (IC base=+0.273)

- **PATRÓN** `volumen_pendiente_norm` > `0.2374` → IC=+0.338 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2374 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` < `1.4259` → IC=+0.278 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4259 (IC base=+0.273)

- **PATRÓN** `volumen_spike_ratio` > `2.1415` → IC=+0.272 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1415 (IC base=+0.273)

- **PATRÓN** `libro_liquidez` > `2630.9346` → IC=+0.277 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2630.9346 (IC base=+0.273)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.170 (n=2688)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.200 (n=2680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.0906` → IC=+0.187 (n=2680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0906 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=8377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `0.5749` → IC=+0.218 (n=8037)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5749 (IC base=+0.167)

- **PATRÓN** `dist_vwap_pct` > `0.1784` → IC=+0.194 (n=3513)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1784 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.335` → IC=+0.255 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.335 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` < `1.2119` → IC=+0.160 (n=5324)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2119 (IC base=+0.167)

- **PATRÓN** `volumen_regimen` > `0.6316` → IC=+0.160 (n=5324)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6316 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2951` → IC=+0.196 (n=1202)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2951 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` < `1.5582` → IC=+0.167 (n=3393)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5582 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `2.6148` → IC=+0.176 (n=2571)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6148 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `2407.6479` → IC=+0.169 (n=5358)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2407.6479 (IC base=+0.167)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.180 (n=6945)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 114.0 (IC base=+0.167)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.181 (n=5120)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0066 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.0814` → IC=+0.207 (n=2558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0814 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=2934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.48` → IC=+0.225 (n=7674)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.48 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` < `0.2356` → IC=+0.157 (n=5561)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.2356 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.343` → IC=+0.192 (n=1301)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 10.343 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.151 (n=5555)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.1737 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.216 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.5585` → IC=+0.164 (n=3074)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5585 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `2.2499` → IC=+0.169 (n=3167)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2499 (IC base=+0.166)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.172 (n=6633)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 115.0 (IC base=+0.166)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.212 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.190 (n=620)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0075 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3425` → IC=+0.206 (n=1365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3425 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=1436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=917)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.308 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.236 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.181 (n=1263)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.248 (n=896)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1889` → IC=+0.287 (n=668)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1889 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.241 (n=906)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3437` → IC=+0.263 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3437 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.34` → IC=+0.248 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.34 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1599` → IC=+0.233 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1599 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2864` → IC=+0.250 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2864 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4205` → IC=+0.265 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4205 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1812.9625` → IC=+0.242 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1812.9625 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.229 (n=400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.0742` → IC=+0.196 (n=399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0742 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=1261)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.4035` → IC=+0.229 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4035 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.2122` → IC=+0.213 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2122 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.481` → IC=+0.236 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.481 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.167 (n=527)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6892 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.0742` → IC=+0.169 (n=542)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.0742 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.211 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.5028` → IC=+0.178 (n=511)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.5028 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.4541` → IC=+0.161 (n=387)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4541 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `11875.7279` → IC=+0.169 (n=1068)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 11875.7279 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.158 (n=1300)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0597` → IC=+0.205 (n=435)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0597 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5665` → IC=+0.187 (n=1300)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.5665 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1346` → IC=+0.159 (n=1289)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1346 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.889` → IC=+0.202 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.889 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2096` → IC=+0.158 (n=1300)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2096 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1553` → IC=+0.154 (n=397)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1553 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.145 (n=1188)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.442 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4211` → IC=+0.136 (n=1188)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4211 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.168 (n=371)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 214.0 (IC base=+0.137)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.220 (n=612)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.2351` → IC=+0.216 (n=900)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2351 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.294 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.435` → IC=+0.273 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.435 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2066` → IC=+0.203 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2066 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.6261` → IC=+0.200 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6261 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.8331` → IC=+0.214 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8331 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.236 (n=985)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.2465` → IC=+0.238 (n=746)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2465 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.276 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.3448` → IC=+0.247 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3448 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.735` → IC=+0.260 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.735 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3546` → IC=+0.265 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3546 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.210 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.2108` → IC=+0.229 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2108 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1900.976` → IC=+0.217 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1900.976 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.206 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.217)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.174 (n=1130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0067 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.4368` → IC=+0.157 (n=1285)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4368 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=1348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.3743` → IC=+0.197 (n=1284)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3743 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.1614` → IC=+0.178 (n=853)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1614 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.228 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.0385` → IC=+0.144 (n=1130)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.0385 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `0.6274` → IC=+0.147 (n=1284)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6274 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.195 (n=201)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.4263` → IC=+0.153 (n=419)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4263 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `2.5072` → IC=+0.168 (n=419)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5072 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `6237.095` → IC=+0.182 (n=856)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 6237.095 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.147 (n=1220)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 162.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.152 (n=1350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0073 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.3855` → IC=+0.142 (n=1349)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3855 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6398` → IC=+0.171 (n=1349)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6398 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.2152` → IC=+0.137 (n=1364)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2152 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.961` → IC=+0.165 (n=476)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.961 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8485` → IC=+0.149 (n=900)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8485 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.187 (n=196)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.7906` → IC=+0.135 (n=818)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.7906 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `10039.916` → IC=+0.156 (n=612)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 10039.916 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.155 (n=662)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0101 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=1489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5143` → IC=+0.205 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5143 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.5201` → IC=+0.199 (n=629)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.5201 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.729` → IC=+0.256 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.729 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2173` → IC=+0.131 (n=1455)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2173 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.6466` → IC=+0.124 (n=1455)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6466 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.125 (n=608)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5436` → IC=+0.139 (n=619)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.5436 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.127 (n=1518)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2898.7698` → IC=+0.195 (n=660)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2898.7698 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.136 (n=1105)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 49.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.156 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0062 (IC base=+0.112)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.161 (n=491)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.129 (n=1492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5682` → IC=+0.210 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5682 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `1.0156` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 1.0156 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.2019` → IC=+0.137 (n=1352)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2019 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.527` → IC=+0.132 (n=305)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 7.527 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.6379` → IC=+0.141 (n=491)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6379 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2741` → IC=+0.156 (n=181)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2741 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `3085.144` → IC=+0.161 (n=491)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3085.144 (IC base=+0.112)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0189` → IC=+0.214 (n=927)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0189 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.1351` → IC=+0.202 (n=464)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1351 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.7396` → IC=+0.257 (n=1243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7396 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.5229` → IC=+0.219 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5229 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.576` → IC=+0.241 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.576 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.204 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2089 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.211 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.267 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.1467` → IC=+0.210 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1467 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4039` → IC=+0.209 (n=1344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4039 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.204 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2831.9152` → IC=+0.208 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2831.9152 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.227 (n=631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.0173` → IC=+0.203 (n=956)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0173 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.219 (n=478)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.219 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=656)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.4384` → IC=+0.244 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4384 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `1.2478` → IC=+0.225 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2478 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.43` → IC=+0.236 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.43 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.632` → IC=+0.213 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.632 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.291 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.2006` → IC=+0.192 (n=1136)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.2006 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.4336` → IC=+0.197 (n=1290)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4336 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2604.6008` → IC=+0.210 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2604.6008 (IC base=+0.202)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.165 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0039 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.173 (n=650)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0089 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.356` → IC=+0.150 (n=1711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.356 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.5385` → IC=+0.188 (n=1739)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5385 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.8737` → IC=+0.175 (n=315)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.8737 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.713` → IC=+0.174 (n=878)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 3.713 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8749` → IC=+0.163 (n=1141)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8749 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `1.214` → IC=+0.154 (n=571)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.214 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.177 (n=536)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.4417` → IC=+0.162 (n=626)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4417 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.2097` → IC=+0.154 (n=850)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.2097 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.152 (n=2205)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `12451.6308` → IC=+0.160 (n=648)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12451.6308 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.167 (n=1726)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 156.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.137 (n=1348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0057 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=2040)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.138 (n=2022)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.6667 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.2153` → IC=+0.121 (n=1792)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.2153 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6987` → IC=+0.127 (n=799)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.6987 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.128 (n=501)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.452` → IC=+0.143 (n=648)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.452 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `2760.1991` → IC=+0.122 (n=1803)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2760.1991 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.121 (n=822)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 29.0 (IC base=+0.110)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3457` → IC=+0.123 (n=483)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.3457 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.150 (n=453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 8.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.2515` → IC=+0.145 (n=483)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.2515 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.3078` → IC=+0.153 (n=171)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.3078 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6182` → IC=+0.150 (n=161)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6182 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `15008.644` → IC=+0.139 (n=322)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 15008.644 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.145 (n=153)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 146.0 (IC base=+0.105)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.216 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.160 (n=639)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6041` → IC=+0.186 (n=562)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6041 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.4828` → IC=+0.152 (n=734)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.4828 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.406` → IC=+0.157 (n=249)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.406 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.218` → IC=+0.143 (n=639)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.218 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.0609` → IC=+0.168 (n=290)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0609 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.194 (n=171)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1106` → IC=+0.157 (n=554)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1106 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.42` → IC=+0.151 (n=629)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.42 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `325.0` → IC=+0.157 (n=534)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 325.0 (IC base=+0.138)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.258 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.201 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.0979` → IC=+0.212 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0979 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `0.6985` → IC=+0.246 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6985 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.1582` → IC=+0.211 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1582 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` < `0.2332` → IC=+0.196 (n=534)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2332 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.948` → IC=+0.225 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.948 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.8389` → IC=+0.200 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8389 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.221 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1605 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2622` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2622 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.218 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.7539` → IC=+0.221 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7539 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `12471.9662` → IC=+0.221 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12471.9662 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.0866` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.0866 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6858` → IC=+0.135 (n=253)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6858 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.132 (n=134)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.3429` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3429
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=500)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.155 (n=297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0073 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1188` → IC=+0.145 (n=150)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.1188 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.164 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 8.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.8906` → IC=+0.242 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8906 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.9739` → IC=+0.226 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9739 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.234` → IC=+0.199 (n=194)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 5.234 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `1.0712` → IC=+0.149 (n=391)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0712 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.1826` → IC=+0.174 (n=127)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1826 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.4827` → IC=+0.153 (n=142)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4827 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.2007` → IC=+0.172 (n=193)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.2007 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=483)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3132.1873` → IC=+0.187 (n=148)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3132.1873 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.5192` → IC=+0.148 (n=402)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.5192 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.7082` → IC=+0.137 (n=177)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.7082 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `1.8403` → IC=+0.156 (n=251)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.8403 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `2554.7355` → IC=+0.122 (n=268)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2554.7355 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.128 (n=345)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 42.0 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0232` → IC=+0.161 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0232 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.183 (n=178)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0068 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2324` → IC=+0.178 (n=119)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2324 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.167 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 16.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.191 (n=179)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.4 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.2434` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2434 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `1.0655` → IC=+0.160 (n=201)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0655 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.0007` → IC=+0.148 (n=157)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.0007 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.6087` → IC=+0.167 (n=178)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6087 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.2548` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2548 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.176 (n=180)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2497.2192` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2497.2192 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.152 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0091 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.139 (n=203)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.6 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.1734` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1734 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.53` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.53 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.0734` → IC=+0.122 (n=178)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.0734 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6515` → IC=+0.132 (n=202)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.6515 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1181` → IC=+0.126 (n=180)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1181 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5435` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.5435 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.8185` → IC=+0.131 (n=63)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.8185 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.142 (n=163)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 17.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.204 (n=3433)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.180 (n=10753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.469` → IC=+0.216 (n=10295)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.469 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9761` → IC=+0.203 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9761 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.859` → IC=+0.234 (n=3783)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.859 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8809` → IC=+0.165 (n=4593)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8809 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.201 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.5938` → IC=+0.186 (n=3302)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.5938 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `1792.5347` → IC=+0.171 (n=10295)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1792.5347 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.195 (n=7861)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 86.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1496` → IC=+0.188 (n=4105)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1496 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=3502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.182 (n=4320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 7.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5669` → IC=+0.237 (n=9329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5669 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2517` → IC=+0.161 (n=5775)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2517 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.036` → IC=+0.200 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.036 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.734` → IC=+0.182 (n=9017)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.734 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7048` → IC=+0.162 (n=2816)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7048 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.2031` → IC=+0.154 (n=2134)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.2031 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2876` → IC=+0.240 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2876 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6167` → IC=+0.192 (n=2859)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6167 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.193 (n=5546)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 48.0 (IC base=+0.181)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.203 (n=581)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.225 (n=580)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.356` → IC=+0.190 (n=1739)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.356 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=1178)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.562` → IC=+0.341 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.562 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.248 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.5623` → IC=+0.198 (n=548)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.5623 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.193 (n=1039)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.256 (n=1372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.259 (n=1373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0045 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.1298` → IC=+0.281 (n=604)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1298 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.265 (n=1245)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.3517` → IC=+0.286 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3517 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.721` → IC=+0.260 (n=1541)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.721 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.278 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.5488` → IC=+0.256 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5488 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6339` → IC=+0.275 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6339 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1808.9325` → IC=+0.260 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1808.9325 (IC base=+0.256)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.192 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0029 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.160 (n=551)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=1729)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3081` → IC=+0.203 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3081 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1337` → IC=+0.184 (n=933)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1337 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.669` → IC=+0.169 (n=294)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.669 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.235` → IC=+0.154 (n=1491)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.235 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.180 (n=551)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6288 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2657` → IC=+0.202 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2657 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.160 (n=1406)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7557` → IC=+0.157 (n=1065)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7557 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `15762.0138` → IC=+0.161 (n=749)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 15762.0138 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `472.0` → IC=+0.158 (n=1531)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 472.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.166 (n=1431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.187 (n=477)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.2708` → IC=+0.239 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2708 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.6891` → IC=+0.158 (n=232)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6891 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.135` → IC=+0.166 (n=1292)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.135 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.493` → IC=+0.161 (n=240)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.493 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.511` → IC=+0.153 (n=1449)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.511 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.1888` → IC=+0.165 (n=1431)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1888 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.196 (n=383)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4038` → IC=+0.161 (n=1333)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.4038 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `1.7535` → IC=+0.166 (n=889)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.7535 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `420.0` → IC=+0.158 (n=1091)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 420.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.246 (n=558)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=1749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1698)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.797` → IC=+0.292 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.797 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.2104` → IC=+0.221 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2104 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.8213` → IC=+0.242 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8213 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.228 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1803.3703` → IC=+0.218 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1803.3703 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.237 (n=1560)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.1686` → IC=+0.237 (n=686)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1686 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.238 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.36` → IC=+0.266 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.36 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.756` → IC=+0.272 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.756 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.3432` → IC=+0.307 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3432 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.7521` → IC=+0.228 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7521 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.184` → IC=+0.234 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.184 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.238 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `1958.2584` → IC=+0.239 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1958.2584 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.229 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.231)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.178 (n=772)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0041 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.145 (n=1755)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=1835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.876` → IC=+0.262 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.876 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3736` → IC=+0.163 (n=696)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3736 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.195` → IC=+0.158 (n=726)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.195 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.8743` → IC=+0.154 (n=1170)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8743 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.217 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `1.5214` → IC=+0.149 (n=748)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.5214 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.767` → IC=+0.149 (n=1132)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.767 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `8024.5486` → IC=+0.234 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8024.5486 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.156 (n=542)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 78.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.160 (n=1258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0066 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.4484` → IC=+0.152 (n=1428)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4484 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=654)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.7054` → IC=+0.181 (n=1428)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.7054 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.5974` → IC=+0.139 (n=1580)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.5974 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.146` → IC=+0.178 (n=212)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.146 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6927` → IC=+0.149 (n=628)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6927 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.1921` → IC=+0.142 (n=476)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1921 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2894` → IC=+0.240 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2894 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4416` → IC=+0.149 (n=1355)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.4416 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7261.8406` → IC=+0.197 (n=648)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 7261.8406 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `177.0` → IC=+0.142 (n=1350)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 177.0 (IC base=+0.136)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.141 (n=1162)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0082 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=1794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.192 (n=1746)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4706 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `1.0924` → IC=+0.198 (n=362)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 1.0924 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.493` → IC=+0.235 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.493 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `0.8932` → IC=+0.136 (n=1162)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8932 (IC base=+0.114)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=1752)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2898.7698` → IC=+0.250 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2898.7698 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.133 (n=1351)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 54.0 (IC base=+0.114)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.175 (n=562)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0058 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.1332` → IC=+0.161 (n=562)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1332 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.125 (n=1744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.205 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2212` → IC=+0.132 (n=1374)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.2212 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.488` → IC=+0.127 (n=1629)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.488 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.717` → IC=+0.152 (n=742)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.717 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.2215` → IC=+0.164 (n=263)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2215 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4441` → IC=+0.143 (n=508)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4441 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2844.2019` → IC=+0.170 (n=562)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2844.2019 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.122 (n=1317)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 51.0 (IC base=+0.113)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0193` → IC=+0.217 (n=1161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0193 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=1816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.209 (n=1562)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.5135` → IC=+0.249 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5135 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.207` → IC=+0.233 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.207 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.208` → IC=+0.271 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.208 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.2457` → IC=+0.211 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2457 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.215 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.247 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.505` → IC=+0.235 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.505 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2633.3465` → IC=+0.220 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2633.3465 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.225 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.200)

- **PATRÓN** `sigma_h` > `0.0257` → IC=+0.220 (n=619)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0257 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.208 (n=1308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.4227` → IC=+0.265 (n=1635)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4227 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `1.2706` → IC=+0.205 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2706 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.9265` → IC=+0.202 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9265 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.826` → IC=+0.252 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.826 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2355` → IC=+0.236 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2355 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.267 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1818` → IC=+0.197 (n=1472)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1818 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.5431` → IC=+0.197 (n=1495)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.5431 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=3131)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.166 (n=2643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0092 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.5198` → IC=+0.166 (n=3003)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.5198 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=1175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.169 (n=1345)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 6.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.215 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.1894` → IC=+0.170 (n=1114)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1894 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.4847` → IC=+0.153 (n=1867)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.4847 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.188` → IC=+0.188 (n=492)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 10.188 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `0.8968` → IC=+0.167 (n=1329)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.8968 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.1706` → IC=+0.191 (n=823)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1706 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4563` → IC=+0.164 (n=989)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4563 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `1.8725` → IC=+0.165 (n=1978)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8725 (IC base=+0.157)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=2120)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `3906.8104` → IC=+0.166 (n=2002)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3906.8104 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.200 (n=788)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.159 (n=2360)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.163 (n=1044)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 6.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.1824` → IC=+0.172 (n=1039)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1824 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.6804` → IC=+0.165 (n=454)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.6804 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.27` → IC=+0.153 (n=2349)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 6.27 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.2441` → IC=+0.148 (n=2258)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2441 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.145 (n=2139)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2198` → IC=+0.145 (n=503)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2198 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `1.4242` → IC=+0.155 (n=777)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4242 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.8137` → IC=+0.145 (n=1553)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.8137 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=3131)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `7275.7832` → IC=+0.154 (n=2108)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7275.7832 (IC base=+0.142)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.185 (n=354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0056 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.184 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0064 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.0895` → IC=+0.201 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0895 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.181 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.5463` → IC=+0.194 (n=269)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5463 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.2158` → IC=+0.177 (n=190)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2158 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.3742` → IC=+0.172 (n=391)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.3742 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.174` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 10.174 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.471` → IC=+0.178 (n=426)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 2.471 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.231` → IC=+0.176 (n=403)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.231 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.8487` → IC=+0.200 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8487 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.3044` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3044 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4501` → IC=+0.193 (n=135)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4501 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6405` → IC=+0.206 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6405 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `12575.9809` → IC=+0.218 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12575.9809 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.217 (n=422)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.179 (n=319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.175 (n=364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1385` → IC=+0.178 (n=420)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1385 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.148 (n=433)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6078 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.174 (n=90)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.2218` → IC=+0.139 (n=969)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2218 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.162 (n=932)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8795` → IC=+0.187 (n=637)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8795 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0682` → IC=+0.165 (n=446)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0682 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.42` → IC=+0.146 (n=317)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.42 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.149 (n=634)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `11474.1256` → IC=+0.153 (n=954)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11474.1256 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `706.0` → IC=+0.144 (n=908)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 706.0 (IC base=+0.139)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.186 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0099 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.5715` → IC=+0.174 (n=623)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.5715 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.994` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.994 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` < `0.3499` → IC=+0.170 (n=749)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.3499 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.204 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `3.3904` → IC=+0.167 (n=622)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3904 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` > `2.2621` → IC=+0.171 (n=414)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2621 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2425.929` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2425.929 (IC base=+0.165)

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

- **PATRÓN** `libro_liquidez` > `2362.106` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.106 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.254)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.168 (n=869)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0073 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.171 (n=988)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0043 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.3873` → IC=+0.165 (n=869)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3873 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.170 (n=337)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 4.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` < `0.545` → IC=+0.172 (n=659)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.545 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.8863` → IC=+0.177 (n=329)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.8863 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.1638` → IC=+0.163 (n=568)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1638 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.4235` → IC=+0.172 (n=918)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.4235 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.134` → IC=+0.174 (n=886)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 4.134 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.0851` → IC=+0.164 (n=869)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.0851 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `0.6431` → IC=+0.167 (n=987)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6431 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.165 (n=909)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.0781` → IC=+0.171 (n=430)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0781 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.4358` → IC=+0.174 (n=323)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4358 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.166 (n=866)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=983)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.185 (n=274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0042 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4985` → IC=+0.175 (n=820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.4985 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.156 (n=583)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 11.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.75` → IC=+0.154 (n=820)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.75 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.0998` → IC=+0.159 (n=819)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.0998 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6151` → IC=+0.180 (n=179)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6151 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.719` → IC=+0.157 (n=843)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 6.719 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6469` → IC=+0.188 (n=274)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6469 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.7218` → IC=+0.151 (n=732)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.7218 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.1513` → IC=+0.152 (n=848)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1513 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.165 (n=344)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.2019` → IC=+0.162 (n=708)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.2019 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7791` → IC=+0.154 (n=535)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7791 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `7578.204` → IC=+0.175 (n=819)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7578.204 (IC base=+0.150)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `ibs_20min` > `0.5405` → IC=+0.150 (n=238)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.5405 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.1981` → IC=+0.147 (n=168)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1981 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.177` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.177 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.212 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` > `1.4255` → IC=+0.134 (n=230)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.4255 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3427.9609` → IC=+0.151 (n=213)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3427.9609 (IC base=+0.102)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.150 (n=224)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0069 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.3998` → IC=+0.156 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3998 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.154 (n=151)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 10.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.1538` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1538 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.5986` → IC=+0.197 (n=107)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.5986 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.684` → IC=+0.129 (n=122)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 2.684 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.9473` → IC=+0.129 (n=149)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.9473 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.0898` → IC=+0.176 (n=171)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.0898 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.867` → IC=+0.133 (n=145)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.867 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `3291.3893` → IC=+0.149 (n=223)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3291.3893 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.156 (n=187)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 49.0 (IC base=+0.115)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.209 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=376)

- **FILTRO** `dist_vwap_pct` > `0.1862` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1862
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=333)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.185 (n=417)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0041 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.125 (n=871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.201 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.157` → IC=+0.157 (n=462)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.157 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.190 (n=201)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.204 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `2.0892` → IC=+0.128 (n=652)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.0892 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2424.4386` → IC=+0.136 (n=377)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2424.4386 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.276 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.5298` → IC=+0.126 (n=241)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.5298 (IC base=+0.005)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.159 (n=323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.006 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.4919` → IC=+0.180 (n=292)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.4919 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.171 (n=153)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` < `0.1568` → IC=+0.131 (n=269)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1568 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `2.0118` → IC=+0.162 (n=223)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.0118 (IC base=+0.102)

- **PATRÓN** `ibs_20min` < `0.0889` → IC=+0.287 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0889 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.71` → IC=+0.147 (n=114)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.71 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.6903` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6903 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.054)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.006` → IC=-0.225 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=117)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=120)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.185 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0041 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.137 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.236 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.348` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.348 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.742` → IC=+0.312 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.742 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` > `0.9325` → IC=+0.134 (n=132)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.9325 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.7281` → IC=+0.177 (n=159)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.7281 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=193)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `1133.3296` → IC=+0.158 (n=255)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1133.3296 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.1674` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1674 (IC base=-0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.956` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.956 (IC base=-0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1353` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1353 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.268` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.268 (IC base=-0.022)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=-0.022)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.271 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=91)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.197 (n=64)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.168 (n=245)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.6667 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.139 (n=153)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.497` → IC=+0.161 (n=110)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 5.497 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `1.0639` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 1.0639 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2436` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2436 (IC base=+0.068)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=-0.040)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.2222 (IC base=-0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.25` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.25 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1368` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1368 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.2847` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.2847 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.3803` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.3803 (IC base=-0.040)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.365 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.169 (n=158)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=193)

- **FILTRO** `volumen_regimen` < `0.7721` → IC=-0.343 (n=68)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7721
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=140)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.367 (n=58)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=114)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=151)

- **FILTRO** `sigma_ewma_delta_pct` > `5.949` → IC=-0.304 (n=49)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.949
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=123)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=70)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2175` → IC=-0.269 (n=37)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2175
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=38)

- **FILTRO** `drift_60min` |x|> `0.1035` → IC=-0.306 (n=34)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1035
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=36)

- **FILTRO** `volumen_regimen` > `0.9309` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9309
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=55)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.899` → IC=-0.413 (n=44)

  - _Acción_: SKIP cuando `ibs_20min` < 0.899
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `volumen_regimen` > `1.1069` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.1069
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=51)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.357 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=38)

- **FILTRO** `ibs_20min` > `0.6404` → IC=-0.367 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6404
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=29)

- **PATRÓN** `ibs_20min` > `0.9883` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9883 (IC base=-0.225)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0073` → IC=-0.300 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=33)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=50)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1832` → IC=-0.129 (n=122)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1832
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=239)

- **FILTRO** `dist_vwap_pct` > `0.6357` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6357
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=336)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.169 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0059 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.132 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 15.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.6382` → IC=+0.160 (n=263)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6382 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.5013` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5013 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1832` → IC=+0.151 (n=239)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1832 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.944` → IC=+0.146 (n=111)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 5.944 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `3805.194` → IC=+0.172 (n=123)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3805.194 (IC base=+0.057)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=94)

- **FILTRO** `ibs_20min` < `0.584` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `ibs_20min` < 0.584
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=86)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.147 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0034 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.2293` → IC=+0.157 (n=106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2293 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.214 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.1108` → IC=+0.203 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1108 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.3016` → IC=+0.132 (n=150)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.3016 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8235` → IC=+0.135 (n=83)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8235 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1172` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.1172 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.123)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.603` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.603
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=69)

- **FILTRO** `ibs_20min` > `0.1832` → IC=-0.159 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1832
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=77)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.288 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0023 (IC base=+0.053)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.603` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.603 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `1529.3843` → IC=+0.125 (n=62)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1529.3843 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.025)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **FILTRO** `dist_vwap_pct` > `0.1432` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1432
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=55)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.226 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.207 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.7027` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7027 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.6943` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6943 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.242 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.7968` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7968 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.396` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.396 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.206 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.0808` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0808 (IC base=-0.037)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.296)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.296)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.365 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `1294.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1294.0 (IC base=+0.296)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.211)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `2.1869` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1869 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.7195` → IC=+0.321 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7195 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.211)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.296)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.365 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.296)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.365 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.296)

- **PATRÓN** `ballena_activa_n` < `1294.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1294.0 (IC base=+0.296)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.211)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `2.1869` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1869 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.7195` → IC=+0.321 (n=26)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7195 (IC base=+0.211)

- **PATRÓN** `ballena_activa_n` < `1770.0` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1770.0 (IC base=+0.211)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2843.9766` → IC=+0.162 (n=329)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2843.9766 (IC base=+0.108)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2843.9766` → IC=+0.162 (n=329)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2843.9766 (IC base=+0.108)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `10.0` → IC=-0.204 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=80)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=133)

- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.173 (n=111)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=213)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=199)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `liq_n` < `4.0` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_n` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.167 (n=16)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1842)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9583` → IC=-0.295 (n=37)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9583
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=82)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

### LIQUIDACIONES_5M#BNB#5min
- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 25.0 (IC base=+0.049)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_usd_total` < `35750.18` → IC=-0.127 (n=65)

  - _Acción_: SKIP cuando `liq_usd_total` < 35750.18
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=132)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

- **FILTRO** `libro_liquidez` < `15247.5472` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 15247.5472
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **PATRÓN** `liq_n` > `18.0` → IC=+0.198 (n=51)

  - _Acción_: Kelly boost +0.99€ cuando `liq_n` > 18.0 (IC base=+0.018)

- **PATRÓN** `liq_usd_total` > `69212.62` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `liq_usd_total` > 69212.62 (IC base=+0.018)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=136)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=807)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=761)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=432)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=184)

- **PATRÓN** `libro_liquidez` > `3962.9688` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3962.9688 (IC base=+0.010)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=633)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=633)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.143 (n=208)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=505)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=366)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=366)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=172)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=109)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=205)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=87)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=90)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=241)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=241)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=130)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.47` → IC=-0.132 (n=474)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=256)

- **FILTRO** `restante_min` < `3.82` → IC=-0.125 (n=238)

  - _Acción_: SKIP cuando `restante_min` < 3.82
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=492)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.170 (n=201)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.47 (IC base=+0.022)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=33)

- **FILTRO** `lag_apertura_s` > `110.07` → IC=-0.176 (n=32)

  - _Acción_: SKIP cuando `lag_apertura_s` > 110.07
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=34)

- **FILTRO** `profundidad_ratio` < `255.7` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `profundidad_ratio` < 255.7
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=50)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=54)

- **PATRÓN** `py_entrada` < `0.54` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.54 (IC base=+0.033)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.56 (IC base=+0.068)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `hora_utc` < `9.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=33)

- **FILTRO** `py_entrada` > `0.47` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=13)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=41)

- **FILTRO** `restante_min` < `3.98` → IC=-0.214 (n=40)

  - _Acción_: SKIP cuando `restante_min` < 3.98
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `lag_apertura_s` > `61.04` → IC=-0.227 (n=42)

  - _Acción_: SKIP cuando `lag_apertura_s` > 61.04
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=34)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.200 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=39)

- **FILTRO** `profundidad_ratio` < `114.6` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `profundidad_ratio` < 114.6
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=45)

- **FILTRO** `restante_min` < `12.89` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `restante_min` < 12.89
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=34)

- **FILTRO** `lag_apertura_s` > `126.34` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `lag_apertura_s` > 126.34
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=34)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `restante_min` < `3.88` → IC=-0.333 (n=40)

  - _Acción_: SKIP cuando `restante_min` < 3.88
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=40)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=64)

- **FILTRO** `lag_apertura_s` > `70.6` → IC=-0.354 (n=39)

  - _Acción_: SKIP cuando `lag_apertura_s` > 70.6
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=41)

- **FILTRO** `profundidad_ratio` < `67.6` → IC=-0.262 (n=40)

  - _Acción_: SKIP cuando `profundidad_ratio` < 67.6
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=40)

- **PATRÓN** `py_entrada` < `0.45` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.45 (IC base=+0.013)

- **PATRÓN** `profundidad_ratio` > `48.0` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `profundidad_ratio` > 48.0 (IC base=+0.013)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **PATRÓN** `restante_min` > `13.48` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `restante_min` > 13.48 (IC base=-0.017)

- **PATRÓN** `lag_apertura_s` < `90.92` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 90.92 (IC base=-0.017)

- **PATRÓN** `py_entrada` < `0.6` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.6 (IC base=+0.049)

- **PATRÓN** `restante_min` > `13.49` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 13.49 (IC base=+0.049)

- **PATRÓN** `lag_apertura_s` < `90.79` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 90.79 (IC base=+0.049)

- **PATRÓN** `profundidad_ratio` > `9.3` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `profundidad_ratio` > 9.3 (IC base=+0.049)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `restante_min` < `3.72` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `restante_min` < 3.72
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=29)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.217 (n=44)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

- **FILTRO** `profundidad_ratio` < `19.6` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `profundidad_ratio` < 19.6
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=69)

- **PATRÓN** `profundidad_ratio` > `13.0` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `profundidad_ratio` > 13.0 (IC base=+0.028)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.191 (n=82)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=29)

- **PATRÓN** `py_entrada` < `0.56` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.56 (IC base=+0.032)

- **PATRÓN** `restante_min` > `3.37` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 3.37 (IC base=+0.032)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 14.0 (IC base=+0.032)

- **PATRÓN** `lag_apertura_s` < `95.01` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `lag_apertura_s` < 95.01 (IC base=+0.032)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=7581)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.166 (n=3603)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=10878)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.166 (n=3727)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=11265)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.207 (n=619)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1897)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.193 (n=629)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=1938)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=650)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=2035)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.176 (n=612)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=1895)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.176 (n=653)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=2037)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `libro_spread` > `0.01` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=2800)

- **FILTRO** `py_entrada` > `0.595` → IC=-0.212 (n=709)

  - _Acción_: SKIP cuando `py_entrada` > 0.595
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2285)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=2973)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.175 (n=121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=394)

- **FILTRO** `ibs_20min` > `0.1705` → IC=-0.154 (n=128)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1705
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=387)

- **FILTRO** `libro_liquidez` < `16996.7551` → IC=-0.146 (n=227)

  - _Acción_: SKIP cuando `libro_liquidez` < 16996.7551
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=683)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=245)

- **FILTRO** `ibs_20min` < `0.1944` → IC=-0.216 (n=107)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1944
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=218)

- **FILTRO** `py_entrada` > `0.625` → IC=-0.279 (n=66)

  - _Acción_: SKIP cuando `py_entrada` > 0.625
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=248)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=786)

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
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 15.0 (IC base=+0.032)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=10193)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=22899)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=8125)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=24967)

- **FILTRO** `ibs_7min` < `0.281` → IC=-0.234 (n=8272)

  - _Acción_: SKIP cuando `ibs_7min` < 0.281
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=24820)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=11245)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=21847)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.231 (n=10182)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=31389)

- **FILTRO** `ibs_7min` > `0.2928` → IC=-0.178 (n=10392)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2928
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31179)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=1664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=3824)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=1303)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4185)

- **FILTRO** `ibs_7min` < `0.7113` → IC=-0.249 (n=1811)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7113
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=3677)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.185 (n=1235)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4253)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.260 (n=1755)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=5389)

- **FILTRO** `drift_7min_pct` |x|> `0.1121` → IC=-0.126 (n=2428)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1121
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4716)

- **FILTRO** `ibs_7min` > `0.7882` → IC=-0.207 (n=1785)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7882
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=5359)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.137 (n=1334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4373)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1383)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=4324)

- **FILTRO** `ibs_7min` < `0.7468` → IC=-0.192 (n=1426)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=4281)

- **FILTRO** `ballena_activa_n` > `161.0` → IC=-0.177 (n=1422)

  - _Acción_: SKIP cuando `ballena_activa_n` > 161.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4285)

- **FILTRO** `py_entrada` > `0.65` → IC=-0.255 (n=1449)

  - _Acción_: SKIP cuando `py_entrada` > 0.65
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=4349)

- **FILTRO** `ibs_7min` > `0.2609` → IC=-0.179 (n=1449)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4349)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.183 (n=1445)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4353)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=1278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=3932)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.306 (n=1289)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=3921)

- **FILTRO** `ibs_7min` < `0.7063` → IC=-0.242 (n=1719)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7063
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=3491)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.222 (n=1193)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4017)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.238 (n=1747)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=5900)

- **FILTRO** `ibs_7min` > `0.7468` → IC=-0.173 (n=1911)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7468
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=5736)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=3708)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.234 (n=1616)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=3847)

- **FILTRO** `ibs_7min` < `0.7406` → IC=-0.180 (n=1365)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7406
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4098)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.172 (n=1335)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4128)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1392)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4177)

- **FILTRO** `ibs_7min` > `0.2747` → IC=-0.178 (n=1392)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4177)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.184 (n=1370)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4199)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.36` → IC=-0.254 (n=1419)

  - _Acción_: SKIP cuando `py_entrada` < 0.36
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=4343)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.233 (n=1436)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4326)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.179 (n=1873)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=6037)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.38` → IC=-0.254 (n=1780)

  - _Acción_: SKIP cuando `py_entrada` < 0.38
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3682)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.227 (n=1362)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=4100)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.215 (n=1331)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4131)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.206 (n=1784)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=5719)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=1098)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=536)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=324)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=562)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4159` → IC=+0.144 (n=503)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4159 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=684)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.112)

- **PATRÓN** `total_vol_5m` < `471.727` → IC=+0.142 (n=252)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 471.727 (IC base=+0.112)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4376` → IC=+0.139 (n=59)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4376 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `453.526` → IC=+0.137 (n=155)

  - _Acción_: Kelly boost +0.68€ cuando `total_vol_5m` < 453.526 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 15.0 (IC base=+0.136)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.141 (n=62)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 12.0 (IC base=+0.092)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4133` → IC=+0.176 (n=103)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4133 (IC base=+0.094)

- **PATRÓN** `total_vol_5m` < `394.3776` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 394.3776 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 77.0 (IC base=+0.094)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.167 (n=133)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.199 (n=91)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `7671.127` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 7671.127 (IC base=+0.131)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.152 (n=133)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.137 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 13.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.101)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.007` → IC=-0.324 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=261)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.309 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=63)

- **FILTRO** `T_h` > `87.9866` → IC=-0.438 (n=30)

  - _Acción_: SKIP cuando `T_h` > 87.9866
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.235 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.119)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=55)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `4.1091` → IC=-0.245 (n=96)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.1091
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=296)

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.326 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=252)

- **FILTRO** `T_h` > `62.1058` → IC=-0.330 (n=251)

  - _Acción_: SKIP cuando `T_h` > 62.1058
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=85)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `77.6652` → IC=-0.160 (n=92)

  - _Acción_: SKIP cuando `T_h` > 77.6652
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=46)

- **FILTRO** `pct_vs_K` |x|> `2.9087` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9087
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=106)

- **FILTRO** `T_h` < `97.7009` → IC=-0.384 (n=41)

  - _Acción_: SKIP cuando `T_h` < 97.7009
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=84)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.4229` → IC=-0.354 (n=53)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4229
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=58)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.321 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=81)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.352 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=82)

- **FILTRO** `T_h` > `48.0686` → IC=-0.305 (n=80)

  - _Acción_: SKIP cuando `T_h` > 48.0686
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=27)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3415` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3415 (IC base=-0.199)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.136 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=63)

- **FILTRO** `T_h` > `132.7892` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `T_h` > 132.7892
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=63)

- **FILTRO** `pct_vs_K` |x|> `4.9375` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.9375
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=71)

- **FILTRO** `sigma_h` < `0.0158` → IC=-0.368 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0158
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **FILTRO** `T_h` > `61.2269` → IC=-0.385 (n=50)

  - _Acción_: SKIP cuando `T_h` > 61.2269
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=18)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.375)

- **PATRÓN** `sigma_h` < `0.0134` → IC=+0.406 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0134 (IC base=+0.375)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.425 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.375)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.433 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.375)

- **PATRÓN** `dist_50` > `0.3641` → IC=+0.462 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3641 (IC base=+0.375)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.375)

- **PATRÓN** `edge` > `0.1152` → IC=+0.452 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1152 (IC base=+0.410)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.420 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.410)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.437 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.410)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.420 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.410)

- **PATRÓN** `T_h` > `1.476` → IC=+0.439 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.476 (IC base=+0.410)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.491 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.468 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.410)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.2492` → IC=+0.447 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2492 (IC base=+0.411)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.395 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0072 (IC base=+0.411)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.411)

- **PATRÓN** `T_h` < `0.6559` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6559 (IC base=+0.411)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.468 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.411)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.429 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.411)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.472 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.464)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.446 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.464)

- **PATRÓN** `T_h` > `0.8497` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8497 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.464 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.464 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

- **PATRÓN** `edge` > `0.1229` → IC=+0.464 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1229 (IC base=+0.456)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.478 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.456)

- **PATRÓN** `T_h` > `0.9178` → IC=+0.464 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9178 (IC base=+0.456)

- **PATRÓN** `dist_50` > `0.5` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.5 (IC base=+0.456)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.460 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.456)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=182)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=298)

- **PATRÓN** `streak_estiramiento` < `0.4117` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `streak_estiramiento` < 0.4117 (IC base=+0.038)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.164 (n=129)

  - _Acción_: Kelly boost +0.82€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.036)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=17)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.029)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4152` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4152
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **PATRÓN** `streak_estiramiento` < `0.4152` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.4152 (IC base=+0.000)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.120 (n=77)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.055)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 49.0 (IC base=+0.055)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=86)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=92)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=36)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=31)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=797)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=803)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=406)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` > `3.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `libro_liquidez` < `2775.6672` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_liquidez` < 2775.6672
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=615)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1120)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=775)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=737)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2961)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1509)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1517)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.219 (n=749)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.0744` → IC=+0.203 (n=728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0744 (IC base=+0.186)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.189 (n=551)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.186)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1263` → IC=+0.235 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1263 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=1534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `ibs_15` > `0.6068` → IC=+0.268 (n=1652)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6068 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.185 (n=846)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.6244` → IC=+0.180 (n=1568)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.6244 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.791` → IC=+0.281 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.791 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `8780.1789` → IC=+0.200 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8780.1789 (IC base=+0.186)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=644)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.220 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0591` → IC=+0.300 (n=123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0591 (IC base=+0.208)

- **PATRÓN** `drift_15min` |x|≤ `0.3843` → IC=+0.212 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3843 (IC base=+0.208)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2587` → IC=+0.252 (n=123)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2587 (IC base=+0.208)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1446` → IC=+0.271 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1446 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.241 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_15` > `0.7036` → IC=+0.276 (n=369)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7036 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.4066` → IC=+0.259 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4066 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.385` → IC=+0.274 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.385 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.244 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.208)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.297` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.297
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=398)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.140 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0065 (IC base=+0.134)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.151 (n=256)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0051 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0678` → IC=+0.155 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0678 (IC base=+0.134)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2337` → IC=+0.169 (n=128)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio_macro` |x|> 0.2337 (IC base=+0.134)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2579` → IC=+0.157 (n=275)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2579 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.153 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.134 (n=170)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_15` > `0.6602` → IC=+0.254 (n=343)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6602 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1631` → IC=+0.153 (n=301)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1631 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.257` → IC=+0.211 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.257 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `3422.7688` → IC=+0.143 (n=343)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3422.7688 (IC base=+0.134)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=103)

- **FILTRO** `ibs_15` > `0.2101` → IC=-0.243 (n=33)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2101
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=102)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.291 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1498` → IC=+0.201 (n=172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1498 (IC base=+0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0712` → IC=+0.195 (n=175)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.0712 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2704` → IC=+0.222 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2704 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.267 (n=195)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.3239` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3239 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.5335` → IC=+0.174 (n=213)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.5335 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.389` → IC=+0.407 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.389 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `3077.8574` → IC=+0.280 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3077.8574 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.172)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.5705` → IC=-0.135 (n=124)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5705
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=918)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=-0.004)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0235` → IC=+0.262 (n=145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0235 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.0857` → IC=+0.211 (n=192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0857 (IC base=+0.189)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0394` → IC=+0.191 (n=435)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.0394 (IC base=+0.189)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0898` → IC=+0.257 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0898 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.230 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.189)

- **PATRÓN** `ibs_15` > `0.5526` → IC=+0.280 (n=435)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5526 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.1339` → IC=+0.208 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1339 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.8385` → IC=+0.190 (n=501)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.8385 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.92` → IC=+0.231 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.92 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.743` → IC=+0.190 (n=436)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 10.743 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `2920.176` → IC=+0.296 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2920.176 (IC base=+0.189)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.159 (n=491)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.80€ cuando `ibs_15` < 0.1176 (IC base=+0.050)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.340 (n=280)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.341)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.375 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.341)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.347 (n=280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.341)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1426` → IC=+0.365 (n=279)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1426 (IC base=+0.341)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1304` → IC=+0.379 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1304 (IC base=+0.341)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.361 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.341)

- **PATRÓN** `ibs_15` > `0.7873` → IC=+0.384 (n=419)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7873 (IC base=+0.341)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.390 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.341)

- **PATRÓN** `dist_vwap_pct` < `0.1089` → IC=+0.340 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1089 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.346 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.341)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.024` → IC=+0.342 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 14.024 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.346 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.355 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.341)

- **PATRÓN** `ballena_activa_n` < `462.0` → IC=+0.362 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 462.0 (IC base=+0.341)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.354 (n=204)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.346)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.375 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.346)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.375 (n=78)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.346)

- **PATRÓN** `drift_15min` |x|≤ `0.4231` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4231 (IC base=+0.346)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.365 (n=154)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.346)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1231` → IC=+0.386 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1231 (IC base=+0.346)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.372 (n=217)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.346)

- **PATRÓN** `ibs_15` > `0.8154` → IC=+0.380 (n=232)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8154 (IC base=+0.346)

- **PATRÓN** `dist_vwap_pct` > `0.4016` → IC=+0.413 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4016 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.352 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.346)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.659` → IC=+0.349 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.659 (IC base=+0.346)

- **PATRÓN** `libro_liquidez` > `11204.8499` → IC=+0.366 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11204.8499 (IC base=+0.346)

- **PATRÓN** `ballena_activa_n` < `574.0` → IC=+0.393 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 574.0 (IC base=+0.346)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.331 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.366 (n=125)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.333)

- **PATRÓN** `drift_60min` |x|≤ `0.0656` → IC=+0.347 (n=83)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0656 (IC base=+0.333)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.358 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.333)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.359 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.398 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.333)

- **PATRÓN** `ibs_15` > `0.7408` → IC=+0.389 (n=187)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7408 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.333)

- **PATRÓN** `dist_vwap_pct` < `0.1197` → IC=+0.339 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1197 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.348 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.333)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.336 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.333)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.343 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.333)

- **PATRÓN** `libro_liquidez` > `3893.6222` → IC=+0.362 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3893.6222 (IC base=+0.333)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0129` → IC=-0.222 (n=670)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0129
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2011)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=912)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1769)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.251 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.064)

- **PATRÓN** `ibs_15` > `0.6395` → IC=+0.275 (n=639)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6395 (IC base=-0.064)

- **PATRÓN** `dist_vwap_pct` < `0.1175` → IC=+0.192 (n=400)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.1175 (IC base=-0.064)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1194` → IC=+0.250 (n=1220)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1194 (IC base=-0.031)

- **PATRÓN** `ibs_15` < `0.3455` → IC=+0.278 (n=1830)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3455 (IC base=-0.031)

- **PATRÓN** `dist_vwap_pct` > `0.6985` → IC=+0.304 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6985 (IC base=-0.031)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.228 (n=409)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1230)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.232 (n=409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1230)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.211 (n=1037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=602)

- **FILTRO** `sigma_ewma_delta_pct` > `19.563` → IC=-0.250 (n=294)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.563
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1345)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.158 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0029 (IC base=+0.082)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.293 (n=80)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.082)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.327 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 12.0 (IC base=+0.082)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.332 (n=176)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.287 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.5498` → IC=+0.286 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5498 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `441.0` → IC=+0.263 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 441.0 (IC base=+0.082)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.6675` → IC=-0.196 (n=100)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6675
  - _Potencial_: sin este filtro IC_bueno=+0.264 (n=303)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=386)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.153 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.006 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.186 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0051 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0757` → IC=+0.218 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0757 (IC base=+0.149)

- **PATRÓN** `drift_15min` |x|≤ `0.4193` → IC=+0.170 (n=101)

  - _Acción_: Kelly boost +0.85€ cuando `drift_15min` |x|≤ 0.4193 (IC base=+0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1335` → IC=+0.157 (n=202)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio_macro` |x|> 0.1335 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2902` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2902 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.206 (n=141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.6675` → IC=+0.264 (n=303)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6675 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.4741` → IC=+0.152 (n=87)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.4741 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1175` → IC=+0.188 (n=216)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1175 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.857` → IC=+0.160 (n=242)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 6.857 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=386)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11008.7835` → IC=+0.193 (n=138)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 11008.7835 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.244 (n=714)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.4455` → IC=+0.235 (n=714)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4455 (IC base=+0.231)

- **PATRÓN** `drift_15min` |x|≤ `0.48` → IC=+0.240 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.48 (IC base=+0.231)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2028` → IC=+0.264 (n=324)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2028 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.244 (n=268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.231)

- **PATRÓN** `ibs_15` < `0.3453` → IC=+0.271 (n=714)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3453 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.7695` → IC=+0.320 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7695 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.403` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.403 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.221` → IC=+0.239 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.221 (IC base=+0.231)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.250 (n=158)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=476)

- **FILTRO** `drift_60min` |x|> `0.1682` → IC=-0.219 (n=215)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=419)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.269 (n=158)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=476)

- **PATRÓN** `ibs_15` > `0.8889` → IC=+0.350 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8889 (IC base=-0.170)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0764` → IC=+0.231 (n=281)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0764 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.267 (n=315)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7712` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7712 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.224 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.199 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2005` → IC=-0.198 (n=266)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2005
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=517)

- **FILTRO** `sigma_h` > `0.0198` → IC=-0.261 (n=391)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0198
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=392)

- **FILTRO** `drift_15min` |x|> `1.2727` → IC=-0.267 (n=195)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2727
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=588)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.260 (n=190)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=593)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1333` → IC=+0.291 (n=218)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1333 (IC base=-0.042)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1028` → IC=+0.343 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1028 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3429` → IC=+0.305 (n=480)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3429 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.943` → IC=+0.345 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.943 (IC base=-0.042)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1645` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1645 (IC base=+0.050)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2775` → IC=-0.136 (n=20)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2775
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **FILTRO** `ibs_15` < `0.8489` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8489
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1645` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1645 (IC base=+0.050)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.302 (n=447)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0567` → IC=+0.327 (n=224)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0567 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.309 (n=223)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.346 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=700)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8411` → IC=+0.327 (n=670)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8411 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2769` → IC=+0.326 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2769 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.337 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `13084.0601` → IC=+0.304 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13084.0601 (IC base=+0.293)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.303 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.288 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.349 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.262` → IC=+0.308 (n=123)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.262 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3807` → IC=+0.311 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3807 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.308 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.317 (n=369)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.444` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.444 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.324 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.312 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.299)

- **PATRÓN** `drift_60min` |x|≤ `0.0694` → IC=+0.300 (n=133)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0694 (IC base=+0.299)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2251` → IC=+0.316 (n=101)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2251 (IC base=+0.299)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.288` → IC=+0.335 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.288 (IC base=+0.299)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.330 (n=269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.299)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.338 (n=301)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.299)

- **PATRÓN** `dist_vwap_pct` > `0.6408` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6408 (IC base=+0.299)

- **PATRÓN** `dist_vwap_pct` < `0.167` → IC=+0.302 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.167 (IC base=+0.299)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.299)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.299)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2547` → IC=-0.158 (n=71)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2547
  - _Potencial_: sin este filtro IC_bueno=-0.116 (n=214)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1143` → IC=-0.171 (n=71)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1143
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=214)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.164 (n=111)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=333)

- **FILTRO** `ballena_activa_n` > `60.0` → IC=-0.223 (n=45)

  - _Acción_: SKIP cuando `ballena_activa_n` > 60.0
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=138)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0682` → IC=-0.155 (n=56)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0682
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=111)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.151 (n=41)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=126)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2236` → IC=-0.133 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2236
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0943` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0943
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.1344` → IC=-0.241 (n=25)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1344
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1195` → IC=-0.206 (n=15)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1195
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.265 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `drift_15min` |x|> `0.3593` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3593
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3119` → IC=-0.184 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3119
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `76.962` → IC=+0.217 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 76.962 (IC base=+0.202)

- **PATRÓN** `ratio` < `0.9779` → IC=+0.465 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9779 (IC base=+0.202)

- **PATRÓN** `T_h` > `145.7851` → IC=+0.394 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7851 (IC base=+0.332)

- **PATRÓN** `ratio` > `1.01` → IC=+0.287 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.01 (IC base=+0.332)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `115.2222` → IC=+0.211 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.176)

- **PATRÓN** `ratio` < `0.973` → IC=+0.446 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.176)

- **PATRÓN** `T_h` < `111.996` → IC=+0.295 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.996 (IC base=+0.282)

- **PATRÓN** `T_h` > `102.8316` → IC=+0.289 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 102.8316 (IC base=+0.282)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.282)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `91.5869` → IC=+0.283 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 91.5869 (IC base=+0.244)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.421 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.244)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.328 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.311)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.320 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.311)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1359` → IC=+0.457 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1359 (IC base=+0.403)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6068 sube el IC de +0.186 a +0.268 en UPDOWN_GBM#15min (n=1652). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7036 sube el IC de +0.208 a +0.276 en UPDOWN_GBM#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6602 sube el IC de +0.134 a +0.254 en UPDOWN_GBM#ETH#15min (n=343). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.172 a +0.267 en UPDOWN_GBM#SOL#15min (n=195). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5526 sube el IC de +0.189 a +0.280 en UPDOWN_GBM#XRP#15min (n=435). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.050 a +0.159 en UPDOWN_GBM#XRP#15min (n=491). Ya aplicado como kelly_boost=+0.80€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6395 sube el IC de -0.064 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=639). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3455 sube el IC de -0.031 a +0.278 en UPDOWN_GBM_15M_TARDIO (n=1830). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.082 a +0.332 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=176). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6675 sube el IC de +0.149 a +0.264 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=303). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3453 sube el IC de +0.231 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=714). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.8889 sube el IC de -0.170 a +0.350 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=18). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.042 a +0.267 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=315). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3429 sube el IC de -0.042 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=480). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8411 sube el IC de +0.293 a +0.327 en UPDOWN_GBM_IBS_ALTO (n=670). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.287 a +0.317 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.299 a +0.338 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=301). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7873 sube el IC de +0.341 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=419). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8154 sube el IC de +0.346 a +0.380 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=232). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7408 sube el IC de +0.333 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=187). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1340 | +0.100 | +201.69€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1340 | +0.100 | +201.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1000 | +0.110 | +174.82€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1000 | +0.110 | +174.82€ | 2 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 254 | +0.055 | +8.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 254 | +0.055 | +8.21€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 28707 | -0.088 | -3851.90€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1485 | -0.045 | -221.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 27222 | -0.091 | -3630.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3773 | -0.098 | -622.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3773 | -0.098 | -622.69€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1485 | -0.045 | -221.27€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1485 | -0.045 | -221.27€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3482 | -0.096 | -787.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3482 | -0.096 | -787.96€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7356 | -0.021 | -689.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7356 | -0.021 | -689.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 6965 | -0.090 | -440.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 6965 | -0.090 | -440.28€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5646 | -0.173 | -1090.50€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5646 | -0.173 | -1090.50€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 18727 | -0.027 | +3989.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 4881 | -0.000 | +1811.92€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 13846 | -0.037 | +2177.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 18727 | -0.027 | +3989.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 4881 | -0.000 | +1811.92€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 13846 | -0.037 | +2177.54€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1478 | -0.103 | -191.97€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 168 | -0.053 | -21.36€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 780 | -0.091 | -97.63€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 144 | -0.048 | -16.13€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 94600 | +0.112 | -4758.13€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14227 | +0.185 | -430.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 381 | -0.080 | -50.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 73866 | +0.100 | -4059.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6126 | +0.107 | -218.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 12283 | +0.098 | -1041.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 45 | -0.160 | -0.32€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 12223 | +0.099 | -1029.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 19133 | +0.132 | -369.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4493 | +0.204 | -132.28€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 12246 | +0.111 | -198.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2352 | +0.103 | -16.22€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 12322 | +0.090 | -1119.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 52 | -0.093 | -6.98€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 12255 | +0.091 | -1101.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 20114 | +0.123 | -393.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5504 | +0.175 | -80.92€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 12379 | +0.105 | -245.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2219 | +0.098 | -58.06€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 18451 | +0.113 | -1106.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4086 | +0.188 | -218.17€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 284 | -0.038 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 12526 | +0.090 | -747.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1555 | +0.125 | -144.10€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 12297 | +0.100 | -727.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 47 | -0.031 | +8.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 12237 | +0.101 | -735.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 15008 | +0.191 | -993.73€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 15008 | +0.191 | -993.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3568 | +0.167 | -378.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3568 | +0.167 | -378.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1276 | +0.196 | -13.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1276 | +0.196 | -13.44€ | 4 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3518 | +0.179 | -304.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3518 | +0.179 | -304.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3117 | +0.239 | -99.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3117 | +0.239 | -99.94€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3450 | +0.192 | -210.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3450 | +0.192 | -210.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 709 | +0.428 | -21.92€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 709 | +0.428 | -21.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 275 | +0.439 | -2.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 275 | +0.439 | -2.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 267 | +0.429 | -6.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 267 | +0.429 | -6.93€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 157 | +0.406 | -10.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 157 | +0.406 | -10.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 51760 | +0.197 | -4058.30€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 51760 | +0.197 | -4058.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 8950 | +0.176 | -1038.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 8950 | +0.176 | -1038.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8269 | +0.223 | -306.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8269 | +0.223 | -306.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 8938 | +0.172 | -1070.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 8938 | +0.172 | -1070.34€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8363 | +0.218 | -329.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8363 | +0.218 | -329.92€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 8557 | +0.203 | -559.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 8557 | +0.203 | -559.28€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 8683 | +0.193 | -753.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 8683 | +0.193 | -753.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 19515 | +0.117 | +162.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 19515 | +0.117 | +162.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 9691 | +0.122 | +141.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 9691 | +0.122 | +141.28€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 9824 | +0.113 | +21.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 9824 | +0.113 | +21.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1493 | +0.289 | -21.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1493 | +0.289 | -21.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 665 | +0.275 | -22.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 665 | +0.275 | -22.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 717 | +0.291 | -1.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 717 | +0.291 | -1.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 111 | +0.341 | +2.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 111 | +0.341 | +2.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 655 | +0.436 | -2.96€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 655 | +0.436 | -2.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 310 | +0.433 | -4.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 310 | +0.433 | -4.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 301 | +0.441 | +0.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 301 | +0.441 | +0.74€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 44 | +0.391 | +0.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 44 | +0.391 | +0.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1134 | +0.075 | -44.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 393 | +0.057 | -33.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 741 | +0.084 | -10.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 61 | +0.119 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 896 | +0.082 | -16.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 155 | +0.073 | -5.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 741 | +0.084 | -10.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 177 | +0.020 | -31.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 177 | +0.020 | -31.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 36326 | +0.097 | -1105.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3000 | +0.090 | +25.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 33326 | +0.098 | -1130.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 20382 | +0.101 | -330.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3000 | +0.090 | +25.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 17382 | +0.103 | -356.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 6853 | +0.107 | -42.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 6853 | +0.107 | -42.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9091 | +0.081 | -731.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9091 | +0.081 | -731.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 816 | +0.215 | -100.30€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 816 | +0.215 | -100.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 816 | +0.215 | -100.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 816 | +0.215 | -100.30€ | 2 | 4 |
| ✅ GBM_LATE_15M | 26036 | +0.083 | +12349.10€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 26036 | +0.083 | +12349.10€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4353 | +0.192 | +3148.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4353 | +0.192 | +3148.02€ | 0 | 18 |
| ✅ GBM_LATE_15M#BTC | 3875 | +0.178 | +2720.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 3875 | +0.178 | +2720.97€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 4541 | +0.197 | +3363.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4541 | +0.197 | +3363.64€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 3822 | +0.021 | +826.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3822 | +0.021 | +826.71€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 3718 | -0.033 | +835.35€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3718 | -0.033 | +835.35€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 5727 | -0.040 | +1454.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 5727 | -0.040 | +1454.41€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 27520 | +0.086 | +14366.85€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 27520 | +0.086 | +14366.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5225 | +0.017 | +2764.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5225 | +0.017 | +2764.10€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 5745 | +0.015 | +1191.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 5745 | +0.015 | +1191.28€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 3910 | +0.262 | +3929.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 3910 | +0.262 | +3929.68€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4470 | +0.004 | +858.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4470 | +0.004 | +858.81€ | 2 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4461 | +0.028 | +1680.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4461 | +0.028 | +1680.66€ | 3 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3709 | +0.275 | +3942.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3709 | +0.275 | +3942.31€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 20945 | +0.167 | +15550.95€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 20945 | +0.167 | +15550.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3154 | +0.205 | +2490.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3154 | +0.205 | +2490.84€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3325 | +0.149 | +2432.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3325 | +0.149 | +2432.04€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3290 | +0.207 | +2607.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3290 | +0.207 | +2607.68€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3510 | +0.132 | +2429.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3510 | +0.132 | +2429.38€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 3901 | +0.115 | +2648.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 3901 | +0.115 | +2648.53€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3765 | +0.202 | +2942.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3765 | +0.202 | +2942.49€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5282 | +0.128 | +2238.35€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5282 | +0.128 | +2238.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 210 | +0.108 | +81.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 210 | +0.108 | +81.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1494 | +0.124 | +671.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1494 | +0.124 | +671.96€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 373 | +0.143 | +176.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1572 | +0.145 | +716.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1572 | +0.145 | +716.25€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1127 | +0.105 | +377.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1127 | +0.105 | +377.00€ | 1 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 26164 | +0.175 | +19426.36€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 26164 | +0.175 | +19426.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4147 | +0.219 | +3472.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4147 | +0.219 | +3472.81€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4109 | +0.151 | +2723.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4109 | +0.151 | +2723.12€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4300 | +0.224 | +3680.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4300 | +0.224 | +3680.22€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4241 | +0.136 | +2885.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4241 | +0.136 | +2885.81€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4570 | +0.114 | +2910.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4570 | +0.114 | +2910.88€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 4797 | +0.204 | +3753.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 4797 | +0.204 | +3753.51€ | 0 | 24 |
| ✅ GBM_LATE_5M | 7149 | +0.150 | +4158.28€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 7149 | +0.150 | +4158.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 594 | +0.186 | +416.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1807 | +0.148 | +1196.41€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1807 | +0.148 | +1196.41€ | 0 | 31 |
| ✅ GBM_LATE_5M#DOGE | 889 | +0.171 | +564.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 889 | +0.171 | +564.50€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 2408 | +0.157 | +1425.39€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2408 | +0.157 | +1425.39€ | 0 | 32 |
| ✅ GBM_LATE_5M#SOL | 614 | +0.109 | +228.50€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 614 | +0.109 | +228.50€ | 0 | 17 |
| ✅ GBM_LATE_5M#XRP | 837 | +0.116 | +326.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 837 | +0.116 | +326.92€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1761 | +0.068 | +752.59€ | 2 | 11 |
| ✅ GBM_LATE_60M#60min | 1761 | +0.068 | +752.59€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 639 | +0.087 | +268.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 639 | +0.087 | +268.03€ | 0 | 11 |
| ✅ GBM_LATE_60M#ETH | 582 | +0.072 | +297.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 582 | +0.072 | +297.28€ | 2 | 15 |
| ✅ GBM_LATE_60M#SOL | 540 | +0.041 | +187.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 540 | +0.041 | +187.28€ | 2 | 11 |
| 🚫 GBM_LATE_60M_FADE | 380 | -0.251 | -19.12€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 380 | -0.251 | -19.12€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 147 | -0.218 | -6.10€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 147 | -0.218 | -6.10€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 124 | -0.254 | -7.92€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 124 | -0.254 | -7.92€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 109 | -0.284 | -5.10€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 109 | -0.284 | -5.10€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 711 | +0.074 | +163.99€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 711 | +0.074 | +163.99€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 279 | +0.062 | +52.40€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 279 | +0.062 | +52.40€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 208 | +0.038 | +17.16€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 208 | +0.038 | +17.16€ | 2 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 224 | +0.119 | +94.43€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 224 | +0.119 | +94.43€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 102 | +0.260 | +85.53€ | 0 | 10 |
| ✅ LATE_WINDOW_5MIN#5min | 102 | +0.260 | +85.53€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 102 | +0.260 | +85.53€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 102 | +0.260 | +85.53€ | 0 | 10 |
| ✅ LEADLAG_BTC_XRP_15M | 1989 | +0.103 | +551.77€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 1989 | +0.103 | +551.77€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 1989 | +0.103 | +551.77€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 1989 | +0.103 | +551.77€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 383 | -0.079 | -34.29€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 383 | -0.079 | -34.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 96 | -0.061 | -5.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 96 | -0.061 | -5.23€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 67 | -0.080 | -7.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 67 | -0.080 | -7.45€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 139 | -0.025 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 139 | -0.025 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 2041 | +0.007 | +17.23€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2041 | +0.007 | +17.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 106 | +0.028 | +0.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 106 | +0.028 | +0.43€ | 0 | 1 |
| ✅ LIQUIDACIONES_5M#BTC | 232 | -0.013 | +7.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 232 | -0.013 | +7.03€ | 5 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 164 | -0.036 | -7.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 164 | -0.036 | -7.46€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 854 | +0.026 | +23.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 854 | +0.026 | +23.39€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 472 | -0.002 | -5.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 472 | -0.002 | -5.95€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 213 | -0.002 | -0.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 213 | -0.002 | -0.22€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M | 1094 | -0.043 | -25.93€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1094 | -0.043 | -25.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 311 | -0.040 | -12.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 311 | -0.040 | -12.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 367 | -0.026 | -0.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 367 | -0.026 | -0.70€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 416 | -0.060 | -12.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 416 | -0.060 | -12.98€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 1494 | -0.025 | +6.52€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 700 | -0.026 | -3.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 794 | -0.025 | +10.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 37 | +0.038 | +7.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 21 | +0.065 | +5.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 16 | +0.000 | +2.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 368 | +0.032 | +45.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 169 | +0.009 | +7.07€ | 4 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 199 | +0.052 | +38.26€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 205 | -0.060 | -13.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 97 | -0.066 | -8.78€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 108 | -0.054 | -4.30€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 280 | -0.082 | -35.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 124 | -0.079 | -13.78€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 156 | -0.082 | -21.85€ | 4 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 254 | +0.000 | +16.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 127 | +0.019 | +13.19€ | 0 | 6 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 127 | -0.019 | +3.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 350 | -0.045 | -14.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 162 | -0.043 | -6.51€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 188 | -0.047 | -7.66€ | 1 | 4 |
| ✅ MOMENTUM_IBS_15M | 14445 | -0.011 | -207.52€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14445 | -0.011 | -207.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3162 | -0.020 | -60.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3162 | -0.020 | -60.71€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 29473 | -0.006 | +1347.33€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 29473 | -0.006 | +1347.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5203 | +0.018 | +640.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5203 | +0.018 | +640.99€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4554 | -0.028 | -48.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4554 | -0.028 | -48.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5252 | +0.015 | +473.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5252 | +0.015 | +473.74€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4333 | -0.051 | -127.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4333 | -0.051 | -127.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 4934 | -0.010 | +193.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 4934 | -0.010 | +193.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5197 | +0.008 | +215.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5197 | +0.008 | +215.01€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5874 | -0.058 | -132.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5874 | -0.058 | -132.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1212 | +0.001 | -14.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1212 | +0.001 | -14.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1425 | -0.083 | -37.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1425 | -0.083 | -37.89€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 44 | -0.130 | -5.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 639 | -0.110 | -17.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 639 | -0.110 | -17.27€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1707 | -0.077 | -31.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1707 | -0.077 | -31.16€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 847 | -0.016 | -25.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 847 | -0.016 | -25.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 74663 | -0.073 | +1693.32€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 74663 | -0.073 | +1693.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 12632 | -0.079 | +712.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 12632 | -0.079 | +712.57€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 11505 | -0.092 | -506.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 11505 | -0.092 | -506.36€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 12857 | -0.067 | +702.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 12857 | -0.067 | +702.83€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 11032 | -0.093 | -210.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 11032 | -0.093 | -210.20€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 13672 | -0.048 | +397.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 13672 | -0.048 | +397.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 12965 | -0.063 | +596.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 12965 | -0.063 | +596.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7631 | -0.025 | -124.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7631 | -0.025 | -124.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1695 | -0.030 | -8.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1695 | -0.030 | -8.90€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2156 | -0.019 | -25.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2156 | -0.019 | -25.66€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1043 | -0.041 | -15.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1043 | -0.041 | -15.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 738 | -0.020 | -23.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1142 | +0.106 | +376.01€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1006 | +0.112 | +363.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 234 | +0.136 | +114.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 234 | +0.136 | +114.86€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 194 | +0.092 | +43.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 194 | +0.092 | +43.99€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 205 | +0.094 | +66.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 205 | +0.094 | +66.91€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#SOL | 177 | +0.131 | +80.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 177 | +0.131 | +80.23€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 196 | +0.101 | +57.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 196 | +0.101 | +57.43€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 508 | -0.061 | -60.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 508 | -0.061 | -60.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 111 | -0.004 | +2.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 111 | -0.004 | +2.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 60 | -0.145 | -19.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 60 | -0.145 | -19.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 150 | -0.079 | -28.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 150 | -0.079 | -28.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 106 | -0.009 | -0.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 106 | -0.009 | -0.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 81 | -0.102 | -15.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 81 | -0.102 | -15.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 580 | -0.105 | -47.18€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 266 | -0.157 | -63.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 218 | -0.200 | -65.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 202 | -0.073 | +0.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 158 | -0.081 | -7.42€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 112 | -0.035 | +15.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 90 | -0.054 | +8.64€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 466 | -0.133 | -64.70€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 728 | -0.204 | -31.94€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 300 | -0.202 | -28.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 263 | -0.198 | -28.19€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 250 | -0.218 | -22.59€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 218 | -0.227 | -27.25€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 178 | -0.183 | +19.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 162 | -0.183 | +14.57€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 643 | -0.205 | -40.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 295 | +0.402 | +218.00€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 29 | +0.048 | -4.24€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 79 | +0.377 | +58.79€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 79 | +0.377 | +58.79€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#SOL | 187 | +0.463 | +163.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 187 | +0.463 | +163.44€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 295 | +0.402 | +218.00€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 518 | +0.036 | +20.02€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 518 | +0.036 | +20.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 247 | +0.034 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 247 | +0.034 | +5.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 55 | +0.009 | -0.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 55 | +0.009 | -0.51€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 180 | +0.038 | +12.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 180 | +0.038 | +12.53€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 2796 | -0.022 | -114.31€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2796 | -0.022 | -114.31€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 808 | -0.017 | -25.89€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 808 | -0.017 | -25.89€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 570 | -0.023 | -23.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 570 | -0.023 | -23.26€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 155 | -0.048 | -14.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 155 | -0.048 | -14.93€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1263 | -0.022 | -50.24€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1263 | -0.022 | -50.24€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 75 | -0.058 | -7.51€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 75 | -0.058 | -7.51€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 37 | -0.013 | -3.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 37 | -0.013 | -3.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 7883 | +0.024 | +121.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 7883 | +0.024 | +121.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2144 | +0.022 | +23.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2144 | +0.022 | +23.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1790 | +0.036 | +54.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1790 | +0.036 | +54.88€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2395 | +0.013 | +6.43€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2395 | +0.013 | +6.43€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1554 | +0.028 | +37.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1554 | +0.028 | +37.08€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7416 | +0.014 | -28.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7416 | +0.014 | -28.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 2980 | +0.018 | -0.71€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 2980 | +0.018 | -0.71€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 2895 | +0.014 | -13.16€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 2895 | +0.014 | -13.16€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1541 | +0.005 | -15.04€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1541 | +0.005 | -15.04€ | 2 | 0 |
| ✅ UPDOWN_GBM | 38227 | +0.031 | +2296.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 10389 | +0.068 | +1884.92€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 1410 | +0.004 | +6.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 23936 | +0.020 | +381.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2344 | +0.005 | +24.59€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 3979 | +0.068 | +448.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 723 | +0.155 | +296.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 32 | +0.000 | -0.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3224 | +0.049 | +151.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 7098 | +0.037 | +499.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1313 | +0.082 | +292.11€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 379 | +0.020 | +8.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 4298 | +0.034 | +173.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1051 | +0.003 | +24.65€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 57 | -0.093 | +1.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4519 | +0.040 | +281.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 670 | +0.140 | +237.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 3821 | +0.023 | +44.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 8094 | +0.018 | +283.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2649 | +0.046 | +268.63€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 370 | +0.005 | +6.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 4232 | +0.007 | +11.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 795 | +0.001 | -5.80€ | 2 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 48 | -0.140 | +3.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 8955 | +0.013 | +211.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2502 | +0.026 | +171.93€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 362 | -0.005 | -2.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 5552 | +0.010 | +39.15€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 498 | +0.014 | +5.74€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 41 | -0.174 | -3.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 5580 | +0.035 | +575.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2532 | +0.082 | +617.99€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 239 | -0.006 | -4.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 2809 | -0.004 | -38.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 146 | -0.135 | +0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 558 | +0.341 | +168.43€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 558 | +0.341 | +168.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 309 | +0.346 | +90.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 309 | +0.346 | +90.11€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 249 | +0.333 | +78.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 249 | +0.333 | +78.32€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 12232 | -0.038 | +2569.34€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 12232 | -0.038 | +2569.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 815 | -0.040 | +363.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 815 | -0.040 | +363.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2249 | -0.123 | +6.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2249 | -0.123 | +6.67€ | 4 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 421 | +0.178 | +279.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 421 | +0.178 | +279.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1354 | +0.207 | +798.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1354 | +0.207 | +798.11€ | 2 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3685 | -0.064 | +548.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3685 | -0.064 | +548.23€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3708 | -0.075 | +573.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3708 | -0.075 | +573.89€ | 4 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 145 | +0.037 | +8.71€ | 2 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 145 | +0.037 | +8.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 145 | +0.037 | +8.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 145 | +0.037 | +8.71€ | 2 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 893 | +0.293 | +720.66€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 893 | +0.293 | +720.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 492 | +0.287 | +376.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 492 | +0.287 | +376.24€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 401 | +0.299 | +344.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 401 | +0.299 | +344.42€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 729 | -0.113 | -85.64€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 729 | -0.113 | -85.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 212 | -0.084 | -16.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 212 | -0.084 | -16.31€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 68 | -0.200 | -9.95€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 68 | -0.200 | -9.95€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2432 | +0.300 | +1226.96€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 839 | +0.249 | +117.57€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 915 | +0.289 | +398.68€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 678 | +0.377 | +710.71€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.011 n=489 — no justifica filtro, seguir monitorizando
  - _Datos_: n=489 IC=+0.011 PNL=+18.76€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 529 celda(s) pasan gate riguroso completo de 2255 evaluadas (n>=40) y 3230 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.026 < 0.08 — monitorear
  - _Datos_: n=2500 IC=+0.026 PNL=+171.96€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=915/15 IC=+0.289 PNL=+398.68€ | BTC: n=839/15 IC=+0.249 PNL=+117.57€ | SOL: n=678/15 IC=+0.377 PNL=+710.71€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 30 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: alineada_con_outcome_prev IC=+0.108 n=332/60 | contraria IC=+0.148 n=316 | gap=-0.040 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=294, boost estimado=+0.003. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=793/40 IC=+0.001 PNL=-5.79€ | BTC#60min: n=1049/40 IC=+0.003 PNL=+24.66€ | SOL#60min: n=496/40 IC=+0.014 PNL=+5.81€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=341539 | tras_1loss IC=+0.078 n=265583 | tras_2loss IC=+0.048 n=111893/40 | gap=+0.002 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.181 > 0.08 con n=333 PNL=+210.09€
  - _Datos_: n=333 IC=+0.181 PNL=+210.09€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.218 > 0.08 con n=388 PNL=+286.86€
  - _Datos_: n=388 IC=+0.218 PNL=+286.86€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.244 > 0.08 con n=41 PNL=+31.47€
  - _Datos_: n=41 IC=+0.244 PNL=+31.47€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.328 > 0.1 con n=1991 PNL=+1118.21€
  - _Datos_: n=1991 IC=+0.328 PNL=+1118.21€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=282 IC=+0.077 PNL=+34.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=282 IC=+0.077 PNL=+34.59€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=51 IC=+0.198 PNL=+36.17€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=51 IC=+0.198 PNL=+36.17€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

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
  - _Estado_: n=1643 IC=+0.013 PNL=+11.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1643 IC=+0.013 PNL=+11.77€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=695 IC=-0.014 PNL=+12.90€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=695 IC=-0.014 PNL=+12.90€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=489 IC=+0.011 PNL=+18.76€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=489 IC=+0.011 PNL=+18.76€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.186 > 0.1 con n=2202 PNL=+1365.29€
  - _Datos_: n=2202 IC=+0.186 PNL=+1365.29€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1313 IC=+0.082 PNL=+292.11€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1313 IC=+0.082 PNL=+292.11€

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
  - _Estado_: n=552 IC=+0.018 PNL=+39.44€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=552 IC=+0.018 PNL=+39.44€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=53 IC=+0.082 PNL=+5.09€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=53 IC=+0.082 PNL=+5.09€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.260 n=102) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=102 IC=+0.260 PNL=+85.53€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=642 PNL=+236.73€
  - _Datos_: n=642 IC=+0.118 PNL=+236.73€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=147 IC=-0.044 PNL=+35.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=147 IC=-0.044 PNL=+35.89€

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
  - _Estado_: n=13400 IC=+0.054 PNL=+1611.90€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=13400 IC=+0.054 PNL=+1611.90€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.160 < -0.1 con n=239 PNL=+21.62€
  - _Datos_: n=239 IC=-0.160 PNL=+21.62€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=1950 IC=+0.050 PNL=+208.85€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1950 IC=+0.050 PNL=+208.85€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=80 IC=-0.122 PNL=+3.66€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=80 IC=-0.122 PNL=+3.66€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.1 con n=420 PNL=+127.39€
  - _Datos_: n=420 IC=+0.128 PNL=+127.39€

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
  - _Estado_: n=18312 IC=-0.137 PNL=+1265.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=18312 IC=-0.137 PNL=+1265.13€

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
  - _Estado_: n=1976 IC=+0.141 PNL=+1085.40€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1976 IC=+0.141 PNL=+1085.40€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=4042 IC=+0.021 PNL=+140.29€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4042 IC=+0.021 PNL=+140.29€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=2116 PNL=+1091.44€
  - _Datos_: n=2116 IC=+0.086 PNL=+1091.44€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.237 < -0.1 con n=1787 PNL=-195.71€
  - _Datos_: n=1787 IC=-0.237 PNL=-195.71€

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
  - _Estado_: 36/40 ops en el filtro definido (IC actual=-0.026 PNL=+3.42€)
  - _Datos_: n=36 IC=-0.026 PNL=+3.42€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.099 n=1022) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1022 IC=+0.099 PNL=+243.76€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.411 n=446) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=446 IC=+0.411 PNL=+628.68€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=8943 IC=+0.176 PNL=-1038.30€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=8943 IC=+0.176 PNL=-1038.30€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.201 > 0.1 con n=135 PNL=+80.38€
  - _Datos_: n=135 IC=+0.201 PNL=+80.38€
