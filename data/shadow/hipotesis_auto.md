# Hipótesis automáticas — 2026-10-23 00:05 UTC
_Generado por shadow_postmortem.py sobre 1014762 resoluciones (PNL=+132802.62€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=630)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.229 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.134)

- **PATRÓN** `n_total_lado` > `65.0` → IC=+0.182 (n=287)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 65.0 (IC base=+0.134)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.264 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.134)

- **PATRÓN** `banda_z` > `9.03` → IC=+0.210 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.03 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.135 (n=417)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 8.0 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=938)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.134)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.225 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `69.0` → IC=+0.202 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 69.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.6161` → IC=+0.254 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6161 (IC base=+0.139)

- **PATRÓN** `banda_z` > `9.489` → IC=+0.202 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.489 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=263)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=839)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.145 (n=443)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 100.0 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `9753.7972` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 9753.7972 (IC base=+0.017)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.239 (n=109)

- **FILTRO** `banda_hit_calibrado` < `0.8028` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8028
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=117)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=108)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=107)

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.239 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.130)

- **PATRÓN** `banda_hit_calibrado` > `0.8028` → IC=+0.258 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8028 (IC base=+0.130)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.135 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 4.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.140 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 14.0 (IC base=+0.130)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=117)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `911.0736` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 911.0736 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.130)

### BALLENAS_CONFIRMADAS_15M#XRP#15min
- **PATRÓN** `n_ballena_banda` > `30.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 30.0 (IC base=+0.149)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.149)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.149)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.719` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ballenas_wallet_edge_medio` > 0.719 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2466.3517` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2466.3517 (IC base=+0.149)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `142.15` → IC=-0.198 (n=10280)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.15
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=30842)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.58` → IC=-0.256 (n=1133)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.58
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3400)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.6` → IC=-0.286 (n=1105)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.6
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3315)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.54` → IC=-0.201 (n=2725)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.54
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8178)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.39` → IC=-0.276 (n=1997)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.39
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=5993)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=22283)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=4406)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `9018.9507` → IC=+0.172 (n=2003)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 9018.9507 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=19114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=34040)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=17788)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=7312)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7028.0416` → IC=+0.157 (n=2826)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7028.0416 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=2053)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=2513)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `16416.4017` → IC=+0.197 (n=652)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 16416.4017 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.189 (n=1802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 7.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=2005)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.285` → IC=+0.317 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.285 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=2572)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `16193.8223` → IC=+0.192 (n=663)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 16193.8223 (IC base=+0.183)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.172 (n=480)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `6771.7305` → IC=+0.156 (n=126)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 6771.7305 (IC base=+0.081)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1149)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=4333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.161 (n=3665)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.372 (n=1427)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.216 (n=1928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.349 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1092)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=929)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.265 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=855)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2210.9325` → IC=+0.157 (n=473)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2210.9325 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.256 (n=861)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=685)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.147)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=863)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.147)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.142 (n=336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 9.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.347 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=211)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `1309.2371` → IC=+0.130 (n=244)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 1309.2371 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=1137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.245 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=149)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.293 (n=138)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=73)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=18925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=15995)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.236 (n=7753)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.183 (n=4117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.182 (n=4328)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.183 (n=4268)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=3550)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.222 (n=2274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.225 (n=2378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.304 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.221)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=4284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.181 (n=4453)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=3344)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.361 (n=1202)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.248)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.195 (n=4193)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=3572)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=3093)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.190)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.432 (n=808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4237.012` → IC=+0.436 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4237.012 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.431 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.441 (n=219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `15539.3062` → IC=+0.433 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15539.3062 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.451 (n=223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.433)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.436 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.433)

- **PATRÓN** `libro_liquidez` > `3610.6662` → IC=+0.443 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3610.6662 (IC base=+0.433)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.428 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.400)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.77` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.77
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=21205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=24747)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=3663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=7813)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=11025)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=5004)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=3580)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.195 (n=3632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.212 (n=5590)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.232 (n=3458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=3915)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.276 (n=3487)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=9437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3645)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=4099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=4085)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4281)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=8941)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=8792)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.74` → IC=+0.136 (n=10718)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.74 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=4427)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=4501)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.130 (n=4686)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.73` → IC=+0.145 (n=4041)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.73 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=4514)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=4777)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.32` → IC=+0.134 (n=5387)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 3.32 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.311 (n=1149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.288 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.280)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.280)

- **PATRÓN** `libro_liquidez` > `5060.4398` → IC=+0.286 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5060.4398 (IC base=+0.280)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.323 (n=551)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=804)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `2114.2422` → IC=+0.312 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2114.2422 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.349 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.347)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.372 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.347)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.383 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.347)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.347)

- **PATRÓN** `libro_liquidez` > `763.8012` → IC=+0.369 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 763.8012 (IC base=+0.347)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.443 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.442)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.437 (n=253)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.440 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `5376.2936` → IC=+0.443 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5376.2936 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.469 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.450)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.453 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.450)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.452 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.450)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.451 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.450)

- **PATRÓN** `libro_liquidez` > `1981.0007` → IC=+0.468 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1981.0007 (IC base=+0.450)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.389 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.398)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.393 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.398)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.398)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=96)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.280 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=60)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.302 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.379 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.272 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `987.2299` → IC=+0.270 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 987.2299 (IC base=+0.255)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=96)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.280 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=60)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.302 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.255)

- **PATRÓN** `py_entrada` > `0.86` → IC=+0.379 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.86 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.272 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `987.2299` → IC=+0.270 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 987.2299 (IC base=+0.255)

### GBM_LATE_15M
- **PATRÓN** `drift_60min` |x|≤ `0.4745` → IC=+0.139 (n=13791)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4745 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=13971)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3778` → IC=+0.166 (n=13792)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3778 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8048` → IC=+0.272 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8048 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.888` → IC=+0.191 (n=5216)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.888 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6175` → IC=+0.266 (n=4016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6175 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3025` → IC=+0.242 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3025 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3476` → IC=+0.229 (n=4452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3476 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=11481)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.5678` → IC=+0.142 (n=17003)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5678 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.6237` → IC=+0.186 (n=1126)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6237 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` < `0.6954` → IC=+0.189 (n=2931)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6954 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.0502` → IC=+0.185 (n=3019)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.0502 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.231 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `2.683` → IC=+0.208 (n=3776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.683 (IC base=+0.076)

- **PATRÓN** `ballena_activa_n` < `107.0` → IC=+0.222 (n=11191)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 107.0 (IC base=+0.076)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.206 (n=1010)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.3463` → IC=+0.205 (n=2994)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3463 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=1463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.205 (n=1999)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.9825` → IC=+0.280 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9825 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.818` → IC=+0.284 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.818 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.2346` → IC=+0.253 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2346 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `1.4401` → IC=+0.203 (n=2857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4401 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=3230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2070.8688` → IC=+0.209 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2070.8688 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.217 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.241 (n=2519)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.240 (n=1147)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.273 (n=843)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=927)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5341` → IC=+0.257 (n=2518)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5341 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0948` → IC=+0.241 (n=2258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0948 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.259 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.242 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.691` → IC=+0.243 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.691 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=2849)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1499.4991` → IC=+0.244 (n=2518)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1499.4991 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.239 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.241 (n=1082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.232 (n=1115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.260 (n=1082)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=2581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9472` → IC=+0.280 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9472 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.1326` → IC=+0.236 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1326 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.325` → IC=+0.268 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.325 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` < `1.2306` → IC=+0.230 (n=2458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2306 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.233 (n=2459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2778` → IC=+0.271 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2778 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.4399` → IC=+0.258 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4399 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.153 (n=2534)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0058 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.171 (n=844)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.7248` → IC=+0.178 (n=2531)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7248 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.063` → IC=+0.151 (n=408)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.063 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.176` → IC=+0.144 (n=2307)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.176 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.142 (n=2531)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2032 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.0954` → IC=+0.161 (n=923)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0954 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `2.4531` → IC=+0.146 (n=2411)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4531 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `1.7906` → IC=+0.138 (n=1607)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.7906 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `215.0` → IC=+0.177 (n=1032)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 215.0 (IC base=+0.135)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.222 (n=1039)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=3275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=2783)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.224` → IC=+0.271 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.224 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.201 (n=2763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.212 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.5927` → IC=+0.199 (n=3025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5927 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.201 (n=3739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `1961.66` → IC=+0.201 (n=1413)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.66 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.221 (n=2471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1778` → IC=+0.233 (n=1236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1778 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1062)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.218 (n=985)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0229` → IC=+0.275 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0229 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.321` → IC=+0.257 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.321 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3477` → IC=+0.258 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3477 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7295` → IC=+0.213 (n=1175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7295 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.73` → IC=+0.229 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.73 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1947.5084` → IC=+0.221 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1947.5084 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.222 (n=2311)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=154)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=3776)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.164 (n=555)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0037 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.9538` → IC=+0.231 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9538 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1424` → IC=+0.334 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1424 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.1966` → IC=+0.329 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1966 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.13` → IC=+0.192 (n=1193)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.13 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.8578` → IC=+0.333 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8578 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `1.2247` → IC=+0.353 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2247 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` < `0.1664` → IC=+0.329 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1664 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.2985` → IC=+0.345 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2985 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.4107` → IC=+0.354 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4107 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `131.0` → IC=+0.336 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 131.0 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.093` → IC=+0.179 (n=983)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.093 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` > `0.5379` → IC=+0.151 (n=310)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.5379 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` < `0.1347` → IC=+0.141 (n=1628)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1347 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.8409` → IC=+0.149 (n=1173)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8409 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` > `1.1689` → IC=+0.143 (n=586)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` > 1.1689 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.200 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.7775` → IC=+0.141 (n=1125)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.7775 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.156` → IC=+0.154 (n=765)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.156 (IC base=+0.038)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.176 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=578)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.182 (n=171)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=513)

- **FILTRO** `ibs_20min` > `0.2143` → IC=-0.131 (n=3696)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2143
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=1821)

- **FILTRO** `sigma_ewma_delta_pct` > `8.637` → IC=-0.235 (n=579)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.637
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4938)

- **PATRÓN** `ibs_20min` > `0.7812` → IC=+0.185 (n=233)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.7812 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0156` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0156 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.4916` → IC=+0.267 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4916 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.141 (n=240)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `1.0233` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0233 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.280 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.5444` → IC=+0.292 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5444 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.272 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.270 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.2143` → IC=+0.147 (n=1821)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2143 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2769` → IC=+0.278 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2769 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6968` → IC=+0.301 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6968 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.296 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4341` → IC=+0.300 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4341 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6093` → IC=-0.182 (n=1018)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6093
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=3056)

- **FILTRO** `ibs_20min` < `0.7585` → IC=-0.151 (n=2688)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7585
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=1386)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.161 (n=976)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3098)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.204 (n=1450)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=4391)

- **PATRÓN** `dist_vwap_pct` > `1.1457` → IC=+0.343 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1457 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.258` → IC=+0.305 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.258 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` > `0.6988` → IC=+0.317 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6988 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.303 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.304 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.4138` → IC=+0.321 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4138 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` > `1.8376` → IC=+0.311 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8376 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.8374` → IC=+0.286 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8374 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` < `0.7172` → IC=+0.260 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7172 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `1.066` → IC=+0.287 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.066 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.288 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.1851` → IC=+0.264 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1851 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.267 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4309 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.209 (n=6043)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.3169` → IC=+0.168 (n=18100)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3169 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.9762` → IC=+0.303 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9762 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.587` → IC=+0.163 (n=8115)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.587 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `1.1692` → IC=+0.265 (n=6661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1692 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `0.6881` → IC=+0.271 (n=5952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6881 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.278 (n=1991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.4599` → IC=+0.263 (n=3542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4599 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `2.6456` → IC=+0.272 (n=3541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6456 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.297 (n=10221)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.095)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.156 (n=5822)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0093 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.6561` → IC=+0.145 (n=17446)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.6561 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7045` → IC=+0.266 (n=2432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7045 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1959` → IC=+0.267 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1959 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.317 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.293 (n=2658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2668` → IC=+0.285 (n=3615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2668 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.296 (n=7897)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5792` → IC=-0.135 (n=2482)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5792
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=2483)

- **FILTRO** `ibs_20min` > `0.7367` → IC=-0.216 (n=1052)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7367
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=3159)

- **FILTRO** `sigma_ewma_delta_pct` > `4.347` → IC=-0.211 (n=918)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.347
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=3293)

- **PATRÓN** `ibs_20min` > `0.9205` → IC=+0.317 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9205 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.959` → IC=+0.217 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.959 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2299` → IC=+0.304 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2299 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.251 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.2584` → IC=+0.278 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2584 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.285 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.028)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.161 (n=1056)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1667 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0743` → IC=+0.415 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0743 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.6293` → IC=+0.406 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6293 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.403 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1177` → IC=+0.219 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1177 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1944` → IC=+0.196 (n=1764)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 1.1944 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.6835` → IC=+0.203 (n=1576)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6835 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.0748` → IC=+0.194 (n=1618)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0748 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.2762` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2762 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `1.425` → IC=+0.218 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.425 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `2.4876` → IC=+0.197 (n=579)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.4876 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `272.0` → IC=+0.231 (n=1155)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 272.0 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1702` → IC=+0.231 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1702 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.236 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6206 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.1578` → IC=+0.234 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1578 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.301 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.242 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1598` → IC=+0.254 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1598 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `199.0` → IC=+0.247 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 199.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.311 (n=876)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.277 (n=2762)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.310 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.268)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.681` → IC=+0.301 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.681 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` < `0.1318` → IC=+0.281 (n=2426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1318 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.274 (n=2542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.279 (n=3133)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `2047.0084` → IC=+0.287 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2047.0084 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.287 (n=1565)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.324 (n=1040)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1806` → IC=+0.310 (n=1010)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1806 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=878)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.292 (n=802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` < `0.3712` → IC=+0.295 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3712 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.2632` → IC=+0.298 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2632 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.468` → IC=+0.305 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.468 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` < `0.1968` → IC=+0.291 (n=2244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1968 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.3404` → IC=+0.303 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3404 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `1.7251` → IC=+0.299 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7251 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.6582` → IC=+0.302 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6582 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.294 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1942.5784` → IC=+0.305 (n=1040)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1942.5784 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.293 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.292)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.736` → IC=-0.188 (n=1099)

  - _Acción_: SKIP cuando `ibs_20min` > 0.736
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=3299)

- **PATRÓN** `ibs_20min` > `0.8747` → IC=+0.169 (n=1051)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8747 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.1581` → IC=+0.232 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1581 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.3726` → IC=+0.232 (n=1449)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3726 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` < `1.0078` → IC=+0.240 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0078 (IC base=+0.028)

- **PATRÓN** `volumen_regimen` > `0.667` → IC=+0.231 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.667 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.1635` → IC=+0.235 (n=1567)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1635 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.1023` → IC=+0.245 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1023 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.4348` → IC=+0.239 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4348 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.256 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 122.0 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.1411` → IC=+0.237 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1411 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.0289` → IC=+0.244 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0289 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.1022` → IC=+0.252 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1022 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.288 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.276 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7982 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.4393` → IC=+0.256 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4393 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.269 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 109.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7586` → IC=-0.218 (n=1906)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7586
  - _Potencial_: sin este filtro IC_bueno=+0.307 (n=1906)

- **FILTRO** `ibs_20min` > `0.6452` → IC=-0.234 (n=927)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6452
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=2787)

- **FILTRO** `sigma_ewma_delta_pct` > `8.468` → IC=-0.245 (n=430)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.468
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=3284)

- **PATRÓN** `ibs_20min` > `0.7586` → IC=+0.307 (n=1906)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7586 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.2166` → IC=+0.338 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2166 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.469` → IC=+0.186 (n=593)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.469 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` < `0.8456` → IC=+0.334 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8456 (IC base=+0.045)

- **PATRÓN** `volumen_regimen` > `0.7014` → IC=+0.328 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7014 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` < `0.1593` → IC=+0.324 (n=1471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1593 (IC base=+0.045)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.353 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.045)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.347 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.045)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.341 (n=1221)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.045)

- **PATRÓN** `ibs_20min` < `0.6452` → IC=+0.122 (n=2787)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6452 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.7017` → IC=+0.264 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7017 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.1018` → IC=+0.245 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1018 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.0777` → IC=+0.256 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0777 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.43` → IC=+0.252 (n=1197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.43 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.270 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.033)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.349 (n=1780)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.306)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.310 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.306)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.315 (n=943)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.306)

- **PATRÓN** `ibs_20min` > `0.6604` → IC=+0.338 (n=1992)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6604 (IC base=+0.306)

- **PATRÓN** `dist_vwap_pct` > `0.2113` → IC=+0.331 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2113 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.809` → IC=+0.325 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.809 (IC base=+0.306)

- **PATRÓN** `volumen_regimen` > `0.6276` → IC=+0.314 (n=1992)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6276 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.347 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` > `1.8015` → IC=+0.322 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8015 (IC base=+0.306)

- **PATRÓN** `libro_liquidez` > `2615.934` → IC=+0.311 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.934 (IC base=+0.306)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.340 (n=1720)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.306)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.337 (n=1408)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.306)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.317 (n=822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.306)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.307 (n=1032)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.306)

