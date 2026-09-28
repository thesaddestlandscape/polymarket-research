# Hipótesis automáticas — 2026-09-28 02:16 UTC
_Generado por shadow_postmortem.py sobre 644125 resoluciones (PNL=+74900.79€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=524)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.235 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.212 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.8035` → IC=+0.252 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8035 (IC base=+0.139)

- **PATRÓN** `banda_z` > `4.143` → IC=+0.165 (n=559)

  - _Acción_: Kelly boost +0.82€ cuando `banda_z` > 4.143 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.156 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=598)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4878.272` → IC=+0.161 (n=187)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4878.272 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=524)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.056)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=389)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.237 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.147)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.211 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.147)

- **PATRÓN** `banda_hit_calibrado` > `0.7991` → IC=+0.265 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7991 (IC base=+0.147)

- **PATRÓN** `banda_z` > `4.334` → IC=+0.170 (n=450)

  - _Acción_: Kelly boost +0.85€ cuando `banda_z` > 4.334 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.168 (n=323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=509)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.165 (n=153)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 94.0 (IC base=+0.060)

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
- **FILTRO** `restante_s_al_confirmar` < `146.18` → IC=-0.216 (n=7434)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 146.18
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=22308)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `138.36` → IC=-0.245 (n=968)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 138.36
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=2905)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `125.51` → IC=-0.308 (n=878)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.51
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2636)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.68` → IC=-0.202 (n=1817)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.68
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=5454)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.39` → IC=-0.336 (n=1459)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.39
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=4379)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.207 (n=14584)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3638)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5620.5496` → IC=+0.177 (n=2329)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5620.5496 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=12307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.138 (n=14909)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 7.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.231 (n=11599)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.171 (n=5904)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7820.9566` → IC=+0.174 (n=2243)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 7820.9566 (IC base=+0.127)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1753)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=2213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `15920.3308` → IC=+0.236 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15920.3308 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.203 (n=1589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.206 (n=1768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.262 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=2262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `15854.5779` → IC=+0.213 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15854.5779 (IC base=+0.200)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.62` → IC=+0.175 (n=340)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.62 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.145 (n=240)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.101)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.143 (n=856)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5754.4405` → IC=+0.167 (n=226)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5754.4405 (IC base=+0.101)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=2981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.345 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.365 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.235 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.232)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.136 (n=633)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 15.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.248 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=574)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1311.0387` → IC=+0.146 (n=702)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1311.0387 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.81` → IC=+0.404 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.81 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.158 (n=574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.165 (n=612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 7.0 (IC base=+0.156)

- **PATRÓN** `py_entrada` < `0.315` → IC=+0.295 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.315 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=750)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.156)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.165)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.369 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `1244.5613` → IC=+0.152 (n=231)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1244.5613 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.209 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.117)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.76` → IC=-0.289 (n=131)

  - _Acción_: SKIP cuando `py_entrada` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=65)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=12340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=11750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.227 (n=4017)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `5111.8837` → IC=+0.335 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5111.8837 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=2967)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.172 (n=2808)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 17.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=2817)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.167)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.250 (n=1010)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.250 (n=1050)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.343 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.243)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=2762)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2774)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=2364)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.251 (n=2567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.240)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.324 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.240)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=2715)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.198 (n=2113)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.71 (IC base=+0.193)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.435 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `11185.2288` → IC=+0.458 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11185.2288 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.445 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `14073.2838` → IC=+0.446 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14073.2838 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.444 (n=193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `3322.2122` → IC=+0.444 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3322.2122 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.412 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.409)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.411 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.409)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.424 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.409)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.409)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=36742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.236 (n=16318)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=6335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.183 (n=5058)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=6872)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=6604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=6558)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.263 (n=3756)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=6687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=6679)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=3329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.266 (n=2278)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=6090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=2446)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=6138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.252 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5583)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.124 (n=5188)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.17 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=5211)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=6834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.64` → IC=+0.139 (n=5166)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.64 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=2812)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.13` → IC=+0.125 (n=2576)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.13 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.94` → IC=+0.140 (n=2858)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.94 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.137 (n=2962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 6.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `3.3` → IC=+0.143 (n=2564)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 3.3 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=2771)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.126 (n=2610)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.2 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=2892)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.138 (n=2602)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=836)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `4106.4567` → IC=+0.304 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4106.4567 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.288 (n=550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.329 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `4254.8679` → IC=+0.295 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4254.8679 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.325 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.294 (n=586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1723.1828` → IC=+0.314 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1723.1828 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.350 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.344)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.344)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.385 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.344)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.344)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.372 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.344)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.438 (n=468)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.433 (n=460)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.434 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.435 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.433 (n=253)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.433 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.454 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.444 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.436 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.437 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `1978.5089` → IC=+0.464 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.5089 (IC base=+0.437)

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
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=57)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=57)

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
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=57)

- **FILTRO** `py_entrada` > `0.785` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.785
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=57)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4857` → IC=+0.126 (n=8698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.4857 (IC base=+0.108)

- **PATRÓN** `ibs_20min` > `0.9822` → IC=+0.243 (n=2899)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9822 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` < `0.2184` → IC=+0.257 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2184 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.343` → IC=+0.189 (n=2305)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 8.343 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` < `1.2103` → IC=+0.251 (n=2392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2103 (IC base=+0.108)

- **PATRÓN** `volumen_regimen` > `0.6157` → IC=+0.254 (n=2392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6157 (IC base=+0.108)

- **PATRÓN** `volumen_pendiente_norm` > `0.3033` → IC=+0.228 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3033 (IC base=+0.108)

- **PATRÓN** `volumen_spike_ratio` > `1.9013` → IC=+0.212 (n=4009)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.9013 (IC base=+0.108)

- **PATRÓN** `ibs_20min` < `0.5708` → IC=+0.134 (n=10508)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5708 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.5985` → IC=+0.205 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5985 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.6986` → IC=+0.188 (n=1643)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6986 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `0.8696` → IC=+0.177 (n=2487)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8696 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1674` → IC=+0.227 (n=1788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1674 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.5706` → IC=+0.202 (n=5648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5706 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.214 (n=6118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 129.0 (IC base=+0.067)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.196 (n=659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0049 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.174 (n=649)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0081 (IC base=+0.167)

- **PATRÓN** `drift_60min` |x|≤ `0.3476` → IC=+0.173 (n=1948)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.3476 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.178 (n=942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.172 (n=1307)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 11.0 (IC base=+0.167)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.167)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.138` → IC=+0.269 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.138 (IC base=+0.167)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.212 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.167)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.170 (n=1829)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.181 (n=1981)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.167)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.247 (n=1340)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0878` → IC=+0.275 (n=500)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0878 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.249 (n=1033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.290 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.526` → IC=+0.244 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.526 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.468` → IC=+0.245 (n=1569)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.468 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0922` → IC=+0.234 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0922 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2782` → IC=+0.270 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2782 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4333` → IC=+0.234 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4333 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6113` → IC=+0.249 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6113 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1820.3192` → IC=+0.237 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1820.3192 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.239 (n=665)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1107` → IC=+0.242 (n=665)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1107 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=1587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.221 (n=1533)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.9861` → IC=+0.269 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9861 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.3443` → IC=+0.223 (n=1409)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3443 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.529` → IC=+0.267 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.529 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.2573` → IC=+0.222 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2573 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `1.0851` → IC=+0.228 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0851 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.248 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.3849` → IC=+0.234 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3849 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `11105.4969` → IC=+0.223 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11105.4969 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.179 (n=521)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0026 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.167 (n=518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.334` → IC=+0.193 (n=1036)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.334 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1271` → IC=+0.154 (n=1392)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1271 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.323` → IC=+0.153 (n=246)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.323 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.323` → IC=+0.145 (n=1423)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.323 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2085` → IC=+0.151 (n=1554)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.2085 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.856` → IC=+0.141 (n=1036)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.856 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1567` → IC=+0.176 (n=412)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1567 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.153 (n=1444)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7746` → IC=+0.147 (n=962)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7746 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `14064.3418` → IC=+0.146 (n=1036)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 14064.3418 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.168 (n=601)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 233.0 (IC base=+0.140)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.213 (n=649)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=2044)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1738)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.268` → IC=+0.258 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.268 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.190 (n=1694)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.3557` → IC=+0.202 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3557 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.7723` → IC=+0.196 (n=1657)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7723 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.194 (n=2313)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.223 (n=1482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.6123` → IC=+0.215 (n=1684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6123 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.241 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.707` → IC=+0.235 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.707 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.506` → IC=+0.212 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.506 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.264 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7564` → IC=+0.209 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7564 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.1766` → IC=+0.217 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1766 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1981.9661` → IC=+0.212 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.9661 (IC base=+0.212)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.214 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.212)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=105)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=2359)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.147 (n=380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0037 (IC base=+0.031)

- **PATRÓN** `ibs_20min` > `0.9471` → IC=+0.217 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9471 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.3549` → IC=+0.328 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3549 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.1947` → IC=+0.330 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1947 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.805` → IC=+0.168 (n=770)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 4.805 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.8627` → IC=+0.337 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8627 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.339 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.350 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.358 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.21` → IC=+0.333 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.21 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.333 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 157.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.1044` → IC=+0.151 (n=617)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1044 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.661` → IC=+0.209 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.661 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.158 (n=615)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8521 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1621` → IC=+0.148 (n=308)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.1621 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2304` → IC=+0.219 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2304 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.5312` → IC=+0.170 (n=776)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.5312 (IC base=+0.020)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.182 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=356)

- **FILTRO** `ibs_20min` < `0.2941` → IC=-0.201 (n=105)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=315)

- **FILTRO** `ibs_20min` > `0.25` → IC=-0.126 (n=2340)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=1178)

- **FILTRO** `sigma_ewma_delta_pct` > `8.716` → IC=-0.215 (n=373)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.716
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=3145)

- **PATRÓN** `ibs_20min` > `0.7834` → IC=+0.224 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7834 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `1.8814` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.8814 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.5572` → IC=+0.277 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5572 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.266` → IC=+0.128 (n=151)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 2.266 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `1.0815` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0815 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.5152` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5152 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.291 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.25` → IC=+0.124 (n=1178)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.25 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7235` → IC=+0.265 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7235 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.4545` → IC=+0.231 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4545 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `0.6732` → IC=+0.268 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6732 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.286 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.280 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6536` → IC=-0.182 (n=611)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6536
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1845)

- **FILTRO** `ibs_20min` < `0.72` → IC=-0.155 (n=1620)

  - _Acción_: SKIP cuando `ibs_20min` < 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=836)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.199 (n=497)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=1959)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.207 (n=899)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=2725)

- **PATRÓN** `dist_vwap_pct` > `0.4566` → IC=+0.315 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4566 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2821` → IC=+0.313 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2821 (IC base=-0.068)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.309 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=-0.068)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.299 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` < `2.1203` → IC=+0.297 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1203 (IC base=-0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.297 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.5572` → IC=+0.273 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5572 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` < `0.7337` → IC=+0.261 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7337 (IC base=-0.021)

- **PATRÓN** `volumen_regimen` > `1.2494` → IC=+0.281 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2494 (IC base=-0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.273 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.141` → IC=+0.265 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.141 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.5237` → IC=+0.252 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5237 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.198 (n=3687)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4748` → IC=+0.186 (n=9882)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4748 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `1.0319` → IC=+0.289 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0319 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.633` → IC=+0.158 (n=5143)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.633 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` > `0.691` → IC=+0.254 (n=3539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.691 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.272 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `1.4648` → IC=+0.240 (n=2142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4648 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` > `2.6649` → IC=+0.249 (n=2142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6649 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.272 (n=5950)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.098)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.161 (n=3633)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0091 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.5502` → IC=+0.153 (n=9580)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.5502 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.7053` → IC=+0.244 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7053 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.2458` → IC=+0.245 (n=3083)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2458 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `0.6348` → IC=+0.246 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6348 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.2051` → IC=+0.249 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2051 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.307 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.5993` → IC=+0.265 (n=1909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5993 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `2.2942` → IC=+0.263 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2942 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.272 (n=4212)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 83.0 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2567` → IC=-0.151 (n=763)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2567
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2292)

- **FILTRO** `sigma_ewma_delta_pct` > `4.525` → IC=-0.166 (n=581)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.525
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=1932)

