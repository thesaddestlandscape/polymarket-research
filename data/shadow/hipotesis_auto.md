# Hipótesis automáticas — 2026-09-29 12:43 UTC
_Generado por shadow_postmortem.py sobre 666084 resoluciones (PNL=+78173.25€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=539)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.235 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.8032` → IC=+0.254 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8032 (IC base=+0.138)

- **PATRÓN** `banda_z` > `9.581` → IC=+0.203 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.581 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.156 (n=393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=606)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4804.7376` → IC=+0.167 (n=190)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 4804.7376 (IC base=+0.138)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.123 (n=539)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.056)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.140 (n=170)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=439)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=404)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.257 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.146)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.146)

- **PATRÓN** `banda_hit_calibrado` > `0.7991` → IC=+0.266 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7991 (IC base=+0.146)

- **PATRÓN** `banda_z` > `10.429` → IC=+0.216 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.429 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.167 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=516)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3313.2914` → IC=+0.151 (n=305)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3313.2914 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.152 (n=159)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 94.0 (IC base=+0.059)

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
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=92)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

- **PATRÓN** `py_entrada` > `0.35` → IC=+0.218 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.35 (IC base=+0.110)

- **PATRÓN** `banda_hit_calibrado` > `0.6297` → IC=+0.239 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6297 (IC base=+0.110)

- **PATRÓN** `banda_z` > `8.424` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.424 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1195.1095` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1195.1095 (IC base=+0.110)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=89)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=-0.004)

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
- **FILTRO** `restante_s_al_confirmar` < `145.81` → IC=-0.219 (n=7604)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.81
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=22812)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `137.94` → IC=-0.246 (n=982)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.94
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2947)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `127.03` → IC=-0.306 (n=895)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.03
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2688)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.14` → IC=-0.205 (n=1856)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.14
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=5573)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.34` → IC=-0.337 (n=1494)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.34
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=4485)

### CANDIDATA9_BOT_CONSENSO
- **FILTRO** `py_entrada` < `0.48` → IC=-0.224 (n=385)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=385)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=174)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=542)

- **FILTRO** `py_entrada` < `0.48` → IC=-0.145 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=566)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.208 (n=14916)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3680)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5600.4068` → IC=+0.177 (n=2365)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5600.4068 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.135 (n=12578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=15501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.230 (n=11900)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=5989)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7781.3502` → IC=+0.171 (n=2280)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7781.3502 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.212 (n=1820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1778)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=2238)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `15920.3308` → IC=+0.238 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15920.3308 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=1601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1787)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.262 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `15860.4955` → IC=+0.214 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15860.4955 (IC base=+0.197)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.169 (n=351)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.615 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.142 (n=241)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.097)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.134 (n=574)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 11.0 (IC base=+0.100)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=870)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.162 (n=226)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.100)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3058)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.151 (n=2612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.150)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.347 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.366 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.233 (n=1591)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `4229.7127` → IC=+0.231 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4229.7127 (IC base=+0.228)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.155 (n=505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.136 (n=729)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.254 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.137 (n=825)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.02 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `1315.39` → IC=+0.147 (n=723)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1315.39 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.076)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` > `0.87` → IC=+0.429 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.87 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.154 (n=1153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` < `0.285` → IC=+0.308 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.285 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=767)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.152)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.369 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `1222.0032` → IC=+0.155 (n=233)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1222.0032 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.219 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.116)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.76` → IC=-0.289 (n=131)

  - _Acción_: SKIP cuando `py_entrada` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=12720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=12165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.229 (n=4092)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `3571.1845` → IC=+0.331 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3571.1845 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=3043)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.173 (n=2888)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=2900)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.252 (n=1081)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.249 (n=1079)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.245)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.341 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.245)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=2994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2858)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2417)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=2635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.326 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.242)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=2914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=2807)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.196 (n=2193)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.435 (n=584)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.939` → IC=+0.464 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.939 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `11247.6748` → IC=+0.459 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11247.6748 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.443 (n=224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.446 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.452 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `14277.5065` → IC=+0.447 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14277.5065 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.450 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.463 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.426 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `3322.2122` → IC=+0.446 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3322.2122 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.413 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.410)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.425 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.410)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.410)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=37817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.236 (n=16734)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=7682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5262)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7097)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=6819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.263 (n=3873)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=6892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=6889)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=6271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2501)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=7098)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=6347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=2906)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=5744)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.18` → IC=+0.124 (n=5366)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.18 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5425)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=7121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.59` → IC=+0.137 (n=5338)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.59 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=2888)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.14` → IC=+0.125 (n=2654)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.14 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.139 (n=2676)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=3514)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.140 (n=2658)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 3.28 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.186 (n=2856)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.132 (n=3003)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.136 (n=2693)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.302 (n=1269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1545.7265` → IC=+0.294 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1545.7265 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=560)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.344 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5065.6943` → IC=+0.306 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5065.6943 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.324 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1447.2132` → IC=+0.303 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1447.2132 (IC base=+0.287)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.352 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.345)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.345)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.386 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.345)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.349 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.345)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.345)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.435 (n=472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.435 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.436 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.435 (n=260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.435 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.455 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `1978.5089` → IC=+0.465 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.5089 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.394)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.406 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.394)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.394)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1366.4094` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1366.4094 (IC base=+0.259)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `py_entrada` > `0.765` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.308 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.383 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.276 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1366.4094` → IC=+0.287 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1366.4094 (IC base=+0.259)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4919` → IC=+0.127 (n=8993)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.4919 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.9821` → IC=+0.242 (n=2997)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9821 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.2206` → IC=+0.259 (n=1986)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2206 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.971` → IC=+0.180 (n=3432)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.971 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.252 (n=2479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2084 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` > `0.6161` → IC=+0.254 (n=2478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6161 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.226 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` > `1.8951` → IC=+0.211 (n=4150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8951 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.5701` → IC=+0.134 (n=10898)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5701 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.6054` → IC=+0.203 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6054 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.184 (n=1716)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6971 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `0.8691` → IC=+0.176 (n=2599)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8691 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.223 (n=1874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.569` → IC=+0.199 (n=5926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.569 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.213 (n=6427)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=+0.067)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.197 (n=677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.176 (n=674)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0081 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3528` → IC=+0.173 (n=2008)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3528 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.174 (n=1359)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 11.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.164` → IC=+0.269 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.164 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.208 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.4344` → IC=+0.169 (n=1887)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4344 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.183 (n=2025)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.250 (n=714)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0913` → IC=+0.278 (n=524)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0913 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=1418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0549` → IC=+0.290 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0549 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.551` → IC=+0.241 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.551 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.461` → IC=+0.244 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.461 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.275 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.586` → IC=+0.246 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.586 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1658.02` → IC=+0.249 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1658.02 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.240 (n=695)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3538` → IC=+0.229 (n=1573)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3538 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.238 (n=1574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.221 (n=1604)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.9845` → IC=+0.269 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9845 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3484` → IC=+0.224 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3484 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.479` → IC=+0.258 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.479 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2525` → IC=+0.223 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2525 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.0844` → IC=+0.227 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0844 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.239 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7497` → IC=+0.223 (n=1029)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7497 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.233 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11003.4334` → IC=+0.224 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11003.4334 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.164 (n=1079)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0039 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.162 (n=540)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=729)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.3342` → IC=+0.193 (n=1075)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.3342 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1316` → IC=+0.151 (n=1450)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1316 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.356` → IC=+0.160 (n=254)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.356 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.327` → IC=+0.142 (n=1482)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.327 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.147 (n=1612)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2116 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8575` → IC=+0.139 (n=1074)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8575 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.177 (n=425)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.151 (n=1501)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.147 (n=1001)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `14001.0043` → IC=+0.142 (n=1074)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 14001.0043 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.171 (n=627)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 231.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.213 (n=671)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=2117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1812)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.255 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.193 (n=1761)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.3548` → IC=+0.205 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3548 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.7731` → IC=+0.197 (n=1718)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7731 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.195 (n=2391)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.217 (n=1756)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.6287` → IC=+0.213 (n=1755)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6287 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.215 (n=825)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.0637` → IC=+0.240 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0637 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.697` → IC=+0.227 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.697 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.57` → IC=+0.212 (n=1902)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.57 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.252 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.7484` → IC=+0.206 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7484 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `3.2498` → IC=+0.226 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2498 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1908.841` → IC=+0.215 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.841 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.211 (n=1386)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.209)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.158 (n=109)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=2433)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.141 (n=393)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0037 (IC base=+0.038)

- **PATRÓN** `ibs_20min` > `0.9519` → IC=+0.221 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9519 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` < `0.1949` → IC=+0.336 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1949 (IC base=+0.038)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.824` → IC=+0.171 (n=798)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.824 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.337 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.345 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.356 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.334 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.038)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.334 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.038)

- **PATRÓN** `ibs_20min` < `0.1047` → IC=+0.152 (n=636)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1047 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.6671` → IC=+0.205 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6671 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.6885` → IC=+0.155 (n=424)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6885 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1666` → IC=+0.147 (n=321)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1666 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2304` → IC=+0.202 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2304 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.5315` → IC=+0.165 (n=813)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5315 (IC base=+0.020)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=365)

- **FILTRO** `ibs_20min` < `0.2941` → IC=-0.200 (n=108)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=324)

- **FILTRO** `ibs_20min` > `0.2456` → IC=-0.124 (n=2432)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2456
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=1199)

- **FILTRO** `sigma_ewma_delta_pct` > `8.696` → IC=-0.217 (n=383)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.696
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3248)

- **PATRÓN** `ibs_20min` > `0.7834` → IC=+0.205 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7834 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `1.7756` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.7756 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` < `0.5528` → IC=+0.273 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5528 (IC base=+0.042)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.5152` → IC=+0.278 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5152 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `1.4536` → IC=+0.261 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4536 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.286 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.2456` → IC=+0.126 (n=1199)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.2456 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7292` → IC=+0.247 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7292 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.4655` → IC=+0.236 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4655 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.6727` → IC=+0.275 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6727 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1591` → IC=+0.289 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1591 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.283 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6579` → IC=-0.184 (n=632)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6579
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1899)

- **FILTRO** `ibs_20min` < `0.7212` → IC=-0.156 (n=1670)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7212
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=861)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.203 (n=551)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1980)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.210 (n=930)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=2828)

- **PATRÓN** `dist_vwap_pct` > `0.4614` → IC=+0.326 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4614 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.21` → IC=+0.318 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.21 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.312 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.302 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.4239` → IC=+0.303 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4239 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.300 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5629` → IC=+0.284 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5629 (IC base=-0.019)

- **PATRÓN** `volumen_regimen` < `0.7286` → IC=+0.258 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7286 (IC base=-0.019)

- **PATRÓN** `volumen_regimen` > `1.2485` → IC=+0.283 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2485 (IC base=-0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.0991` → IC=+0.269 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0991 (IC base=-0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.141` → IC=+0.262 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.141 (IC base=-0.019)

- **PATRÓN** `volumen_spike_ratio` > `1.5239` → IC=+0.255 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5239 (IC base=-0.019)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.197 (n=3841)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0098 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4745` → IC=+0.187 (n=10292)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4745 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `1.0207` → IC=+0.289 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0207 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.158 (n=5320)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.1808` → IC=+0.243 (n=4134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1808 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `0.6905` → IC=+0.255 (n=3692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6905 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2924` → IC=+0.269 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2924 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.462` → IC=+0.241 (n=2230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.462 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `2.6435` → IC=+0.250 (n=2229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6435 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.272 (n=6228)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.167 (n=3754)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0092 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5484` → IC=+0.155 (n=9910)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5484 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.712` → IC=+0.254 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.712 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2514` → IC=+0.245 (n=3222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2514 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7098` → IC=+0.246 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7098 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.205` → IC=+0.254 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.205 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2414` → IC=+0.303 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2414 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5941` → IC=+0.268 (n=2007)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5941 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2837` → IC=+0.264 (n=2068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2837 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.274 (n=4444)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2526` → IC=-0.155 (n=795)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2526
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2388)

- **FILTRO** `ibs_20min` > `0.7572` → IC=-0.148 (n=651)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7572
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=1955)

