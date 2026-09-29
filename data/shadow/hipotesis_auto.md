# Hipótesis automáticas — 2026-09-29 10:32 UTC
_Generado por shadow_postmortem.py sobre 664680 resoluciones (PNL=+78048.12€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=538)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.234 (n=570)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.137)

- **PATRÓN** `n_total_lado` > `75.0` → IC=+0.208 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 75.0 (IC base=+0.137)

- **PATRÓN** `banda_hit_calibrado` > `0.803` → IC=+0.254 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.803 (IC base=+0.137)

- **PATRÓN** `banda_z` > `9.581` → IC=+0.203 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.581 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.155 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=605)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `4766.038` → IC=+0.162 (n=190)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4766.038 (IC base=+0.137)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.122 (n=538)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.055)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.140 (n=170)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=438)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=403)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.257 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.146)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.146)

- **PATRÓN** `banda_hit_calibrado` > `0.7991` → IC=+0.265 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7991 (IC base=+0.146)

- **PATRÓN** `banda_z` > `10.478` → IC=+0.214 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.478 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.166 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=515)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3313.2914` → IC=+0.150 (n=304)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3313.2914 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.152 (n=159)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 94.0 (IC base=+0.058)

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
- **FILTRO** `restante_s_al_confirmar` < `145.81` → IC=-0.218 (n=7595)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.81
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=22791)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `137.94` → IC=-0.246 (n=981)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 137.94
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=2944)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `127.03` → IC=-0.307 (n=894)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.03
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2684)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.21` → IC=-0.204 (n=1854)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.21
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=5563)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.208 (n=14888)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3676)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5598.8888` → IC=+0.177 (n=2361)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 5598.8888 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.135 (n=12578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.136 (n=15501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.230 (n=11874)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=5985)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7788.6778` → IC=+0.172 (n=2278)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7788.6778 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=1815)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=1773)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.207 (n=2234)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `15920.3308` → IC=+0.237 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15920.3308 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.202 (n=1600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.203 (n=1786)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` < `0.375` → IC=+0.262 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.375 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=2283)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `15854.5779` → IC=+0.214 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15854.5779 (IC base=+0.197)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.169 (n=351)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.615 (IC base=+0.097)

- **PATRÓN** `libro_liquidez` > `4566.8958` → IC=+0.142 (n=241)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 4566.8958 (IC base=+0.097)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.134 (n=572)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 11.0 (IC base=+0.100)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=869)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.162 (n=226)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.100)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=3052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=2606)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.150)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.347 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.366 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.232 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `4232.2075` → IC=+0.230 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4232.2075 (IC base=+0.228)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.136 (n=728)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.253 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=586)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `1315.39` → IC=+0.146 (n=722)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1315.39 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.87` → IC=+0.429 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.87 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.155 (n=1151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 7.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `py_entrada` < `0.285` → IC=+0.308 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.285 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.165 (n=766)

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

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.222 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.116)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.76` → IC=-0.289 (n=131)

  - _Acción_: SKIP cuando `py_entrada` > 0.76
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=12690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=12135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.229 (n=4087)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `3571.1845` → IC=+0.331 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3571.1845 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=3038)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.173 (n=2883)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 17.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=2895)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.168)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.253 (n=1074)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.251 (n=1072)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.246)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.343 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.246)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=2988)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2852)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=2413)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.252 (n=2630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.325 (n=860)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=2907)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.193 (n=2800)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.196 (n=2188)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.71 (IC base=+0.192)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.435 (n=580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.429)

- **PATRÓN** `py_entrada` > `0.939` → IC=+0.464 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.939 (IC base=+0.429)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.428 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.429)

- **PATRÓN** `libro_liquidez` > `11185.2288` → IC=+0.459 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11185.2288 (IC base=+0.429)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.442 (n=222)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.446 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `14179.602` → IC=+0.447 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14179.602 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.449 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.463 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.425 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `3299.2146` → IC=+0.446 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3299.2146 (IC base=+0.428)

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

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=37690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.237 (n=16708)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=7660)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 5.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5240)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=7080)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=6799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=6785)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.263 (n=3865)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=6871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=6878)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.174)

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

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=2342)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=6251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2500)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.195 (n=7074)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 6.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=6323)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=2901)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.193)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=5739)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` < `4.18` → IC=+0.124 (n=5356)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.18 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5415)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=7121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.59` → IC=+0.137 (n=5328)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.59 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=2886)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.14` → IC=+0.125 (n=2649)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.14 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.139 (n=2669)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=3514)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.28` → IC=+0.140 (n=2651)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 3.28 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.186 (n=2853)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.113)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.132 (n=2999)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.113)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.136 (n=2689)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.25 (IC base=+0.113)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.301 (n=1267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.379 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1545.7265` → IC=+0.293 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1545.7265 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.344 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5065.6943` → IC=+0.306 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5065.6943 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.324 (n=406)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1447.2132` → IC=+0.303 (n=515)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.434 (n=470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.435 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.436 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.435 (n=259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.434 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.455 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.445 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.438 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `1978.5089` → IC=+0.464 (n=110)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4916` → IC=+0.127 (n=8972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.4916 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.9808` → IC=+0.243 (n=2991)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9808 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.2197` → IC=+0.258 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2197 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.971` → IC=+0.180 (n=3426)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.971 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `1.2099` → IC=+0.252 (n=2473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2099 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` > `0.6162` → IC=+0.255 (n=2472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6162 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` > `0.3018` → IC=+0.226 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3018 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` > `1.4592` → IC=+0.207 (n=6212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4592 (IC base=+0.110)

- **PATRÓN** `ibs_20min` < `0.5706` → IC=+0.134 (n=10877)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.5706 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.6045` → IC=+0.202 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6045 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.184 (n=1712)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6971 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `0.869` → IC=+0.176 (n=2594)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.869 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.224 (n=1868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.5684` → IC=+0.199 (n=5912)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.5684 (IC base=+0.067)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.213 (n=6410)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=+0.067)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.196 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0049 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.176 (n=668)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0081 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3528` → IC=+0.173 (n=2005)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3528 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.173 (n=1355)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 11.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.172` → IC=+0.270 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.172 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.208 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.4349` → IC=+0.169 (n=1884)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4349 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.182 (n=2020)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.04 (IC base=+0.168)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.242 (n=1406)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.0917` → IC=+0.277 (n=523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0917 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.243 (n=1413)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0538` → IC=+0.289 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0538 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.544` → IC=+0.239 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.544 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.459` → IC=+0.244 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.459 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2821` → IC=+0.275 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2821 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.586` → IC=+0.246 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.586 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1657.2084` → IC=+0.249 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1657.2084 (IC base=+0.235)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.242 (n=692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.3538` → IC=+0.229 (n=1568)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3538 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=1647)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=1597)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.9845` → IC=+0.270 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9845 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` < `0.347` → IC=+0.225 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.347 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.469` → IC=+0.261 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.469 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.2558` → IC=+0.224 (n=1568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2558 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `1.0844` → IC=+0.229 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0844 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.242 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.7485` → IC=+0.224 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7485 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.3728` → IC=+0.234 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3728 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `11000.801` → IC=+0.224 (n=1568)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11000.801 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.164 (n=1075)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0039 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.164 (n=539)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=624)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=729)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.3342` → IC=+0.193 (n=1073)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3342 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1308` → IC=+0.152 (n=1449)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1308 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.158 (n=255)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.327` → IC=+0.142 (n=1479)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.327 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.147 (n=1609)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.2116 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `0.8575` → IC=+0.139 (n=1072)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 0.8575 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1564` → IC=+0.178 (n=424)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1564 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.4311` → IC=+0.150 (n=1498)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4311 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7701` → IC=+0.146 (n=999)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7701 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `13996.9972` → IC=+0.142 (n=1072)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 13996.9972 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.171 (n=624)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 231.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.212 (n=669)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=2110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=1805)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.268 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.254 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.193 (n=1757)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.3549` → IC=+0.205 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3549 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.7734` → IC=+0.197 (n=1714)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.7734 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.196 (n=2384)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.220 (n=1543)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6283` → IC=+0.213 (n=1750)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6283 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.215 (n=825)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0643` → IC=+0.240 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0643 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.695` → IC=+0.228 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.695 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.57` → IC=+0.212 (n=1898)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.57 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3501` → IC=+0.255 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3501 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.75` → IC=+0.206 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.75 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `3.26` → IC=+0.225 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.26 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.218 (n=1106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1908.66` → IC=+0.215 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1908.66 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.211 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.158 (n=109)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=2431)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.140 (n=392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0037 (IC base=+0.037)

- **PATRÓN** `ibs_20min` > `0.9502` → IC=+0.223 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9502 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` < `0.1949` → IC=+0.336 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1949 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.823` → IC=+0.171 (n=797)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 4.823 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.336 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.345 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.356 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.356 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.334 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.037)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.333 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.037)

- **PATRÓN** `ibs_20min` < `0.1049` → IC=+0.152 (n=636)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1049 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` > `0.6662` → IC=+0.212 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6662 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `0.6137` → IC=+0.156 (n=321)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6137 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.150 (n=321)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.1643 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2304` → IC=+0.206 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2304 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.5315` → IC=+0.165 (n=811)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.5315 (IC base=+0.020)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=67)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=365)

- **FILTRO** `ibs_20min` < `0.2941` → IC=-0.200 (n=108)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=324)

- **FILTRO** `ibs_20min` > `0.2456` → IC=-0.124 (n=2427)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2456
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=1196)

- **FILTRO** `sigma_ewma_delta_pct` > `8.692` → IC=-0.216 (n=382)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.692
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3241)

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