- **PATRÓN** `ibs_20min` > `0.8947` → IC=+0.271 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8947 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.851` → IC=+0.207 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.851 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2226` → IC=+0.269 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2226 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.184 (n=327)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.189` → IC=+0.211 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.189 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.204 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.2144` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2144 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4082` → IC=+0.458 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4082 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.0785` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.0785 (IC base=-0.023)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.477 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=-0.023)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8668` → IC=+0.165 (n=741)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.8668 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.2962` → IC=+0.174 (n=397)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.2962 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.6758` → IC=+0.179 (n=916)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.6758 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2748` → IC=+0.248 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2748 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.191 (n=335)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4267 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.4088` → IC=+0.179 (n=335)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.4088 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `238.0` → IC=+0.199 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 238.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1497` → IC=+0.221 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1497 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.8583` → IC=+0.233 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8583 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2677` → IC=+0.310 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2677 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.222 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1651` → IC=+0.235 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1651 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `460.0` → IC=+0.221 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 460.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.292 (n=574)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.253 (n=1725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.249 (n=1734)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.742` → IC=+0.285 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.742 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.263 (n=1463)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `3.3191` → IC=+0.270 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3191 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2029)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `1914.6432` → IC=+0.259 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1914.6432 (IC base=+0.249)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.315 (n=636)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.6123` → IC=+0.287 (n=1399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6123 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.326 (n=476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.3456` → IC=+0.293 (n=1399)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3456 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.693` → IC=+0.299 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.693 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.3376` → IC=+0.301 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3376 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.7371` → IC=+0.290 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7371 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.6923` → IC=+0.293 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6923 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=903)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `1907.76` → IC=+0.302 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1907.76 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.283 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.284)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` < `0.3034` → IC=-0.163 (n=552)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3034
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1658)

- **FILTRO** `ibs_20min` > `0.7732` → IC=-0.182 (n=650)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7732
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=1954)

- **PATRÓN** `ibs_20min` > `0.912` → IC=+0.177 (n=553)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.912 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` < `0.1815` → IC=+0.226 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1815 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` < `0.9991` → IC=+0.242 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9991 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` > `0.5902` → IC=+0.221 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5902 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.263 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.5082` → IC=+0.265 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5082 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.271 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 69.0 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` > `0.1468` → IC=+0.217 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1468 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` < `0.64` → IC=+0.241 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.64 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `1.8148` → IC=+0.257 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8148 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `2.1389` → IC=+0.249 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1389 (IC base=-0.006)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.259 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7407` → IC=-0.194 (n=1173)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7407
  - _Potencial_: sin este filtro IC_bueno=+0.281 (n=1174)

- **FILTRO** `ibs_20min` > `0.6838` → IC=-0.235 (n=594)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6838
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=1786)

- **FILTRO** `sigma_ewma_delta_pct` > `4.728` → IC=-0.189 (n=519)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.728
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=1861)

