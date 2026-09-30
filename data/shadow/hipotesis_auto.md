# Hipótesis automáticas — 2026-09-30 00:41 UTC
_Generado por shadow_postmortem.py sobre 674004 resoluciones (PNL=+79308.65€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=545)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.236 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `74.0` → IC=+0.213 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 74.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.8033` → IC=+0.255 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8033 (IC base=+0.139)

- **PATRÓN** `banda_z` > `9.568` → IC=+0.205 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.568 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.157 (n=395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=608)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4766.038` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4766.038 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.125 (n=545)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.137 (n=202)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 93.0 (IC base=+0.058)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=410)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.239 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.148)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.148)

- **PATRÓN** `banda_hit_calibrado` > `0.7998` → IC=+0.266 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7998 (IC base=+0.148)

- **PATRÓN** `banda_z` > `4.287` → IC=+0.170 (n=459)

  - _Acción_: Kelly boost +0.85€ cuando `banda_z` > 4.287 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.169 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 11.0 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=518)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `3317.318` → IC=+0.153 (n=306)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3317.318 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `8317.7389` → IC=+0.122 (n=231)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 8317.7389 (IC base=+0.062)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.154 (n=163)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 94.0 (IC base=+0.062)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.214 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=101)

- **FILTRO** `banda_hit_calibrado` < `0.6297` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.6297
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=90)

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
- **FILTRO** `restante_s_al_confirmar` < `145.74` → IC=-0.217 (n=7666)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.74
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=22999)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `137.45` → IC=-0.246 (n=996)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.45
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=2988)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `127.67` → IC=-0.304 (n=898)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.67
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=2695)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.29` → IC=-0.204 (n=1874)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.29
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=5625)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `126.74` → IC=-0.331 (n=1502)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 126.74
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=4507)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.209 (n=15027)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=3696)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5585.0055` → IC=+0.176 (n=2377)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 5585.0055 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=12868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=15529)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.230 (n=12036)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=6026)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7768.3763` → IC=+0.170 (n=2295)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 7768.3763 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=1738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.206 (n=1782)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=2243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `15944.5355` → IC=+0.235 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15944.5355 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.200 (n=1610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=1792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.262 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2293)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `15889.5889` → IC=+0.215 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15889.5889 (IC base=+0.196)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.170 (n=353)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.615 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.137 (n=243)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.095)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.144 (n=389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 7.0 (IC base=+0.100)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=872)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `5784.0902` → IC=+0.155 (n=227)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 5784.0902 (IC base=+0.100)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=3091)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=2623)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.150)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.349 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.366 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.233 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `4240.0828` → IC=+0.229 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4240.0828 (IC base=+0.228)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.136 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.251 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=592)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1317.494` → IC=+0.147 (n=729)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1317.494 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.077)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.404 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.154 (n=1162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` < `0.285` → IC=+0.308 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.285 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=773)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.01 (IC base=+0.152)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.369 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.167)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `1222.0032` → IC=+0.155 (n=233)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1222.0032 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.222 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.117)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.205 (n=12193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.201 (n=12249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.230 (n=4128)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `3571.1845` → IC=+0.331 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3571.1845 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.172 (n=2906)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.173 (n=2905)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 17.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.177 (n=2930)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.169)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.249 (n=1113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.246 (n=1097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.351 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.243)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.189 (n=2862)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=2874)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2439)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=2663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.327 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.307 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.243)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=2947)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.192 (n=2825)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.194 (n=2216)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.192 (n=1089)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.73 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=590)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `11452.1989` → IC=+0.459 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11452.1989 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.444 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.446 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.453 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_liquidez` > `14422.037` → IC=+0.448 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14422.037 (IC base=+0.441)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=38375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.237 (n=16897)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.180 (n=6604)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5268)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7178)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=6910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.264 (n=3906)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=6988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=6957)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=3469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=2362)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=6366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2522)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=6414)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.242 (n=2945)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=5809)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.18` → IC=+0.124 (n=5406)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.18 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5501)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=7135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.58` → IC=+0.137 (n=5404)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.58 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=2920)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.15` → IC=+0.124 (n=2689)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.15 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=2720)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.134 (n=3090)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.26` → IC=+0.138 (n=2688)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.26 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.186 (n=2889)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=3043)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.136 (n=2725)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=863)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.380 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1547.5346` → IC=+0.294 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1547.5346 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.345 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5084.4032` → IC=+0.312 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5084.4032 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.286)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.295 (n=608)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `1447.4658` → IC=+0.303 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1447.4658 (IC base=+0.286)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=534)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.435 (n=472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.436 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.439 (n=228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.435 (n=260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.435 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.445 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.455 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.439 (n=291)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=60)

- **FILTRO** `py_entrada` > `0.76` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=53)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=60)