- **PATRÓN** `ibs_20min` < `0.2456` → IC=+0.127 (n=1196)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.2456 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` > `0.7288` → IC=+0.259 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7288 (IC base=-0.042)

- **PATRÓN** `dist_vwap_pct` < `0.4579` → IC=+0.236 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4579 (IC base=-0.042)

- **PATRÓN** `volumen_regimen` < `0.6727` → IC=+0.275 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6727 (IC base=-0.042)

- **PATRÓN** `volumen_pendiente_norm` > `0.1591` → IC=+0.296 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1591 (IC base=-0.042)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.283 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=-0.042)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6579` → IC=-0.184 (n=631)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6579
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1896)

- **FILTRO** `ibs_20min` < `0.7197` → IC=-0.157 (n=1667)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7197
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=860)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.202 (n=548)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1979)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.210 (n=929)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=2821)

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

- **PATRÓN** `dist_vwap_pct` > `0.5597` → IC=+0.279 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5597 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` < `0.7286` → IC=+0.257 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7286 (IC base=-0.020)

- **PATRÓN** `volumen_regimen` > `1.2467` → IC=+0.282 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2467 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.0991` → IC=+0.268 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0991 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `2.1399` → IC=+0.262 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1399 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.5237` → IC=+0.254 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5237 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.198 (n=3831)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0098 (IC base=+0.099)

- **PATRÓN** `ibs_20min` > `0.4741` → IC=+0.187 (n=10265)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4741 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `1.0199` → IC=+0.291 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0199 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.158 (n=5308)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` < `1.1808` → IC=+0.244 (n=4121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1808 (IC base=+0.099)

- **PATRÓN** `volumen_regimen` > `0.691` → IC=+0.255 (n=3681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.691 (IC base=+0.099)

- **PATRÓN** `volumen_pendiente_norm` > `0.2925` → IC=+0.270 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2925 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` < `1.4619` → IC=+0.242 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4619 (IC base=+0.099)

- **PATRÓN** `volumen_spike_ratio` > `2.6443` → IC=+0.251 (n=2223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6443 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.273 (n=6205)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 94.0 (IC base=+0.099)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.168 (n=3749)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0092 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5484` → IC=+0.154 (n=9888)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.5484 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7099` → IC=+0.252 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7099 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2507` → IC=+0.245 (n=3221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2507 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7094` → IC=+0.246 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7094 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.2049` → IC=+0.253 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2049 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2413` → IC=+0.302 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2413 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5938` → IC=+0.268 (n=2002)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5938 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2837` → IC=+0.264 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2837 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.273 (n=4431)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2526` → IC=-0.156 (n=794)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2526
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2382)

- **FILTRO** `ibs_20min` > `0.7572` → IC=-0.148 (n=649)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7572
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1951)

- **FILTRO** `sigma_ewma_delta_pct` > `4.528` → IC=-0.166 (n=594)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.528
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2006)

- **PATRÓN** `ibs_20min` > `0.8961` → IC=+0.271 (n=794)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8961 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.907` → IC=+0.206 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.907 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.261 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.192 (n=339)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.041)

- **PATRÓN** `volumen_spike_ratio` > `2.1594` → IC=+0.214 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1594 (IC base=+0.041)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.207 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.041)

- **PATRÓN** `volumen_pendiente_norm` < `0.0916` → IC=+0.452 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0916 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4701` → IC=+0.450 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4701 (IC base=-0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.7565` → IC=+0.438 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7565 (IC base=-0.021)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.488 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.021)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8671` → IC=+0.167 (n=770)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8671 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.299` → IC=+0.180 (n=408)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.299 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.180 (n=951)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.6754 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2725` → IC=+0.238 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2725 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.4226` → IC=+0.200 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4226 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.397` → IC=+0.171 (n=348)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.397 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `236.0` → IC=+0.207 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 236.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.221 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.8596` → IC=+0.230 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8596 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2686` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2686 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.243 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `456.0` → IC=+0.219 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 456.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.280 (n=1187)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.255 (n=1783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.251 (n=1795)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.681` → IC=+0.281 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.681 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.265 (n=1514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` > `3.2944` → IC=+0.270 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2944 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=2090)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `1911.8529` → IC=+0.259 (n=806)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.8529 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.310 (n=660)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.294 (n=640)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.327 (n=488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.290 (n=1456)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.290 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.773` → IC=+0.285 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.773 (IC base=+0.283)

- **PATRÓN** `volumen_pendiente_norm` > `0.3387` → IC=+0.290 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3387 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` < `1.5833` → IC=+0.293 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5833 (IC base=+0.283)

- **PATRÓN** `volumen_spike_ratio` > `2.6851` → IC=+0.291 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6851 (IC base=+0.283)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.287 (n=915)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `1900.976` → IC=+0.296 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1900.976 (IC base=+0.283)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.287 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.283)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7735` → IC=-0.187 (n=669)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7735
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=2011)

- **PATRÓN** `ibs_20min` > `0.9124` → IC=+0.182 (n=579)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.9124 (IC base=+0.020)

- **PATRÓN** `dist_vwap_pct` < `0.1867` → IC=+0.231 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1867 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` < `1.0031` → IC=+0.249 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0031 (IC base=+0.020)

- **PATRÓN** `volumen_regimen` > `0.5875` → IC=+0.225 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.5875 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.0811` → IC=+0.262 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0811 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.3994` → IC=+0.270 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3994 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `1.7567` → IC=+0.239 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7567 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.257 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.020)

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
- **FILTRO** `ibs_20min` < `0.7451` → IC=-0.191 (n=1219)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7451
  - _Potencial_: sin este filtro IC_bueno=+0.279 (n=1220)

- **FILTRO** `ibs_20min` > `0.68` → IC=-0.236 (n=611)

  - _Acción_: SKIP cuando `ibs_20min` > 0.68
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=1842)

- **FILTRO** `sigma_ewma_delta_pct` > `4.71` → IC=-0.192 (n=534)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.71
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=1919)

- **PATRÓN** `ibs_20min` > `0.7451` → IC=+0.279 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7451 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.8456` → IC=+0.325 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8456 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.659` → IC=+0.168 (n=383)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.659 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8618` → IC=+0.309 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8618 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `0.6396` → IC=+0.298 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6396 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.0998` → IC=+0.298 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0998 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2703` → IC=+0.294 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2703 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.324 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4267 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.324 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.5783` → IC=+0.127 (n=1619)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.5783 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` < `0.2979` → IC=+0.229 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2979 (IC base=+0.018)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.255 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` < `0.0971` → IC=+0.222 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0971 (IC base=+0.018)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.237 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.018)