- **PATRÓN** `ibs_20min` > `0.7407` → IC=+0.281 (n=1174)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7407 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.8477` → IC=+0.324 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8477 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.655` → IC=+0.169 (n=370)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.655 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.305 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `0.6422` → IC=+0.297 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6422 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1013` → IC=+0.297 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1013 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2708` → IC=+0.305 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2708 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4368` → IC=+0.322 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4368 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.319 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 55.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.5806` → IC=+0.124 (n=1571)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.5806 (IC base=+0.015)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.227 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.015)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.255 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6973 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` < `0.097` → IC=+0.219 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.097 (IC base=+0.015)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.224 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.015)

- **PATRÓN** `volumen_spike_ratio` < `2.46` → IC=+0.233 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.46 (IC base=+0.015)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.242 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 58.0 (IC base=+0.015)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0167` → IC=+0.316 (n=940)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0167 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.296 (n=661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.324 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7391 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.315 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.675` → IC=+0.303 (n=720)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.675 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.8619` → IC=+0.308 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8619 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.329 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `1.4333` → IC=+0.290 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4333 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.283 (n=1470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2468.3035` → IC=+0.290 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2468.3035 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.321 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0155` → IC=+0.307 (n=1004)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0155 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.1984` → IC=+0.281 (n=663)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1984 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.289 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.282 (n=747)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.278)

- **PATRÓN** `ibs_20min` < `0.2907` → IC=+0.317 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2907 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.3139` → IC=+0.284 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3139 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.2288` → IC=+0.280 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2288 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.471` → IC=+0.294 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.471 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.282 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.278)

- **PATRÓN** `volumen_regimen` > `1.244` → IC=+0.307 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.244 (IC base=+0.278)

- **PATRÓN** `volumen_pendiente_norm` > `0.2357` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2357 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` < `1.4234` → IC=+0.286 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4234 (IC base=+0.278)

- **PATRÓN** `volumen_spike_ratio` > `2.1456` → IC=+0.278 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1456 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `2613.0376` → IC=+0.279 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2613.0376 (IC base=+0.278)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.178 (n=2833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.202 (n=2822)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.3572` → IC=+0.177 (n=7437)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3572 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=8834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.573` → IC=+0.220 (n=8451)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.573 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.1742` → IC=+0.194 (n=3654)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1742 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.363` → IC=+0.255 (n=1726)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.363 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.2084` → IC=+0.162 (n=5605)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2084 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.6287` → IC=+0.161 (n=5604)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6287 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2427` → IC=+0.196 (n=1710)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2427 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.559` → IC=+0.168 (n=3575)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.559 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.177 (n=2707)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `1956.8086` → IC=+0.171 (n=7550)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1956.8086 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.183 (n=7362)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 110.0 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.184 (n=5408)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0066 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0812` → IC=+0.213 (n=2705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0812 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.170 (n=3824)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.4828` → IC=+0.227 (n=8106)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4828 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.2333` → IC=+0.162 (n=5872)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2333 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.342` → IC=+0.196 (n=1375)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.342 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.1748` → IC=+0.155 (n=5843)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1748 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2914` → IC=+0.217 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2914 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5608` → IC=+0.169 (n=3263)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5608 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6244` → IC=+0.173 (n=2472)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6244 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.177 (n=7069)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 111.0 (IC base=+0.170)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.221 (n=485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.187 (n=480)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0083 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.341` → IC=+0.211 (n=1432)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.341 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=1510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.18` → IC=+0.331 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.18 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.238 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.4398` → IC=+0.186 (n=1330)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4398 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.242 (n=940)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.249 (n=955)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1821` → IC=+0.285 (n=711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1821 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.244 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=526)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.3469` → IC=+0.259 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3469 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.305` → IC=+0.249 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.305 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.237 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4215` → IC=+0.268 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4215 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1820.92` → IC=+0.245 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1820.92 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.236 (n=419)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.201 (n=419)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=1262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.4035` → IC=+0.228 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4035 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2011` → IC=+0.211 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2011 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.481` → IC=+0.235 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.481 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `0.6876` → IC=+0.170 (n=553)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6876 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.0768` → IC=+0.168 (n=570)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0768 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.201 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5076` → IC=+0.179 (n=537)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5076 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.168 (n=407)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `10596.8161` → IC=+0.170 (n=1257)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10596.8161 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `445.0` → IC=+0.161 (n=1179)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 445.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.198 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0026 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2906` → IC=+0.162 (n=1348)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2906 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=655)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.139 (n=630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.5752` → IC=+0.190 (n=1348)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5752 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1321` → IC=+0.163 (n=1341)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1321 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.912` → IC=+0.206 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.912 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.159 (n=1348)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2089 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1561` → IC=+0.155 (n=413)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1561 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.4531` → IC=+0.149 (n=1236)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4531 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.4262` → IC=+0.137 (n=1236)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4262 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.163 (n=387)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 213.0 (IC base=+0.139)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.214 (n=642)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.2378` → IC=+0.218 (n=945)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2378 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.280 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2027` → IC=+0.204 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2027 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.7994` → IC=+0.199 (n=595)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.7994 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.7756` → IC=+0.215 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7756 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.209 (n=1672)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.237 (n=1053)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0995` → IC=+0.258 (n=399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0995 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.273 (n=417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.247 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.257 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3531` → IC=+0.256 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3531 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7646` → IC=+0.220 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7646 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `3.3633` → IC=+0.238 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.3633 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.217 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.219)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.220 (n=452)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4227` → IC=+0.159 (n=1348)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4227 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=1414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3707` → IC=+0.196 (n=1348)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.3707 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1491` → IC=+0.177 (n=883)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1491 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.229 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.0335` → IC=+0.150 (n=1188)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.0335 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6204` → IC=+0.146 (n=1349)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6204 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2902` → IC=+0.196 (n=212)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2902 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.4294` → IC=+0.159 (n=441)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4294 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5103` → IC=+0.167 (n=440)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5103 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5983.7933` → IC=+0.186 (n=899)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 5983.7933 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.149 (n=1286)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 160.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.156 (n=1424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.144 (n=1423)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.4737` → IC=+0.190 (n=1252)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.4737 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.1535` → IC=+0.142 (n=1399)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1535 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.161 (n=506)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8525` → IC=+0.150 (n=949)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8525 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.184 (n=213)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.140 (n=867)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8106 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.5251` → IC=+0.125 (n=433)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.5251 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `10015.5876` → IC=+0.163 (n=645)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 10015.5876 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.122 (n=1240)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 157.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.154 (n=698)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0101 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=1579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5045` → IC=+0.206 (n=1538)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5045 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.8341` → IC=+0.208 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8341 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.76` → IC=+0.254 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.76 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.131 (n=1537)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.2036 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6441` → IC=+0.123 (n=1537)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.6441 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1637` → IC=+0.127 (n=1544)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1637 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.123 (n=648)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.5416` → IC=+0.137 (n=654)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5416 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1594)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2403.067` → IC=+0.175 (n=1025)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2403.067 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.135 (n=1195)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 49.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.159 (n=687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0061 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.171 (n=521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.214 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.004` → IC=+0.127 (n=226)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 1.004 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.2013` → IC=+0.144 (n=1424)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2013 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.13` → IC=+0.139 (n=253)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.13 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6359` → IC=+0.144 (n=521)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6359 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2754` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2754 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4572` → IC=+0.139 (n=471)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4572 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.4248` → IC=+0.134 (n=470)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4248 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2760.1991` → IC=+0.166 (n=708)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2760.1991 (IC base=+0.117)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.228 (n=1309)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.2932` → IC=+0.203 (n=976)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2932 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.207 (n=1526)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.209 (n=662)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.7381` → IC=+0.260 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7381 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.5159` → IC=+0.215 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5159 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.241 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2049` → IC=+0.206 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2049 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.214 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6285 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.265 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.1464` → IC=+0.212 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1464 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.4039` → IC=+0.211 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4039 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.206 (n=1518)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2814.0154` → IC=+0.209 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2814.0154 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.226 (n=506)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.217 (n=686)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.226 (n=505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.215 (n=692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.0208` → IC=+0.302 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0208 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.184` → IC=+0.227 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.184 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.207 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.43` → IC=+0.247 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.43 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6333` → IC=+0.217 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6333 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.285 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.2006` → IC=+0.200 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2006 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4271` → IC=+0.204 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4271 (IC base=+0.207)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.196 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.175 (n=708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0086 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.3431` → IC=+0.166 (n=1867)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3431 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=1078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.236 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.8205` → IC=+0.175 (n=346)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.8205 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.163 (n=1540)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.759` → IC=+0.187 (n=950)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.759 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `0.871` → IC=+0.182 (n=1258)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.871 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `1.2084` → IC=+0.168 (n=630)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.2084 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.182 (n=577)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4459` → IC=+0.171 (n=684)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4459 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `1.8277` → IC=+0.168 (n=1368)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.8277 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.165 (n=2400)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `2650.5037` → IC=+0.163 (n=1895)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 2650.5037 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.178 (n=1900)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 150.0 (IC base=+0.159)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.137 (n=1446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0056 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.3415` → IC=+0.130 (n=1904)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.3415 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.126 (n=2176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 5.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.0598` → IC=+0.189 (n=722)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0598 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2074` → IC=+0.122 (n=1941)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2074 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2261` → IC=+0.121 (n=1959)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2261 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1654` → IC=+0.135 (n=540)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.1654 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4512` → IC=+0.149 (n=696)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4512 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2767.6856` → IC=+0.124 (n=1933)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2767.6856 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.133 (n=671)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 19.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.167 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0025 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.1084` → IC=+0.152 (n=234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1084 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.172 (n=498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` > `0.6659` → IC=+0.195 (n=352)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.6659 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.284` → IC=+0.158 (n=188)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.284 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1594` → IC=+0.133 (n=456)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1594 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.243` → IC=+0.147 (n=239)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.243 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.184` → IC=+0.132 (n=492)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 4.184 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6182` → IC=+0.176 (n=177)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6182 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.0914` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.0914 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.211` → IC=+0.137 (n=452)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.211 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.5157` → IC=+0.138 (n=459)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.5157 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `10902.4411` → IC=+0.143 (n=528)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 10902.4411 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `233.0` → IC=+0.155 (n=334)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 233.0 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.207 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.3378` → IC=+0.157 (n=669)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3378 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.147 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6112` → IC=+0.185 (n=589)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6112 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.3005` → IC=+0.154 (n=706)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.3005 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.494` → IC=+0.155 (n=253)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.494 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2242` → IC=+0.144 (n=669)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2242 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.7175` → IC=+0.149 (n=597)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.7175 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.198 (n=180)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1165` → IC=+0.160 (n=580)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1165 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4219` → IC=+0.147 (n=659)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4219 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `321.0` → IC=+0.151 (n=560)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 321.0 (IC base=+0.137)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.271 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.2048` → IC=+0.221 (n=443)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2048 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.9667` → IC=+0.268 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9667 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.1417` → IC=+0.213 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1417 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2089` → IC=+0.210 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2089 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.05` → IC=+0.240 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.05 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.212 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8331 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.232 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.1546` → IC=+0.269 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1546 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4055` → IC=+0.220 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4055 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7615` → IC=+0.236 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7615 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `12369.1399` → IC=+0.210 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12369.1399 (IC base=+0.207)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.120 (n=546)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0062 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.0839` → IC=+0.160 (n=207)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.0839 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6877` → IC=+0.136 (n=273)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6877 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2266` → IC=+0.133 (n=96)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2266 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.170 (n=237)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0089 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.5372` → IC=+0.140 (n=517)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5372 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.173 (n=484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.6895` → IC=+0.199 (n=134)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6895 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1792` → IC=+0.140 (n=415)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1792 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.556` → IC=+0.196 (n=278)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.556 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.0671` → IC=+0.161 (n=455)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0671 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.7217` → IC=+0.147 (n=462)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7217 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1794` → IC=+0.160 (n=142)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1794 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.4827` → IC=+0.149 (n=166)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4827 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.2151` → IC=+0.174 (n=225)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.2151 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=546)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3108.4588` → IC=+0.197 (n=173)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 3108.4588 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.4167` → IC=+0.167 (n=412)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.4167 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.154 (n=206)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7031 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.5803` → IC=+0.175 (n=195)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.5803 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2616.434` → IC=+0.137 (n=312)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2616.434 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.143 (n=415)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 40.0 (IC base=+0.096)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.174 (n=3639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0047 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.209 (n=3632)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=11384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=3661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.9399` → IC=+0.201 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9399 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.871` → IC=+0.238 (n=3992)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.871 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.8801` → IC=+0.169 (n=4858)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8801 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.201 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5948` → IC=+0.191 (n=3498)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5948 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1797.8356` → IC=+0.176 (n=10890)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1797.8356 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.200 (n=8374)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 83.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6576)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.149` → IC=+0.190 (n=4338)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.149 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=3748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=4545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.449` → IC=+0.248 (n=8673)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.449 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2484` → IC=+0.164 (n=6123)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.2484 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.063` → IC=+0.201 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.063 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.735` → IC=+0.184 (n=9526)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.735 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7046` → IC=+0.164 (n=2965)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7046 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.240 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.614` → IC=+0.192 (n=3032)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.614 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.198 (n=5909)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 47.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.218 (n=612)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.210 (n=1219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.3504` → IC=+0.198 (n=1828)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3504 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.211 (n=880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.200 (n=1235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.328 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.593` → IC=+0.351 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.593 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.255 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.8455` → IC=+0.196 (n=1154)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8455 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1845)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.264 (n=972)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.266 (n=1461)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.1244` → IC=+0.284 (n=641)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1244 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.260 (n=1321)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.3548` → IC=+0.283 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3548 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.483` → IC=+0.263 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.483 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.285 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.263 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` > `2.6294` → IC=+0.278 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6294 (IC base=+0.260)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `1818.86` → IC=+0.264 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1818.86 (IC base=+0.260)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.205 (n=582)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1127` → IC=+0.164 (n=768)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1127 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.3061` → IC=+0.204 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3061 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.186 (n=980)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.173 (n=396)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.156 (n=1572)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6267` → IC=+0.181 (n=581)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.6267 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2669` → IC=+0.198 (n=253)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2669 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.1192` → IC=+0.163 (n=1484)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1192 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.7577` → IC=+0.160 (n=1124)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7577 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `11247.6748` → IC=+0.160 (n=1556)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11247.6748 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `472.0` → IC=+0.163 (n=1623)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 472.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=1499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.3218` → IC=+0.163 (n=1498)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3218 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.282` → IC=+0.238 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.282 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.6688` → IC=+0.157 (n=240)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6688 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1309` → IC=+0.165 (n=1361)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1309 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.52` → IC=+0.160 (n=251)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.52 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.31` → IC=+0.153 (n=1363)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.31 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.165 (n=1498)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1913 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1512` → IC=+0.195 (n=401)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1512 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.409` → IC=+0.161 (n=1400)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.409 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.7588` → IC=+0.160 (n=933)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.7588 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `418.0` → IC=+0.155 (n=1151)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 418.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.255 (n=593)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=1863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.223 (n=1797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.349` → IC=+0.302 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.349 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` < `0.2087` → IC=+0.221 (n=1767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2087 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `1.77` → IC=+0.231 (n=1517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.77 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1918.8784` → IC=+0.222 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1918.8784 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.241 (n=1660)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0118 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1734` → IC=+0.240 (n=730)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1734 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.239 (n=777)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.3593` → IC=+0.266 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3593 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.751` → IC=+0.275 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.751 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.301 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7482` → IC=+0.230 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7482 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1697` → IC=+0.238 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1697 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1910.06` → IC=+0.241 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1910.06 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.234 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.234)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.190 (n=816)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0039 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4312` → IC=+0.152 (n=1853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.4312 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=1937)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.8747` → IC=+0.263 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8747 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3572` → IC=+0.163 (n=717)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3572 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.174` → IC=+0.165 (n=767)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.174 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8727` → IC=+0.159 (n=1236)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8727 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.213 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.157 (n=792)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.4733` → IC=+0.157 (n=599)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4733 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7958.7991` → IC=+0.236 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7958.7991 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `87.0` → IC=+0.172 (n=764)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 87.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.157 (n=1329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0065 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.147 (n=1510)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.140 (n=689)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 7.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.5838` → IC=+0.198 (n=1329)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5838 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1579` → IC=+0.138 (n=1314)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1579 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.3` → IC=+0.167 (n=226)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.3 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.151 (n=665)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6971 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.2015` → IC=+0.136 (n=504)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.2015 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.238 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.4426` → IC=+0.146 (n=1437)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4426 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `7156.4491` → IC=+0.193 (n=685)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7156.4491 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.139 (n=1433)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 173.0 (IC base=+0.134)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.138 (n=1235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0081 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4673` → IC=+0.194 (n=1851)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.4673 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.0828` → IC=+0.203 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0828 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.525` → IC=+0.238 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.525 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.8929` → IC=+0.140 (n=1235)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8929 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1622` → IC=+0.121 (n=1896)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_pendiente_norm` < 0.1622 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.5707` → IC=+0.123 (n=793)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.5707 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=1862)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2897.8254` → IC=+0.253 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2897.8254 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.136 (n=1443)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 53.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.176 (n=596)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0058 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1334` → IC=+0.156 (n=594)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1334 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.6371` → IC=+0.206 (n=1780)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6371 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` < `0.2212` → IC=+0.134 (n=1447)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2212 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.46` → IC=+0.126 (n=1714)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.46 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.7129` → IC=+0.155 (n=783)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.7129 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2202` → IC=+0.169 (n=279)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2202 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4381` → IC=+0.141 (n=539)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4381 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2801.7024` → IC=+0.176 (n=593)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2801.7024 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.125 (n=1410)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 51.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.231 (n=1645)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=1926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.214 (n=1644)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.262 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.2117` → IC=+0.234 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2117 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.275` → IC=+0.271 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.275 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.2484` → IC=+0.215 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2484 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.222 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2323` → IC=+0.251 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2323 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.221 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4406 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2820.5354` → IC=+0.220 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2820.5354 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.220 (n=651)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.228 (n=652)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.216 (n=1380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.267 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `1.2216` → IC=+0.208 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2216 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.9133` → IC=+0.209 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9133 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.857` → IC=+0.266 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.857 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `1.2355` → IC=+0.238 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2355 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.271 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.1829` → IC=+0.203 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1829 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4297` → IC=+0.204 (n=1764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4297 (IC base=+0.206)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.153 (n=3330)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.185 (n=2896)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0091 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.5136` → IC=+0.182 (n=3290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.5136 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=1303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.176 (n=1454)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.9463` → IC=+0.233 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9463 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1798` → IC=+0.182 (n=1226)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1798 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.4611` → IC=+0.167 (n=2051)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.4611 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.2` → IC=+0.202 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.2 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.170 (n=2188)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.6279 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.1706` → IC=+0.203 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1706 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` < `1.4563` → IC=+0.180 (n=1084)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4563 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `1.8777` → IC=+0.180 (n=2166)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8777 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=2353)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `2914.473` → IC=+0.175 (n=2939)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2914.473 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.207 (n=840)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4848` → IC=+0.170 (n=2509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.4848 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.170 (n=1104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 6.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.1814` → IC=+0.178 (n=1104)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1814 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.671` → IC=+0.178 (n=479)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.671 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.238` → IC=+0.162 (n=2502)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.238 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2471` → IC=+0.156 (n=2372)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.2471 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.156 (n=2281)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.5396` → IC=+0.163 (n=1091)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5396 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.8264` → IC=+0.157 (n=1652)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.8264 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3330)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `6002.8639` → IC=+0.158 (n=2242)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 6002.8639 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.155 (n=1629)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 89.0 (IC base=+0.151)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.199 (n=367)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.180 (n=373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0033 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0869` → IC=+0.231 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0869 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.190 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 8.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.5463` → IC=+0.204 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5463 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1436` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1436 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.3655` → IC=+0.187 (n=404)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.3655 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.517` → IC=+0.185 (n=440)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 2.517 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.8402` → IC=+0.210 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8402 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.3007` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3007 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.209 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6311` → IC=+0.209 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6311 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `12563.2849` → IC=+0.222 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12563.2849 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.217 (n=425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.3673` → IC=+0.152 (n=958)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3673 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.174 (n=366)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.180 (n=423)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1409 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6103` → IC=+0.148 (n=435)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.6103 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.6922` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6922 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.162 (n=938)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8795` → IC=+0.185 (n=640)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8795 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.0686` → IC=+0.166 (n=447)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0686 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4209` → IC=+0.145 (n=319)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4209 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.149 (n=637)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `14911.0423` → IC=+0.161 (n=435)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 14911.0423 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `705.0` → IC=+0.145 (n=913)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 705.0 (IC base=+0.139)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.187 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.181 (n=283)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.01 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.5756` → IC=+0.175 (n=625)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.5756 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.233 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.706` → IC=+0.225 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.706 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` < `0.3498` → IC=+0.169 (n=751)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` < 0.3498 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.2085` → IC=+0.201 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2085 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `3.3854` → IC=+0.166 (n=623)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 3.3854 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.8279` → IC=+0.169 (n=557)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.8279 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2427.507` → IC=+0.195 (n=283)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2427.507 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.318 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.250 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `0.4634` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4634 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` > `0.1043` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1043 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` < `2.564` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.564 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `4.0788` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 4.0788 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `2362.8582` → IC=+0.258 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2362.8582 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.246)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.181 (n=929)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0072 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3766` → IC=+0.181 (n=926)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3766 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=403)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.182 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 4.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.190 (n=702)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5305 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.8827` → IC=+0.183 (n=351)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8827 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.2131` → IC=+0.182 (n=873)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2131 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.178` → IC=+0.185 (n=940)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 4.178 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `1.0845` → IC=+0.176 (n=926)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 1.0845 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` > `0.6393` → IC=+0.176 (n=1052)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6393 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.1656` → IC=+0.192 (n=319)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1656 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` < `2.4732` → IC=+0.179 (n=1033)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 2.4732 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.5228` → IC=+0.176 (n=923)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.5228 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=1048)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.202 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.4837` → IC=+0.184 (n=859)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.4837 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=298)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.160 (n=604)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.7466` → IC=+0.160 (n=860)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.7466 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.0954` → IC=+0.164 (n=858)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.0954 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.6041` → IC=+0.172 (n=187)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6041 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.399` → IC=+0.165 (n=780)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 4.399 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.647` → IC=+0.196 (n=287)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.647 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `0.7253` → IC=+0.157 (n=767)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.7253 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.175 (n=364)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `2.1996` → IC=+0.170 (n=741)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 2.1996 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7506.7691` → IC=+0.172 (n=858)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7506.7691 (IC base=+0.156)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.159 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0111 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.3886` → IC=+0.136 (n=201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3886 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.172 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.2142` → IC=+0.188 (n=219)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2142 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `1.2406` → IC=+0.137 (n=312)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 1.2406 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.177` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.177 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8864` → IC=+0.170 (n=201)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8864 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.5495` → IC=+0.149 (n=129)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.5495 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7686` → IC=+0.163 (n=194)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.7686 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=354)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `3372.8412` → IC=+0.172 (n=269)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3372.8412 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.152 (n=248)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 55.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.181 (n=258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0069 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.3939` → IC=+0.190 (n=172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3939 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.163 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 16.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.180 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 10.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.1364` → IC=+0.250 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1364 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.5982` → IC=+0.230 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5982 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.67` → IC=+0.152 (n=136)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 2.67 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.281` → IC=+0.164 (n=248)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 5.281 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6758` → IC=+0.182 (n=86)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6758 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.1117` → IC=+0.220 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1117 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.611` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.611 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.164 (n=114)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `3291.3893` → IC=+0.185 (n=258)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3291.3893 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.200 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.152)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0065` → IC=-0.206 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=406)

- **FILTRO** `dist_vwap_pct` > `0.1776` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1776
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=371)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.169 (n=451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0039 (IC base=+0.083)

- **PATRÓN** `ibs_20min` > `0.4727` → IC=+0.165 (n=927)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.4727 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.1429` → IC=+0.144 (n=495)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1429 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.465` → IC=+0.187 (n=215)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.465 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.188 (n=123)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.083)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.123 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0045 (IC base=+0.024)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.303 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1776` → IC=+0.130 (n=371)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1776 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.187` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 3.187 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1383` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1383 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.5523` → IC=+0.138 (n=269)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5523 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.4436` → IC=+0.136 (n=240)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4436 (IC base=+0.024)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.146 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0058 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4669` → IC=+0.183 (n=320)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.4669 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1286` → IC=+0.171 (n=165)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1286 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `2.4916` → IC=+0.142 (n=280)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4916 (IC base=+0.097)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.136 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0043 (IC base=+0.069)

- **PATRÓN** `drift_60min` |x|≤ `0.0543` → IC=+0.153 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0543 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.0662` → IC=+0.138 (n=158)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.0662 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.557` → IC=+0.157 (n=132)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.557 (IC base=+0.069)

- **PATRÓN** `volumen_regimen` < `1.1168` → IC=+0.129 (n=149)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1168 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.07` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.07 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `2.0359` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.0359 (IC base=+0.069)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6598` → IC=-0.133 (n=137)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6598
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=279)

- **FILTRO** `sigma_h` > `0.0059` → IC=-0.198 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0059
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=124)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=130)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.136 (n=229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0049 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6598` → IC=+0.219 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6598 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.3347` → IC=+0.178 (n=119)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.3347 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.499` → IC=+0.294 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.499 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `1.7371` → IC=+0.146 (n=173)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.7371 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `1122.8965` → IC=+0.150 (n=275)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1122.8965 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.287 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=+0.003)

- **PATRÓN** `dist_vwap_pct` < `0.1269` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1269 (IC base=+0.003)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.258` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.258 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.3281` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.3281 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.268` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.268 (IC base=+0.003)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.163 (n=90)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.003)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.265 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=96)

- **FILTRO** `ibs_20min` > `0.2051` → IC=-0.311 (n=35)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2051
  - _Potencial_: sin este filtro IC_bueno=+0.232 (n=69)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.149 (n=263)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6429 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.521` → IC=+0.121 (n=122)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` > 5.521 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2443` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2443 (IC base=+0.055)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.200 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=-0.024)

- **PATRÓN** `ibs_20min` < `0.2051` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2051 (IC base=-0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=-0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.5975` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.5975 (IC base=-0.024)

- **PATRÓN** `volumen_spike_ratio` > `1.4883` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4883 (IC base=-0.024)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0033` → IC=-0.308 (n=71)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=146)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.365 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=167)

- **FILTRO** `dist_vwap_pct` > `0.1613` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1613
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=193)

- **FILTRO** `volumen_regimen` < `0.7148` → IC=-0.339 (n=54)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7148
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=163)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.357 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=119)

- **FILTRO** `dist_vwap_pct` > `0.4126` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4126
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=158)

- **FILTRO** `sigma_ewma_delta_pct` > `8.423` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.423
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=150)

- **FILTRO** `volumen_pendiente_norm` > `0.0895` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0895
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=78)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=51)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.275 (n=38)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=38)

- **FILTRO** `sigma_h` < `0.0018` → IC=-0.300 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0018
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **FILTRO** `dist_vwap_pct` < `0.0689` → IC=-0.283 (n=44)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0689
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=30)

- **FILTRO** `volumen_regimen` > `0.9258` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9258
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=56)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.7001` → IC=-0.444 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7001
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=34)

- **FILTRO** `volumen_regimen` > `1.108` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 1.108
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=52)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.441 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=48)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.367 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=35)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.447 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=55)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1681` → IC=-0.134 (n=129)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1681
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=253)

- **FILTRO** `dist_vwap_pct` > `0.6226` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6226
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=355)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.162 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0058 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.6417` → IC=+0.144 (n=276)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.6417 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.4919` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.4919 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.178 (n=253)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.1681 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.105` → IC=+0.155 (n=117)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 6.105 (IC base=+0.073)

- **PATRÓN** `libro_liquidez` > `3752.8201` → IC=+0.174 (n=130)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3752.8201 (IC base=+0.073)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=98)

- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=90)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.132 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0044 (IC base=+0.131)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.167 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0033 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.2293` → IC=+0.158 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2293 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.206 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.153 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 5.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.101` → IC=+0.209 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.101 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.191` → IC=+0.141 (n=151)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.191 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.611` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.611 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.1369` → IC=+0.147 (n=131)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.1369 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.193 (n=99)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.2913` → IC=+0.178 (n=88)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.2913 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.153 (n=99)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.131)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6191` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6191
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=76)

- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.174 (n=84)

- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.194 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0022 (IC base=+0.015)

- **PATRÓN** `ibs_20min` > `0.8782` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.8782 (IC base=+0.015)

- **PATRÓN** `libro_liquidez` > `1624.9844` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1624.9844 (IC base=+0.015)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.122 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0053 (IC base=+0.062)

- **PATRÓN** `ibs_20min` < `0.1644` → IC=+0.174 (n=84)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1644 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.429` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.429 (IC base=+0.062)

- **PATRÓN** `volumen_regimen` < `0.8247` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.8247 (IC base=+0.062)

- **PATRÓN** `volumen_pendiente_norm` > `0.0753` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0753 (IC base=+0.062)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=62)

