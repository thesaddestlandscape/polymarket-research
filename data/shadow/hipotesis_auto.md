# Hipótesis automáticas — 2026-10-01 04:51 UTC
_Generado por shadow_postmortem.py sobre 692767 resoluciones (PNL=+82360.75€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.263 (n=112)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=561)

- **PATRÓN** `py_entrada` > `0.375` → IC=+0.235 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.375 (IC base=+0.137)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.216 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.137)

- **PATRÓN** `banda_hit_calibrado` > `0.8028` → IC=+0.256 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8028 (IC base=+0.137)

- **PATRÓN** `banda_z` > `9.53` → IC=+0.201 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.53 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=615)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `3000.8686` → IC=+0.151 (n=388)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3000.8686 (IC base=+0.137)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.142 (n=174)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=445)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.370 (n=52)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=426)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.258 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.146)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.146)

- **PATRÓN** `banda_hit_calibrado` > `0.7998` → IC=+0.266 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7998 (IC base=+0.146)

- **PATRÓN** `banda_z` > `10.374` → IC=+0.213 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.374 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.171 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=524)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `4281.7668` → IC=+0.153 (n=211)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 4281.7668 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.137 (n=169)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 93.0 (IC base=+0.058)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
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
- **FILTRO** `restante_s_al_confirmar` < `145.6` → IC=-0.218 (n=7795)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 145.6
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=23386)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `136.42` → IC=-0.253 (n=1021)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 136.42
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=3065)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `126.99` → IC=-0.308 (n=916)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 126.99
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=2753)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.74` → IC=-0.206 (n=1918)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.74
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=5759)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.3` → IC=-0.330 (n=1512)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.3
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=4538)

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
- **PATRÓN** `py_entrada` > `0.69` → IC=+0.210 (n=15253)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.69 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=3723)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `5526.6187` → IC=+0.173 (n=2404)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 5526.6187 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.136 (n=13169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=16047)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=12329)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=6103)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7740.2163` → IC=+0.168 (n=2328)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 7740.2163 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.209 (n=1833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.204 (n=1793)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.351 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `15993.2948` → IC=+0.232 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15993.2948 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.199 (n=1620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.200 (n=1809)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2315)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `15920.8748` → IC=+0.208 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15920.8748 (IC base=+0.195)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.615` → IC=+0.169 (n=360)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.615 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `4614.6151` → IC=+0.128 (n=245)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 4614.6151 (IC base=+0.092)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.147 (n=400)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 7.0 (IC base=+0.101)

- **PATRÓN** `py_entrada` < `0.444` → IC=+0.145 (n=886)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.444 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `5763.4424` → IC=+0.154 (n=229)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 5763.4424 (IC base=+0.101)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=3146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.353 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.363 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.231 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.226)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.137 (n=747)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.133)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.250 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.135 (n=850)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.02 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `1318.0949` → IC=+0.147 (n=744)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1318.0949 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.078)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.406 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2116.1107` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2116.1107 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.154 (n=591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.160 (n=637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.291 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=783)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.151)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.179 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 7.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.369 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.168)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=192)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `1218.3909` → IC=+0.152 (n=234)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1218.3909 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.228 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.118)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=66)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=13139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.202 (n=12567)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.231 (n=4199)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=3127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=2965)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=2997)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.172)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.244 (n=1159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.240)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.342 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.240)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=3079)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=2941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=2488)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=2713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.328 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=3002)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.191 (n=2892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 17.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.193 (n=2271)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.71 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.194 (n=1105)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.73 (IC base=+0.191)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `11452.1989` → IC=+0.460 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11452.1989 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.445 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.442)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.446 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.454 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_liquidez` > `14504.3208` → IC=+0.449 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14504.3208 (IC base=+0.442)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.443 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.94` → IC=+0.464 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.94 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3369.9988` → IC=+0.448 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3369.9988 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.413 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.412)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.414 (n=114)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.412)

- **PATRÓN** `py_entrada` < `0.915` → IC=+0.426 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.915 (IC base=+0.412)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.413 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.412)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=39176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.237 (n=17284)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=6742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=5418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=7375)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=7056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.265 (n=4006)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.178 (n=7131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 7.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=7144)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=3544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.267 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=6501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=2575)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=7737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.241 (n=3013)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.192)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=5980)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.134 (n=5710)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.52` → IC=+0.135 (n=5558)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.52 (IC base=+0.115)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=3008)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.124 (n=2766)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.16 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.137 (n=2824)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=3646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `3.23` → IC=+0.138 (n=2755)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.23 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.182 (n=2972)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.38 (IC base=+0.112)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.129 (n=3152)

  - _Acción_: Kelly boost +0.65€ cuando `restante_min` > 4.96 (IC base=+0.112)

- **PATRÓN** `lag_apertura_s` < `2.24` → IC=+0.135 (n=2794)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.24 (IC base=+0.112)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.315 (n=875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.288)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.383 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `1546.3244` → IC=+0.294 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1546.3244 (IC base=+0.288)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.349 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `5132.4682` → IC=+0.305 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5132.4682 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.287)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.396 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `1447.4658` → IC=+0.304 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1447.4658 (IC base=+0.287)

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
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.441 (n=542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.436 (n=481)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.439 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.437 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.440 (n=232)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.436 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.456 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.925` → IC=+0.454 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.925 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `1966.3827` → IC=+0.457 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1966.3827 (IC base=+0.440)

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
- **FILTRO** `py_entrada` > `0.75` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=55)

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
- **FILTRO** `py_entrada` > `0.75` → IC=-0.362 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.75
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=55)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4925` → IC=+0.128 (n=9334)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4925 (IC base=+0.112)

- **PATRÓN** `ibs_20min` > `0.9822` → IC=+0.244 (n=3112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9822 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.2169` → IC=+0.258 (n=2082)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2169 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.366` → IC=+0.190 (n=2454)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 8.366 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.254 (n=1722)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` > `0.6157` → IC=+0.255 (n=2581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6157 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.3016` → IC=+0.231 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3016 (IC base=+0.112)

- **PATRÓN** `volumen_spike_ratio` > `1.8946` → IC=+0.215 (n=4320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8946 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.5672` → IC=+0.135 (n=11339)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5672 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.6036` → IC=+0.204 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6036 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.1559` → IC=+0.177 (n=3769)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1559 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` < `0.6983` → IC=+0.187 (n=1795)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6983 (IC base=+0.068)

- **PATRÓN** `volumen_regimen` > `0.8704` → IC=+0.177 (n=2720)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.8704 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.167` → IC=+0.225 (n=1960)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.167 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` > `1.4473` → IC=+0.199 (n=6968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4473 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `123.0` → IC=+0.212 (n=6759)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 123.0 (IC base=+0.068)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.206 (n=695)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.183 (n=696)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0081 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.3557` → IC=+0.179 (n=2084)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.3557 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=1007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.178 (n=1397)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 11.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.186` → IC=+0.271 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.186 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.212 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.176 (n=1963)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.174)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.191 (n=2118)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.04 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.232 (n=1099)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.232)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.241 (n=1471)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.232)

- **PATRÓN** `drift_60min` |x|≤ `0.0903` → IC=+0.273 (n=549)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0903 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=1487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.0583` → IC=+0.284 (n=725)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0583 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.49` → IC=+0.244 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.49 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.438` → IC=+0.239 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.438 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.271 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `2.5704` → IC=+0.245 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5704 (IC base=+0.232)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.232)

- **PATRÓN** `libro_liquidez` > `1567.34` → IC=+0.243 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1567.34 (IC base=+0.232)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.238 (n=727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3554` → IC=+0.228 (n=1643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3554 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=1725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.221 (n=1673)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.8968` → IC=+0.264 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8968 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.3452` → IC=+0.223 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3452 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.619` → IC=+0.256 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.619 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.2524` → IC=+0.223 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2524 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.223 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2787` → IC=+0.244 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2787 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.3839` → IC=+0.239 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3839 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `11084.2751` → IC=+0.225 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11084.2751 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.168 (n=1118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0038 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0741` → IC=+0.168 (n=558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0741 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.148 (n=760)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.7169` → IC=+0.172 (n=1673)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7169 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1307` → IC=+0.155 (n=1519)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1307 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.152 (n=265)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.3` → IC=+0.147 (n=1544)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.3 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.150 (n=1673)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 1.2089 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.8607` → IC=+0.143 (n=1115)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 0.8607 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1561` → IC=+0.185 (n=445)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1561 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4376` → IC=+0.150 (n=1563)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4376 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.77` → IC=+0.151 (n=1042)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.77 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `14091.9548` → IC=+0.144 (n=1115)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 14091.9548 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `231.0` → IC=+0.174 (n=655)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 231.0 (IC base=+0.140)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.210 (n=698)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=2198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=1879)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.299` → IC=+0.259 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.299 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.195 (n=1832)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.205 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.77` → IC=+0.199 (n=1788)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 1.77 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.197 (n=2486)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.04 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `1998.2464` → IC=+0.197 (n=697)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1998.2464 (IC base=+0.189)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.219 (n=1615)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.6306` → IC=+0.214 (n=1835)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6306 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=695)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.213 (n=862)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.0645` → IC=+0.234 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0645 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.685` → IC=+0.228 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.685 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.569` → IC=+0.211 (n=1988)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.569 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3474` → IC=+0.246 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3474 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7249` → IC=+0.213 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7249 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `3.225` → IC=+0.220 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.225 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.219 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1988.6161` → IC=+0.217 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1988.6161 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.209 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.210)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.164 (n=114)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=2513)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.148 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0037 (IC base=+0.040)

- **PATRÓN** `ibs_20min` > `0.9545` → IC=+0.222 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9545 (IC base=+0.040)

- **PATRÓN** `dist_vwap_pct` < `0.5336` → IC=+0.333 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5336 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.854` → IC=+0.170 (n=829)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 4.854 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` < `0.8553` → IC=+0.340 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8553 (IC base=+0.040)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.337 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2985` → IC=+0.362 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2985 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` < `1.4124` → IC=+0.355 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4124 (IC base=+0.040)

- **PATRÓN** `volumen_spike_ratio` > `1.8361` → IC=+0.334 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8361 (IC base=+0.040)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.331 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.040)

- **PATRÓN** `ibs_20min` < `0.1014` → IC=+0.154 (n=657)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1014 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` > `0.6684` → IC=+0.204 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6684 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.8511` → IC=+0.155 (n=670)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8511 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.209 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `1.518` → IC=+0.166 (n=849)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.518 (IC base=+0.021)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.181 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=380)

- **FILTRO** `ibs_20min` < `0.2941` → IC=-0.202 (n=112)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=+0.127 (n=338)

- **FILTRO** `ibs_20min` > `0.2411` → IC=-0.125 (n=2527)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2411
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=1245)

- **FILTRO** `sigma_ewma_delta_pct` > `8.719` → IC=-0.206 (n=396)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.719
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=3376)

- **PATRÓN** `ibs_20min` > `0.6129` → IC=+0.165 (n=225)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.6129 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `1.695` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.695 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` < `0.6571` → IC=+0.291 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6571 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `1.0824` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0824 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.286 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4963 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` > `1.4536` → IC=+0.271 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4536 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.295 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.2411` → IC=+0.130 (n=1245)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.2411 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7288` → IC=+0.250 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7288 (IC base=-0.041)

- **PATRÓN** `dist_vwap_pct` < `0.4503` → IC=+0.242 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4503 (IC base=-0.041)

- **PATRÓN** `volumen_regimen` < `0.6806` → IC=+0.278 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6806 (IC base=-0.041)

- **PATRÓN** `volumen_pendiente_norm` > `0.1591` → IC=+0.293 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1591 (IC base=-0.041)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.286 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.041)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6549` → IC=-0.180 (n=657)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6549
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1972)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.203 (n=607)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=2022)

- **FILTRO** `ibs_20min` > `0.7692` → IC=-0.208 (n=959)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=2952)

- **PATRÓN** `dist_vwap_pct` > `0.7963` → IC=+0.326 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7963 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.21` → IC=+0.317 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.21 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` < `0.9729` → IC=+0.295 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9729 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.6166` → IC=+0.310 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6166 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.303 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.0704` → IC=+0.297 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0704 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `2.4513` → IC=+0.303 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4513 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8027` → IC=+0.302 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8027 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.5647` → IC=+0.280 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5647 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` < `0.728` → IC=+0.260 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.728 (IC base=-0.017)