- **PATRÓN** `volumen_spike_ratio` < `2.4528` → IC=+0.239 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4528 (IC base=+0.018)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.252 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.018)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0169` → IC=+0.314 (n=970)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0169 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.298 (n=690)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.325 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7391 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2169` → IC=+0.316 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2169 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.662` → IC=+0.305 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.662 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.8621` → IC=+0.308 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8621 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` < `0.0784` → IC=+0.284 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0784 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.328 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `1.4303` → IC=+0.289 (n=1384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4303 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2452.9003` → IC=+0.290 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2452.9003 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.320 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.309 (n=1034)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.1979` → IC=+0.286 (n=682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1979 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.292 (n=528)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.1393` → IC=+0.333 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1393 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.3173` → IC=+0.290 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3173 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` < `0.231` → IC=+0.280 (n=1420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.231 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.095` → IC=+0.303 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.095 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.283 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `1.2435` → IC=+0.309 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2435 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.235` → IC=+0.331 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.235 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `1.4259` → IC=+0.289 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4259 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `2.1399` → IC=+0.279 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1399 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2399.3806` → IC=+0.282 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.3806 (IC base=+0.280)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.178 (n=2930)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0049 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.204 (n=2914)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.3629` → IC=+0.176 (n=7686)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.3629 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=9125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.221 (n=8739)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1761` → IC=+0.194 (n=3763)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1761 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.251 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.163 (n=5810)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2068 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.161 (n=5811)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6285 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.2419` → IC=+0.194 (n=1758)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2419 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.5578` → IC=+0.169 (n=3692)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.5578 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.6056` → IC=+0.174 (n=2797)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6056 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `1944.89` → IC=+0.171 (n=7803)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 1944.89 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.183 (n=7655)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 110.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.184 (n=5613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0067 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.0821` → IC=+0.211 (n=2802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0821 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=3218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.4839` → IC=+0.225 (n=8404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4839 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` < `0.1746` → IC=+0.163 (n=5886)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1746 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.323` → IC=+0.197 (n=1414)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.323 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.155 (n=6044)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1776 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.212 (n=1214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.5608` → IC=+0.171 (n=3394)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5608 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.6138` → IC=+0.172 (n=2571)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6138 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.178 (n=7374)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 110.0 (IC base=+0.169)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.220 (n=495)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.191 (n=493)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0083 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3426` → IC=+0.210 (n=1466)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3426 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=1548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.195 (n=986)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.301 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.308 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2301` → IC=+0.237 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2301 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.5417` → IC=+0.178 (n=1363)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 2.5417 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.185 (n=1363)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=1482)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.241 (n=984)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.247 (n=998)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.1881` → IC=+0.289 (n=743)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1881 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.248 (n=1069)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.3485` → IC=+0.260 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3485 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.305` → IC=+0.249 (n=1213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.305 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.235 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.256 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4233` → IC=+0.261 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4233 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1548.68` → IC=+0.251 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1548.68 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.242 (n=436)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.163)

- **PATRÓN** `drift_60min` |x|≤ `0.0729` → IC=+0.194 (n=436)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0729 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=1308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `ibs_20min` > `0.3965` → IC=+0.227 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3965 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.2016` → IC=+0.209 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2016 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.472` → IC=+0.229 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.472 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` < `1.2593` → IC=+0.167 (n=1306)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2593 (IC base=+0.163)

- **PATRÓN** `volumen_regimen` > `1.0769` → IC=+0.165 (n=592)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.0769 (IC base=+0.163)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.204 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.163)

- **PATRÓN** `volumen_spike_ratio` < `1.5005` → IC=+0.180 (n=558)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5005 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `10569.7673` → IC=+0.170 (n=1305)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10569.7673 (IC base=+0.163)

- **PATRÓN** `ballena_activa_n` < `383.0` → IC=+0.161 (n=1081)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 383.0 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.157 (n=1398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0057 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.2922` → IC=+0.164 (n=1396)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.2922 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.177 (n=465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.583` → IC=+0.189 (n=1396)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.583 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1332` → IC=+0.161 (n=1389)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1332 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.924` → IC=+0.208 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.924 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.2145` → IC=+0.157 (n=1396)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2145 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.149 (n=425)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.449` → IC=+0.146 (n=1284)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.449 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4235` → IC=+0.137 (n=1284)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4235 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.167 (n=403)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 211.0 (IC base=+0.138)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.223 (n=665)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.2456` → IC=+0.220 (n=974)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2456 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.276 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2018` → IC=+0.209 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2018 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.7565` → IC=+0.218 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7565 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.235 (n=1097)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1026` → IC=+0.254 (n=416)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1026 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.274 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.3506` → IC=+0.245 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3506 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.679` → IC=+0.252 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.679 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.354` → IC=+0.248 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.354 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7564` → IC=+0.224 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7564 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `3.318` → IC=+0.234 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.318 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1904.2616` → IC=+0.220 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.2616 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.214 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.217)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.178 (n=1236)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0066 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4327` → IC=+0.160 (n=1402)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4327 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.165 (n=1465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.3614` → IC=+0.197 (n=1401)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.3614 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1517` → IC=+0.176 (n=919)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.1517 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.936` → IC=+0.220 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.936 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `0.8559` → IC=+0.153 (n=935)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8559 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` > `0.6204` → IC=+0.147 (n=1402)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6204 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.101` → IC=+0.186 (n=594)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.101 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.160 (n=457)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.167 (n=457)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5222.8208` → IC=+0.187 (n=934)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 5222.8208 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.148 (n=1342)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 159.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.154 (n=1473)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.3831` → IC=+0.145 (n=1473)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3831 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.182 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.6524` → IC=+0.170 (n=1473)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6524 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.957` → IC=+0.163 (n=517)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.957 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.8528` → IC=+0.148 (n=982)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8528 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.177 (n=218)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.8129` → IC=+0.139 (n=900)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8129 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `9652.4338` → IC=+0.166 (n=668)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 9652.4338 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `155.0` → IC=+0.123 (n=1286)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 155.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.158 (n=723)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=1635)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.204 (n=1610)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.2883` → IC=+0.185 (n=885)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.2883 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.731` → IC=+0.250 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.731 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.132 (n=1595)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2036 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1634` → IC=+0.125 (n=1599)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1634 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.0979` → IC=+0.123 (n=606)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.0979 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.5419` → IC=+0.135 (n=677)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.5419 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=1660)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2872.7619` → IC=+0.198 (n=723)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2872.7619 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.138 (n=1242)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 48.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.160 (n=716)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0062 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1057` → IC=+0.166 (n=540)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1057 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=587)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5758` → IC=+0.213 (n=1619)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5758 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `1.0109` → IC=+0.128 (n=224)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 1.0109 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2097` → IC=+0.144 (n=1494)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2097 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.137` → IC=+0.135 (n=261)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 9.137 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6379` → IC=+0.146 (n=540)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6379 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2297` → IC=+0.160 (n=283)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2297 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4564` → IC=+0.142 (n=490)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.4564 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4253` → IC=+0.132 (n=490)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.4253 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2727.1824` → IC=+0.166 (n=734)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2727.1824 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.125 (n=1407)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 52.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.227 (n=1348)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.1357` → IC=+0.207 (n=503)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1357 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.208 (n=1576)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=683)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.7386` → IC=+0.262 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7386 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.5177` → IC=+0.217 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5177 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.238 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `1.1937` → IC=+0.206 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1937 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.216 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.261 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.1457` → IC=+0.213 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1457 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.4095` → IC=+0.210 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4095 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2433.9004` → IC=+0.207 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2433.9004 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.224 (n=520)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.215 (n=708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.0961` → IC=+0.228 (n=520)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0961 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=727)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.02` → IC=+0.299 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.02 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.1962` → IC=+0.231 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1962 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.392` → IC=+0.247 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.392 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `0.6338` → IC=+0.217 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6338 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.283 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1966` → IC=+0.199 (n=1245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1966 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4348` → IC=+0.203 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4348 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2369.6476` → IC=+0.211 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2369.6476 (IC base=+0.207)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.198 (n=746)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.170 (n=743)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0086 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3475` → IC=+0.167 (n=1959)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3475 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.200 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `0.5152` → IC=+0.197 (n=1989)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.5152 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.609` → IC=+0.178 (n=464)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.609 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.719` → IC=+0.188 (n=988)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.719 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.183 (n=1328)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.8725 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `1.2092` → IC=+0.165 (n=664)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.2092 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1634` → IC=+0.176 (n=606)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1634 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.4355` → IC=+0.177 (n=719)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4355 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8208` → IC=+0.165 (n=1437)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8208 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.167 (n=2526)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `2657.0511` → IC=+0.166 (n=1989)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2657.0511 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `147.0` → IC=+0.177 (n=2004)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 147.0 (IC base=+0.161)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.138 (n=1524)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0057 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.3455` → IC=+0.128 (n=2013)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3455 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=2139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.0589` → IC=+0.192 (n=762)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.0589 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2259` → IC=+0.122 (n=2081)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2259 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1653` → IC=+0.139 (n=574)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1653 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4453` → IC=+0.151 (n=737)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4453 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2768.8884` → IC=+0.121 (n=2042)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 2768.8884 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.132 (n=957)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 28.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.172 (n=248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0029 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.3302` → IC=+0.148 (n=563)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3302 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 8.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.6559` → IC=+0.208 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6559 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.2873` → IC=+0.167 (n=193)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2873 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.159 (n=256)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.623` → IC=+0.190 (n=188)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.623 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` < `0.1545` → IC=+0.137 (n=585)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` < 0.1545 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.0906` → IC=+0.140 (n=201)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.0906 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.2054` → IC=+0.145 (n=482)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.2054 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.494` → IC=+0.136 (n=490)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.494 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `10454.9515` → IC=+0.153 (n=563)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10454.9515 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `228.0` → IC=+0.160 (n=357)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 228.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.207 (n=237)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.34` → IC=+0.154 (n=710)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.34 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.6119` → IC=+0.181 (n=625)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.6119 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.3076` → IC=+0.147 (n=755)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.3076 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.41` → IC=+0.143 (n=267)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 4.41 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.162` → IC=+0.136 (n=647)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.162 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.2242` → IC=+0.142 (n=710)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2242 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `0.7151` → IC=+0.146 (n=634)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.7151 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1594` → IC=+0.206 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1594 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.1022` → IC=+0.154 (n=616)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1022 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.407` → IC=+0.141 (n=700)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.407 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `310.0` → IC=+0.149 (n=597)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 310.0 (IC base=+0.134)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.274 (n=308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.2112` → IC=+0.221 (n=467)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2112 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.224 (n=731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.9585` → IC=+0.271 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9585 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.149` → IC=+0.218 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.149 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2194` → IC=+0.211 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2194 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.948` → IC=+0.230 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.948 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.219 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8342 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.233 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1643 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.1538` → IC=+0.255 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1538 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.4055` → IC=+0.234 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4055 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.7615` → IC=+0.232 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7615 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.084` → IC=+0.153 (n=220)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.084 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` < `0.6885` → IC=+0.137 (n=290)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6885 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2242` → IC=+0.141 (n=104)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2242 (IC base=+0.091)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.150 (n=493)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0059 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.5425` → IC=+0.139 (n=552)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.5425 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.172 (n=510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.9964` → IC=+0.224 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9964 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.1938` → IC=+0.136 (n=449)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1938 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.489` → IC=+0.187 (n=289)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.489 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `1.069` → IC=+0.158 (n=486)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.069 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `0.7217` → IC=+0.142 (n=493)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.7217 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.1756` → IC=+0.156 (n=152)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1756 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `2.2097` → IC=+0.171 (n=241)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.2097 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.140 (n=579)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.02 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `3094.7708` → IC=+0.188 (n=184)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3094.7708 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.121 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0098 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.126 (n=172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 16.0 (IC base=+0.103)

- **PATRÓN** `ibs_20min` < `0.0427` → IC=+0.240 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0427 (IC base=+0.103)

- **PATRÓN** `volumen_regimen` < `1.2224` → IC=+0.125 (n=513)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2224 (IC base=+0.103)

- **PATRÓN** `volumen_spike_ratio` < `1.8403` → IC=+0.169 (n=324)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 1.8403 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2918.7797` → IC=+0.151 (n=233)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2918.7797 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.146 (n=458)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 39.0 (IC base=+0.103)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.176 (n=3763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0047 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.208 (n=3761)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=11782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.9972` → IC=+0.309 (n=3760)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9972 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.9326` → IC=+0.201 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9326 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.344` → IC=+0.246 (n=2816)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.344 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.88` → IC=+0.170 (n=5042)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.88 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2384` → IC=+0.198 (n=2085)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2384 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.5852` → IC=+0.192 (n=3624)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5852 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `1781.6665` → IC=+0.177 (n=11279)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 1781.6665 (IC base=+0.173)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.198 (n=8717)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 82.0 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.192 (n=6805)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1507` → IC=+0.191 (n=4489)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1507 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=3848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.4499` → IC=+0.246 (n=8977)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4499 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2524` → IC=+0.161 (n=6370)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.2524 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.071` → IC=+0.203 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.071 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.744` → IC=+0.183 (n=9861)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.744 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.705` → IC=+0.162 (n=3065)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.705 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2888` → IC=+0.239 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2888 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6081` → IC=+0.191 (n=3148)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6081 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.199 (n=6097)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 46.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.218 (n=629)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.196)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.210 (n=1258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.3604` → IC=+0.198 (n=1883)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3604 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.213 (n=898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.200 (n=1281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.626` → IC=+0.347 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.626 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.250 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `1.8459` → IC=+0.196 (n=1190)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8459 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.263 (n=670)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.261 (n=1523)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1277` → IC=+0.285 (n=669)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1277 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=1369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.4788` → IC=+0.286 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4788 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.502` → IC=+0.262 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.502 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.291 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.549` → IC=+0.257 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.549 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.622` → IC=+0.275 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.622 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1658.02` → IC=+0.271 (n=1357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1658.02 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.208 (n=604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.1134` → IC=+0.164 (n=796)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1134 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.3049` → IC=+0.207 (n=1806)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3049 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1279` → IC=+0.185 (n=1012)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1279 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.664` → IC=+0.176 (n=405)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.664 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.15` → IC=+0.157 (n=1640)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.15 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.628` → IC=+0.184 (n=603)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.628 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2657` → IC=+0.191 (n=263)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2657 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `2.1124` → IC=+0.163 (n=1540)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.1124 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.4063` → IC=+0.159 (n=1750)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.4063 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `11188.0133` → IC=+0.162 (n=1614)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11188.0133 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `281.0` → IC=+0.174 (n=746)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 281.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.162 (n=1550)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0057 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.3206` → IC=+0.160 (n=1549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.3206 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.183 (n=600)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.152 (n=707)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.2847` → IC=+0.234 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2847 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6645` → IC=+0.153 (n=246)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.6645 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.1329` → IC=+0.161 (n=1412)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.1329 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.52` → IC=+0.172 (n=260)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.52 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.327` → IC=+0.148 (n=1412)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.327 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.194` → IC=+0.160 (n=1549)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.194 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1513` → IC=+0.200 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1513 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4003` → IC=+0.156 (n=1451)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4003 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.757` → IC=+0.162 (n=967)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.757 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `413.0` → IC=+0.150 (n=1194)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 413.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.258 (n=614)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=1928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=1866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.349` → IC=+0.302 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.349 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` < `0.1337` → IC=+0.220 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1337 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.7698` → IC=+0.230 (n=1574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7698 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `1915.305` → IC=+0.226 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1915.305 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.238 (n=1721)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.6056` → IC=+0.235 (n=1721)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6056 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.232)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.236 (n=819)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0138` → IC=+0.300 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0138 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.774` → IC=+0.268 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.774 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.3408` → IC=+0.294 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3408 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` < `1.7349` → IC=+0.229 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7349 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.155` → IC=+0.237 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.155 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.242 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1904.8952` → IC=+0.240 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1904.8952 (IC base=+0.232)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.252 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.232)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.193 (n=643)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.436` → IC=+0.150 (n=1927)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.436 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=2011)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8688` → IC=+0.261 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8688 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.364` → IC=+0.161 (n=752)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.364 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.515` → IC=+0.167 (n=313)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.515 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8719` → IC=+0.158 (n=1285)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8719 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2353` → IC=+0.206 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2353 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5194` → IC=+0.156 (n=823)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5194 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1517` → IC=+0.154 (n=847)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1517 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7651.3805` → IC=+0.241 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7651.3805 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.172 (n=602)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 74.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.154 (n=1378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0066 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.357` → IC=+0.141 (n=1376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.357 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.15` → IC=+0.259 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.15 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1611` → IC=+0.133 (n=1359)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1611 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.258` → IC=+0.167 (n=232)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.258 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.148 (n=688)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6971 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `1.2022` → IC=+0.135 (n=521)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.2022 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.225 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.444` → IC=+0.141 (n=1490)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.444 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6506.899` → IC=+0.191 (n=709)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6506.899 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `172.0` → IC=+0.135 (n=1490)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 172.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.143 (n=1282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0082 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=1976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.463` → IC=+0.193 (n=1922)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.463 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0841` → IC=+0.203 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0841 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.558` → IC=+0.239 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.558 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8904` → IC=+0.143 (n=1282)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8904 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.1941` → IC=+0.130 (n=847)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.1941 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=1939)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2875.1364` → IC=+0.257 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2875.1364 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.140 (n=1492)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 52.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.178 (n=613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0058 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.136` → IC=+0.159 (n=613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.136 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=676)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.206 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.2229` → IC=+0.135 (n=1517)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.2229 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.449` → IC=+0.127 (n=1774)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.449 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.7144` → IC=+0.156 (n=810)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.7144 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.2212` → IC=+0.175 (n=287)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2212 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.4382` → IC=+0.145 (n=559)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4382 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `2755.5964` → IC=+0.180 (n=613)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2755.5964 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.129 (n=1469)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 51.0 (IC base=+0.116)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.229 (n=1700)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=1991)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.215 (n=1707)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.263 (n=1704)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.217` → IC=+0.236 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.217 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.219` → IC=+0.268 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.219 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `1.0608` → IC=+0.215 (n=1675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0608 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `0.64` → IC=+0.222 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.64 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.247 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.220 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4406 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1900)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `2430.6475` → IC=+0.220 (n=1700)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2430.6475 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.222 (n=671)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.018` → IC=+0.219 (n=1341)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.018 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.218 (n=1409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.4215` → IC=+0.264 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4215 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `1.2224` → IC=+0.214 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2224 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.2187` → IC=+0.211 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2187 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.262 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `1.2355` → IC=+0.237 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2355 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.270 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `2.1798` → IC=+0.202 (n=1606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1798 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.203 (n=1824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `2376.977` → IC=+0.208 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2376.977 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.196 (n=1730)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 37.0 (IC base=+0.206)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=3463)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.187 (n=3032)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0092 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.515` → IC=+0.183 (n=3444)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.515 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=1313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `0.945` → IC=+0.237 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.945 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.186` → IC=+0.183 (n=1238)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.186 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` < `0.4754` → IC=+0.170 (n=2188)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.4754 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.187` → IC=+0.200 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.187 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.170 (n=1011)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.7067 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.8929` → IC=+0.176 (n=1531)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.8929 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.1685` → IC=+0.205 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1685 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.4541` → IC=+0.183 (n=1135)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4541 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `1.8639` → IC=+0.182 (n=2266)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 1.8639 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.174 (n=2468)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `2462.763` → IC=+0.177 (n=3442)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2462.763 (IC base=+0.173)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.203 (n=870)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.4933` → IC=+0.171 (n=2609)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.4933 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.175 (n=1186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` < `0.1819` → IC=+0.183 (n=1148)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1819 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.6804` → IC=+0.180 (n=482)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6804 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.184` → IC=+0.166 (n=2605)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 6.184 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `1.2513` → IC=+0.158 (n=2445)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2513 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.161 (n=2379)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.5388` → IC=+0.165 (n=1134)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5388 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `1.8229` → IC=+0.162 (n=1718)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.8229 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=3463)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `12308.4211` → IC=+0.158 (n=870)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 12308.4211 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `83.0` → IC=+0.160 (n=1690)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 83.0 (IC base=+0.155)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.202 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.182 (n=375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0033 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0866` → IC=+0.232 (n=140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0866 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.193 (n=187)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5463` → IC=+0.206 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5463 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.1436` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1436 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2023` → IC=+0.184 (n=362)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.2023 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.129` → IC=+0.219 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.129 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.526` → IC=+0.188 (n=443)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.526 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.8386` → IC=+0.212 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8386 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2983` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2983 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.211 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6272` → IC=+0.204 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6272 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `12545.7532` → IC=+0.221 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12545.7532 (IC base=+0.182)

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
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.187 (n=212)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.006 (IC base=+0.166)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.179 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.01 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.5868` → IC=+0.172 (n=636)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.5868 (IC base=+0.166)

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

- **PATRÓN** `volumen_spike_ratio` > `1.8086` → IC=+0.171 (n=567)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8086 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `2429.8516` → IC=+0.203 (n=288)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.193 (n=476)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0047 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3766` → IC=+0.184 (n=951)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3766 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=408)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.189 (n=486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.5305` → IC=+0.192 (n=721)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.5305 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.8838` → IC=+0.191 (n=360)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.8838 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.3963` → IC=+0.188 (n=1017)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.3963 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.254` → IC=+0.188 (n=966)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 4.254 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.0856` → IC=+0.180 (n=951)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.0856 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `1.2511` → IC=+0.182 (n=360)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.2511 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.1655` → IC=+0.195 (n=326)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1655 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.4343` → IC=+0.188 (n=354)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4343 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.5168` → IC=+0.178 (n=948)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.5168 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=1075)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.200 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.184 (n=881)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=300)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.170 (n=594)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 10.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.748` → IC=+0.165 (n=881)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.748 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.0945` → IC=+0.165 (n=881)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.0945 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.6004` → IC=+0.180 (n=192)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6004 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.615` → IC=+0.165 (n=905)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 6.615 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.6472` → IC=+0.193 (n=294)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6472 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` > `0.7259` → IC=+0.162 (n=787)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.7259 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.175 (n=370)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.1956` → IC=+0.173 (n=760)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.1956 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `7807.1671` → IC=+0.178 (n=787)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 7807.1671 (IC base=+0.158)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.165 (n=299)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0112 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.145 (n=350)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 14.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.254 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.2317` → IC=+0.190 (n=227)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.2317 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.157` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.157 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.8918` → IC=+0.172 (n=227)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8918 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.2654` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.2654 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.227 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.4196` → IC=+0.166 (n=330)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4196 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=404)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `2978.1742` → IC=+0.164 (n=340)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2978.1742 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.162 (n=282)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 51.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.186 (n=285)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0069 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.6706` → IC=+0.181 (n=286)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.6706 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.163 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 16.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` < `0.1224` → IC=+0.235 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1224 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.6259` → IC=+0.234 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6259 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.258` → IC=+0.169 (n=276)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 5.258 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `1.3627` → IC=+0.170 (n=286)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.3627 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.225 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `1.5095` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.5095 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `2.1901` → IC=+0.172 (n=126)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1901 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `3143.016` → IC=+0.200 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3143.016 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.204 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.160)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0064` → IC=-0.190 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=426)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.174 (n=467)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0039 (IC base=+0.084)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.124 (n=964)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 8.0 (IC base=+0.084)

- **PATRÓN** `ibs_20min` > `0.6471` → IC=+0.189 (n=865)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.6471 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1483` → IC=+0.147 (n=519)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1483 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.190 (n=227)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.192 (n=131)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `1380.3758` → IC=+0.123 (n=629)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1380.3758 (IC base=+0.084)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.124 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0033 (IC base=+0.030)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.301 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.1816` → IC=+0.133 (n=393)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1816 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.036` → IC=+0.140 (n=134)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 3.036 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1373` → IC=+0.212 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1373 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.5298` → IC=+0.143 (n=289)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.5298 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `1.437` → IC=+0.135 (n=258)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.437 (IC base=+0.030)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.133 (n=298)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.030)

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

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.128 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0045 (IC base=+0.077)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.173 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.279` → IC=+0.252 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.279 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.0673` → IC=+0.143 (n=169)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.0673 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.92` → IC=+0.181 (n=155)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.92 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.9523` → IC=+0.134 (n=140)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.9523 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.0669` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0669 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `2.0636` → IC=+0.183 (n=121)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.0636 (IC base=+0.077)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6741` → IC=-0.136 (n=141)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6741
  - _Potencial_: sin este filtro IC_bueno=+0.221 (n=292)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=138)

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

- **PATRÓN** `ibs_20min` < `0.1891` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1891 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` < `0.1303` → IC=+0.140 (n=112)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1303 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.256` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.256 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.1312` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1312 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.1755` → IC=+0.182 (n=42)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.1755 (IC base=+0.009)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.009)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.01` → IC=-0.269 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=99)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.230 (n=72)

- **PATRÓN** `ibs_20min` > `0.7826` → IC=+0.188 (n=206)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7826 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0104` → IC=+0.134 (n=69)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 1.0104 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.104` → IC=+0.140 (n=87)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 8.104 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.2389` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2389 (IC base=+0.057)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.149 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0066 (IC base=-0.023)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.230 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=-0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.757` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.757 (IC base=-0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=-0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.4444 (IC base=-0.023)

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
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=260)

- **FILTRO** `dist_vwap_pct` > `0.6226` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6226
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=366)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.159 (n=130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0059 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.6429` → IC=+0.153 (n=286)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.6429 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.512` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.512 (IC base=+0.085)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.128 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.004 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.179 (n=260)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.1622 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.0` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 6.0 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `3771.3449` → IC=+0.184 (n=134)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 3771.3449 (IC base=+0.077)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=101)

- **FILTRO** `ibs_20min` < `0.5964` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5964
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=93)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.174 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0034 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.211 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.098` → IC=+0.219 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.098 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.0669` → IC=+0.150 (n=141)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.0669 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.794` → IC=+0.150 (n=121)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 6.794 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1443` → IC=+0.152 (n=136)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1443 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` < `0.1907` → IC=+0.192 (n=102)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1907 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.6881` → IC=+0.189 (n=104)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.6881 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.160 (n=104)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.137)

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
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=811)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2901.0854` → IC=+0.166 (n=279)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2901.0854 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2335.1174` → IC=+0.120 (n=864)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 2335.1174 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.121 (n=811)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2901.0854` → IC=+0.166 (n=279)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2901.0854 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2335.1174` → IC=+0.120 (n=864)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 2335.1174 (IC base=+0.101)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=2040)

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

- **PATRÓN** `liq_usd_total` > `59740.4` → IC=+0.147 (n=117)

  - _Acción_: Kelly boost +0.74€ cuando `liq_usd_total` > 59740.4 (IC base=+0.025)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=475)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=209)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.495 (IC base=+0.020)

- **PATRÓN** `libro_liquidez` > `3951.8303` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3951.8303 (IC base=+0.020)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=685)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=685)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=417)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=417)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=184)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=184)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=398)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=1031)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **PATRÓN** `py_entrada` > `0.52` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.52 (IC base=+0.016)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.59` → IC=+0.120 (n=135)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.59 (IC base=+0.058)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `restante_min` > `13.33` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `restante_min` > 13.33
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=64)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=72)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.153 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 9.0 (IC base=+0.091)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.132 (n=85)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=33)

- **FILTRO** `profundidad_ratio` < `54.8` → IC=-0.250 (n=38)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.8
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=80)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=108)

- **FILTRO** `profundidad_ratio` < `9.5` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `profundidad_ratio` < 9.5
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=102)

- **PATRÓN** `py_entrada` > `0.53` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.53 (IC base=-0.033)

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

- **PATRÓN** `profundidad_ratio` > `10.3` → IC=+0.129 (n=103)

  - _Acción_: Kelly boost +0.64€ cuando `profundidad_ratio` > 10.3 (IC base=+0.068)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **PATRÓN** `restante_min` > `13.44` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 13.44 (IC base=+0.015)

- **PATRÓN** `lag_apertura_s` < `91.0` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 91.0 (IC base=+0.015)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.136 (n=108)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=61)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.5 (IC base=-0.021)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.259 (n=56)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=146)