- **FILTRO** `sigma_ewma_delta_pct` > `4.528` → IC=-0.166 (n=594)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.528
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2012)

- **PATRÓN** `ibs_20min` > `0.8964` → IC=+0.271 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8964 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.223` → IC=+0.195 (n=571)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 7.223 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2226` → IC=+0.261 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2226 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.4395` → IC=+0.192 (n=339)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4395 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.1547` → IC=+0.215 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1547 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.209 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.093` → IC=+0.452 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.093 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4701` → IC=+0.451 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4701 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.7565` → IC=+0.439 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7565 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.488 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8684` → IC=+0.166 (n=773)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8684 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.2995` → IC=+0.180 (n=411)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2995 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.6747` → IC=+0.180 (n=953)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6747 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.232 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.201 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.3955` → IC=+0.170 (n=349)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.3955 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.208 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 236.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.1527` → IC=+0.222 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1527 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.8596` → IC=+0.231 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8596 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2683` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2683 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.244 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `456.0` → IC=+0.219 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 456.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.279 (n=1188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.254 (n=1789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.251 (n=1801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.299 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.691` → IC=+0.281 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.691 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.265 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `3.294` → IC=+0.269 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.294 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=2096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `1912.1584` → IC=+0.259 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.1584 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.310 (n=663)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.184` → IC=+0.295 (n=642)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.184 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.327 (n=488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.291 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.693` → IC=+0.289 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.693 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.8` → IC=+0.285 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.8 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.3387` → IC=+0.291 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3387 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.5833` → IC=+0.294 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5833 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.6851` → IC=+0.292 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6851 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `1902.41` → IC=+0.296 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1902.41 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.287 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.283)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7739` → IC=-0.189 (n=670)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7739
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=2013)

- **PATRÓN** `ibs_20min` > `0.9124` → IC=+0.183 (n=581)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.9124 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.187` → IC=+0.232 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.187 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.0017` → IC=+0.248 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0017 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.5867` → IC=+0.225 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5867 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.0807` → IC=+0.263 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0807 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.3995` → IC=+0.267 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3995 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.7566` → IC=+0.240 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7566 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.257 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.221 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1525 (IC base=-0.007)

- **PATRÓN** `volumen_regimen` < `0.6435` → IC=+0.235 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6435 (IC base=-0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.8148` → IC=+0.257 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8148 (IC base=-0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.244 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.007)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.262 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=-0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7468` → IC=-0.190 (n=1222)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=+0.280 (n=1223)

- **FILTRO** `ibs_20min` > `0.68` → IC=-0.236 (n=612)

  - _Acción_: SKIP cuando `ibs_20min` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=1847)

- **FILTRO** `sigma_ewma_delta_pct` > `4.71` → IC=-0.193 (n=535)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.71
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1924)

- **PATRÓN** `ibs_20min` > `0.7468` → IC=+0.280 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7468 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `1.0993` → IC=+0.327 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0993 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.659` → IC=+0.166 (n=384)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.659 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.8618` → IC=+0.308 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8618 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` > `0.639` → IC=+0.299 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.639 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` < `0.0998` → IC=+0.299 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0998 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.325 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4267 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.324 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.5778` → IC=+0.127 (n=1623)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.5778 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` > `0.7382` → IC=+0.215 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7382 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` < `0.2979` → IC=+0.229 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2979 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.255 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.223 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.237 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `2.46` → IC=+0.240 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.46 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.253 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.018)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0168` → IC=+0.315 (n=974)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0168 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.298 (n=690)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.323 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7391 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2183` → IC=+0.314 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2183 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.655` → IC=+0.303 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.655 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` > `0.8619` → IC=+0.306 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8619 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` < `0.0784` → IC=+0.283 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0784 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.329 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `1.4307` → IC=+0.288 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4307 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2454.0554` → IC=+0.290 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2454.0554 (IC base=+0.279)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.318 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0156` → IC=+0.309 (n=1036)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0156 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.1984` → IC=+0.287 (n=684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1984 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.292 (n=528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.1389` → IC=+0.333 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1389 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.3209` → IC=+0.291 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3209 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` < `0.2317` → IC=+0.280 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2317 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.095` → IC=+0.305 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.095 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.283 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `1.2436` → IC=+0.310 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2436 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.235` → IC=+0.331 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.235 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `1.4259` → IC=+0.289 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4259 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.1403` → IC=+0.279 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1403 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2399.8048` → IC=+0.283 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.8048 (IC base=+0.280)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.178 (n=2925)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.204 (n=2918)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.3638` → IC=+0.177 (n=7703)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3638 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=9151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.221 (n=8764)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1769` → IC=+0.194 (n=3778)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1769 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.352` → IC=+0.251 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.352 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.2075` → IC=+0.163 (n=5824)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2075 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.161 (n=5825)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6285 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2417` → IC=+0.195 (n=1763)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2417 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5576` → IC=+0.169 (n=3700)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5576 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6056` → IC=+0.174 (n=2803)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6056 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `1945.202` → IC=+0.171 (n=7820)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1945.202 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.183 (n=7677)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 110.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.184 (n=5610)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0067 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.082` → IC=+0.212 (n=2805)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.082 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=3218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.4839` → IC=+0.225 (n=8417)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4839 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.2371` → IC=+0.161 (n=6104)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2371 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.336` → IC=+0.197 (n=1415)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.336 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.156 (n=6050)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1776 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.212 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5608` → IC=+0.170 (n=3400)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5608 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6136` → IC=+0.172 (n=2575)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6136 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.178 (n=7386)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 110.0 (IC base=+0.169)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.222 (n=491)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.191 (n=493)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0083 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3429` → IC=+0.210 (n=1469)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3429 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=1552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.196 (n=989)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.307 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.237 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.5417` → IC=+0.178 (n=1366)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.5417 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.185 (n=1365)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=1486)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.243 (n=983)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.247 (n=998)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1878` → IC=+0.290 (n=745)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1878 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=1072)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.239 (n=1031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3485` → IC=+0.261 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3485 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.305` → IC=+0.249 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.305 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.235 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.256 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.262 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1548.958` → IC=+0.251 (n=1116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1548.958 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.240 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.0732` → IC=+0.195 (n=437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0732 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=1312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.3983` → IC=+0.227 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3983 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.208 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.479` → IC=+0.230 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.479 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2572` → IC=+0.166 (n=1309)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2572 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `1.0781` → IC=+0.164 (n=593)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.0781 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.206 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5024` → IC=+0.181 (n=560)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5024 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `2.4602` → IC=+0.160 (n=424)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4602 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `10581.1275` → IC=+0.169 (n=1308)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10581.1275 (IC base=+0.162)

- **PATRÓN** `ballena_activa_n` < `383.0` → IC=+0.161 (n=1085)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 383.0 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.157 (n=1400)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0057 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.291` → IC=+0.163 (n=1397)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.291 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.5802` → IC=+0.188 (n=1397)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.5802 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1334` → IC=+0.161 (n=1389)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1334 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.912` → IC=+0.209 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.912 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2129` → IC=+0.157 (n=1397)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2129 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.147 (n=426)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.4481` → IC=+0.146 (n=1285)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4481 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4235` → IC=+0.136 (n=1285)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4235 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `210.0` → IC=+0.170 (n=401)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 210.0 (IC base=+0.137)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.223 (n=665)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.2466` → IC=+0.221 (n=976)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2466 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.277 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2017` → IC=+0.209 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2017 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.7959` → IC=+0.200 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7959 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.7565` → IC=+0.216 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7565 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1726)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.235 (n=1099)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1437` → IC=+0.252 (n=550)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1437 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.274 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.245 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.685` → IC=+0.251 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.685 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3531` → IC=+0.248 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3531 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7564` → IC=+0.222 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7564 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `3.3132` → IC=+0.235 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3132 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.217 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1904.2932` → IC=+0.219 (n=567)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.2932 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.212 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.217)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.179 (n=1240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0066 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.161 (n=1405)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=1470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3616` → IC=+0.198 (n=1405)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3616 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.153` → IC=+0.179 (n=923)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.153 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.222 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8554` → IC=+0.155 (n=937)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8554 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6196` → IC=+0.147 (n=1405)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6196 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.101` → IC=+0.187 (n=596)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.101 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4275` → IC=+0.162 (n=459)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4275 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5072` → IC=+0.167 (n=458)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5072 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `5222.8208` → IC=+0.188 (n=937)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 5222.8208 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.151 (n=1341)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 158.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=1474)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3834` → IC=+0.145 (n=1474)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3834 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6527` → IC=+0.169 (n=1474)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6527 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.961` → IC=+0.162 (n=518)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.961 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8536` → IC=+0.149 (n=983)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8536 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.173 (n=218)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.8129` → IC=+0.139 (n=900)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8129 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `9652.4338` → IC=+0.166 (n=668)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 9652.4338 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.122 (n=1287)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 155.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.156 (n=725)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0101 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=1638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.5045` → IC=+0.207 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5045 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.2885` → IC=+0.187 (n=887)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2885 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.76` → IC=+0.251 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.76 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.2054` → IC=+0.132 (n=1597)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2054 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `0.6417` → IC=+0.125 (n=1597)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6417 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1634` → IC=+0.126 (n=1601)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1634 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.0978` → IC=+0.125 (n=608)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0978 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5416` → IC=+0.135 (n=678)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.5416 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=1663)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2873.0862` → IC=+0.198 (n=724)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2873.0862 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.138 (n=1245)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 48.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.161 (n=718)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0062 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1057` → IC=+0.167 (n=541)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1057 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5745` → IC=+0.213 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5745 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2099` → IC=+0.144 (n=1495)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2099 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.335` → IC=+0.130 (n=495)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 5.335 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6381` → IC=+0.147 (n=542)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6381 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.160 (n=283)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.141 (n=491)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4306` → IC=+0.134 (n=490)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4306 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2729.0252` → IC=+0.165 (n=735)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2729.0252 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.125 (n=1410)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 52.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.228 (n=1352)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.1357` → IC=+0.206 (n=505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1357 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.6491` → IC=+0.246 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6491 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.2123` → IC=+0.212 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2123 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.237 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.1949` → IC=+0.206 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1949 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.215 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6285 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.262 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.214 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4098` → IC=+0.209 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4098 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2434.1618` → IC=+0.205 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2434.1618 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.226 (n=520)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.215 (n=708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0946` → IC=+0.230 (n=520)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0946 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.02` → IC=+0.300 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.02 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.1962` → IC=+0.231 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1962 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.402` → IC=+0.247 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.402 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6338` → IC=+0.217 (n=1560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6338 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.283 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1933` → IC=+0.200 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1933 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4348` → IC=+0.204 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4348 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2369.7134` → IC=+0.212 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2369.7134 (IC base=+0.207)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.199 (n=751)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.170 (n=746)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0086 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3479` → IC=+0.167 (n=1969)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3479 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.5156` → IC=+0.197 (n=1998)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.5156 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.6099` → IC=+0.177 (n=472)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6099 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.731` → IC=+0.186 (n=990)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.731 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.184 (n=1336)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8725 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.2088` → IC=+0.167 (n=667)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.2088 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.163` → IC=+0.175 (n=610)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.163 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.4352` → IC=+0.177 (n=722)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4352 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8204` → IC=+0.164 (n=1444)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8204 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.167 (n=2538)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `2216.8968` → IC=+0.165 (n=2236)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2216.8968 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.178 (n=2014)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 147.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.139 (n=1530)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0057 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.3455` → IC=+0.128 (n=2017)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3455 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=2147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.0589` → IC=+0.192 (n=764)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0589 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2241` → IC=+0.123 (n=2087)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2241 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.140 (n=573)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4454` → IC=+0.152 (n=739)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4454 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `2771.2508` → IC=+0.121 (n=2047)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2771.2508 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.133 (n=961)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 28.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.169 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0029 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3322` → IC=+0.151 (n=568)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3322 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.6562` → IC=+0.205 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6562 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.291` → IC=+0.163 (n=197)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.291 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.158 (n=255)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.623` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.623 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.1541` → IC=+0.137 (n=591)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1541 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0905` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.0905 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.2024` → IC=+0.145 (n=486)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.2024 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.4937` → IC=+0.137 (n=494)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4937 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=734)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `10464.6185` → IC=+0.152 (n=567)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 10464.6185 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `227.0` → IC=+0.158 (n=361)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 227.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.208 (n=241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.154 (n=713)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.6123` → IC=+0.179 (n=628)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.6123 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.31` → IC=+0.146 (n=756)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.31 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.41` → IC=+0.144 (n=268)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 4.41 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.162` → IC=+0.137 (n=650)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.162 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.142 (n=713)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2216 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `0.7093` → IC=+0.146 (n=637)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7093 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.203 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.1022` → IC=+0.154 (n=619)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1022 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.4106` → IC=+0.143 (n=703)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4106 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `310.0` → IC=+0.149 (n=600)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 310.0 (IC base=+0.135)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.276 (n=310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.212 (n=234)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2112` → IC=+0.222 (n=469)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2112 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9593` → IC=+0.275 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9593 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.15` → IC=+0.219 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.15 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.2204` → IC=+0.211 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2204 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.948` → IC=+0.231 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.948 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.220 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8342 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `1.168` → IC=+0.233 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.168 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.0998` → IC=+0.249 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0998 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.4055` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4055 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.7595` → IC=+0.233 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7595 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.084` → IC=+0.153 (n=220)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.084 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.6877` → IC=+0.137 (n=290)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6877 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.145 (n=105)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.150 (n=498)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0058 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.5425` → IC=+0.139 (n=555)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5425 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.172 (n=514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.263 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `1.0116` → IC=+0.229 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0116 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.496` → IC=+0.185 (n=290)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.496 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.069` → IC=+0.157 (n=488)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.069 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.7177` → IC=+0.143 (n=496)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7177 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1756` → IC=+0.152 (n=153)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1756 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.2097` → IC=+0.168 (n=242)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.2097 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=583)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `3102.4168` → IC=+0.190 (n=185)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3102.4168 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.123 (n=515)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0098 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.0441` → IC=+0.241 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0441 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `1.2218` → IC=+0.129 (n=515)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.2218 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.0757` → IC=+0.123 (n=460)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.0757 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.836` → IC=+0.170 (n=325)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.836 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `1616.593` → IC=+0.123 (n=515)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1616.593 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.148 (n=461)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 39.0 (IC base=+0.105)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.176 (n=3781)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0047 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.209 (n=3768)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=11816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.9976` → IC=+0.310 (n=3768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9976 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.9349` → IC=+0.201 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9349 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.354` → IC=+0.245 (n=2820)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.354 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.8797` → IC=+0.170 (n=5051)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8797 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2384` → IC=+0.197 (n=2095)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2384 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5851` → IC=+0.192 (n=3633)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5851 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1782.7807` → IC=+0.177 (n=11304)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1782.7807 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.199 (n=8742)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 82.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6826)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1507` → IC=+0.191 (n=4497)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1507 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=3848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.4493` → IC=+0.246 (n=8993)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4493 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2526` → IC=+0.161 (n=6370)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2526 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.075` → IC=+0.203 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.075 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.747` → IC=+0.183 (n=9877)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.747 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.705` → IC=+0.163 (n=3068)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.705 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.238 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6081` → IC=+0.191 (n=3154)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6081 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.200 (n=6114)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.220 (n=629)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.210 (n=1258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.3604` → IC=+0.199 (n=1886)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3604 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.213 (n=898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.201 (n=1285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.628` → IC=+0.347 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.628 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2269` → IC=+0.250 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2269 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.8445` → IC=+0.197 (n=1192)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8445 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=1885)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.265 (n=671)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.263 (n=691)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1274` → IC=+0.289 (n=670)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1274 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.3544` → IC=+0.284 (n=1340)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3544 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.507` → IC=+0.263 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.507 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.292 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.549` → IC=+0.258 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.549 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.622` → IC=+0.275 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.622 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=1654)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1659.1648` → IC=+0.273 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1659.1648 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.210 (n=604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1131` → IC=+0.165 (n=797)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1131 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1897)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3047` → IC=+0.207 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3047 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.186 (n=1017)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.176 (n=405)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.15` → IC=+0.157 (n=1645)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.15 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6277` → IC=+0.185 (n=604)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6277 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2665` → IC=+0.189 (n=265)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2665 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `2.1124` → IC=+0.164 (n=1544)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.1124 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.4077` → IC=+0.159 (n=1754)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4077 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `11197.4423` → IC=+0.162 (n=1617)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11197.4423 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `280.0` → IC=+0.177 (n=742)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 280.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.163 (n=1553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3224` → IC=+0.160 (n=1552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3224 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=707)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.2852` → IC=+0.234 (n=1035)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2852 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6658` → IC=+0.157 (n=246)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6658 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1331` → IC=+0.161 (n=1413)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1331 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.523` → IC=+0.172 (n=260)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.523 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.327` → IC=+0.149 (n=1414)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.327 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.161 (n=1552)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1954 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.198 (n=409)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4003` → IC=+0.156 (n=1453)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4003 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.757` → IC=+0.162 (n=969)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.757 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `413.0` → IC=+0.151 (n=1196)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 413.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.260 (n=618)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=1934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=1872)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.371` → IC=+0.300 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.371 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.1336` → IC=+0.221 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1336 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.7692` → IC=+0.229 (n=1578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7692 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1915.447` → IC=+0.226 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.447 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.238 (n=1725)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.6056` → IC=+0.235 (n=1725)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6056 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.236 (n=819)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.3593` → IC=+0.263 (n=1518)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3593 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.149` → IC=+0.277 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.149 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3406` → IC=+0.295 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3406 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7349` → IC=+0.228 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7349 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.1556` → IC=+0.237 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1556 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1905.4784` → IC=+0.240 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1905.4784 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.231 (n=1531)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.194 (n=648)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.436` → IC=+0.150 (n=1933)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.436 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2019)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.2831` → IC=+0.186 (n=1933)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.2831 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3655` → IC=+0.161 (n=758)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3655 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.523` → IC=+0.169 (n=315)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.523 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8703` → IC=+0.158 (n=1289)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8703 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2353` → IC=+0.208 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2353 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.154 (n=825)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.4717` → IC=+0.157 (n=625)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4717 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7649.1944` → IC=+0.242 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7649.1944 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.174 (n=606)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 74.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.166 (n=1045)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0052 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4443` → IC=+0.145 (n=1565)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4443 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.15` → IC=+0.260 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.15 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1611` → IC=+0.133 (n=1359)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1611 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.238` → IC=+0.167 (n=232)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.238 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.148 (n=689)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6971 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `1.2022` → IC=+0.134 (n=522)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.2022 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.221 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.444` → IC=+0.141 (n=1491)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.444 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `9886.4406` → IC=+0.199 (n=522)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 9886.4406 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `172.0` → IC=+0.135 (n=1492)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 172.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.142 (n=1284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0082 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4634` → IC=+0.194 (n=1926)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.4634 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0849` → IC=+0.205 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0849 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.559` → IC=+0.238 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.559 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8902` → IC=+0.143 (n=1284)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8902 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.120 (n=1973)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.1945` → IC=+0.131 (n=848)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.1945 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=1943)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2875.1364` → IC=+0.258 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2875.1364 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.140 (n=1497)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 52.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.180 (n=616)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0058 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.136` → IC=+0.159 (n=614)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.136 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.206 (n=1844)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.223` → IC=+0.134 (n=1518)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.223 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.449` → IC=+0.128 (n=1777)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.449 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.7146` → IC=+0.157 (n=811)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.7146 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2212` → IC=+0.175 (n=287)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2212 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4382` → IC=+0.146 (n=560)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4382 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2755.5964` → IC=+0.180 (n=614)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2755.5964 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.130 (n=1472)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 51.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.230 (n=1704)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=1997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.215 (n=1713)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.263 (n=1709)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.2177` → IC=+0.235 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2177 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.587` → IC=+0.253 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.587 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2401` → IC=+0.215 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2401 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.6407` → IC=+0.223 (n=1908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6407 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.248 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.549` → IC=+0.222 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.549 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1901)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2431.0275` → IC=+0.221 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2431.0275 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.223 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.018` → IC=+0.220 (n=1344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.018 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.218 (n=1412)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.4214` → IC=+0.265 (n=1774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4214 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.223` → IC=+0.215 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.223 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.211 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.263 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.2357` → IC=+0.237 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2357 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.271 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1798` → IC=+0.203 (n=1609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1798 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.204 (n=1828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2377.7754` → IC=+0.208 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2377.7754 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.196 (n=1734)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 37.0 (IC base=+0.207)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=3475)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.188 (n=3040)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0092 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.5153` → IC=+0.184 (n=3453)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.5153 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=1313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.9455` → IC=+0.237 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9455 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1865` → IC=+0.185 (n=1251)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1865 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.4772` → IC=+0.170 (n=2191)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.4772 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.192` → IC=+0.200 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.192 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.172 (n=1015)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.7067 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.8941` → IC=+0.177 (n=1537)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8941 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1688` → IC=+0.206 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1688 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `1.4541` → IC=+0.183 (n=1137)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4541 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.8646` → IC=+0.182 (n=2273)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.8646 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.175 (n=2482)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `2464.7221` → IC=+0.178 (n=3453)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2464.7221 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.203 (n=873)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.3889` → IC=+0.176 (n=2305)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3889 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.175 (n=1186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.1825` → IC=+0.182 (n=1152)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1825 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.6833` → IC=+0.179 (n=490)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6833 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.193` → IC=+0.166 (n=2615)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.193 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.2546` → IC=+0.158 (n=2454)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2546 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.162 (n=2385)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.5396` → IC=+0.165 (n=1138)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5396 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.825` → IC=+0.162 (n=1724)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.825 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=3475)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `12292.3336` → IC=+0.159 (n=873)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12292.3336 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.161 (n=1699)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 83.0 (IC base=+0.155)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.198 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0054 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.182 (n=375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0033 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0866` → IC=+0.232 (n=140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0866 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.193 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 8.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5463` → IC=+0.206 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5463 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2023` → IC=+0.184 (n=362)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.2023 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.174` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.174 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.188 (n=443)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.8386` → IC=+0.209 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8386 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2983` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2983 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.4394` → IC=+0.204 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4394 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6272` → IC=+0.204 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6272 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `12545.7532` → IC=+0.219 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12545.7532 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.217 (n=425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.176 (n=322)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.174 (n=369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.181 (n=424)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1409 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6117` → IC=+0.145 (n=437)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6117 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6926` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.6926 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.162 (n=945)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8794` → IC=+0.188 (n=643)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8794 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0691` → IC=+0.166 (n=447)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0691 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4202` → IC=+0.147 (n=321)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4202 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.824` → IC=+0.151 (n=640)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.824 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `14911.0423` → IC=+0.161 (n=437)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 14911.0423 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `708.0` → IC=+0.143 (n=918)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 708.0 (IC base=+0.139)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.188 (n=213)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.180 (n=289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.01 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.173 (n=637)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.242 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.56` → IC=+0.231 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.56 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.2079` → IC=+0.204 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2079 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `1.6711` → IC=+0.173 (n=212)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.6711 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` > `1.8234` → IC=+0.171 (n=567)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8234 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2429.8516` → IC=+0.204 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2429.8516 (IC base=+0.166)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.241 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.295 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.288 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1988` → IC=+0.259 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1988 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.237)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.196 (n=478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0046 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3797` → IC=+0.184 (n=956)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3797 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.189 (n=486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.5313` → IC=+0.193 (n=725)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.5313 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.8838` → IC=+0.190 (n=362)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.8838 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` < `0.397` → IC=+0.189 (n=1019)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.397 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.254` → IC=+0.190 (n=973)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 4.254 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.0861` → IC=+0.181 (n=956)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.0861 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `1.2514` → IC=+0.187 (n=362)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 1.2514 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.194 (n=328)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `2.4728` → IC=+0.183 (n=1067)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.4728 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=1083)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.199 (n=297)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.004 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.185 (n=886)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.170 (n=594)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 10.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.751` → IC=+0.166 (n=886)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.751 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `0.0956` → IC=+0.166 (n=886)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.0956 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.6046` → IC=+0.185 (n=198)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6046 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.639` → IC=+0.165 (n=910)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.639 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.6472` → IC=+0.191 (n=296)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6472 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.163 (n=792)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.7259 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.1513` → IC=+0.161 (n=915)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.1513 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.173 (n=374)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.174 (n=765)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `7466.057` → IC=+0.174 (n=886)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7466.057 (IC base=+0.159)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.171 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0111 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.167 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 3.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.146 (n=343)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 13.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.255 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.2318` → IC=+0.195 (n=231)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2318 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8924` → IC=+0.171 (n=229)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8924 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `1.2801` → IC=+0.167 (n=115)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.2801 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.232 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7681` → IC=+0.183 (n=222)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.7681 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=408)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.02 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2993.9342` → IC=+0.167 (n=343)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2993.9342 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.166 (n=285)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 51.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.187 (n=289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0069 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3939` → IC=+0.197 (n=193)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3939 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.163 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 16.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.6836` → IC=+0.197 (n=255)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6836 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.6343` → IC=+0.229 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6343 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.315` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.315 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.203` → IC=+0.167 (n=280)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 5.203 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.3724` → IC=+0.170 (n=289)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.3724 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.224 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.5187` → IC=+0.188 (n=94)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.5187 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.162 (n=128)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3162.2916` → IC=+0.198 (n=289)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3162.2916 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.204 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.159)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.188 (n=142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=427)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.174 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0039 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.125 (n=965)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 8.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6471` → IC=+0.189 (n=866)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.6471 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1483` → IC=+0.147 (n=520)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1483 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.429` → IC=+0.190 (n=227)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.429 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.192 (n=131)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `1378.8357` → IC=+0.122 (n=630)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1378.8357 (IC base=+0.085)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.123 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0045 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.302 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.182` → IC=+0.134 (n=394)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.182 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.036` → IC=+0.145 (n=136)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.036 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.1368` → IC=+0.216 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1368 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.5184` → IC=+0.145 (n=291)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.5184 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.4395` → IC=+0.137 (n=260)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4395 (IC base=+0.032)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.136 (n=300)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.02 (IC base=+0.032)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.147 (n=366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0058 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4562` → IC=+0.176 (n=334)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4562 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.0809` → IC=+0.151 (n=259)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.0809 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.134 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0044 (IC base=+0.079)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.173 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.079)

- **PATRÓN** `ibs_20min` < `0.2748` → IC=+0.252 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2748 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.0673` → IC=+0.143 (n=169)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.0673 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.92` → IC=+0.181 (n=155)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.92 (IC base=+0.079)

- **PATRÓN** `volumen_regimen` < `0.6161` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6161 (IC base=+0.079)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.079)

- **PATRÓN** `volumen_spike_ratio` < `2.4111` → IC=+0.171 (n=138)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.4111 (IC base=+0.079)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6741` → IC=-0.136 (n=141)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6741
  - _Potencial_: sin este filtro IC_bueno=+0.221 (n=292)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=139)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.142 (n=238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0049 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.131 (n=334)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.221 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.3424` → IC=+0.195 (n=129)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3424 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.779` → IC=+0.284 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.779 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.807` → IC=+0.130 (n=217)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.807 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.7434` → IC=+0.147 (n=182)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.7434 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `1128.1831` → IC=+0.150 (n=287)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1128.1831 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.1674` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1674 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1303` → IC=+0.140 (n=112)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1303 (IC base=+0.011)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.256` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.256 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.1312` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1312 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.3281` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.3281 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.1755` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.1755 (IC base=+0.011)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.011)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.01` → IC=-0.269 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=100)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.229 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=104)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=73)

- **PATRÓN** `ibs_20min` > `0.7826` → IC=+0.189 (n=207)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7826 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `1.0159` → IC=+0.139 (n=70)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 1.0159 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.144` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 8.144 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.2389` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2389 (IC base=+0.058)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.154 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0066 (IC base=-0.020)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.233 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=-0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.815` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.815 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.4788` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4788 (IC base=-0.020)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.303 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=151)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.365 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=175)

- **FILTRO** `dist_vwap_pct` > `0.1657` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1657
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=202)

- **FILTRO** `volumen_regimen` < `0.7224` → IC=-0.345 (n=56)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7224
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=169)

- **FILTRO** `volumen_spike_ratio` > `3.0912` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.0912
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=114)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.359 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=122)

- **FILTRO** `dist_vwap_pct` > `0.3287` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3287
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=151)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=154)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=82)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.250 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=39)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.275 (n=38)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=39)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.309 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=57)