- **PATRÓN** `volumen_regimen` > `1.2368` → IC=+0.276 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2368 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` > `0.1678` → IC=+0.266 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1678 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.1399` → IC=+0.261 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1399 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.5239` → IC=+0.253 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5239 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.199 (n=4024)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0097 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `0.4733` → IC=+0.188 (n=10758)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4733 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.0156` → IC=+0.291 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0156 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.644` → IC=+0.158 (n=5529)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.644 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` < `1.1795` → IC=+0.245 (n=4350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1795 (IC base=+0.100)

- **PATRÓN** `volumen_regimen` > `0.6915` → IC=+0.254 (n=3886)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6915 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` < `0.0803` → IC=+0.240 (n=6436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0803 (IC base=+0.100)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.272 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` < `1.4632` → IC=+0.242 (n=2341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4632 (IC base=+0.100)

- **PATRÓN** `volumen_spike_ratio` > `2.6391` → IC=+0.253 (n=2341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6391 (IC base=+0.100)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.275 (n=6548)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.100)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.169 (n=3910)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0092 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.157 (n=10314)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.5455 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.7144` → IC=+0.250 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7144 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2488` → IC=+0.248 (n=3391)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2488 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7084` → IC=+0.249 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7084 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1996` → IC=+0.258 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1996 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2409` → IC=+0.303 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2409 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5897` → IC=+0.274 (n=2118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5897 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `81.0` → IC=+0.277 (n=4699)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 81.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.2578` → IC=-0.149 (n=832)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2578
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=2499)

- **FILTRO** `ibs_20min` > `0.7573` → IC=-0.158 (n=680)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7573
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2044)

- **FILTRO** `sigma_ewma_delta_pct` > `4.561` → IC=-0.172 (n=619)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.561
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=2105)

- **PATRÓN** `ibs_20min` > `0.8982` → IC=+0.275 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8982 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.913` → IC=+0.207 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.913 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.2255` → IC=+0.269 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2255 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.44` → IC=+0.201 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.44 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` > `2.1694` → IC=+0.222 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1694 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.219 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.0958` → IC=+0.440 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0958 (IC base=-0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1478` → IC=+0.446 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1478 (IC base=-0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4745` → IC=+0.447 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4745 (IC base=-0.022)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.471 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=-0.022)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8652` → IC=+0.166 (n=806)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8652 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.2987` → IC=+0.186 (n=421)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.2987 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6774` → IC=+0.177 (n=1000)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6774 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.238 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4243` → IC=+0.201 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4243 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` > `2.4058` → IC=+0.177 (n=366)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 2.4058 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.217 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 234.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.227 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` > `0.6902` → IC=+0.228 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6902 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2671` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2671 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1582` → IC=+0.247 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1582 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `456.0` → IC=+0.223 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 456.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.285 (n=1233)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.253)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=1856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.253)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.253 (n=1865)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.253)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.253)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.725` → IC=+0.283 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.725 (IC base=+0.253)

- **PATRÓN** `volumen_pendiente_norm` < `0.0996` → IC=+0.267 (n=1579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0996 (IC base=+0.253)

- **PATRÓN** `volumen_spike_ratio` > `3.2706` → IC=+0.271 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2706 (IC base=+0.253)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2177)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.253)

- **PATRÓN** `libro_liquidez` > `1918.5184` → IC=+0.268 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1918.5184 (IC base=+0.253)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.316 (n=692)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.1856` → IC=+0.297 (n=672)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1856 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.323 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` < `0.3571` → IC=+0.291 (n=1528)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3571 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.7` → IC=+0.291 (n=543)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.7 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` > `0.1195` → IC=+0.290 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1195 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` < `1.5718` → IC=+0.300 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5718 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `2.6513` → IC=+0.288 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6513 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.289 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `1911.8434` → IC=+0.303 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.8434 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.287 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.284)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7732` → IC=-0.188 (n=696)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7732
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=2092)

- **PATRÓN** `ibs_20min` > `0.9077` → IC=+0.184 (n=615)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.9077 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1824` → IC=+0.236 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1824 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.0017` → IC=+0.253 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0017 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.0811` → IC=+0.257 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0811 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.275 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.261 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1474` → IC=+0.223 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1474 (IC base=-0.005)

- **PATRÓN** `volumen_regimen` < `1.176` → IC=+0.215 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.176 (IC base=-0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.297 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=-0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.8148` → IC=+0.262 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8148 (IC base=-0.005)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.258 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 135.0 (IC base=-0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7547` → IC=-0.186 (n=1277)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7547
  - _Potencial_: sin este filtro IC_bueno=+0.283 (n=1278)

- **FILTRO** `ibs_20min` > `0.675` → IC=-0.235 (n=639)

  - _Acción_: SKIP cuando `ibs_20min` > 0.675
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=1918)

- **FILTRO** `sigma_ewma_delta_pct` > `4.71` → IC=-0.191 (n=554)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.71
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=2003)

- **PATRÓN** `ibs_20min` > `0.7547` → IC=+0.283 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7547 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `1.0905` → IC=+0.329 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0905 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.69` → IC=+0.167 (n=403)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.69 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.8618` → IC=+0.308 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8618 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `0.6366` → IC=+0.303 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6366 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.300 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.4239` → IC=+0.322 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4239 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.323 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.5741` → IC=+0.130 (n=1689)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.5741 (IC base=+0.021)

- **PATRÓN** `dist_vwap_pct` < `0.22` → IC=+0.238 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.22 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `0.7031` → IC=+0.265 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7031 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.224 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.236 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `2.4505` → IC=+0.244 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4505 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `56.0` → IC=+0.254 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 56.0 (IC base=+0.021)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.325 (n=1359)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.299 (n=716)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` > `0.7442` → IC=+0.322 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7442 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.2166` → IC=+0.314 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2166 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.72` → IC=+0.302 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.72 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.293 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.330 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` > `1.4307` → IC=+0.291 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4307 (IC base=+0.280)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.284 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2464.9288` → IC=+0.291 (n=1359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2464.9288 (IC base=+0.280)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.320 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.280)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.309 (n=1078)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.280)

- **PATRÓN** `drift_60min` |x|≤ `0.1959` → IC=+0.287 (n=712)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1959 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.291 (n=812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.280)

- **PATRÓN** `ibs_20min` < `0.1341` → IC=+0.330 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1341 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` > `0.3162` → IC=+0.291 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3162 (IC base=+0.280)

- **PATRÓN** `dist_vwap_pct` < `0.2297` → IC=+0.280 (n=1487)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2297 (IC base=+0.280)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.513` → IC=+0.298 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.513 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` < `0.6418` → IC=+0.286 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6418 (IC base=+0.280)

- **PATRÓN** `volumen_regimen` > `1.2368` → IC=+0.311 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2368 (IC base=+0.280)

- **PATRÓN** `volumen_pendiente_norm` > `0.2336` → IC=+0.336 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2336 (IC base=+0.280)

- **PATRÓN** `volumen_spike_ratio` < `1.4219` → IC=+0.290 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4219 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `2414.1045` → IC=+0.283 (n=1444)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2414.1045 (IC base=+0.280)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.176 (n=3042)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0048 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.203 (n=3042)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.127` → IC=+0.185 (n=4010)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.127 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=9495)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.5714` → IC=+0.223 (n=9118)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5714 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.1742` → IC=+0.195 (n=3901)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1742 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.371` → IC=+0.253 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.371 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.2087` → IC=+0.163 (n=6064)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2087 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` > `0.6297` → IC=+0.160 (n=6064)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 0.6297 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.198 (n=1351)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.559` → IC=+0.170 (n=3857)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.559 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6045` → IC=+0.177 (n=2922)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.6045 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `1957.406` → IC=+0.173 (n=8139)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 1957.406 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.184 (n=8023)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 108.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.185 (n=5848)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0067 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0817` → IC=+0.214 (n=2925)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0817 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=3381)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.226 (n=8771)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.1749` → IC=+0.165 (n=6155)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1749 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.32` → IC=+0.198 (n=1469)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.32 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `1.1764` → IC=+0.158 (n=6301)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.1764 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.291` → IC=+0.215 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.291 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.556` → IC=+0.170 (n=3554)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.556 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.6033` → IC=+0.173 (n=2693)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.6033 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.179 (n=7749)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 109.0 (IC base=+0.171)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.231 (n=510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.201 (n=509)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.3439` → IC=+0.213 (n=1527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3439 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=1609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.199 (n=1025)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.9062` → IC=+0.283 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9062 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.238` → IC=+0.327 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.238 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2305` → IC=+0.243 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2305 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.191 (n=1423)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.207 (n=1558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.242 (n=1027)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.246 (n=1042)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.1839` → IC=+0.283 (n=778)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1839 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.247 (n=1121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.35` → IC=+0.258 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.35 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.26` → IC=+0.244 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.26 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2892` → IC=+0.260 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2892 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.4205` → IC=+0.256 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4205 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1564.64` → IC=+0.248 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1564.64 (IC base=+0.236)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.237 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.0719` → IC=+0.194 (n=456)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0719 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=1370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.3933` → IC=+0.224 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3933 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.1985` → IC=+0.210 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1985 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.223 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.174 (n=602)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6895 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.204 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `1.5028` → IC=+0.180 (n=585)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5028 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `2.4677` → IC=+0.158 (n=443)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.4677 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `11900.8434` → IC=+0.162 (n=1221)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 11900.8434 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `383.0` → IC=+0.157 (n=1136)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 383.0 (IC base=+0.158)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.161 (n=1458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0057 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.2932` → IC=+0.168 (n=1457)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2932 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.180 (n=488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 18.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.141 (n=692)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.5844` → IC=+0.191 (n=1457)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.5844 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.912` → IC=+0.208 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.912 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2116` → IC=+0.158 (n=1457)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.2116 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1567` → IC=+0.152 (n=444)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.1567 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4507` → IC=+0.146 (n=1345)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4507 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4202` → IC=+0.141 (n=1345)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4202 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `209.0` → IC=+0.169 (n=427)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 209.0 (IC base=+0.140)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.224 (n=690)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.2514` → IC=+0.220 (n=1015)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2514 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1580)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.280 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.201` → IC=+0.212 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.201 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `1.7866` → IC=+0.204 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7866 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.7351` → IC=+0.216 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7351 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `1992.1632` → IC=+0.213 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1992.1632 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.233 (n=1148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1437` → IC=+0.255 (n=574)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1437 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.275 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.3509` → IC=+0.244 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3509 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.649` → IC=+0.254 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.649 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.0923` → IC=+0.238 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0923 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7398` → IC=+0.230 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7398 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `3.2696` → IC=+0.232 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2696 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1912.76` → IC=+0.223 (n=591)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.76 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.212 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.218)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.179 (n=1290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0065 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4312` → IC=+0.161 (n=1466)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.4312 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=1527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.3498` → IC=+0.200 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3498 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1478` → IC=+0.181 (n=945)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.1478 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.887` → IC=+0.222 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.887 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.0361` → IC=+0.155 (n=1290)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.0361 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1013` → IC=+0.182 (n=620)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1013 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.163 (n=478)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.5102` → IC=+0.165 (n=478)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5102 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5280.4621` → IC=+0.191 (n=977)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 5280.4621 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.150 (n=1403)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 156.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.157 (n=1541)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0071 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.3855` → IC=+0.146 (n=1540)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3855 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.6596` → IC=+0.173 (n=1540)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.6596 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.1576` → IC=+0.142 (n=1513)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1576 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.926` → IC=+0.162 (n=537)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.926 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.856` → IC=+0.151 (n=1027)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.856 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.180 (n=229)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8021` → IC=+0.139 (n=944)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8021 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.5177` → IC=+0.127 (n=472)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.5177 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `9356.662` → IC=+0.163 (n=698)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 9356.662 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `128.0` → IC=+0.126 (n=1193)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 128.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.161 (n=753)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0101 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=1697)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.5045` → IC=+0.208 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5045 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `1.0933` → IC=+0.215 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0933 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.836` → IC=+0.257 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.836 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2087` → IC=+0.132 (n=1661)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.2087 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.127 (n=1666)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.0708` → IC=+0.122 (n=692)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.0708 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` < `1.5416` → IC=+0.137 (n=706)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.5416 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=1735)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `2891.3724` → IC=+0.202 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2891.3724 (IC base=+0.121)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.140 (n=1293)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 47.0 (IC base=+0.121)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.164 (n=743)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0062 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.170 (n=562)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=615)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.216 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2099` → IC=+0.148 (n=1560)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2099 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.609` → IC=+0.137 (n=351)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 7.609 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6381` → IC=+0.153 (n=563)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6381 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2271` → IC=+0.162 (n=297)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2271 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.146 (n=512)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4205` → IC=+0.130 (n=512)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.4205 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2744.0462` → IC=+0.176 (n=764)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2744.0462 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.127 (n=1477)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 52.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.226 (n=1405)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.1828` → IC=+0.207 (n=692)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1828 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=1638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.210 (n=712)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.243 (n=1577)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.5256` → IC=+0.211 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5256 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.602` → IC=+0.242 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.602 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.1976` → IC=+0.207 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1976 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` > `0.6285` → IC=+0.213 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6285 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.267 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.210 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.7991` → IC=+0.211 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7991 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.206 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2615.1096` → IC=+0.203 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.1096 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0117` → IC=+0.223 (n=713)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0117 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0174` → IC=+0.213 (n=1080)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0174 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.093` → IC=+0.231 (n=541)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.093 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.0205` → IC=+0.296 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0205 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `1.2401` → IC=+0.226 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2401 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.409` → IC=+0.249 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.409 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.7028` → IC=+0.216 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7028 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.282 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `2.1966` → IC=+0.202 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1966 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.205 (n=1476)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.209 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2384.9953` → IC=+0.213 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2384.9953 (IC base=+0.208)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.187 (n=1041)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0043 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.173 (n=789)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0085 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.3469` → IC=+0.170 (n=2081)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.3469 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.205 (n=1187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.51` → IC=+0.199 (n=2112)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.51 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.8055` → IC=+0.180 (n=379)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.8055 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.719` → IC=+0.189 (n=1039)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.719 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.186 (n=1405)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.8725 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `1.2045` → IC=+0.176 (n=702)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 1.2045 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1638` → IC=+0.176 (n=634)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1638 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4378` → IC=+0.174 (n=765)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4378 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `1.823` → IC=+0.171 (n=1527)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.823 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.169 (n=2680)

  - _Acción_: Kelly boost +0.85€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2671.4273` → IC=+0.169 (n=2112)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 2671.4273 (IC base=+0.164)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.179 (n=2142)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 143.0 (IC base=+0.164)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.144 (n=1625)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0056 (IC base=+0.113)

- **PATRÓN** `drift_60min` |x|≤ `0.3435` → IC=+0.128 (n=2144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3435 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.127 (n=2272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.0634` → IC=+0.194 (n=812)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.0634 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `1.2242` → IC=+0.122 (n=2205)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 1.2242 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.140 (n=600)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.151 (n=786)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.4415 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2767.6856` → IC=+0.124 (n=2176)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2767.6856 (IC base=+0.113)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.133 (n=1028)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 28.0 (IC base=+0.113)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.183 (n=269)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0029 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3311` → IC=+0.154 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.3311 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.181 (n=563)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.6508` → IC=+0.208 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6508 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.2846` → IC=+0.170 (n=207)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.2846 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.159` → IC=+0.144 (n=535)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.159 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.137` → IC=+0.154 (n=273)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 3.137 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.847` → IC=+0.141 (n=636)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 6.847 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.623` → IC=+0.194 (n=204)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.623 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` < `0.1556` → IC=+0.143 (n=634)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.1556 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.0916` → IC=+0.148 (n=214)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.0916 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.2078` → IC=+0.151 (n=523)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2078 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.5086` → IC=+0.145 (n=530)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5086 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=788)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `10682.1975` → IC=+0.156 (n=609)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 10682.1975 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.174 (n=256)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 160.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.211 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.3396` → IC=+0.158 (n=765)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3396 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.6186` → IC=+0.178 (n=673)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6186 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.183` → IC=+0.154 (n=762)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.183 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.284` → IC=+0.145 (n=288)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 4.284 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.074` → IC=+0.142 (n=700)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.074 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.2242` → IC=+0.147 (n=765)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 1.2242 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.7077` → IC=+0.153 (n=683)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.7077 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.211 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1022` → IC=+0.156 (n=664)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1022 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.4063` → IC=+0.147 (n=755)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.4063 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `361.0` → IC=+0.150 (n=735)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 361.0 (IC base=+0.140)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.263 (n=331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.210 (n=250)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.4055` → IC=+0.217 (n=748)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4055 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.253 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1455` → IC=+0.217 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1455 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.2194` → IC=+0.212 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2194 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.230 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.219 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8342 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.1625` → IC=+0.234 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1625 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.155` → IC=+0.255 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.155 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4105` → IC=+0.234 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4105 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.4387` → IC=+0.246 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4387 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.123 (n=613)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0062 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.0867` → IC=+0.147 (n=233)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.0867 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.6874` → IC=+0.150 (n=307)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6874 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.140 (n=109)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `3866.7412` → IC=+0.120 (n=622)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 3866.7412 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.157 (n=511)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0058 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.5423` → IC=+0.141 (n=572)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.5423 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.179 (n=527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 8.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.262 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.9964` → IC=+0.236 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9964 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.329` → IC=+0.193 (n=239)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.329 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.0674` → IC=+0.157 (n=503)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0674 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `0.7219` → IC=+0.147 (n=511)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7219 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.1735` → IC=+0.165 (n=159)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1735 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.2078` → IC=+0.167 (n=250)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.2078 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.145 (n=603)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `2963.0907` → IC=+0.183 (n=260)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2963.0907 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.141 (n=544)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5714 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `1.836` → IC=+0.150 (n=344)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.836 (IC base=+0.086)