- **PATRÓN** `ibs_20min` < `0.3684` → IC=+0.329 (n=2113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3684 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.613` → IC=+0.318 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.613 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.086` → IC=+0.307 (n=2511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.086 (IC base=+0.306)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.312 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.306)

- **PATRÓN** `volumen_regimen` > `1.224` → IC=+0.334 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.224 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.356 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.316 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` > `2.1353` → IC=+0.308 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1353 (IC base=+0.306)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.226 (n=4451)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.0869` → IC=+0.202 (n=4451)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0869 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=13872)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.5573` → IC=+0.235 (n=13336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5573 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1674` → IC=+0.209 (n=5358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1674 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.341` → IC=+0.257 (n=3496)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.341 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1861` → IC=+0.167 (n=8851)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1861 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.6229` → IC=+0.164 (n=8850)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6229 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2927` → IC=+0.205 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2927 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6089` → IC=+0.192 (n=4313)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6089 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `1968.1` → IC=+0.181 (n=11914)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1968.1 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.198 (n=12267)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 94.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.185 (n=11337)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0092 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.229 (n=4290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=4822)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5027` → IC=+0.237 (n=12869)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5027 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.967` → IC=+0.197 (n=2099)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.967 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.669` → IC=+0.183 (n=11371)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.669 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.165 (n=9174)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1823 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.224 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.64` → IC=+0.187 (n=4036)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.64 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.194 (n=11840)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 99.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.233 (n=747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.3313` → IC=+0.234 (n=2234)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3313 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.229 (n=839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.223 (n=1501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` > `0.9291` → IC=+0.294 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9291 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.899` → IC=+0.327 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.899 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.276 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.8412` → IC=+0.211 (n=1412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8412 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.217 (n=2117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.229 (n=2432)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.217)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.253 (n=1744)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.264 (n=791)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.251)

- **PATRÓN** `drift_60min` |x|≤ `0.0659` → IC=+0.310 (n=581)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0659 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=1790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.252 (n=838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` < `0.022` → IC=+0.298 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.022 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.255 (n=1518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` > `0.298` → IC=+0.287 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.298 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` < `1.437` → IC=+0.272 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.437 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.7246` → IC=+0.256 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7246 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `1475.9048` → IC=+0.258 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1475.9048 (IC base=+0.251)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.251 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.251)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.220 (n=673)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1592` → IC=+0.181 (n=1342)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1592 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=2122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.3296` → IC=+0.222 (n=2013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3296 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1382` → IC=+0.215 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1382 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.256` → IC=+0.222 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.256 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.6901` → IC=+0.162 (n=886)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6901 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `1.0617` → IC=+0.152 (n=913)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 1.0617 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.191 (n=322)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4131` → IC=+0.173 (n=658)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.4131 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.4963` → IC=+0.168 (n=658)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.4963 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `419.0` → IC=+0.156 (n=1939)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 419.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.173 (n=2110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0059 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2361` → IC=+0.174 (n=1856)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2361 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.188 (n=1009)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6155` → IC=+0.208 (n=2110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6155 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.492` → IC=+0.193 (n=399)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.492 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.207` → IC=+0.148 (n=1830)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.207 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.162 (n=2111)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.204 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.151 (n=1798)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4922` → IC=+0.156 (n=1990)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4922 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `225.0` → IC=+0.181 (n=845)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 225.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.243 (n=752)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3954` → IC=+0.223 (n=1983)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3954 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=831)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.414` → IC=+0.301 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.414 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0992` → IC=+0.215 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0992 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.228 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.7658` → IC=+0.213 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7658 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.7073` → IC=+0.227 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7073 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=2699)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1952.3598` → IC=+0.226 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1952.3598 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.244 (n=1720)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.2488` → IC=+0.264 (n=1303)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2488 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0119` → IC=+0.302 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0119 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.409` → IC=+0.273 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.409 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3579` → IC=+0.279 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3579 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7474` → IC=+0.237 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7474 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.237 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2034.1068` → IC=+0.243 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2034.1068 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.234 (n=1234)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.207 (n=955)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0767` → IC=+0.199 (n=722)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0767 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=2249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.3068` → IC=+0.212 (n=2164)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3068 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.148` → IC=+0.196 (n=1311)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.148 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.676` → IC=+0.206 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.676 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.8475` → IC=+0.157 (n=1443)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8475 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` > `0.6162` → IC=+0.148 (n=2165)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.6162 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.174 (n=888)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.8198` → IC=+0.149 (n=1415)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.8198 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` > `2.5053` → IC=+0.164 (n=707)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5053 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `4545.4038` → IC=+0.180 (n=1443)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 4545.4038 (IC base=+0.147)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.155 (n=2100)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 137.0 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.157 (n=2286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3949` → IC=+0.144 (n=2285)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3949 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6818` → IC=+0.186 (n=2285)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6818 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1588` → IC=+0.155 (n=2289)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1588 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.793` → IC=+0.151 (n=805)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.793 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8557` → IC=+0.155 (n=1524)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8557 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.3001` → IC=+0.194 (n=348)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.3001 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8098` → IC=+0.135 (n=1429)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8098 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.554` → IC=+0.135 (n=715)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.554 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7290.0547` → IC=+0.191 (n=1036)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7290.0547 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.150 (n=923)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 66.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.178 (n=1102)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0104 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.171 (n=1164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4872` → IC=+0.218 (n=2431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4872 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1998` → IC=+0.193 (n=1401)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1998 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.512` → IC=+0.283 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.512 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.142 (n=2431)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1753 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.1609` → IC=+0.133 (n=2465)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1609 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.5436` → IC=+0.144 (n=1038)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5436 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2549)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2747.518` → IC=+0.209 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2747.518 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.156 (n=762)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 19.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.142 (n=2495)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0109 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1081` → IC=+0.175 (n=833)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.1081 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=2548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6061` → IC=+0.222 (n=2495)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6061 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.807` → IC=+0.124 (n=381)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 8.807 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.461` → IC=+0.135 (n=2205)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.461 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1786` → IC=+0.132 (n=2494)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1786 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.8636` → IC=+0.124 (n=1663)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.8636 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1651` → IC=+0.127 (n=2419)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1651 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2767` → IC=+0.144 (n=338)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2767 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4448` → IC=+0.132 (n=776)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4448 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.4306` → IC=+0.136 (n=776)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4306 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2625.2681` → IC=+0.189 (n=1131)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2625.2681 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.130 (n=2009)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 41.0 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.245 (n=2005)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1724` → IC=+0.241 (n=988)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1724 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2014)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.259 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `1.2777` → IC=+0.233 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2777 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.618` → IC=+0.251 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.618 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.1767` → IC=+0.225 (n=2244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1767 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.619` → IC=+0.232 (n=2244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.619 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.269 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.4689` → IC=+0.228 (n=2185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4689 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8092` → IC=+0.233 (n=1456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8092 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2587.257` → IC=+0.225 (n=1496)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2587.257 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.233 (n=1006)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.243 (n=1036)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.266 (n=763)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=1120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.4271` → IC=+0.258 (n=2286)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4271 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.3025` → IC=+0.243 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3025 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.3` → IC=+0.264 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.3 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `0.8684` → IC=+0.232 (n=1524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8684 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `0.6376` → IC=+0.237 (n=2286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6376 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.284 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.234 (n=2129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.231)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.209 (n=1498)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.192 (n=1137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0089 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.1295` → IC=+0.203 (n=1499)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1295 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=3418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.4901` → IC=+0.219 (n=3041)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4901 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.8089` → IC=+0.203 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8089 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.617` → IC=+0.214 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.617 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.8627` → IC=+0.206 (n=2042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8627 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.187 (n=2736)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6949 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0998` → IC=+0.194 (n=1219)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0998 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.4279` → IC=+0.196 (n=1104)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4279 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.4846` → IC=+0.187 (n=1103)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4846 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3849)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2672.5659` → IC=+0.190 (n=3041)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2672.5659 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.131 (n=1232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0038 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.7191` → IC=+0.122 (n=3694)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.7191 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.125 (n=1589)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 27.0 (IC base=+0.086)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.209 (n=414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0985` → IC=+0.236 (n=414)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0985 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=858)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.239 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6364 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.202 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.079` → IC=+0.199 (n=403)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 3.079 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.041` → IC=+0.182 (n=904)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 4.041 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.8739` → IC=+0.207 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8739 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.186 (n=371)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `2.1976` → IC=+0.191 (n=810)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.1976 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `14663.1359` → IC=+0.185 (n=627)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14663.1359 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.210 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.134 (n=1125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0057 (IC base=+0.109)

- **PATRÓN** `drift_60min` |x|≤ `0.2654` → IC=+0.131 (n=991)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.2654 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.121 (n=1020)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 7.0 (IC base=+0.109)

- **PATRÓN** `ibs_20min` < `0.6339` → IC=+0.159 (n=990)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.6339 (IC base=+0.109)

- **PATRÓN** `volumen_pendiente_norm` > `0.1607` → IC=+0.160 (n=298)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1607 (IC base=+0.109)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.156 (n=731)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 223.0 (IC base=+0.109)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.249 (n=706)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.2096` → IC=+0.226 (n=703)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2096 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=1105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.3792` → IC=+0.254 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3792 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.8171` → IC=+0.213 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8171 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.218` → IC=+0.219 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.218 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.869` → IC=+0.243 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.869 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.8389` → IC=+0.224 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8389 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.217 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1643 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.2665` → IC=+0.255 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2665 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.231 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.7736` → IC=+0.220 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7736 (IC base=+0.211)

- **PATRÓN** `ibs_20min` < `0.1053` → IC=+0.162 (n=356)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1053 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `5709.6016` → IC=+0.130 (n=711)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 5709.6016 (IC base=+0.064)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.199 (n=284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.5286` → IC=+0.171 (n=852)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.5286 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.200 (n=761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.276 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.9868` → IC=+0.245 (n=155)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9868 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.092` → IC=+0.241 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.092 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.0562` → IC=+0.185 (n=751)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.0562 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.7105` → IC=+0.179 (n=761)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.7105 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1612` → IC=+0.192 (n=235)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1612 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.192 (n=274)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.1591` → IC=+0.171 (n=372)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1591 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.179 (n=883)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `3017.7122` → IC=+0.189 (n=284)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 3017.7122 (IC base=+0.170)

- **PATRÓN** `ibs_20min` < `0.5581` → IC=+0.132 (n=824)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5581 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `2663.6465` → IC=+0.150 (n=424)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2663.6465 (IC base=+0.054)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0239` → IC=+0.161 (n=219)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0239 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0144` → IC=+0.203 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0144 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2536` → IC=+0.176 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2536 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 16.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.207 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.56 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.2021` → IC=+0.167 (n=115)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2021 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.738` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 7.738 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.275` → IC=+0.182 (n=187)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.275 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` > `0.6893` → IC=+0.165 (n=195)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6893 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.1109` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1109 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.216 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.5669` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.5669 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.177 (n=255)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.03 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `2474.2976` → IC=+0.176 (n=146)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2474.2976 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.146 (n=227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0125 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.614` → IC=+0.128 (n=253)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.614 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.9016` → IC=+0.134 (n=170)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.9016 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` > `2.3609` → IC=+0.127 (n=108)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.3609 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.130 (n=233)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 19.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.229 (n=5800)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=18159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.4453` → IC=+0.232 (n=17397)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4453 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.9198` → IC=+0.216 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9198 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.221` → IC=+0.255 (n=4255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.221 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `1.2204` → IC=+0.170 (n=11665)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2204 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.2406` → IC=+0.205 (n=3148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2406 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.6131` → IC=+0.196 (n=5648)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6131 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `1958.3448` → IC=+0.185 (n=15542)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1958.3448 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.209 (n=14139)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.196 (n=6986)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0056 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.4894` → IC=+0.193 (n=15817)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.4894 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5915)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.5841` → IC=+0.243 (n=15817)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5841 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.786` → IC=+0.206 (n=2197)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.786 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.546` → IC=+0.192 (n=15314)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 3.546 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.6322` → IC=+0.166 (n=3556)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6322 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.252 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.6209` → IC=+0.199 (n=4994)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6209 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.235 (n=4955)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.189)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.228 (n=955)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.347` → IC=+0.230 (n=2836)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.347 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=1383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1902)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.387` → IC=+0.355 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.387 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.286 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.2926` → IC=+0.239 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2926 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.244 (n=3045)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2070.3` → IC=+0.231 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2070.3 (IC base=+0.227)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.251 (n=1670)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.267 (n=2427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.263)

- **PATRÓN** `drift_60min` |x|≤ `0.1182` → IC=+0.285 (n=1067)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1182 (IC base=+0.263)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=2228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` < `0.5142` → IC=+0.288 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5142 (IC base=+0.263)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.09` → IC=+0.266 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.09 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` < `0.0956` → IC=+0.265 (n=2177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0956 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` > `0.288` → IC=+0.285 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.288 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` < `1.5583` → IC=+0.265 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5583 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` > `2.6462` → IC=+0.272 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6462 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2749)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `1497.8186` → IC=+0.269 (n=2424)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1497.8186 (IC base=+0.263)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.273 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.263)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.200 (n=942)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.166 (n=1242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2946)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3643` → IC=+0.222 (n=2519)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3643 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1298` → IC=+0.196 (n=1444)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1298 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.562` → IC=+0.163 (n=597)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.562 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.169` → IC=+0.152 (n=2596)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 4.169 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.63` → IC=+0.175 (n=940)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.63 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0726` → IC=+0.153 (n=2517)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0726 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.182 (n=404)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.173` → IC=+0.158 (n=2428)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.173 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5314` → IC=+0.155 (n=2465)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5314 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `238.0` → IC=+0.186 (n=900)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 238.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.166 (n=2372)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0779` → IC=+0.189 (n=791)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0779 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=889)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6942` → IC=+0.198 (n=2372)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6942 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.229` → IC=+0.157 (n=392)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.229 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.461` → IC=+0.146 (n=2389)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.461 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.1895` → IC=+0.155 (n=2371)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1895 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2175` → IC=+0.202 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2175 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.152 (n=2266)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.7807` → IC=+0.156 (n=1511)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7807 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=3078)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `272.0` → IC=+0.160 (n=961)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 272.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.259 (n=968)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0124 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2588)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.325 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.231 (n=2717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.6215` → IC=+0.231 (n=2817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6215 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=3469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1961.3384` → IC=+0.237 (n=1314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1961.3384 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.245 (n=2402)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.261 (n=1201)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.242 (n=963)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0347` → IC=+0.308 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0347 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.549` → IC=+0.299 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.549 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3456` → IC=+0.303 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3456 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1351` → IC=+0.250 (n=1733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1351 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.245 (n=1431)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1941.6632` → IC=+0.251 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1941.6632 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.258 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.204 (n=1005)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4224` → IC=+0.159 (n=2992)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4224 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=3109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.193 (n=2991)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2458 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1465` → IC=+0.172 (n=1582)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1465 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.122` → IC=+0.162 (n=1215)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.122 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8639` → IC=+0.165 (n=1995)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8639 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.186 (n=393)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5219` → IC=+0.163 (n=1285)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5219 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1716` → IC=+0.154 (n=1324)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 2.1716 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `5823.4379` → IC=+0.240 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5823.4379 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.169 (n=1274)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 73.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.153 (n=2492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0075 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4369` → IC=+0.140 (n=2492)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4369 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.7348` → IC=+0.186 (n=2492)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7348 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1525` → IC=+0.145 (n=2279)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1525 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.138` → IC=+0.168 (n=380)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.138 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.163` → IC=+0.132 (n=2170)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.163 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.146 (n=1097)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6961 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2975` → IC=+0.219 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2975 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4287` → IC=+0.137 (n=2397)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4287 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6977.262` → IC=+0.213 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6977.262 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.132 (n=1615)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 100.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.164 (n=1370)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0103 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=1117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.44` → IC=+0.201 (n=3020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.44 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0619` → IC=+0.207 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0619 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.657` → IC=+0.262 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.657 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2211` → IC=+0.135 (n=3016)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2211 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1622` → IC=+0.125 (n=3139)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1622 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.128 (n=388)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.4811` → IC=+0.126 (n=2947)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.4811 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `2.1879` → IC=+0.127 (n=1336)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.1879 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=3144)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2476.871` → IC=+0.229 (n=1367)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2476.871 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.141 (n=981)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 24.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.154 (n=2516)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.01 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1345` → IC=+0.154 (n=955)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1345 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=2955)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.65` → IC=+0.213 (n=2863)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.65 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.218` → IC=+0.137 (n=2753)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.218 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6411` → IC=+0.143 (n=954)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6411 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2246` → IC=+0.169 (n=490)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2246 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4386` → IC=+0.151 (n=894)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4386 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2652.1888` → IC=+0.206 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2652.1888 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.133 (n=2384)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 47.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.253 (n=2537)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=2970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.236 (n=2542)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.6106` → IC=+0.273 (n=2537)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6106 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.1942` → IC=+0.248 (n=1536)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1942 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.721` → IC=+0.274 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.721 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `1.2283` → IC=+0.240 (n=2840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2283 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.7067` → IC=+0.237 (n=2537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7067 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.260 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `1.5476` → IC=+0.241 (n=2471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5476 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2953.2954` → IC=+0.237 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2953.2954 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.255 (n=981)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.232)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.239 (n=2776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.232)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.266 (n=2944)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.232)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.201` → IC=+0.269 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.201 (IC base=+0.232)

- **PATRÓN** `volumen_regimen` > `1.2282` → IC=+0.261 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2282 (IC base=+0.232)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.297 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.232)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.234 (n=2739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.232)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=5053)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.244 (n=1743)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.5106` → IC=+0.220 (n=5218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5106 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=1894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.252 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.1724` → IC=+0.213 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1724 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.4361` → IC=+0.214 (n=3721)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4361 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.969` → IC=+0.221 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.969 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.585` → IC=+0.212 (n=4646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.585 (IC base=+0.211)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.224 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` < `0.1068` → IC=+0.211 (n=4876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1068 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.1666` → IC=+0.222 (n=1468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1666 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.219 (n=1712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `1.8464` → IC=+0.211 (n=3424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8464 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.217 (n=3999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `3732.8792` → IC=+0.220 (n=3479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3732.8792 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.239 (n=1272)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.208 (n=3802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.209 (n=1690)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7337` → IC=+0.199 (n=3802)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7337 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6764` → IC=+0.201 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6764 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2413` → IC=+0.189 (n=3472)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2413 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.803` → IC=+0.202 (n=3415)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.803 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.095` → IC=+0.201 (n=3174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.095 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.197 (n=3492)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.195 (n=766)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.198 (n=1648)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.1921` → IC=+0.201 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1921 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=5053)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.209 (n=1647)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.193)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.275 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.260)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.260 (n=684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.294 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.260 (n=766)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.4896` → IC=+0.279 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4896 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.054` → IC=+0.274 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.054 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.268 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2151 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `0.8685` → IC=+0.273 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8685 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.350 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.8249` → IC=+0.267 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8249 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `16321.2566` → IC=+0.274 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16321.2566 (IC base=+0.260)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.253 (n=585)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3687` → IC=+0.191 (n=1327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3687 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.195 (n=486)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.205 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1382 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.177 (n=602)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6078 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.7054` → IC=+0.178 (n=116)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.7054 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.194 (n=1309)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.189 (n=1327)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.2212 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.199 (n=267)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.4032` → IC=+0.192 (n=440)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4032 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.1667` → IC=+0.187 (n=598)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.1667 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `14904.1418` → IC=+0.185 (n=602)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14904.1418 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `692.0` → IC=+0.187 (n=1281)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 692.0 (IC base=+0.175)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.196 (n=363)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.007 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.215 (n=373)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.204 (n=820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.7037` → IC=+0.196 (n=547)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.7037 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.239 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.492` → IC=+0.234 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.492 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2099` → IC=+0.238 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2099 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.8704` → IC=+0.205 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.8704 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2543.292` → IC=+0.219 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2543.292 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.197 (n=553)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 10.0 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.275 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.281 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.2121` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2121 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.442` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.442 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.214 (n=1381)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1485` → IC=+0.216 (n=608)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1485 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.519` → IC=+0.210 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.519 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.8779` → IC=+0.200 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8779 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.4078` → IC=+0.212 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4078 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.112` → IC=+0.207 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.112 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `0.8778` → IC=+0.202 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8778 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.204 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` < `0.105` → IC=+0.202 (n=1271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.105 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.206 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.199 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.204 (n=1132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.4933` → IC=+0.210 (n=1131)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4933 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.201 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.198 (n=755)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.3984` → IC=+0.193 (n=754)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3984 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `0.6238` → IC=+0.189 (n=513)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.6238 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.671` → IC=+0.197 (n=199)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.671 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.2254` → IC=+0.187 (n=1092)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2254 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.2445` → IC=+0.197 (n=1131)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.2445 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` > `0.721` → IC=+0.187 (n=1010)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.721 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.0741` → IC=+0.208 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0741 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `2.1885` → IC=+0.195 (n=974)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1885 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.7842` → IC=+0.189 (n=738)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.7842 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `6718.7638` → IC=+0.197 (n=1131)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6718.7638 (IC base=+0.186)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.011` → IC=+0.205 (n=683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.211 (n=743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.259 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.7483` → IC=+0.242 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7483 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.23` → IC=+0.205 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.23 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.7001` → IC=+0.230 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7001 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.196 (n=698)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0781` → IC=+0.195 (n=345)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.0781 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.5628` → IC=+0.194 (n=331)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.5628 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.4649` → IC=+0.211 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4649 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=905)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `4314.892` → IC=+0.224 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4314.892 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.199 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.216 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.211 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.6042` → IC=+0.229 (n=578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6042 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.245 (n=391)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.7304` → IC=+0.232 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7304 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.5153` → IC=+0.212 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5153 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.3069` → IC=+0.210 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3069 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.848` → IC=+0.217 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.848 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.1288` → IC=+0.211 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1288 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.9335` → IC=+0.210 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9335 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.227 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.242 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `3255.1743` → IC=+0.218 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3255.1743 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.252 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.208)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.154 (n=768)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.004 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.7818` → IC=+0.208 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7818 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.144 (n=853)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.919` → IC=+0.153 (n=477)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 8.919 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2759` → IC=+0.149 (n=229)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2759 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0263` → IC=+0.267 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0263 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.358` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 10.358 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.1459` → IC=+0.149 (n=266)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1459 (IC base=+0.055)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.132 (n=574)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0056 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.5136` → IC=+0.193 (n=486)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.5136 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.2965` → IC=+0.184 (n=185)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.2965 (IC base=+0.091)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.120 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0038 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.0602` → IC=+0.278 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0602 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.2123` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2123 (IC base=+0.067)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.124 (n=501)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.006 (IC base=+0.091)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.091)

- **PATRÓN** `ibs_20min` > `0.4203` → IC=+0.172 (n=538)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.4203 (IC base=+0.091)

- **PATRÓN** `dist_vwap_pct` > `0.1272` → IC=+0.192 (n=274)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1272 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.128` → IC=+0.242 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.128 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.2854` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2854 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.106` → IC=+0.250 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.106 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.022)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7391` → IC=+0.163 (n=378)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.7391 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.7402` → IC=+0.140 (n=137)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.7402 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.265` → IC=+0.153 (n=119)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 9.265 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2779` → IC=+0.142 (n=79)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2779 (IC base=+0.031)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.155 (n=253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0106 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.209 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1744` → IC=+0.140 (n=212)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1744 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.474` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.474 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.0779` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` > 1.0779 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.1499` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1499 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `2.18` → IC=+0.150 (n=175)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.18 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `1.4089` → IC=+0.157 (n=199)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.4089 (IC base=+0.074)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.143 (n=197)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.06 (IC base=+0.074)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.326 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=251)

- **FILTRO** `dist_vwap_pct` > `0.2334` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2334
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=301)

- **FILTRO** `volumen_regimen` < `0.7666` → IC=-0.315 (n=79)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7666
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=239)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.341 (n=67)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=204)

- **FILTRO** `dist_vwap_pct` > `0.4684` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4684
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=252)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=155)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `volumen_regimen` < `0.8402` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8402
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=74)

- **FILTRO** `volumen_spike_ratio` > `3.276` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.276
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=57)

- **FILTRO** `sigma_h` > `0.0042` → IC=-0.312 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=91)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=91)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0026` → IC=-0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0026
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=81)

- **FILTRO** `drift_60min` |x|> `0.149` → IC=-0.321 (n=26)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.149
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=81)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.352 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=78)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=81)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=88)

- **FILTRO** `libro_liquidez` < `1599.2889` → IC=-0.311 (n=51)

  - _Acción_: SKIP cuando `libro_liquidez` < 1599.2889
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=52)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 1.0 (IC base=-0.151)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=95)

- **FILTRO** `volumen_regimen` < `0.7468` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7468
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=85)

- **FILTRO** `sigma_h` < `0.006` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.294 (n=32)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **FILTRO** `dist_vwap_pct` < `0.2328` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2328
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=22)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1471` → IC=-0.120 (n=293)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1471
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=569)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.201 (n=185)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.193 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.6786` → IC=+0.155 (n=555)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.6786 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.7699` → IC=+0.253 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7699 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6172` → IC=+0.170 (n=186)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6172 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1517` → IC=+0.149 (n=462)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.1517 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4188` → IC=+0.180 (n=151)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4188 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.1471` → IC=+0.143 (n=569)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.1471 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.083` → IC=+0.175 (n=149)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 11.083 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `3253.1348` → IC=+0.131 (n=431)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3253.1348 (IC base=+0.053)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6946` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6946
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=170)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.189 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0049 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.135 (n=206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 12.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.158 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 6.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.1684` → IC=+0.192 (n=303)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1684 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.168` → IC=+0.160 (n=95)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 10.168 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.146 (n=303)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6182 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.139 (n=239)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.159 (n=271)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.5218` → IC=+0.147 (n=242)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5218 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `5391.3885` → IC=+0.147 (n=202)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 5391.3885 (IC base=+0.130)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1261` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1261
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=180)

- **FILTRO** `ibs_20min` > `0.3236` → IC=-0.171 (n=77)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3236
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=234)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.136 (n=127)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0039 (IC base=+0.102)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.102)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.143 (n=169)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.8015 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` < `0.0943` → IC=+0.134 (n=159)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.0943 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.146 (n=142)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.102)

- **PATRÓN** `volumen_regimen` < `0.6141` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6141 (IC base=+0.102)

- **PATRÓN** `volumen_pendiente_norm` < `0.1261` → IC=+0.148 (n=180)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` < 0.1261 (IC base=+0.102)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.102)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.018)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.25` → IC=-0.250 (n=50)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=98)

- **FILTRO** `dist_vwap_pct` > `0.1813` → IC=-0.158 (n=36)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1813
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=112)

- **FILTRO** `volumen_spike_ratio` > `2.3635` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3635
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=84)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.315 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.312 (n=131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `0.6364` → IC=+0.269 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6364 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.6973` → IC=+0.394 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6973 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.233` → IC=+0.325 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.233 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `0.778` → IC=+0.276 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.778 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.0991` → IC=+0.324 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0991 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.614` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.614 (IC base=-0.080)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.311 (n=72)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.321)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.391 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.321)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.321)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.391 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.321)

- **PATRÓN** `ballena_activa_n` < `1107.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1107.0 (IC base=+0.321)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3366` → IC=+0.254 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3366 (IC base=+0.225)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.225)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.225)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.287 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.287 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.225)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.225)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.225)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.311 (n=72)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.328 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.321)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.391 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.321)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.321)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.391 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.321)

- **PATRÓN** `ballena_activa_n` < `1107.0` → IC=+0.370 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1107.0 (IC base=+0.321)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3366` → IC=+0.254 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3366 (IC base=+0.225)

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.242 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.225)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.225)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.287 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.287 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.225)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.311 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.225)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.283 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.225)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2942.1423` → IC=+0.135 (n=431)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2942.1423 (IC base=+0.103)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2942.1423` → IC=+0.135 (n=431)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2942.1423 (IC base=+0.103)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=197)