- **FILTRO** `restante_min` < `3.26` → IC=-0.127 (n=65)

  - _Acción_: SKIP cuando `restante_min` < 3.26
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=137)

- **FILTRO** `lag_apertura_s` > `102.62` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `lag_apertura_s` > 102.62
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=134)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.166 (n=3917)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=12066)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.162 (n=4046)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=12513)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.202 (n=683)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=2112)

- **PATRÓN** `libro_liquidez` > `1554.47` → IC=+0.134 (n=1007)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1554.47 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.183 (n=695)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2156)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=711)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2272)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.170 (n=682)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=2112)

- **FILTRO** `py_entrada` > `0.56` → IC=-0.171 (n=731)

  - _Acción_: SKIP cuando `py_entrada` > 0.56
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=2253)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2223)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2341)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3081)

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
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=689)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ballena_activa_n` > `89.0` → IC=-0.218 (n=115)

  - _Acción_: SKIP cuando `ballena_activa_n` > 89.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=227)

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
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=24984)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.275 (n=9007)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=27251)

- **FILTRO** `ibs_7min` < `0.2723` → IC=-0.235 (n=9064)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2723
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=27194)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=12092)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=24166)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.231 (n=11210)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=34670)

- **FILTRO** `ibs_7min` > `0.2917` → IC=-0.179 (n=11445)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2917
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=34435)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.140 (n=1836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=4237)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=1452)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4621)

- **FILTRO** `ibs_7min` < `0.7087` → IC=-0.254 (n=2004)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7087
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=4069)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.178 (n=1465)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4608)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.261 (n=1950)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=5947)

- **FILTRO** `ibs_7min` > `0.789` → IC=-0.207 (n=1974)

  - _Acción_: SKIP cuando `ibs_7min` > 0.789
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=5923)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.142 (n=1476)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=4751)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.252 (n=1517)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4710)

- **FILTRO** `ibs_7min` < `0.7461` → IC=-0.197 (n=1556)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7461
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=4671)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.181 (n=1555)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4672)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=1467)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=4881)

- **FILTRO** `ibs_7min` > `0.2617` → IC=-0.185 (n=1586)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2617
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=4762)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.181 (n=1583)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=4765)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.163 (n=1640)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=4140)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.304 (n=1434)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=4346)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.243 (n=1900)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3880)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.210 (n=1410)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4370)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.245 (n=1948)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=6508)

- **FILTRO** `ibs_7min` > `0.7465` → IC=-0.176 (n=2113)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7465
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=6343)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.241 (n=1464)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4504)

- **FILTRO** `ibs_7min` < `0.7406` → IC=-0.180 (n=1492)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7406
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4476)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.173 (n=1445)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=4523)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.256 (n=1527)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4612)

- **FILTRO** `ibs_7min` > `0.2759` → IC=-0.175 (n=1532)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2759
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4607)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.180 (n=1506)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4633)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.262 (n=1478)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4757)

- **FILTRO** `ibs_7min` < `0.2778` → IC=-0.233 (n=1558)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2778
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=4677)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.169 (n=2173)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=6583)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.272 (n=1473)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=4502)

- **FILTRO** `ibs_7min` < `0.285` → IC=-0.224 (n=1493)

  - _Acción_: SKIP cuando `ibs_7min` < 0.285
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=4482)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.215 (n=1410)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=4565)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.208 (n=1937)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=6347)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=1158)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=573)

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
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.131 (n=821)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=736)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.115)

- **PATRÓN** `total_vol_5m` < `459.6089` → IC=+0.149 (n=274)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 459.6089 (IC base=+0.115)

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

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 11.0 (IC base=+0.108)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4139` → IC=+0.181 (n=114)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.91€ cuando `delta_ratio` |x|> 0.4139 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.178 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 16.0 (IC base=+0.100)