- **PATRÓN** `libro_liquidez` > `2511.7349` → IC=+0.135 (n=362)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2511.7349 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.133 (n=488)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 40.0 (IC base=+0.086)

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
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.209 (n=3926)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=12282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.4615` → IC=+0.221 (n=11772)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4615 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.9272` → IC=+0.202 (n=1641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9272 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.362` → IC=+0.247 (n=2918)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.362 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.172 (n=5265)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.8803 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2884` → IC=+0.201 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2884 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.58` → IC=+0.195 (n=3788)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.58 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `1792.61` → IC=+0.178 (n=11771)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1792.61 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `82.0` → IC=+0.201 (n=9194)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 82.0 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.193 (n=7115)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.007 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1508` → IC=+0.192 (n=4682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1508 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=4029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.57` → IC=+0.236 (n=10637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.57 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.2512` → IC=+0.163 (n=6656)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.2512 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.05` → IC=+0.204 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.05 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.739` → IC=+0.183 (n=10265)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.739 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.6345` → IC=+0.165 (n=2415)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6345 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.243 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6004` → IC=+0.193 (n=3291)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6004 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.200 (n=6355)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.182)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.231 (n=655)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.203)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.226 (n=652)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.3621` → IC=+0.204 (n=1957)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3621 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=942)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=1321)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.334 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.666` → IC=+0.354 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.666 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2285` → IC=+0.256 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2285 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.242` → IC=+0.206 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.242 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.260 (n=1065)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.260 (n=1594)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.1263` → IC=+0.281 (n=701)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1263 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=1437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.4803` → IC=+0.283 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4803 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.466` → IC=+0.258 (n=1673)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.466 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.296 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.5488` → IC=+0.257 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5488 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.274 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1567.2992` → IC=+0.266 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1567.2992 (IC base=+0.257)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.206 (n=631)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0832` → IC=+0.164 (n=631)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0832 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=1977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.2982` → IC=+0.206 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2982 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.189 (n=1049)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.721` → IC=+0.173 (n=414)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 9.721 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.181` → IC=+0.156 (n=1726)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.181 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.181 (n=632)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6288 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.0731` → IC=+0.157 (n=1667)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.0731 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.2676` → IC=+0.189 (n=271)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2676 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.1149` → IC=+0.163 (n=1614)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 2.1149 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.156 (n=1834)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `11338.6336` → IC=+0.158 (n=1689)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 11338.6336 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `278.0` → IC=+0.173 (n=781)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 278.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.167 (n=1605)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0057 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.326` → IC=+0.163 (n=1605)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.326 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=621)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.2865` → IC=+0.237 (n=1070)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2865 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.6505` → IC=+0.156 (n=254)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6505 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1329` → IC=+0.165 (n=1472)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1329 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.534` → IC=+0.168 (n=269)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.534 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.314` → IC=+0.152 (n=1465)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.314 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.163 (n=1605)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1967 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.204 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4071` → IC=+0.157 (n=1507)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.4071 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.757` → IC=+0.166 (n=1004)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.757 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `259.0` → IC=+0.162 (n=471)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 259.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.259 (n=641)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=2012)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.224 (n=1946)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.349` → IC=+0.305 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.349 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.1336` → IC=+0.222 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1336 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.6215` → IC=+0.228 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6215 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1998.3436` → IC=+0.235 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1998.3436 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.238 (n=1587)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.615` → IC=+0.235 (n=1804)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.615 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=854)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.0152` → IC=+0.303 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0152 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.154` → IC=+0.276 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.154 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.3406` → IC=+0.291 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3406 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.7265` → IC=+0.231 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7265 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.1492` → IC=+0.238 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1492 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=1120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `1981.9661` → IC=+0.245 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.9661 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.231 (n=1610)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.231)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.192 (n=674)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4364` → IC=+0.150 (n=2016)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4364 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.157 (n=2098)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.2755` → IC=+0.188 (n=2016)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2755 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3654` → IC=+0.162 (n=776)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3654 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.576` → IC=+0.167 (n=325)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.576 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8719` → IC=+0.162 (n=1344)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8719 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.207 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.154 (n=862)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1629` → IC=+0.156 (n=888)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1629 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `7627.5668` → IC=+0.240 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7627.5668 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.177 (n=639)

  - _Acción_: Kelly boost +0.89€ cuando `ballena_activa_n` < 73.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.169 (n=1086)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0052 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4451` → IC=+0.145 (n=1624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4451 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.133 (n=750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 7.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.5855` → IC=+0.198 (n=1429)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.5855 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` < `0.1596` → IC=+0.134 (n=1423)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1596 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.298` → IC=+0.171 (n=244)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.298 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6988` → IC=+0.144 (n=715)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6988 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.227 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.443` → IC=+0.141 (n=1551)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.443 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `9617.9713` → IC=+0.200 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9617.9713 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.131 (n=1364)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 146.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.145 (n=1339)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0082 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2060)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4667` → IC=+0.198 (n=2008)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4667 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.0792` → IC=+0.206 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0792 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.558` → IC=+0.238 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.558 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8904` → IC=+0.144 (n=1338)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.8904 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.125 (n=2061)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.8367` → IC=+0.122 (n=1301)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 1.8367 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.1893` → IC=+0.131 (n=885)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.1893 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.131 (n=2036)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2883.9504` → IC=+0.256 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2883.9504 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.143 (n=1583)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 52.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.183 (n=642)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0058 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1368` → IC=+0.160 (n=640)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1368 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=709)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.209 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2221` → IC=+0.139 (n=1593)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2221 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.46` → IC=+0.129 (n=1842)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 3.46 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6464` → IC=+0.164 (n=640)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6464 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2197` → IC=+0.182 (n=300)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2197 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4357` → IC=+0.147 (n=585)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4357 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2797.1957` → IC=+0.184 (n=640)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2797.1957 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.133 (n=1544)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 51.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.230 (n=1772)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.216 (n=2074)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.213 (n=1778)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.260 (n=1782)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.217` → IC=+0.231 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.217 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.591` → IC=+0.254 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.591 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `1.063` → IC=+0.216 (n=1746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.063 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` > `0.6415` → IC=+0.220 (n=1983)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6415 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.2856` → IC=+0.246 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2856 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.4852` → IC=+0.234 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4852 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=1945)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `2616.0932` → IC=+0.219 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2616.0932 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.216 (n=699)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0093 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.230 (n=701)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.221 (n=1476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.4214` → IC=+0.262 (n=1844)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4214 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `1.2401` → IC=+0.210 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2401 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2182` → IC=+0.212 (n=1859)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2182 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.876` → IC=+0.259 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.876 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.237 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2332 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.279 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `2.1798` → IC=+0.202 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1798 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.205 (n=1907)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `2393.0118` → IC=+0.209 (n=1872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2393.0118 (IC base=+0.207)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.197 (n=1821)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 37.0 (IC base=+0.207)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=3624)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.214 (n=1196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.5102` → IC=+0.188 (n=3587)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.5102 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=1357)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1647)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.239 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.1744` → IC=+0.186 (n=1307)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1744 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` < `0.4592` → IC=+0.177 (n=2336)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.4592 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.2` → IC=+0.208 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.2 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `0.7082` → IC=+0.181 (n=1074)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.7082 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.8924` → IC=+0.181 (n=1627)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.8924 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.1688` → IC=+0.208 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1688 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.455` → IC=+0.188 (n=1181)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.455 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.8658` → IC=+0.185 (n=2362)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 1.8658 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=2641)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2879.5978` → IC=+0.186 (n=3204)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2879.5978 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.218 (n=912)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.3836` → IC=+0.183 (n=2402)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3836 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.194 (n=967)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=1245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.1829` → IC=+0.186 (n=1201)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.1829 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.6719` → IC=+0.182 (n=511)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.6719 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.207` → IC=+0.171 (n=2724)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.207 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.2513` → IC=+0.166 (n=2566)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.2513 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` < `0.0968` → IC=+0.168 (n=2492)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.0968 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.5357` → IC=+0.170 (n=1187)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5357 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `1.8237` → IC=+0.172 (n=1798)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.8237 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=3624)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `5261.8397` → IC=+0.166 (n=2439)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5261.8397 (IC base=+0.161)