- **FILTRO** `dist_vwap_pct` > `0.1415` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1415
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=57)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.218 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.231 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.233 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.212 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.6875` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6875 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.289 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.0812` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0812 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.409 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.216 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.036)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.282)

- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.397 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.282)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.7846` → IC=+0.338 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7846 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `1695.0` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1695.0 (IC base=+0.282)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.222)

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
- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.282)

- **PATRÓN** `elapsed_s` > `210.1` → IC=+0.397 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.1 (IC base=+0.282)

- **PATRÓN** `drift_15min` |x|≤ `1.1328` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.1328 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.7846` → IC=+0.338 (n=35)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7846 (IC base=+0.282)

- **PATRÓN** `ballena_activa_n` < `1695.0` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1695.0 (IC base=+0.282)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.222)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=783)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2905.4554` → IC=+0.167 (n=268)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2905.4554 (IC base=+0.108)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.124 (n=783)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2905.4554` → IC=+0.167 (n=268)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2905.4554 (IC base=+0.108)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=139)

- **FILTRO** `libro_liquidez` < `11811.9773` → IC=-0.161 (n=116)

  - _Acción_: SKIP cuando `libro_liquidez` < 11811.9773
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=218)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=204)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=43)

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

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=88)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=1930)

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
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=81)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.127 (n=81)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 16.0 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 25.0 (IC base=+0.051)

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

- **PATRÓN** `liq_n` > `18.0` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 18.0 (IC base=+0.021)

- **PATRÓN** `liq_usd_total` > `69212.62` → IC=+0.164 (n=105)

  - _Acción_: Kelly boost +0.82€ cuando `liq_usd_total` > 69212.62 (IC base=+0.021)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=141)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=845)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=799)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=439)

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
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=205)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.495 (IC base=+0.016)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=658)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=658)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=395)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=395)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=176)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=176)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=111)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.132 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=68)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=95)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=119)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=218)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=95)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=98)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=249)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=249)

- **FILTRO** `py_entrada` < `0.425` → IC=-0.152 (n=67)

  - _Acción_: SKIP cuando `py_entrada` < 0.425
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=212)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=141)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.146 (n=314)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=770)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `profundidad_ratio` < `293.3` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `profundidad_ratio` < 293.3
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=63)

- **PATRÓN** `py_entrada` > `0.44` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.44 (IC base=+0.016)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.59` → IC=+0.120 (n=106)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.59 (IC base=+0.070)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.070)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` > `13.45` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `restante_min` > 13.45
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=58)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=61)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=63)

- **FILTRO** `profundidad_ratio` < `56.9` → IC=-0.150 (n=58)

  - _Acción_: SKIP cuando `profundidad_ratio` < 56.9
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.122 (n=43)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 9.0 (IC base=+0.061)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=69)

- **FILTRO** `profundidad_ratio` < `78.4` → IC=-0.204 (n=42)

  - _Acción_: SKIP cuando `profundidad_ratio` < 78.4
  - _Potencial_: sin este filtro IC_bueno=+0.144 (n=43)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=81)

- **PATRÓN** `py_entrada` > `0.51` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.51 (IC base=-0.029)

- **PATRÓN** `profundidad_ratio` > `78.4` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `profundidad_ratio` > 78.4 (IC base=-0.029)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.51 (IC base=-0.015)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=95)

- **FILTRO** `restante_min` < `3.82` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `restante_min` < 3.82
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.210 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=89)

- **FILTRO** `lag_apertura_s` > `70.81` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `lag_apertura_s` > 70.81
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=60)

- **FILTRO** `profundidad_ratio` < `81.9` → IC=-0.205 (n=59)

  - _Acción_: SKIP cuando `profundidad_ratio` < 81.9
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=59)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.44 (IC base=+0.065)

- **PATRÓN** `profundidad_ratio` > `24.5` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `profundidad_ratio` > 24.5 (IC base=+0.065)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `restante_min` < `13.48` → IC=-0.146 (n=63)

  - _Acción_: SKIP cuando `restante_min` < 13.48
  - _Potencial_: sin este filtro IC_bueno=+0.219 (n=30)

- **FILTRO** `lag_apertura_s` > `90.91` → IC=-0.134 (n=69)

  - _Acción_: SKIP cuando `lag_apertura_s` > 90.91
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=24)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 13.48 (IC base=-0.026)

- **PATRÓN** `lag_apertura_s` < `90.91` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 90.91 (IC base=-0.026)