- **FILTRO** `dist_vwap_pct` < `0.0874` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0874
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=32)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7335` → IC=-0.446 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7335
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `volumen_spike_ratio` > `2.5041` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.5041
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=30)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.389 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=49)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.375 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

- **PATRÓN** `ibs_20min` > `0.9883` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9883 (IC base=-0.226)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=61)

- **FILTRO** `ibs_20min` < `0.125` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.125
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1622` → IC=-0.122 (n=133)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1622
  - _Potencial_: sin este filtro IC_bueno=+0.181 (n=261)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.159 (n=130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0059 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.153 (n=286)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6429 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.512` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.512 (IC base=+0.085)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.130 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.004 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.181 (n=261)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1622 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.007` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.007 (IC base=+0.078)

- **PATRÓN** `libro_liquidez` > `3787.1326` → IC=+0.184 (n=134)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3787.1326 (IC base=+0.078)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=101)

- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=93)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.167 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0034 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.211 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.203 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1681 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.3016` → IC=+0.147 (n=165)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3016 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.794` → IC=+0.153 (n=122)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 6.794 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.138` → IC=+0.152 (n=136)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.138 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.6881` → IC=+0.192 (n=105)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.6881 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.164 (n=105)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4359.9001` → IC=+0.156 (n=91)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4359.9001 (IC base=+0.139)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6305` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6305
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=79)