- **FILTRO** `libro_liquidez` < `5350.5492` → IC=-0.167 (n=106)

  - _Acción_: SKIP cuando `libro_liquidez` < 5350.5492
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=107)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=370)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11939.3802` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 11939.3802
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=64)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=55)

- **PATRÓN** `liq_n` > `6.0` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `liq_n` > 6.0 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `309.0` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 309.0 (IC base=+0.019)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4006.09` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `liq_usd_total` < 4006.09
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **PATRÓN** `liq_n` > `5.0` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 5.0 (IC base=+0.044)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3592)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=106)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=106)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.133 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=131)

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

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=1354)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=1308)

- **FILTRO** `liq_usd_total` < `12056.79` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `liq_usd_total` < 12056.79
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.292 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=717)

- **FILTRO** `liq_n` < `11.0` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `liq_n` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `liq_usd_total` < `13082.51` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `liq_usd_total` < 13082.51
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M#XRP#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=422)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=403)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.145 (n=181)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=859)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=859)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=876)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=876)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=223)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=223)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.132 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=172)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=255)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=279)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=265)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=356)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=356)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=201)

- **FILTRO** `libro_liquidez` < `631.7738` → IC=-0.128 (n=127)

  - _Acción_: SKIP cuando `libro_liquidez` < 631.7738
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=259)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=267)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=195)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `profundidad_ratio` < `11.3` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `profundidad_ratio` < 11.3
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=61)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=38)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.125 (n=38)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.58 (IC base=+0.009)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=36)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=18)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.173 (n=163)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` < 0.46 (IC base=+0.016)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.151 (n=61)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=279)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.140 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=188)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` < 0.5 (IC base=+0.055)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.123 (n=343)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=188)