- **PATRÓN** `restante_min` > `13.48` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `restante_min` > 13.48 (IC base=+0.009)

- **PATRÓN** `lag_apertura_s` < `90.91` → IC=+0.176 (n=35)

  - _Acción_: Kelly boost +0.88€ cuando `lag_apertura_s` < 90.91 (IC base=+0.009)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **FILTRO** `restante_min` < `3.75` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `restante_min` < 3.75
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=48)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.152 (n=87)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=52)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.5 (IC base=-0.032)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.205 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=88)

- **FILTRO** `restante_min` < `3.12` → IC=-0.143 (n=54)

  - _Acción_: SKIP cuando `restante_min` < 3.12
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=110)

- **FILTRO** `lag_apertura_s` > `112.83` → IC=-0.149 (n=55)

  - _Acción_: SKIP cuando `lag_apertura_s` > 112.83
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=109)

- **FILTRO** `profundidad_ratio` < `6.1` → IC=-0.174 (n=41)

  - _Acción_: SKIP cuando `profundidad_ratio` < 6.1
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=123)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7778)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.168 (n=3767)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=11675)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.162 (n=3943)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=12062)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.198 (n=674)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=2025)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.187 (n=675)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2073)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=694)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2187)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.175 (n=657)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=2034)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.174 (n=716)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=2165)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2222)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2314)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3054)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=409)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=400)

- **FILTRO** `libro_liquidez` < `17011.7455` → IC=-0.143 (n=228)

  - _Acción_: SKIP cuando `libro_liquidez` < 17011.7455
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=685)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `hora_utc` > `18.0` → IC=-0.146 (n=80)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=262)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.214 (n=82)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=260)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=10781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=24333)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.274 (n=8684)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=26430)

- **FILTRO** `ibs_7min` < `0.2755` → IC=-0.234 (n=8778)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=26336)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=11797)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=23317)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.232 (n=10852)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=33446)

- **FILTRO** `ibs_7min` > `0.2919` → IC=-0.179 (n=11074)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2919
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33224)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.138 (n=1759)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4098)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=1390)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4467)

- **FILTRO** `ibs_7min` < `0.7103` → IC=-0.252 (n=1932)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7103
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3925)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.175 (n=1449)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=4408)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.259 (n=1888)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=5724)

- **FILTRO** `drift_7min_pct` |x|> `0.1365` → IC=-0.130 (n=1901)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1365
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5711)

- **FILTRO** `ibs_7min` > `0.7903` → IC=-0.208 (n=1902)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7903
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=5710)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=1419)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=4634)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.251 (n=1475)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=4578)

- **FILTRO** `ibs_7min` < `0.7466` → IC=-0.194 (n=1513)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7466
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=4540)

- **FILTRO** `ballena_activa_n` > `158.0` → IC=-0.177 (n=1505)

  - _Acción_: SKIP cuando `ballena_activa_n` > 158.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4548)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=1418)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4718)

- **FILTRO** `ibs_7min` > `0.2611` → IC=-0.185 (n=1533)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2611
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4603)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.180 (n=1532)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4604)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.168 (n=1358)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=4216)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.303 (n=1391)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4183)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.242 (n=1833)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=3741)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.211 (n=1388)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=4186)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.243 (n=1889)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=6279)

- **FILTRO** `ibs_7min` > `0.75` → IC=-0.174 (n=2038)

  - _Acción_: SKIP cuando `ibs_7min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6130)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.130 (n=1855)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=3932)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.234 (n=1705)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=4082)

- **FILTRO** `ibs_7min` < `0.7406` → IC=-0.183 (n=1446)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7406
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4341)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.173 (n=1413)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4374)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.257 (n=1478)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=4453)

- **FILTRO** `ibs_7min` > `0.2753` → IC=-0.179 (n=1482)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2753
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4449)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.182 (n=1475)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4456)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.263 (n=1415)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4643)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.234 (n=1507)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=4551)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.180 (n=1997)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=6450)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.273 (n=1414)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4371)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.224 (n=1446)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4339)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1382)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4403)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.208 (n=1875)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=6129)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1139)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=567)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=329)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=571)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.130 (n=801)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `469.512` → IC=+0.143 (n=267)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 469.512 (IC base=+0.115)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.135 (n=61)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.197 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 11.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.136 (n=160)

  - _Acción_: Kelly boost +0.68€ cuando `total_vol_5m` < 445.688 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 14.0 (IC base=+0.131)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.167 (n=70)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 11.0 (IC base=+0.107)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.175 (n=112)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.124 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 4.0 (IC base=+0.098)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.210 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.184 (n=74)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 75.0 (IC base=+0.098)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.179 (n=138)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.235 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `5032.488` → IC=+0.163 (n=93)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 5032.488 (IC base=+0.134)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4006` → IC=+0.144 (n=144)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.4006 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.130 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 13.0 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.102)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0071` → IC=-0.324 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0071
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=273)

- **FILTRO** `T_h` > `54.3209` → IC=-0.248 (n=276)

  - _Acción_: SKIP cuando `T_h` > 54.3209
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=137)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `54.581` → IC=-0.315 (n=63)

  - _Acción_: SKIP cuando `T_h` > 54.581
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=65)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.250 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.115)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0107` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0107
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.013` → IC=-0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=58)

- **FILTRO** `T_h` < `39.9918` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `T_h` < 39.9918
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=58)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `2.719` → IC=-0.228 (n=200)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.719
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=210)

- **FILTRO** `sigma_h` > `0.0095` → IC=-0.320 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.293 (n=264)

- **FILTRO** `sigma_h` < `0.0044` → IC=-0.332 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=264)

- **FILTRO** `T_h` > `61.3303` → IC=-0.330 (n=263)

  - _Acción_: SKIP cuando `T_h` > 61.3303
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **PATRÓN** `pct_vs_K` |x|≤ `1.0396` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `pct_vs_K` |x|≤ 1.0396 (IC base=-0.114)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.004` → IC=-0.158 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.004
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=109)

- **FILTRO** `T_h` > `79.6334` → IC=-0.146 (n=97)

  - _Acción_: SKIP cuando `T_h` > 79.6334
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=48)

- **FILTRO** `pct_vs_K` |x|> `2.84` → IC=-0.368 (n=36)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.84
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=109)

- **FILTRO** `pct_vs_K` |x|> `2.9509` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9509
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=88)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.4229` → IC=-0.357 (n=54)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4229
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=62)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.328 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=84)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=84)

- **FILTRO** `T_h` > `60.9515` → IC=-0.329 (n=74)

  - _Acción_: SKIP cuando `T_h` > 60.9515
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

- **PATRÓN** `pct_vs_K` |x|≤ `1.3415` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.3415 (IC base=-0.203)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0073` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0073
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=75)

- **FILTRO** `T_h` > `132.7892` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `T_h` > 132.7892
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=67)

- **FILTRO** `pct_vs_K` |x|> `4.8556` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.8556
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=76)

- **FILTRO** `sigma_h` < `0.0146` → IC=-0.375 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0146
  - _Potencial_: sin este filtro IC_bueno=-0.315 (n=25)

- **FILTRO** `T_h` > `58.2361` → IC=-0.373 (n=53)

  - _Acción_: SKIP cuando `T_h` > 58.2361
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=18)

- **PATRÓN** `pct_vs_K` |x|≤ `1.14` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.14 (IC base=-0.039)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1186` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1186 (IC base=+0.378)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.407 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.378)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.427 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.378)

- **PATRÓN** `T_h` > `0.4704` → IC=+0.435 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4704 (IC base=+0.378)

- **PATRÓN** `dist_50` > `0.4377` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4377 (IC base=+0.378)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.378)

- **PATRÓN** `edge` > `0.1118` → IC=+0.456 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1118 (IC base=+0.416)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.416)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.443 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.416)

- **PATRÓN** `T_h` < `0.6208` → IC=+0.424 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6208 (IC base=+0.416)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.462 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.480 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.472 (n=104)
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

- **PATRÓN** `edge` > `0.114` → IC=+0.467 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.114 (IC base=+0.460)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.486 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.460)

- **PATRÓN** `T_h` > `0.9563` → IC=+0.467 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.9563 (IC base=+0.460)

- **PATRÓN** `dist_50` > `0.5` → IC=+0.482 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.5 (IC base=+0.460)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.465 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.460)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=198)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=308)

- **FILTRO** `streak_estiramiento` > `0.8566` → IC=-0.162 (n=66)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8566
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=201)

- **PATRÓN** `streak_estiramiento` < `0.4787` → IC=+0.123 (n=67)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.4787 (IC base=+0.030)

- **PATRÓN** `streak_estiramiento` < `0.7314` → IC=+0.120 (n=177)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.7314 (IC base=+0.035)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=19)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `2331737.7` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 2331737.7
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=46)

- **FILTRO** `streak_estiramiento` > `0.479` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.479
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=37)

- **PATRÓN** `streak_estiramiento` < `0.479` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.479 (IC base=-0.008)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.122 (n=80)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.121 (n=93)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 49.0 (IC base=+0.053)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=430)

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

- **FILTRO** `streak_estiramiento` > `0.9124` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.9124
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

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
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=654)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1205)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=810)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=784)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3068)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1559)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1567)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.193 (n=597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0043 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.226 (n=596)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.201 (n=787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.188)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2165` → IC=+0.192 (n=596)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2165 (IC base=+0.188)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.233 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=1679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=1856)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_15` > `0.6087` → IC=+0.268 (n=1787)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6087 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.1185` → IC=+0.183 (n=899)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1185 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.6071` → IC=+0.180 (n=1695)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.6071 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.833` → IC=+0.274 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.833 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `8780.1789` → IC=+0.196 (n=596)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 8780.1789 (IC base=+0.188)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=719)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.218 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.0598` → IC=+0.291 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0598 (IC base=+0.208)

- **PATRÓN** `drift_15min` |x|≤ `0.3838` → IC=+0.216 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3838 (IC base=+0.208)

- **PATRÓN** `delta_ratio_macro` |x|> `0.255` → IC=+0.246 (n=132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.255 (IC base=+0.208)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1084` → IC=+0.280 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1084 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.240 (n=371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.276 (n=395)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.3842` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3842 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.55` → IC=+0.272 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.55 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `16060.5409` → IC=+0.231 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16060.5409 (IC base=+0.208)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.693` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.693
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=442)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.169 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0035 (IC base=+0.130)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.133 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.005 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.160 (n=183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.130)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.171 (n=138)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.86€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.130)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1217` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1217 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.135 (n=434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_15` > `0.6586` → IC=+0.253 (n=370)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6586 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1133` → IC=+0.148 (n=296)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1133 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.257` → IC=+0.219 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.257 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `9475.4181` → IC=+0.147 (n=188)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 9475.4181 (IC base=+0.130)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.281 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.1481` → IC=+0.195 (n=188)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1481 (IC base=+0.171)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0606` → IC=+0.188 (n=213)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.0606 (IC base=+0.171)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2673` → IC=+0.216 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2673 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.171)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.255 (n=214)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.177 (n=122)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.175 (n=207)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.286` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.286 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=154)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `3071.8702` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3071.8702 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.213 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.171)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.68` → IC=-0.154 (n=105)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=1099)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=-0.007)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.271 (n=155)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.225 (n=205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.196)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0403` → IC=+0.200 (n=465)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0403 (IC base=+0.196)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.260 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=228)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `ibs_15` > `0.5695` → IC=+0.286 (n=465)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5695 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.3546` → IC=+0.209 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3546 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` < `0.8342` → IC=+0.199 (n=539)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.8342 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.251` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.251 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.374` → IC=+0.199 (n=423)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 7.374 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2911.0954` → IC=+0.283 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.0954 (IC base=+0.196)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.150 (n=524)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1176 (IC base=+0.053)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.355 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.349)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.373 (n=148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.349)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.352 (n=296)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.349)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.362 (n=441)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.349)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.387 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.349)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.369 (n=449)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.349)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.390 (n=442)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.349)

- **PATRÓN** `dist_vwap_pct` > `0.4241` → IC=+0.389 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4241 (IC base=+0.349)