- **FILTRO** `libro_liquidez` < `1348.7155` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 1348.7155
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=79)

- **FILTRO** `ibs_20min` > `0.156` → IC=-0.144 (n=43)

  - _Acción_: SKIP cuando `ibs_20min` > 0.156
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=86)

- **PATRÓN** `sigma_h` < `0.0023` → IC=+0.203 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0023 (IC base=+0.014)

- **PATRÓN** `ibs_20min` > `0.8766` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.8766 (IC base=+0.014)

- **PATRÓN** `libro_liquidez` > `1627.214` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1627.214 (IC base=+0.014)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.130 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0053 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.182 (n=86)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.156 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.706` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.706 (IC base=+0.072)

- **PATRÓN** `volumen_regimen` < `0.9961` → IC=+0.125 (n=86)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.9961 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.0745` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.0745 (IC base=+0.072)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `volumen_pendiente_norm` < `0.0772` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` < 0.0772
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=21)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.263 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.248 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.227 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.9714` → IC=+0.247 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9714 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.254 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.300 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.4833` → IC=+0.400 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4833 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `579.6494` → IC=+0.224 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 579.6494 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.046)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.2733` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2733 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.346 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1695.0` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1695.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.222)

- **PATRÓN** `elapsed_s` > `184.2` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.2 (IC base=+0.222)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.222)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.328 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.222)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4605` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4605 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `193.7` → IC=+0.372 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 193.7 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.2733` → IC=+0.452 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2733 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.8011` → IC=+0.346 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8011 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1695.0` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1695.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.222)

- **PATRÓN** `elapsed_s` > `184.2` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.2 (IC base=+0.222)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.222)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.328 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `1768.0` → IC=+0.311 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1768.0 (IC base=+0.222)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=814)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2900.177` → IC=+0.163 (n=280)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2900.177 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2335.12` → IC=+0.120 (n=867)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 2335.12 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.122 (n=814)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2900.177` → IC=+0.163 (n=280)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2900.177 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2335.12` → IC=+0.120 (n=867)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 2335.12 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `py_entrada` < `0.435` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `py_entrada` < 0.435
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=119)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=141)

- **FILTRO** `libro_liquidez` < `11811.9773` → IC=-0.164 (n=117)

  - _Acción_: SKIP cuando `libro_liquidez` < 11811.9773
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=40)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=222)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=208)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=44)

- **FILTRO** `libro_liquidez` < `10452.0502` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 10452.0502
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `libro_liquidez` < `15479.8554` → IC=-0.133 (n=28)

  - _Acción_: SKIP cuando `libro_liquidez` < 15479.8554
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=90)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=2044)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=50)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=82)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=93)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=89)

### LIQUIDACIONES_5M#BTC#5min
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

- **PATRÓN** `liq_usd_total` > `59480.98` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `liq_usd_total` > 59480.98 (IC base=+0.025)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=875)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=829)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=476)

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
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=210)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=79)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.022)

- **PATRÓN** `libro_liquidez` > `3962.9688` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 3962.9688 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=686)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=686)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=417)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=417)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=185)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=185)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=101)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=125)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=227)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=104)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=107)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=259)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=259)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.157 (n=68)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=221)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=148)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.137 (n=400)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1040)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **PATRÓN** `py_entrada` > `0.52` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.52 (IC base=+0.016)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.147 (n=100)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.56 (IC base=+0.053)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` > `13.33` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `restante_min` > 13.33
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=64)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=72)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.147 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 9.0 (IC base=+0.089)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.132 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=34)

- **FILTRO** `profundidad_ratio` < `54.9` → IC=-0.232 (n=39)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.9
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=80)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=109)

- **FILTRO** `profundidad_ratio` < `19.0` → IC=-0.160 (n=45)

  - _Acción_: SKIP cuando `profundidad_ratio` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=92)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.53 (IC base=-0.029)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.47 (IC base=-0.040)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=125)

- **FILTRO** `restante_min` < `3.46` → IC=-0.255 (n=51)

  - _Acción_: SKIP cuando `restante_min` < 3.46
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=104)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.173 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=105)

- **FILTRO** `lag_apertura_s` > `91.82` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `lag_apertura_s` > 91.82
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=103)

- **FILTRO** `profundidad_ratio` < `77.2` → IC=-0.209 (n=77)

  - _Acción_: SKIP cuando `profundidad_ratio` < 77.2
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=78)

- **PATRÓN** `profundidad_ratio` > `10.3` → IC=+0.126 (n=105)

  - _Acción_: Kelly boost +0.63€ cuando `profundidad_ratio` > 10.3 (IC base=+0.067)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **PATRÓN** `restante_min` > `13.44` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 13.44 (IC base=+0.011)