- **FILTRO** `py_entrada` > `0.76` → IC=-0.357 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=53)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4922` → IC=+0.128 (n=9089)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4922 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.9831` → IC=+0.243 (n=3030)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9831 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.258 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2197 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.974` → IC=+0.180 (n=3460)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.974 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.854` → IC=+0.252 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.854 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` > `0.6157` → IC=+0.254 (n=2509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6157 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.226 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` > `1.8946` → IC=+0.211 (n=4203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8946 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.5699` → IC=+0.135 (n=11028)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5699 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.6109` → IC=+0.204 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6109 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.697` → IC=+0.185 (n=1737)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.697 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.8687` → IC=+0.178 (n=2628)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8687 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.224 (n=1892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.4504` → IC=+0.199 (n=6722)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.4504 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.213 (n=6523)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=+0.068)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.203 (n=682)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.174 (n=679)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0081 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.3528` → IC=+0.175 (n=2032)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3528 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.174 (n=1360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 11.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.164` → IC=+0.270 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.164 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.208 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.171 (n=1911)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.186 (n=2056)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.04 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.243 (n=1430)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0915` → IC=+0.279 (n=531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0915 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=1445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0531` → IC=+0.287 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0531 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.551` → IC=+0.242 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.551 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.459` → IC=+0.243 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.459 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.230 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.277 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6054` → IC=+0.246 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6054 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1661.62` → IC=+0.248 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1661.62 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.237 (n=705)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3547` → IC=+0.228 (n=1594)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3547 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=1600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.220 (n=1618)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.9844` → IC=+0.267 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9844 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.1319` → IC=+0.223 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1319 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.572` → IC=+0.255 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.572 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2524` → IC=+0.222 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2524 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `1.0826` → IC=+0.226 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0826 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.237 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `1.7515` → IC=+0.219 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7515 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.368` → IC=+0.236 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.368 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11016.3169` → IC=+0.224 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11016.3169 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.165 (n=1087)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0038 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.165 (n=545)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=731)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.3332` → IC=+0.193 (n=1085)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.3332 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.361` → IC=+0.165 (n=258)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.361 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.345` → IC=+0.142 (n=1497)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.345 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2117` → IC=+0.149 (n=1627)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2117 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8602` → IC=+0.140 (n=1085)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 0.8602 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1566` → IC=+0.179 (n=428)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1566 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4267` → IC=+0.152 (n=1517)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4267 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.148 (n=1011)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `14029.1139` → IC=+0.142 (n=1085)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 14029.1139 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `230.0` → IC=+0.172 (n=632)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 230.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.212 (n=679)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=2037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=1823)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.266 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.253 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.194 (n=1783)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.200 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.7731` → IC=+0.196 (n=1739)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7731 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2420)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `1917.4584` → IC=+0.189 (n=923)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 1917.4584 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.220 (n=1565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.6287` → IC=+0.213 (n=1778)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6287 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=827)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.0636` → IC=+0.239 (n=784)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0636 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.68` → IC=+0.228 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.68 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.534` → IC=+0.211 (n=1924)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.534 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3484` → IC=+0.251 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3484 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.7379` → IC=+0.207 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7379 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `3.2453` → IC=+0.225 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2453 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1911.3596` → IC=+0.215 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.3596 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.211 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.209)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=111)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=2459)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.150 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0037 (IC base=+0.039)

- **PATRÓN** `ibs_20min` > `0.9545` → IC=+0.223 (n=395)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9545 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1962` → IC=+0.336 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1962 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.846` → IC=+0.172 (n=806)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.846 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.339 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.039)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.340 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.358 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.039)

- **PATRÓN** `volumen_spike_ratio` > `2.1967` → IC=+0.330 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1967 (IC base=+0.039)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.334 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.039)

- **PATRÓN** `ibs_20min` < `0.1024` → IC=+0.150 (n=643)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1024 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.6725` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6725 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.6116` → IC=+0.162 (n=326)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6116 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `1.1641` → IC=+0.151 (n=325)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.1641 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2304` → IC=+0.205 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2304 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.5242` → IC=+0.166 (n=824)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5242 (IC base=+0.022)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.176 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=373)

- **FILTRO** `ibs_20min` < `0.3056` → IC=-0.205 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3056
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=332)

- **FILTRO** `ibs_20min` > `0.2432` → IC=-0.124 (n=2459)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2432
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=1214)

- **FILTRO** `sigma_ewma_delta_pct` > `8.692` → IC=-0.208 (n=389)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.692
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3284)

- **PATRÓN** `ibs_20min` > `0.6129` → IC=+0.164 (n=221)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.6129 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `1.695` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.695 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` < `0.6571` → IC=+0.285 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6571 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `1.0233` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0233 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.283 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4963 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `1.4704` → IC=+0.266 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4704 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.292 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.2432` → IC=+0.127 (n=1214)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.2432 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7288` → IC=+0.250 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7288 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.4579` → IC=+0.235 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4579 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.6727` → IC=+0.278 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6727 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.289 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.281 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6579` → IC=-0.182 (n=636)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6579
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1915)

- **FILTRO** `ibs_20min` < `0.7218` → IC=-0.157 (n=1683)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7218
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=868)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.207 (n=564)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1987)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.209 (n=939)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=2864)

- **PATRÓN** `dist_vwap_pct` > `0.4705` → IC=+0.327 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4705 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2845` → IC=+0.316 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2845 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.313 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6229 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.303 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.4163` → IC=+0.304 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4163 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.7985` → IC=+0.302 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7985 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5676` → IC=+0.281 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5676 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` < `0.7283` → IC=+0.256 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7283 (IC base=-0.018)

- **PATRÓN** `volumen_regimen` > `1.2494` → IC=+0.285 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2494 (IC base=-0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.099` → IC=+0.268 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.099 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` < `2.1396` → IC=+0.265 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1396 (IC base=-0.018)

- **PATRÓN** `volumen_spike_ratio` > `1.5237` → IC=+0.256 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5237 (IC base=-0.018)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.196 (n=3894)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0097 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4741` → IC=+0.186 (n=10426)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4741 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.0302` → IC=+0.290 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0302 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.633` → IC=+0.158 (n=5376)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.633 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1795` → IC=+0.243 (n=4201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1795 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6901` → IC=+0.253 (n=3752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6901 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2924` → IC=+0.268 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2924 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.4628` → IC=+0.240 (n=2265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4628 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6398` → IC=+0.251 (n=2264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6398 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.272 (n=6313)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.166 (n=3810)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0091 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5472` → IC=+0.155 (n=10043)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5472 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.7234` → IC=+0.249 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7234 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2531` → IC=+0.245 (n=3279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2531 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7088` → IC=+0.246 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7088 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.2033` → IC=+0.254 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2033 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2416` → IC=+0.304 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2416 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5955` → IC=+0.269 (n=2043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5955 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2846` → IC=+0.264 (n=2104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2846 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.274 (n=4535)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2541` → IC=-0.151 (n=806)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2541
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=2419)

- **FILTRO** `ibs_20min` > `0.7566` → IC=-0.149 (n=660)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7566
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1983)

- **FILTRO** `sigma_ewma_delta_pct` > `4.536` → IC=-0.166 (n=602)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.536
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=2041)

- **PATRÓN** `ibs_20min` > `0.8969` → IC=+0.268 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8969 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.89` → IC=+0.206 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.89 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.2239` → IC=+0.259 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2239 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` < `1.4395` → IC=+0.194 (n=344)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4395 (IC base=+0.042)

- **PATRÓN** `volumen_spike_ratio` > `2.1623` → IC=+0.216 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1623 (IC base=+0.042)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.211 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.042)

- **PATRÓN** `volumen_pendiente_norm` < `0.2221` → IC=+0.436 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2221 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.1478` → IC=+0.439 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1478 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.4701` → IC=+0.439 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4701 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.1202` → IC=+0.434 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1202 (IC base=-0.020)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.479 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8671` → IC=+0.166 (n=782)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8671 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.2995` → IC=+0.183 (n=414)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.2995 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.6758` → IC=+0.179 (n=967)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6758 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.234 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.197 (n=354)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.3919` → IC=+0.174 (n=354)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.3919 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.211 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 236.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.222 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.003)

- **PATRÓN** `volumen_regimen` > `0.8583` → IC=+0.231 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8583 (IC base=+0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2677` → IC=+0.302 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2677 (IC base=+0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.242 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.003)

- **PATRÓN** `ballena_activa_n` < `456.0` → IC=+0.219 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 456.0 (IC base=+0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.281 (n=1202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.255 (n=1816)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.251 (n=1815)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.678` → IC=+0.282 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.678 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.0999` → IC=+0.265 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0999 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.1944` → IC=+0.262 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1944 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.263 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `1913.32` → IC=+0.263 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.32 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.313 (n=671)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.295 (n=651)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.325 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.290 (n=1479)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.283)

- **PATRÓN** `ibs_20min` > `0.0909` → IC=+0.283 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0909 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.689` → IC=+0.290 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.689 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.765` → IC=+0.285 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.765 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.1194` → IC=+0.289 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1194 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.5811` → IC=+0.295 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5811 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.6774` → IC=+0.292 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6774 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.288 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `1904.5592` → IC=+0.298 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.5592 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.286 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.283)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7739` → IC=-0.184 (n=679)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7739
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=2040)

- **PATRÓN** `ibs_20min` > `0.9105` → IC=+0.186 (n=590)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.9105 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.1901` → IC=+0.234 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1901 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `0.9991` → IC=+0.244 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9991 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.081` → IC=+0.257 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.081 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.262 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.7573` → IC=+0.241 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7573 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.256 (n=683)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.221 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1534 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.1649` → IC=+0.213 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1649 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2771` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2771 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.260 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8106 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.237 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.263 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 136.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.75` → IC=-0.189 (n=1227)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.279 (n=1246)

- **FILTRO** `ibs_20min` > `0.6792` → IC=-0.234 (n=622)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6792
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=1873)

- **FILTRO** `sigma_ewma_delta_pct` > `4.704` → IC=-0.191 (n=544)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.704
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1951)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.279 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.75 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `1.1001` → IC=+0.326 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1001 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.659` → IC=+0.165 (n=389)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 9.659 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.86` → IC=+0.307 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.86 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` > `0.6364` → IC=+0.300 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6364 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.298 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.4355` → IC=+0.325 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4355 (IC base=+0.047)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.326 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.5778` → IC=+0.126 (n=1647)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.5778 (IC base=+0.019)

- **PATRÓN** `dist_vwap_pct` < `0.4821` → IC=+0.227 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4821 (IC base=+0.019)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.259 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.222 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.233 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `2.46` → IC=+0.241 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.46 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.253 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.019)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.324 (n=1324)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.279)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.285 (n=1554)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.279)

- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.321 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7391 (IC base=+0.279)

- **PATRÓN** `dist_vwap_pct` > `0.2191` → IC=+0.313 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2191 (IC base=+0.279)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.672` → IC=+0.300 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.672 (IC base=+0.279)

- **PATRÓN** `volumen_regimen` > `0.8606` → IC=+0.304 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8606 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` < `0.0784` → IC=+0.283 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0784 (IC base=+0.279)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.325 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.279)

- **PATRÓN** `volumen_spike_ratio` > `1.429` → IC=+0.288 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.429 (IC base=+0.279)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `2457.7909` → IC=+0.287 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2457.7909 (IC base=+0.279)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.317 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.279)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.307 (n=1053)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.1975` → IC=+0.289 (n=694)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1975 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.292 (n=541)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.281 (n=783)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.1379` → IC=+0.332 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1379 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.3237` → IC=+0.289 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3237 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` < `0.2332` → IC=+0.281 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2332 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.095` → IC=+0.304 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.095 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.284 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `1.2435` → IC=+0.311 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2435 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.330 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `2.4899` → IC=+0.279 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4899 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.1415` → IC=+0.279 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1415 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2404.9954` → IC=+0.284 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2404.9954 (IC base=+0.280)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.179 (n=2956)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0048 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.203 (n=2948)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.364` → IC=+0.177 (n=7780)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.364 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=9262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.221 (n=8851)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1772` → IC=+0.194 (n=3797)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1772 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.364` → IC=+0.250 (n=1788)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.364 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.2063` → IC=+0.163 (n=5878)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2063 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.161 (n=5880)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6279 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1046` → IC=+0.189 (n=3452)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1046 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.559` → IC=+0.169 (n=3738)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.559 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6045` → IC=+0.175 (n=2831)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6045 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `1946.335` → IC=+0.171 (n=7896)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1946.335 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.183 (n=7748)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 109.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.185 (n=5688)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0821` → IC=+0.213 (n=2841)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0821 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=3281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.4831` → IC=+0.225 (n=8521)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4831 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.342` → IC=+0.199 (n=1434)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.342 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.1769` → IC=+0.157 (n=6121)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1769 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2918` → IC=+0.215 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2918 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5584` → IC=+0.172 (n=3445)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5584 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6119` → IC=+0.172 (n=2610)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6119 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.179 (n=7485)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 109.0 (IC base=+0.170)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.228 (n=498)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.189)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.193 (n=497)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0082 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3425` → IC=+0.212 (n=1484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3425 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.194 (n=1486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.196 (n=990)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.137` → IC=+0.307 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.137 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.239 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.4343` → IC=+0.187 (n=1380)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.4343 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.203 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.243 (n=997)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.245 (n=1014)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.1866` → IC=+0.287 (n=755)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1866 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=1013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=561)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.3455` → IC=+0.259 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3455 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.317` → IC=+0.248 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.317 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.099` → IC=+0.234 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.099 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.258 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4248` → IC=+0.259 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4248 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1552.26` → IC=+0.249 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1552.26 (IC base=+0.237)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.238 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.162)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.194 (n=442)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=1332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` > `0.3965` → IC=+0.227 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3965 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.1998` → IC=+0.208 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1998 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.506` → IC=+0.228 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.506 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.2487` → IC=+0.166 (n=1324)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2487 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.206 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `1.5031` → IC=+0.180 (n=566)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5031 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `11845.601` → IC=+0.168 (n=1183)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 11845.601 (IC base=+0.162)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.159 (n=1413)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.2932` → IC=+0.164 (n=1413)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2932 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.583` → IC=+0.189 (n=1413)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.583 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.943` → IC=+0.211 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.943 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.215` → IC=+0.157 (n=1413)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.215 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1571` → IC=+0.150 (n=432)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1571 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4453` → IC=+0.147 (n=1301)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4453 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.137 (n=1301)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4236 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `210.0` → IC=+0.168 (n=408)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 210.0 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.215 (n=985)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.2476` → IC=+0.219 (n=985)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2476 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.210 (n=1543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.296 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.435` → IC=+0.273 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.435 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2015` → IC=+0.208 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2015 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.7959` → IC=+0.203 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7959 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.7447` → IC=+0.212 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7447 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.211 (n=1744)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `1913.4832` → IC=+0.202 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1913.4832 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.234 (n=1117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1435` → IC=+0.254 (n=558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1435 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.275 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.245 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.666` → IC=+0.254 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.666 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.354` → IC=+0.252 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.354 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7487` → IC=+0.222 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7487 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.1786` → IC=+0.225 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1786 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1908.66` → IC=+0.223 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.66 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.212 (n=773)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.217)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.177 (n=1247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0066 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.161 (n=1417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1486)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3605` → IC=+0.199 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3605 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1549` → IC=+0.180 (n=925)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1549 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.953` → IC=+0.219 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.953 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8529` → IC=+0.157 (n=945)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8529 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.145 (n=1417)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6188 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1008` → IC=+0.186 (n=600)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1008 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.160 (n=462)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.166 (n=462)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `5305.4954` → IC=+0.187 (n=945)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 5305.4954 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.150 (n=1357)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 158.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.157 (n=1493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3872` → IC=+0.146 (n=1493)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3872 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=583)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6524` → IC=+0.171 (n=1493)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6524 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.165 (n=526)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8536` → IC=+0.151 (n=996)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8536 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.174 (n=222)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8095` → IC=+0.140 (n=913)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.8095 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.524` → IC=+0.127 (n=456)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.524 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `9568.5341` → IC=+0.164 (n=677)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 9568.5341 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.124 (n=1311)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 155.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.157 (n=732)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0101 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.5098` → IC=+0.209 (n=1611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5098 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.2883` → IC=+0.187 (n=893)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2883 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.821` → IC=+0.252 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.821 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.132 (n=1612)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2036 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.126 (n=1617)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.0708` → IC=+0.125 (n=675)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0708 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.5437` → IC=+0.135 (n=685)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.5437 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1681)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2878.9982` → IC=+0.200 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2878.9982 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.139 (n=1260)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 48.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.163 (n=722)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0062 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1059` → IC=+0.170 (n=546)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1059 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5741` → IC=+0.214 (n=1637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5741 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.145 (n=1512)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.13` → IC=+0.137 (n=265)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 9.13 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6359` → IC=+0.148 (n=546)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6359 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.163 (n=286)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4538` → IC=+0.143 (n=496)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4538 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.135 (n=496)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2734.9583` → IC=+0.168 (n=742)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2734.9583 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.125 (n=1426)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 52.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.227 (n=1364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.183` → IC=+0.205 (n=672)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.183 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=1600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.6491` → IC=+0.245 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6491 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.5326` → IC=+0.214 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5326 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.588` → IC=+0.236 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.588 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.1976` → IC=+0.206 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1976 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.214 (n=1527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.262 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `2.47` → IC=+0.214 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.47 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.7978` → IC=+0.210 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7978 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.208 (n=1537)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2435.8884` → IC=+0.203 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2435.8884 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.230 (n=527)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0175` → IC=+0.210 (n=1053)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0175 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.230 (n=528)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.210 (n=729)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.0196` → IC=+0.298 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0196 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `1.2417` → IC=+0.226 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2417 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.388` → IC=+0.248 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.388 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.6338` → IC=+0.218 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6338 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.282 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `2.199` → IC=+0.201 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.199 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.205 (n=1436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2375.5796` → IC=+0.214 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2375.5796 (IC base=+0.208)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.193 (n=758)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.160)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.169 (n=759)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0086 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.3484` → IC=+0.168 (n=2000)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.3484 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.202 (n=1141)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.5122` → IC=+0.197 (n=2030)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5122 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.8241` → IC=+0.177 (n=366)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.8241 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.731` → IC=+0.187 (n=1002)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.731 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `0.8708` → IC=+0.183 (n=1359)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8708 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` > `1.2058` → IC=+0.168 (n=679)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.2058 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.1627` → IC=+0.174 (n=618)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1627 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.175 (n=734)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.8205` → IC=+0.164 (n=1467)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8205 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.166 (n=2584)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `2666.351` → IC=+0.166 (n=2030)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2666.351 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.176 (n=2053)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 147.0 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.141 (n=1557)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0056 (IC base=+0.114)

- **PATRÓN** `drift_60min` |x|≤ `0.3462` → IC=+0.129 (n=2051)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3462 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=2192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.114)

- **PATRÓN** `ibs_20min` < `0.0568` → IC=+0.191 (n=777)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.0568 (IC base=+0.114)

- **PATRÓN** `volumen_regimen` < `1.2231` → IC=+0.122 (n=2125)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2231 (IC base=+0.114)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.141 (n=577)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.114)

- **PATRÓN** `volumen_spike_ratio` < `1.4453` → IC=+0.155 (n=751)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4453 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `3921.3253` → IC=+0.127 (n=1553)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3921.3253 (IC base=+0.114)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.134 (n=969)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 28.0 (IC base=+0.114)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.172 (n=257)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0029 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.3342` → IC=+0.153 (n=583)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.3342 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.178 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.6562` → IC=+0.203 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6562 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.2886` → IC=+0.162 (n=199)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.2886 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.1629` → IC=+0.136 (n=511)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1629 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.203` → IC=+0.154 (n=261)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.203 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.865` → IC=+0.135 (n=604)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 6.865 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.6219` → IC=+0.190 (n=195)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6219 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` < `0.1544` → IC=+0.136 (n=607)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1544 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0908` → IC=+0.149 (n=206)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0908 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.1928` → IC=+0.145 (n=499)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1928 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.5042` → IC=+0.137 (n=507)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.5042 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=753)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `10581.1275` → IC=+0.151 (n=582)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 10581.1275 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `164.0` → IC=+0.161 (n=246)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 164.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.202 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3426` → IC=+0.156 (n=728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.3426 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.149 (n=698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` < `0.6186` → IC=+0.176 (n=641)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.6186 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1832` → IC=+0.150 (n=718)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1832 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.437` → IC=+0.150 (n=272)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.437 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.177` → IC=+0.137 (n=665)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.177 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.2216` → IC=+0.144 (n=728)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 1.2216 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.7151` → IC=+0.149 (n=650)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7151 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.207 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1022` → IC=+0.155 (n=632)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1022 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.407` → IC=+0.142 (n=718)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.407 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `308.0` → IC=+0.149 (n=613)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 308.0 (IC base=+0.136)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.270 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.4065` → IC=+0.213 (n=716)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4065 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.956` → IC=+0.272 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.956 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.152` → IC=+0.214 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.152 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.93` → IC=+0.236 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.93 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `0.8331` → IC=+0.215 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8331 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.1649` → IC=+0.230 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1649 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.1004` → IC=+0.248 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1004 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4055` → IC=+0.227 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4055 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `2.4379` → IC=+0.239 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4379 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.0837` → IC=+0.152 (n=225)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.0837 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6874` → IC=+0.141 (n=296)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.6874 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2234` → IC=+0.139 (n=106)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2234 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.151 (n=503)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0058 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.5425` → IC=+0.140 (n=562)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.5425 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.176 (n=522)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 8.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.260 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `1.0116` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0116 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.496` → IC=+0.187 (n=292)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.496 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `1.0674` → IC=+0.157 (n=494)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0674 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `0.7162` → IC=+0.147 (n=502)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7162 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.1748` → IC=+0.158 (n=156)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.1748 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.4787` → IC=+0.139 (n=181)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4787 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.2114` → IC=+0.168 (n=245)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.2114 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=591)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `3102.4188` → IC=+0.193 (n=187)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3102.4188 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.0441` → IC=+0.240 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0441 (IC base=+0.101)

- **PATRÓN** `volumen_regimen` < `1.2218` → IC=+0.125 (n=523)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 1.2218 (IC base=+0.101)

- **PATRÓN** `volumen_spike_ratio` < `1.8403` → IC=+0.170 (n=331)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.8403 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `2922.5748` → IC=+0.148 (n=237)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2922.5748 (IC base=+0.101)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.144 (n=473)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 40.0 (IC base=+0.101)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.176 (n=3829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0047 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.209 (n=3814)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=11987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.219 (n=11441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.9408` → IC=+0.202 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9408 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.36` → IC=+0.243 (n=2846)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.36 (IC base=+0.174)

- **PATRÓN** `volumen_regimen` < `0.8788` → IC=+0.170 (n=5109)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8788 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.197 (n=1559)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.5852` → IC=+0.193 (n=3676)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.5852 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `1784.7206` → IC=+0.178 (n=11436)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1784.7206 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.199 (n=8875)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.197 (n=4563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1507` → IC=+0.192 (n=4551)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1507 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=3928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.4483` → IC=+0.246 (n=9099)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4483 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2539` → IC=+0.163 (n=6458)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2539 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.07` → IC=+0.206 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.07 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.754` → IC=+0.183 (n=9980)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 3.754 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.7044` → IC=+0.164 (n=3103)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7044 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2889` → IC=+0.241 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2889 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6067` → IC=+0.192 (n=3193)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6067 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.200 (n=6216)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.183)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.230 (n=639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.216 (n=636)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.3603` → IC=+0.202 (n=1908)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3603 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.219 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.201 (n=1285)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.331 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.634` → IC=+0.348 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.634 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.2273` → IC=+0.252 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2273 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.561` → IC=+0.205 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.561 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.262 (n=1032)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.258)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.263 (n=1549)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1275` → IC=+0.286 (n=680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1275 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=1401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.3544` → IC=+0.282 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3544 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.502` → IC=+0.261 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.502 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2841` → IC=+0.294 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2841 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` < `1.5513` → IC=+0.258 (n=630)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5513 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.6218` → IC=+0.275 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6218 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.260 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1662.78` → IC=+0.270 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1662.78 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.210 (n=611)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1128` → IC=+0.163 (n=806)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1128 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1924)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.3033` → IC=+0.207 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3033 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.185 (n=1024)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.173 (n=405)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.169` → IC=+0.158 (n=1668)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.169 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.6277` → IC=+0.183 (n=611)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6277 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2668` → IC=+0.188 (n=267)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2668 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.1124` → IC=+0.164 (n=1562)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.1124 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.159 (n=1776)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `11232.4092` → IC=+0.161 (n=1636)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11232.4092 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `280.0` → IC=+0.177 (n=756)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 280.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.164 (n=1564)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0057 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.165 (n=1377)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=708)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.2835` → IC=+0.236 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2835 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.6644` → IC=+0.152 (n=248)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6644 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.534` → IC=+0.177 (n=261)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.534 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.2003` → IC=+0.162 (n=1564)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2003 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1514` → IC=+0.202 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1514 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.3977` → IC=+0.157 (n=1466)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.3977 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.7588` → IC=+0.162 (n=977)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7588 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `413.0` → IC=+0.152 (n=1207)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 413.0 (IC base=+0.149)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.260 (n=622)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.228 (n=1866)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=1887)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.349` → IC=+0.299 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.349 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.1336` → IC=+0.222 (n=1711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1336 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.7706` → IC=+0.229 (n=1598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7706 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1917.5696` → IC=+0.226 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.5696 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.237 (n=1748)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.6056` → IC=+0.235 (n=1748)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6056 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=665)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.235 (n=821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.013` → IC=+0.300 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.013 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.806` → IC=+0.276 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.806 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3404` → IC=+0.295 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3404 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7308` → IC=+0.229 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7308 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.1534` → IC=+0.239 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1534 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1908.1032` → IC=+0.245 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.1032 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.232 (n=1544)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.193 (n=652)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4376` → IC=+0.150 (n=1955)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4376 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.2821` → IC=+0.186 (n=1955)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.2821 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3732` → IC=+0.160 (n=757)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3732 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.181` → IC=+0.159 (n=801)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 4.181 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8693` → IC=+0.159 (n=1304)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.8693 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.206 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5207` → IC=+0.152 (n=835)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5207 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1553` → IC=+0.157 (n=860)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1553 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7649.1944` → IC=+0.239 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7649.1944 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.175 (n=619)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 74.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.170 (n=1059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0052 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.3585` → IC=+0.143 (n=1394)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3585 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.1452` → IC=+0.260 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1452 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.305` → IC=+0.175 (n=235)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.305 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.148 (n=697)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6971 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` > `1.2017` → IC=+0.132 (n=528)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.2017 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.224 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.444` → IC=+0.141 (n=1510)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.444 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6504.6367` → IC=+0.190 (n=718)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6504.6367 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.135 (n=1325)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 147.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.142 (n=1300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0081 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2010)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.195 (n=1949)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.4667 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.0841` → IC=+0.207 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0841 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.559` → IC=+0.234 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.559 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.8889` → IC=+0.143 (n=1299)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8889 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.123 (n=1996)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.1945` → IC=+0.132 (n=859)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.1945 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=1970)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2529.0124` → IC=+0.241 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2529.0124 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.141 (n=1523)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 52.0 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.179 (n=622)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0058 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.136` → IC=+0.161 (n=621)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.136 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=689)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6343` → IC=+0.207 (n=1862)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6343 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.223` → IC=+0.136 (n=1538)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.223 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.469` → IC=+0.128 (n=1792)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.469 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.7141` → IC=+0.159 (n=820)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7141 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2212` → IC=+0.178 (n=290)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2212 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4382` → IC=+0.150 (n=566)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4382 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2756.4844` → IC=+0.184 (n=621)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2756.4844 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.132 (n=1488)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.231 (n=1724)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=2025)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.214 (n=1725)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.262 (n=1730)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.2192` → IC=+0.233 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2192 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.251 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` < `1.243` → IC=+0.216 (n=1930)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.243 (IC base=+0.213)

- **PATRÓN** `volumen_regimen` > `0.6408` → IC=+0.222 (n=1929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6408 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.2342` → IC=+0.243 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2342 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.5001` → IC=+0.234 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5001 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `2432.4268` → IC=+0.220 (n=1724)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2432.4268 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.225 (n=681)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.226 (n=680)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.221 (n=1441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.42` → IC=+0.265 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.42 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `1.2452` → IC=+0.211 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2452 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.2206` → IC=+0.212 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2206 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.266 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `1.2355` → IC=+0.239 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2355 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.270 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `2.1818` → IC=+0.204 (n=1629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1818 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.205 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2381.2305` → IC=+0.210 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2381.2305 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.198 (n=1759)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 37.0 (IC base=+0.208)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=3504)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.191 (n=3069)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0091 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.5146` → IC=+0.186 (n=3485)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.5146 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=1335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.179 (n=1575)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.9458` → IC=+0.239 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9458 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1865` → IC=+0.186 (n=1259)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1865 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` < `0.4802` → IC=+0.173 (n=2232)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.4802 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.2` → IC=+0.205 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.2 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `0.7046` → IC=+0.175 (n=1029)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.7046 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `0.8915` → IC=+0.178 (n=1559)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8915 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.169` → IC=+0.206 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.169 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.184 (n=1148)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.8667` → IC=+0.184 (n=2295)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.8667 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2520)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `2469.463` → IC=+0.181 (n=3485)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2469.463 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.206 (n=885)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.3889` → IC=+0.177 (n=2323)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3889 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=940)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.175 (n=1190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.1824` → IC=+0.182 (n=1162)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1824 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.6876` → IC=+0.175 (n=494)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.6876 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.184` → IC=+0.167 (n=2634)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.184 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `1.2537` → IC=+0.160 (n=2476)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2537 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.162 (n=2404)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.5395` → IC=+0.165 (n=1147)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5395 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.8251` → IC=+0.165 (n=1738)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 1.8251 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=3504)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `4873.1789` → IC=+0.158 (n=2358)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 4873.1789 (IC base=+0.156)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.162 (n=1718)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 83.0 (IC base=+0.156)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.201 (n=376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.183 (n=380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0033 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.0866` → IC=+0.236 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0866 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.191 (n=189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 8.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.5544` → IC=+0.206 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5544 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.2017` → IC=+0.186 (n=368)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.2017 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.33` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 10.33 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.191 (n=451)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` > `0.5792` → IC=+0.199 (n=426)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 0.5792 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.208 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.5955` → IC=+0.201 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5955 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `12545.7532` → IC=+0.220 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12545.7532 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.217 (n=426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3673` → IC=+0.154 (n=968)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3673 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.173 (n=371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.181 (n=427)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1409 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.6124` → IC=+0.146 (n=439)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6124 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.6916` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6916 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.369` → IC=+0.163 (n=948)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.369 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8795` → IC=+0.187 (n=646)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8795 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0686` → IC=+0.168 (n=450)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.0686 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.42` → IC=+0.145 (n=322)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.42 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.825` → IC=+0.153 (n=643)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.825 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `14904.1418` → IC=+0.160 (n=439)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 14904.1418 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `707.0` → IC=+0.144 (n=922)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 707.0 (IC base=+0.140)

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

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.237)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.209 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.3786` → IC=+0.188 (n=971)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3786 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.186 (n=489)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5313` → IC=+0.195 (n=736)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5313 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.8859` → IC=+0.195 (n=368)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.8859 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.219` → IC=+0.191 (n=922)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.219 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.221` → IC=+0.193 (n=989)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 4.221 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.0828` → IC=+0.184 (n=971)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.0828 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.183 (n=1016)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.1657` → IC=+0.197 (n=331)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1657 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `2.4736` → IC=+0.187 (n=1084)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.4736 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=1103)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.210 (n=301)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.187 (n=898)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.165 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 11.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.7538` → IC=+0.168 (n=898)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.7538 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.0937` → IC=+0.168 (n=898)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.0937 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.6108` → IC=+0.185 (n=195)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6108 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.392` → IC=+0.169 (n=811)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 4.392 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.6434` → IC=+0.199 (n=300)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.6434 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `0.7218` → IC=+0.163 (n=802)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.7218 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.164 (n=839)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.175 (n=380)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `2.1956` → IC=+0.177 (n=775)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 2.1956 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `7806.8621` → IC=+0.182 (n=802)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 7806.8621 (IC base=+0.161)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.188 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0089 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.3752` → IC=+0.150 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.3752 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.172 (n=349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 3.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.152 (n=357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 14.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.9404` → IC=+0.247 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9404 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.2317` → IC=+0.196 (n=235)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.2317 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8924` → IC=+0.179 (n=235)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.8924 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `1.2654` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.2654 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.7834` → IC=+0.194 (n=227)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7834 (IC base=+0.150)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=418)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.02 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `2999.8942` → IC=+0.175 (n=352)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2999.8942 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.173 (n=295)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 51.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.189 (n=294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0068 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.6953` → IC=+0.177 (n=295)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.6953 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.189 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 10.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` < `0.125` → IC=+0.233 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.125 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.6481` → IC=+0.221 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6481 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.315` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.315 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.203` → IC=+0.163 (n=286)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 5.203 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `1.3789` → IC=+0.167 (n=295)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.3789 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.218 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.6109` → IC=+0.182 (n=127)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.6109 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.167 (n=130)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.157)

- **PATRÓN** `libro_liquidez` > `3188.7067` → IC=+0.196 (n=294)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3188.7067 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.201 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.157)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.185 (n=144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=434)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.175 (n=475)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0039 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.125 (n=985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6459` → IC=+0.186 (n=879)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.6459 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.146 (n=524)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.429` → IC=+0.191 (n=231)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.429 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.194 (n=132)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `1378.8357` → IC=+0.121 (n=640)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1378.8357 (IC base=+0.085)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.122 (n=382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0056 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.0455` → IC=+0.306 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0455 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1871` → IC=+0.141 (n=402)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1871 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.104` → IC=+0.147 (n=137)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 3.104 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.1368` → IC=+0.216 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1368 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.5035` → IC=+0.157 (n=298)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.5035 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.4395` → IC=+0.145 (n=266)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4395 (IC base=+0.040)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.142 (n=305)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `3560.4084` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3560.4084 (IC base=+0.040)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.211 (n=164)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.098)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.121 (n=381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.098)

- **PATRÓN** `ibs_20min` > `0.4419` → IC=+0.172 (n=339)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4419 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1288` → IC=+0.167 (n=175)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1288 (IC base=+0.098)

- **PATRÓN** `volumen_spike_ratio` < `2.0731` → IC=+0.147 (n=264)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.0731 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.143 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0044 (IC base=+0.089)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.185 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.089)

- **PATRÓN** `ibs_20min` < `0.279` → IC=+0.259 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.279 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` < `0.0677` → IC=+0.149 (n=172)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.0677 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.069` → IC=+0.187 (n=161)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 7.069 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` < `0.6161` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6161 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.8156` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.8156 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.0669` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0669 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `2.3987` → IC=+0.188 (n=142)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.3987 (IC base=+0.089)

- **PATRÓN** `libro_liquidez` > `3607.5216` → IC=+0.157 (n=103)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3607.5216 (IC base=+0.089)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6816` → IC=-0.130 (n=144)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6816
  - _Potencial_: sin este filtro IC_bueno=+0.222 (n=293)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=139)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.141 (n=240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0049 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.6816` → IC=+0.222 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6816 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.3463` → IC=+0.197 (n=130)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3463 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.74` → IC=+0.286 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.74 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `1133.0595` → IC=+0.156 (n=289)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 1133.0595 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.1674` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1674 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1303` → IC=+0.140 (n=112)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1303 (IC base=+0.011)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.256` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.256 (IC base=+0.011)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.558` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.558 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.1312` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1312 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.3281` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.3281 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.1755` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.1755 (IC base=+0.011)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.011)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=115)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=104)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=76)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.132 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0061 (IC base=+0.060)

- **PATRÓN** `ibs_20min` > `0.7805` → IC=+0.185 (n=211)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7805 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `1.0195` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 1.0195 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.144` → IC=+0.148 (n=89)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.144 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.2436` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2436 (IC base=+0.060)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.217 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=-0.010)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.244 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=-0.010)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.815` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.815 (IC base=-0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.0903` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0903 (IC base=-0.010)

- **PATRÓN** `volumen_spike_ratio` < `2.1906` → IC=+0.144 (n=57)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1906 (IC base=-0.010)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4444 (IC base=-0.010)

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

- **FILTRO** `sigma_h` > `0.005` → IC=-0.361 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=125)

- **FILTRO** `drift_60min` |x|> `0.2175` → IC=-0.308 (n=45)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2175
  - _Potencial_: sin este filtro IC_bueno=-0.255 (n=137)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=167)

- **FILTRO** `volumen_pendiente_norm` > `0.0812` → IC=-0.389 (n=16)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0812
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=86)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.250 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=39)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.275 (n=38)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=39)

- **FILTRO** `volumen_regimen` > `0.9045` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.9045
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=59)

- **FILTRO** `volumen_spike_ratio` > `1.4666` → IC=-0.333 (n=22)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.4666
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=23)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5777` → IC=-0.460 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5777
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=48)

- **FILTRO** `volumen_spike_ratio` > `2.5041` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.5041
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=30)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.389 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=51)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=47)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.375 (n=22)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=45)

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
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.169 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0059 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.6438` → IC=+0.150 (n=295)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6438 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.7229` → IC=+0.191 (n=53)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.7229 (IC base=+0.087)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.127 (n=306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.006 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.194 (n=269)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.1558 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.734` → IC=+0.189 (n=88)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 8.734 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` < `2.6401` → IC=+0.137 (n=232)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.6401 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `1.5807` → IC=+0.132 (n=207)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.5807 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.123 (n=322)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `3925.9695` → IC=+0.209 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3925.9695 (IC base=+0.092)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=101)

- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=93)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.188 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0034 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.222 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.220 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.0995` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.0995 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.794` → IC=+0.167 (n=127)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.794 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.1737` → IC=+0.164 (n=141)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1737 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.212 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.5892` → IC=+0.212 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5892 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.4639` → IC=+0.185 (n=109)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4639 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4433.8504` → IC=+0.177 (n=94)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 4433.8504 (IC base=+0.151)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `libro_liquidez` < `1457.1387` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `libro_liquidez` < 1457.1387
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=76)

- **PATRÓN** `sigma_h` < `0.0024` → IC=+0.175 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0024 (IC base=+0.013)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.135 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0053 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.149 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 12.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1558 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` < `0.1615` → IC=+0.124 (n=107)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1615 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.769` → IC=+0.306 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.769 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `0.9961` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.9961 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.0713` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.0713 (IC base=+0.091)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=77)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `2175.2667` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2175.2667 (IC base=+0.091)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1837` → IC=-0.159 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1837
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=43)

- **FILTRO** `dist_vwap_pct` > `0.2902` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2902
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.268 (n=80)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.269 (n=106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.231 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` < `0.9474` → IC=+0.253 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9474 (IC base=+0.230)

- **PATRÓN** `dist_vwap_pct` > `0.6943` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6943 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.257 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.305 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.240 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.040)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3583` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3583 (IC base=+0.232)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.232)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.232)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.333 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.232)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3583` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3583 (IC base=+0.232)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.232)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.232)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.333 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `1750.0` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1750.0 (IC base=+0.232)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=825)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2902.476` → IC=+0.157 (n=284)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2902.476 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2428.3902` → IC=+0.121 (n=788)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2428.3902 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=825)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2902.476` → IC=+0.157 (n=284)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2902.476 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2428.3902` → IC=+0.121 (n=788)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2428.3902 (IC base=+0.102)

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
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=223)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=209)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=91)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=2092)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=94)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=51)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=83)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=94)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=91)

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

- **PATRÓN** `liq_usd_total` > `105211.46` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `liq_usd_total` > 105211.46 (IC base=+0.024)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.139 (n=117)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=+0.024)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=892)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=846)

- **FILTRO** `liq_usd_total` < `12056.79` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `liq_usd_total` < 12056.79
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9855` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.318 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `ballena_activa_n` > `142.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 142.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=487)

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
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=212)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.495 (IC base=+0.022)

- **PATRÓN** `libro_liquidez` > `3990.7434` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3990.7434 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=697)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=697)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=425)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=425)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=189)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=189)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.127 (n=81)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=123)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.129 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=73)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=102)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=126)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=230)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=108)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=111)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=263)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=263)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=151)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.142 (n=442)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=1124)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.141 (n=51)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=139)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.5 (IC base=+0.032)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.56` → IC=+0.144 (n=102)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.56 (IC base=+0.056)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.186 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=69)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.147 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 9.0 (IC base=+0.089)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.135 (n=94)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.218 (n=37)