- **PATRÓN** `ballena_activa_n` < `85.0` → IC=+0.166 (n=1772)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 85.0 (IC base=+0.161)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.222 (n=426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.0805` → IC=+0.262 (n=162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0805 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.207 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.211 (n=216)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.515` → IC=+0.226 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.515 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.761` → IC=+0.210 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.761 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.3306` → IC=+0.210 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3306 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.96` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.96 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.554` → IC=+0.202 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.554 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.8386` → IC=+0.225 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8386 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.328 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.232 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `2.5955` → IC=+0.199 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5955 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `12584.6611` → IC=+0.235 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12584.6611 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.224 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.195 (n=345)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.195 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.198 (n=346)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 4.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.1496` → IC=+0.183 (n=453)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.1496 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.157 (n=467)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.6078 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.6721` → IC=+0.197 (n=97)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6721 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1634` → IC=+0.150 (n=1016)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1634 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.171 (n=1009)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8811` → IC=+0.193 (n=686)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8811 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.0691` → IC=+0.170 (n=474)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.0691 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4164` → IC=+0.154 (n=342)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4164 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.8167` → IC=+0.167 (n=683)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 1.8167 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `12136.4448` → IC=+0.159 (n=919)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 12136.4448 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.158 (n=984)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 701.0 (IC base=+0.150)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.207 (n=380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1524` → IC=+0.200 (n=501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1524 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.187 (n=522)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 6.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.5342` → IC=+0.197 (n=759)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.5342 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.886` → IC=+0.189 (n=380)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.886 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.2031` → IC=+0.194 (n=953)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2031 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.192 (n=1025)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.0789` → IC=+0.187 (n=1002)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0789 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `1.2332` → IC=+0.183 (n=380)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.2332 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.1659` → IC=+0.198 (n=339)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1659 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `2.4779` → IC=+0.189 (n=1118)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.4779 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.187 (n=1139)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.224 (n=310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.166)

- **PATRÓN** `drift_60min` |x|≤ `0.4837` → IC=+0.192 (n=924)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4837 (IC base=+0.166)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.175 (n=617)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 10.0 (IC base=+0.166)

- **PATRÓN** `ibs_20min` < `0.7607` → IC=+0.172 (n=924)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7607 (IC base=+0.166)

- **PATRÓN** `ibs_20min` > `0.0909` → IC=+0.171 (n=924)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.0909 (IC base=+0.166)

- **PATRÓN** `dist_vwap_pct` > `0.6082` → IC=+0.191 (n=202)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6082 (IC base=+0.166)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.639` → IC=+0.173 (n=946)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.639 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` < `0.6426` → IC=+0.200 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6426 (IC base=+0.166)

- **PATRÓN** `volumen_regimen` > `0.7218` → IC=+0.168 (n=825)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.7218 (IC base=+0.166)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.183 (n=392)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.166)

- **PATRÓN** `volumen_spike_ratio` < `2.1958` → IC=+0.182 (n=797)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.1958 (IC base=+0.166)

- **PATRÓN** `libro_liquidez` > `7791.0091` → IC=+0.184 (n=825)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7791.0091 (IC base=+0.166)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.166 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0108 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.188 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 11.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.144 (n=366)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 14.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` > `0.9326` → IC=+0.241 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9326 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` > `0.2235` → IC=+0.194 (n=240)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.2235 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.028` → IC=+0.220 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.028 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `0.7086` → IC=+0.189 (n=159)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.7086 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` > `1.2638` → IC=+0.142 (n=121)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.2638 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.1587` → IC=+0.237 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1587 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7715` → IC=+0.181 (n=233)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.7715 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=428)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `2997.549` → IC=+0.164 (n=361)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2997.549 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.166 (n=303)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 51.0 (IC base=+0.142)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.190 (n=298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0068 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.6689` → IC=+0.177 (n=298)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.6689 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.160 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 16.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.6782` → IC=+0.191 (n=263)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6782 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.6343` → IC=+0.225 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6343 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.639` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.639 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.281` → IC=+0.163 (n=289)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 5.281 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.3839` → IC=+0.167 (n=298)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.3839 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.218 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.6095` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.6095 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3191.6314` → IC=+0.197 (n=298)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3191.6314 (IC base=+0.159)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.203 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.159)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.170 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0039 (IC base=+0.081)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.123 (n=1008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 8.0 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.6439` → IC=+0.179 (n=908)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6439 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1434` → IC=+0.146 (n=538)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1434 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.192 (n=238)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.081)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.125 (n=401)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0056 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.0431` → IC=+0.311 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0431 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.1829` → IC=+0.142 (n=428)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1829 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.023` → IC=+0.145 (n=150)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.023 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.074` → IC=+0.143 (n=320)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.074 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.221 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `2.5184` → IC=+0.151 (n=319)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.5184 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `1.7085` → IC=+0.156 (n=213)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7085 (IC base=+0.047)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.141 (n=327)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.02 (IC base=+0.047)

- **PATRÓN** `libro_liquidez` > `3232.5296` → IC=+0.147 (n=154)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3232.5296 (IC base=+0.047)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.200 (n=168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.089)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.120 (n=388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 6.0 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.4301` → IC=+0.162 (n=350)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.4301 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.169 (n=179)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` < `2.4916` → IC=+0.128 (n=310)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 2.4916 (IC base=+0.089)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.148 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0045 (IC base=+0.096)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.190 (n=56)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.096)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.1678` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1678 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.0677` → IC=+0.156 (n=187)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.0677 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.876` → IC=+0.191 (n=173)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.876 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `0.6161` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6161 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.8156` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8156 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.0668` → IC=+0.196 (n=67)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0668 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `2.4035` → IC=+0.181 (n=155)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.4035 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `3269.2861` → IC=+0.162 (n=149)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3269.2861 (IC base=+0.096)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.6869` → IC=-0.127 (n=148)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6869
  - _Potencial_: sin este filtro IC_bueno=+0.215 (n=303)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.257 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=147)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.131 (n=247)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0049 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6869` → IC=+0.215 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6869 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.3368` → IC=+0.202 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3368 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.74` → IC=+0.292 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.74 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.093)

- **PATRÓN** `volumen_spike_ratio` < `1.7617` → IC=+0.148 (n=191)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7617 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `1133.3296` → IC=+0.151 (n=299)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1133.3296 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.1891` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1891 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` < `0.1182` → IC=+0.145 (n=119)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1182 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.258` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.258 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.558` → IC=+0.152 (n=90)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.558 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` < `0.0788` → IC=+0.134 (n=99)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.0788 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` > `0.136` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.136 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` > `2.1925` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.1925 (IC base=+0.016)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=102)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.016)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` > `0.0119` → IC=-0.281 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0119
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=118)

- **FILTRO** `ibs_20min` > `0.1837` → IC=-0.305 (n=39)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1837
  - _Potencial_: sin este filtro IC_bueno=+0.260 (n=77)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.179 (n=219)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.7778 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0159` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 1.0159 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.076` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.076 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.057)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.123 (n=104)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0094 (IC base=-0.003)

- **PATRÓN** `ibs_20min` < `0.1837` → IC=+0.260 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1837 (IC base=-0.003)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.93` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.93 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.0953` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0953 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.4444` → IC=+0.177 (n=60)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4444 (IC base=-0.003)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=175)

- **FILTRO** `dist_vwap_pct` > `0.1613` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1613
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=208)

- **FILTRO** `volumen_regimen` < `0.7296` → IC=-0.350 (n=58)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7296
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=175)

- **FILTRO** `volumen_spike_ratio` > `3.0912` → IC=-0.256 (n=39)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.0912
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=120)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.368 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=129)

- **FILTRO** `ibs_20min` > `0.9091` → IC=-0.300 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9091
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=147)

- **FILTRO** `dist_vwap_pct` > `0.4139` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4139
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=174)

- **FILTRO** `sigma_ewma_delta_pct` > `8.389` → IC=-0.312 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.389
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=165)

- **FILTRO** `volumen_pendiente_norm` > `0.0718` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.228 (n=90)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0034` → IC=-0.256 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=40)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=40)

- **FILTRO** `sigma_h` < `0.0019` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0019
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

- **FILTRO** `sigma_ewma_delta_pct` > `2.55` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.55
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=52)

- **FILTRO** `volumen_regimen` > `0.8664` → IC=-0.364 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8664
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=62)

- **FILTRO** `libro_liquidez` < `3685.6992` → IC=-0.224 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 3685.6992
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.395 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=53)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.364 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=50)

- **FILTRO** `ibs_20min` > `0.8039` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8039
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=47)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=-0.220)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=65)

- **FILTRO** `ibs_20min` < `0.125` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `ibs_20min` < 0.125
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=62)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

- **FILTRO** `dist_vwap_pct` < `0.1871` → IC=-0.370 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `volumen_regimen` < `1.1043` → IC=-0.433 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1043
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.167 (n=142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0058 (IC base=+0.084)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.146 (n=312)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.6522 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.5113` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.5113 (IC base=+0.084)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.123 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0059 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.1558` → IC=+0.195 (n=280)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1558 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.126` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 6.126 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2687` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2687 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `2.5723` → IC=+0.142 (n=244)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.5723 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` > `1.5807` → IC=+0.132 (n=218)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 1.5807 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=337)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `3934.0004` → IC=+0.214 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3934.0004 (IC base=+0.094)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6781` → IC=-0.250 (n=42)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6781
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=86)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.187 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0034 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.232 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.179 (n=51)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 5.0 (IC base=+0.162)

- **PATRÓN** `ibs_20min` < `0.1622` → IC=+0.228 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1622 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.668` → IC=+0.177 (n=131)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 6.668 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` < `1.1644` → IC=+0.173 (n=145)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.1644 (IC base=+0.162)

- **PATRÓN** `volumen_regimen` > `0.8617` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.8617 (IC base=+0.162)

- **PATRÓN** `volumen_pendiente_norm` < `0.1895` → IC=+0.224 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1895 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` < `2.5856` → IC=+0.224 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5856 (IC base=+0.162)

- **PATRÓN** `volumen_spike_ratio` > `1.4478` → IC=+0.190 (n=114)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.4478 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `4472.275` → IC=+0.187 (n=97)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4472.275 (IC base=+0.162)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` < `0.6686` → IC=-0.197 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6686
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=96)

- **FILTRO** `libro_liquidez` < `1401.4113` → IC=-0.227 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 1401.4113
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=96)

- **FILTRO** `ibs_20min` > `0.156` → IC=-0.128 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.156
  - _Potencial_: sin este filtro IC_bueno=+0.187 (n=97)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.136 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0026 (IC base=+0.027)

- **PATRÓN** `libro_liquidez` > `1529.3843` → IC=+0.125 (n=86)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1529.3843 (IC base=+0.027)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.167 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0026 (IC base=+0.081)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.146 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 12.0 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.156` → IC=+0.187 (n=97)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.156 (IC base=+0.081)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.769` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.769 (IC base=+0.081)

- **PATRÓN** `volumen_regimen` < `0.9994` → IC=+0.126 (n=97)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.9994 (IC base=+0.081)

- **PATRÓN** `volumen_pendiente_norm` > `0.1683` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.1683 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `2188.8928` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2188.8928 (IC base=+0.081)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4194` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4194
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=64)

- **FILTRO** `dist_vwap_pct` > `0.2902` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2902
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=68)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.274 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.271 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.235 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.9583` → IC=+0.256 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.9583 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.6843` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6843 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.688` → IC=+0.261 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.688 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.307 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.3956` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3956 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `579.6494` → IC=+0.234 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 579.6494 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.040)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.271)

- **PATRÓN** `elapsed_s` > `210.3` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.3 (IC base=+0.271)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.8301` → IC=+0.354 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8301 (IC base=+0.271)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.271)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.219)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.219)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.219)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.333 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `1508.0` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1508.0 (IC base=+0.219)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.4522` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4522 (IC base=+0.271)

- **PATRÓN** `elapsed_s` > `210.3` → IC=+0.406 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 210.3 (IC base=+0.271)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.271)

- **PATRÓN** `drift_60min` |x|≤ `0.8301` → IC=+0.354 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8301 (IC base=+0.271)

- **PATRÓN** `ballena_activa_n` < `1127.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1127.0 (IC base=+0.271)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3676` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3676 (IC base=+0.219)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.219)

- **PATRÓN** `elapsed_s` < `207.3` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 207.3 (IC base=+0.219)

- **PATRÓN** `drift_15min` |x|≤ `2.1564` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.1564 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.6716` → IC=+0.333 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6716 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `1508.0` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1508.0 (IC base=+0.219)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.126 (n=853)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2919.5028` → IC=+0.159 (n=294)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2919.5028 (IC base=+0.108)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.126 (n=853)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` > 0.5 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2919.5028` → IC=+0.159 (n=294)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2919.5028 (IC base=+0.108)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `9.0` → IC=-0.175 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=84)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=146)

- **FILTRO** `libro_liquidez` < `2607.8903` → IC=-0.262 (n=40)

  - _Acción_: SKIP cuando `libro_liquidez` < 2607.8903
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=122)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=229)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=215)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=49)

- **FILTRO** `liq_n` < `6.0` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `liq_n` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.182 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=95)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=2211)

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
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=96)

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

- **PATRÓN** `liq_usd_total` > `96879.35` → IC=+0.134 (n=99)

  - _Acción_: Kelly boost +0.67€ cuando `liq_usd_total` > 96879.35 (IC base=+0.046)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.495 (IC base=+0.046)

### LIQUIDACIONES_5M#DOGE#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=152)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=921)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=875)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=522)

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
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=219)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.027)

- **PATRÓN** `libro_liquidez` > `4039.6046` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4039.6046 (IC base=+0.027)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=712)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=712)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=441)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=441)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=192)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=192)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.127 (n=81)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=126)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=106)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=130)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=233)

- **FILTRO** `py_entrada` > `0.55` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `py_entrada` > 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=114)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=117)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=272)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=272)

- **FILTRO** `libro_liquidez` < `535.3587` → IC=-0.124 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 535.3587
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=203)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=157)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.120 (n=872)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=873)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.123 (n=75)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=83)

- **PATRÓN** `py_entrada` > `0.52` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.52 (IC base=+0.006)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.46 (IC base=+0.046)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=95)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.184 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=81)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.127 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.078)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.130 (n=106)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=40)

- **FILTRO** `profundidad_ratio` < `54.9` → IC=-0.220 (n=48)

  - _Acción_: SKIP cuando `profundidad_ratio` < 54.9
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=98)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=130)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=159)

- **FILTRO** `restante_min` < `3.37` → IC=-0.254 (n=63)

  - _Acción_: SKIP cuando `restante_min` < 3.37
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=130)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.153 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=97)

- **FILTRO** `lag_apertura_s` > `96.03` → IC=-0.261 (n=65)

  - _Acción_: SKIP cuando `lag_apertura_s` > 96.03
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=128)