- **PATRÓN** `lag_apertura_s` < `91.0` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 91.0 (IC base=+0.011)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.136 (n=108)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=61)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.5 (IC base=-0.021)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.259 (n=56)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=147)

- **FILTRO** `restante_min` < `3.26` → IC=-0.127 (n=65)

  - _Acción_: SKIP cuando `restante_min` < 3.26
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=138)

- **FILTRO** `lag_apertura_s` > `101.85` → IC=-0.134 (n=69)

  - _Acción_: SKIP cuando `lag_apertura_s` > 101.85
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=134)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7798)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.167 (n=3923)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=12098)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.163 (n=4053)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=12549)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.203 (n=685)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=2118)

- **PATRÓN** `libro_liquidez` > `1558.4` → IC=+0.135 (n=1010)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1558.4 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.182 (n=696)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2162)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=713)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2278)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.170 (n=683)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2119)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.171 (n=731)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=2260)

- **PATRÓN** `libro_liquidez` > `2575.0556` → IC=+0.121 (n=953)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 2575.0556 (IC base=+0.022)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2223)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=2345)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3085)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=410)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=401)

- **FILTRO** `libro_liquidez` < `17032.3169` → IC=-0.145 (n=229)

  - _Acción_: SKIP cuando `libro_liquidez` < 17032.3169
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=690)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ballena_activa_n` > `89.0` → IC=-0.218 (n=115)

  - _Acción_: SKIP cuando `ballena_activa_n` > 89.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=228)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=230)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=11274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=25063)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=9029)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=27308)

- **FILTRO** `ibs_7min` < `0.2719` → IC=-0.235 (n=9083)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2719
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=27254)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=12110)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=24227)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.232 (n=11236)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=34748)

- **FILTRO** `ibs_7min` > `0.2917` → IC=-0.179 (n=11475)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2917
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=34509)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.140 (n=1836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4250)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=1457)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4629)

- **FILTRO** `ibs_7min` < `0.7087` → IC=-0.255 (n=2008)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7087
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=4078)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.178 (n=1466)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4620)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.261 (n=1955)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=5959)

- **FILTRO** `ibs_7min` > `0.7895` → IC=-0.208 (n=1977)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7895
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=5937)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=1476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=4762)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1520)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4718)

- **FILTRO** `ibs_7min` < `0.746` → IC=-0.196 (n=1559)

  - _Acción_: SKIP cuando `ibs_7min` < 0.746
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4679)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.181 (n=1555)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4683)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=1469)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4894)

- **FILTRO** `ibs_7min` > `0.2621` → IC=-0.185 (n=1588)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2621
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4775)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.181 (n=1583)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4780)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.163 (n=1640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=4153)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=1438)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4355)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.243 (n=1903)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3890)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.210 (n=1411)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=4382)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.246 (n=1953)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=6526)

- **FILTRO** `ibs_7min` > `0.748` → IC=-0.177 (n=2119)

  - _Acción_: SKIP cuando `ibs_7min` > 0.748
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=6360)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.242 (n=1466)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4519)

- **FILTRO** `ibs_7min` < `0.7407` → IC=-0.181 (n=1495)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4490)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.173 (n=1446)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4539)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.256 (n=1531)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4617)

- **FILTRO** `ibs_7min` > `0.2759` → IC=-0.176 (n=1534)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4614)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.181 (n=1507)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4641)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.262 (n=1484)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4762)

- **FILTRO** `ibs_7min` < `0.2759` → IC=-0.232 (n=1560)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4686)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.169 (n=2175)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=6603)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.271 (n=1476)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4513)

- **FILTRO** `ibs_7min` < `0.285` → IC=-0.223 (n=1497)

  - _Acción_: SKIP cuando `ibs_7min` < 0.285
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4492)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.214 (n=1413)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=4576)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.208 (n=1944)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=6358)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1159)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=574)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=332)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=575)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.132 (n=823)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=739)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.150 (n=275)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 459.6089 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4061` → IC=+0.131 (n=166)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.4061 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.199 (n=131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `422.506` → IC=+0.133 (n=164)

  - _Acción_: Kelly boost +0.66€ cuando `total_vol_5m` < 422.506 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `2333.2912` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2333.2912 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.155 (n=82)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 14.0 (IC base=+0.131)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 11.0 (IC base=+0.110)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.184 (n=115)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.102)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.102)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.175 (n=75)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 73.0 (IC base=+0.102)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.169 (n=143)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.240 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `6100.528` → IC=+0.156 (n=126)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 6100.528 (IC base=+0.130)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.151 (n=147)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.127 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 13.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.257 (n=286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=141)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.247 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=35)

- **FILTRO** `T_h` > `95.4629` → IC=-0.412 (n=32)

  - _Acción_: SKIP cuando `T_h` > 95.4629
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.112)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.221 (n=59)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.8113` → IC=-0.238 (n=105)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8113
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=316)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.324 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=271)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.326 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=270)

- **FILTRO** `T_h` > `61.7816` → IC=-0.316 (n=269)

  - _Acción_: SKIP cuando `T_h` > 61.7816
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=91)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `63.9952` → IC=-0.143 (n=110)

  - _Acción_: SKIP cuando `T_h` > 63.9952
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

- **FILTRO** `pct_vs_K` |x|> `2.84` → IC=-0.368 (n=36)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.84
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=112)

- **FILTRO** `T_h` > `144.522` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `T_h` > 144.522
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=104)

- **FILTRO** `pct_vs_K` |x|> `2.9616` → IC=-0.438 (n=46)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9616
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=90)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9836` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `T_h` > 135.9836
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=89)

- **FILTRO** `pct_vs_K` |x|> `2.4229` → IC=-0.357 (n=54)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4229
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=64)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.333 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=85)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.333 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=85)

- **FILTRO** `T_h` > `60.9515` → IC=-0.331 (n=75)

  - _Acción_: SKIP cuando `T_h` > 60.9515
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=38)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0141` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0141
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=78)

- **FILTRO** `T_h` > `135.7816` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `T_h` > 135.7816
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=78)

- **FILTRO** `pct_vs_K` |x|> `3.8` → IC=-0.230 (n=35)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=68)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.373 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=18)

- **FILTRO** `T_h` > `58.2361` → IC=-0.373 (n=53)

  - _Acción_: SKIP cuando `T_h` > 58.2361
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=18)

- **PATRÓN** `pct_vs_K` |x|≤ `1.0286` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.0286 (IC base=-0.043)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1186` → IC=+0.452 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1186 (IC base=+0.370)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.405 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.370)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.405 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.370)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.419 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.370)

- **PATRÓN** `dist_50` > `0.4222` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4222 (IC base=+0.370)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.412 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.370)

- **PATRÓN** `edge` > `0.097` → IC=+0.451 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.097 (IC base=+0.416)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.416)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.445 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.416)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.429 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.416)

- **PATRÓN** `T_h` > `1.48` → IC=+0.446 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.48 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.4092` → IC=+0.481 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4092 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.474 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.416)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1078` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1078 (IC base=+0.414)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.400 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.414)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.450 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.414)

- **PATRÓN** `T_h` < `0.9168` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9168 (IC base=+0.414)

- **PATRÓN** `dist_50` > `0.4178` → IC=+0.473 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4178 (IC base=+0.414)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.414)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.429 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.414)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.474 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.447)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.473 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.447)

- **PATRÓN** `T_h` < `1.0409` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0409 (IC base=+0.447)

- **PATRÓN** `T_h` > `0.8566` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8566 (IC base=+0.447)

- **PATRÓN** `dist_50` > `0.4692` → IC=+0.466 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4692 (IC base=+0.447)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.447)

- **PATRÓN** `edge` > `0.1155` → IC=+0.470 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.487 (n=73)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.463)

- **PATRÓN** `T_h` > `0.8072` → IC=+0.464 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8072 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.5` → IC=+0.485 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.5 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.468 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=208)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=315)

- **FILTRO** `streak_estiramiento` > `0.8469` → IC=-0.171 (n=68)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8469
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=206)

- **PATRÓN** `streak_estiramiento` < `0.3906` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `streak_estiramiento` < 0.3906 (IC base=+0.033)

- **PATRÓN** `streak_estiramiento` < `0.5782` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.5782 (IC base=+0.029)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=20)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=-0.013)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `2331737.7` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 2331737.7
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=48)

- **FILTRO** `streak_estiramiento` > `0.4576` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4576
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=38)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.4576 (IC base=-0.008)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.121 (n=93)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 49.0 (IC base=+0.053)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=88)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=94)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

- **FILTRO** `streak_estiramiento` > `1.1202` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1202
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=32)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=797)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=803)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=452)

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
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=678)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1248)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=832)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=810)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3135)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1585)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1593)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.197 (n=611)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0043 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.229 (n=611)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.201 (n=806)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.190)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2159` → IC=+0.194 (n=610)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.2159 (IC base=+0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1268` → IC=+0.235 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1268 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=1711)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.192 (n=1909)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.269 (n=1832)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.1201` → IC=+0.190 (n=929)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1201 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.771` → IC=+0.276 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.771 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `8758.4418` → IC=+0.202 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8758.4418 (IC base=+0.190)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=769)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.223 (n=410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0602` → IC=+0.284 (n=137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0602 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `0.3844` → IC=+0.212 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3844 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.241 (n=137)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4004` → IC=+0.247 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4004 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.7112` → IC=+0.277 (n=410)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7112 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.277 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.280 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `16049.3542` → IC=+0.241 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16049.3542 (IC base=+0.212)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.180 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0035 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.141 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.005 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.158 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.178 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.137 (n=433)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 16.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.6586` → IC=+0.258 (n=386)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6586 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.147 (n=341)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.386` → IC=+0.224 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.386 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4165.118` → IC=+0.141 (n=288)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 4165.118 (IC base=+0.133)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=127)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.287 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.1498` → IC=+0.200 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1498 (IC base=+0.177)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0713` → IC=+0.189 (n=194)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.0713 (IC base=+0.177)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.224 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.192 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.258 (n=217)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1256` → IC=+0.180 (n=123)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1256 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.181 (n=211)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `3071.8702` → IC=+0.262 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3071.8702 (IC base=+0.177)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.688` → IC=-0.157 (n=103)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.688
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=1161)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.936` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.936 (IC base=-0.006)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.280 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.224 (n=208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.197)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0404` → IC=+0.200 (n=471)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0404 (IC base=+0.197)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0883` → IC=+0.264 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0883 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.231 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.286 (n=471)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.3623` → IC=+0.209 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3623 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.188` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.188 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.799` → IC=+0.199 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.799 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `2910.1242` → IC=+0.274 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2910.1242 (IC base=+0.197)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.148 (n=530)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` < 0.1176 (IC base=+0.053)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.359 (n=304)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.352)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.377 (n=152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.352)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.353 (n=304)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.352)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.375 (n=303)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.352)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.391 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.352)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.371 (n=465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.352)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.391 (n=456)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.352)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.393 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.352)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.360 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.352)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.954` → IC=+0.354 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.954 (IC base=+0.352)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.355 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.352)

- **PATRÓN** `libro_liquidez` > `3425.1488` → IC=+0.365 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3425.1488 (IC base=+0.352)

- **PATRÓN** `ballena_activa_n` < `457.0` → IC=+0.373 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 457.0 (IC base=+0.352)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1164` → IC=+0.358 (n=111)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1164 (IC base=+0.358)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.366 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.384 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.372 (n=84)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.358)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.367 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0739` → IC=+0.366 (n=251)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0739 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1284` → IC=+0.398 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1284 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.383 (n=255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.390 (n=252)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.364 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.360 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `11137.3038` → IC=+0.377 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11137.3038 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `568.0` → IC=+0.402 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 568.0 (IC base=+0.358)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.384 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.343)