- **FILTRO** `profundidad_ratio` < `54.8` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.8
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=88)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.274 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=111)

- **FILTRO** `profundidad_ratio` < `19.0` → IC=-0.146 (n=46)

  - _Acción_: SKIP cuando `profundidad_ratio` < 19.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=94)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.53 (IC base=-0.034)

- **PATRÓN** `py_entrada` < `0.47` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.47 (IC base=-0.035)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.324 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=138)

- **FILTRO** `restante_min` < `3.79` → IC=-0.236 (n=85)

  - _Acción_: SKIP cuando `restante_min` < 3.79
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=85)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.185 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=118)

- **FILTRO** `lag_apertura_s` > `95.78` → IC=-0.280 (n=57)

  - _Acción_: SKIP cuando `lag_apertura_s` > 95.78
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=113)

- **PATRÓN** `profundidad_ratio` > `49.7` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `profundidad_ratio` > 49.7 (IC base=+0.057)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **PATRÓN** `restante_min` > `13.42` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `restante_min` > 13.42 (IC base=+0.007)

- **PATRÓN** `lag_apertura_s` < `93.77` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 93.77 (IC base=+0.007)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.150 (n=118)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.171 (n=68)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.5 (IC base=-0.032)

- **PATRÓN** `profundidad_ratio` > `19.7` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `profundidad_ratio` > 19.7 (IC base=+0.023)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.262 (n=61)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=156)