- **PATRÓN** `dist_vwap_pct` < `0.1081` → IC=+0.350 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1081 (IC base=+0.349)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.247` → IC=+0.356 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.247 (IC base=+0.349)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.350 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.349)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.353 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.349)

- **PATRÓN** `libro_liquidez` > `3425.1488` → IC=+0.360 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3425.1488 (IC base=+0.349)

- **PATRÓN** `ballena_activa_n` < `459.0` → IC=+0.371 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 459.0 (IC base=+0.349)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.362 (n=216)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.354)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.381 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.354)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.369 (n=82)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.354)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.364 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.354)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.373 (n=163)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.354)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1241` → IC=+0.394 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1241 (IC base=+0.354)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.380 (n=247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.354)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.387 (n=245)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.354)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.405 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.152` → IC=+0.360 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.152 (IC base=+0.354)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.356 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.354)

- **PATRÓN** `libro_liquidez` > `11121.9309` → IC=+0.373 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11121.9309 (IC base=+0.354)

- **PATRÓN** `ballena_activa_n` < `571.0` → IC=+0.399 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 571.0 (IC base=+0.354)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.340 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.342)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.370 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.342)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.351 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.366 (n=177)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.342)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.367 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.342)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.405 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.342)

- **PATRÓN** `ibs_15` > `0.743` → IC=+0.395 (n=198)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.743 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.375 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` < `0.1133` → IC=+0.353 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1133 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.358 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.344 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.342)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.349 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.342)

- **PATRÓN** `libro_liquidez` > `3456.6166` → IC=+0.351 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3456.6166 (IC base=+0.342)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.352 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.342)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0127` → IC=-0.223 (n=706)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0127
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2121)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=981)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=1846)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1373` → IC=+0.250 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1373 (IC base=-0.068)

- **PATRÓN** `ibs_15` > `0.6409` → IC=+0.273 (n=672)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6409 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.191 (n=541)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0765` → IC=+0.247 (n=1782)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0765 (IC base=-0.028)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1786` → IC=+0.243 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1786 (IC base=-0.028)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.276 (n=1994)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.679` → IC=+0.300 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.679 (IC base=-0.028)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0471` → IC=-0.214 (n=1140)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0471
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=563)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.226 (n=425)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1278)

- **FILTRO** `sigma_ewma_delta_pct` > `19.642` → IC=-0.255 (n=304)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.642
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1399)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.163 (n=164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0027 (IC base=+0.081)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2051` → IC=+0.275 (n=87)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2051 (IC base=+0.081)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1073` → IC=+0.341 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1073 (IC base=+0.081)

- **PATRÓN** `ibs_15` > `0.7496` → IC=+0.334 (n=191)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7496 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.0982` → IC=+0.280 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0982 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` < `0.3564` → IC=+0.275 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3564 (IC base=+0.081)

- **PATRÓN** `ibs_15` < `0.213` → IC=+0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.213 (IC base=-0.198)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=408)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.151 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0067 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.172 (n=285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.004 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.220 (n=141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.149)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0901` → IC=+0.148 (n=285)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio_macro` |x|> 0.0901 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.232 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.6647` → IC=+0.260 (n=319)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6647 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.181 (n=230)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.042` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 14.042 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.024` → IC=+0.151 (n=273)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 9.024 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=408)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `11052.2058` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 11052.2058 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.249 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.3574` → IC=+0.242 (n=672)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3574 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `0.4743` → IC=+0.257 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4743 (IC base=+0.237)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2064` → IC=+0.267 (n=346)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2064 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.256 (n=289)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.237)

- **PATRÓN** `ibs_15` < `0.2722` → IC=+0.284 (n=671)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2722 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.7515` → IC=+0.325 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7515 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.82` → IC=+0.260 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.82 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.283` → IC=+0.244 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.283 (IC base=+0.237)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.256 (n=166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=502)

- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.225 (n=227)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=441)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.274 (n=166)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=502)

- **PATRÓN** `ibs_15` > `0.9` → IC=+0.309 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9 (IC base=-0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0769` → IC=+0.230 (n=305)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0769 (IC base=-0.042)

- **PATRÓN** `ibs_15` < `0.3455` → IC=+0.258 (n=341)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3455 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7388` → IC=+0.240 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7388 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.1821` → IC=+0.223 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1821 (IC base=-0.042)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.259 (n=409)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=411)

- **FILTRO** `drift_15min` |x|> `1.2549` → IC=-0.267 (n=204)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2549
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=616)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.260 (n=215)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=605)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1379` → IC=+0.300 (n=238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1379 (IC base=-0.039)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1078` → IC=+0.334 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1078 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3391` → IC=+0.305 (n=525)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3391 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.8999` → IC=+0.340 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8999 (IC base=-0.039)

### UPDOWN_GBM_ETH_15M_HORA7
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1645` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1645 (IC base=+0.049)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **FILTRO** `ibs_15` < `0.879` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.879
  - _Potencial_: sin este filtro IC_bueno=+0.389 (n=7)

- **PATRÓN** `dist_vwap_pct` > `0.1645` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1645 (IC base=+0.049)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.299 (n=626)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.333 (n=238)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.307 (n=237)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.337 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8411` → IC=+0.329 (n=711)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8411 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.339 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4333 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.347 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.292 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `13022.3239` → IC=+0.297 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13022.3239 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.292 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.287)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.289 (n=349)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.003 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.350 (n=131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2605` → IC=+0.311 (n=130)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2605 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3906` → IC=+0.311 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3906 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.339 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.319 (n=390)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.365 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16113.4131` → IC=+0.326 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16113.4131 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.312 (n=322)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.069` → IC=+0.312 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.069 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.301 (n=214)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.326 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8539` → IC=+0.339 (n=321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8539 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.302 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` < `0.1135` → IC=+0.294 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1135 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.169` → IC=+0.333 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.169 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.301 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.162 (n=72)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=217)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.134 (n=192)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=65)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.121` → IC=-0.173 (n=111)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.121
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=336)

- **FILTRO** `ballena_activa_n` > `56.0` → IC=-0.208 (n=46)

  - _Acción_: SKIP cuando `ballena_activa_n` > 56.0
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=140)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1232` → IC=-0.159 (n=42)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1232
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=129)