- **PATRÓN** `drift_60min` |x|≤ `0.1039` → IC=+0.349 (n=137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1039 (IC base=+0.343)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.365 (n=183)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.343)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.373 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.407 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.343)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.393 (n=204)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.343)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.381 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.343)

- **PATRÓN** `dist_vwap_pct` < `0.1212` → IC=+0.345 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1212 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.353 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.349 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.343)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.343)

- **PATRÓN** `libro_liquidez` > `3465.3078` → IC=+0.355 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3465.3078 (IC base=+0.343)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.352 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=+0.343)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `libro_spread` > `0.01` → IC=-0.205 (n=994)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1893)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1363` → IC=+0.248 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1363 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6423` → IC=+0.273 (n=697)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6423 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.190 (n=562)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.122` → IC=+0.250 (n=1370)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.122 (IC base=-0.028)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1809` → IC=+0.244 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1809 (IC base=-0.028)

- **PATRÓN** `ibs_15` < `0.3514` → IC=+0.274 (n=2054)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3514 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.6856` → IC=+0.300 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6856 (IC base=-0.028)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0472` → IC=-0.217 (n=1180)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0472
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=582)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.229 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1322)

- **FILTRO** `sigma_ewma_delta_pct` > `19.563` → IC=-0.256 (n=313)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.563
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1449)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.157 (n=170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0028 (IC base=+0.082)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.277 (n=92)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.082)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.336 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.082)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.120 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 12.0 (IC base=+0.082)

- **PATRÓN** `ibs_15` > `0.7497` → IC=+0.324 (n=203)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7497 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1351` → IC=+0.290 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1351 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.354` → IC=+0.270 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.354 (IC base=+0.082)

- **PATRÓN** `ibs_15` < `0.199` → IC=+0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.199 (IC base=-0.198)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.198)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=425)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.150 (n=332)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0068 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.166 (n=297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0041 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.216 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.146)

- **PATRÓN** `drift_15min` |x|≤ `0.4178` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `drift_15min` |x|≤ 0.4178 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.228 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.174 (n=240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.6642` → IC=+0.261 (n=332)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6642 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.149 (n=95)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1047` → IC=+0.176 (n=236)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1047 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.009` → IC=+0.146 (n=286)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 9.009 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=425)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `10911.5134` → IC=+0.173 (n=151)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 10911.5134 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.249 (n=802)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.4431` → IC=+0.238 (n=802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4431 (IC base=+0.233)

- **PATRÓN** `drift_15min` |x|≤ `0.4752` → IC=+0.258 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4752 (IC base=+0.233)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2077` → IC=+0.254 (n=364)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2077 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.243 (n=309)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.233)

- **PATRÓN** `ibs_15` < `0.2756` → IC=+0.278 (n=705)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2756 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.7529` → IC=+0.319 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7529 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.868` → IC=+0.259 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.868 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.366` → IC=+0.238 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.366 (IC base=+0.233)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.225 (n=231)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=451)

- **FILTRO** `drift_15min` |x|> `0.8935` → IC=-0.267 (n=170)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8935
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=512)

- **FILTRO** `sigma_ewma_delta_pct` > `18.173` → IC=-0.138 (n=363)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.173
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2935)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.192 (n=50)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.5625 (IC base=-0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0777` → IC=+0.229 (n=315)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0777 (IC base=-0.041)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.261 (n=354)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7501` → IC=+0.240 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7501 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.1869` → IC=+0.224 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1869 (IC base=-0.041)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.230 (n=579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=244)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.264 (n=218)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=605)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1397` → IC=+0.302 (n=240)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1397 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1078` → IC=+0.336 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1078 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3391` → IC=+0.304 (n=530)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3391 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.9056` → IC=+0.346 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9056 (IC base=-0.039)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.306 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0563` → IC=+0.327 (n=247)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0563 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.306 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2224` → IC=+0.323 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2224 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.315 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8408` → IC=+0.330 (n=738)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8408 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.340 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.352 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12879.5491` → IC=+0.301 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12879.5491 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.297 (n=357)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.341 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.288)

- **PATRÓN** `drift_15min` |x|≤ `0.4216` → IC=+0.290 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4216 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2603` → IC=+0.310 (n=135)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2603 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.313 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.318 (n=405)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.4113` → IC=+0.362 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4113 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.101` → IC=+0.371 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.101 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.332 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.307 (n=294)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.1119` → IC=+0.304 (n=223)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1119 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1481` → IC=+0.299 (n=222)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1481 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.330 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.875` → IC=+0.357 (n=298)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.875 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.6145` → IC=+0.310 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6145 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.463` → IC=+0.333 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.463 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.296)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.162 (n=72)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=220)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.138 (n=194)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=66)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.167 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=337)

- **FILTRO** `ballena_activa_n` > `56.0` → IC=-0.208 (n=46)

  - _Acción_: SKIP cuando `ballena_activa_n` > 56.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=142)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0687` → IC=-0.139 (n=59)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0687
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=115)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1259` → IC=-0.167 (n=43)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1259
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=131)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1819` → IC=-0.260 (n=23)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1819
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

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

- **FILTRO** `drift_15min` |x|> `0.1655` → IC=-0.241 (n=25)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1655
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

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
- **PATRÓN** `T_h` > `79.3918` → IC=+0.218 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.3918 (IC base=+0.203)

- **PATRÓN** `ratio` < `0.9775` → IC=+0.468 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.203)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.331)