- **PATRÓN** `total_vol_5m` < `390.044` → IC=+0.218 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 390.044 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.175 (n=75)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 74.0 (IC base=+0.100)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3989` → IC=+0.174 (n=142)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.3989 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.240 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `6100.528` → IC=+0.153 (n=125)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 6100.528 (IC base=+0.128)

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
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.222 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=27)

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

- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.400 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=90)

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
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=448)

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
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=676)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1248)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=830)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=807)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=3131)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1581)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1589)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.194 (n=610)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0043 (IC base=+0.190)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.229 (n=610)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.0727` → IC=+0.200 (n=805)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0727 (IC base=+0.190)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.193 (n=610)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.190)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.236 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=1707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.192 (n=1905)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.190)

- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.270 (n=1829)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6111 (IC base=+0.190)

- **PATRÓN** `dist_vwap_pct` > `0.1199` → IC=+0.190 (n=926)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1199 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.77` → IC=+0.277 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.77 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `8758.4418` → IC=+0.201 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8758.4418 (IC base=+0.190)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=768)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.223 (n=409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.0602` → IC=+0.284 (n=137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0602 (IC base=+0.211)

- **PATRÓN** `drift_15min` |x|≤ `0.3844` → IC=+0.212 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3844 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.255` → IC=+0.246 (n=136)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.255 (IC base=+0.211)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4004` → IC=+0.246 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4004 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=380)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` > `0.7112` → IC=+0.276 (n=409)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7112 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.3824` → IC=+0.275 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3824 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.199` → IC=+0.280 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.199 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `16045.3097` → IC=+0.241 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16045.3097 (IC base=+0.211)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6559` → IC=-0.123 (n=189)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6559
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=386)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.178 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0035 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.141 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.005 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0673` → IC=+0.156 (n=190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0673 (IC base=+0.133)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.178 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.133)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1229` → IC=+0.171 (n=159)

  - _Acción_: Kelly boost +0.85€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1229 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.136 (n=432)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 16.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.6559` → IC=+0.258 (n=386)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6559 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1597` → IC=+0.146 (n=340)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1597 (IC base=+0.133)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0234 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.227 (n=207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.198)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0403` → IC=+0.201 (n=470)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0403 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0893` → IC=+0.264 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0893 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.231 (n=232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.5695` → IC=+0.288 (n=470)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5695 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.3602` → IC=+0.213 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3602 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.188` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.188 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.799` → IC=+0.199 (n=476)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 10.799 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2910.1242` → IC=+0.274 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2910.1242 (IC base=+0.198)

- **PATRÓN** `ibs_15` < `0.1176` → IC=+0.149 (n=528)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1176 (IC base=+0.053)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.359 (n=303)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.352)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.377 (n=152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.352)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.352 (n=303)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.352)

- **PATRÓN** `drift_15min` |x|≤ `0.4111` → IC=+0.351 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4111 (IC base=+0.352)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0703` → IC=+0.364 (n=453)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0703 (IC base=+0.352)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.391 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.352)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.371 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.352)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.390 (n=454)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.352)