- **FILTRO** `lag_apertura_s` > `102.62` → IC=-0.127 (n=73)

  - _Acción_: SKIP cuando `lag_apertura_s` > 102.62
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=144)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.166 (n=3994)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=12220)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.162 (n=4104)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=12719)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.200 (n=699)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=2142)

- **PATRÓN** `libro_liquidez` > `1563.8324` → IC=+0.136 (n=1023)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1563.8324 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.180 (n=708)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=2191)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=721)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=2314)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.170 (n=692)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2142)

- **PATRÓN** `libro_liquidez` > `2577.5669` → IC=+0.121 (n=964)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2577.5669 (IC base=+0.022)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2224)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2351)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3091)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=411)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=402)

- **FILTRO** `libro_liquidez` < `17036.5309` → IC=-0.147 (n=230)

  - _Acción_: SKIP cuando `libro_liquidez` < 17036.5309
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=692)

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

- **FILTRO** `drift_7min_pct` |x|> `0.0331` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0331
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=19)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=11292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=25467)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=9160)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=27599)

- **FILTRO** `ibs_7min` < `0.27` → IC=-0.235 (n=9187)

  - _Acción_: SKIP cuando `ibs_7min` < 0.27
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=27572)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=12240)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=24519)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.232 (n=11395)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=35157)