- **PATRÓN** `ratio` > `1.0094` → IC=+0.291 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0094 (IC base=+0.331)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.4188` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.4188 (IC base=+0.183)

- **PATRÓN** `ratio` < `0.973` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.183)

- **PATRÓN** `T_h` < `111.9965` → IC=+0.290 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9965 (IC base=+0.282)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.292 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.282)

- **PATRÓN** `ratio` > `1.0467` → IC=+0.367 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0467 (IC base=+0.282)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `81.6124` → IC=+0.266 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6124 (IC base=+0.240)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.420 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.240)

- **PATRÓN** `T_h` > `105.6124` → IC=+0.327 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 105.6124 (IC base=+0.311)

- **PATRÓN** `ratio` > `1.0131` → IC=+0.330 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0131 (IC base=+0.311)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1332` → IC=+0.459 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1332 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.190 a +0.269 en UPDOWN_GBM#15min (n=1832). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7112 sube el IC de +0.212 a +0.277 en UPDOWN_GBM#BTC#15min (n=410). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6586 sube el IC de +0.133 a +0.258 en UPDOWN_GBM#ETH#15min (n=386). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.177 a +0.258 en UPDOWN_GBM#SOL#15min (n=217). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.197 a +0.286 en UPDOWN_GBM#XRP#15min (n=471). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6423 sube el IC de -0.066 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=697). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3514 sube el IC de -0.028 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=2054). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7497 sube el IC de +0.082 a +0.324 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=203). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.199 sube el IC de -0.198 a +0.382 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6642 sube el IC de +0.146 a +0.261 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=332). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2756 sube el IC de +0.233 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=705). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.172 a +0.192 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=50). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.041 a +0.261 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=354). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3391 sube el IC de -0.039 a +0.304 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=530). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8408 sube el IC de +0.292 a +0.330 en UPDOWN_GBM_IBS_ALTO (n=738). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.288 a +0.318 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=405). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.875 sube el IC de +0.296 a +0.357 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=298). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.352 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=456). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.358 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=252). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.343 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=204). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1411 | +0.100 | +202.64€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1411 | +0.100 | +202.64€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1065 | +0.109 | +173.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1065 | +0.109 | +173.78€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 30416 | -0.084 | -4033.78€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1590 | -0.026 | -213.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 28826 | -0.087 | -3819.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3929 | -0.098 | -643.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3929 | -0.098 | -643.91€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1590 | -0.026 | -213.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1590 | -0.026 | -213.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3583 | -0.099 | -806.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3583 | -0.099 | -806.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7906 | -0.016 | -767.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7906 | -0.016 | -767.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7429 | -0.090 | -466.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7429 | -0.090 | -466.66€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5979 | -0.165 | -1135.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5979 | -0.165 | -1135.88€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 21285 | -0.024 | +3838.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5515 | +0.001 | +1783.64€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 15770 | -0.033 | +2055.17€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 21285 | -0.024 | +3838.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5515 | +0.001 | +1783.64€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 15770 | -0.033 | +2055.17€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO | 1486 | -0.102 | -190.28€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#15min | 176 | -0.045 | -19.67€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#5min | 1310 | -0.110 | -170.61€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BNB#5min | 22 | -0.083 | +4.56€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC | 788 | -0.089 | -95.94€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#15min | 152 | -0.039 | -14.45€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#BTC#5min | 636 | -0.100 | -81.50€ | 2 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH | 491 | -0.125 | -74.32€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#15min | 24 | -0.077 | -5.22€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#ETH#5min | 467 | -0.127 | -69.10€ | 3 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#SOL#5min | 119 | -0.045 | -14.09€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ CANDIDATA9_BOT_CONSENSO#XRP#5min | 66 | -0.191 | -10.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 102496 | +0.112 | -5023.97€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14999 | +0.185 | -451.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 423 | -0.067 | -55.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 80553 | +0.100 | -4282.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6521 | +0.106 | -235.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 13387 | +0.100 | -1047.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 48 | -0.160 | +1.58€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 13324 | +0.102 | -1037.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 20592 | +0.131 | -371.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4667 | +0.201 | -125.63€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 13359 | +0.113 | -185.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2524 | +0.098 | -38.11€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13428 | +0.090 | -1206.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 55 | -0.114 | -9.21€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 13358 | +0.091 | -1186.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 21765 | +0.124 | -410.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5886 | +0.177 | -73.06€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13504 | +0.105 | -268.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2363 | +0.100 | -60.45€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 19924 | +0.113 | -1180.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4294 | +0.187 | -254.58€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 326 | -0.027 | -1.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13670 | +0.091 | -787.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1634 | +0.129 | -136.79€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13400 | +0.099 | -807.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 49 | -0.029 | +9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 13338 | +0.100 | -816.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 16286 | +0.194 | -1023.10€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 16286 | +0.194 | -1023.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3836 | +0.168 | -396.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3836 | +0.168 | -396.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1538 | +0.206 | -2.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1538 | +0.206 | -2.12€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3780 | +0.181 | -311.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3780 | +0.181 | -311.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3335 | +0.243 | -99.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3335 | +0.243 | -99.80€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3718 | +0.191 | -226.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3718 | +0.191 | -226.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 765 | +0.430 | -21.75€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 765 | +0.430 | -21.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 297 | +0.440 | -1.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 297 | +0.440 | -1.66€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 291 | +0.428 | -8.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 291 | +0.428 | -8.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 165 | +0.410 | -9.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 165 | +0.410 | -9.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 56362 | +0.198 | -4368.16€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 56362 | +0.198 | -4368.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9712 | +0.178 | -1100.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9712 | +0.178 | -1100.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9026 | +0.222 | -341.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9026 | +0.222 | -341.47€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9729 | +0.174 | -1126.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9729 | +0.174 | -1126.01€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9115 | +0.218 | -371.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9115 | +0.218 | -371.52€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9327 | +0.203 | -612.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9327 | +0.203 | -612.26€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9453 | +0.193 | -816.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9453 | +0.193 | -816.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 21348 | +0.116 | +136.65€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 21348 | +0.116 | +136.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10601 | +0.119 | +113.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10601 | +0.119 | +113.74€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10747 | +0.113 | +22.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10747 | +0.113 | +22.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1594 | +0.288 | -25.38€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1594 | +0.288 | -25.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 711 | +0.278 | -18.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 711 | +0.278 | -18.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 769 | +0.287 | -10.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 769 | +0.287 | -10.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 114 | +0.345 | +3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 114 | +0.345 | +3.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 707 | +0.435 | -4.98€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 707 | +0.435 | -4.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 338 | +0.432 | -4.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 338 | +0.432 | -4.84€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 324 | +0.439 | -0.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 324 | +0.439 | -0.54€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1218 | +0.068 | -61.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 431 | +0.052 | -39.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 787 | +0.077 | -21.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 959 | +0.075 | -29.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 172 | +0.069 | -7.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 787 | +0.077 | -21.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 195 | +0.013 | -35.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 195 | +0.013 | -35.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 40220 | +0.098 | -1161.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3297 | +0.087 | +12.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 36923 | +0.099 | -1174.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 22452 | +0.102 | -344.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3297 | +0.087 | +12.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 19155 | +0.104 | -357.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7746 | +0.109 | -16.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7746 | +0.109 | -16.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10022 | +0.081 | -799.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10022 | +0.081 | -799.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 849 | +0.214 | -101.09€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 849 | +0.214 | -101.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 849 | +0.214 | -101.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 849 | +0.214 | -101.09€ | 2 | 4 |
| ✅ GBM_LATE_15M | 28499 | +0.085 | +13878.38€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 28499 | +0.085 | +13878.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4771 | +0.198 | +3559.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4771 | +0.198 | +3559.67€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 4245 | +0.179 | +3033.25€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4245 | +0.179 | +3033.25€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 5021 | +0.198 | +3739.80€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5021 | +0.198 | +3739.80€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4110 | +0.027 | +979.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4110 | +0.027 | +979.67€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4063 | -0.033 | +922.34€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4063 | -0.033 | +922.34€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6289 | -0.040 | +1643.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6289 | -0.040 | +1643.64€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 30371 | +0.086 | +16098.16€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 30371 | +0.086 | +16098.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5789 | +0.013 | +3043.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5789 | +0.013 | +3043.66€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6334 | +0.015 | +1353.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6334 | +0.015 | +1353.04€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4319 | +0.265 | +4397.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4319 | +0.265 | +4397.77€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5007 | +0.006 | +1012.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5007 | +0.006 | +1012.22€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4904 | +0.032 | +1941.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4904 | +0.032 | +1941.75€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4018 | +0.280 | +4349.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4018 | +0.280 | +4349.72€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 22890 | +0.170 | +17406.49€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 22890 | +0.170 | +17406.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3446 | +0.210 | +2788.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3446 | +0.210 | +2788.88€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3606 | +0.149 | +2656.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3606 | +0.149 | +2656.01€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3615 | +0.209 | +2893.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3615 | +0.209 | +2893.15€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3837 | +0.134 | +2731.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3837 | +0.134 | +2731.32€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4290 | +0.119 | +3076.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4290 | +0.119 | +3076.48€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4096 | +0.205 | +3260.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4096 | +0.205 | +3260.65€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6036 | +0.137 | +2797.32€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6036 | +0.137 | +2797.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1706 | +0.135 | +853.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1706 | +0.135 | +853.96€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1813 | +0.153 | +878.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1813 | +0.153 | +878.30€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1425 | +0.122 | +585.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1425 | +0.122 | +585.72€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 28697 | +0.178 | +21837.18€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 28697 | +0.178 | +21837.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4544 | +0.225 | +3911.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4544 | +0.225 | +3911.30€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4481 | +0.152 | +3004.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4481 | +0.152 | +3004.47€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4757 | +0.226 | +4097.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4757 | +0.226 | +4097.60€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4663 | +0.135 | +3233.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4663 | +0.135 | +3233.04€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5022 | +0.118 | +3376.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5022 | +0.118 | +3376.90€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5230 | +0.210 | +4213.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5230 | +0.210 | +4213.86€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8093 | +0.166 | +5183.49€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 8093 | +0.166 | +5183.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1843 | +0.152 | +1254.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1843 | +0.152 | +1254.17€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2629 | +0.169 | +1664.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2629 | +0.169 | +1664.15€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 842 | +0.152 | +464.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 842 | +0.152 | +464.49€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1982 | +0.070 | +756.72€ | 1 | 15 |
| ✅ GBM_LATE_60M#60min | 1982 | +0.070 | +756.72€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 731 | +0.092 | +275.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 731 | +0.092 | +275.28€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 648 | +0.072 | +302.19€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 648 | +0.072 | +302.19€ | 2 | 16 |
| ✅ GBM_LATE_60M#SOL | 603 | +0.039 | +179.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 603 | +0.039 | +179.25€ | 3 | 9 |
| 🚫 GBM_LATE_60M_FADE | 409 | -0.254 | -21.79€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 409 | -0.254 | -21.79€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 153 | -0.223 | -7.57€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 153 | -0.223 | -7.57€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 136 | -0.254 | -7.60€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 136 | -0.254 | -7.60€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 120 | -0.287 | -6.62€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 120 | -0.287 | -6.62€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 775 | +0.082 | +181.96€ | 1 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 775 | +0.082 | +181.96€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 304 | +0.072 | +63.69€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 304 | +0.072 | +63.69€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 234 | +0.047 | +18.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 234 | +0.047 | +18.86€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 237 | +0.128 | +99.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 237 | +0.128 | +99.41€ | 1 | 11 |
| ✅ LATE_WINDOW_5MIN | 107 | +0.262 | +91.86€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 107 | +0.262 | +91.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 107 | +0.262 | +91.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 107 | +0.262 | +91.86€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2273 | +0.104 | +620.89€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2273 | +0.104 | +620.89€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2273 | +0.104 | +620.89€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2273 | +0.104 | +620.89€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 400 | -0.075 | -33.13€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 400 | -0.075 | -33.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 103 | -0.043 | -3.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 103 | -0.043 | -3.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 148 | -0.027 | -5.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 148 | -0.027 | -5.06€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2243 | +0.012 | +32.96€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2243 | +0.012 | +32.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 119 | +0.021 | -2.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 119 | +0.021 | -2.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 271 | -0.002 | +12.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 271 | -0.002 | +12.23€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 176 | -0.022 | -5.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 176 | -0.022 | -5.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 922 | +0.023 | +22.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 922 | +0.023 | +22.12€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 516 | +0.012 | +0.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 516 | +0.012 | +0.70€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 239 | +0.010 | +5.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 239 | +0.010 | +5.74€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1198 | -0.043 | -26.03€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1198 | -0.043 | -26.03€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 340 | -0.041 | -12.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 340 | -0.041 | -12.76€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 406 | -0.027 | -0.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 406 | -0.027 | -0.86€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 452 | -0.057 | -12.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 452 | -0.057 | -12.40€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 2783 | -0.011 | +92.17€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1317 | -0.013 | +39.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1466 | -0.009 | +52.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 83 | +0.029 | +9.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 44 | +0.065 | +9.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 39 | -0.012 | -0.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 659 | +0.002 | +34.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 305 | +0.002 | +12.37€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 354 | +0.003 | +21.90€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 341 | -0.010 | +16.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 164 | -0.042 | -1.63€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 177 | +0.020 | +18.56€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 550 | -0.029 | -13.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 256 | -0.035 | -10.80€ | 4 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 294 | -0.024 | -2.55€ | 5 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 525 | -0.010 | +24.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 256 | -0.012 | +15.13€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 269 | -0.009 | +9.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 625 | -0.015 | +20.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 292 | -0.007 | +14.46€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 333 | -0.022 | +5.61€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 32623 | -0.006 | +1447.83€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 32623 | -0.006 | +1447.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5771 | +0.020 | +718.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5771 | +0.020 | +718.26€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4968 | -0.031 | -82.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4968 | -0.031 | -82.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5849 | +0.017 | +524.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5849 | +0.017 | +524.20€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4751 | -0.053 | -162.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4751 | -0.053 | -162.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5491 | -0.010 | +203.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5491 | -0.010 | +203.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5793 | +0.010 | +246.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5793 | +0.010 | +246.64€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE | 6026 | -0.061 | -155.55€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6026 | -0.061 | -155.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1452 | -0.086 | -44.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1452 | -0.086 | -44.18€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 685 | -0.124 | -31.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 685 | -0.124 | -31.62€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1774 | -0.079 | -35.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1774 | -0.079 | -35.53€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3347 | +0.004 | -3.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3347 | +0.004 | -3.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1317 | +0.006 | +6.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1317 | +0.006 | +6.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 82321 | -0.072 | +1763.63€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 82321 | -0.072 | +1763.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 14000 | -0.076 | +824.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 14000 | -0.076 | +824.47€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12601 | -0.095 | -639.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12601 | -0.095 | -639.32€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 14272 | -0.067 | +750.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 14272 | -0.067 | +750.66€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 12133 | -0.092 | -195.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 12133 | -0.092 | -195.65€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 15024 | -0.049 | +389.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 15024 | -0.049 | +389.49€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 14291 | -0.063 | +633.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 14291 | -0.063 | +633.97€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7829 | -0.028 | -142.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7829 | -0.028 | -142.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1794 | -0.036 | -13.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1794 | -0.036 | -13.17€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2213 | -0.025 | -32.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2213 | -0.025 | -32.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1064 | -0.045 | -20.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1064 | -0.045 | -20.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 759 | -0.022 | -24.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 759 | -0.022 | -24.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1232 | +0.109 | +423.78€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1096 | +0.116 | +411.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 247 | +0.131 | +116.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 247 | +0.131 | +116.42€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 211 | +0.110 | +61.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 211 | +0.110 | +61.57€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 229 | +0.102 | +81.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 229 | +0.102 | +81.85€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 190 | +0.130 | +86.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 190 | +0.130 | +86.41€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 219 | +0.102 | +64.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 219 | +0.102 | +64.94€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 644 | -0.043 | -49.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 644 | -0.043 | -49.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 129 | -0.004 | +3.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 129 | -0.004 | +3.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 89 | -0.071 | -11.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 89 | -0.071 | -11.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 188 | -0.063 | -24.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 188 | -0.063 | -24.80€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 131 | -0.019 | -4.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 131 | -0.019 | -4.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 107 | -0.060 | -12.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 107 | -0.060 | -12.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 621 | -0.110 | -54.39€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 284 | -0.161 | -66.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 231 | -0.200 | -67.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 53 | +0.009 | +0.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 216 | -0.073 | -0.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 166 | -0.077 | -6.90€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 50 | -0.058 | +6.23€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 121 | -0.053 | +12.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 97 | -0.076 | +6.36€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 24 | +0.038 | +6.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 494 | -0.135 | -67.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 127 | -0.012 | +13.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 781 | -0.200 | -33.26€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 325 | -0.197 | -28.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 284 | -0.196 | -28.79€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 41 | -0.198 | +0.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 266 | -0.216 | -24.23€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 231 | -0.225 | -29.32€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 35 | -0.149 | +5.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 190 | -0.177 | +19.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 174 | -0.176 | +14.88€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 689 | -0.202 | -43.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 92 | -0.181 | +9.98€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 327 | +0.406 | +244.64€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 33 | +0.071 | -3.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 33 | +0.071 | -3.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 81 | +0.380 | +59.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 81 | +0.380 | +59.35€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 213 | +0.463 | +188.71€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 213 | +0.463 | +188.71€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 327 | +0.406 | +244.64€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 561 | +0.031 | +15.69€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 561 | +0.031 | +15.69€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 272 | +0.029 | +3.54€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 272 | +0.029 | +3.54€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 59 | -0.008 | -1.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 59 | -0.008 | -1.62€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 193 | +0.033 | +10.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 193 | +0.033 | +10.59€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2932 | -0.021 | -116.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2932 | -0.021 | -116.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 894 | -0.020 | -30.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 894 | -0.020 | -30.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 573 | -0.024 | -23.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 573 | -0.024 | -23.73€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1309 | -0.019 | -47.98€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1309 | -0.019 | -47.98€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 77 | -0.044 | -5.84€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 77 | -0.044 | -5.84€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8661 | +0.023 | +127.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8661 | +0.023 | +127.06€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2381 | +0.025 | +34.05€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2381 | +0.025 | +34.05€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1959 | +0.032 | +52.02€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1959 | +0.032 | +52.02€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2637 | +0.013 | +8.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2637 | +0.013 | +8.09€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1684 | +0.024 | +32.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1684 | +0.024 | +32.90€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7889 | +0.013 | -40.42€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7889 | +0.013 | -40.42€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3154 | +0.016 | -8.91€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3154 | +0.016 | -8.91€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3118 | +0.012 | -20.28€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3118 | +0.012 | -20.28€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1617 | +0.008 | -11.23€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1617 | +0.008 | -11.23€ | 2 | 0 |
| ✅ UPDOWN_GBM | 43997 | +0.035 | +2854.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11469 | +0.071 | +2164.31€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1568 | +0.004 | +7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 28123 | +0.027 | +658.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2673 | +0.002 | +24.56€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4426 | +0.075 | +542.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 795 | +0.161 | +345.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3598 | +0.057 | +197.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 8456 | +0.043 | +632.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1497 | +0.086 | +338.94€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 422 | +0.014 | +5.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5265 | +0.043 | +256.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1210 | +0.003 | +30.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 62 | -0.094 | +0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5066 | +0.042 | +321.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 752 | +0.137 | +261.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4286 | +0.025 | +61.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 9646 | +0.025 | +415.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2925 | +0.049 | +335.72€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 414 | +0.007 | +7.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5348 | +0.018 | +76.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 905 | -0.001 | -7.91€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 54 | -0.125 | +3.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 10014 | +0.016 | +273.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2766 | +0.027 | +196.01€ | 0 | 10 |
| ✅ UPDOWN_GBM#SOL#240min | 405 | -0.004 | -0.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6239 | +0.015 | +79.48€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 558 | +0.005 | +2.27€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 46 | -0.167 | -3.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6387 | +0.040 | +671.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2734 | +0.086 | +686.45€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 266 | +0.000 | -2.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3387 | +0.005 | -12.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 162 | -0.128 | +0.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 607 | +0.352 | +205.17€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 607 | +0.352 | +205.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 335 | +0.358 | +111.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 335 | +0.358 | +111.92€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 272 | +0.343 | +93.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 272 | +0.343 | +93.25€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 13241 | -0.036 | +2883.46€ | 1 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 13241 | -0.036 | +2883.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 896 | -0.046 | +379.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 896 | -0.046 | +379.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2439 | -0.121 | +29.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2439 | -0.121 | +29.89€ | 3 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 474 | +0.187 | +330.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 474 | +0.187 | +330.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1510 | +0.208 | +926.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1510 | +0.208 | +926.03€ | 1 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3980 | -0.064 | +581.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3980 | -0.064 | +581.22€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3942 | -0.074 | +635.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3942 | -0.074 | +635.98€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 156 | +0.038 | +7.79€ | 1 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 156 | +0.038 | +7.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 156 | +0.038 | +7.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 156 | +0.038 | +7.79€ | 1 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 984 | +0.292 | +790.15€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 984 | +0.292 | +790.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 540 | +0.288 | +411.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 540 | +0.288 | +411.38€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 444 | +0.296 | +378.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 444 | +0.296 | +378.77€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 741 | -0.112 | -84.77€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 741 | -0.112 | -84.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 220 | -0.081 | -16.26€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 220 | -0.081 | -16.26€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 2 | 0 |
| 🚫 UPDOWN_OU_5M#SOL | 72 | -0.203 | -9.13€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#SOL#5min | 72 | -0.203 | -9.13€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2597 | +0.300 | +1268.48€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 911 | +0.251 | +127.47€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 981 | +0.289 | +414.37€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 705 | +0.377 | +726.64€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.057) — sin ventaja clara. oversold(IBS<0.3): IC=+0.048 n=15493 | neutral: IC=+0.034 n=16340 | overbought(IBS>0.7): IC=+0.090 n=15823
  - _Datos_: n=49346 IC=+0.058 PNL=+6209.96€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 569 celda(s) pasan gate riguroso completo de 2325 evaluadas (n>=40) y 3295 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.027 < 0.08 — monitorear
  - _Datos_: n=2766 IC=+0.027 PNL=+196.01€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=981/15 IC=+0.289 PNL=+414.37€ | BTC: n=911/15 IC=+0.251 PNL=+127.47€ | SOL: n=705/15 IC=+0.377 PNL=+726.64€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 30 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: 43935 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.126 n=396/60 | contraria IC=+0.173 n=368 | gap=-0.047 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=328, boost estimado=+0.010. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 190 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=905/40 IC=-0.001 PNL=-7.91€ | BTC#60min: n=1210/40 IC=+0.003 PNL=+30.19€ | SOL#60min: n=558/40 IC=+0.005 PNL=+2.27€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=375489 | tras_1loss IC=+0.083 n=290302 | tras_2loss IC=+0.053 n=121050/40 | gap=-0.003 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.017 n=5297 | contrario_BTC IC=+0.032 n=4697/40 | gap=+0.014 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.198 > 0.08 con n=379 PNL=+258.93€
  - _Datos_: n=379 IC=+0.198 PNL=+258.93€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.214 > 0.08 con n=431 PNL=+323.62€
  - _Datos_: n=431 IC=+0.214 PNL=+323.62€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.245 > 0.08 con n=45 PNL=+34.88€
  - _Datos_: n=45 IC=+0.245 PNL=+34.88€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.327 > 0.1 con n=2123 PNL=+1155.66€
  - _Datos_: n=2123 IC=+0.327 PNL=+1155.66€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=343 IC=+0.059 PNL=+32.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=343 IC=+0.059 PNL=+32.76€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=57 IC=+0.178 PNL=+35.97€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=57 IC=+0.178 PNL=+35.97€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=42089 IC=+0.035 PNL=+2721.49€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=42089 IC=+0.035 PNL=+2721.49€

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
  - _Estado_: n=1850 IC=+0.008 PNL=+2.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1850 IC=+0.008 PNL=+2.60€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=823 IC=-0.009 PNL=+21.96€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=823 IC=-0.009 PNL=+21.96€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=558 IC=+0.027 PNL=+30.78€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=558 IC=+0.027 PNL=+30.78€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.190 > 0.1 con n=2441 PNL=+1573.69€
  - _Datos_: n=2441 IC=+0.190 PNL=+1573.69€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1380 IC=+0.054 PNL=+102.23€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1380 IC=+0.054 PNL=+102.23€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1497 IC=+0.086 PNL=+338.94€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1497 IC=+0.086 PNL=+338.94€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=6546 PNL=+1601.68€
  - _Datos_: n=6546 IC=+0.087 PNL=+1601.68€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=181 IC=-0.254 PNL=-7.72€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=181 IC=-0.254 PNL=-7.72€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=295 IC=-0.035 PNL=-1.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=295 IC=-0.035 PNL=-1.44€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=617 IC=+0.025 PNL=+45.37€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=617 IC=+0.025 PNL=+45.37€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=65 IC=+0.052 PNL=+3.92€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=65 IC=+0.052 PNL=+3.92€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6184 IC=-0.001 PNL=+1.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6184 IC=-0.001 PNL=+1.12€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.08 con n=68 PNL=+18.45€
  - _Datos_: n=68 IC=+0.171 PNL=+18.45€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.262 n=107) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=107 IC=+0.262 PNL=+91.86€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=8140 IC=+0.038 PNL=+520.96€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=8140 IC=+0.038 PNL=+520.96€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2744 IC=+0.055 PNL=+334.69€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2744 IC=+0.055 PNL=+334.69€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=395 PNL=+122.72€
  - _Datos_: n=395 IC=+0.112 PNL=+122.72€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.149 > 0.08 con n=690 PNL=+181.75€
  - _Datos_: n=690 IC=+0.149 PNL=+181.75€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.110 > 0.08 con n=519 PNL=+248.10€
  - _Datos_: n=519 IC=+0.110 PNL=+248.10€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=63614 IC=+0.118 PNL=+23696.38€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=63614 IC=+0.118 PNL=+23696.38€

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
  - _Estado_: n=6595 IC=+0.041 PNL=+512.83€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6595 IC=+0.041 PNL=+512.83€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.117 > 0.02 con n=703 PNL=+259.88€
  - _Datos_: n=703 IC=+0.117 PNL=+259.88€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=156 IC=-0.063 PNL=+31.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=156 IC=-0.063 PNL=+31.89€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.448 > 0.1 con n=1216 PNL=+1196.09€
  - _Datos_: n=1216 IC=+0.448 PNL=+1196.09€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=15967 IC=+0.057 PNL=+1949.78€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=15967 IC=+0.057 PNL=+1949.78€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.1 con n=3974 PNL=+2186.41€
  - _Datos_: n=3974 IC=+0.203 PNL=+2186.41€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.151 < -0.1 con n=267 PNL=+27.69€
  - _Datos_: n=267 IC=-0.151 PNL=+27.69€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2106 IC=+0.053 PNL=+223.46€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2106 IC=+0.053 PNL=+223.46€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=89 IC=-0.115 PNL=+3.54€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=89 IC=-0.115 PNL=+3.54€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.1 con n=488 PNL=+136.72€
  - _Datos_: n=488 IC=+0.120 PNL=+136.72€

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
  - _Estado_: n=20376 IC=-0.136 PNL=+1457.01€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=20376 IC=-0.136 PNL=+1457.01€

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
  - _Estado_: n=2148 IC=+0.138 PNL=+1206.13€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2148 IC=+0.138 PNL=+1206.13€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.191 > 0.08 con n=2402 PNL=+1561.05€
  - _Datos_: n=2402 IC=+0.191 PNL=+1561.05€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=4683 IC=+0.026 PNL=+200.09€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4683 IC=+0.026 PNL=+200.09€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=2327 PNL=+1232.12€
  - _Datos_: n=2327 IC=+0.087 PNL=+1232.12€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.08 con n=545 PNL=+283.66€
  - _Datos_: n=545 IC=+0.211 PNL=+283.66€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.234 < -0.1 con n=2014 PNL=-194.03€
  - _Datos_: n=2014 IC=-0.234 PNL=-194.03€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=5991 IC=+0.176 PNL=+4124.49€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=5991 IC=+0.176 PNL=+4124.49€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=81 PNL=+29.26€
  - _Datos_: n=81 IC=+0.102 PNL=+29.26€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2180 IC=+0.068 PNL=+658.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2180 IC=+0.068 PNL=+658.43€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.181 > 0.08 con n=1990 PNL=+1414.62€
  - _Datos_: n=1990 IC=+0.181 PNL=+1414.62€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3304 IC=-0.032 PNL=+856.63€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3304 IC=-0.032 PNL=+856.63€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=586 PNL=-52.48€
  - _Datos_: n=586 IC=+0.087 PNL=-52.48€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.236 > 0.08 con n=3572 PNL=-322.75€
  - _Datos_: n=3572 IC=+0.236 PNL=-322.75€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=40 IC=+0.000 PNL=+5.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=40 IC=+0.000 PNL=+5.94€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1155) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1155 IC=+0.102 PNL=+275.58€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.337 > 0.08 con n=298 PNL=+106.37€
  - _Datos_: n=298 IC=+0.337 PNL=+106.37€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=454) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=454 IC=+0.410 PNL=+639.66€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=9712 IC=+0.178 PNL=-1100.68€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=9712 IC=+0.178 PNL=-1100.68€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.197 > 0.1 con n=153 PNL=+90.03€
  - _Datos_: n=153 IC=+0.197 PNL=+90.03€