- **PATRÓN** `dist_vwap_pct` > `0.4241` → IC=+0.392 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4241 (IC base=+0.352)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.66` → IC=+0.360 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.66 (IC base=+0.352)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.954` → IC=+0.353 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.954 (IC base=+0.352)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.354 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.352)

- **PATRÓN** `libro_liquidez` > `3425.1488` → IC=+0.364 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3425.1488 (IC base=+0.352)

- **PATRÓN** `ballena_activa_n` < `457.0` → IC=+0.373 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 457.0 (IC base=+0.352)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.1164` → IC=+0.358 (n=111)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.1164 (IC base=+0.357)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.365 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.357)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.384 (n=84)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.357)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.372 (n=84)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.357)

- **PATRÓN** `drift_15min` |x|≤ `0.4185` → IC=+0.367 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4185 (IC base=+0.357)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.376 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.357)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.13` → IC=+0.398 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.13 (IC base=+0.357)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.383 (n=254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.357)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.389 (n=251)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.357)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.408 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.859` → IC=+0.362 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.859 (IC base=+0.357)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.922` → IC=+0.360 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.922 (IC base=+0.357)

- **PATRÓN** `libro_liquidez` > `11137.3038` → IC=+0.376 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11137.3038 (IC base=+0.357)

- **PATRÓN** `ballena_activa_n` < `568.0` → IC=+0.402 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 568.0 (IC base=+0.357)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.384 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.343)

- **PATRÓN** `drift_60min` |x|≤ `0.1039` → IC=+0.348 (n=136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1039 (IC base=+0.343)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.364 (n=182)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.343)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.372 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.407 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.343)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.393 (n=204)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.343)

- **PATRÓN** `dist_vwap_pct` > `0.4534` → IC=+0.381 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4534 (IC base=+0.343)

- **PATRÓN** `dist_vwap_pct` < `0.1197` → IC=+0.344 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1197 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.031` → IC=+0.353 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.031 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.77` → IC=+0.348 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.77 (IC base=+0.343)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.347 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.343)

- **PATRÓN** `libro_liquidez` > `3456.6166` → IC=+0.355 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3456.6166 (IC base=+0.343)

- **PATRÓN** `ballena_activa_n` < `152.0` → IC=+0.351 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 152.0 (IC base=+0.343)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0126` → IC=-0.222 (n=721)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0126
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2164)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.205 (n=993)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1892)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1363` → IC=+0.248 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1363 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6423` → IC=+0.272 (n=696)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6423 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.190 (n=562)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.122` → IC=+0.250 (n=1369)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.122 (IC base=-0.028)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1809` → IC=+0.244 (n=1332)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1809 (IC base=-0.028)

- **PATRÓN** `ibs_15` < `0.3514` → IC=+0.274 (n=2053)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3514 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.6848` → IC=+0.297 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6848 (IC base=-0.028)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0472` → IC=-0.216 (n=1178)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0472
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=581)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.228 (n=439)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1320)

- **FILTRO** `sigma_ewma_delta_pct` > `19.521` → IC=-0.255 (n=312)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.521
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=1447)

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

- **PATRÓN** `ibs_15` < `0.199` → IC=+0.382 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.199 (IC base=-0.199)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.417 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.199)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=424)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.149 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0068 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.168 (n=296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0041 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.216 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.146)

- **PATRÓN** `drift_15min` |x|≤ `0.4178` → IC=+0.173 (n=111)

  - _Acción_: Kelly boost +0.86€ cuando `drift_15min` |x|≤ 0.4178 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.148 (n=296)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.228 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.172 (n=239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.6642` → IC=+0.260 (n=331)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6642 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.146 (n=94)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.1047` → IC=+0.176 (n=236)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1047 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.1` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 23.1 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=424)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `10966.626` → IC=+0.178 (n=150)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 10966.626 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.248 (n=801)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0076 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.4422` → IC=+0.237 (n=801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4422 (IC base=+0.233)

- **PATRÓN** `drift_15min` |x|≤ `0.4752` → IC=+0.258 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4752 (IC base=+0.233)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2077` → IC=+0.253 (n=363)
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

- **PATRÓN** `dist_vwap_pct` > `0.7528` → IC=+0.319 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7528 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.01` → IC=+0.258 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.01 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.366` → IC=+0.238 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.366 (IC base=+0.233)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.222 (n=340)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=341)

- **FILTRO** `drift_60min` |x|> `0.1702` → IC=-0.225 (n=231)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1702
  - _Potencial_: sin este filtro IC_bueno=-0.146 (n=450)

- **FILTRO** `drift_15min` |x|> `0.8935` → IC=-0.267 (n=170)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8935
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=511)

- **FILTRO** `sigma_ewma_delta_pct` > `18.184` → IC=-0.138 (n=363)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.184
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=2930)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.192 (n=50)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.5625 (IC base=-0.173)

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
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.306 (n=492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0563` → IC=+0.327 (n=246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0563 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.302 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2224` → IC=+0.323 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2224 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8405` → IC=+0.328 (n=737)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8405 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.4333` → IC=+0.340 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4333 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.34` → IC=+0.345 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.34 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12879.5491` → IC=+0.301 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12879.5491 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.296 (n=356)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0046 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.339 (n=135)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.287)