- **FILTRO** `ibs_7min` > `0.2917` → IC=-0.180 (n=11622)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2917
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=34930)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.140 (n=1838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4325)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=1475)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4688)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.254 (n=2033)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=4130)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.177 (n=1471)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4692)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.262 (n=1982)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=6042)

- **FILTRO** `ibs_7min` > `0.7925` → IC=-0.210 (n=2005)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7925
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=6019)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=1479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=4832)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=1540)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4771)

- **FILTRO** `ibs_7min` < `0.7467` → IC=-0.197 (n=1577)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7467
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4734)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.180 (n=1576)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4735)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=1486)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4947)

- **FILTRO** `ibs_7min` > `0.2612` → IC=-0.184 (n=1608)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2612
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4825)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.182 (n=1600)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4833)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=1434)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=4431)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.304 (n=1463)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=4402)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.244 (n=1929)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=3936)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.209 (n=1426)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4439)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.246 (n=1981)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=6603)

- **FILTRO** `ibs_7min` > `0.75` → IC=-0.176 (n=2139)

  - _Acción_: SKIP cuando `ibs_7min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=6445)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=1941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=4114)

- **FILTRO** `py_entrada` < `0.37` → IC=-0.235 (n=1777)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=4278)

- **FILTRO** `ibs_7min` < `0.741` → IC=-0.182 (n=1513)

  - _Acción_: SKIP cuando `ibs_7min` < 0.741
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=4542)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.174 (n=1455)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4600)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.257 (n=1547)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4674)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.178 (n=1555)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4666)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.181 (n=1511)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4710)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.264 (n=1513)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4805)

- **FILTRO** `ibs_7min` < `0.2727` → IC=-0.234 (n=1576)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=4742)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.171 (n=2206)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=6680)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.270 (n=1495)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4552)

- **FILTRO** `ibs_7min` < `0.2781` → IC=-0.224 (n=1511)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2781
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=4536)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1430)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=4617)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.208 (n=1975)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=6429)

- **FILTRO** `ibs_7min` > `0.29` → IC=-0.163 (n=2096)

  - _Acción_: SKIP cuando `ibs_7min` > 0.29
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=6308)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=1162)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=578)

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
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=577)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.133 (n=829)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.66€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.117)

- **PATRÓN** `total_vol_5m` < `464.449` → IC=+0.149 (n=277)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 464.449 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `55.0` → IC=+0.123 (n=701)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 55.0 (IC base=+0.117)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4061` → IC=+0.133 (n=167)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.4061 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.204 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `445.688` → IC=+0.135 (n=165)

  - _Acción_: Kelly boost +0.67€ cuando `total_vol_5m` < 445.688 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2352.9473` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2352.9473 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 14.0 (IC base=+0.134)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 11.0 (IC base=+0.112)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.186 (n=116)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.183 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 16.0 (IC base=+0.107)

- **PATRÓN** `total_vol_5m` < `390.044` → IC=+0.222 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 390.044 (IC base=+0.107)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 73.0 (IC base=+0.107)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.167 (n=145)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.186 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 11.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `5032.488` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 5032.488 (IC base=+0.126)

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
- **FILTRO** `pct_vs_K` |x|> `3.7081` → IC=-0.291 (n=108)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.7081
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=330)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.238 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=35)

- **FILTRO** `T_h` > `98.7549` → IC=-0.414 (n=33)

  - _Acción_: SKIP cuando `T_h` > 98.7549
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=103)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.109)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0063` → IC=-0.226 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0063
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=21)

- **FILTRO** `T_h` > `123.7153` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `T_h` > 123.7153
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=61)

- **FILTRO** `T_h` < `51.359` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `T_h` < 51.359
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=55)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0088` → IC=-0.176 (n=282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=146)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.328 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=275)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.328 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=275)

- **FILTRO** `T_h` > `61.3189` → IC=-0.315 (n=274)

  - _Acción_: SKIP cuando `T_h` > 61.3189
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=92)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `63.9952` → IC=-0.149 (n=112)

  - _Acción_: SKIP cuando `T_h` > 63.9952
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=38)

- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.372 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=113)

- **FILTRO** `T_h` > `144.5168` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `T_h` > 144.5168
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=104)

- **FILTRO** `pct_vs_K` |x|> `2.9891` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9891
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=93)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` < `87.9866` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `T_h` < 87.9866
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=81)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.333 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=87)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.333 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=87)

- **FILTRO** `T_h` > `57.801` → IC=-0.335 (n=77)

  - _Acción_: SKIP cuando `T_h` > 57.801
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=38)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `T_h` > `135.6166` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `T_h` > 135.6166
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=80)

- **FILTRO** `pct_vs_K` |x|> `3.8` → IC=-0.230 (n=35)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=71)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.375 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=19)

- **FILTRO** `T_h` > `54.2531` → IC=-0.375 (n=54)

  - _Acción_: SKIP cuando `T_h` > 54.2531
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=19)

- **PATRÓN** `pct_vs_K` |x|≤ `1.0286` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.0286 (IC base=-0.046)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1357` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1357 (IC base=+0.356)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.381 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.356)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.411 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.356)

- **PATRÓN** `T_h` > `0.4742` → IC=+0.396 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4742 (IC base=+0.356)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.356)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.385 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.356)

- **PATRÓN** `edge` > `0.096` → IC=+0.452 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.431 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.418)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.447 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.418)

- **PATRÓN** `T_h` < `0.608` → IC=+0.430 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.608 (IC base=+0.418)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.448 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.4085` → IC=+0.482 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4085 (IC base=+0.418)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.474 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.418)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1072` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.400 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.452 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.417)

- **PATRÓN** `T_h` < `0.8618` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8618 (IC base=+0.417)

- **PATRÓN** `T_h` > `0.5062` → IC=+0.397 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5062 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.417)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.409 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.429 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.448)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.474 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.448)

- **PATRÓN** `T_h` < `1.0409` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0409 (IC base=+0.448)

- **PATRÓN** `T_h` > `0.8566` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8566 (IC base=+0.448)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.466 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.448)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.448)

- **PATRÓN** `edge` > `0.1155` → IC=+0.470 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.487 (n=74)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.463)

- **PATRÓN** `T_h` > `0.8021` → IC=+0.465 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8021 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4939` → IC=+0.487 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4939 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.468 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=210)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=315)

- **FILTRO** `streak_estiramiento` > `0.8469` → IC=-0.171 (n=68)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8469
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=206)

- **PATRÓN** `streak_estiramiento` < `0.4787` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.4787 (IC base=+0.033)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=458)

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
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=688)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1248)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=842)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=820)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3153)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1594)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1602)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.204 (n=620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.230 (n=620)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.072` → IC=+0.199 (n=819)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.072 (IC base=+0.190)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2172` → IC=+0.199 (n=620)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2172 (IC base=+0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1267` → IC=+0.233 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1267 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=1865)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.191 (n=1927)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_15` > `0.6129` → IC=+0.270 (n=1859)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6129 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.1207` → IC=+0.189 (n=936)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1207 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.77` → IC=+0.279 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.77 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `8803.312` → IC=+0.199 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8803.312 (IC base=+0.190)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=789)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.226 (n=367)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.275 (n=140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `0.3838` → IC=+0.218 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3838 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.245 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.211)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4` → IC=+0.246 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.245 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` > `0.7141` → IC=+0.276 (n=417)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7141 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.3854` → IC=+0.271 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3854 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.385` → IC=+0.285 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.385 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.245 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.211)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.418` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.418
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=480)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6586` → IC=-0.122 (n=191)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6586
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=390)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.182 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0035 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.135 (n=291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.005 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0672` → IC=+0.155 (n=192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0672 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2346` → IC=+0.176 (n=146)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio_macro` |x|> 0.2346 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.163 (n=161)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=320)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.141 (n=457)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.6586` → IC=+0.258 (n=390)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6586 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.148 (n=345)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.257` → IC=+0.226 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.257 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4204.0039` → IC=+0.138 (n=291)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 4204.0039 (IC base=+0.133)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=132)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.289 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.1804` → IC=+0.193 (n=223)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1804 (IC base=+0.174)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0592` → IC=+0.188 (n=222)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.0592 (IC base=+0.174)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3238` → IC=+0.223 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3238 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.175 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.174)

- **PATRÓN** `ibs_15` > `0.6` → IC=+0.259 (n=222)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1256` → IC=+0.180 (n=123)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1256 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.177 (n=218)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.265` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.265 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.173 (n=246)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `3074.419` → IC=+0.267 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3074.419 (IC base=+0.174)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.210 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.174)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.6834` → IC=-0.160 (n=104)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6834
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=1191)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.936` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.936 (IC base=-0.006)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0234` → IC=+0.276 (n=159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.226 (n=210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.198)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0403` → IC=+0.201 (n=476)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0403 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0848` → IC=+0.267 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0848 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.231 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.5728` → IC=+0.287 (n=476)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5728 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1419` → IC=+0.204 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1419 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.104` → IC=+0.222 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.104 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.797` → IC=+0.200 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.797 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2911.0954` → IC=+0.276 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2911.0954 (IC base=+0.198)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.145 (n=539)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.73€ cuando `ibs_15` < 0.1176 (IC base=+0.054)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.355 (n=308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.351)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.378 (n=154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.351)

- **PATRÓN** `drift_60min` |x|≤ `0.1114` → IC=+0.352 (n=308)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1114 (IC base=+0.351)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0699` → IC=+0.364 (n=461)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0699 (IC base=+0.351)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1326` → IC=+0.387 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1326 (IC base=+0.351)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.369 (n=473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.351)

- **PATRÓN** `ibs_15` > `0.7872` → IC=+0.390 (n=462)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7872 (IC base=+0.351)

- **PATRÓN** `dist_vwap_pct` > `0.4265` → IC=+0.386 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4265 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.361 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.954` → IC=+0.351 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.954 (IC base=+0.351)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.353 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.351)