- **FILTRO** `profundidad_ratio` < `41.8` → IC=-0.172 (n=132)

  - _Acción_: SKIP cuando `profundidad_ratio` < 41.8
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=399)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.135 (n=209)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=238)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.163 (n=93)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=406)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.138 (n=136)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=498)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=6301)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=19265)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.176 (n=6329)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=19976)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.193 (n=1147)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3531)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.176 (n=1083)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3607)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.129 (n=3147)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` > 0.495 (IC base=+0.041)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.143 (n=1228)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `1222.0628` → IC=+0.135 (n=2339)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1222.0628 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.127 (n=2199)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.012)

- **PATRÓN** `libro_liquidez` > `1429.8648` → IC=+0.149 (n=1595)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1429.8648 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.154 (n=877)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=2839)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.178 (n=910)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=2823)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=1198)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=3598)

- **PATRÓN** `ibs_20min` > `0.9655` → IC=+0.131 (n=1588)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9655 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1508.4106` → IC=+0.121 (n=2335)

  - _Acción_: Kelly boost +0.60€ cuando `libro_liquidez` > 1508.4106 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.157 (n=1148)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=3520)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2405)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2329)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.191 (n=898)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2709)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3586)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=445)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.257 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=428)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=902)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=358)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=943)

- **FILTRO** `libro_liquidez` < `1786.4389` → IC=-0.161 (n=240)

  - _Acción_: SKIP cuando `libro_liquidez` < 1786.4389
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=722)