- **FILTRO** `profundidad_ratio` < `77.2` → IC=-0.204 (n=96)

  - _Acción_: SKIP cuando `profundidad_ratio` < 77.2
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=97)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=119)

- **PATRÓN** `restante_min` > `13.49` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `restante_min` > 13.49 (IC base=-0.009)

- **PATRÓN** `lag_apertura_s` < `95.05` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `lag_apertura_s` < 95.05 (IC base=-0.009)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.154 (n=131)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=70)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.167 (n=70)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.5 (IC base=-0.042)

- **PATRÓN** `profundidad_ratio` > `13.3` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `profundidad_ratio` > 13.3 (IC base=+0.031)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=174)

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
- **FILTRO** `py_entrada` < `0.475` → IC=-0.164 (n=4154)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=12562)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.163 (n=4199)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=13098)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.197 (n=725)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=2210)

- **PATRÓN** `libro_liquidez` > `1564.8769` → IC=+0.140 (n=1052)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 1564.8769 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.180 (n=732)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=2263)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=739)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=2387)

- **PATRÓN** `libro_liquidez` > `1791.0756` → IC=+0.122 (n=1019)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1791.0756 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.165 (n=718)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=2216)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2225)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2370)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3110)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `ibs_20min` > `0.1725` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1725
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=403)

- **FILTRO** `libro_liquidez` < `17076.8097` → IC=-0.144 (n=231)

  - _Acción_: SKIP cuando `libro_liquidez` < 17076.8097
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=695)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.146 (n=80)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=254)

- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ballena_activa_n` > `89.0` → IC=-0.220 (n=116)

  - _Acción_: SKIP cuando `ballena_activa_n` > 89.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=230)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=798)

- **FILTRO** `libro_liquidez` < `1911.1265` → IC=-0.177 (n=320)

  - _Acción_: SKIP cuando `libro_liquidez` < 1911.1265
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=652)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=11724)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=26066)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=8757)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=29033)

- **FILTRO** `ibs_7min` < `0.2667` → IC=-0.235 (n=9438)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=28352)

- **FILTRO** `ballena_activa_n` > `15.0` → IC=-0.156 (n=12537)

  - _Acción_: SKIP cuando `ballena_activa_n` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=25253)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=11681)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=36166)

- **FILTRO** `ibs_7min` > `0.291` → IC=-0.180 (n=11961)

  - _Acción_: SKIP cuando `ibs_7min` > 0.291
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=35886)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.139 (n=1905)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4443)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=1522)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=4826)

- **FILTRO** `ibs_7min` < `0.7077` → IC=-0.253 (n=2094)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7077
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=4254)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.178 (n=1497)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=4851)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.262 (n=2032)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=6219)

- **FILTRO** `ibs_7min` > `0.7925` → IC=-0.210 (n=2062)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7925
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6189)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.138 (n=1546)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=4939)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.250 (n=1587)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=4898)

- **FILTRO** `ibs_7min` < `0.744` → IC=-0.196 (n=1621)

  - _Acción_: SKIP cuando `ibs_7min` < 0.744
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4864)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.180 (n=1607)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=4878)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.262 (n=1530)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=5065)

- **FILTRO** `ibs_7min` > `0.2609` → IC=-0.184 (n=1648)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2609
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4947)

- **FILTRO** `ballena_activa_n` > `150.0` → IC=-0.185 (n=1644)

  - _Acción_: SKIP cuando `ballena_activa_n` > 150.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=4951)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.162 (n=1717)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=4335)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=1416)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4636)

- **FILTRO** `ibs_7min` < `0.705` → IC=-0.244 (n=1997)

  - _Acción_: SKIP cuando `ibs_7min` < 0.705
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=4055)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.209 (n=1450)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=4602)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.246 (n=2028)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=6796)

- **FILTRO** `ibs_7min` > `0.7456` → IC=-0.177 (n=2204)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7456
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=6620)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.233 (n=1835)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=4392)

- **FILTRO** `ibs_7min` < `0.7406` → IC=-0.180 (n=1556)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7406
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=4671)

- **FILTRO** `ballena_activa_n` > `30.0` → IC=-0.171 (n=1547)

  - _Acción_: SKIP cuando `ballena_activa_n` > 30.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=4680)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.258 (n=1582)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=4806)

- **FILTRO** `ibs_7min` > `0.2744` → IC=-0.179 (n=1594)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2744
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4794)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.182 (n=1540)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=4848)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.35` → IC=-0.263 (n=1569)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4904)

- **FILTRO** `ibs_7min` < `0.2647` → IC=-0.232 (n=1617)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2647
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=4856)

- **FILTRO** `py_entrada` > `0.6` → IC=-0.172 (n=2279)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=6866)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.37` → IC=-0.253 (n=1941)

  - _Acción_: SKIP cuando `py_entrada` < 0.37
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4264)

- **FILTRO** `ibs_7min` < `0.2702` → IC=-0.222 (n=1551)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2702
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=4654)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.213 (n=1454)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=4751)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.207 (n=2029)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=6615)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=1172)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=46)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=582)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1156)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=333)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=579)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=251)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4164` → IC=+0.147 (n=562)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4164 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.123 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `total_vol_5m` < `451.687` → IC=+0.154 (n=281)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 451.687 (IC base=+0.116)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.124 (n=710)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 54.0 (IC base=+0.116)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.142 (n=65)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.225 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.137)

- **PATRÓN** `total_vol_5m` < `421.686` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `total_vol_5m` < 421.686 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `2558.8539` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2558.8539 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.162 (n=69)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 11.0 (IC base=+0.137)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 11.0 (IC base=+0.113)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4137` → IC=+0.189 (n=117)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.4137 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.128 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 4.0 (IC base=+0.104)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.209 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.104)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 74.0 (IC base=+0.104)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3985` → IC=+0.158 (n=147)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.3985 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.173 (n=102)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 11.0 (IC base=+0.121)

- **PATRÓN** `total_vol_5m` < `6272.013` → IC=+0.144 (n=130)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 6272.013 (IC base=+0.121)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.4` → IC=+0.147 (n=148)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.127 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 13.0 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `3589.6144` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3589.6144 (IC base=+0.099)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.75` → IC=-0.244 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.75
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=113)

- **FILTRO** `sigma_h` > `0.0044` → IC=-0.245 (n=312)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0044
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=154)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0049` → IC=-0.226 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.257 (n=35)

- **FILTRO** `T_h` > `95.4629` → IC=-0.417 (n=34)

  - _Acción_: SKIP cuando `T_h` > 95.4629
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=105)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.103)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0087` → IC=-0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0087
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=26)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=34)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0081` → IC=-0.221 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

- **FILTRO** `T_h` < `39.9918` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `T_h` < 39.9918
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=63)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `pct_vs_K` |x|> `3.8113` → IC=-0.245 (n=108)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.8113
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=331)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.325 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=288)

- **FILTRO** `sigma_h` < `0.0045` → IC=-0.325 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0045
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=288)

- **FILTRO** `T_h` > `61.2269` → IC=-0.310 (n=287)

  - _Acción_: SKIP cuando `T_h` > 61.2269
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=96)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `68.7654` → IC=-0.152 (n=113)

  - _Acción_: SKIP cuando `T_h` > 68.7654
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=39)

- **FILTRO** `pct_vs_K` |x|> `2.8026` → IC=-0.372 (n=37)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8026
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=115)

- **FILTRO** `T_h` > `144.5168` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `T_h` > 144.5168
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=105)

- **FILTRO** `pct_vs_K` |x|> `2.9616` → IC=-0.439 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9616
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=92)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `135.9836` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `T_h` > 135.9836
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=92)

- **FILTRO** `pct_vs_K` |x|> `3.4756` → IC=-0.400 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4756
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=94)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.339 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=88)

- **FILTRO** `sigma_h` < `0.0048` → IC=-0.339 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=88)

- **FILTRO** `T_h` > `57.801` → IC=-0.338 (n=78)

  - _Acción_: SKIP cuando `T_h` > 57.801
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=39)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0141` → IC=-0.179 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0141
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=82)

- **FILTRO** `sigma_h` < `0.008` → IC=-0.155 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=81)

- **FILTRO** `T_h` > `135.6166` → IC=-0.179 (n=26)

  - _Acción_: SKIP cuando `T_h` > 135.6166
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=82)

- **FILTRO** `T_h` > `49.3826` → IC=-0.379 (n=56)

  - _Acción_: SKIP cuando `T_h` > 49.3826
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **PATRÓN** `pct_vs_K` |x|≤ `1.14` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.14 (IC base=-0.054)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1255` → IC=+0.468 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1255 (IC base=+0.353)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.387 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.353)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.391 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.353)

- **PATRÓN** `T_h` < `0.5922` → IC=+0.375 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5922 (IC base=+0.353)

- **PATRÓN** `T_h` > `1.2259` → IC=+0.420 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2259 (IC base=+0.353)

- **PATRÓN** `dist_50` > `0.4086` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4086 (IC base=+0.353)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.377 (n=55)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.353)

- **PATRÓN** `edge` > `0.096` → IC=+0.453 (n=169)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.420)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.432 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.420)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.448 (n=113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.420)

- **PATRÓN** `T_h` < `0.5967` → IC=+0.431 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5967 (IC base=+0.420)

- **PATRÓN** `T_h` > `1.4774` → IC=+0.449 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4774 (IC base=+0.420)

- **PATRÓN** `dist_50` > `0.4077` → IC=+0.482 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4077 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.474 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.420)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1072` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1072 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.403 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.418)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.452 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.418)

- **PATRÓN** `T_h` < `0.9168` → IC=+0.449 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9168 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.4172` → IC=+0.474 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4172 (IC base=+0.418)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.409 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.418)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.431 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.418)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.225` → IC=+0.476 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.225 (IC base=+0.434)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.469 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.434)

- **PATRÓN** `T_h` > `0.8294` → IC=+0.451 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8294 (IC base=+0.434)

- **PATRÓN** `dist_50` > `0.3691` → IC=+0.452 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3691 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.433 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.434)

- **PATRÓN** `edge` > `0.1155` → IC=+0.471 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1155 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0113` → IC=+0.487 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0113 (IC base=+0.463)

- **PATRÓN** `T_h` > `0.8021` → IC=+0.465 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8021 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.491 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.468 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=219)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=319)

- **PATRÓN** `streak_estiramiento` < `0.4493` → IC=+0.181 (n=92)

  - _Acción_: Kelly boost +0.90€ cuando `streak_estiramiento` < 0.4493 (IC base=+0.032)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4576` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4576
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=38)

- **PATRÓN** `streak_estiramiento` < `0.4576` → IC=+0.150 (n=38)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.4576 (IC base=-0.008)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.056)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 49.0 (IC base=+0.056)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=473)

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
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=707)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1279)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=859)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=841)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3197)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1618)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.202 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.231 (n=649)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.1593` → IC=+0.199 (n=1713)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.1593 (IC base=+0.193)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2187` → IC=+0.201 (n=649)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2187 (IC base=+0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.233 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.201 (n=1806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=2017)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_15` > `0.6154` → IC=+0.272 (n=1948)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6154 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.1189` → IC=+0.189 (n=971)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1189 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.822` → IC=+0.284 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.822 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `8676.3608` → IC=+0.205 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8676.3608 (IC base=+0.193)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=827)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.226 (n=378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.279 (n=143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.212)

- **PATRÓN** `drift_15min` |x|≤ `0.3831` → IC=+0.224 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3831 (IC base=+0.212)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2012` → IC=+0.245 (n=194)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2012 (IC base=+0.212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.4004` → IC=+0.246 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.4004 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.244 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.212)

- **PATRÓN** `ibs_15` > `0.7141` → IC=+0.277 (n=429)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7141 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.3824` → IC=+0.276 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3824 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.582` → IC=+0.273 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.582 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `16163.1166` → IC=+0.245 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16163.1166 (IC base=+0.212)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `29.297` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 29.297
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=502)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `ibs_15` < `0.6602` → IC=-0.125 (n=198)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6602
  - _Potencial_: sin este filtro IC_bueno=+0.262 (n=405)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.173 (n=151)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0035 (IC base=+0.135)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.141 (n=302)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.005 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.067` → IC=+0.152 (n=199)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.067 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2344` → IC=+0.173 (n=151)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio_macro` |x|> 0.2344 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1274` → IC=+0.159 (n=168)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1274 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.141 (n=474)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.6602` → IC=+0.262 (n=405)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6602 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.2902` → IC=+0.145 (n=421)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2902 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.307` → IC=+0.230 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.307 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `8676.3608` → IC=+0.149 (n=206)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 8676.3608 (IC base=+0.135)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `hora_utc` > `16.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=137)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.287 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1498` → IC=+0.210 (n=205)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1498 (IC base=+0.179)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0592` → IC=+0.194 (n=233)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.0592 (IC base=+0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3249` → IC=+0.229 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3249 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_15` > `0.5926` → IC=+0.270 (n=233)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5926 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1248` → IC=+0.195 (n=129)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1248 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.3278` → IC=+0.180 (n=229)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.3278 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.981` → IC=+0.400 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.981 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.180 (n=254)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `3077.8574` → IC=+0.278 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3077.8574 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.216 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.179)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `dist_vwap_pct` > `0.6834` → IC=-0.160 (n=104)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6834
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=1282)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.524` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 8.524 (IC base=-0.009)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.237 (n=447)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.085` → IC=+0.221 (n=220)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.085 (IC base=+0.198)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0626` → IC=+0.198 (n=448)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.99€ cuando `delta_ratio_macro` |x|> 0.0626 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0847` → IC=+0.259 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0847 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.228 (n=248)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.5769` → IC=+0.285 (n=500)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5769 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.3623` → IC=+0.210 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3623 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.994` → IC=+0.231 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.994 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2920.176` → IC=+0.287 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2920.176 (IC base=+0.198)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.358 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.352)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.381 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.352)

- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.355 (n=315)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.352)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.377 (n=314)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.352)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.390 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.352)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.371 (n=479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.352)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.390 (n=472)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.352)

- **PATRÓN** `dist_vwap_pct` > `0.4248` → IC=+0.387 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4248 (IC base=+0.352)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.357` → IC=+0.363 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.357 (IC base=+0.352)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.899` → IC=+0.352 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.899 (IC base=+0.352)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.356 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.352)

- **PATRÓN** `libro_liquidez` > `3823.0046` → IC=+0.370 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3823.0046 (IC base=+0.352)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.369 (n=173)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.358)

- **PATRÓN** `sigma_h` > `0.0025` → IC=+0.361 (n=258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0025 (IC base=+0.358)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.376 (n=87)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.358)

- **PATRÓN** `drift_15min` |x|≤ `0.4182` → IC=+0.371 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4182 (IC base=+0.358)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0706` → IC=+0.369 (n=258)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0706 (IC base=+0.358)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1241` → IC=+0.390 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1241 (IC base=+0.358)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.382 (n=260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.358)

- **PATRÓN** `ibs_15` > `0.8154` → IC=+0.389 (n=258)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8154 (IC base=+0.358)

- **PATRÓN** `dist_vwap_pct` > `0.3894` → IC=+0.397 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3894 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.106` → IC=+0.358 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.106 (IC base=+0.358)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.763` → IC=+0.361 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.763 (IC base=+0.358)

- **PATRÓN** `libro_liquidez` > `15909.0735` → IC=+0.386 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15909.0735 (IC base=+0.358)

- **PATRÓN** `ballena_activa_n` < `566.0` → IC=+0.401 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 566.0 (IC base=+0.358)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.379 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.343)

- **PATRÓN** `drift_60min` |x|≤ `0.1058` → IC=+0.355 (n=143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1058 (IC base=+0.343)

- **PATRÓN** `delta_ratio_macro` |x|> `0.087` → IC=+0.365 (n=191)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.087 (IC base=+0.343)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2986` → IC=+0.373 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2986 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.404 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.343)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.393 (n=213)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.343)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.394 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.343)

- **PATRÓN** `dist_vwap_pct` < `0.1197` → IC=+0.342 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1197 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.937` → IC=+0.358 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.937 (IC base=+0.343)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.694` → IC=+0.344 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 13.694 (IC base=+0.343)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.349 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.343)

- **PATRÓN** `libro_liquidez` > `4305.62` → IC=+0.363 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4305.62 (IC base=+0.343)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.226 (n=756)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2271)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=1060)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1967)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1366` → IC=+0.236 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1366 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6444` → IC=+0.276 (n=733)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6444 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2658` → IC=+0.192 (n=602)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.2658 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1231` → IC=+0.249 (n=1479)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1231 (IC base=-0.024)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1809` → IC=+0.246 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1809 (IC base=-0.024)

- **PATRÓN** `ibs_15` < `0.3507` → IC=+0.275 (n=2215)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3507 (IC base=-0.024)

- **PATRÓN** `dist_vwap_pct` > `0.6771` → IC=+0.295 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6771 (IC base=-0.024)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.217 (n=458)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1375)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.220 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1375)