- **PATRÓN** `libro_liquidez` > `3813.5418` → IC=+0.367 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3813.5418 (IC base=+0.351)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.366 (n=170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.356)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.374 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.356)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.374 (n=85)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.356)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.368 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.356)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0739` → IC=+0.367 (n=253)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0739 (IC base=+0.356)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1241` → IC=+0.388 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1241 (IC base=+0.356)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.356)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.387 (n=254)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.356)

- **PATRÓN** `dist_vwap_pct` > `0.3926` → IC=+0.396 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3926 (IC base=+0.356)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.364 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.356)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.357 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.356)

- **PATRÓN** `libro_liquidez` > `11247.6748` → IC=+0.371 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11247.6748 (IC base=+0.356)

- **PATRÓN** `ballena_activa_n` < `568.0` → IC=+0.399 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 568.0 (IC base=+0.356)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.376 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.342)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.351 (n=139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.342)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.367 (n=186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.342)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.369 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.342)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.402 (n=100)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.342)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.395 (n=208)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.342)

- **PATRÓN** `dist_vwap_pct` < `0.1227` → IC=+0.344 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1227 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.981` → IC=+0.356 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.981 (IC base=+0.342)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.696` → IC=+0.346 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.696 (IC base=+0.342)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.345 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.342)

- **PATRÓN** `libro_liquidez` > `4304.5454` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4304.5454 (IC base=+0.342)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.222 (n=729)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2191)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.205 (n=1005)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1915)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.237 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.6423` → IC=+0.271 (n=709)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6423 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2726` → IC=+0.189 (n=576)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2726 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.122` → IC=+0.251 (n=1395)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.122 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1809` → IC=+0.245 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1809 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.275 (n=2094)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.6898` → IC=+0.301 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6898 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.216 (n=445)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=1337)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.223 (n=445)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1337)

- **FILTRO** `sigma_ewma_delta_pct` > `23.3` → IC=-0.259 (n=247)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.3
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1535)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.157 (n=173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0028 (IC base=+0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2023` → IC=+0.283 (n=95)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2023 (IC base=+0.084)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1378` → IC=+0.322 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1378 (IC base=+0.084)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.123 (n=356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.084)

- **PATRÓN** `ibs_15` > `0.7503` → IC=+0.325 (n=209)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7503 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1319` → IC=+0.289 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1319 (IC base=+0.084)

- **PATRÓN** `ibs_15` < `0.199` → IC=+0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.199 (IC base=-0.196)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.196)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=432)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.152 (n=337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0067 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.163 (n=301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.004 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.209 (n=149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.145)

- **PATRÓN** `drift_15min` |x|≤ `0.4169` → IC=+0.178 (n=113)

  - _Acción_: Kelly boost +0.89€ cuando `drift_15min` |x|≤ 0.4169 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.147 (n=301)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.221 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.6625` → IC=+0.258 (n=337)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6625 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1109` → IC=+0.176 (n=242)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1109 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=432)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `10832.9607` → IC=+0.177 (n=153)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 10832.9607 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.248 (n=819)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.445` → IC=+0.237 (n=819)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.445 (IC base=+0.232)

- **PATRÓN** `drift_15min` |x|≤ `0.4781` → IC=+0.255 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4781 (IC base=+0.232)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2084` → IC=+0.248 (n=371)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2084 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.240 (n=310)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.232)

- **PATRÓN** `ibs_15` < `0.2756` → IC=+0.277 (n=721)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2756 (IC base=+0.232)

- **PATRÓN** `dist_vwap_pct` > `0.7631` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7631 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.213` → IC=+0.266 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.213 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.457` → IC=+0.237 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.457 (IC base=+0.232)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.228 (n=233)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=455)

- **FILTRO** `drift_15min` |x|> `0.8935` → IC=-0.263 (n=171)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8935
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=517)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.179 (n=51)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` > 0.5625 (IC base=-0.172)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0776` → IC=+0.230 (n=317)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0776 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.263 (n=357)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.7427` → IC=+0.243 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7427 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1863` → IC=+0.227 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1863 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.229 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=244)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.261 (n=220)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=605)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1379` → IC=+0.303 (n=242)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1379 (IC base=-0.038)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.107` → IC=+0.333 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.107 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.303 (n=532)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.9146` → IC=+0.340 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9146 (IC base=-0.038)

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
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.304 (n=499)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0541` → IC=+0.325 (n=250)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0541 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.309 (n=250)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2224` → IC=+0.322 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2224 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8405` → IC=+0.328 (n=748)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8405 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.4406` → IC=+0.334 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4406 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.353 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `13070.3814` → IC=+0.295 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13070.3814 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.298 (n=275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.286)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.329 (n=138)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.286)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.306 (n=137)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.286)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3977` → IC=+0.311 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3977 (IC base=+0.286)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.286)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.316 (n=412)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.286)

- **PATRÓN** `dist_vwap_pct` > `0.2534` → IC=+0.350 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2534 (IC base=+0.286)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.372 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `16163.1166` → IC=+0.321 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16163.1166 (IC base=+0.286)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.309 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.296)

- **PATRÓN** `drift_60min` |x|≤ `0.1126` → IC=+0.302 (n=225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1126 (IC base=+0.296)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1481` → IC=+0.301 (n=224)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1481 (IC base=+0.296)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.328 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.296)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.296)

- **PATRÓN** `ibs_15` > `0.8539` → IC=+0.343 (n=336)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8539 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` > `0.6363` → IC=+0.305 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6363 (IC base=+0.296)

- **PATRÓN** `dist_vwap_pct` < `0.167` → IC=+0.294 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.167 (IC base=+0.296)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.221` → IC=+0.334 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.221 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.297 (n=373)

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

- **FILTRO** `sigma_h` < `0.0062` → IC=-0.200 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

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
- **PATRÓN** `T_h` > `79.3918` → IC=+0.218 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.3918 (IC base=+0.206)

- **PATRÓN** `ratio` < `0.9771` → IC=+0.469 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9771 (IC base=+0.206)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.333)

- **PATRÓN** `ratio` > `1.0098` → IC=+0.302 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0098 (IC base=+0.333)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.3604` → IC=+0.208 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.3604 (IC base=+0.184)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.184)

- **PATRÓN** `T_h` < `111.9974` → IC=+0.284 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9974 (IC base=+0.284)

- **PATRÓN** `T_h` > `103.3918` → IC=+0.295 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.3918 (IC base=+0.284)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.284)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `79.3918` → IC=+0.267 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.3918 (IC base=+0.242)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.422 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.242)

- **PATRÓN** `T_h` > `106.9024` → IC=+0.330 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 106.9024 (IC base=+0.314)