- **PATRÓN** `drift_15min` |x|≤ `0.4205` → IC=+0.289 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4205 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2603` → IC=+0.310 (n=135)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2603 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.312 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.827` → IC=+0.316 (n=405)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.827 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.4105` → IC=+0.362 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4105 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.916` → IC=+0.371 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.916 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16060.5409` → IC=+0.332 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16060.5409 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.307 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.314 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1481` → IC=+0.299 (n=222)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1481 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.329 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.314 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8539` → IC=+0.342 (n=333)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8539 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.300 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` < `0.1658` → IC=+0.294 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1658 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.332 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.297 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2527` → IC=-0.162 (n=72)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2527
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=219)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1149` → IC=-0.162 (n=72)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1149
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=219)

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
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0702` → IC=-0.127 (n=57)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0702
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=116)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1259` → IC=-0.167 (n=43)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1259
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=130)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6111 sube el IC de +0.190 a +0.270 en UPDOWN_GBM#15min (n=1829). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7112 sube el IC de +0.211 a +0.276 en UPDOWN_GBM#BTC#15min (n=409). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6559 sube el IC de +0.133 a +0.258 en UPDOWN_GBM#ETH#15min (n=386). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.6 sube el IC de +0.177 a +0.258 en UPDOWN_GBM#SOL#15min (n=217). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5695 sube el IC de +0.198 a +0.288 en UPDOWN_GBM#XRP#15min (n=470). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6423 sube el IC de -0.066 a +0.272 en UPDOWN_GBM_15M_TARDIO (n=696). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3514 sube el IC de -0.028 a +0.274 en UPDOWN_GBM_15M_TARDIO (n=2053). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7497 sube el IC de +0.082 a +0.324 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=203). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.199 sube el IC de -0.199 a +0.382 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6642 sube el IC de +0.146 a +0.260 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=331). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2756 sube el IC de +0.233 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=705). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.173 a +0.192 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=50). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.041 a +0.261 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=354). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3391 sube el IC de -0.039 a +0.304 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=530). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8405 sube el IC de +0.292 a +0.328 en UPDOWN_GBM_IBS_ALTO (n=737). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.827 sube el IC de +0.287 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=405). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8539 sube el IC de +0.295 a +0.342 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=333). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.352 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=454). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.357 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=251). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.343 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=204). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.090 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1409 | +0.100 | +200.95€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1409 | +0.100 | +200.95€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1063 | +0.108 | +172.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1063 | +0.108 | +172.09€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 6 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.145 | +20.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.145 | +20.16€ | 0 | 7 |
| ✅ BALLENAS_TARDIAS | 30386 | -0.084 | -4018.19€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1590 | -0.026 | -213.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 28796 | -0.087 | -3804.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 3925 | -0.098 | -639.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 3925 | -0.098 | -639.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1590 | -0.026 | -213.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1590 | -0.026 | -213.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3578 | -0.099 | -806.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3578 | -0.099 | -806.43€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 7897 | -0.016 | -760.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 7897 | -0.016 | -760.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7417 | -0.090 | -462.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7417 | -0.090 | -462.14€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 5979 | -0.165 | -1135.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 5979 | -0.165 | -1135.88€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 21236 | -0.024 | +3852.88€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5500 | +0.001 | +1787.56€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 15736 | -0.033 | +2065.32€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 21236 | -0.024 | +3852.88€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5500 | +0.001 | +1787.56€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 15736 | -0.033 | +2065.32€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 102287 | +0.112 | -5010.54€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 14981 | +0.184 | -456.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 421 | -0.067 | -54.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 80372 | +0.100 | -4263.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6513 | +0.106 | -235.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 13359 | +0.100 | -1049.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 48 | -0.160 | +1.58€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 13296 | +0.101 | -1039.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 20550 | +0.131 | -370.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4661 | +0.202 | -127.49€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 13327 | +0.113 | -182.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2520 | +0.098 | -37.45€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13398 | +0.090 | -1203.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 55 | -0.114 | -9.21€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 13328 | +0.091 | -1183.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 21725 | +0.124 | -411.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 5878 | +0.176 | -76.04€ | 1 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13474 | +0.105 | -264.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2361 | +0.099 | -62.15€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 19885 | +0.113 | -1174.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4290 | +0.187 | -254.76€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 324 | -0.028 | -1.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 13639 | +0.091 | -783.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1632 | +0.129 | -135.57€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13370 | +0.099 | -801.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 49 | -0.029 | +9.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 13308 | +0.100 | -810.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 16256 | +0.194 | -1020.84€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 16256 | +0.194 | -1020.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3831 | +0.168 | -396.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3831 | +0.168 | -396.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1531 | +0.207 | -0.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1531 | +0.207 | -0.62€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3774 | +0.181 | -311.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3774 | +0.181 | -311.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3330 | +0.242 | -100.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3330 | +0.242 | -100.56€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3711 | +0.192 | -225.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3711 | +0.192 | -225.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 761 | +0.429 | -22.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 761 | +0.429 | -22.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 295 | +0.439 | -1.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 295 | +0.439 | -1.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 289 | +0.428 | -8.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 289 | +0.428 | -8.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 165 | +0.410 | -9.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 165 | +0.410 | -9.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 56235 | +0.198 | -4361.79€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 56235 | +0.198 | -4361.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 9690 | +0.178 | -1095.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 9690 | +0.178 | -1095.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9006 | +0.222 | -338.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9006 | +0.222 | -338.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 9708 | +0.174 | -1126.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 9708 | +0.174 | -1126.76€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9095 | +0.217 | -373.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9095 | +0.217 | -373.73€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9307 | +0.203 | -614.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9307 | +0.203 | -614.34€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9429 | +0.193 | -812.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9429 | +0.193 | -812.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 21307 | +0.116 | +143.56€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 21307 | +0.116 | +143.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 10581 | +0.119 | +117.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 10581 | +0.119 | +117.43€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 10726 | +0.113 | +26.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 10726 | +0.113 | +26.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1592 | +0.288 | -26.10€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1592 | +0.288 | -26.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 710 | +0.278 | -18.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 710 | +0.278 | -18.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 768 | +0.287 | -10.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 768 | +0.287 | -10.68€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 114 | +0.345 | +3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 114 | +0.345 | +3.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 705 | +0.435 | -5.16€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 705 | +0.435 | -5.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 337 | +0.432 | -4.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 337 | +0.432 | -4.94€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 323 | +0.439 | -0.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 323 | +0.439 | -0.62€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1215 | +0.068 | -61.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 430 | +0.051 | -40.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 785 | +0.077 | -21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 64 | +0.121 | +3.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 956 | +0.075 | -29.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 171 | +0.067 | -8.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 785 | +0.077 | -21.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 195 | +0.013 | -35.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 195 | +0.013 | -35.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 40122 | +0.098 | -1155.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3290 | +0.087 | +11.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 36832 | +0.099 | -1166.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 22399 | +0.102 | -343.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3290 | +0.087 | +11.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 19109 | +0.104 | -354.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 7725 | +0.109 | -11.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 7725 | +0.109 | -11.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 9998 | +0.080 | -801.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 9998 | +0.080 | -801.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 849 | +0.214 | -101.09€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 849 | +0.214 | -101.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 849 | +0.214 | -101.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 849 | +0.214 | -101.09€ | 2 | 4 |
| ✅ GBM_LATE_15M | 28440 | +0.085 | +13855.83€ | 0 | 15 |
| ✅ GBM_LATE_15M#15min | 28440 | +0.085 | +13855.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4761 | +0.197 | +3544.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4761 | +0.197 | +3544.30€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 4234 | +0.179 | +3028.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4234 | +0.179 | +3028.29€ | 0 | 28 |
| ✅ GBM_LATE_15M#DOGE | 5008 | +0.198 | +3734.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5008 | +0.198 | +3734.32€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 4105 | +0.027 | +979.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4105 | +0.027 | +979.86€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 4055 | -0.033 | +924.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4055 | -0.033 | +924.37€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6277 | -0.040 | +1644.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6277 | -0.040 | +1644.69€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 30299 | +0.086 | +16069.87€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 30299 | +0.086 | +16069.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 5776 | +0.013 | +3041.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 5776 | +0.013 | +3041.15€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6320 | +0.015 | +1351.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6320 | +0.015 | +1351.69€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4309 | +0.265 | +4386.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4309 | +0.265 | +4386.17€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 4996 | +0.006 | +1011.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 4996 | +0.006 | +1011.93€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 4892 | +0.031 | +1940.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 4892 | +0.031 | +1940.47€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4006 | +0.280 | +4338.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4006 | +0.280 | +4338.47€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 22849 | +0.170 | +17389.45€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 22849 | +0.170 | +17389.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3439 | +0.210 | +2779.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3439 | +0.210 | +2779.28€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3600 | +0.150 | +2658.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3600 | +0.150 | +2658.96€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3607 | +0.210 | +2893.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3607 | +0.210 | +2893.47€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 3831 | +0.133 | +2727.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 3831 | +0.133 | +2727.84€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4284 | +0.119 | +3072.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4284 | +0.119 | +3072.94€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4088 | +0.205 | +3256.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4088 | +0.205 | +3256.97€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6015 | +0.137 | +2772.55€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6015 | +0.137 | +2772.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 212 | +0.112 | +86.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1696 | +0.135 | +845.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1696 | +0.135 | +845.25€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1809 | +0.152 | +871.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1809 | +0.152 | +871.71€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1418 | +0.120 | +576.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1418 | +0.120 | +576.25€ | 0 | 20 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 28639 | +0.177 | +21781.94€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 28639 | +0.177 | +21781.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4535 | +0.224 | +3893.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4535 | +0.224 | +3893.89€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4473 | +0.151 | +2995.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4473 | +0.151 | +2995.79€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4746 | +0.226 | +4088.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4746 | +0.226 | +4088.04€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4653 | +0.135 | +3231.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4653 | +0.135 | +3231.58€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5013 | +0.117 | +3372.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5013 | +0.117 | +3372.06€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5219 | +0.210 | +4200.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5219 | +0.210 | +4200.58€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8067 | +0.166 | +5156.27€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 8067 | +0.166 | +5156.27€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 825 | +0.226 | +709.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 1842 | +0.152 | +1256.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 1842 | +0.152 | +1256.21€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 921 | +0.172 | +587.54€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 921 | +0.172 | +587.54€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2614 | +0.169 | +1646.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2614 | +0.169 | +1646.66€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 833 | +0.150 | +454.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 833 | +0.150 | +454.81€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_60M | 1978 | +0.069 | +756.03€ | 1 | 15 |
| ✅ GBM_LATE_60M#60min | 1978 | +0.069 | +756.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 730 | +0.091 | +275.14€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 730 | +0.091 | +275.14€ | 0 | 13 |
| ✅ GBM_LATE_60M#ETH | 647 | +0.072 | +301.82€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 647 | +0.072 | +301.82€ | 2 | 15 |
| ✅ GBM_LATE_60M#SOL | 601 | +0.037 | +179.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 601 | +0.037 | +179.07€ | 2 | 9 |
| 🚫 GBM_LATE_60M_FADE | 409 | -0.254 | -21.79€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 409 | -0.254 | -21.79€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 153 | -0.223 | -7.57€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 153 | -0.223 | -7.57€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 136 | -0.254 | -7.60€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 136 | -0.254 | -7.60€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 120 | -0.287 | -6.62€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 120 | -0.287 | -6.62€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 774 | +0.081 | +181.35€ | 2 | 7 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 774 | +0.081 | +181.35€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 303 | +0.070 | +63.08€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 303 | +0.070 | +63.08€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 234 | +0.047 | +18.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 234 | +0.047 | +18.86€ | 3 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 237 | +0.128 | +99.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 237 | +0.128 | +99.41€ | 1 | 11 |
| ✅ LATE_WINDOW_5MIN | 107 | +0.262 | +91.86€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 107 | +0.262 | +91.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 107 | +0.262 | +91.86€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 107 | +0.262 | +91.86€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2264 | +0.104 | +617.50€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2264 | +0.104 | +617.50€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2264 | +0.104 | +617.50€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2264 | +0.104 | +617.50€ | 0 | 3 |
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
| ✅ LIQUIDACIONES_5M | 2239 | +0.012 | +31.13€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2239 | +0.012 | +31.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 119 | +0.021 | -2.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 119 | +0.021 | -2.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 269 | -0.002 | +12.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 269 | -0.002 | +12.26€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 176 | -0.022 | -5.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 176 | -0.022 | -5.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 922 | +0.023 | +22.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 922 | +0.023 | +22.12€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 515 | +0.011 | +0.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 515 | +0.011 | +0.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 238 | +0.008 | +4.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 238 | +0.008 | +4.37€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1197 | -0.042 | -25.52€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1197 | -0.042 | -25.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 339 | -0.040 | -12.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 339 | -0.040 | -12.25€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 406 | -0.027 | -0.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 406 | -0.027 | -0.86€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 452 | -0.057 | -12.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 452 | -0.057 | -12.40€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 2757 | -0.011 | +87.85€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1307 | -0.014 | +37.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1450 | -0.009 | +50.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 83 | +0.029 | +9.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 44 | +0.065 | +9.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 39 | -0.012 | -0.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 651 | +0.004 | +37.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 302 | +0.000 | +11.97€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 349 | +0.007 | +25.16€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 338 | -0.012 | +15.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 163 | -0.045 | -3.25€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 175 | +0.020 | +18.26€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 546 | -0.029 | -13.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 254 | -0.035 | -10.44€ | 4 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 292 | -0.024 | -2.97€ | 5 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 518 | -0.011 | +22.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 253 | -0.010 | +16.53€ | 0 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 265 | -0.013 | +5.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 621 | -0.017 | +17.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 291 | -0.009 | +12.91€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 330 | -0.024 | +4.30€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 32542 | -0.006 | +1449.66€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 32542 | -0.006 | +1449.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 5754 | +0.020 | +720.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 5754 | +0.020 | +720.15€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 4958 | -0.031 | -80.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 4958 | -0.031 | -80.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 5834 | +0.016 | +519.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 5834 | +0.016 | +519.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4742 | -0.053 | -159.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4742 | -0.053 | -159.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5476 | -0.009 | +204.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5476 | -0.009 | +204.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 5778 | +0.010 | +245.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 5778 | +0.010 | +245.53€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6022 | -0.061 | -154.68€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6022 | -0.061 | -154.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1451 | -0.086 | -43.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1451 | -0.086 | -43.67€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 684 | -0.124 | -31.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 684 | -0.124 | -31.11€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1772 | -0.079 | -35.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1772 | -0.079 | -35.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 854 | -0.015 | -25.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 854 | -0.015 | -25.03€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3346 | +0.004 | -3.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3346 | +0.004 | -3.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 189 | +0.013 | -1.05€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 189 | +0.013 | -1.05€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 137 | -0.004 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 137 | -0.004 | -2.36€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1316 | +0.007 | +7.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1316 | +0.007 | +7.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1388 | +0.007 | +0.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1388 | +0.007 | +0.29€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 188 | -0.011 | -6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 82138 | -0.072 | +1772.13€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 82138 | -0.072 | +1772.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 13970 | -0.076 | +830.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 13970 | -0.076 | +830.03€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 12575 | -0.095 | -643.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 12575 | -0.095 | -643.00€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 14236 | -0.067 | +755.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 14236 | -0.067 | +755.17€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 12107 | -0.092 | -196.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 12107 | -0.092 | -196.92€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 14991 | -0.049 | +392.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 14991 | -0.049 | +392.02€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 14259 | -0.063 | +634.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 14259 | -0.063 | +634.84€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7825 | -0.028 | -141.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7825 | -0.028 | -141.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1792 | -0.036 | -12.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1792 | -0.036 | -12.15€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2212 | -0.024 | -32.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2212 | -0.024 | -32.40€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1064 | -0.045 | -20.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1064 | -0.045 | -20.27€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 758 | -0.022 | -25.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 758 | -0.022 | -25.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1229 | +0.108 | +417.97€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#5min | 1093 | +0.115 | +405.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 247 | +0.131 | +116.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 247 | +0.131 | +116.42€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 210 | +0.108 | +59.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 210 | +0.108 | +59.77€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 228 | +0.100 | +79.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 228 | +0.100 | +79.85€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 189 | +0.128 | +84.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 189 | +0.128 | +84.41€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 219 | +0.102 | +64.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 219 | +0.102 | +64.94€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 636 | -0.039 | -42.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 636 | -0.039 | -42.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 128 | -0.008 | +2.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 128 | -0.008 | +2.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 86 | -0.057 | -8.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 86 | -0.057 | -8.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 185 | -0.056 | -21.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 185 | -0.056 | -21.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 130 | -0.015 | -3.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 130 | -0.015 | -3.33€ | 0 | 0 |
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
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 174 | -0.176 | +14.88€ | 4 | 1 |
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
| ✅ STREAK_FADE_5M | 2925 | -0.021 | -116.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2925 | -0.021 | -116.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 891 | -0.021 | -31.18€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 891 | -0.021 | -31.18€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 573 | -0.024 | -23.73€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 573 | -0.024 | -23.73€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1305 | -0.018 | -46.93€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1305 | -0.018 | -46.93€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 77 | -0.044 | -5.84€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 77 | -0.044 | -5.84€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 8639 | +0.023 | +128.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 8639 | +0.023 | +128.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2371 | +0.025 | +33.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2371 | +0.025 | +33.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 1953 | +0.032 | +52.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 1953 | +0.032 | +52.11€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2636 | +0.013 | +8.60€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2636 | +0.013 | +8.60€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1679 | +0.025 | +34.44€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1679 | +0.025 | +34.44€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 7874 | +0.013 | -40.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 7874 | +0.013 | -40.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3150 | +0.016 | -9.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3150 | +0.016 | -9.75€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3111 | +0.012 | -19.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3111 | +0.012 | -19.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1613 | +0.008 | -11.17€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1613 | +0.008 | -11.17€ | 2 | 0 |
| ✅ UPDOWN_GBM | 43862 | +0.035 | +2844.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 11452 | +0.071 | +2163.63€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1561 | +0.004 | +7.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 28015 | +0.026 | +651.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2670 | +0.002 | +24.02€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4414 | +0.075 | +541.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 795 | +0.161 | +345.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3586 | +0.057 | +196.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 8427 | +0.043 | +630.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1495 | +0.086 | +339.28€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 420 | +0.014 | +5.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5242 | +0.043 | +254.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1208 | +0.003 | +30.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 62 | -0.094 | +0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5046 | +0.041 | +318.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 752 | +0.137 | +261.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4266 | +0.025 | +58.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 9621 | +0.024 | +411.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 2921 | +0.049 | +335.17€ | 1 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 412 | +0.007 | +7.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5330 | +0.018 | +73.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 904 | -0.001 | -8.41€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 54 | -0.125 | +3.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 9997 | +0.016 | +272.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2762 | +0.027 | +196.00€ | 0 | 10 |
| ✅ UPDOWN_GBM#SOL#240min | 403 | -0.004 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6228 | +0.015 | +79.11€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 558 | +0.005 | +2.27€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 46 | -0.167 | -3.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6355 | +0.040 | +671.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2727 | +0.086 | +686.00€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 265 | -0.002 | -3.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3363 | +0.005 | -10.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 162 | -0.128 | +0.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 605 | +0.352 | +203.84€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 605 | +0.352 | +203.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 334 | +0.357 | +111.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 334 | +0.357 | +111.75€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 271 | +0.343 | +92.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 271 | +0.343 | +92.09€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 13224 | -0.036 | +2879.96€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 13224 | -0.036 | +2879.96€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 896 | -0.046 | +379.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 896 | -0.046 | +379.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2436 | -0.121 | +30.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2436 | -0.121 | +30.48€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 474 | +0.187 | +330.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 474 | +0.187 | +330.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1508 | +0.207 | +923.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1508 | +0.207 | +923.17€ | 1 | 23 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 3974 | -0.064 | +582.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 3974 | -0.064 | +582.71€ | 4 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 3936 | -0.074 | +633.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 3936 | -0.074 | +633.26€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 156 | +0.038 | +7.79€ | 1 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 156 | +0.038 | +7.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 156 | +0.038 | +7.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 156 | +0.038 | +7.79€ | 1 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 982 | +0.292 | +788.82€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 982 | +0.292 | +788.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 539 | +0.287 | +411.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 539 | +0.287 | +411.21€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 443 | +0.295 | +377.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 443 | +0.295 | +377.61€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 740 | -0.112 | -84.26€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 740 | -0.112 | -84.26€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 219 | -0.079 | -15.75€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 219 | -0.079 | -15.75€ | 3 | 0 |
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