- **FILTRO** `sigma_ewma_delta_pct` > `23.552` → IC=-0.257 (n=257)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.552
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=1576)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.167 (n=178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0028 (IC base=+0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2011` → IC=+0.282 (n=99)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2011 (IC base=+0.084)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.084)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.128 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 15.0 (IC base=+0.084)

- **PATRÓN** `ibs_15` > `0.7533` → IC=+0.332 (n=218)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7533 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1267` → IC=+0.289 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1267 (IC base=+0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0802` → IC=+0.157 (n=33)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.0802 (IC base=-0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1833` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1833 (IC base=-0.194)

- **PATRÓN** `ibs_15` < `0.5472` → IC=+0.294 (n=32)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.5472 (IC base=-0.194)

- **PATRÓN** `dist_vwap_pct` < `0.0553` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0553 (IC base=-0.194)

- **PATRÓN** `ballena_activa_n` < `305.0` → IC=+0.385 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 305.0 (IC base=-0.194)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=451)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.150 (n=352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0065 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.168 (n=314)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.004 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0736` → IC=+0.207 (n=155)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0736 (IC base=+0.147)

- **PATRÓN** `drift_15min` |x|≤ `0.4157` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `drift_15min` |x|≤ 0.4157 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.219 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.173 (n=255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.6642` → IC=+0.262 (n=351)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6642 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.4682` → IC=+0.150 (n=98)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.4682 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.1109` → IC=+0.176 (n=254)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1109 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=451)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `10510.4052` → IC=+0.185 (n=160)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 10510.4052 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.245 (n=853)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.239 (n=853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.233)

- **PATRÓN** `drift_15min` |x|≤ `0.7826` → IC=+0.245 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7826 (IC base=+0.233)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2075` → IC=+0.256 (n=387)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2075 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=330)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.235 (n=587)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.233)

- **PATRÓN** `ibs_15` < `0.2756` → IC=+0.278 (n=751)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2756 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.7528` → IC=+0.318 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7528 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.226` → IC=+0.264 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.226 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.457` → IC=+0.238 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.457 (IC base=+0.233)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1704` → IC=-0.233 (n=241)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1704
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=470)

- **FILTRO** `drift_15min` |x|> `0.9054` → IC=-0.265 (n=177)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9054
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=534)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.185 (n=52)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.5625 (IC base=-0.175)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0785` → IC=+0.231 (n=332)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0785 (IC base=-0.040)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.183` → IC=+0.224 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.183 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.270 (n=372)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.7305` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7305 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.1721` → IC=+0.234 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1721 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.267 (n=427)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=428)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.265 (n=240)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=615)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.272 (n=257)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=-0.036)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1664` → IC=+0.310 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1664 (IC base=-0.036)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.296 (n=566)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` > `0.8954` → IC=+0.343 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8954 (IC base=-0.036)

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
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.303 (n=512)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.326 (n=256)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2394` → IC=+0.306 (n=256)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2394 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2223` → IC=+0.320 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2223 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.311 (n=804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8418` → IC=+0.330 (n=768)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8418 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.436` → IC=+0.338 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.436 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.348 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `13050.0559` → IC=+0.297 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13050.0559 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.299 (n=282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0549` → IC=+0.332 (n=141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0549 (IC base=+0.285)

- **PATRÓN** `drift_15min` |x|≤ `0.4201` → IC=+0.287 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4201 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2556` → IC=+0.311 (n=141)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2556 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3977` → IC=+0.308 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3977 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.318 (n=422)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.4113` → IC=+0.358 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4113 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.469` → IC=+0.357 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.469 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `16196.8854` → IC=+0.318 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16196.8854 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.305 (n=306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0525` → IC=+0.314 (n=116)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0525 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.298 (n=231)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2925` → IC=+0.325 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2925 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.313 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8539` → IC=+0.339 (n=346)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8539 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.312 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.564` → IC=+0.334 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.564 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.295 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

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
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=339)

- **FILTRO** `ballena_activa_n` > `41.0` → IC=-0.197 (n=64)

  - _Acción_: SKIP cuando `ballena_activa_n` > 41.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=126)

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

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.318 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2122` → IC=-0.395 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2122
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0943` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0943
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.188 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `79.3918` → IC=+0.222 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 79.3918 (IC base=+0.209)

- **PATRÓN** `ratio` < `0.9771` → IC=+0.470 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9771 (IC base=+0.209)

- **PATRÓN** `T_h` > `145.7579` → IC=+0.393 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7579 (IC base=+0.334)

- **PATRÓN** `ratio` > `1.0104` → IC=+0.309 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0104 (IC base=+0.334)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.3604` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.3604 (IC base=+0.189)

- **PATRÓN** `ratio` < `0.9722` → IC=+0.467 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9722 (IC base=+0.189)

- **PATRÓN** `T_h` > `103.5964` → IC=+0.295 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 103.5964 (IC base=+0.285)

- **PATRÓN** `ratio` > `1.0467` → IC=+0.371 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0467 (IC base=+0.285)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `80.0063` → IC=+0.267 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 80.0063 (IC base=+0.245)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.425 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.245)

- **PATRÓN** `T_h` > `106.9285` → IC=+0.333 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 106.9285 (IC base=+0.316)

- **PATRÓN** `ratio` > `1.015` → IC=+0.345 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.015 (IC base=+0.316)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1132` → IC=+0.455 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.402)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6154 sube el IC de +0.193 a +0.272 en UPDOWN_GBM#15min (n=1948). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7141 sube el IC de +0.212 a +0.277 en UPDOWN_GBM#BTC#15min (n=429). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6602 sube el IC de +0.135 a +0.262 en UPDOWN_GBM#ETH#15min (n=405). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.5926 sube el IC de +0.179 a +0.270 en UPDOWN_GBM#SOL#15min (n=233). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5769 sube el IC de +0.198 a +0.285 en UPDOWN_GBM#XRP#15min (n=500). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6444 sube el IC de -0.066 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=733). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3507 sube el IC de -0.024 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=2215). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7533 sube el IC de +0.084 a +0.332 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=218). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.5472 sube el IC de -0.194 a +0.294 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=32). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6642 sube el IC de +0.147 a +0.262 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=351). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.2756 sube el IC de +0.233 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=751). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.175 a +0.185 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=52). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.040 a +0.270 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=372). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.036 a +0.296 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=566). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8418 sube el IC de +0.290 a +0.330 en UPDOWN_GBM_IBS_ALTO (n=768). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.285 a +0.318 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=422). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8539 sube el IC de +0.295 a +0.339 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=346). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.352 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=472). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8154 sube el IC de +0.358 a +0.389 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=258). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.343 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=213). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC#sniper` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#BTC` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.085 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.085 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1448 | +0.099 | +202.00€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1448 | +0.099 | +202.00€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1097 | +0.108 | +172.28€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1097 | +0.108 | +172.28€ | 2 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 255 | +0.056 | +9.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 255 | +0.056 | +9.04€ | 4 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 65 | +0.142 | +21.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 65 | +0.142 | +21.02€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 15 | +0.022 | -2.28€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 15 | +0.022 | -2.28€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 12 | +0.043 | -1.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 12 | +0.043 | -1.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 31181 | -0.087 | -4052.54€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1613 | -0.025 | -216.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 29568 | -0.090 | -3835.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4086 | -0.106 | -652.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4086 | -0.106 | -652.19€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1613 | -0.025 | -216.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1613 | -0.025 | -216.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 3669 | -0.104 | -835.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 3669 | -0.104 | -835.20€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 8086 | -0.018 | -766.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 8086 | -0.018 | -766.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 7677 | -0.095 | -453.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 7677 | -0.095 | -453.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 6050 | -0.162 | -1128.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 6050 | -0.162 | -1128.10€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 22442 | -0.023 | +3801.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 5811 | +0.001 | +1772.86€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 16631 | -0.031 | +2028.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 22442 | -0.023 | +3801.51€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 5811 | +0.001 | +1772.86€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 16631 | -0.031 | +2028.65€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 105938 | +0.112 | -5170.89€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 15334 | +0.184 | -471.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 442 | -0.063 | -57.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 83474 | +0.101 | -4398.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 6688 | +0.106 | -243.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 13868 | +0.100 | -1075.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 49 | -0.147 | +8.51€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 13804 | +0.101 | -1072.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 21204 | +0.130 | -424.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 4717 | +0.199 | -149.82€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 13845 | +0.113 | -197.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 2600 | +0.096 | -54.97€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 13914 | +0.091 | -1216.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 57 | -0.110 | -7.74€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 13842 | +0.092 | -1197.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 22491 | +0.124 | -429.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 6062 | +0.177 | -76.51€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 13994 | +0.105 | -289.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2423 | +0.101 | -54.78€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 20573 | +0.114 | -1174.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4397 | +0.188 | -255.48€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 345 | -0.025 | -3.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 14166 | +0.092 | -781.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1665 | +0.131 | -134.16€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13888 | +0.098 | -850.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 52 | -0.037 | +9.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 13823 | +0.099 | -860.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 16847 | +0.195 | -1038.02€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 16847 | +0.195 | -1038.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 3949 | +0.172 | -383.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 3949 | +0.172 | -383.79€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 1649 | +0.204 | -10.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 1649 | +0.204 | -10.02€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 3894 | +0.182 | -315.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 3894 | +0.182 | -315.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 3440 | +0.243 | -103.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 3440 | +0.243 | -103.69€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 3836 | +0.191 | -238.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 3836 | +0.191 | -238.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 788 | +0.432 | -18.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 788 | +0.432 | -18.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 307 | +0.442 | -0.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 307 | +0.442 | -0.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 301 | +0.431 | -7.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 301 | +0.431 | -7.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 168 | +0.412 | -8.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 168 | +0.412 | -8.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 58389 | +0.198 | -4495.57€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 58389 | +0.198 | -4495.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 10055 | +0.179 | -1125.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 10055 | +0.179 | -1125.66€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 9352 | +0.222 | -346.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 9352 | +0.222 | -346.71€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 10070 | +0.175 | -1160.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 10070 | +0.175 | -1160.21€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 9442 | +0.218 | -372.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 9442 | +0.218 | -372.76€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 9671 | +0.203 | -635.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 9671 | +0.203 | -635.90€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 9799 | +0.192 | -854.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 9799 | +0.192 | -854.33€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 22183 | +0.115 | +111.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 22183 | +0.115 | +111.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 11012 | +0.119 | +109.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 11012 | +0.119 | +109.40€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 11171 | +0.112 | +2.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 11171 | +0.112 | +2.34€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1632 | +0.288 | -28.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1632 | +0.288 | -28.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 730 | +0.277 | -21.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 730 | +0.277 | -21.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 788 | +0.287 | -10.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 788 | +0.287 | -10.84€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 114 | +0.345 | +3.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 114 | +0.345 | +3.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 722 | +0.436 | -3.20€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 722 | +0.436 | -3.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 346 | +0.434 | -3.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 346 | +0.434 | -3.90€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 331 | +0.440 | +0.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 331 | +0.440 | +0.31€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 45 | +0.394 | +0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 45 | +0.394 | +0.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1248 | +0.065 | -68.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 438 | +0.050 | -41.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 810 | +0.073 | -27.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 65 | +0.112 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 65 | +0.112 | +2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 986 | +0.071 | -37.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 176 | +0.062 | -10.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 810 | +0.073 | -27.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 197 | +0.018 | -34.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 197 | +0.018 | -34.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 41982 | +0.098 | -1218.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 3440 | +0.088 | +18.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 38542 | +0.099 | -1237.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 23393 | +0.102 | -352.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 3440 | +0.088 | +18.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 19953 | +0.104 | -370.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 8157 | +0.107 | -39.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 8157 | +0.107 | -39.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 10432 | +0.081 | -827.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 10432 | +0.081 | -827.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 855 | +0.212 | -100.84€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 855 | +0.212 | -100.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 855 | +0.212 | -100.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 855 | +0.212 | -100.84€ | 1 | 4 |
| ✅ GBM_LATE_15M | 29625 | +0.087 | +14547.20€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 29625 | +0.087 | +14547.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 4970 | +0.200 | +3763.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 4970 | +0.200 | +3763.09€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 4420 | +0.180 | +3192.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 4420 | +0.180 | +3192.11€ | 0 | 27 |
| ✅ GBM_LATE_15M#DOGE | 5232 | +0.199 | +3921.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 5232 | +0.199 | +3921.70€ | 0 | 23 |
| ✅ GBM_LATE_15M#ETH | 4241 | +0.029 | +1022.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 4241 | +0.029 | +1022.49€ | 1 | 15 |
| ✅ GBM_LATE_15M#SOL | 4222 | -0.032 | +937.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 4222 | -0.032 | +937.92€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 6540 | -0.038 | +1709.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 6540 | -0.038 | +1709.89€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 31681 | +0.088 | +16866.87€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 31681 | +0.088 | +16866.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 6055 | +0.014 | +3164.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 6055 | +0.014 | +3164.67€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 6592 | +0.016 | +1407.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 6592 | +0.016 | +1407.81€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 4498 | +0.267 | +4617.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 4498 | +0.267 | +4617.02€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 5242 | +0.009 | +1105.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 5242 | +0.009 | +1105.33€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 5112 | +0.035 | +2039.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 5112 | +0.035 | +2039.64€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4182 | +0.280 | +4532.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4182 | +0.280 | +4532.40€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 23840 | +0.171 | +18210.82€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 23840 | +0.171 | +18210.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 3590 | +0.212 | +2930.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 3590 | +0.212 | +2930.34€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 3764 | +0.149 | +2756.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 3764 | +0.149 | +2756.38€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 3764 | +0.211 | +3038.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 3764 | +0.211 | +3038.57€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4006 | +0.135 | +2886.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4006 | +0.135 | +2886.34€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 4461 | +0.121 | +3216.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 4461 | +0.121 | +3216.03€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 4255 | +0.205 | +3383.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 4255 | +0.205 | +3383.15€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 6399 | +0.138 | +3002.01€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 6399 | +0.138 | +3002.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 278 | +0.132 | +144.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 278 | +0.132 | +144.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 1831 | +0.140 | +956.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 1831 | +0.140 | +956.61€ | 0 | 29 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 374 | +0.144 | +177.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 1925 | +0.154 | +943.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 1925 | +0.154 | +943.07€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1485 | +0.114 | +565.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1485 | +0.114 | +565.70€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 506 | +0.134 | +215.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 506 | +0.134 | +215.28€ | 0 | 27 |
| ✅ GBM_LATE_15M_TARDIO | 29876 | +0.178 | +22811.80€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 29876 | +0.178 | +22811.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 4732 | +0.227 | +4129.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 4732 | +0.227 | +4129.16€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 4659 | +0.152 | +3107.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 4659 | +0.152 | +3107.73€ | 0 | 28 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 4964 | +0.226 | +4283.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 4964 | +0.226 | +4283.58€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 4852 | +0.135 | +3381.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 4852 | +0.135 | +3381.97€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 5232 | +0.120 | +3540.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 5232 | +0.120 | +3540.40€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 5437 | +0.209 | +4368.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 5437 | +0.209 | +4368.96€ | 0 | 25 |
| ✅ GBM_LATE_5M | 8421 | +0.171 | +5553.93€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 8421 | +0.171 | +5553.93€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 826 | +0.226 | +711.40€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2015 | +0.166 | +1460.59€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2015 | +0.166 | +1460.59€ | 0 | 29 |
| ✅ GBM_LATE_5M#DOGE | 922 | +0.172 | +589.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 922 | +0.172 | +589.62€ | 0 | 20 |
| ✅ GBM_LATE_5M#ETH | 2748 | +0.176 | +1801.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 2748 | +0.176 | +1801.38€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 878 | +0.150 | +489.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 878 | +0.150 | +489.28€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1032 | +0.139 | +501.65€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2083 | +0.071 | +758.70€ | 0 | 16 |
| ✅ GBM_LATE_60M#60min | 2083 | +0.071 | +758.70€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 775 | +0.092 | +275.90€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 775 | +0.092 | +275.90€ | 0 | 16 |
| ✅ GBM_LATE_60M#ETH | 674 | +0.072 | +300.70€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 674 | +0.072 | +300.70€ | 2 | 16 |
| ✅ GBM_LATE_60M#SOL | 634 | +0.043 | +182.10€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 634 | +0.043 | +182.10€ | 2 | 9 |
| 🚫 GBM_LATE_60M_FADE | 428 | -0.246 | -16.22€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 428 | -0.246 | -16.22€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 161 | -0.218 | -5.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 161 | -0.218 | -5.44€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 143 | -0.245 | -5.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 143 | -0.245 | -5.01€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 124 | -0.278 | -5.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 124 | -0.278 | -5.77€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 838 | +0.089 | +202.71€ | 0 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 838 | +0.089 | +202.71€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 321 | +0.079 | +64.13€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 321 | +0.079 | +64.13€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 273 | +0.056 | +31.46€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 273 | +0.056 | +31.46€ | 3 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 244 | +0.138 | +107.12€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 244 | +0.138 | +107.12€ | 2 | 11 |
| ✅ LATE_WINDOW_5MIN | 114 | +0.250 | +94.41€ | 0 | 11 |
| ✅ LATE_WINDOW_5MIN#5min | 114 | +0.250 | +94.41€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 114 | +0.250 | +94.41€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 114 | +0.250 | +94.41€ | 0 | 11 |
| ✅ LEADLAG_BTC_XRP_15M | 2400 | +0.104 | +644.34€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 2400 | +0.104 | +644.34€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 2400 | +0.104 | +644.34€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 2400 | +0.104 | +644.34€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 412 | -0.075 | -34.00€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 412 | -0.075 | -34.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 109 | -0.050 | -4.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 109 | -0.050 | -4.14€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 68 | -0.086 | -7.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 68 | -0.086 | -7.96€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 154 | -0.026 | -5.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 154 | -0.026 | -5.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 2411 | +0.017 | +53.02€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 2411 | +0.017 | +53.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 126 | +0.016 | -3.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 126 | +0.016 | -3.07€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 326 | +0.021 | +23.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 326 | +0.021 | +23.24€ | 4 | 2 |
| ✅ LIQUIDACIONES_5M#DOGE | 180 | -0.017 | -4.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 180 | -0.017 | -4.39€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 969 | +0.027 | +27.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 969 | +0.027 | +27.41€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 562 | +0.009 | -0.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 562 | +0.009 | -0.75€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 248 | +0.016 | +10.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 248 | +0.016 | +10.59€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M | 1248 | -0.042 | -24.53€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1248 | -0.042 | -24.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 352 | -0.040 | -12.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 352 | -0.040 | -12.37€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 422 | -0.026 | -0.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 422 | -0.026 | -0.38€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 474 | -0.057 | -11.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 474 | -0.057 | -11.79€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 3355 | -0.016 | +86.90€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 1583 | -0.019 | +28.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 1772 | -0.013 | +58.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 94 | +0.021 | +9.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 48 | +0.080 | +12.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 46 | -0.042 | -3.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 794 | +0.003 | +47.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 373 | +0.007 | +21.72€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 421 | -0.001 | +25.86€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 400 | -0.015 | +17.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 192 | -0.036 | +0.39€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 208 | +0.005 | +17.18€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 672 | -0.044 | -35.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 306 | -0.052 | -23.13€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 366 | -0.038 | -12.20€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 656 | -0.020 | +15.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 318 | -0.028 | +3.48€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 338 | -0.012 | +11.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 739 | -0.011 | +32.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 346 | -0.011 | +13.53€ | 1 | 2 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 393 | -0.011 | +18.93€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 34013 | -0.005 | +1541.99€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 34013 | -0.005 | +1541.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 6027 | +0.022 | +763.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 6027 | +0.022 | +763.07€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 5149 | -0.031 | -71.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 5149 | -0.031 | -71.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 6121 | +0.017 | +553.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 6121 | +0.017 | +553.46€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 4931 | -0.054 | -169.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 4931 | -0.054 | -169.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 5729 | -0.010 | +195.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 5729 | -0.010 | +195.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 6056 | +0.011 | +271.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 6056 | +0.011 | +271.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6053 | -0.061 | -154.92€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6053 | -0.061 | -154.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1216 | +0.001 | -13.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1461 | -0.084 | -41.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1461 | -0.084 | -41.97€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 45 | -0.117 | -5.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 688 | -0.126 | -33.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 688 | -0.126 | -33.15€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1789 | -0.078 | -35.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1789 | -0.078 | -35.57€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 85637 | -0.073 | +1823.78€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 85637 | -0.073 | +1823.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 14599 | -0.076 | +866.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 14599 | -0.076 | +866.72€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 13080 | -0.095 | -673.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 13080 | -0.095 | -673.35€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 14876 | -0.067 | +767.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 14876 | -0.067 | +767.11€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 12615 | -0.091 | -220.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 12615 | -0.091 | -220.25€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 15618 | -0.049 | +383.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 15618 | -0.049 | +383.22€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 14849 | -0.063 | +700.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 14849 | -0.063 | +700.33€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 7879 | -0.028 | -131.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 7879 | -0.028 | -131.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1815 | -0.037 | -11.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1815 | -0.037 | -11.46€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1003 | -0.020 | -31.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2230 | -0.024 | -27.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2230 | -0.024 | -27.68€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1069 | -0.043 | -16.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1069 | -0.043 | -16.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 766 | -0.022 | -24.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 766 | -0.022 | -24.97€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1257 | +0.110 | +435.89€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1121 | +0.116 | +423.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 257 | +0.137 | +128.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 257 | +0.137 | +128.14€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 215 | +0.113 | +65.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 215 | +0.113 | +65.10€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 233 | +0.104 | +84.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 233 | +0.104 | +84.73€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 196 | +0.121 | +82.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 196 | +0.121 | +82.21€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 220 | +0.099 | +63.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 220 | +0.099 | +63.12€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 699 | -0.036 | -44.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 699 | -0.036 | -44.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 140 | +0.000 | +5.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 140 | +0.000 | +5.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 100 | -0.059 | -10.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 100 | -0.059 | -10.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 199 | -0.052 | -22.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 199 | -0.052 | -22.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 145 | -0.024 | -7.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 145 | -0.024 | -7.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 115 | -0.047 | -9.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 115 | -0.047 | -9.62€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 683 | -0.097 | -63.73€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 312 | -0.146 | -73.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 241 | -0.191 | -68.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 71 | +0.007 | -4.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 242 | -0.061 | -3.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 173 | -0.071 | -6.51€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 69 | -0.035 | +3.24€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 129 | -0.042 | +13.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 101 | -0.063 | +7.26€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 28 | +0.033 | +5.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 515 | -0.127 | -68.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 168 | -0.006 | +4.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 822 | -0.199 | -37.16€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 341 | -0.194 | -29.51€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 291 | -0.196 | -29.68€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 50 | -0.173 | +0.17€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 280 | -0.216 | -25.34€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 239 | -0.226 | -31.18€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 41 | -0.151 | +5.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 201 | -0.180 | +17.69€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 183 | -0.176 | +14.04€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#reach | 18 | -0.180 | +3.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 713 | -0.202 | -46.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 109 | -0.176 | +9.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 347 | +0.403 | +266.83€ | 0 | 14 |
| ✅ RESOLUTION_SNIPER#BTC | 39 | +0.134 | +0.80€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 39 | +0.134 | +0.80€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 87 | +0.365 | +72.33€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 87 | +0.365 | +72.33€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 221 | +0.460 | +193.70€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 221 | +0.460 | +193.70€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 347 | +0.403 | +266.83€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 576 | +0.033 | +17.69€ | 2 | 1 |
| ✅ STREAK_FADE_15M#15min | 576 | +0.033 | +17.69€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 281 | +0.030 | +3.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 281 | +0.030 | +3.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 39 | +0.085 | +3.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 39 | +0.085 | +3.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 62 | +0.000 | -1.18€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 62 | +0.000 | -1.18€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 194 | +0.036 | +11.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 194 | +0.036 | +11.78€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 2959 | -0.022 | -118.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 2959 | -0.022 | -118.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 897 | -0.021 | -31.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 897 | -0.021 | -31.16€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 576 | -0.024 | -24.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 576 | -0.024 | -24.20€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 156 | -0.044 | -14.41€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 156 | -0.044 | -14.41€ | 5 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1330 | -0.019 | -48.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1330 | -0.019 | -48.80€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 77 | -0.044 | -5.84€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 77 | -0.044 | -5.84€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 38 | -0.100 | -4.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 38 | -0.100 | -4.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 39 | +0.012 | -1.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 9009 | +0.022 | +126.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 9009 | +0.022 | +126.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2488 | +0.024 | +32.52€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2488 | +0.024 | +32.52€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2053 | +0.031 | +52.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2053 | +0.031 | +52.12€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2726 | +0.014 | +9.94€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2726 | +0.014 | +9.94€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 1742 | +0.024 | +32.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 1742 | +0.024 | +32.30€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 8080 | +0.013 | -44.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 8080 | +0.013 | -44.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3216 | +0.017 | -8.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3216 | +0.017 | -8.14€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3212 | +0.012 | -21.19€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3212 | +0.012 | -21.19€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 1652 | +0.006 | -15.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 1652 | +0.006 | -15.21€ | 1 | 0 |
| ✅ UPDOWN_GBM | 47197 | +0.037 | +3171.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 12206 | +0.073 | +2347.59€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 1647 | +0.004 | +7.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 30336 | +0.029 | +791.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 2832 | +0.003 | +25.84€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 4782 | +0.075 | +594.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 886 | +0.158 | +383.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 33 | -0.014 | -0.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 3863 | +0.057 | +212.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 9073 | +0.046 | +705.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 1589 | +0.089 | +369.85€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 441 | +0.012 | +5.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 5696 | +0.047 | +298.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1281 | +0.004 | +31.92€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 66 | -0.088 | +0.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 5439 | +0.044 | +374.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 835 | +0.142 | +304.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 28 | +0.000 | -1.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 4576 | +0.026 | +70.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 10369 | +0.027 | +469.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3065 | +0.050 | +353.43€ | 1 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 434 | +0.007 | +9.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 5860 | +0.023 | +112.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 952 | -0.001 | -8.55€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 58 | -0.117 | +3.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 10643 | +0.018 | +313.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 2925 | +0.028 | +213.86€ | 0 | 13 |
| ✅ UPDOWN_GBM#SOL#240min | 425 | -0.004 | -1.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 6644 | +0.018 | +101.88€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 599 | +0.006 | +2.48€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 50 | -0.154 | -3.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 6889 | +0.041 | +715.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 2906 | +0.087 | +722.41€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 286 | +0.000 | -3.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 3697 | +0.007 | -3.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 174 | -0.119 | +0.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 628 | +0.352 | +213.13€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 628 | +0.352 | +213.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 344 | +0.358 | +115.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 344 | +0.358 | +115.60€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 284 | +0.343 | +97.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 284 | +0.343 | +97.54€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 13917 | -0.033 | +3049.84€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 13917 | -0.033 | +3049.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 986 | -0.050 | +384.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 986 | -0.050 | +384.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 2542 | -0.116 | +53.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 2542 | -0.116 | +53.87€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 525 | +0.196 | +386.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 525 | +0.196 | +386.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 1605 | +0.208 | +972.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 1605 | +0.208 | +972.73€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 4143 | -0.063 | +587.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 4143 | -0.063 | +587.39€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 4116 | -0.072 | +664.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 4116 | -0.072 | +664.89€ | 2 | 4 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 157 | +0.035 | +7.28€ | 1 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 157 | +0.035 | +7.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 157 | +0.035 | +7.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 157 | +0.035 | +7.28€ | 1 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1023 | +0.290 | +827.45€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1023 | +0.290 | +827.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 562 | +0.285 | +433.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 562 | +0.285 | +433.41€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 461 | +0.295 | +394.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 461 | +0.295 | +394.04€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 743 | -0.112 | -83.46€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 743 | -0.112 | -83.46€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 220 | -0.081 | -16.26€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 220 | -0.081 | -16.26€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 70 | -0.167 | -9.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 70 | -0.167 | -9.32€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 74 | -0.197 | -7.82€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 74 | -0.197 | -7.82€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 34 | -0.194 | -7.31€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 2686 | +0.303 | +1314.66€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 941 | +0.255 | +137.45€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1022 | +0.294 | +439.08€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 723 | +0.377 | +738.13€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.054) — sin ventaja clara. oversold(IBS<0.3): IC=+0.049 n=16563 | neutral: IC=+0.037 n=17580 | overbought(IBS>0.7): IC=+0.091 n=16885
  - _Datos_: n=52869 IC=+0.060 PNL=+6763.88€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 585 celda(s) pasan gate riguroso completo de 2349 evaluadas (n>=40) y 3325 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.028 < 0.08 — monitorear
  - _Datos_: n=2925 IC=+0.028 PNL=+213.86€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1022/15 IC=+0.294 PNL=+439.08€ | BTC: n=941/15 IC=+0.255 PNL=+137.45€ | SOL: n=723/15 IC=+0.377 PNL=+738.13€

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
  - _Estado_: 47135 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.121 n=428/60 | contraria IC=+0.174 n=406 | gap=-0.053 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=337, boost estimado=+0.007. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 196 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=952/40 IC=-0.001 PNL=-8.55€ | BTC#60min: n=1281/40 IC=+0.004 PNL=+31.92€ | SOL#60min: n=599/40 IC=+0.006 PNL=+2.48€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.049 n=390811 | tras_1loss IC=+0.084 n=301659 | tras_2loss IC=+0.054 n=125364/40 | gap=-0.005 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.021 n=5808 | contrario_BTC IC=+0.034 n=5138/40 | gap=+0.013 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.08 con n=399 PNL=+285.45€
  - _Datos_: n=399 IC=+0.206 PNL=+285.45€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.08 con n=454 PNL=+335.34€
  - _Datos_: n=454 IC=+0.210 PNL=+335.34€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.330 > 0.1 con n=2193 PNL=+1194.85€
  - _Datos_: n=2193 IC=+0.330 PNL=+1194.85€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=375 IC=+0.070 PNL=+41.13€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=375 IC=+0.070 PNL=+41.13€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=58 IC=+0.167 PNL=+33.93€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=58 IC=+0.167 PNL=+33.93€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=45152 IC=+0.037 PNL=+3033.04€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=45152 IC=+0.037 PNL=+3033.04€

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
  - _Estado_: n=1951 IC=+0.004 PNL=-4.55€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1951 IC=+0.004 PNL=-4.55€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=881 IC=-0.001 PNL=+30.40€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=881 IC=-0.001 PNL=+30.40€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=605 IC=+0.017 PNL=+26.45€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=605 IC=+0.017 PNL=+26.45€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.193 > 0.1 con n=2595 PNL=+1714.49€
  - _Datos_: n=2595 IC=+0.193 PNL=+1714.49€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=1476 IC=+0.055 PNL=+105.96€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1476 IC=+0.055 PNL=+105.96€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=1589 IC=+0.089 PNL=+369.85€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=1589 IC=+0.089 PNL=+369.85€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.091 > 0.08 con n=6964 PNL=+1776.07€
  - _Datos_: n=6964 IC=+0.091 PNL=+1776.07€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=186 IC=-0.250 PNL=-6.59€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=186 IC=-0.250 PNL=-6.59€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=308 IC=-0.035 PNL=-3.81€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=308 IC=-0.035 PNL=-3.81€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=634 IC=+0.022 PNL=+44.99€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=634 IC=+0.022 PNL=+44.99€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=68 IC=+0.057 PNL=+4.37€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=68 IC=+0.057 PNL=+4.37€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=6333 IC=+0.000 PNL=+7.42€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6333 IC=+0.000 PNL=+7.42€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.184 > 0.08 con n=74 PNL=+21.75€
  - _Datos_: n=74 IC=+0.184 PNL=+21.75€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.250 n=114) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=114 IC=+0.250 PNL=+94.41€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=8620 IC=+0.039 PNL=+557.09€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=8620 IC=+0.039 PNL=+557.09€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=2889 IC=+0.058 PNL=+366.72€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2889 IC=+0.058 PNL=+366.72€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.08 con n=400 PNL=+124.43€
  - _Datos_: n=400 IC=+0.112 PNL=+124.43€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.147 > 0.08 con n=724 PNL=+188.64€
  - _Datos_: n=724 IC=+0.147 PNL=+188.64€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.08 con n=558 PNL=+264.76€
  - _Datos_: n=558 IC=+0.105 PNL=+264.76€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64104 IC=+0.118 PNL=+23839.01€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64104 IC=+0.118 PNL=+23839.01€

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
  - _Estado_: n=6919 IC=+0.042 PNL=+542.04€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6919 IC=+0.042 PNL=+542.04€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.02 con n=715 PNL=+271.49€
  - _Datos_: n=715 IC=+0.119 PNL=+271.49€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=179 IC=-0.064 PNL=+28.99€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=179 IC=-0.064 PNL=+28.99€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.449 > 0.1 con n=1256 PNL=+1230.93€
  - _Datos_: n=1256 IC=+0.449 PNL=+1230.93€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=17181 IC=+0.060 PNL=+2154.68€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=17181 IC=+0.060 PNL=+2154.68€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.1 con n=4218 PNL=+2350.81€
  - _Datos_: n=4218 IC=+0.202 PNL=+2350.81€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.152 < -0.1 con n=285 PNL=+27.20€
  - _Datos_: n=285 IC=-0.152 PNL=+27.20€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2240 IC=+0.053 PNL=+228.31€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2240 IC=+0.053 PNL=+228.31€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=95 IC=-0.108 PNL=+4.21€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=95 IC=-0.108 PNL=+4.21€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.1 con n=524 PNL=+142.82€
  - _Datos_: n=524 IC=+0.124 PNL=+142.82€

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
  - _Estado_: n=21400 IC=-0.136 PNL=+1529.56€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=21400 IC=-0.136 PNL=+1529.56€

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
  - _Estado_: n=2230 IC=+0.140 PNL=+1282.46€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2230 IC=+0.140 PNL=+1282.46€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.194 > 0.08 con n=2556 PNL=+1701.86€
  - _Datos_: n=2556 IC=+0.194 PNL=+1701.86€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=4955 IC=+0.028 PNL=+222.30€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4955 IC=+0.028 PNL=+222.30€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.089 > 0.08 con n=2413 PNL=+1298.65€
  - _Datos_: n=2413 IC=+0.089 PNL=+1298.65€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.211 > 0.08 con n=570 PNL=+305.82€
  - _Datos_: n=570 IC=+0.211 PNL=+305.82€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.230 < -0.1 con n=2117 PNL=-176.85€
  - _Datos_: n=2117 IC=-0.230 PNL=-176.85€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=6245 IC=+0.181 PNL=+4383.98€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=6245 IC=+0.181 PNL=+4383.98€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.093 > 0.08 con n=84 PNL=+27.18€
  - _Datos_: n=84 IC=+0.093 PNL=+27.18€

**〰️ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: n=2257 IC=+0.069 PNL=+688.92€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2257 IC=+0.069 PNL=+688.92€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.181 > 0.08 con n=2061 PNL=+1463.37€
  - _Datos_: n=2061 IC=+0.181 PNL=+1463.37€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=3436 IC=-0.032 PNL=+885.86€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3436 IC=-0.032 PNL=+885.86€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=592 PNL=-47.51€
  - _Datos_: n=592 IC=+0.087 PNL=-47.51€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.238 > 0.08 con n=3677 PNL=-319.29€
  - _Datos_: n=3677 IC=+0.238 PNL=-319.29€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=44 IC=+0.000 PNL=+5.87€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=44 IC=+0.000 PNL=+5.87€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.100 n=1227) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1227 IC=+0.100 PNL=+283.89€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.329 > 0.08 con n=313 PNL=+106.97€
  - _Datos_: n=313 IC=+0.329 PNL=+106.97€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.409 n=461) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=461 IC=+0.409 PNL=+649.06€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=10055 IC=+0.179 PNL=-1125.66€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=10055 IC=+0.179 PNL=-1125.66€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.206 > 0.1 con n=158 PNL=+97.19€
  - _Datos_: n=158 IC=+0.206 PNL=+97.19€