- **FILTRO** `libro_liquidez` < `2090.2217` → IC=-0.168 (n=350)

  - _Acción_: SKIP cuando `libro_liquidez` < 2090.2217
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=712)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=43)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.037)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=68)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=17505)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=39436)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=14088)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=42853)

- **FILTRO** `ibs_7min` < `0.2348` → IC=-0.229 (n=14235)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2348
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=42706)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=18858)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=38083)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.241 (n=17564)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=53960)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.182 (n=17667)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=53857)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.148 (n=2479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=7510)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=2385)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=7604)

- **FILTRO** `ibs_7min` < `0.7123` → IC=-0.243 (n=3296)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7123
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6693)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.182 (n=2062)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7927)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.272 (n=3084)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=9314)

- **FILTRO** `ibs_7min` > `0.7692` → IC=-0.211 (n=3099)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=9299)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.130 (n=2288)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=7304)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.266 (n=2248)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7344)

- **FILTRO** `ibs_7min` < `0.7238` → IC=-0.200 (n=2397)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7238
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7195)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.191 (n=2389)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7203)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.261 (n=2398)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=7350)

- **FILTRO** `ibs_7min` > `0.267` → IC=-0.194 (n=2436)

  - _Acción_: SKIP cuando `ibs_7min` > 0.267
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7312)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.183 (n=2427)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7321)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.161 (n=2313)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=7150)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=2335)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=7128)

- **FILTRO** `ibs_7min` < `0.2945` → IC=-0.246 (n=3122)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2945
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6341)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.195 (n=2227)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7236)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.254 (n=3073)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=10112)

- **FILTRO** `ibs_7min` > `0.7321` → IC=-0.178 (n=3296)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7321
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=9889)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.126 (n=3008)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=6263)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2176)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7095)

- **FILTRO** `ibs_7min` < `0.7263` → IC=-0.188 (n=2317)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7263
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6954)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.189 (n=2268)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7003)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=2164)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7449)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.176 (n=2403)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7210)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.177 (n=2333)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7280)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=2258)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7048)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.222 (n=3020)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6286)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.218 (n=2245)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7061)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.191 (n=3342)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=10315)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.293 (n=2222)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=7098)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.223 (n=2323)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6997)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.197 (n=2306)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7014)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.219 (n=3163)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9760)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=120)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=986)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1270)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.121 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=499)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=552)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=853)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.475` → IC=-0.122 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=333)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=328)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=445)

- **FILTRO** `libro_liquidez` < `3257.5356` → IC=-0.154 (n=180)

  - _Acción_: SKIP cuando `libro_liquidez` < 3257.5356
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=543)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.140 (n=1195)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.139 (n=621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 6.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `441.7389` → IC=+0.156 (n=399)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 441.7389 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3591.1308` → IC=+0.147 (n=542)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3591.1308 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.148 (n=396)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 11.0 (IC base=+0.131)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.438` → IC=+0.142 (n=93)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.438 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.188 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 14.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `375.759` → IC=+0.148 (n=245)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 375.759 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2555.2732` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 2555.2732 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 6.0 (IC base=+0.134)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3987` → IC=+0.139 (n=247)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3987 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.137 (n=221)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.129 (n=297)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.04 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2349.306` → IC=+0.135 (n=165)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2349.306 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.137 (n=169)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 13.0 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.189 (n=159)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.153 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 4.0 (IC base=+0.140)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.220 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7632.4676` → IC=+0.146 (n=159)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 7632.4676 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 69.0 (IC base=+0.140)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4324` → IC=+0.253 (n=95)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4324 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.175 (n=192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.154)

- **PATRÓN** `total_vol_5m` < `4970.298` → IC=+0.190 (n=140)

  - _Acción_: Kelly boost +0.95€ cuando `total_vol_5m` < 4970.298 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `3221.1629` → IC=+0.167 (n=187)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3221.1629 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.171 (n=74)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 27.0 (IC base=+0.154)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.128 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.103)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=140)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3582.6278` → IC=+0.154 (n=102)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3582.6278 (IC base=+0.103)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.9794` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.9794
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=139)

- **FILTRO** `sigma_h` > `0.0073` → IC=-0.335 (n=168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=508)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.180 (n=170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0035 (IC base=-0.084)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.327 (n=50)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=151)

- **FILTRO** `T_h` > `87.9901` → IC=-0.250 (n=50)

  - _Acción_: SKIP cuando `T_h` > 87.9901
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=151)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.292 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.032)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.232 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `pct_vs_K` |x|> `9.8932` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.8932
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.274 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=91)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.229 (n=411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=212)

- **FILTRO** `T_h` > `87.6255` → IC=-0.199 (n=417)

  - _Acción_: SKIP cuando `T_h` > 87.6255
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=206)

- **FILTRO** `sigma_h` > `0.0095` → IC=-0.243 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=403)

- **FILTRO** `T_h` > `54.4279` → IC=-0.265 (n=402)

  - _Acción_: SKIP cuando `T_h` > 54.4279
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=135)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.7856` → IC=-0.365 (n=50)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7856
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=154)

- **FILTRO** `T_h` > `144.0601` → IC=-0.296 (n=47)

  - _Acción_: SKIP cuando `T_h` > 144.0601
  - _Potencial_: sin este filtro IC_bueno=-0.253 (n=144)

- **FILTRO** `pct_vs_K` |x|> `2.9778` → IC=-0.439 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9778
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=144)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.01` → IC=-0.301 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=45)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.360 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=127)

- **FILTRO** `T_h` > `57.7851` → IC=-0.270 (n=111)

  - _Acción_: SKIP cuando `T_h` > 57.7851
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=57)

- **PATRÓN** `pct_vs_K` |x|≤ `0.7908` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `pct_vs_K` |x|≤ 0.7908 (IC base=-0.182)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.008` → IC=-0.273 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=131)

- **FILTRO** `T_h` > `89.5392` → IC=-0.218 (n=115)

  - _Acción_: SKIP cuando `T_h` > 89.5392
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=58)

- **FILTRO** `sigma_h` > `0.0135` → IC=-0.357 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0135
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=79)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.281 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=80)

- **FILTRO** `T_h` > `45.0112` → IC=-0.290 (n=79)

  - _Acción_: SKIP cuando `T_h` > 45.0112
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=40)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.477 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.343)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.359 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.343)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.394 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.343)

- **PATRÓN** `T_h` < `0.3604` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3604 (IC base=+0.343)

- **PATRÓN** `T_h` > `0.7606` → IC=+0.379 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7606 (IC base=+0.343)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.343)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.359 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.343)

- **PATRÓN** `edge` > `0.0992` → IC=+0.443 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0992 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.436 (n=200)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.417)

- **PATRÓN** `T_h` > `1.484` → IC=+0.422 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.472 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1831` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1831 (IC base=+0.186)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.186)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.420)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.419 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.420)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.423 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.420)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.458 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.420)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.407 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.420)

- **PATRÓN** `dist_50` > `0.3792` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3792 (IC base=+0.420)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.431 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.420)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.420)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1838` → IC=+0.484 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1838 (IC base=+0.440)

- **PATRÓN** `sigma_h` < `0.0163` → IC=+0.468 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0163 (IC base=+0.440)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.452 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.440)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.468 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.440)

- **PATRÓN** `edge` > `0.2005` → IC=+0.479 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.479 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.465)

- **PATRÓN** `T_h` > `0.6729` → IC=+0.465 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.6729 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.4658` → IC=+0.492 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4658 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.473 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=321)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=396)

- **PATRÓN** `streak_estiramiento` < `0.8365` → IC=+0.124 (n=267)

  - _Acción_: Kelly boost +0.62€ cuando `streak_estiramiento` < 0.8365 (IC base=+0.051)

- **PATRÓN** `libro_liquidez` > `2508.1541` → IC=+0.141 (n=143)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2508.1541 (IC base=+0.051)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.2566` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `streak_estiramiento` < 0.2566 (IC base=+0.004)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.093)

- **PATRÓN** `streak_estiramiento` < `0.4376` → IC=+0.195 (n=103)

  - _Acción_: Kelly boost +0.98€ cuando `streak_estiramiento` < 0.4376 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 35.0 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2208.5143` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2208.5143 (IC base=+0.093)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=94)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=748)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `volumen_racha` > `3677.1957` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `volumen_racha` > 3677.1957
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `libro_liquidez` < `3338.6704` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_liquidez` < 3338.6704
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `streak_estiramiento` > `1.1496` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1496
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=43)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `streak_len` > `4.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### STREAK_FADE_60M#SOL#60min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.056)

- **PATRÓN** `volumen_racha` < `17126.646` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 17126.646 (IC base=+0.056)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1028)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1332)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=1186)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1229)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `19.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=26)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=4105)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=26)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=2286)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.194 (n=1654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0054 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.192 (n=1252)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0121 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.190 (n=3307)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.174)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1327` → IC=+0.181 (n=1505)

  - _Acción_: Kelly boost +0.91€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1327 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.182 (n=3481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=3453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.174)