- **FILTRO** `drift_15min` |x|> `0.2287` → IC=-0.250 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2287
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1681` → IC=-0.250 (n=22)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1681
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

- **FILTRO** `drift_15min` |x|> `0.2131` → IC=-0.231 (n=24)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2131
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
- **PATRÓN** `T_h` > `79.3918` → IC=+0.219 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.3918 (IC base=+0.202)

- **PATRÓN** `ratio` < `0.9775` → IC=+0.472 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9775 (IC base=+0.202)

- **PATRÓN** `T_h` > `145.7785` → IC=+0.394 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7785 (IC base=+0.333)

- **PATRÓN** `ratio` > `1.0115` → IC=+0.290 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0115 (IC base=+0.333)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `122.1058` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 122.1058 (IC base=+0.180)

- **PATRÓN** `ratio` < `0.973` → IC=+0.448 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.180)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.289 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.284)

- **PATRÓN** `ratio` > `1.0468` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0468 (IC base=+0.284)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `93.6267` → IC=+0.278 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 93.6267 (IC base=+0.240)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.425 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.240)

- **PATRÓN** `T_h` > `105.6124` → IC=+0.327 (n=535)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 105.6124 (IC base=+0.314)

- **PATRÓN** `ratio` > `1.0151` → IC=+0.333 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0151 (IC base=+0.314)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1332` → IC=+0.459 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1332 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6087 sube el IC de +0.188 a +0.268 en UPDOWN_GBM#15min (n=1787). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.208 a +0.276 en UPDOWN_GBM#BTC#15min (n=395). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6586 sube el IC de +0.130 a +0.253 en UPDOWN_GBM#ETH#15min (n=370). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.171 a +0.255 en UPDOWN_GBM#SOL#15min (n=214). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5695 sube el IC de +0.196 a +0.286 en UPDOWN_GBM#XRP#15min (n=465). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1176 sube el IC de +0.053 a +0.150 en UPDOWN_GBM#XRP#15min (n=524). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6409 sube el IC de -0.068 a +0.273 en UPDOWN_GBM_15M_TARDIO (n=672). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.028 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1994). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7496 sube el IC de +0.081 a +0.334 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=191). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.213 sube el IC de -0.198 a +0.382 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6647 sube el IC de +0.149 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=319). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2722 sube el IC de +0.237 a +0.284 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=671). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9 sube el IC de -0.175 a +0.309 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3455 sube el IC de -0.042 a +0.258 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=341). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3391 sube el IC de -0.039 a +0.305 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=525). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8411 sube el IC de +0.292 a +0.329 en UPDOWN_GBM_IBS_ALTO (n=711). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.287 a +0.319 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=390). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8539 sube el IC de +0.295 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.349 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=442). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.354 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=245). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.743 sube el IC de +0.342 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=198). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.088 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1381 | +0.101 | +199.99€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1381 | +0.101 | +199.99€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 26 | +0.036 | -1.50€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1040 | +0.110 | +172.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1040 | +0.110 | +172.29€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 29742 | -0.083 | -3963.84€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1567 | -0.028 | -213.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 28175 | -0.086 | -3750.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3873 | -0.097 | -642.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3873 | -0.097 | -642.45€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1567 | -0.028 | -213.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1567 | -0.028 | -213.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3514 | -0.098 | -802.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3514 | -0.098 | -802.93€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7679 | -0.015 | -724.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7679 | -0.015 | -724.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7271 | -0.088 | -457.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7271 | -0.088 | -457.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5838 | -0.162 | -1123.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5838 | -0.162 | -1123.26€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 20336 | -0.025 | +3885.26€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5270 | +0.001 | +1794.16€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 15066 | -0.034 | +2091.10€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 20336 | -0.025 | +3885.26€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5270 | +0.001 | +1794.16€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 15066 | -0.034 | +2091.10€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 99502 | +0.113 | -4781.27€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14721 | +0.185 | -421.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 405 | -0.070 | -51.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 78008 | +0.101 | -4090.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6368 | +0.107 | -217.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 12967 | +0.099 | -1041.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 48 | -0.160 | +1.58€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 12904 | +0.101 | -1031.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 20053 | +0.132 | -336.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4618 | +0.202 | -127.53€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 12933 | +0.114 | -156.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2460 | +0.100 | -30.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13006 | +0.091 | -1157.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 54 | -0.107 | -8.00€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 12937 | +0.092 | -1138.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 21133 | +0.124 | -369.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5738 | +0.177 | -64.42€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13077 | +0.106 | -237.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2306 | +0.100 | -59.18€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 19364 | +0.114 | -1114.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4214 | +0.188 | -233.13€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 308 | -0.029 | +2.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13240 | +0.092 | -755.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1602 | +0.130 | -128.12€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 12979 | +0.100 | -761.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 49 | -0.029 | +9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 12917 | +0.101 | -770.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 15796 | +0.193 | -1013.75€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 15796 | +0.193 | -1013.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3741 | +0.167 | -391.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3741 | +0.167 | -391.83€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1440 | +0.202 | -9.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1440 | +0.202 | -9.30€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3680 | +0.180 | -310.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3680 | +0.180 | -310.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3247 | +0.240 | -104.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3247 | +0.240 | -104.48€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3609 | +0.193 | -211.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3609 | +0.193 | -211.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 746 | +0.429 | -21.63€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 746 | +0.429 | -21.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 291 | +0.439 | -2.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 291 | +0.439 | -2.35€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 282 | +0.430 | -7.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 282 | +0.430 | -7.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 163 | +0.409 | -9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 163 | +0.409 | -9.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 54590 | +0.198 | -4221.71€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 54590 | +0.198 | -4221.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9419 | +0.178 | -1063.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9419 | +0.178 | -1063.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 8732 | +0.223 | -314.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 8732 | +0.223 | -314.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9425 | +0.174 | -1099.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9425 | +0.174 | -1099.63€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 8827 | +0.218 | -353.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 8827 | +0.218 | -353.92€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9030 | +0.203 | -594.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9030 | +0.203 | -594.94€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9157 | +0.193 | -794.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9157 | +0.193 | -794.53€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 20642 | +0.117 | +161.99€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 20642 | +0.117 | +161.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10249 | +0.120 | +127.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10249 | +0.120 | +127.98€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10393 | +0.114 | +34.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10393 | +0.114 | +34.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1557 | +0.288 | -25.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1557 | +0.288 | -25.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 697 | +0.277 | -19.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 697 | +0.277 | -19.96€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 747 | +0.288 | -8.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 747 | +0.288 | -8.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 113 | +0.344 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 113 | +0.344 | +2.86€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 690 | +0.433 | -7.07€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 690 | +0.433 | -7.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 330 | +0.431 | -5.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 330 | +0.431 | -5.81€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 315 | +0.437 | -1.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 315 | +0.437 | -1.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1182 | +0.068 | -60.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 416 | +0.048 | -42.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 766 | +0.078 | -18.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 62 | +0.109 | +2.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 62 | +0.109 | +2.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 933 | +0.075 | -28.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 167 | +0.062 | -9.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 766 | +0.078 | -18.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 187 | +0.013 | -34.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 187 | +0.013 | -34.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 38694 | +0.098 | -1102.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3175 | +0.090 | +28.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 35519 | +0.099 | -1130.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 21627 | +0.103 | -302.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3175 | +0.090 | +28.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 18452 | +0.105 | -331.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7401 | +0.109 | -22.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7401 | +0.109 | -22.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9666 | +0.080 | -777.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9666 | +0.080 | -777.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 845 | +0.217 | -100.74€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 845 | +0.217 | -100.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 845 | +0.217 | -100.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 845 | +0.217 | -100.74€ | 2 | 4 |
| ✅ GBM_LATE_15M | 27515 | +0.085 | +13300.89€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 27515 | +0.085 | +13300.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4595 | +0.197 | +3426.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4595 | +0.197 | +3426.55€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 4086 | +0.179 | +2910.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4086 | +0.179 | +2910.37€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 4833 | +0.198 | +3611.34€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 4833 | +0.198 | +3611.34€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 3983 | +0.025 | +912.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 3983 | +0.025 | +912.03€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 3938 | -0.033 | +897.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3938 | -0.033 | +897.01€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6080 | -0.040 | +1543.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6080 | -0.040 | +1543.58€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 29262 | +0.086 | +15376.46€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 29262 | +0.086 | +15376.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5568 | +0.013 | +2912.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5568 | +0.013 | +2912.51€ | 2 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6109 | +0.015 | +1281.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6109 | +0.015 | +1281.94€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4160 | +0.265 | +4230.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4160 | +0.265 | +4230.32€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4814 | +0.005 | +936.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4814 | +0.005 | +936.38€ | 2 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4727 | +0.029 | +1820.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4727 | +0.029 | +1820.12€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 3884 | +0.279 | +4195.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 3884 | +0.279 | +4195.19€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 22073 | +0.170 | +16719.20€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 22073 | +0.170 | +16719.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3329 | +0.209 | +2682.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3329 | +0.209 | +2682.83€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3471 | +0.150 | +2561.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3471 | +0.150 | +2561.22€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3482 | +0.209 | +2783.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3482 | +0.209 | +2783.06€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3693 | +0.134 | +2615.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3693 | +0.134 | +2615.97€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4130 | +0.118 | +2911.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4130 | +0.118 | +2911.81€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 3968 | +0.205 | +3164.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 3968 | +0.205 | +3164.31€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 5712 | +0.136 | +2606.56€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 5712 | +0.136 | +2606.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1595 | +0.134 | +790.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1595 | +0.134 | +790.29€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1712 | +0.152 | +823.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1712 | +0.152 | +823.69€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1313 | +0.119 | +513.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1313 | +0.119 | +513.24€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 27656 | +0.178 | +20984.19€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 27656 | +0.178 | +20984.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4379 | +0.225 | +3767.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4379 | +0.225 | +3767.75€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4319 | +0.153 | +2894.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4319 | +0.153 | +2894.93€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4579 | +0.226 | +3952.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4579 | +0.226 | +3952.82€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4483 | +0.137 | +3106.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4483 | +0.137 | +3106.55€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 4840 | +0.117 | +3189.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 4840 | +0.117 | +3189.10€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5056 | +0.210 | +4073.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5056 | +0.210 | +4073.03€ | 0 | 23 |
| ✅ GBM_LATE_5M | 7731 | +0.163 | +4833.99€ | 1 | 28 |
| ✅ GBM_LATE_5M#5min | 7731 | +0.163 | +4833.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 758 | +0.221 | +637.63€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 758 | +0.221 | +637.63€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1831 | +0.151 | +1221.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1831 | +0.151 | +1221.83€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 893 | +0.170 | +564.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 893 | +0.170 | +564.35€ | 0 | 21 |
| ✅ GBM_LATE_5M#ETH | 2546 | +0.166 | +1571.90€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2546 | +0.166 | +1571.90€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 744 | +0.143 | +383.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 744 | +0.143 | +383.30€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 959 | +0.137 | +454.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 959 | +0.137 | +454.98€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1896 | +0.066 | +725.21€ | 2 | 12 |
| ✅ GBM_LATE_60M#60min | 1896 | +0.066 | +725.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 697 | +0.088 | +257.99€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 697 | +0.088 | +257.99€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 622 | +0.069 | +289.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 622 | +0.069 | +289.83€ | 3 | 15 |
| ✅ GBM_LATE_60M#SOL | 577 | +0.035 | +177.40€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 577 | +0.035 | +177.40€ | 2 | 9 |
| 🚫 GBM_LATE_60M_FADE | 397 | -0.257 | -21.97€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 397 | -0.257 | -21.97€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 150 | -0.224 | -7.63€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 150 | -0.224 | -7.63€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 131 | -0.259 | -7.49€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 131 | -0.259 | -7.49€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 116 | -0.288 | -6.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 116 | -0.288 | -6.85€ | 3 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 750 | +0.077 | +175.15€ | 2 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 750 | +0.077 | +175.15€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 294 | +0.068 | +61.28€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 294 | +0.068 | +61.28€ | 2 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 227 | +0.042 | +13.76€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 227 | +0.042 | +13.76€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 229 | +0.123 | +100.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 229 | +0.123 | +100.11€ | 2 | 12 |
| ✅ LATE_WINDOW_5MIN | 105 | +0.257 | +87.77€ | 0 | 10 |
| ✅ LATE_WINDOW_5MIN#5min | 105 | +0.257 | +87.77€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 105 | +0.257 | +87.77€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 105 | +0.257 | +87.77€ | 0 | 10 |
| ✅ LEADLAG_BTC_XRP_15M | 2169 | +0.106 | +604.11€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2169 | +0.106 | +604.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2169 | +0.106 | +604.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2169 | +0.106 | +604.11€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 394 | -0.076 | -33.23€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 394 | -0.076 | -33.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 101 | -0.053 | -4.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 101 | -0.053 | -4.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 144 | -0.021 | -4.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 144 | -0.021 | -4.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2129 | +0.010 | +27.78€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2129 | +0.010 | +27.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 111 | +0.031 | +1.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 111 | +0.031 | +1.36€ | 1 | 2 |
| ✅ LIQUIDACIONES_5M#BTC | 244 | -0.008 | +11.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 244 | -0.008 | +11.69€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 169 | -0.021 | -4.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 169 | -0.021 | -4.84€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 892 | +0.022 | +21.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 892 | +0.022 | +21.12€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 479 | +0.003 | -3.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 479 | +0.003 | -3.33€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 234 | +0.004 | +1.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 234 | +0.004 | +1.79€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M | 1148 | -0.043 | -26.15€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1148 | -0.043 | -26.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 325 | -0.044 | -13.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 325 | -0.044 | -13.92€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 388 | -0.026 | -0.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 388 | -0.026 | -0.47€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 435 | -0.056 | -11.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 435 | -0.056 | -11.76€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 2161 | -0.012 | +75.58€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1030 | -0.013 | +30.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1131 | -0.012 | +45.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 59 | +0.041 | +8.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 33 | +0.071 | +7.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 26 | +0.000 | +1.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 509 | +0.017 | +47.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 236 | +0.013 | +14.56€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 273 | +0.020 | +32.56€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 281 | -0.041 | -3.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 139 | -0.060 | -7.33€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 142 | -0.021 | +4.25€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 408 | -0.027 | -5.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 184 | -0.021 | +0.26€ | 3 | 3 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 224 | -0.031 | -5.73€ | 5 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 395 | -0.004 | +25.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 199 | -0.007 | +12.13€ | 2 | 4 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 196 | +0.000 | +12.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 509 | -0.026 | +3.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 239 | -0.019 | +3.25€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 270 | -0.033 | +0.29€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M | 14642 | -0.012 | -218.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14642 | -0.012 | -218.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3359 | -0.022 | -71.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3359 | -0.022 | -71.28€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 31447 | -0.006 | +1377.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 31447 | -0.006 | +1377.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5555 | +0.019 | +687.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5555 | +0.019 | +687.46€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4812 | -0.030 | -71.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4812 | -0.030 | -71.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5629 | +0.015 | +489.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5629 | +0.015 | +489.99€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4598 | -0.053 | -151.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4598 | -0.053 | -151.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5281 | -0.010 | +208.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5281 | -0.010 | +208.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5572 | +0.009 | +214.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5572 | +0.009 | +214.53€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 5994 | -0.060 | -149.44€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 5994 | -0.060 | -149.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1445 | -0.084 | -40.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1445 | -0.084 | -40.56€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 676 | -0.122 | -29.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 676 | -0.122 | -29.33€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1758 | -0.079 | -35.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1758 | -0.079 | -35.34€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3345 | +0.004 | -2.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1315 | +0.007 | +7.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1315 | +0.007 | +7.70€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 79412 | -0.073 | +1676.81€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 79412 | -0.073 | +1676.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 13469 | -0.078 | +781.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 13469 | -0.078 | +781.64€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12189 | -0.095 | -607.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12189 | -0.095 | -607.98€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 13742 | -0.067 | +722.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 13742 | -0.067 | +722.84€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 11718 | -0.093 | -225.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 11718 | -0.093 | -225.24€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 14505 | -0.048 | +389.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 14505 | -0.048 | +389.04€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 13789 | -0.063 | +616.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 13789 | -0.063 | +616.50€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7767 | -0.027 | -137.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7767 | -0.027 | -137.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1767 | -0.036 | -17.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1767 | -0.036 | -17.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2194 | -0.021 | -25.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2194 | -0.021 | -25.47€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1057 | -0.046 | -21.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1057 | -0.046 | -21.21€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 750 | -0.019 | -22.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 750 | -0.019 | -22.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1202 | +0.109 | +409.44€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1066 | +0.115 | +396.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 242 | +0.131 | +114.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 242 | +0.131 | +114.58€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 204 | +0.107 | +56.52€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 204 | +0.107 | +56.52€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 222 | +0.098 | +75.75€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 222 | +0.098 | +75.75€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 184 | +0.134 | +86.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 184 | +0.134 | +86.57€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 214 | +0.102 | +63.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 214 | +0.102 | +63.43€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 595 | -0.051 | -58.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 595 | -0.051 | -58.76€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 122 | -0.016 | +0.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 122 | -0.016 | +0.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 79 | -0.105 | -18.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 79 | -0.105 | -18.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 173 | -0.060 | -25.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 173 | -0.060 | -25.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 120 | -0.025 | -4.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 120 | -0.025 | -4.72€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 101 | -0.063 | -11.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 101 | -0.063 | -11.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 598 | -0.110 | -51.30€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 275 | -0.161 | -65.48€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 227 | -0.203 | -68.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 48 | +0.040 | +2.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 206 | -0.072 | +1.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 162 | -0.079 | -6.75€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 44 | -0.043 | +8.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 117 | -0.055 | +12.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 95 | -0.077 | +6.09€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 22 | +0.042 | +6.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 484 | -0.138 | -68.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 114 | +0.009 | +17.52€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 761 | -0.201 | -33.33€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 315 | -0.200 | -29.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 278 | -0.196 | -29.04€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 37 | -0.218 | -0.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 259 | -0.216 | -23.73€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 227 | -0.225 | -28.39€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 32 | -0.147 | +4.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 187 | -0.177 | +19.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 171 | -0.176 | +15.17€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 676 | -0.202 | -42.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 85 | -0.190 | +8.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 313 | +0.408 | +227.18€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 32 | +0.088 | -2.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 32 | +0.088 | -2.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 81 | +0.380 | +59.35€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 81 | +0.380 | +59.35€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 200 | +0.465 | +170.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 200 | +0.465 | +170.41€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 313 | +0.408 | +227.18€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 544 | +0.033 | +17.42€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 544 | +0.033 | +17.42€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 260 | +0.034 | +6.25€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 260 | +0.034 | +6.25€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 36 | +0.079 | +2.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 57 | -0.009 | -1.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 57 | -0.009 | -1.59€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 191 | +0.034 | +10.66€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 191 | +0.034 | +10.66€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2835 | -0.022 | -114.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2835 | -0.022 | -114.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 822 | -0.018 | -26.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 822 | -0.018 | -26.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 570 | -0.023 | -23.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 570 | -0.023 | -23.26€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1287 | -0.021 | -49.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1287 | -0.021 | -49.62€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 76 | -0.051 | -6.76€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 76 | -0.051 | -6.76€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 38 | +0.000 | -2.32€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 38 | +0.000 | -2.32€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8370 | +0.024 | +129.96€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8370 | +0.024 | +129.96€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2285 | +0.025 | +32.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2285 | +0.025 | +32.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1896 | +0.032 | +51.10€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1896 | +0.032 | +51.10€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2553 | +0.013 | +6.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2553 | +0.013 | +6.60€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1636 | +0.029 | +39.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1636 | +0.029 | +39.38€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7709 | +0.014 | -29.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7709 | +0.014 | -29.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3087 | +0.017 | -4.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3087 | +0.017 | -4.88€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3031 | +0.014 | -13.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3031 | +0.014 | -13.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1591 | +0.009 | -10.84€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1591 | +0.009 | -10.84€ | 2 | 0 |
| ✅ UPDOWN_GBM | 42303 | +0.034 | +2696.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11144 | +0.071 | +2096.23€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 1515 | +0.004 | +6.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 26933 | +0.025 | +576.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2553 | +0.001 | +19.51€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4373 | +0.074 | +529.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 789 | +0.160 | +340.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3551 | +0.056 | +190.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 7979 | +0.041 | +581.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1416 | +0.087 | +323.38€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 405 | +0.016 | +6.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 4946 | +0.040 | +223.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1152 | +0.003 | +27.57€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 60 | -0.097 | +0.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 4941 | +0.041 | +313.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 746 | +0.138 | +260.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4167 | +0.024 | +54.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 9145 | +0.023 | +367.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2807 | +0.049 | +306.71€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 397 | +0.006 | +7.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5032 | +0.016 | +60.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 857 | -0.003 | -9.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 52 | -0.130 | +3.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 9682 | +0.015 | +246.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2681 | +0.027 | +186.52€ | 0 | 12 |
| ✅ UPDOWN_GBM#SOL#240min | 389 | -0.004 | -2.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6024 | +0.013 | +64.70€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 544 | +0.005 | +1.46€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 44 | -0.174 | -3.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6181 | +0.040 | +659.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2705 | +0.086 | +678.72€ | 0 | 12 |
| ✅ UPDOWN_GBM#XRP#240min | 263 | -0.002 | -3.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3213 | +0.004 | -16.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 156 | -0.133 | +0.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 589 | +0.349 | +193.44€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 589 | +0.349 | +193.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 326 | +0.354 | +104.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 326 | +0.354 | +104.07€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 263 | +0.342 | +89.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 263 | +0.342 | +89.38€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 12957 | -0.036 | +2854.73€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 12957 | -0.036 | +2854.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 887 | -0.046 | +379.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2355 | -0.121 | +44.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2355 | -0.121 | +44.10€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 471 | +0.187 | +329.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1441 | +0.211 | +887.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1441 | +0.211 | +887.68€ | 1 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3888 | -0.065 | +576.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3888 | -0.065 | +576.15€ | 3 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3915 | -0.073 | +638.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3915 | -0.073 | +638.56€ | 3 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 148 | +0.040 | +8.49€ | 1 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 148 | +0.040 | +8.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 148 | +0.040 | +8.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 148 | +0.040 | +8.49€ | 1 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 948 | +0.292 | +756.31€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 948 | +0.292 | +756.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 520 | +0.287 | +395.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 520 | +0.287 | +395.43€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 428 | +0.295 | +360.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 428 | +0.295 | +360.87€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 736 | -0.113 | -84.24€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 736 | -0.113 | -84.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 216 | -0.083 | -16.24€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 216 | -0.083 | -16.24€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 71 | -0.199 | -8.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 71 | -0.199 | -8.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 4 | 0 |
| ✅ WEEKLY_PRICE | 2526 | +0.301 | +1260.63€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 876 | +0.252 | +123.78€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 954 | +0.291 | +411.49€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 696 | +0.377 | +725.36€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.058) — sin ventaja clara. oversold(IBS<0.3): IC=+0.048 n=14963 | neutral: IC=+0.032 n=15730 | overbought(IBS>0.7): IC=+0.090 n=15152
  - _Datos_: n=47475 IC=+0.057 PNL=+5931.80€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 554 celda(s) pasan gate riguroso completo de 2298 evaluadas (n>=40) y 3272 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.027 < 0.08 — monitorear
  - _Datos_: n=2681 IC=+0.027 PNL=+186.52€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=954/15 IC=+0.291 PNL=+411.49€ | BTC: n=876/15 IC=+0.252 PNL=+123.78€ | SOL: n=696/15 IC=+0.377 PNL=+725.36€

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
  - _Estado_: 42241 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.125 n=382/60 | contraria IC=+0.166 n=357 | gap=-0.041 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=316, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 184 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=857/40 IC=-0.003 PNL=-9.51€ | BTC#60min: n=1152/40 IC=+0.003 PNL=+27.57€ | SOL#60min: n=544/40 IC=+0.005 PNL=+1.46€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=363056 | tras_1loss IC=+0.081 n=280778 | tras_2loss IC=+0.051 n=117488/40 | gap=-0.001 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.015 n=4970 | contrario_BTC IC=+0.032 n=4436/40 | gap=+0.017 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.188 > 0.08 con n=363 PNL=+236.61€
  - _Datos_: n=363 IC=+0.188 PNL=+236.61€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.213 > 0.08 con n=427 PNL=+319.55€
  - _Datos_: n=427 IC=+0.213 PNL=+319.55€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.239 > 0.08 con n=44 PNL=+32.90€
  - _Datos_: n=44 IC=+0.239 PNL=+32.90€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.329 > 0.1 con n=2064 PNL=+1148.56€
  - _Datos_: n=2064 IC=+0.329 PNL=+1148.56€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=328 IC=+0.064 PNL=+33.41€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=328 IC=+0.064 PNL=+33.41€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=55 IC=+0.184 PNL=+36.05€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=55 IC=+0.184 PNL=+36.05€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=40429 IC=+0.034 PNL=+2566.78€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=40429 IC=+0.034 PNL=+2566.78€

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
  - _Estado_: n=1780 IC=+0.007 PNL=+1.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1780 IC=+0.007 PNL=+1.26€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=773 IC=-0.011 PNL=+18.25€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=773 IC=-0.011 PNL=+18.25€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=549 IC=+0.025 PNL=+29.38€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=549 IC=+0.025 PNL=+29.38€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.188 > 0.1 con n=2382 PNL=+1509.58€
  - _Datos_: n=2382 IC=+0.188 PNL=+1509.58€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1351 IC=+0.055 PNL=+101.97€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1351 IC=+0.055 PNL=+101.97€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1416 IC=+0.087 PNL=+323.38€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1416 IC=+0.087 PNL=+323.38€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=6347 PNL=+1542.11€
  - _Datos_: n=6347 IC=+0.086 PNL=+1542.11€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=160 IC=-0.235 PNL=-0.68€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=160 IC=-0.235 PNL=-0.68€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=278 IC=-0.043 PNL=-6.04€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=278 IC=-0.043 PNL=-6.04€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=587 IC=+0.021 PNL=+42.06€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=587 IC=+0.021 PNL=+42.06€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=59 IC=+0.074 PNL=+5.01€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=59 IC=+0.074 PNL=+5.01€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6110 IC=-0.001 PNL=-0.09€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6110 IC=-0.001 PNL=-0.09€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.257 n=105) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=105 IC=+0.257 PNL=+87.77€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=7896 IC=+0.039 PNL=+520.17€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=7896 IC=+0.039 PNL=+520.17€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2624 IC=+0.058 PNL=+329.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2624 IC=+0.058 PNL=+329.74€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.110 > 0.08 con n=383 PNL=+116.16€
  - _Datos_: n=383 IC=+0.110 PNL=+116.16€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.151 > 0.08 con n=660 PNL=+173.32€
  - _Datos_: n=660 IC=+0.151 PNL=+173.32€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=499 PNL=+233.05€
  - _Datos_: n=499 IC=+0.113 PNL=+233.05€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=54936 IC=+0.117 PNL=+20080.99€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=54936 IC=+0.117 PNL=+20080.99€

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
  - _Estado_: n=6289 IC=+0.041 PNL=+479.75€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6289 IC=+0.041 PNL=+479.75€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=682 PNL=+255.02€
  - _Datos_: n=682 IC=+0.118 PNL=+255.02€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=147 IC=-0.044 PNL=+35.89€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=147 IC=-0.044 PNL=+35.89€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.447 > 0.1 con n=1195 PNL=+1185.53€
  - _Datos_: n=1195 IC=+0.447 PNL=+1185.53€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=15229 IC=+0.056 PNL=+1841.66€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=15229 IC=+0.056 PNL=+1841.66€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.1 con n=3867 PNL=+2117.51€
  - _Datos_: n=3867 IC=+0.203 PNL=+2117.51€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.143 < -0.1 con n=253 PNL=+29.57€
  - _Datos_: n=253 IC=-0.143 PNL=+29.57€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2085 IC=+0.053 PNL=+223.26€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2085 IC=+0.053 PNL=+223.26€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=86 IC=-0.136 PNL=+1.62€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=86 IC=-0.136 PNL=+1.62€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.1 con n=466 PNL=+137.16€
  - _Datos_: n=466 IC=+0.128 PNL=+137.16€

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
  - _Estado_: n=19548 IC=-0.138 PNL=+1248.78€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=19548 IC=-0.138 PNL=+1248.78€

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
  - _Estado_: n=2071 IC=+0.140 PNL=+1174.71€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2071 IC=+0.140 PNL=+1174.71€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=2343 PNL=+1496.95€
  - _Datos_: n=2343 IC=+0.189 PNL=+1496.95€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=4411 IC=+0.024 PNL=+160.09€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4411 IC=+0.024 PNL=+160.09€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=2216 PNL=+1164.12€
  - _Datos_: n=2216 IC=+0.086 PNL=+1164.12€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.208 > 0.08 con n=525 PNL=+267.72€
  - _Datos_: n=525 IC=+0.208 PNL=+267.72€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.239 < -0.1 con n=1922 PNL=-228.33€
  - _Datos_: n=1922 IC=-0.239 PNL=-228.33€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=5753 IC=+0.173 PNL=+3902.78€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=5753 IC=+0.173 PNL=+3902.78€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=79 PNL=+29.34€
  - _Datos_: n=79 IC=+0.105 PNL=+29.34€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2117 IC=+0.067 PNL=+623.43€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2117 IC=+0.067 PNL=+623.43€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.183 > 0.08 con n=1927 PNL=+1382.68€
  - _Datos_: n=1927 IC=+0.183 PNL=+1382.68€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3193 IC=-0.031 PNL=+832.30€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3193 IC=-0.031 PNL=+832.30€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.086 > 0.08 con n=577 PNL=-55.49€
  - _Datos_: n=577 IC=+0.086 PNL=-55.49€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.238 > 0.08 con n=3462 PNL=-306.27€
  - _Datos_: n=3462 IC=+0.238 PNL=-306.27€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.103 n=1099) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1099 IC=+0.103 PNL=+268.25€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.347 > 0.08 con n=286 PNL=+106.22€
  - _Datos_: n=286 IC=+0.347 PNL=+106.22€

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
  - _Estado_: n=9419 IC=+0.178 PNL=-1063.91€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=9419 IC=+0.178 PNL=-1063.91€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.197 > 0.1 con n=150 PNL=+88.34€
  - _Datos_: n=150 IC=+0.197 PNL=+88.34€