- **PATRÓN** `ratio` > `1.015` → IC=+0.341 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.015 (IC base=+0.314)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1332` → IC=+0.459 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1332 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6129 sube el IC de +0.190 a +0.270 en UPDOWN_GBM#15min (n=1859). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7141 sube el IC de +0.211 a +0.276 en UPDOWN_GBM#BTC#15min (n=417). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6586 sube el IC de +0.133 a +0.258 en UPDOWN_GBM#ETH#15min (n=390). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.174 a +0.259 en UPDOWN_GBM#SOL#15min (n=222). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5728 sube el IC de +0.198 a +0.287 en UPDOWN_GBM#XRP#15min (n=476). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6423 sube el IC de -0.065 a +0.271 en UPDOWN_GBM_15M_TARDIO (n=709). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.026 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=2094). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7503 sube el IC de +0.084 a +0.325 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=209). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.199 sube el IC de -0.196 a +0.382 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6625 sube el IC de +0.145 a +0.258 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=337). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2756 sube el IC de +0.232 a +0.277 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=721). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.172 a +0.179 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=51). Ya aplicado como kelly_boost=+0.90€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.040 a +0.263 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.038 a +0.303 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=532). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8405 sube el IC de +0.291 a +0.328 en UPDOWN_GBM_IBS_ALTO (n=748). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.286 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=412). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8539 sube el IC de +0.296 a +0.343 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=336). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7872 sube el IC de +0.351 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=462). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.356 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=254). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.342 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=208). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.105 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.105 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1419 | +0.102 | +208.23€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1419 | +0.102 | +208.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1073 | +0.111 | +179.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1073 | +0.111 | +179.37€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 5 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 30665 | -0.085 | -4071.13€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1600 | -0.026 | -215.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 29065 | -0.088 | -3855.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3984 | -0.102 | -665.46€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3984 | -0.102 | -665.46€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1600 | -0.026 | -215.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1600 | -0.026 | -215.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3593 | -0.099 | -809.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3593 | -0.099 | -809.06€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7980 | -0.017 | -782.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7980 | -0.017 | -782.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7499 | -0.091 | -467.22€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7499 | -0.091 | -467.22€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6009 | -0.163 | -1130.90€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6009 | -0.163 | -1130.90€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 21642 | -0.024 | +3817.25€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5605 | +0.000 | +1777.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 16037 | -0.032 | +2039.28€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 21642 | -0.024 | +3817.25€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5605 | +0.000 | +1777.97€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 16037 | -0.032 | +2039.28€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 103524 | +0.113 | -5042.05€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15100 | +0.184 | -459.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 429 | -0.066 | -56.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 81423 | +0.101 | -4285.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6572 | +0.106 | -241.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 13529 | +0.101 | -1033.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 49 | -0.147 | +8.51€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 13465 | +0.102 | -1030.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 20775 | +0.131 | -397.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4682 | +0.200 | -139.80€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 13504 | +0.113 | -190.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2547 | +0.098 | -44.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13574 | +0.090 | -1212.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 56 | -0.103 | -7.23€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 13503 | +0.091 | -1194.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 21982 | +0.124 | -412.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5937 | +0.177 | -75.88€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13651 | +0.106 | -267.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2382 | +0.100 | -61.01€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 20118 | +0.114 | -1178.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4325 | +0.187 | -256.35€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 332 | -0.027 | -2.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13818 | +0.092 | -784.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1643 | +0.130 | -135.34€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13546 | +0.100 | -806.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 51 | -0.028 | +11.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 13482 | +0.100 | -817.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 16453 | +0.194 | -1028.60€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 16453 | +0.194 | -1028.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3873 | +0.169 | -391.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3873 | +0.169 | -391.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1572 | +0.205 | -6.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1572 | +0.205 | -6.01€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3812 | +0.182 | -311.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3812 | +0.182 | -311.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3364 | +0.243 | -101.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3364 | +0.243 | -101.64€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3753 | +0.191 | -232.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3753 | +0.191 | -232.21€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 771 | +0.430 | -21.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 771 | +0.430 | -21.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 303 | +0.441 | -0.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 303 | +0.441 | -0.92€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 291 | +0.428 | -8.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 291 | +0.428 | -8.40€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 165 | +0.410 | -9.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 165 | +0.410 | -9.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 56951 | +0.198 | -4394.14€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 56951 | +0.198 | -4394.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9810 | +0.178 | -1105.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9810 | +0.178 | -1105.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9122 | +0.222 | -346.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9122 | +0.222 | -346.70€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9831 | +0.175 | -1135.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9831 | +0.175 | -1135.07€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9207 | +0.218 | -370.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9207 | +0.218 | -370.55€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9427 | +0.203 | -614.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9427 | +0.203 | -614.27€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9554 | +0.193 | -821.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9554 | +0.193 | -821.72€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 21596 | +0.116 | +122.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 21596 | +0.116 | +122.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10722 | +0.119 | +114.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10722 | +0.119 | +114.14€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10874 | +0.112 | +8.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10874 | +0.112 | +8.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1605 | +0.288 | -26.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1605 | +0.288 | -26.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 716 | +0.279 | -18.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 716 | +0.279 | -18.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 775 | +0.286 | -12.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 775 | +0.286 | -12.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 114 | +0.345 | +3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 114 | +0.345 | +3.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 710 | +0.435 | -4.66€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 710 | +0.435 | -4.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 340 | +0.433 | -4.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 340 | +0.433 | -4.59€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 325 | +0.439 | -0.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 325 | +0.439 | -0.46€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1228 | +0.066 | -66.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 435 | +0.051 | -40.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 793 | +0.074 | -26.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 967 | +0.072 | -35.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 174 | +0.062 | -9.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 793 | +0.074 | -26.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 197 | +0.018 | -34.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 197 | +0.018 | -34.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 40730 | +0.098 | -1162.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3338 | +0.088 | +16.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 37392 | +0.099 | -1178.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 22723 | +0.102 | -341.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3338 | +0.088 | +16.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 19385 | +0.104 | -358.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7866 | +0.109 | -16.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7866 | +0.109 | -16.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10141 | +0.081 | -803.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10141 | +0.081 | -803.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 852 | +0.212 | -102.62€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 852 | +0.212 | -102.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 852 | +0.212 | -102.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 852 | +0.212 | -102.62€ | 2 | 4 |
| ✅ GBM_LATE_15M | 28826 | +0.086 | +14073.97€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 28826 | +0.086 | +14073.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4832 | +0.198 | +3628.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4832 | +0.198 | +3628.49€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 4293 | +0.179 | +3070.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4293 | +0.179 | +3070.46€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 5083 | +0.198 | +3789.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5083 | +0.198 | +3789.09€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 4149 | +0.029 | +1003.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4149 | +0.029 | +1003.47€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4115 | -0.032 | +925.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4115 | -0.032 | +925.54€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6354 | -0.039 | +1656.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6354 | -0.039 | +1656.92€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 30773 | +0.087 | +16316.66€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 30773 | +0.087 | +16316.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5868 | +0.014 | +3084.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5868 | +0.014 | +3084.42€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6409 | +0.016 | +1367.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6409 | +0.016 | +1367.22€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4375 | +0.265 | +4459.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4375 | +0.265 | +4459.30€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5077 | +0.008 | +1030.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5077 | +0.008 | +1030.60€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4968 | +0.033 | +1967.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4968 | +0.033 | +1967.57€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4076 | +0.280 | +4407.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4076 | +0.280 | +4407.55€ | 0 | 26 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 23144 | +0.170 | +17626.66€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 23144 | +0.170 | +17626.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3487 | +0.210 | +2827.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3487 | +0.210 | +2827.84€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3648 | +0.150 | +2684.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3648 | +0.150 | +2684.80€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3659 | +0.209 | +2931.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3659 | +0.209 | +2931.44€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3879 | +0.134 | +2768.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3879 | +0.134 | +2768.53€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4330 | +0.120 | +3112.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4330 | +0.120 | +3112.55€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4141 | +0.205 | +3301.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4141 | +0.205 | +3301.51€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6135 | +0.137 | +2847.44€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6135 | +0.137 | +2847.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 214 | +0.111 | +95.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 214 | +0.111 | +95.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1746 | +0.136 | +881.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1746 | +0.136 | +881.44€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1850 | +0.152 | +893.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1850 | +0.152 | +893.65€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1445 | +0.121 | +584.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1445 | +0.121 | +584.42€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 29032 | +0.178 | +22107.52€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 29032 | +0.178 | +22107.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4602 | +0.226 | +3986.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4602 | +0.226 | +3986.24€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4526 | +0.152 | +3023.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4526 | +0.152 | +3023.51€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4818 | +0.226 | +4148.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4818 | +0.226 | +4148.93€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4717 | +0.136 | +3260.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4717 | +0.136 | +3260.72€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5079 | +0.119 | +3416.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5079 | +0.119 | +3416.47€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5290 | +0.210 | +4271.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5290 | +0.210 | +4271.66€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8165 | +0.168 | +5279.22€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 8165 | +0.168 | +5279.22€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1857 | +0.154 | +1274.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1857 | +0.154 | +1274.28€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2668 | +0.173 | +1722.20€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2668 | +0.173 | +1722.20€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 861 | +0.153 | +482.06€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 861 | +0.153 | +482.06€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2011 | +0.072 | +766.62€ | 1 | 16 |
| ✅ GBM_LATE_60M#60min | 2011 | +0.072 | +766.62€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 744 | +0.095 | +276.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 744 | +0.095 | +276.51€ | 0 | 15 |
| ✅ GBM_LATE_60M#ETH | 652 | +0.073 | +303.42€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 652 | +0.073 | +303.42€ | 2 | 15 |
| ✅ GBM_LATE_60M#SOL | 615 | +0.043 | +186.69€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 615 | +0.043 | +186.69€ | 3 | 11 |
| 🚫 GBM_LATE_60M_FADE | 413 | -0.252 | -19.18€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 413 | -0.252 | -19.18€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 155 | -0.220 | -5.26€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 155 | -0.220 | -5.26€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 138 | -0.250 | -7.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 138 | -0.250 | -7.31€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 120 | -0.287 | -6.62€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 120 | -0.287 | -6.62€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 800 | +0.090 | +203.42€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 800 | +0.090 | +203.42€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 310 | +0.080 | +67.43€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 310 | +0.080 | +67.43€ | 2 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 248 | +0.056 | +29.43€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 248 | +0.056 | +29.43€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 242 | +0.135 | +106.56€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 242 | +0.135 | +106.56€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 109 | +0.266 | +95.86€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 109 | +0.266 | +95.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 109 | +0.266 | +95.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 109 | +0.266 | +95.86€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2309 | +0.104 | +628.06€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2309 | +0.104 | +628.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2309 | +0.104 | +628.06€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2309 | +0.104 | +628.06€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M | 401 | -0.076 | -33.64€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 401 | -0.076 | -33.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 103 | -0.043 | -3.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 103 | -0.043 | -3.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 149 | -0.030 | -5.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 149 | -0.030 | -5.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2292 | +0.012 | +31.05€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2292 | +0.012 | +31.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 121 | +0.012 | -3.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 121 | +0.012 | -3.49€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 287 | -0.002 | +9.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 287 | -0.002 | +9.93€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 176 | -0.022 | -5.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 176 | -0.022 | -5.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 940 | +0.023 | +23.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 940 | +0.023 | +23.14€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 527 | +0.012 | +1.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 527 | +0.012 | +1.08€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 241 | +0.010 | +5.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 241 | +0.010 | +5.74€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1217 | -0.041 | -23.36€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1217 | -0.041 | -23.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 345 | -0.042 | -13.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 345 | -0.042 | -13.18€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 413 | -0.025 | -0.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 413 | -0.025 | -0.08€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 459 | -0.053 | -10.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 459 | -0.053 | -10.09€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 2968 | -0.014 | +77.85€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1405 | -0.011 | +44.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1563 | -0.017 | +33.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 85 | +0.029 | +10.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 45 | +0.074 | +11.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 40 | -0.024 | -1.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 703 | +0.009 | +48.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 327 | +0.017 | +23.50€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 376 | +0.003 | +25.37€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 356 | -0.017 | +11.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 170 | -0.041 | -2.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 186 | +0.005 | +14.37€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 588 | -0.036 | -20.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 271 | -0.035 | -10.73€ | 4 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 317 | -0.036 | -9.66€ | 4 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 566 | -0.021 | +10.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 276 | -0.018 | +10.35€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 290 | -0.024 | +0.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 670 | -0.018 | +16.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 316 | -0.009 | +12.83€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 354 | -0.025 | +3.86€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 33037 | -0.006 | +1459.00€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 33037 | -0.006 | +1459.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5847 | +0.020 | +725.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5847 | +0.020 | +725.50€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5022 | -0.032 | -86.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5022 | -0.032 | -86.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5934 | +0.016 | +529.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5934 | +0.016 | +529.33€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4804 | -0.054 | -165.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4804 | -0.054 | -165.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5562 | -0.010 | +202.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5562 | -0.010 | +202.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5868 | +0.011 | +252.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5868 | +0.011 | +252.92€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_FADE | 6033 | -0.061 | -153.53€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6033 | -0.061 | -153.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1456 | -0.085 | -42.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1456 | -0.085 | -42.79€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 685 | -0.124 | -31.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 685 | -0.124 | -31.62€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1777 | -0.078 | -34.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1777 | -0.078 | -34.89€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 83311 | -0.073 | +1747.22€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 83311 | -0.073 | +1747.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 14187 | -0.076 | +833.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 14187 | -0.076 | +833.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12744 | -0.095 | -668.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12744 | -0.095 | -668.64€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 14449 | -0.067 | +761.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 14449 | -0.067 | +761.79€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 12276 | -0.092 | -211.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 12276 | -0.092 | -211.59€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 15204 | -0.049 | +366.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 15204 | -0.049 | +366.02€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 14451 | -0.063 | +666.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 14451 | -0.063 | +666.07€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7852 | -0.028 | -137.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7852 | -0.028 | -137.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1801 | -0.036 | -12.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1801 | -0.036 | -12.09€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2221 | -0.024 | -30.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2221 | -0.024 | -30.38€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1066 | -0.045 | -19.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1066 | -0.045 | -19.44€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 765 | -0.021 | -24.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 765 | -0.021 | -24.46€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1241 | +0.111 | +432.47€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1105 | +0.117 | +419.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 249 | +0.134 | +120.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 249 | +0.134 | +120.38€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 212 | +0.112 | +63.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 212 | +0.112 | +63.46€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 232 | +0.107 | +86.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 232 | +0.107 | +86.77€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 193 | +0.126 | +84.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 193 | +0.126 | +84.33€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 219 | +0.102 | +64.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 219 | +0.102 | +64.94€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 663 | -0.044 | -53.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 663 | -0.044 | -53.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 131 | -0.004 | +3.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 131 | -0.004 | +3.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 92 | -0.074 | -12.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 92 | -0.074 | -12.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 192 | -0.057 | -22.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 192 | -0.057 | -22.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 136 | -0.029 | -7.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 136 | -0.029 | -7.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 112 | -0.061 | -12.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 112 | -0.061 | -12.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 632 | -0.107 | -54.19€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 289 | -0.156 | -66.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 236 | -0.193 | -67.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 53 | +0.009 | +0.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 220 | -0.072 | -0.33€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 170 | -0.076 | -6.56€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 50 | -0.058 | +6.23€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 123 | -0.052 | +12.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 99 | -0.074 | +6.55€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 24 | +0.038 | +6.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 505 | -0.131 | -67.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 127 | -0.012 | +13.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 794 | -0.200 | -34.62€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 329 | -0.198 | -28.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 288 | -0.197 | -29.11€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 41 | -0.198 | +0.21€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 270 | -0.217 | -25.15€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 235 | -0.226 | -30.24€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 35 | -0.149 | +5.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 195 | -0.175 | +19.42€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 179 | -0.174 | +14.75€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 16 | -0.133 | +4.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 702 | -0.202 | -44.60€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 92 | -0.181 | +9.98€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 338 | +0.403 | +260.58€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 36 | +0.105 | -1.22€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 36 | +0.105 | -1.22€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 86 | +0.364 | +71.63€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 86 | +0.364 | +71.63€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 216 | +0.463 | +190.17€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 216 | +0.463 | +190.17€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 338 | +0.403 | +260.58€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 563 | +0.031 | +15.62€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 563 | +0.031 | +15.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 274 | +0.029 | +3.47€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 274 | +0.029 | +3.47€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 37 | +0.090 | +3.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 59 | -0.008 | -1.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 59 | -0.008 | -1.62€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 193 | +0.033 | +10.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 193 | +0.033 | +10.59€ | 2 | 3 |
| ✅ STREAK_FADE_5M | 2940 | -0.021 | -116.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2940 | -0.021 | -116.87€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 896 | -0.020 | -30.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 896 | -0.020 | -30.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 573 | -0.024 | -23.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 573 | -0.024 | -23.73€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1315 | -0.019 | -48.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1315 | -0.019 | -48.07€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 77 | -0.044 | -5.84€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 77 | -0.044 | -5.84€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8752 | +0.021 | +116.55€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8752 | +0.021 | +116.55€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2409 | +0.023 | +29.80€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2409 | +0.023 | +29.80€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1985 | +0.030 | +48.69€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1985 | +0.030 | +48.69€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2654 | +0.013 | +8.39€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2654 | +0.013 | +8.39€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1704 | +0.022 | +29.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1704 | +0.022 | +29.66€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7940 | +0.013 | -37.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7940 | +0.013 | -37.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3172 | +0.017 | -6.43€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3172 | +0.017 | -6.43€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3142 | +0.012 | -18.80€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3142 | +0.012 | -18.80€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1626 | +0.008 | -11.86€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1626 | +0.008 | -11.86€ | 2 | 0 |
| ✅ UPDOWN_GBM | 44978 | +0.036 | +2938.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11679 | +0.072 | +2213.20€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1592 | +0.004 | +7.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 28811 | +0.027 | +694.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2726 | +0.003 | +24.37€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4541 | +0.075 | +559.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 818 | +0.161 | +356.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3690 | +0.057 | +203.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 8644 | +0.044 | +657.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1527 | +0.088 | +349.62€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 428 | +0.014 | +5.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5392 | +0.045 | +271.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1233 | +0.004 | +30.45€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 64 | -0.091 | +0.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5186 | +0.042 | +334.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 775 | +0.138 | +273.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4383 | +0.025 | +62.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 9840 | +0.026 | +430.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2965 | +0.050 | +339.66€ | 1 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 420 | +0.007 | +7.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5477 | +0.020 | +88.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 922 | -0.001 | -8.77€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 56 | -0.121 | +3.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 10211 | +0.017 | +275.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2813 | +0.027 | +195.73€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 411 | -0.004 | -0.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6368 | +0.015 | +81.84€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 571 | +0.006 | +2.69€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 48 | -0.160 | -3.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6554 | +0.040 | +681.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2781 | +0.087 | +697.86€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 272 | +0.000 | -2.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3501 | +0.005 | -12.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 168 | -0.123 | +1.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 615 | +0.351 | +205.92€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 615 | +0.351 | +205.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 338 | +0.356 | +111.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 338 | +0.356 | +111.19€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 277 | +0.342 | +94.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 277 | +0.342 | +94.73€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 13436 | -0.035 | +2937.06€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 13436 | -0.035 | +2937.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 921 | -0.048 | +376.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 921 | -0.048 | +376.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2472 | -0.118 | +41.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2472 | -0.118 | +41.93€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 488 | +0.194 | +354.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 488 | +0.194 | +354.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1540 | +0.207 | +932.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1540 | +0.207 | +932.65€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4028 | -0.063 | +580.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4028 | -0.063 | +580.49€ | 2 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3987 | -0.072 | +651.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3987 | -0.072 | +651.48€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 156 | +0.038 | +7.79€ | 1 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 156 | +0.038 | +7.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 156 | +0.038 | +7.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 156 | +0.038 | +7.79€ | 1 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 997 | +0.291 | +800.05€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 997 | +0.291 | +800.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 549 | +0.286 | +417.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 549 | +0.286 | +417.66€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 448 | +0.296 | +382.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 448 | +0.296 | +382.39€ | 0 | 10 |
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
| ✅ WEEKLY_PRICE | 2643 | +0.302 | +1285.15€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 927 | +0.254 | +133.10€ | 0 | 5 |
| ✅ WEEKLY_PRICE#ETH | 1002 | +0.292 | +425.04€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 714 | +0.377 | +727.01€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.056) — sin ventaja clara. oversold(IBS<0.3): IC=+0.049 n=15832 | neutral: IC=+0.035 n=16710 | overbought(IBS>0.7): IC=+0.090 n=16139
  - _Datos_: n=50413 IC=+0.059 PNL=+6349.04€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 576 celda(s) pasan gate riguroso completo de 2338 evaluadas (n>=40) y 3309 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.027 < 0.08 — monitorear
  - _Datos_: n=2813 IC=+0.027 PNL=+195.73€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1002/15 IC=+0.292 PNL=+425.04€ | BTC: n=927/15 IC=+0.254 PNL=+133.10€ | SOL: n=714/15 IC=+0.377 PNL=+727.01€

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
  - _Estado_: 44916 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.125 n=401/60 | contraria IC=+0.173 n=374 | gap=-0.048 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=333, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 193 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=922/40 IC=-0.001 PNL=-8.77€ | BTC#60min: n=1233/40 IC=+0.004 PNL=+30.45€ | SOL#60min: n=571/40 IC=+0.006 PNL=+2.69€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.050 n=380118 | tras_1loss IC=+0.083 n=293593 | tras_2loss IC=+0.053 n=122321/40 | gap=-0.003 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.017 n=5436 | contrario_BTC IC=+0.034 n=4822/40 | gap=+0.017 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.08 con n=443 PNL=+328.42€
  - _Datos_: n=443 IC=+0.210 PNL=+328.42€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.329 > 0.1 con n=2159 PNL=+1171.19€
  - _Datos_: n=2159 IC=+0.329 PNL=+1171.19€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=363 IC=+0.067 PNL=+40.55€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=363 IC=+0.067 PNL=+40.55€

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
  - _Estado_: n=42985 IC=+0.035 PNL=+2800.36€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=42985 IC=+0.035 PNL=+2800.36€

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
  - _Estado_: n=1883 IC=+0.006 PNL=-0.53€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1883 IC=+0.006 PNL=-0.53€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=843 IC=-0.005 PNL=+24.90€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=843 IC=-0.005 PNL=+24.90€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=587 IC=+0.026 PNL=+31.61€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=587 IC=+0.026 PNL=+31.61€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.190 > 0.1 con n=2478 PNL=+1601.89€
  - _Datos_: n=2478 IC=+0.190 PNL=+1601.89€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1447 IC=+0.056 PNL=+105.76€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1447 IC=+0.056 PNL=+105.76€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1527 IC=+0.088 PNL=+349.62€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1527 IC=+0.088 PNL=+349.62€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.088 > 0.08 con n=6653 PNL=+1642.03€
  - _Datos_: n=6653 IC=+0.088 PNL=+1642.03€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=182 IC=-0.255 PNL=-8.23€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=182 IC=-0.255 PNL=-8.23€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=301 IC=-0.035 PNL=-3.25€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=301 IC=-0.035 PNL=-3.25€

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
  - _Estado_: n=6213 IC=-0.000 PNL=+3.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6213 IC=-0.000 PNL=+3.32€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.266 n=109) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=109 IC=+0.266 PNL=+95.86€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=8268 IC=+0.039 PNL=+541.95€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=8268 IC=+0.039 PNL=+541.95€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2790 IC=+0.056 PNL=+342.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2790 IC=+0.056 PNL=+342.57€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.08 con n=396 PNL=+124.61€
  - _Datos_: n=396 IC=+0.113 PNL=+124.61€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.151 > 0.08 con n=702 PNL=+183.46€
  - _Datos_: n=702 IC=+0.151 PNL=+183.46€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.107 > 0.08 con n=530 PNL=+248.74€
  - _Datos_: n=530 IC=+0.107 PNL=+248.74€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64024 IC=+0.118 PNL=+23817.77€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64024 IC=+0.118 PNL=+23817.77€

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
  - _Estado_: n=6734 IC=+0.042 PNL=+528.22€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6734 IC=+0.042 PNL=+528.22€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.02 con n=709 PNL=+267.63€
  - _Datos_: n=709 IC=+0.119 PNL=+267.63€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.448 > 0.1 con n=1237 PNL=+1209.51€
  - _Datos_: n=1237 IC=+0.448 PNL=+1209.51€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=16302 IC=+0.058 PNL=+1996.06€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=16302 IC=+0.058 PNL=+1996.06€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.1 con n=4028 PNL=+2219.44€
  - _Datos_: n=4028 IC=+0.203 PNL=+2219.44€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.148 < -0.1 con n=271 PNL=+28.16€
  - _Datos_: n=271 IC=-0.148 PNL=+28.16€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2147 IC=+0.054 PNL=+227.06€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2147 IC=+0.054 PNL=+227.06€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=92 IC=-0.096 PNL=+5.74€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=92 IC=-0.096 PNL=+5.74€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.121 > 0.1 con n=510 PNL=+142.52€
  - _Datos_: n=510 IC=+0.121 PNL=+142.52€

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
  - _Estado_: n=20646 IC=-0.137 PNL=+1419.32€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=20646 IC=-0.137 PNL=+1419.32€

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
  - _Estado_: n=2169 IC=+0.138 PNL=+1226.79€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2169 IC=+0.138 PNL=+1226.79€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.192 > 0.08 con n=2439 PNL=+1589.25€
  - _Datos_: n=2439 IC=+0.192 PNL=+1589.25€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.08 con n=555 PNL=+290.19€
  - _Datos_: n=555 IC=+0.211 PNL=+290.19€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.234 < -0.1 con n=2031 PNL=-200.99€
  - _Datos_: n=2031 IC=-0.234 PNL=-200.99€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6080 IC=+0.178 PNL=+4198.26€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6080 IC=+0.178 PNL=+4198.26€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=83 PNL=+29.22€
  - _Datos_: n=83 IC=+0.100 PNL=+29.22€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2203 IC=+0.069 PNL=+671.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2203 IC=+0.069 PNL=+671.74€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.181 > 0.08 con n=2009 PNL=+1427.26€
  - _Datos_: n=2009 IC=+0.181 PNL=+1427.26€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3341 IC=-0.032 PNL=+860.90€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3341 IC=-0.032 PNL=+860.90€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.088 > 0.08 con n=590 PNL=-52.48€
  - _Datos_: n=590 IC=+0.088 PNL=-52.48€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.237 > 0.08 con n=3611 PNL=-319.57€
  - _Datos_: n=3611 IC=+0.237 PNL=-319.57€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=42 IC=+0.000 PNL=+5.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=42 IC=+0.000 PNL=+5.94€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1176) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1176 IC=+0.102 PNL=+281.48€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.08 con n=302 PNL=+106.09€
  - _Datos_: n=302 IC=+0.332 PNL=+106.09€

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
  - _Estado_: n=9810 IC=+0.178 PNL=-1105.84€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=9810 IC=+0.178 PNL=-1105.84€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.1 con n=157 PNL=+95.67€
  - _Datos_: n=157 IC=+0.204 PNL=+95.67€