- **PATRÓN** `ibs_15` > `0.5455` → IC=+0.249 (n=3759)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5455 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.1305` → IC=+0.170 (n=1786)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1305 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.3236` → IC=+0.160 (n=3005)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.3236 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.462` → IC=+0.258 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.462 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `4612.7985` → IC=+0.191 (n=1252)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 4612.7985 (IC base=+0.174)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1498)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.256 (n=211)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.270 (n=211)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.218)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.245 (n=210)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `ibs_15` > `0.7231` → IC=+0.284 (n=631)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7231 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.232 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.295 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `8703.7944` → IC=+0.228 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8703.7944 (IC base=+0.218)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.188 (n=248)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.153 (n=496)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1411` → IC=+0.151 (n=496)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio_macro` |x|> 0.1411 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1276` → IC=+0.153 (n=295)

  - _Acción_: Kelly boost +0.77€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1276 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.153 (n=682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.149 (n=772)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.537` → IC=+0.240 (n=744)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.537 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.159 (n=458)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.163` → IC=+0.146 (n=591)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.163 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.707` → IC=+0.276 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.707 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3217.9115` → IC=+0.151 (n=744)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3217.9115 (IC base=+0.144)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.725` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.725
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=359)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8857` → IC=+0.242 (n=293)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8857 (IC base=+0.088)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=480)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.088)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.781` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 15.781 (IC base=+0.002)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0241` → IC=+0.230 (n=287)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0241 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.1304` → IC=+0.222 (n=574)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1304 (IC base=+0.199)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0952` → IC=+0.239 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0952 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=785)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.209 (n=768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.199)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.274 (n=861)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.1316` → IC=+0.216 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1316 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.291` → IC=+0.231 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.291 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2956.4998` → IC=+0.296 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2956.4998 (IC base=+0.199)

- **PATRÓN** `ibs_15` < `0.1087` → IC=+0.165 (n=790)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.1087 (IC base=+0.070)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.364 (n=431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.389 (n=215)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1464` → IC=+0.384 (n=429)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1464 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1392` → IC=+0.387 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1392 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.376 (n=650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7862` → IC=+0.400 (n=646)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7862 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1483` → IC=+0.382 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1483 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.388 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `10217.3693` → IC=+0.385 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10217.3693 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.364 (n=292)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.403 (n=111)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.0554` → IC=+0.367 (n=111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0554 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.388 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.393 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.380 (n=332)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8048` → IC=+0.392 (n=331)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8048 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2499` → IC=+0.387 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2499 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.521` → IC=+0.380 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.521 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `16828.3206` → IC=+0.403 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16828.3206 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.404 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.371 (n=138)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.383 (n=143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.363 (n=210)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.380 (n=281)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.382 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.390 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.375 (n=142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7485` → IC=+0.408 (n=314)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7485 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4673` → IC=+0.386 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4673 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.2966` → IC=+0.367 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2966 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.352` → IC=+0.395 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.352 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3991.4206` → IC=+0.397 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3991.4206 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.374 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 159.0 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.177 (n=2225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2227)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=1751)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2701)

- **PATRÓN** `ibs_15` > `0.6335` → IC=+0.281 (n=1069)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6335 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.205 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2726` → IC=+0.197 (n=913)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2726 (IC base=-0.069)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2307` → IC=+0.271 (n=1241)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2307 (IC base=-0.012)

- **PATRÓN** `ibs_15` < `0.3626` → IC=+0.283 (n=3723)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3626 (IC base=-0.012)

- **PATRÓN** `dist_vwap_pct` > `0.6717` → IC=+0.278 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6717 (IC base=-0.012)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.215 (n=655)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=1969)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.230 (n=656)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1968)

- **FILTRO** `sigma_ewma_delta_pct` > `23.313` → IC=-0.265 (n=377)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.313
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=2247)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=2558)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.172 (n=260)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0028 (IC base=+0.093)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2081` → IC=+0.283 (n=159)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2081 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.130 (n=384)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 15.0 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.7591` → IC=+0.332 (n=349)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7591 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1061` → IC=+0.282 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1061 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` < `0.2456` → IC=+0.279 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2456 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.603` → IC=+0.128 (n=390)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 8.603 (IC base=+0.093)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.219 (n=62)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.193)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.159` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.159 (IC base=-0.193)

- **PATRÓN** `ibs_15` < `0.6128` → IC=+0.312 (n=62)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6128 (IC base=-0.193)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.193)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=-0.193)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=700)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=474)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.159 (n=359)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0049 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0545` → IC=+0.187 (n=180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.0545 (IC base=+0.151)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.195 (n=414)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.173 (n=387)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 11.0 (IC base=+0.151)

- **PATRÓN** `ibs_15` > `0.5959` → IC=+0.248 (n=538)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5959 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.4741` → IC=+0.169 (n=140)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.4741 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1621` → IC=+0.152 (n=423)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1621 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.387` → IC=+0.248 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.387 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=700)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `7912.0475` → IC=+0.154 (n=244)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7912.0475 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.249 (n=1373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7725` → IC=+0.255 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7725 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1569` → IC=+0.260 (n=915)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1569 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.248 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.245 (n=1215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3764` → IC=+0.278 (n=1373)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3764 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6309` → IC=+0.263 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6309 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.399` → IC=+0.254 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.399 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.238 (n=258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=778)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.251 (n=352)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=684)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.285 (n=258)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=778)

- **FILTRO** `sigma_ewma_delta_pct` > `6.662` → IC=-0.201 (n=239)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.662
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=797)

- **FILTRO** `sigma_ewma_delta_pct` > `17.839` → IC=-0.147 (n=539)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.839
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.190)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.190)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.190)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.190)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.292 (n=599)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.1869` → IC=+0.243 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1869 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.249 (n=547)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=682)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.211)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.07` → IC=+0.276 (n=794)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.07 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1784` → IC=+0.289 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1784 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.1376` → IC=+0.317 (n=593)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1376 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.786` → IC=+0.353 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.786 (IC base=-0.025)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.080)

- **PATRÓN** `drift_15min` |x|≤ `0.3927` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3927 (IC base=+0.080)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.080)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.080)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.080)

- **PATRÓN** `drift_15min` |x|≤ `0.3927` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3927 (IC base=+0.080)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.080)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.080)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.296 (n=976)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0537` → IC=+0.320 (n=370)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0537 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2408` → IC=+0.312 (n=370)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2408 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.224` → IC=+0.301 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.224 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=1156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.318 (n=1109)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2762` → IC=+0.322 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2762 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.376 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `12232.3596` → IC=+0.312 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12232.3596 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.310 (n=261)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.301 (n=269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.315 (n=198)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.258` → IC=+0.314 (n=197)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.258 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=594)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8305` → IC=+0.313 (n=592)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8305 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.1465` → IC=+0.322 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1465 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.369 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16163.1166` → IC=+0.335 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16163.1166 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.303 (n=517)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.317 (n=173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.296 (n=517)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.309 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.312 (n=499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.295 (n=466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.321 (n=517)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.6708` → IC=+0.325 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6708 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.372 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2626` → IC=-0.132 (n=85)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2626
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=256)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1232` → IC=-0.155 (n=85)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1232
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=256)

- **FILTRO** `ballena_activa_n` > `44.0` → IC=-0.136 (n=229)

  - _Acción_: SKIP cuando `ballena_activa_n` > 44.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=80)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.208 (n=118)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=364)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.180 (n=120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=362)

- **FILTRO** `drift_15min` |x|> `0.4386` → IC=-0.148 (n=163)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4386
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=319)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1334` → IC=-0.147 (n=49)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1334
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=150)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2395` → IC=-0.121 (n=93)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2395
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=94)

- **FILTRO** `drift_15min` |x|> `0.3423` → IC=-0.289 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3423
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=35)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2021` → IC=-0.250 (n=26)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2021
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=26)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1254` → IC=-0.200 (n=18)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1254
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=39)

- **FILTRO** `drift_15min` |x|> `0.1605` → IC=-0.340 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1605
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0611` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0611
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.150 (n=38)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0898` → IC=-0.227 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0898
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0058` → IC=-0.250 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `87.7391` → IC=+0.193 (n=496)

  - _Acción_: Kelly boost +0.96€ cuando `T_h` > 87.7391 (IC base=+0.189)

- **PATRÓN** `ratio` < `0.973` → IC=+0.406 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.189)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.353 (n=2263)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.375 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `109.3643` → IC=+0.183 (n=206)

  - _Acción_: Kelly boost +0.91€ cuando `T_h` > 109.3643 (IC base=+0.159)

- **PATRÓN** `ratio` < `0.9831` → IC=+0.327 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9831 (IC base=+0.159)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.305 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.294)

- **PATRÓN** `ratio` > `1.0451` → IC=+0.406 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0451 (IC base=+0.294)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.233 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.229)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.396 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.229)

- **PATRÓN** `T_h` > `111.9922` → IC=+0.353 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9922 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.333 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0966` → IC=+0.441 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0966 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5455 sube el IC de +0.174 a +0.249 en UPDOWN_GBM#15min (n=3759). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7231 sube el IC de +0.218 a +0.284 en UPDOWN_GBM#BTC#15min (n=631). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.537 sube el IC de +0.144 a +0.240 en UPDOWN_GBM#ETH#15min (n=744). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8857 sube el IC de +0.088 a +0.242 en UPDOWN_GBM#SOL#15min (n=293). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.199 a +0.274 en UPDOWN_GBM#XRP#15min (n=861). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1087 sube el IC de +0.070 a +0.165 en UPDOWN_GBM#XRP#15min (n=790). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6335 sube el IC de -0.069 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=1069). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3626 sube el IC de -0.012 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=3723). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7591 sube el IC de +0.093 a +0.332 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=349). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6128 sube el IC de -0.193 a +0.312 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5959 sube el IC de +0.151 a +0.248 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=538). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3764 sube el IC de +0.244 a +0.278 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1373). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.190 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.039 a +0.292 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=599). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.211 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1376 sube el IC de -0.025 a +0.317 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=593). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.080 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7 (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.080 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.290 a +0.318 en UPDOWN_GBM_IBS_ALTO (n=1109). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8305 sube el IC de +0.288 a +0.313 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=592). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.293 a +0.321 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=517). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7862 sube el IC de +0.364 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=646). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8048 sube el IC de +0.362 a +0.392 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=331). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7485 sube el IC de +0.364 a +0.408 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=314). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1969 | +0.089 | +207.43€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1969 | +0.089 | +207.43€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1577 | +0.092 | +178.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1577 | +0.092 | +178.70€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 740 | -0.004 | +77.80€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 740 | -0.004 | +77.80€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 5 | +0.018 | +2.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 551 | -0.034 | +42.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 551 | -0.034 | +42.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 148 | +0.093 | +27.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 148 | +0.093 | +27.91€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 41122 | -0.080 | -5061.81€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2307 | +0.041 | -261.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 38815 | -0.087 | -4800.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4533 | -0.114 | -775.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4533 | -0.114 | -775.02€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2307 | +0.041 | -261.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2307 | +0.041 | -261.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4420 | -0.107 | -879.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4420 | -0.107 | -879.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10969 | -0.018 | -1019.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10969 | -0.018 | -1019.30€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10903 | -0.105 | -799.72€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10903 | -0.105 | -799.72€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7990 | -0.132 | -1326.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7990 | -0.132 | -1326.03€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 36686 | -0.015 | +3284.32€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9494 | +0.004 | +1648.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 27192 | -0.021 | +1635.80€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 36686 | -0.015 | +3284.32€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9494 | +0.004 | +1648.53€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 27192 | -0.021 | +1635.80€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 150292 | +0.115 | -6023.85€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 19052 | +0.181 | -624.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 663 | -0.013 | -68.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 121629 | +0.107 | -4999.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8948 | +0.098 | -331.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 20164 | +0.108 | -1235.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 20088 | +0.109 | -1235.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 29015 | +0.127 | -452.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5259 | +0.186 | -198.77€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 20148 | +0.121 | -116.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3566 | +0.081 | -115.91€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 20219 | +0.100 | -1398.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 75 | -0.123 | -6.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 20129 | +0.101 | -1380.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 31980 | +0.124 | -615.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8252 | +0.176 | -180.80€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 20431 | +0.107 | -371.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3285 | +0.100 | -54.25€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 28728 | +0.115 | -1393.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5336 | +0.197 | -253.15€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 566 | +0.019 | -14.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 20729 | +0.095 | -964.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2097 | +0.123 | -161.61€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 20186 | +0.106 | -927.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 69 | -0.091 | +4.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 20104 | +0.107 | -931.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 24177 | +0.197 | -1447.51€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 24177 | +0.197 | -1447.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5493 | +0.180 | -456.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5493 | +0.180 | -456.81€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3127 | +0.203 | -75.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3127 | +0.203 | -75.29€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5432 | +0.180 | -432.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5432 | +0.180 | -432.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4699 | +0.248 | -161.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4699 | +0.248 | -161.37€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5347 | +0.189 | -335.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5347 | +0.189 | -335.71€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1053 | +0.426 | -37.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1053 | +0.426 | -37.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 416 | +0.433 | -8.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 416 | +0.433 | -8.98€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 416 | +0.433 | -7.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 416 | +0.433 | -7.56€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 207 | +0.400 | -17.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 207 | +0.400 | -17.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 84724 | +0.201 | -6036.31€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 84724 | +0.201 | -6036.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14556 | +0.185 | -1496.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14556 | +0.185 | -1496.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13676 | +0.225 | -459.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13676 | +0.225 | -459.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14514 | +0.181 | -1521.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14514 | +0.181 | -1521.16€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13777 | +0.219 | -538.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13777 | +0.219 | -538.30€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 14058 | +0.202 | -915.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 14058 | +0.202 | -915.75€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 14143 | +0.198 | -1104.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 14143 | +0.198 | -1104.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 32461 | +0.116 | +187.21€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 32461 | +0.116 | +187.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 16143 | +0.119 | +166.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 16143 | +0.119 | +166.96€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 16318 | +0.114 | +20.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 16318 | +0.114 | +20.26€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2137 | +0.292 | -7.56€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2137 | +0.292 | -7.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 982 | +0.280 | -25.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 982 | +0.280 | -25.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1033 | +0.297 | +13.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1033 | +0.297 | +13.94€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 122 | +0.347 | +4.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 122 | +0.347 | +4.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 981 | +0.442 | +5.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 981 | +0.442 | +5.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 478 | +0.435 | -5.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 478 | +0.435 | -5.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 456 | +0.450 | +9.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 456 | +0.450 | +9.62€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 47 | +0.398 | +0.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 47 | +0.398 | +0.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1695 | +0.070 | -71.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 654 | +0.046 | -59.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1041 | +0.085 | -11.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 74 | +0.118 | +4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1303 | +0.078 | -30.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 262 | +0.049 | -19.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1041 | +0.085 | -11.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 318 | +0.025 | -45.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 318 | +0.025 | -45.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 64352 | +0.101 | -1602.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5198 | +0.092 | +62.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 59154 | +0.101 | -1664.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 35368 | +0.105 | -397.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5198 | +0.092 | +62.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 30170 | +0.108 | -459.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 13296 | +0.109 | -68.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 13296 | +0.109 | -68.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 15688 | +0.083 | -1136.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 15688 | +0.083 | -1136.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 898 | +0.192 | -109.62€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 898 | +0.192 | -109.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 898 | +0.192 | -109.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 898 | +0.192 | -109.62€ | 2 | 4 |
| ✅ GBM_LATE_15M | 44149 | +0.095 | +23227.18€ | 0 | 17 |
| ✅ GBM_LATE_15M#15min | 44149 | +0.095 | +23227.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7348 | +0.218 | +6098.10€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7348 | +0.218 | +6098.10€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6650 | +0.181 | +5132.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6650 | +0.181 | +5132.94€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 7897 | +0.205 | +6148.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7897 | +0.205 | +6148.22€ | 0 | 22 |
| ✅ GBM_LATE_15M#ETH | 6138 | +0.044 | +1745.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6138 | +0.044 | +1745.18€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 6201 | -0.031 | +1324.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6201 | -0.031 | +1324.05€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 9915 | -0.029 | +2778.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9915 | -0.029 | +2778.69€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 47394 | +0.085 | +25877.33€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 47394 | +0.085 | +25877.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9176 | +0.002 | +4643.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9176 | +0.002 | +4643.66€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 10065 | +0.010 | +2427.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 10065 | +0.010 | +2427.02€ | 0 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6561 | +0.279 | +7074.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6561 | +0.279 | +7074.27€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8595 | +0.013 | +2121.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8595 | +0.013 | +2121.90€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7526 | +0.039 | +3118.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7526 | +0.039 | +3118.70€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5471 | +0.306 | +6491.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5471 | +0.306 | +6491.78€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 34939 | +0.181 | +28403.27€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 34939 | +0.181 | +28403.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5301 | +0.232 | +4754.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5301 | +0.232 | +4754.13€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5495 | +0.150 | +4091.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5495 | +0.150 | +4091.36€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5609 | +0.223 | +4819.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5609 | +0.223 | +4819.47€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5931 | +0.138 | +4506.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5931 | +0.138 | +4506.60€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6565 | +0.125 | +4902.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6565 | +0.125 | +4902.88€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6038 | +0.227 | +5328.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6038 | +0.227 | +5328.83€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9463 | +0.133 | +4621.26€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9463 | +0.133 | +4621.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 409 | +0.154 | +256.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 409 | +0.154 | +256.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2752 | +0.142 | +1547.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2752 | +0.142 | +1547.85€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2826 | +0.137 | +1356.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2826 | +0.137 | +1356.97€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2382 | +0.110 | +939.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2382 | +0.110 | +939.14€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 627 | +0.133 | +281.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 627 | +0.133 | +281.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 44285 | +0.186 | +35593.00€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 44285 | +0.186 | +35593.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7012 | +0.243 | +6583.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7012 | +0.243 | +6583.66€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6920 | +0.148 | +4771.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6920 | +0.148 | +4771.79€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7501 | +0.233 | +6701.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7501 | +0.233 | +6701.61€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7310 | +0.139 | +5201.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7310 | +0.139 | +5201.30€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7832 | +0.121 | +5426.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7832 | +0.121 | +5426.27€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7710 | +0.233 | +6908.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7710 | +0.233 | +6908.37€ | 0 | 18 |
| ✅ GBM_LATE_5M | 12025 | +0.203 | +9423.62€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 12025 | +0.203 | +9423.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 999 | +0.241 | +926.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 999 | +0.241 | +926.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2786 | +0.206 | +2377.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2786 | +0.206 | +2377.80€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1167 | +0.196 | +861.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1167 | +0.196 | +861.83€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3348 | +0.193 | +2353.77€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3348 | +0.193 | +2353.77€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1802 | +0.195 | +1406.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1802 | +0.195 | +1406.58€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1923 | +0.208 | +1497.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1923 | +0.208 | +1497.52€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3673 | +0.065 | +1163.03€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3673 | +0.065 | +1163.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1350 | +0.081 | +470.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1350 | +0.081 | +470.01€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1191 | +0.066 | +406.62€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1191 | +0.066 | +406.62€ | 0 | 8 |
| ✅ GBM_LATE_60M#SOL | 1132 | +0.044 | +286.40€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1132 | +0.044 | +286.40€ | 0 | 13 |
| 🚫 GBM_LATE_60M_FADE | 589 | -0.241 | -16.66€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 589 | -0.241 | -16.66€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 219 | -0.242 | -12.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 219 | -0.242 | -12.64€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 210 | -0.226 | +2.50€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 210 | -0.226 | +2.50€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 160 | -0.253 | -6.52€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 160 | -0.253 | -6.52€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1602 | +0.083 | +405.75€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1602 | +0.083 | +405.75€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 629 | +0.080 | +152.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 629 | +0.080 | +152.29€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 563 | +0.056 | +90.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 563 | +0.056 | +90.70€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 410 | +0.124 | +162.76€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 410 | +0.124 | +162.76€ | 3 | 9 |
| ✅ LATE_WINDOW_5MIN | 171 | +0.275 | +166.39€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 171 | +0.275 | +166.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 171 | +0.275 | +166.39€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 171 | +0.275 | +166.39€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3502 | +0.102 | +863.44€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3502 | +0.102 | +863.44€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3502 | +0.102 | +863.44€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3502 | +0.102 | +863.44€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 604 | -0.026 | -7.57€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 604 | -0.026 | -7.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 172 | +0.000 | +6.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 172 | +0.000 | +6.12€ | 2 | 2 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 127 | +0.004 | +2.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 127 | +0.004 | +2.92€ | 3 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 220 | -0.009 | -0.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 220 | -0.009 | -0.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3804 | +0.016 | +87.46€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3804 | +0.016 | +87.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 184 | +0.027 | -1.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 184 | +0.027 | -1.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 797 | +0.007 | +28.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 797 | +0.007 | +28.91€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 209 | -0.007 | -2.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 209 | -0.007 | -2.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1404 | +0.024 | +30.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1404 | +0.024 | +30.86€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 758 | +0.012 | +2.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 758 | +0.012 | +2.16€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 452 | +0.018 | +29.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 452 | +0.018 | +29.11€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1830 | -0.039 | -26.67€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1830 | -0.039 | -26.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 532 | -0.028 | -10.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 532 | -0.028 | -10.90€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 630 | -0.017 | +5.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 630 | -0.017 | +5.08€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 668 | -0.067 | -20.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 668 | -0.067 | -20.86€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 9553 | -0.028 | +0.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4539 | -0.038 | -98.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 5014 | -0.018 | +99.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 289 | -0.029 | -3.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 148 | -0.013 | +2.50€ | 2 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 141 | -0.045 | -5.73€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2403 | -0.023 | -3.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1138 | -0.030 | -18.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1265 | -0.017 | +15.01€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1033 | -0.026 | +12.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 521 | -0.043 | -12.99€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 512 | -0.008 | +25.63€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2105 | -0.040 | -55.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 978 | -0.053 | -59.36€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1127 | -0.028 | +3.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1863 | -0.017 | +45.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 895 | -0.029 | +0.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 968 | -0.005 | +45.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1860 | -0.032 | +4.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 859 | -0.040 | -10.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1001 | -0.024 | +14.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 3379 | -0.021 | -71.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 3379 | -0.021 | -71.38€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 2562 | +0.007 | -17.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 3075 | -0.015 | -29.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 3075 | -0.015 | -29.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 3388 | -0.018 | -66.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 1680 | -0.005 | -32.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 51871 | +0.000 | +2632.86€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 51871 | +0.000 | +2632.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9368 | +0.026 | +1207.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9368 | +0.026 | +1207.36€ | 2 | 5 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7449 | -0.033 | -100.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7449 | -0.033 | -100.07€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9466 | +0.025 | +1003.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9466 | +0.025 | +1003.91€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7292 | -0.048 | -151.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7292 | -0.048 | -151.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8771 | -0.004 | +241.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8771 | -0.004 | +241.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9525 | +0.016 | +431.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9525 | +0.016 | +431.61€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6709 | -0.057 | -149.16€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6709 | -0.057 | -149.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1230 | -0.001 | -15.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1230 | -0.001 | -15.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1759 | -0.074 | -37.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1759 | -0.074 | -37.88€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 61 | -0.024 | -0.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 61 | -0.024 | -0.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 778 | -0.119 | -33.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 778 | -0.119 | -33.14€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2024 | -0.072 | -36.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2024 | -0.072 | -36.23€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 857 | -0.016 | -25.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 857 | -0.016 | -25.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M | 3368 | +0.004 | -1.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3368 | +0.004 | -1.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 128465 | -0.076 | +1726.02€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 128465 | -0.076 | +1726.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 22387 | -0.077 | +1118.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 22387 | -0.077 | +1118.73€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 19340 | -0.101 | -1030.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 19340 | -0.101 | -1030.90€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 22648 | -0.068 | +1207.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 22648 | -0.068 | +1207.40€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 18884 | -0.097 | -594.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 18884 | -0.097 | -594.13€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 22963 | -0.057 | +340.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 22963 | -0.057 | +340.86€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 22243 | -0.067 | +684.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 22243 | -0.067 | +684.06€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8799 | -0.034 | -185.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8799 | -0.034 | -185.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1993 | -0.047 | -26.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1993 | -0.047 | -26.70€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2604 | -0.027 | -43.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2604 | -0.027 | -43.23€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1218 | -0.057 | -28.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1218 | -0.057 | -28.33€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 975 | -0.031 | -35.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 975 | -0.031 | -35.88€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1728 | +0.125 | +713.82€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1592 | +0.131 | +701.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 370 | +0.134 | +181.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 370 | +0.134 | +181.14€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 329 | +0.119 | +115.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 329 | +0.119 | +115.57€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#ETH | 317 | +0.140 | +158.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 317 | +0.140 | +158.54€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 278 | +0.154 | +155.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 278 | +0.154 | +155.69€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 298 | +0.103 | +90.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 298 | +0.103 | +90.28€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1549 | -0.018 | -28.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1549 | -0.018 | -28.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 299 | +0.002 | +10.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 299 | +0.002 | +10.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 271 | -0.024 | -1.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 271 | -0.024 | -1.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 402 | -0.047 | -34.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 402 | -0.047 | -34.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 326 | -0.003 | -4.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 326 | -0.003 | -4.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 251 | -0.010 | +0.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 251 | -0.010 | +0.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 927 | -0.074 | -50.09€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 432 | -0.113 | -80.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 336 | -0.142 | -68.17€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 326 | -0.030 | +23.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 235 | -0.019 | +26.42€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 169 | -0.056 | +6.72€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 138 | -0.064 | +2.34€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 709 | -0.086 | -39.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1160 | -0.206 | -69.34€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 452 | -0.209 | -42.98€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 395 | -0.213 | -42.75€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 395 | -0.208 | -30.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 347 | -0.219 | -38.00€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 313 | -0.198 | +4.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 292 | -0.194 | +2.51€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1034 | -0.210 | -78.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 126 | -0.172 | +8.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 460 | +0.396 | +438.23€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 69 | +0.162 | +55.45€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 69 | +0.162 | +55.45€ | 0 | 2 |
| ✅ RESOLUTION_SNIPER#ETH | 110 | +0.366 | +102.82€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 110 | +0.366 | +102.82€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 281 | +0.461 | +279.96€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 281 | +0.461 | +279.96€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 460 | +0.396 | +438.23€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 755 | +0.030 | +45.02€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 755 | +0.030 | +45.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 306 | +0.019 | +2.32€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 306 | +0.019 | +2.32€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 63 | -0.008 | -1.05€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 63 | -0.008 | -1.05€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 77 | -0.006 | +1.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 77 | -0.006 | +1.97€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 309 | +0.056 | +41.79€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 309 | +0.056 | +41.79€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3443 | -0.021 | -133.25€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3443 | -0.021 | -133.25€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1059 | -0.020 | -35.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1059 | -0.020 | -35.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 591 | -0.026 | -25.53€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 591 | -0.026 | -25.53€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 165 | -0.039 | -13.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 165 | -0.039 | -13.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1628 | -0.018 | -58.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1628 | -0.018 | -58.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 103 | -0.052 | -9.27€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 103 | -0.052 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 60 | -0.016 | -4.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 60 | -0.016 | -4.20€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11077 | +0.016 | +84.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11077 | +0.016 | +84.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2831 | +0.020 | +29.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2831 | +0.020 | +29.03€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2897 | +0.018 | +34.88€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2897 | +0.018 | +34.88€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2892 | +0.009 | -0.90€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2892 | +0.009 | -0.90€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2457 | +0.015 | +21.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2457 | +0.015 | +21.46€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10064 | +0.013 | -51.74€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10064 | +0.013 | -51.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4124 | +0.018 | -7.21€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4124 | +0.018 | -7.21€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3620 | +0.010 | -29.23€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3620 | +0.010 | -29.23€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2320 | +0.009 | -15.30€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2320 | +0.009 | -15.30€ | 1 | 0 |
| ✅ UPDOWN_GBM | 79647 | +0.054 | +7072.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 19757 | +0.083 | +4306.23€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2541 | +0.004 | +24.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 52337 | +0.051 | +2650.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4730 | +0.007 | +93.13€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 17418 | +0.056 | +1498.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2584 | +0.090 | +630.04€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 690 | +0.009 | +11.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11933 | +0.061 | +789.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2109 | +0.004 | +64.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 102 | -0.067 | +3.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8671 | +0.070 | +917.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7038 | +0.054 | +308.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 18470 | +0.045 | +1208.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4722 | +0.068 | +693.73€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 671 | +0.007 | +16.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 11313 | +0.045 | +478.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1670 | +0.010 | +18.32€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 94 | -0.104 | +2.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 17520 | +0.033 | +868.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5016 | +0.035 | +395.93€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 637 | -0.009 | +0.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10832 | +0.039 | +467.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 951 | +0.007 | +10.53€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 84 | -0.128 | -5.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10715 | +0.066 | +1504.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4304 | +0.104 | +1277.49€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6023 | +0.042 | +227.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 280 | -0.099 | -0.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 859 | +0.364 | +313.65€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 859 | +0.364 | +313.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 441 | +0.362 | +151.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 441 | +0.362 | +151.78€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 418 | +0.364 | +161.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 418 | +0.364 | +161.87€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 20458 | -0.025 | +4778.09€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 20458 | -0.025 | +4778.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3662 | -0.112 | +135.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3662 | -0.112 | +135.04€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2547 | +0.218 | +1656.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2547 | +0.218 | +1656.35€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5865 | -0.066 | +706.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5865 | -0.066 | +706.44€ | 5 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5718 | -0.065 | +1006.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5718 | -0.065 | +1006.98€ | 1 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 240 | +0.050 | +14.41€ | 0 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 240 | +0.050 | +14.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 240 | +0.050 | +14.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 240 | +0.050 | +14.41€ | 0 | 5 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1478 | +0.290 | +1261.69€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1478 | +0.290 | +1261.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 789 | +0.288 | +639.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 789 | +0.288 | +639.13€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 689 | +0.293 | +622.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 689 | +0.293 | +622.57€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 823 | -0.112 | -81.93€ | 6 | 0 |
| ✅ UPDOWN_OU_5M#5min | 823 | -0.112 | -81.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 251 | -0.081 | -18.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 251 | -0.081 | -18.64€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 89 | -0.170 | -10.17€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 89 | -0.170 | -10.17€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 100 | -0.176 | -3.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 100 | -0.176 | -3.77€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3732 | +0.304 | +1760.10€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1376 | +0.258 | +172.01€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1435 | +0.299 | +644.37€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 921 | +0.380 | +943.72€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.023 n=1003 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1003 IC=+0.023 PNL=+44.32€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 726 celda(s) pasan gate riguroso completo de 2728 evaluadas (n>=40) y 3777 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=5015 IC=+0.035 PNL=+396.44€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1435/15 IC=+0.299 PNL=+644.37€ | BTC: n=1376/15 IC=+0.258 PNL=+172.01€ | SOL: n=921/15 IC=+0.380 PNL=+943.72€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 31 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
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
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=806/60 | contraria IC=+0.193 n=842 | gap=-0.053 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=479, boost estimado=+0.018. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1669/40 IC=+0.009 PNL=+17.80€ | BTC#60min: n=2109/40 IC=+0.004 PNL=+64.28€ | SOL#60min: n=951/40 IC=+0.007 PNL=+10.53€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=576385 | tras_1loss IC=+0.096 n=437555 | tras_2loss IC=+0.066 n=176746/40 | gap=-0.018 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.195 > 0.08 con n=779 PNL=+571.15€
  - _Datos_: n=779 IC=+0.195 PNL=+571.15€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.169 > 0.08 con n=885 PNL=+504.15€
  - _Datos_: n=885 IC=+0.169 PNL=+504.15€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.157 > 0.08 con n=65 PNL=+31.12€
  - _Datos_: n=65 IC=+0.157 PNL=+31.12€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=3047 PNL=+1686.71€
  - _Datos_: n=3047 IC=+0.333 PNL=+1686.71€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=730 IC=+0.071 PNL=+81.25€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=730 IC=+0.071 PNL=+81.25€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=86 IC=+0.193 PNL=+60.93€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=86 IC=+0.193 PNL=+60.93€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 5/15 ops en el filtro definido (IC actual=+0.054 PNL=+5.10€)
  - _Datos_: n=5 IC=+0.054 PNL=+5.10€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 2/20 ops en el filtro definido (IC actual=+0.000 PNL=-0.08€)
  - _Datos_: n=2 IC=+0.000 PNL=-0.08€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=3177 IC=+0.009 PNL=+13.84€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3177 IC=+0.009 PNL=+13.84€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1552 IC=+0.001 PNL=+78.77€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1552 IC=+0.001 PNL=+78.77€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1003 IC=+0.023 PNL=+44.32€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1003 IC=+0.023 PNL=+44.32€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.173 > 0.1 con n=5006 PNL=+3059.16€
  - _Datos_: n=5006 IC=+0.173 PNL=+3059.16€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2583 IC=+0.090 PNL=+629.46€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2583 IC=+0.090 PNL=+629.46€

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
  - _Estado_: n=1025 IC=+0.035 PNL=+85.65€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1025 IC=+0.035 PNL=+85.65€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=128 IC=+0.015 PNL=+1.92€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=128 IC=+0.015 PNL=+1.92€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.275 n=171) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=171 IC=+0.275 PNL=+166.39€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.02 con n=998 PNL=+418.96€
  - _Datos_: n=998 IC=+0.125 PNL=+418.96€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=213 IC=-0.091 PNL=+19.65€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=213 IC=-0.091 PNL=+19.65€

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
  - _Estado_: n=31379 IC=+0.073 PNL=+4503.21€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=31379 IC=+0.073 PNL=+4503.21€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.138 < -0.1 con n=509 PNL=+63.28€
  - _Datos_: n=509 IC=-0.138 PNL=+63.28€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3157 IC=+0.070 PNL=+414.47€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3157 IC=+0.070 PNL=+414.47€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=150 IC=-0.099 PNL=+3.96€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=150 IC=-0.099 PNL=+3.96€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.1 con n=842 PNL=+229.17€
  - _Datos_: n=842 IC=+0.113 PNL=+229.17€

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
  - _Estado_: n=33574 IC=-0.133 PNL=+2788.88€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=33574 IC=-0.133 PNL=+2788.88€

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
  - _Estado_: n=3372 IC=+0.135 PNL=+2104.16€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3372 IC=+0.135 PNL=+2104.16€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=8166 IC=+0.052 PNL=+651.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8166 IC=+0.052 PNL=+651.26€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.095 > 0.08 con n=3591 PNL=+1975.65€
  - _Datos_: n=3591 IC=+0.095 PNL=+1975.65€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.223 < -0.1 con n=3493 PNL=-301.86€
  - _Datos_: n=3493 IC=-0.223 PNL=-301.86€

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

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=73 IC=+0.033 PNL=+10.66€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=73 IC=+0.033 PNL=+10.66€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1779) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1779 IC=+0.101 PNL=+386.39€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=579) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=579 IC=+0.410 PNL=+827.96€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=14547 IC=+0.185 PNL=-1497.96€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=14547 IC=+0.185 PNL=-1497.96€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.226 > 0.1 con n=235 PNL=+159.44€
  - _Datos_: n=235 IC=+0.226 PNL=+159.44€
