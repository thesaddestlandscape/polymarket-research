# Hipótesis automáticas — 2026-10-12 10:34 UTC
_Generado por shadow_postmortem.py sobre 864063 resoluciones (PNL=+108865.19€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=157)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=599)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.215 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.127)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.194 (n=246)

  - _Acción_: Kelly boost +0.97€ cuando `n_total_lado` > 68.0 (IC base=+0.127)

- **PATRÓN** `banda_hit_calibrado` > `0.6191` → IC=+0.256 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6191 (IC base=+0.127)

- **PATRÓN** `banda_z` > `9.322` → IC=+0.196 (n=241)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 9.322 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=246)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=774)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.127)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.217 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.133)

- **PATRÓN** `n_total_lado` > `73.0` → IC=+0.213 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 73.0 (IC base=+0.133)

- **PATRÓN** `banda_hit_calibrado` > `0.6157` → IC=+0.247 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6157 (IC base=+0.133)

- **PATRÓN** `banda_z` > `9.759` → IC=+0.221 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.759 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=676)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.133)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=115)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.126 (n=97)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=113)

- **PATRÓN** `py_entrada` > `0.705` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.705 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8019` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8019 (IC base=+0.125)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=115)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.126 (n=97)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.495 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.004)

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
- **FILTRO** `restante_s_al_confirmar` < `143.98` → IC=-0.206 (n=9172)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.98
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=27530)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.91` → IC=-0.265 (n=1106)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.91
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3318)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.47` → IC=-0.300 (n=1030)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.47
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=3091)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `166.29` → IC=-0.220 (n=2383)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 166.29
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7150)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.73` → IC=-0.297 (n=1778)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.73
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=5334)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=19366)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=4081)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `9415.8912` → IC=+0.180 (n=1826)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9415.8912 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=16201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.134 (n=19738)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=15019)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=6746)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7393.0386` → IC=+0.162 (n=2597)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7393.0386 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=1952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.197 (n=1910)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 17.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.348 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=2399)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `16156.1391` → IC=+0.208 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16156.1391 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.195 (n=1727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 7.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=1928)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=2469)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `libro_liquidez` > `16067.9503` → IC=+0.202 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16067.9503 (IC base=+0.189)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.170 (n=431)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `6926.0677` → IC=+0.167 (n=118)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 6926.0677 (IC base=+0.088)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.136 (n=1020)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.44 (IC base=+0.085)

- **PATRÓN** `libro_liquidez` > `5815.7893` → IC=+0.127 (n=239)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 5815.7893 (IC base=+0.085)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=3774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.365 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.225 (n=1671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.361 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=1946)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.217)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=939)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=805)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.260 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=732)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1510.5581` → IC=+0.149 (n=802)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1510.5581 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4420.281` → IC=+0.165 (n=150)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4420.281 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.240 (n=891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.408 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=665)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.289 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=833)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.177 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 7.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.362 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3371.7925` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3371.7925 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.229 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.795` → IC=-0.329 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.795
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=16173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=13735)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.230 (n=6786)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.199)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=3773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.177 (n=3565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.71` → IC=+0.184 (n=2679)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=1740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.228 (n=1736)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.313 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=3705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.184 (n=3542)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3797)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.187 (n=2035)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.254 (n=3236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.244)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.349 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.244)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=3629)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.190 (n=3108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.198 (n=1274)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.430 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.427)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.427 (n=630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `4010.7815` → IC=+0.438 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4010.7815 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.433 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.447 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `18155.0675` → IC=+0.438 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18155.0675 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.443 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3430.6036` → IC=+0.440 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3430.6036 (IC base=+0.431)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.405 (n=103)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.402 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.93` → IC=+0.421 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.93 (IC base=+0.402)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=24)

- **FILTRO** `libro_liquidez` < `7880.4556` → IC=-0.344 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 7880.4556
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=20775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.245 (n=21208)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=3092)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=6662)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=9260)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.227 (n=4260)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3062)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.182 (n=8751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=8850)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.178)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.234 (n=4367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.277 (n=3012)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=7995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=7940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3154)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=3454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.196 (n=3504)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=3644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.195)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=7512)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.118)

- **PATRÓN** `restante_min` < `4.2` → IC=+0.124 (n=6879)

  - _Acción_: Kelly boost +0.62€ cuando `restante_min` < 4.2 (IC base=+0.118)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=7315)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.127 (n=9167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.118)

- **PATRÓN** `lag_apertura_s` < `2.44` → IC=+0.140 (n=6888)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.44 (IC base=+0.118)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.196 (n=3718)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.121)

- **PATRÓN** `restante_min` < `4.17` → IC=+0.127 (n=3412)

  - _Acción_: Kelly boost +0.64€ cuando `restante_min` < 4.17 (IC base=+0.121)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=3684)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.95 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.135 (n=4543)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 7.0 (IC base=+0.121)

- **PATRÓN** `lag_apertura_s` < `2.92` → IC=+0.146 (n=3412)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.92 (IC base=+0.121)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=3794)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=4007)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.25` → IC=+0.139 (n=3463)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.25 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=1499)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.296 (n=1480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

- **PATRÓN** `libro_liquidez` > `4263.4949` → IC=+0.303 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4263.4949 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.296 (n=673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.286)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.356 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.286)

- **PATRÓN** `libro_liquidez` > `5350.3552` → IC=+0.315 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5350.3552 (IC base=+0.286)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.326 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.298 (n=712)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `1705.54` → IC=+0.307 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1705.54 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.351)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.377 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.351)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.351)

- **PATRÓN** `libro_spread` < `0.07` → IC=+0.356 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.07 (IC base=+0.351)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.351)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=696)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.443 (n=684)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.446 (n=329)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.441 (n=319)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.447 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.464 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.453 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.446)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.447 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.446)

- **PATRÓN** `libro_liquidez` > `2089.6231` → IC=+0.461 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2089.6231 (IC base=+0.446)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.385 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.396)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.409 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.396)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.431 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.396)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.296 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.241 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

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
- **FILTRO** `hora_utc` > `10.0` → IC=-0.296 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=55)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.241 (n=56)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=46)

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
- **PATRÓN** `drift_60min` |x|≤ `0.364` → IC=+0.138 (n=10186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.364 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.9846` → IC=+0.244 (n=3859)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9846 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.2108` → IC=+0.254 (n=2679)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2108 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.973` → IC=+0.186 (n=4367)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.973 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `1.2089` → IC=+0.252 (n=3272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2089 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` > `0.6177` → IC=+0.256 (n=3270)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6177 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` > `0.3021` → IC=+0.233 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3021 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `1.5905` → IC=+0.211 (n=3593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5905 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` > `2.3404` → IC=+0.222 (n=3701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3404 (IC base=+0.116)

- **PATRÓN** `ibs_20min` < `0.5687` → IC=+0.142 (n=14181)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5687 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.7385` → IC=+0.201 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7385 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.182 (n=5329)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.1967 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0553` → IC=+0.182 (n=2416)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0553 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2953` → IC=+0.229 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2953 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4513` → IC=+0.204 (n=9119)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4513 (IC base=+0.073)

- **PATRÓN** `ballena_activa_n` < `111.0` → IC=+0.219 (n=8942)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 111.0 (IC base=+0.073)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.214 (n=852)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.211 (n=855)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.2784` → IC=+0.190 (n=2249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.2784 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.201 (n=1237)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=1714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.9736` → IC=+0.271 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9736 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.119` → IC=+0.275 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.119 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.241 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2666` → IC=+0.201 (n=1101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2666 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=2670)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.236 (n=2095)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.244 (n=1870)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.266 (n=699)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.5048` → IC=+0.256 (n=2093)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5048 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.929` → IC=+0.234 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.929 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.237 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.251 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6474` → IC=+0.255 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6474 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.236 (n=911)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1749` → IC=+0.248 (n=1372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1749 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=2162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=2100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.9705` → IC=+0.267 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9705 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1881` → IC=+0.226 (n=1051)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1881 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.469` → IC=+0.261 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.469 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.2476` → IC=+0.223 (n=2055)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2476 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.226 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.249 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `1.5138` → IC=+0.224 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5138 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.246 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.188 (n=690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0026 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0739` → IC=+0.172 (n=686)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0739 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=782)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.7276` → IC=+0.181 (n=2057)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.7276 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.229` → IC=+0.152 (n=331)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 11.229 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.285` → IC=+0.145 (n=1882)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 4.285 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1967` → IC=+0.148 (n=2057)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1967 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.165 (n=758)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.466` → IC=+0.149 (n=1942)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.466 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4233` → IC=+0.144 (n=1941)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.4233 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `225.0` → IC=+0.180 (n=822)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 225.0 (IC base=+0.138)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.216 (n=876)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.196 (n=2761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=2349)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.342` → IC=+0.262 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.342 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.194 (n=2310)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.3485` → IC=+0.206 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3485 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.1566` → IC=+0.202 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1566 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=3098)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.227 (n=1545)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.1743` → IC=+0.229 (n=1019)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1743 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.218 (n=1084)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.0698` → IC=+0.236 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0698 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.556` → IC=+0.255 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.556 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.3458` → IC=+0.255 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3458 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.7245` → IC=+0.216 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7245 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.7242` → IC=+0.230 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7242 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.221 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.216)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=137)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=3125)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.146 (n=636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.004 (IC base=+0.050)

- **PATRÓN** `ibs_20min` > `0.9584` → IC=+0.223 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9584 (IC base=+0.050)

- **PATRÓN** `dist_vwap_pct` < `0.1829` → IC=+0.335 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1829 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.06` → IC=+0.183 (n=1019)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.06 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` < `0.8546` → IC=+0.332 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8546 (IC base=+0.050)

- **PATRÓN** `volumen_regimen` > `1.236` → IC=+0.351 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.236 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` < `0.1787` → IC=+0.325 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1787 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.342 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.364 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.050)

- **PATRÓN** `volumen_spike_ratio` > `2.2083` → IC=+0.325 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2083 (IC base=+0.050)

- **PATRÓN** `ballena_activa_n` < `149.0` → IC=+0.334 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 149.0 (IC base=+0.050)

- **PATRÓN** `ibs_20min` < `0.0992` → IC=+0.171 (n=816)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.0992 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `0.4508` → IC=+0.186 (n=269)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.4508 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.852` → IC=+0.147 (n=911)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.852 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.204 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5154` → IC=+0.158 (n=1166)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.5154 (IC base=+0.031)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=486)

- **FILTRO** `ibs_20min` > `0.2222` → IC=-0.130 (n=3149)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2222
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=1553)

- **FILTRO** `sigma_ewma_delta_pct` > `8.666` → IC=-0.228 (n=483)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.666
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=4219)

- **PATRÓN** `ibs_20min` > `0.8` → IC=+0.182 (n=196)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.8 (IC base=+0.037)

- **PATRÓN** `dist_vwap_pct` > `1.6532` → IC=+0.294 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.6532 (IC base=+0.037)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.362` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 9.362 (IC base=+0.037)

- **PATRÓN** `volumen_regimen` > `0.992` → IC=+0.281 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.992 (IC base=+0.037)

- **PATRÓN** `volumen_pendiente_norm` < `0.1539` → IC=+0.266 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1539 (IC base=+0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.1915` → IC=+0.281 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1915 (IC base=+0.037)

- **PATRÓN** `ibs_20min` < `0.2222` → IC=+0.146 (n=1553)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2222 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2566` → IC=+0.279 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2566 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.7071` → IC=+0.281 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7071 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.08` → IC=+0.302 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.08 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4034` → IC=+0.298 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4034 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6317` → IC=-0.180 (n=823)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6317
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2473)

- **FILTRO** `ibs_20min` < `0.717` → IC=-0.154 (n=2173)

  - _Acción_: SKIP cuando `ibs_20min` < 0.717
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=1123)

- **FILTRO** `ibs_20min` > `0.7628` → IC=-0.205 (n=1224)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7628
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=3677)

- **PATRÓN** `dist_vwap_pct` > `0.7008` → IC=+0.320 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7008 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2576` → IC=+0.307 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2576 (IC base=-0.074)

- **PATRÓN** `volumen_regimen` < `1.0034` → IC=+0.299 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0034 (IC base=-0.074)

- **PATRÓN** `volumen_regimen` > `0.6377` → IC=+0.308 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6377 (IC base=-0.074)

- **PATRÓN** `volumen_pendiente_norm` < `0.1052` → IC=+0.303 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1052 (IC base=-0.074)

- **PATRÓN** `volumen_spike_ratio` < `2.5248` → IC=+0.298 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5248 (IC base=-0.074)

- **PATRÓN** `volumen_spike_ratio` > `1.8742` → IC=+0.305 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8742 (IC base=-0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7916` → IC=+0.279 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7916 (IC base=-0.010)

- **PATRÓN** `volumen_regimen` > `1.0812` → IC=+0.279 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0812 (IC base=-0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.1045` → IC=+0.282 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1045 (IC base=-0.010)

- **PATRÓN** `volumen_spike_ratio` < `2.1865` → IC=+0.258 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1865 (IC base=-0.010)

- **PATRÓN** `volumen_spike_ratio` > `1.5509` → IC=+0.262 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5509 (IC base=-0.010)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.204 (n=5095)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.4601` → IC=+0.186 (n=13641)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4601 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.65` → IC=+0.280 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.65 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.662` → IC=+0.156 (n=6857)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.662 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.1748` → IC=+0.252 (n=5606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1748 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6892` → IC=+0.259 (n=5008)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6892 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2402` → IC=+0.267 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2402 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` < `1.4634` → IC=+0.249 (n=3003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4634 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.6413` → IC=+0.263 (n=3002)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6413 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.283 (n=8570)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.159 (n=4901)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0089 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.5402` → IC=+0.159 (n=12926)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.5402 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.8763` → IC=+0.254 (n=3019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8763 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1973` → IC=+0.261 (n=1509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1973 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.309 (n=934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5881` → IC=+0.282 (n=2803)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5881 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2867` → IC=+0.275 (n=2887)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2867 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `78.0` → IC=+0.286 (n=6269)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 78.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3731` → IC=-0.157 (n=1394)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3731
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=2831)

- **FILTRO** `ibs_20min` > `0.7572` → IC=-0.192 (n=869)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7572
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2610)

- **FILTRO** `sigma_ewma_delta_pct` > `4.57` → IC=-0.189 (n=766)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.57
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2713)

- **PATRÓN** `ibs_20min` > `0.9137` → IC=+0.287 (n=1057)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9137 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.205` → IC=+0.205 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.205 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.2299` → IC=+0.293 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2299 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.220 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` > `2.2336` → IC=+0.255 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2336 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.251 (n=950)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.036)

- **PATRÓN** `ibs_20min` < `0.1596` → IC=+0.149 (n=870)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1596 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0774` → IC=+0.425 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0774 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.5496` → IC=+0.413 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5496 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` > `1.5561` → IC=+0.406 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5561 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.410 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `ibs_20min` > `0.8585` → IC=+0.144 (n=1039)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.8585 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.1106` → IC=+0.195 (n=785)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1106 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6787` → IC=+0.184 (n=1320)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 0.6787 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2745` → IC=+0.219 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2745 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.4243` → IC=+0.200 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4243 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.4708` → IC=+0.192 (n=485)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4708 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `222.0` → IC=+0.227 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 222.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1041` → IC=+0.232 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1041 (IC base=+0.002)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.235 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.0739` → IC=+0.227 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0739 (IC base=+0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.273` → IC=+0.298 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.273 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.5571` → IC=+0.230 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5571 (IC base=+0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1954` → IC=+0.251 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1954 (IC base=+0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.281 (n=2036)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.262 (n=2282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.258 (n=2040)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1183)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.288 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.1318` → IC=+0.269 (n=2077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1318 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.165` → IC=+0.266 (n=1459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.165 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.268 (n=2674)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.305 (n=1923)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.1777` → IC=+0.305 (n=846)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1777 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.323 (n=737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.3644` → IC=+0.294 (n=1922)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3644 (IC base=+0.290)

- **PATRÓN** `ibs_20min` > `0.1071` → IC=+0.292 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1071 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.687` → IC=+0.304 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.687 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.1948` → IC=+0.288 (n=1867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1948 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.3387` → IC=+0.303 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3387 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.57` → IC=+0.303 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.57 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` > `2.1041` → IC=+0.291 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1041 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.292 (n=1591)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.290)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7556` → IC=-0.183 (n=901)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7556
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=2705)

- **PATRÓN** `ibs_20min` > `0.8942` → IC=+0.168 (n=842)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8942 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.2026` → IC=+0.228 (n=960)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2026 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0163` → IC=+0.237 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0163 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6696` → IC=+0.220 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6696 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.240 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4012` → IC=+0.260 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4012 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.257 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 109.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1234` → IC=+0.217 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1234 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.041` → IC=+0.231 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.041 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1038` → IC=+0.238 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1038 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.282 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.8295` → IC=+0.264 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8295 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.5` → IC=+0.247 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.252 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 129.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7639` → IC=-0.198 (n=1616)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7639
  - _Potencial_: sin este filtro IC_bueno=+0.294 (n=1617)

- **FILTRO** `ibs_20min` > `0.6612` → IC=-0.237 (n=803)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6612
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=2412)

- **FILTRO** `sigma_ewma_delta_pct` > `8.591` → IC=-0.230 (n=365)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.591
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=2850)

- **PATRÓN** `ibs_20min` > `0.7639` → IC=+0.294 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7639 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.2084` → IC=+0.328 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2084 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.64` → IC=+0.167 (n=502)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.64 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.8519` → IC=+0.320 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8519 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `0.6339` → IC=+0.314 (n=1227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6339 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.309 (n=1156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.344 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.7961` → IC=+0.323 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7961 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.336 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.137 (n=2122)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.5556 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `0.7045` → IC=+0.260 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7045 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.236 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.247 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4243` → IC=+0.251 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4243 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.268 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 54.0 (IC base=+0.026)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.338 (n=1574)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.309 (n=836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.294)

- **PATRÓN** `ibs_20min` > `0.65` → IC=+0.325 (n=1763)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.65 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2123` → IC=+0.321 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2123 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.787` → IC=+0.316 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.787 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.926` → IC=+0.294 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.926 (IC base=+0.294)

- **PATRÓN** `volumen_regimen` > `0.6248` → IC=+0.305 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6248 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` > `0.2824` → IC=+0.341 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2824 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.306 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `2995.3274` → IC=+0.317 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2995.3274 (IC base=+0.294)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.329 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 43.0 (IC base=+0.294)

- **PATRÓN** `sigma_h` > `0.015` → IC=+0.326 (n=1243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.015 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.1854` → IC=+0.294 (n=820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1854 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.297 (n=1769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.294)

- **PATRÓN** `ibs_20min` < `0.3696` → IC=+0.320 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3696 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.3041` → IC=+0.294 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3041 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.516` → IC=+0.305 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.516 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.036` → IC=+0.294 (n=2226)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.036 (IC base=+0.294)

- **PATRÓN** `volumen_regimen` > `1.2298` → IC=+0.325 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2298 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.342 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` < `1.4194` → IC=+0.301 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4194 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` > `2.1432` → IC=+0.297 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1432 (IC base=+0.294)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.186 (n=3765)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0047 (IC base=+0.177)

- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.218 (n=3756)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3444` → IC=+0.188 (n=9908)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3444 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=11734)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.5632` → IC=+0.230 (n=11259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5632 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.1633` → IC=+0.203 (n=4712)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1633 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.37` → IC=+0.254 (n=2246)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.37 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1991` → IC=+0.168 (n=7467)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1991 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` > `0.6273` → IC=+0.163 (n=7468)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6273 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.198 (n=1657)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `1.4525` → IC=+0.175 (n=3630)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.4525 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6089` → IC=+0.186 (n=3631)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6089 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `2525.3252` → IC=+0.180 (n=7506)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2525.3252 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.193 (n=10174)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 100.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.187 (n=7180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0067 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0791` → IC=+0.225 (n=3589)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0791 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=4029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.4942` → IC=+0.234 (n=10760)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4942 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.185` → IC=+0.195 (n=1784)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 10.185 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.166 (n=7694)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1817 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.224 (n=1587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6243` → IC=+0.183 (n=3346)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6243 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.193 (n=8574)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 68.0 (IC base=+0.177)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.234 (n=633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.224 (n=631)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.225 (n=1893)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.211 (n=1997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.208 (n=1274)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.9196` → IC=+0.286 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9196 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.18` → IC=+0.334 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.18 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.263 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `1.44` → IC=+0.204 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.44 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.215 (n=1992)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.245 (n=1278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.251 (n=1297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0691` → IC=+0.301 (n=485)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0691 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=1302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=722)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.2667` → IC=+0.265 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2667 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.134` → IC=+0.246 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.134 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.242 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.278 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4252` → IC=+0.256 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4252 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.6473` → IC=+0.249 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6473 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.246 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `2015.1048` → IC=+0.244 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2015.1048 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.239 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.242)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.220 (n=565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1598` → IC=+0.187 (n=1126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1598 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.179 (n=1781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.367` → IC=+0.224 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.367 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.1353` → IC=+0.209 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1353 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.501` → IC=+0.230 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.501 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6892` → IC=+0.169 (n=743)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6892 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.0731` → IC=+0.159 (n=766)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.0731 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.186 (n=269)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.181 (n=550)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.5038` → IC=+0.158 (n=550)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5038 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `426.0` → IC=+0.162 (n=1611)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 426.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.166 (n=1769)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0056 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.2293` → IC=+0.175 (n=1557)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2293 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6038` → IC=+0.205 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6038 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.719` → IC=+0.205 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.719 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.166 (n=1769)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.204 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0946` → IC=+0.146 (n=1483)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0946 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.1596` → IC=+0.150 (n=544)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.1596 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.4999` → IC=+0.154 (n=1652)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.4999 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `1.781` → IC=+0.148 (n=1101)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.781 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `206.0` → IC=+0.172 (n=526)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 206.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.234 (n=863)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.3998` → IC=+0.221 (n=1673)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3998 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.215 (n=1982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=992)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.494` → IC=+0.288 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.494 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3513` → IC=+0.218 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3513 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.7707` → IC=+0.216 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7707 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.6973` → IC=+0.218 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6973 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=2239)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.246 (n=1422)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.5589` → IC=+0.245 (n=1615)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5589 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.3529` → IC=+0.252 (n=1616)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3529 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.641` → IC=+0.267 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.641 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.3507` → IC=+0.270 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3507 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.7192` → IC=+0.243 (n=675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7192 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `2.7242` → IC=+0.236 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7242 (IC base=+0.231)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.233 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.231)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.184 (n=1594)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0063 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0756` → IC=+0.200 (n=604)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0756 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=1886)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` > `0.3204` → IC=+0.210 (n=1810)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3204 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.1362` → IC=+0.190 (n=1140)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1362 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.979` → IC=+0.209 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.979 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.163 (n=1207)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8561 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` > `0.1015` → IC=+0.177 (n=747)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1015 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `1.4265` → IC=+0.162 (n=592)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4265 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.168 (n=592)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `5059.0224` → IC=+0.200 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5059.0224 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `146.0` → IC=+0.160 (n=1755)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 146.0 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.156 (n=1898)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.007 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.3806` → IC=+0.146 (n=1898)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3806 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` < `0.6818` → IC=+0.188 (n=1898)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6818 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.869` → IC=+0.153 (n=664)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.869 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8571` → IC=+0.162 (n=1266)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8571 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.190 (n=288)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.808` → IC=+0.132 (n=1178)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.808 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `1.4141` → IC=+0.131 (n=1766)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.4141 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `4507.0902` → IC=+0.172 (n=1265)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4507.0902 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.128 (n=1507)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 122.0 (IC base=+0.127)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.168 (n=933)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0099 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.5601` → IC=+0.128 (n=2059)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.5601 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=2104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.5` → IC=+0.214 (n=2060)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1914` → IC=+0.188 (n=1230)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1914 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.71` → IC=+0.265 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.71 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1928` → IC=+0.140 (n=2059)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1928 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `0.7154` → IC=+0.127 (n=1839)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.7154 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.136 (n=2081)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4403` → IC=+0.140 (n=665)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4403 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=2135)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2895.2022` → IC=+0.210 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2895.2022 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.160 (n=645)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 21.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.143 (n=1833)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0091 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1032` → IC=+0.170 (n=695)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1032 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2105)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.218 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.7332` → IC=+0.129 (n=356)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.7332 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.558` → IC=+0.125 (n=422)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 7.558 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1776` → IC=+0.132 (n=2083)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1776 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2745` → IC=+0.151 (n=270)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2745 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4534` → IC=+0.138 (n=641)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4534 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4388` → IC=+0.127 (n=641)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4388 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2755.5964` → IC=+0.191 (n=944)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2755.5964 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.128 (n=1894)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 51.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.237 (n=1708)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.2828` → IC=+0.224 (n=1274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2828 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.219 (n=1984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=1293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.6533` → IC=+0.252 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6533 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.1876` → IC=+0.218 (n=1268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1876 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.216 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2672 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.247 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `1.0265` → IC=+0.216 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0265 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `0.6192` → IC=+0.222 (n=1911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6192 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2335` → IC=+0.264 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2335 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `2.4913` → IC=+0.219 (n=1858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4913 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.8141` → IC=+0.230 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8141 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2668.1484` → IC=+0.227 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2668.1484 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0095` → IC=+0.233 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0095 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0224` → IC=+0.229 (n=883)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0224 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.254 (n=649)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.225 (n=892)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` < `0.4231` → IC=+0.256 (n=1946)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4231 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `1.1311` → IC=+0.237 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1311 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.355` → IC=+0.253 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.355 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6385` → IC=+0.234 (n=1946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6385 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.284 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.4397` → IC=+0.226 (n=1798)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4397 (IC base=+0.225)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.208 (n=978)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.3303` → IC=+0.183 (n=2578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.3303 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.203 (n=1454)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.4871` → IC=+0.206 (n=2617)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4871 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.361` → IC=+0.179 (n=864)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.361 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.691` → IC=+0.198 (n=1254)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 3.691 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `1.0582` → IC=+0.182 (n=2313)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.0582 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.174 (n=2348)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 0.6955 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1019` → IC=+0.183 (n=1055)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.1019 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.189 (n=949)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.522` → IC=+0.173 (n=949)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.522 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.174 (n=3338)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.02 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `2775.0073` → IC=+0.177 (n=2617)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2775.0073 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `151.0` → IC=+0.184 (n=2710)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 151.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.143 (n=1013)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0036 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.0826` → IC=+0.195 (n=1006)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.0826 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `1.4323` → IC=+0.136 (n=976)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4323 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `4461.2314` → IC=+0.132 (n=2008)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 4461.2314 (IC base=+0.106)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.132 (n=1259)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 29.0 (IC base=+0.106)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.207 (n=370)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.160)

- **PATRÓN** `drift_60min` |x|≤ `0.099` → IC=+0.214 (n=369)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.099 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.160)

- **PATRÓN** `ibs_20min` > `0.6402` → IC=+0.215 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6402 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.2999` → IC=+0.180 (n=264)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.2999 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.092` → IC=+0.185 (n=360)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 3.092 (IC base=+0.160)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.189 (n=560)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.8753 (IC base=+0.160)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.171 (n=329)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` < `2.2256` → IC=+0.168 (n=723)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` < 2.2256 (IC base=+0.160)

- **PATRÓN** `volumen_spike_ratio` > `1.417` → IC=+0.162 (n=821)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.417 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `14746.216` → IC=+0.170 (n=559)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 14746.216 (IC base=+0.160)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.200 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.160)

- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.190 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0027 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.2647` → IC=+0.149 (n=852)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.2647 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.146 (n=871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6202` → IC=+0.178 (n=852)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.6202 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.74` → IC=+0.138 (n=186)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 8.74 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.177` → IC=+0.142 (n=878)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.177 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.2004` → IC=+0.139 (n=968)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2004 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `0.7005` → IC=+0.148 (n=865)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 0.7005 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.0696` → IC=+0.176 (n=381)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.0696 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.152 (n=842)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=1255)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `358.0` → IC=+0.150 (n=936)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 358.0 (IC base=+0.137)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.247 (n=611)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.2006` → IC=+0.224 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2006 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.6787` → IC=+0.264 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6787 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.3552` → IC=+0.210 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3552 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.2052` → IC=+0.210 (n=827)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2052 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.951` → IC=+0.224 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.951 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.8363` → IC=+0.211 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8363 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.1816` → IC=+0.223 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1816 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` > `0.1588` → IC=+0.237 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1588 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `1.4109` → IC=+0.246 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4109 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` > `2.4387` → IC=+0.223 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4387 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.127 (n=395)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0037 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.0933` → IC=+0.168 (n=299)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0933 (IC base=+0.090)

- **PATRÓN** `libro_liquidez` > `3973.2352` → IC=+0.127 (n=799)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 3973.2352 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.128 (n=382)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 43.0 (IC base=+0.090)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.150 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0075 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.149 (n=311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0091 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.5315` → IC=+0.145 (n=685)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.5315 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.174 (n=614)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 8.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.264 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.6865` → IC=+0.188 (n=171)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6865 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.207 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0604` → IC=+0.163 (n=603)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.0604 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6538` → IC=+0.154 (n=685)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 0.6538 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2809` → IC=+0.173 (n=102)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2809 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4594` → IC=+0.146 (n=221)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4594 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.2007` → IC=+0.159 (n=300)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.2007 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.151 (n=711)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3082.2108` → IC=+0.193 (n=229)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3082.2108 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.475` → IC=+0.156 (n=585)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.475 (IC base=+0.068)

- **PATRÓN** `volumen_spike_ratio` < `1.4645` → IC=+0.140 (n=212)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4645 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `2858.4736` → IC=+0.157 (n=301)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2858.4736 (IC base=+0.068)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.121 (n=534)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 32.0 (IC base=+0.068)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0238` → IC=+0.170 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0238 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.186 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.007 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.167 (n=169)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.204 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.184 (n=172)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5556 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.2393` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2393 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `1.115` → IC=+0.162 (n=214)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 1.115 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.181 (n=164)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.175 (n=192)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.6182 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` < `0.2537` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.2537 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `2503.8283` → IC=+0.169 (n=128)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2503.8283 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.158 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0117 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.134 (n=214)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.61 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1597` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1597 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.009` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.009 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `1.2382` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.2382 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 17.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.179 (n=4886)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0046 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.220 (n=4885)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=15303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5594` → IC=+0.238 (n=13084)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5594 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1591` → IC=+0.188 (n=5374)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1591 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.348` → IC=+0.251 (n=3605)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.348 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8782` → IC=+0.174 (n=6540)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.8782 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.203 (n=1967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6105` → IC=+0.195 (n=4736)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6105 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2497.8056` → IC=+0.185 (n=9764)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2497.8056 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.204 (n=11698)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.194 (n=5822)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0053 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1441` → IC=+0.196 (n=5809)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1441 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=4916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5769` → IC=+0.242 (n=13198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5769 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.987` → IC=+0.208 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.987 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.677` → IC=+0.190 (n=12734)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.677 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.7048` → IC=+0.164 (n=3922)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.7048 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2896` → IC=+0.251 (n=1782)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2896 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6171` → IC=+0.199 (n=4134)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6171 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.213 (n=8095)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.243 (n=805)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.214)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.245 (n=803)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=1162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.217 (n=1624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.664` → IC=+0.349 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.664 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2754` → IC=+0.275 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2754 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.2534` → IC=+0.227 (n=1045)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2534 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=2500)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.229 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.262 (n=2022)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.259)

- **PATRÓN** `sigma_h` > `0.0044` → IC=+0.265 (n=2025)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0044 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.2026` → IC=+0.271 (n=1348)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2026 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.266 (n=1830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.494` → IC=+0.284 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.494 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.523` → IC=+0.262 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.523 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.1574` → IC=+0.258 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1574 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2846` → IC=+0.280 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2846 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6427` → IC=+0.279 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6427 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.201 (n=786)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.175` → IC=+0.169 (n=1568)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.175 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.2711` → IC=+0.208 (n=2350)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2711 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.124` → IC=+0.192 (n=1283)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.124 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.703` → IC=+0.167 (n=394)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.703 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.184` → IC=+0.155 (n=2141)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.184 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.176 (n=785)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6288 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0723` → IC=+0.153 (n=2090)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0723 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.180 (n=339)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1781` → IC=+0.160 (n=2017)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1781 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5329` → IC=+0.153 (n=2047)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5329 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `269.0` → IC=+0.182 (n=983)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 269.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.195 (n=654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0026 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.184 (n=650)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6963` → IC=+0.200 (n=1948)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6963 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.479` → IC=+0.159 (n=329)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.479 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.1838` → IC=+0.160 (n=1948)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.1838 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1542` → IC=+0.193 (n=523)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1542 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.154 (n=1846)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.442 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.7866` → IC=+0.163 (n=1231)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.7866 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `253.0` → IC=+0.147 (n=588)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 253.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.249 (n=810)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=917)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.405` → IC=+0.310 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.405 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.224 (n=2134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.7686` → IC=+0.228 (n=2100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7686 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2862)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.245 (n=1510)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.240)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.241 (n=2021)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1782` → IC=+0.259 (n=996)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1782 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0198` → IC=+0.303 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0198 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.079` → IC=+0.290 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.079 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3417` → IC=+0.299 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3417 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.723` → IC=+0.239 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.723 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1336` → IC=+0.248 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1336 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.262 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.186 (n=1679)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0049 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.325` → IC=+0.156 (n=2208)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.325 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2615)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.2654` → IC=+0.193 (n=2509)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2654 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.5319` → IC=+0.169 (n=644)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.5319 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.195` → IC=+0.165 (n=1024)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 4.195 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8732` → IC=+0.164 (n=1673)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8732 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2831` → IC=+0.181 (n=334)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2831 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.172 (n=1077)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5223 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1724` → IC=+0.159 (n=1109)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1724 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `7183.8819` → IC=+0.239 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7183.8819 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.171 (n=1069)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 79.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.196 (n=683)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0032 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3362` → IC=+0.140 (n=1801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3362 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7429` → IC=+0.188 (n=2046)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.7429 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.332` → IC=+0.169 (n=418)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.332 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8749` → IC=+0.141 (n=1364)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8749 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.228 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.141 (n=1962)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `5332.0555` → IC=+0.204 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5332.0555 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.143 (n=1689)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.008 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4485` → IC=+0.199 (n=2533)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4485 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.0085` → IC=+0.205 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0085 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.919` → IC=+0.263 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.919 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.8883` → IC=+0.146 (n=1689)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8883 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1625` → IC=+0.126 (n=2622)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1625 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2808` → IC=+0.136 (n=330)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2808 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `2.4798` → IC=+0.123 (n=2470)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4798 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.4667` → IC=+0.128 (n=2469)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4667 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2578)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2916.8993` → IC=+0.252 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2916.8993 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.137 (n=799)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 26.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.143 (n=2405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0108 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.1292` → IC=+0.163 (n=801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1292 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.157 (n=1121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 15.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6364` → IC=+0.213 (n=2403)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6364 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.394` → IC=+0.134 (n=2311)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.394 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.7128` → IC=+0.148 (n=1057)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.7128 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2225` → IC=+0.168 (n=399)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2225 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4366` → IC=+0.157 (n=744)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4366 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2793.7543` → IC=+0.206 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2793.7543 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.138 (n=1969)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 49.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.240 (n=2160)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0133 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2525)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.228 (n=1749)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.605` → IC=+0.268 (n=2160)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.605 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1948` → IC=+0.236 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1948 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.264 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.2323` → IC=+0.228 (n=2418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2323 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6387` → IC=+0.224 (n=2418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6387 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2377` → IC=+0.251 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2377 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.5212` → IC=+0.249 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5212 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.226 (n=2110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2674.5374` → IC=+0.237 (n=1612)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2674.5374 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.225 (n=840)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.223)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.242 (n=1142)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.231 (n=2360)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.262 (n=2520)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.169` → IC=+0.256 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.169 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `1.2323` → IC=+0.254 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2323 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2822` → IC=+0.294 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2822 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.4366` → IC=+0.228 (n=2325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4366 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2662.0286` → IC=+0.223 (n=1679)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2662.0286 (IC base=+0.223)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=4330)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.235 (n=1475)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.196)

- **PATRÓN** `drift_60min` |x|≤ `0.4948` → IC=+0.206 (n=4416)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4948 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=1606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.197 (n=3054)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 11.0 (IC base=+0.196)

- **PATRÓN** `ibs_20min` > `0.9412` → IC=+0.245 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9412 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` > `0.1653` → IC=+0.201 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1653 (IC base=+0.196)

- **PATRÓN** `dist_vwap_pct` < `0.2349` → IC=+0.198 (n=2733)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2349 (IC base=+0.196)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.187` → IC=+0.213 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.187 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` < `0.7085` → IC=+0.209 (n=1394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7085 (IC base=+0.196)

- **PATRÓN** `volumen_regimen` > `0.8916` → IC=+0.200 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8916 (IC base=+0.196)

- **PATRÓN** `volumen_pendiente_norm` > `0.1673` → IC=+0.219 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1673 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` < `1.4558` → IC=+0.204 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4558 (IC base=+0.196)

- **PATRÓN** `volumen_spike_ratio` > `2.2773` → IC=+0.201 (n=1972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2773 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=3324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `libro_liquidez` > `2979.398` → IC=+0.207 (n=3945)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2979.398 (IC base=+0.196)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.227 (n=1091)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.4846` → IC=+0.196 (n=3259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4846 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=1106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.196 (n=2195)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 10.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` < `0.1814` → IC=+0.199 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1814 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.6337` → IC=+0.189 (n=571)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6337 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.881` → IC=+0.186 (n=2751)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 2.881 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.1036` → IC=+0.191 (n=2698)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.1036 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.185 (n=2973)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.184 (n=1487)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.5357` → IC=+0.186 (n=1415)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.5357 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `1.8199` → IC=+0.188 (n=2143)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.8199 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=4330)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.193 (n=2131)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 69.0 (IC base=+0.180)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.250 (n=498)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.0804` → IC=+0.275 (n=189)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0804 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.228 (n=413)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` < `0.2763` → IC=+0.261 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2763 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.7622` → IC=+0.226 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7622 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.3151` → IC=+0.235 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3151 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.102` → IC=+0.239 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.102 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.584` → IC=+0.227 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.584 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.234 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.85` → IC=+0.244 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.85 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.322 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.5576` → IC=+0.237 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5576 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `12467.3842` → IC=+0.246 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12467.3842 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.237 (n=489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.158)

- **PATRÓN** `drift_60min` |x|≤ `0.3655` → IC=+0.172 (n=1107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.3655 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=409)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.188 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 5.0 (IC base=+0.158)

- **PATRÓN** `ibs_20min` < `0.1561` → IC=+0.189 (n=487)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.1561 (IC base=+0.158)

- **PATRÓN** `ibs_20min` > `0.6081` → IC=+0.161 (n=502)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.6081 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `0.6609` → IC=+0.188 (n=110)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6609 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` < `0.1554` → IC=+0.159 (n=1081)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.1554 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.172` → IC=+0.170 (n=1212)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 9.172 (IC base=+0.158)

- **PATRÓN** `volumen_regimen` < `0.8817` → IC=+0.196 (n=738)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8817 (IC base=+0.158)

- **PATRÓN** `volumen_pendiente_norm` > `0.2216` → IC=+0.192 (n=232)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2216 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` < `2.5318` → IC=+0.163 (n=1103)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.5318 (IC base=+0.158)

- **PATRÓN** `volumen_spike_ratio` > `1.8156` → IC=+0.176 (n=735)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.8156 (IC base=+0.158)

- **PATRÓN** `libro_liquidez` > `11518.9437` → IC=+0.171 (n=1107)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 11518.9437 (IC base=+0.158)

- **PATRÓN** `ballena_activa_n` < `700.0` → IC=+0.171 (n=1061)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 700.0 (IC base=+0.158)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.201 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.185 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0098 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.4284` → IC=+0.176 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.4284 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.51` → IC=+0.217 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.51 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2084` → IC=+0.226 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2084 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `3.3854` → IC=+0.184 (n=232)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 3.3854 (IC base=+0.172)

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

- **PATRÓN** `volumen_pendiente_norm` < `0.2021` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2021 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4518` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4518 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.861` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.861 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2407.5596` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.5596 (IC base=+0.227)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.216 (n=1290)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4566` → IC=+0.208 (n=1290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4566 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.5211` → IC=+0.215 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5211 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.8798` → IC=+0.208 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8798 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.12` → IC=+0.209 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.12 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.8843` → IC=+0.206 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8843 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2448` → IC=+0.211 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2448 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.204 (n=1189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.1639` → IC=+0.207 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1639 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `1.4177` → IC=+0.221 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4177 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.242 (n=347)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.4878` → IC=+0.202 (n=1035)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4878 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.190 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 16.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.192 (n=705)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 10.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.7579` → IC=+0.182 (n=1035)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.7579 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.087` → IC=+0.180 (n=1035)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.087 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.6242` → IC=+0.197 (n=196)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6242 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.719` → IC=+0.181 (n=1059)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 6.719 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2459` → IC=+0.191 (n=1035)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.2459 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `0.7208` → IC=+0.177 (n=924)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` > 0.7208 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.197 (n=437)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `2.1843` → IC=+0.190 (n=892)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.1843 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `1.7774` → IC=+0.179 (n=675)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.7774 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `7344.2404` → IC=+0.190 (n=1035)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7344.2404 (IC base=+0.176)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.225 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.2895` → IC=+0.170 (n=416)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.2895 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.199 (n=593)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.250 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.2488` → IC=+0.201 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2488 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.252` → IC=+0.217 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.252 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `0.7034` → IC=+0.206 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7034 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` < `0.1079` → IC=+0.174 (n=562)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.1079 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.1633` → IC=+0.191 (n=189)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1633 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `2.5465` → IC=+0.206 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5465 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.175 (n=718)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.02 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `3205.049` → IC=+0.196 (n=557)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3205.049 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `54.0` → IC=+0.184 (n=605)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 54.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.217 (n=203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.3574` → IC=+0.228 (n=299)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3574 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.223 (n=305)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.245 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.758` → IC=+0.213 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.758 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.952` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.952 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.848` → IC=+0.194 (n=393)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.848 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `0.758` → IC=+0.214 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.758 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.1095` → IC=+0.228 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1095 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.626` → IC=+0.201 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.626 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.214 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `3138.4241` → IC=+0.219 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3138.4241 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.230 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.192)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.157 (n=636)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.072)

- **PATRÓN** `ibs_20min` > `0.4159` → IC=+0.147 (n=1353)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.4159 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` > `0.1382` → IC=+0.138 (n=725)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1382 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.442` → IC=+0.185 (n=303)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.442 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2792` → IC=+0.158 (n=182)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2792 (IC base=+0.072)

- **PATRÓN** `ibs_20min` < `0.1925` → IC=+0.248 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1925 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.0861` → IC=+0.125 (n=625)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.0861 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.188 (n=168)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.4804` → IC=+0.125 (n=254)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.4804 (IC base=+0.057)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.138 (n=490)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0056 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.137 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 18.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.3752` → IC=+0.168 (n=459)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3752 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.119` → IC=+0.158 (n=241)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.119 (IC base=+0.092)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.125 (n=214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0034 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.282 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.1051` → IC=+0.130 (n=301)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.1051 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.652` → IC=+0.130 (n=255)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 4.652 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.0753` → IC=+0.150 (n=121)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0753 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` < `2.5724` → IC=+0.122 (n=273)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.5724 (IC base=+0.077)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.156 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0046 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.6741` → IC=+0.210 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6741 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.181 (n=236)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.658` → IC=+0.270 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.658 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.8183` → IC=+0.122 (n=294)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_regimen` < 0.8183 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `1727.3747` → IC=+0.149 (n=146)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1727.3747 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.106` → IC=+0.259 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.106 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.103` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 11.103 (IC base=+0.009)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1333` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1333
  - _Potencial_: sin este filtro IC_bueno=+0.253 (n=152)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.158 (n=314)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.75 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.968` → IC=+0.136 (n=127)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 7.968 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2436` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2436 (IC base=+0.030)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.160 (n=183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0092 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.1333` → IC=+0.253 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1333 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1353` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1353 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.3347` → IC=+0.169 (n=167)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.3347 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.757` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.757 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6683` → IC=+0.138 (n=67)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6683 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0544` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0544 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `1.8779` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8779 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `788.7958` → IC=+0.177 (n=91)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 788.7958 (IC base=+0.075)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.328 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=219)

- **FILTRO** `dist_vwap_pct` > `0.2348` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2348
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=264)

- **FILTRO** `volumen_regimen` < `0.7615` → IC=-0.333 (n=70)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7615
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=211)

- **FILTRO** `sigma_h` > `0.0053` → IC=-0.381 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=175)

- **FILTRO** `drift_60min` |x|> `0.1969` → IC=-0.310 (n=56)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1969
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=170)

- **FILTRO** `dist_vwap_pct` > `0.3328` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3328
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=199)

- **FILTRO** `sigma_ewma_delta_pct` > `10.779` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.779
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=209)

- **FILTRO** `volumen_pendiente_norm` > `0.0549` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0549
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=121)

- **FILTRO** `libro_liquidez` < `1272.5864` → IC=-0.300 (n=58)

  - _Acción_: SKIP cuando `libro_liquidez` < 1272.5864
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=174)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.266 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=48)

- **FILTRO** `ibs_20min` < `0.1017` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1017
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=63)

- **FILTRO** `volumen_regimen` < `0.8417` → IC=-0.300 (n=23)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8417
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=70)

- **FILTRO** `volumen_spike_ratio` > `3.5274` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 3.5274
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=53)

- **FILTRO** `sigma_h` < `0.002` → IC=-0.315 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.002
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=76)

- **FILTRO** `volumen_spike_ratio` > `1.5538` → IC=-0.329 (n=33)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5538
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=35)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` < `0.0025` → IC=-0.340 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0025
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=72)

- **FILTRO** `ibs_20min` < `0.6398` → IC=-0.439 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6398
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=64)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.350 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=68)

- **FILTRO** `dist_vwap_pct` > `0.1182` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1182
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=58)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=36)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=56)

- **PATRÓN** `ibs_20min` > `0.9508` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.9508 (IC base=-0.160)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=77)

- **FILTRO** `volumen_spike_ratio` < `1.5847` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5847
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=51)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.225 (n=67)

- **FILTRO** `dist_vwap_pct` < `0.219` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.219
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=21)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.170 (n=207)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0057 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=478)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.106)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.149 (n=454)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6757 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.4828` → IC=+0.207 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4828 (IC base=+0.106)

- **PATRÓN** `volumen_regimen` < `0.66` → IC=+0.156 (n=152)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.66 (IC base=+0.106)

- **PATRÓN** `volumen_pendiente_norm` < `0.2347` → IC=+0.140 (n=392)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.2347 (IC base=+0.106)

- **PATRÓN** `volumen_spike_ratio` < `2.5471` → IC=+0.138 (n=352)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.5471 (IC base=+0.106)

- **PATRÓN** `ibs_20min` < `0.1628` → IC=+0.165 (n=461)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1628 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.19` → IC=+0.192 (n=128)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.19 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `2938.1704` → IC=+0.155 (n=349)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2938.1704 (IC base=+0.070)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.228 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.167 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 12.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.1361` → IC=+0.203 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1361 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.2133` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.2133 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.0895` → IC=+0.158 (n=241)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.0895 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.253` → IC=+0.175 (n=75)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.253 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.645` → IC=+0.167 (n=187)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 4.645 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` > `0.6754` → IC=+0.168 (n=212)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6754 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0813` → IC=+0.179 (n=182)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.0813 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.2594` → IC=+0.172 (n=181)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.2594 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.162 (n=205)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `5151.5741` → IC=+0.163 (n=158)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5151.5741 (IC base=+0.150)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.2375` → IC=-0.126 (n=89)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2375
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=174)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.139 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0045 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.161 (n=57)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.7141` → IC=+0.132 (n=161)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.7141 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.139 (n=120)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` < `0.1363` → IC=+0.127 (n=148)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1363 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `1.7926` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.7926 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `1868.6989` → IC=+0.124 (n=107)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1868.6989 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.2375` → IC=+0.125 (n=174)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.2375 (IC base=+0.040)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.255 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.2221` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2221 (IC base=+0.040)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.1679` → IC=-0.221 (n=59)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1679
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=61)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.302 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.270 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.6434` → IC=+0.375 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6434 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` < `0.2189` → IC=+0.242 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2189 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.333` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.333 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.294 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.2516` → IC=+0.296 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2516 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.246 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `665.8128` → IC=+0.245 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 665.8128 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.074)

### LATE_WINDOW_5MIN
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.352 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1245.0` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1245.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.216)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.216)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.216)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.269 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.216)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.216)

### LATE_WINDOW_5MIN#BTC#5min
- **PATRÓN** `drift_ventana_pct` |x|> `0.332` → IC=+0.296 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.332 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.450 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.352 (n=52)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1245.0` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1245.0 (IC base=+0.289)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3418` → IC=+0.250 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3418 (IC base=+0.216)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.216)

- **PATRÓN** `elapsed_s` < `214.1` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 214.1 (IC base=+0.216)

- **PATRÓN** `drift_15min` |x|≤ `1.2534` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2534 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.269 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.216)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.216)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=168)

- **FILTRO** `libro_liquidez` < `2696.1504` → IC=-0.229 (n=46)

  - _Acción_: SKIP cuando `libro_liquidez` < 2696.1504
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=138)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=246)

- **FILTRO** `py_entrada` > `0.515` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=232)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=60)

- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=60)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.136 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=107)

### LIQUIDACIONES_15M#XRP#15min
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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=3076)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=57)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.265 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=89)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.217 (n=58)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `15.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=123)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.135 (n=206)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.495 (IC base=+0.045)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=1125)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=1079)

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
- **FILTRO** `py_entrada` > `0.505` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=695)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=703)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=388)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=369)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.144 (n=147)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.015)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=793)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=793)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=246)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=627)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=655)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=655)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=218)

- **FILTRO** `hora_utc` > `13.0` → IC=-0.136 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=180)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=145)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=164)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=188)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=243)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=202)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=317)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=317)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=228)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.145 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=169)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.43` → IC=-0.124 (n=1638)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1760)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `restante_min` < `3.89` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `restante_min` < 3.89
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `lag_apertura_s` > `66.61` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `lag_apertura_s` > 66.61
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.138 (n=222)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=117)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.182 (n=108)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.46 (IC base=+0.026)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.210 (n=36)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=182)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.160 (n=101)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=120)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.133 (n=224)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=76)

- **FILTRO** `profundidad_ratio` < `37.6` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `profundidad_ratio` < 37.6
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=225)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.245 (n=53)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=244)

- **PATRÓN** `py_entrada` < `0.46` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.46 (IC base=-0.032)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.122 (n=244)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=139)

- **FILTRO** `restante_min` < `3.34` → IC=-0.188 (n=126)

  - _Acción_: SKIP cuando `restante_min` < 3.34
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=257)

- **FILTRO** `lag_apertura_s` > `97.61` → IC=-0.197 (n=130)

  - _Acción_: SKIP cuando `lag_apertura_s` > 97.61
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=253)

- **FILTRO** `profundidad_ratio` < `23.2` → IC=-0.125 (n=102)

  - _Acción_: SKIP cuando `profundidad_ratio` < 23.2
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=210)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.146 (n=63)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=235)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.143 (n=233)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=122)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.190 (n=98)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=339)

### MOMENTUM_IBS_15M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=1073)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=5550)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.126 (n=241)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=7798)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.475` → IC=-0.158 (n=5306)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=15954)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.167 (n=5433)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=16494)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.184 (n=949)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=2856)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.157 (n=908)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=3014)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.122 (n=1812)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.5 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.174 (n=753)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=2393)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.174 (n=935)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=2919)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.184 (n=992)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=2999)

- **PATRÓN** `ibs_20min` > `0.9656` → IC=+0.122 (n=1311)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.9656 (IC base=+0.037)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2244)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2658)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3398)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.172 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=412)

- **FILTRO** `libro_liquidez` < `16920.0467` → IC=-0.163 (n=176)

  - _Acción_: SKIP cuando `libro_liquidez` < 16920.0467
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=359)

### MOMENTUM_IBS_15M_FADE#DOGE#15min
- **FILTRO** `libro_liquidez` < `2574.706` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2574.706
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=323)

- **FILTRO** `libro_liquidez` < `3139.5911` → IC=-0.184 (n=134)

  - _Acción_: SKIP cuando `libro_liquidez` < 3139.5911
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=275)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=817)

- **FILTRO** `libro_liquidez` < `2042.3274` → IC=-0.163 (n=342)

  - _Acción_: SKIP cuando `libro_liquidez` < 2042.3274
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=696)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.037)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=39)

### MOMENTUM_IBS_5M#ETH#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=414)

### MOMENTUM_IBS_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=631)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.131 (n=14761)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=32794)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=11426)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=36129)

- **FILTRO** `ibs_7min` < `0.25` → IC=-0.232 (n=11856)

  - _Acción_: SKIP cuando `ibs_7min` < 0.25
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=35699)

- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.154 (n=15705)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=31850)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.237 (n=14614)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=45686)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.179 (n=15011)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=45289)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2381)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=5801)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.310 (n=1962)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=6220)

- **FILTRO** `ibs_7min` < `0.7091` → IC=-0.247 (n=2700)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7091
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=5482)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.173 (n=1929)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=6253)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.269 (n=2565)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=7891)

- **FILTRO** `ibs_7min` > `0.7759` → IC=-0.207 (n=2613)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7759
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=7843)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.128 (n=1948)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6133)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=1836)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=6245)

- **FILTRO** `ibs_7min` < `0.7355` → IC=-0.197 (n=2020)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7355
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=6061)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.187 (n=2004)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6077)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.265 (n=1983)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=6246)

- **FILTRO** `ibs_7min` > `0.2665` → IC=-0.196 (n=2057)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2665
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6172)

- **FILTRO** `ballena_activa_n` > `147.0` → IC=-0.184 (n=2056)

  - _Acción_: SKIP cuando `ballena_activa_n` > 147.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6173)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.163 (n=1918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=5856)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=1864)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=5910)

- **FILTRO** `ibs_7min` < `0.7021` → IC=-0.245 (n=2565)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7021
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=5209)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.222 (n=1655)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6119)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.247 (n=2527)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=8612)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.174 (n=2784)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=8355)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.126 (n=2545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=5248)

- **FILTRO** `py_entrada` < `0.35` → IC=-0.253 (n=1946)

  - _Acción_: SKIP cuando `py_entrada` < 0.35
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=5847)

- **FILTRO** `ibs_7min` < `0.7344` → IC=-0.186 (n=1947)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7344
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5846)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.190 (n=1935)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=5858)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2011)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=6045)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.179 (n=2012)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6044)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.180 (n=1980)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6076)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.271 (n=1943)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=5986)

- **FILTRO** `ibs_7min` < `0.2353` → IC=-0.233 (n=1979)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2353
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=5950)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=2729)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=8786)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=1913)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=5883)

- **FILTRO** `ibs_7min` < `0.23` → IC=-0.223 (n=1949)

  - _Acción_: SKIP cuando `ibs_7min` < 0.23
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=5847)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.201 (n=1828)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=5968)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.208 (n=2656)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=8249)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1057` → IC=-0.129 (n=60)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1057
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=119)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=979)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=1263)

- **FILTRO** `ibs_7min` < `1.0` → IC=-0.160 (n=51)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=631)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.167 (n=103)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=371)

- **FILTRO** `ballena_activa_n` > `7.0` → IC=-0.138 (n=158)

  - _Acción_: SKIP cuando `ballena_activa_n` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=315)

- **FILTRO** `libro_liquidez` < `3312.3658` → IC=-0.151 (n=167)

  - _Acción_: SKIP cuando `libro_liquidez` < 3312.3658
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=501)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=335)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.140 (n=1021)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.135 (n=475)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 14.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `3689.18` → IC=+0.146 (n=681)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 3689.18 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3729.2002` → IC=+0.130 (n=463)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3729.2002 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.143 (n=348)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 14.0 (IC base=+0.126)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4367` → IC=+0.159 (n=80)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio` |x|> 0.4367 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.218 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2615.3166` → IC=+0.232 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.3166 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.182 (n=105)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 10.0 (IC base=+0.143)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.129 (n=203)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.110)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.121 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 14.0 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.121 (n=238)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.04 (IC base=+0.110)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.144 (n=99)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 10.0 (IC base=+0.110)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4156` → IC=+0.176 (n=137)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4156 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.149 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 4.0 (IC base=+0.127)

- **PATRÓN** `total_vol_5m` < `388.5476` → IC=+0.220 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 388.5476 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `7205.1728` → IC=+0.134 (n=184)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 7205.1728 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 72.0 (IC base=+0.127)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4332` → IC=+0.241 (n=83)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4332 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.214 (n=61)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.149)

- **PATRÓN** `total_vol_5m` < `8043.774` → IC=+0.170 (n=183)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 8043.774 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `3092.8641` → IC=+0.160 (n=183)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3092.8641 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 28.0 (IC base=+0.149)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=121)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `3656.7944` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3656.7944 (IC base=+0.093)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.4547` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.4547
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=130)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.264 (n=294)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=295)

- **FILTRO** `T_h` > `130.2581` → IC=-0.211 (n=147)

  - _Acción_: SKIP cuando `T_h` > 130.2581
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=442)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.167 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0034 (IC base=-0.084)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0056` → IC=-0.264 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0056
  - _Potencial_: sin este filtro IC_bueno=+0.178 (n=88)

- **FILTRO** `T_h` > `88.1896` → IC=-0.300 (n=43)

  - _Acción_: SKIP cuando `T_h` > 88.1896
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=132)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.304 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.042)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7112` → IC=+0.150 (n=58)

  - _Acción_: Kelly boost +0.75€ cuando `pct_vs_K` |x|≤ 1.7112 (IC base=-0.042)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.152 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0097` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=70)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.066)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.222 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=135)

- **FILTRO** `pct_vs_K` |x|> `2.2275` → IC=-0.382 (n=227)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.2275
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=229)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0042` → IC=-0.202 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=138)

- **FILTRO** `T_h` > `79.3043` → IC=-0.177 (n=122)

  - _Acción_: SKIP cuando `T_h` > 79.3043
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=61)

- **FILTRO** `sigma_h` > `0.006` → IC=-0.309 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=84)

- **FILTRO** `pct_vs_K` |x|> `2.067` → IC=-0.393 (n=82)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.067
  - _Potencial_: sin este filtro IC_bueno=-0.163 (n=84)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `T_h` > `144.5457` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` > 144.5457
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0049` → IC=-0.288 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=102)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.361 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=106)

- **FILTRO** `pct_vs_K` |x|> `2.6475` → IC=-0.401 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6475
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=71)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.245 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=94)

- **FILTRO** `T_h` > `111.9844` → IC=-0.176 (n=69)

  - _Acción_: SKIP cuando `T_h` > 111.9844
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=70)

- **FILTRO** `sigma_h` > `0.0132` → IC=-0.348 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=63)

- **FILTRO** `pct_vs_K` |x|> `3.9474` → IC=-0.409 (n=31)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.9474
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=63)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.475 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.341)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.365 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.341)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.386 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.341)

- **PATRÓN** `T_h` < `0.9781` → IC=+0.359 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9781 (IC base=+0.341)

- **PATRÓN** `T_h` > `1.1834` → IC=+0.403 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1834 (IC base=+0.341)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.476 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.341)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.361 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.341)

- **PATRÓN** `edge` > `0.096` → IC=+0.446 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.429 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.418)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.441 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.418)

- **PATRÓN** `T_h` < `1.014` → IC=+0.426 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.014 (IC base=+0.418)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.442 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.3874` → IC=+0.465 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3874 (IC base=+0.418)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.418)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1026` → IC=+0.457 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1026 (IC base=+0.430)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.417 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.430)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.460 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.430)

- **PATRÓN** `T_h` < `0.9672` → IC=+0.456 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.9672 (IC base=+0.430)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.423 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.430)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.478 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.430)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.430)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.430)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1975` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1975 (IC base=+0.432)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.464 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.432)

- **PATRÓN** `T_h` > `0.639` → IC=+0.459 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.639 (IC base=+0.432)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.432)

- **PATRÓN** `edge` > `0.2005` → IC=+0.477 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.477 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.2025` → IC=+0.477 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.2025 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4455` → IC=+0.485 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4455 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=271)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=352)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `2526.423` → IC=+0.123 (n=128)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2526.423 (IC base=+0.041)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=26)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.143 (n=12)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.012)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `volumen_racha` < `945898.4` → IC=+0.128 (n=49)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_racha` < 945898.4 (IC base=+0.010)

- **PATRÓN** `streak_estiramiento` < `0.2918` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `streak_estiramiento` < 0.2918 (IC base=+0.010)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.092)

- **PATRÓN** `streak_estiramiento` < `0.3243` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `streak_estiramiento` < 0.3243 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 45.0 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2659.6588` → IC=+0.136 (n=75)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2659.6588 (IC base=+0.092)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=100)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=41)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=26)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=685)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `9.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `volumen_racha` > `9229.0178` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 9229.0178
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `libro_liquidez` < `2349.4469` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 2349.4469
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

### STREAK_FADE_60M#ETH#60min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

### STREAK_FADE_60M#SOL#60min
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.050)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=892)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1325)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1030)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=1043)

### STRUCT_NO_15M
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=3692)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `libro_liquidez` < `7203.0371` → IC=-0.300 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7203.0371
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1971)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.205 (n=1014)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.231 (n=1013)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.1654` → IC=+0.200 (n=2675)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1654 (IC base=+0.192)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2289` → IC=+0.194 (n=1013)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio_macro` |x|> 0.2289 (IC base=+0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3523` → IC=+0.205 (n=2706)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3523 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=2823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.197 (n=2784)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `ibs_15` > `0.5874` → IC=+0.269 (n=3039)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5874 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.1207` → IC=+0.186 (n=1442)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1207 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.2984` → IC=+0.180 (n=2281)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2984 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.579` → IC=+0.273 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.579 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `5486.381` → IC=+0.203 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5486.381 (IC base=+0.192)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1183)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.238 (n=360)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.264 (n=180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.218)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2541` → IC=+0.264 (n=180)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2541 (IC base=+0.218)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2321` → IC=+0.232 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2321 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=543)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.218)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.280 (n=540)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.241 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.196` → IC=+0.295 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.196 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.220 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `16220.2116` → IC=+0.247 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16220.2116 (IC base=+0.218)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.513` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.513
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=677)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.185 (n=201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0033 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.159 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.147)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1507` → IC=+0.163 (n=401)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio_macro` |x|> 0.1507 (IC base=+0.147)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1312` → IC=+0.164 (n=233)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1312 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.155 (n=282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.152 (n=631)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 17.0 (IC base=+0.147)

- **PATRÓN** `ibs_15` > `0.5728` → IC=+0.243 (n=602)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5728 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.149 (n=337)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.2646` → IC=+0.151 (n=559)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2646 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.049` → IC=+0.286 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.049 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `3532.4883` → IC=+0.152 (n=538)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3532.4883 (IC base=+0.147)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `19.46` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.46
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=242)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.147 (n=188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0055 (IC base=+0.116)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.168 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0095 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.137` → IC=+0.156 (n=376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.137 (IC base=+0.116)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3414` → IC=+0.136 (n=514)

  - _Acción_: Kelly boost +0.68€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3414 (IC base=+0.116)

- **PATRÓN** `ibs_15` > `0.913` → IC=+0.286 (n=190)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.913 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.1876` → IC=+0.135 (n=497)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1876 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.128` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.128 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=315)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.116)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.788` → IC=+0.167 (n=40)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 15.788 (IC base=+0.013)

- **PATRÓN** `libro_liquidez` > `3388.6908` → IC=+0.128 (n=76)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3388.6908 (IC base=+0.013)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0232` → IC=+0.283 (n=233)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0232 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1653` → IC=+0.230 (n=616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1653 (IC base=+0.222)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1101` → IC=+0.223 (n=467)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1101 (IC base=+0.222)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.327` → IC=+0.248 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.327 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.237 (n=645)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_15` > `0.5745` → IC=+0.303 (n=699)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5745 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1857` → IC=+0.232 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1857 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.758` → IC=+0.272 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.758 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2928.9931` → IC=+0.277 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2928.9931 (IC base=+0.222)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.162 (n=722)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.81€ cuando `ibs_15` < 0.1111 (IC base=+0.065)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.366 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.372 (n=576)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1522` → IC=+0.386 (n=384)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1522 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2309` → IC=+0.388 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2309 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.398 (n=576)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4129` → IC=+0.384 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4129 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.88` → IC=+0.385 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.88 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3851.736` → IC=+0.372 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3851.736 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.360 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.376 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.361)

- **PATRÓN** `drift_15min` |x|≤ `0.5078` → IC=+0.360 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5078 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.394 (n=139)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.393 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.381 (n=309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.387 (n=307)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.2515` → IC=+0.394 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2515 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.382 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `15252.9657` → IC=+0.387 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15252.9657 (IC base=+0.361)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.409 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.361)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.363 (n=180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.375 (n=270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.368 (n=180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0904` → IC=+0.377 (n=241)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0904 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.393 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.407 (n=127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.364 (n=123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7557` → IC=+0.408 (n=270)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7557 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4366` → IC=+0.366 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4366 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.2765` → IC=+0.370 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2765 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.391 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3893.6222` → IC=+0.388 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3893.6222 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `140.0` → IC=+0.372 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 140.0 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0121` → IC=-0.221 (n=985)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0121
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2957)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.207 (n=1529)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=2413)

- **FILTRO** `libro_liquidez` < `4124.0401` → IC=-0.146 (n=2601)

  - _Acción_: SKIP cuando `libro_liquidez` < 4124.0401
  - _Potencial_: sin este filtro IC_bueno=+0.090 (n=1341)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1425` → IC=+0.189 (n=631)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1425 (IC base=-0.065)

- **PATRÓN** `ibs_15` > `0.6349` → IC=+0.284 (n=947)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6349 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.1071` → IC=+0.206 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1071 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2612` → IC=+0.201 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2612 (IC base=-0.065)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1326` → IC=+0.262 (n=2132)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1326 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3519` → IC=+0.282 (n=3195)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3519 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.8606` → IC=+0.283 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8606 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.203 (n=546)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=1642)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.225 (n=722)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=1466)

- **FILTRO** `sigma_ewma_delta_pct` > `23.858` → IC=-0.270 (n=316)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.858
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=1872)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.203 (n=62)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=2126)

- **FILTRO** `libro_liquidez` < `16292.8606` → IC=-0.204 (n=1444)

  - _Acción_: SKIP cuando `libro_liquidez` < 16292.8606
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=744)

- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.171 (n=223)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0026 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2139` → IC=+0.307 (n=133)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2139 (IC base=+0.095)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1064` → IC=+0.294 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1064 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.137 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 15.0 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.336 (n=291)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1039` → IC=+0.302 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1039 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` < `0.3639` → IC=+0.295 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3639 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.877` → IC=+0.141 (n=154)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 24.877 (IC base=+0.095)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.236 (n=51)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1779` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1779 (IC base=-0.194)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.311 (n=51)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.194)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.194)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.417 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 295.0 (IC base=-0.194)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=615)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.162 (n=418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.162 (n=474)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0033 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.1111` → IC=+0.183 (n=317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1111 (IC base=+0.153)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.157 (n=316)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.79€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=+0.153)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2968` → IC=+0.200 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2968 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.177 (n=335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.254 (n=474)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6314 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.5931` → IC=+0.156 (n=88)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.5931 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.266` → IC=+0.157 (n=444)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.266 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.258 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.161 (n=615)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `10832.5702` → IC=+0.169 (n=158)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10832.5702 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.256 (n=482)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.3466` → IC=+0.243 (n=963)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3466 (IC base=+0.241)

- **PATRÓN** `drift_15min` |x|≤ `0.7479` → IC=+0.252 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7479 (IC base=+0.241)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2139` → IC=+0.262 (n=497)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2139 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.258 (n=366)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.241)

- **PATRÓN** `ibs_15` < `0.3657` → IC=+0.271 (n=1095)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3657 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.7604` → IC=+0.288 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7604 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.464` → IC=+0.258 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.464 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.584` → IC=+0.245 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.584 (IC base=+0.241)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.172` → IC=-0.253 (n=306)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.172
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=596)

- **FILTRO** `drift_15min` |x|> `0.8765` → IC=-0.271 (n=225)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8765
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=677)

- **FILTRO** `sigma_ewma_delta_pct` > `6.572` → IC=-0.194 (n=220)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.572
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=682)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.180)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.180)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.180)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.180)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0649` → IC=+0.242 (n=495)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0649 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.288 (n=498)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.1721` → IC=+0.245 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1721 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0195` → IC=-0.249 (n=548)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0195
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=550)

- **FILTRO** `drift_15min` |x|> `1.2333` → IC=-0.261 (n=274)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2333
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=824)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1079)

- **FILTRO** `libro_liquidez` < `2982.5179` → IC=-0.213 (n=823)

  - _Acción_: SKIP cuando `libro_liquidez` < 2982.5179
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.202)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1517` → IC=+0.276 (n=351)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1517 (IC base=-0.027)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1114` → IC=+0.302 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1114 (IC base=-0.027)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.295 (n=778)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` > `0.7812` → IC=+0.344 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7812 (IC base=-0.027)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.036)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `dist_vwap_pct` > `0.1506` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1506 (IC base=+0.036)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.297 (n=841)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.292 (n=957)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0533` → IC=+0.322 (n=319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0533 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.248` → IC=+0.301 (n=319)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.248 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2247` → IC=+0.312 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2247 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.324 (n=956)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.424` → IC=+0.323 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.424 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.005` → IC=+0.366 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.005 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12762.7474` → IC=+0.307 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12762.7474 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.309 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.311 (n=173)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2605` → IC=+0.317 (n=173)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2605 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.310 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8267` → IC=+0.311 (n=518)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8267 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.327 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.371` → IC=+0.374 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 24.371 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.287 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16334.7136` → IC=+0.323 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16334.7136 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.307 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.297)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.298 (n=438)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.297)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.326 (n=147)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.297)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1536` → IC=+0.303 (n=292)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1536 (IC base=+0.297)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.320 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.297)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.317 (n=424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.297)

- **PATRÓN** `ibs_15` > `0.8537` → IC=+0.334 (n=438)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8537 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.5931` → IC=+0.325 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5931 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.866` → IC=+0.348 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.866 (IC base=+0.297)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0857` → IC=-0.250 (n=78)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0857
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=242)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.172 (n=117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=353)

- **FILTRO** `ballena_activa_n` > `50.0` → IC=-0.204 (n=52)

  - _Acción_: SKIP cuando `ballena_activa_n` > 50.0
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=157)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1289` → IC=-0.167 (n=46)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1289
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=141)

- **FILTRO** `drift_60min` |x|> `0.2244` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2244
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=33)

- **FILTRO** `drift_15min` |x|> `0.3481` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3481
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1941` → IC=-0.231 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1941
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.3151` → IC=-0.158 (n=36)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3151
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.296` → IC=-0.370 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.296
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.243 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `81.6471` → IC=+0.198 (n=429)

  - _Acción_: Kelly boost +0.99€ cuando `T_h` > 81.6471 (IC base=+0.192)

- **PATRÓN** `ratio` < `0.9744` → IC=+0.415 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9744 (IC base=+0.192)

- **PATRÓN** `T_h` > `145.7201` → IC=+0.384 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7201 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0236` → IC=+0.366 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0236 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.3918` → IC=+0.176 (n=177)

  - _Acción_: Kelly boost +0.88€ cuando `T_h` > 103.3918 (IC base=+0.165)

- **PATRÓN** `ratio` < `0.9702` → IC=+0.370 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9702 (IC base=+0.165)

- **PATRÓN** `T_h` > `106.964` → IC=+0.299 (n=665)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 106.964 (IC base=+0.289)

- **PATRÓN** `ratio` > `1.0466` → IC=+0.392 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0466 (IC base=+0.289)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `81.6124` → IC=+0.237 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 81.6124 (IC base=+0.229)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.401 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.229)

- **PATRÓN** `T_h` > `111.9668` → IC=+0.347 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9668 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.348 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1062` → IC=+0.450 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1062 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5874 sube el IC de +0.192 a +0.269 en UPDOWN_GBM#15min (n=3039). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.218 a +0.280 en UPDOWN_GBM#BTC#15min (n=540). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5728 sube el IC de +0.147 a +0.243 en UPDOWN_GBM#ETH#15min (n=602). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.913 sube el IC de +0.116 a +0.286 en UPDOWN_GBM#SOL#15min (n=190). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5745 sube el IC de +0.222 a +0.303 en UPDOWN_GBM#XRP#15min (n=699). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.065 a +0.162 en UPDOWN_GBM#XRP#15min (n=722). Ya aplicado como kelly_boost=+0.81€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6349 sube el IC de -0.065 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=947). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3519 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3195). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.095 a +0.336 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=291). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.194 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=51). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6314 sube el IC de +0.153 a +0.254 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=474). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3657 sube el IC de +0.241 a +0.271 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1095). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.180 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.038 a +0.288 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=498). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.202 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.027 a +0.295 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=778). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.292 a +0.324 en UPDOWN_GBM_IBS_ALTO (n=956). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8267 sube el IC de +0.288 a +0.311 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=518). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8537 sube el IC de +0.297 a +0.334 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=438). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.364 a +0.398 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=576). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.361 a +0.387 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=307). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7557 sube el IC de +0.364 a +0.408 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=270). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1720 | +0.088 | +196.29€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1720 | +0.088 | +196.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1346 | +0.091 | +168.44€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1346 | +0.091 | +168.44€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 271 | +0.068 | +12.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 271 | +0.068 | +12.14€ | 3 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 72 | +0.108 | +16.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 72 | +0.108 | +16.05€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 414 | +0.002 | +69.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 414 | +0.002 | +69.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 298 | +0.000 | +46.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 298 | +0.000 | +46.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 91 | +0.016 | +17.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 91 | +0.016 | +17.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 23 | -0.060 | +1.23€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 36702 | -0.083 | -4701.75€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 1935 | +0.004 | -243.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 34767 | -0.088 | -4458.28€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4424 | -0.116 | -761.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4424 | -0.116 | -761.68€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 1935 | +0.004 | -243.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 1935 | +0.004 | -243.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4121 | -0.113 | -845.32€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4121 | -0.113 | -845.32€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 9577 | +0.000 | -866.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 9577 | +0.000 | -866.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 9533 | -0.109 | -718.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 9533 | -0.109 | -718.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7112 | -0.148 | -1266.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7112 | -0.148 | -1266.92€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 29879 | -0.018 | +3568.82€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 7726 | +0.004 | +1744.12€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 22153 | -0.025 | +1824.70€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 29879 | -0.018 | +3568.82€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 7726 | +0.004 | +1744.12€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 22153 | -0.025 | +1824.70€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 128907 | +0.114 | -5420.24€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 17328 | +0.182 | -532.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 558 | -0.034 | -65.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 103151 | +0.105 | -4547.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 7870 | +0.103 | -275.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 17119 | +0.105 | -1103.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 58 | -0.150 | +11.01€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 17046 | +0.107 | -1102.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 25272 | +0.129 | -394.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5027 | +0.193 | -150.61€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 17101 | +0.118 | -136.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3102 | +0.087 | -85.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 17169 | +0.097 | -1261.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 68 | -0.114 | -5.90€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 17086 | +0.098 | -1244.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 27394 | +0.124 | -482.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7203 | +0.176 | -122.63€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 17312 | +0.106 | -302.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 2867 | +0.100 | -48.90€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 24816 | +0.114 | -1329.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 4912 | +0.191 | -270.72€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 461 | +0.001 | -11.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 17542 | +0.093 | -906.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1901 | +0.133 | -140.61€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 17137 | +0.104 | -849.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 60 | -0.065 | +6.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 17064 | +0.105 | -855.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 20682 | +0.194 | -1308.58€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 20682 | +0.194 | -1308.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 4754 | +0.175 | -435.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 4754 | +0.175 | -435.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2418 | +0.200 | -53.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2418 | +0.200 | -53.37€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4694 | +0.179 | -387.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4694 | +0.179 | -387.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4107 | +0.244 | -140.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4107 | +0.244 | -140.60€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4630 | +0.188 | -305.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4630 | +0.188 | -305.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 932 | +0.427 | -31.67€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 932 | +0.427 | -31.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 369 | +0.435 | -5.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 369 | +0.435 | -5.95€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 360 | +0.431 | -8.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 360 | +0.431 | -8.65€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 191 | +0.402 | -14.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 191 | +0.402 | -14.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 71892 | +0.201 | -5237.67€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 71892 | +0.201 | -5237.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 12357 | +0.185 | -1272.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 12357 | +0.185 | -1272.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 11576 | +0.225 | -390.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 11576 | +0.225 | -390.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 12340 | +0.178 | -1350.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 12340 | +0.178 | -1350.44€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 11661 | +0.221 | -425.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 11661 | +0.221 | -425.50€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 11926 | +0.201 | -805.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 11926 | +0.201 | -805.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 12032 | +0.195 | -993.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 12032 | +0.195 | -993.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 27461 | +0.118 | +225.01€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 27461 | +0.118 | +225.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 13644 | +0.121 | +188.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 13644 | +0.121 | +188.63€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 13817 | +0.114 | +36.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 13817 | +0.114 | +36.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1882 | +0.295 | +6.86€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1882 | +0.295 | +6.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 853 | +0.286 | -4.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 853 | +0.286 | -4.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 910 | +0.294 | +6.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 910 | +0.294 | +6.52€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 868 | +0.443 | +6.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 868 | +0.443 | +6.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 419 | +0.441 | +0.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 419 | +0.441 | +0.71€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 403 | +0.446 | +5.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 403 | +0.446 | +5.16€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1462 | +0.073 | -55.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 547 | +0.065 | -34.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 915 | +0.078 | -20.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 69 | +0.106 | +2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 69 | +0.106 | +2.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1132 | +0.079 | -23.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 217 | +0.085 | -2.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 915 | +0.078 | -20.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 261 | +0.036 | -34.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 261 | +0.036 | -34.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 53401 | +0.100 | -1357.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4322 | +0.094 | +69.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 49079 | +0.101 | -1426.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 29498 | +0.105 | -304.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4322 | +0.094 | +69.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 25176 | +0.107 | -373.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 10779 | +0.109 | -51.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 10779 | +0.109 | -51.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 13124 | +0.081 | -1001.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 13124 | +0.081 | -1001.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 883 | +0.197 | -111.73€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 883 | +0.197 | -111.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 883 | +0.197 | -111.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 883 | +0.197 | -111.73€ | 2 | 4 |
| ✅ GBM_LATE_15M | 36917 | +0.091 | +18727.63€ | 0 | 16 |
| ✅ GBM_LATE_15M#15min | 36917 | +0.091 | +18727.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6197 | +0.208 | +4902.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6197 | +0.208 | +4902.52€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 5481 | +0.180 | +4052.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 5481 | +0.180 | +4052.32€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 6585 | +0.203 | +5058.79€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 6585 | +0.203 | +5058.79€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 5184 | +0.038 | +1358.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5184 | +0.038 | +1358.24€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 5273 | -0.030 | +1151.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5273 | -0.030 | +1151.90€ | 3 | 11 |
| ✅ GBM_LATE_15M#XRP | 8197 | -0.036 | +2203.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 8197 | -0.036 | +2203.88€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 39942 | +0.086 | +21459.93€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 39942 | +0.086 | +21459.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 7704 | +0.007 | +4029.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 7704 | +0.007 | +4029.76€ | 3 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 8391 | +0.013 | +1852.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 8391 | +0.013 | +1852.24€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 5596 | +0.272 | +5872.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 5596 | +0.272 | +5872.63€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 6971 | +0.013 | +1622.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 6971 | +0.013 | +1622.02€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6448 | +0.037 | +2589.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6448 | +0.037 | +2589.35€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 4832 | +0.294 | +5493.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 4832 | +0.294 | +5493.93€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 29358 | +0.177 | +23275.42€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 29358 | +0.177 | +23275.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4458 | +0.221 | +3801.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4458 | +0.221 | +3801.07€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4609 | +0.151 | +3381.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4609 | +0.151 | +3381.07€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 4687 | +0.219 | +3950.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 4687 | +0.219 | +3950.79€ | 0 | 18 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 4943 | +0.139 | +3728.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 4943 | +0.139 | +3728.60€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5520 | +0.123 | +4028.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5520 | +0.123 | +4028.27€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5141 | +0.220 | +4385.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5141 | +0.220 | +4385.62€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 7921 | +0.138 | +3814.45€ | 0 | 19 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 7921 | +0.138 | +3814.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 355 | +0.144 | +210.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 355 | +0.144 | +210.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2408 | +0.148 | +1348.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2408 | +0.148 | +1348.69€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 411 | +0.144 | +197.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 411 | +0.144 | +197.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2410 | +0.148 | +1167.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2410 | +0.148 | +1167.07€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 1798 | +0.107 | +650.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 1798 | +0.107 | +650.51€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 539 | +0.134 | +240.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 539 | +0.134 | +240.28€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO | 37119 | +0.183 | +29123.15€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 37119 | +0.183 | +29123.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 5904 | +0.235 | +5342.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 5904 | +0.235 | +5342.93€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 5730 | +0.149 | +3818.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 5730 | +0.149 | +3818.18€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6254 | +0.231 | +5527.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6254 | +0.231 | +5527.40€ | 0 | 18 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6071 | +0.138 | +4301.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6071 | +0.138 | +4301.12€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 6580 | +0.122 | +4496.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 6580 | +0.122 | +4496.64€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 6580 | +0.223 | +5636.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 6580 | +0.223 | +5636.88€ | 0 | 21 |
| ✅ GBM_LATE_5M | 10232 | +0.190 | +7455.80€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 10232 | +0.190 | +7455.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2229 | +0.181 | +1698.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2229 | +0.181 | +1698.66€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1002 | +0.176 | +657.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1002 | +0.176 | +657.98€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 3097 | +0.190 | +2157.68€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3097 | +0.190 | +2157.68€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 1426 | +0.179 | +1018.68€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1426 | +0.179 | +1018.68€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1559 | +0.193 | +1108.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1559 | +0.193 | +1108.81€ | 0 | 0 |
| ✅ GBM_LATE_60M | 2879 | +0.067 | +974.57€ | 0 | 9 |
| ✅ GBM_LATE_60M#60min | 2879 | +0.067 | +974.57€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1078 | +0.086 | +381.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1078 | +0.086 | +381.71€ | 0 | 10 |
| ✅ GBM_LATE_60M#ETH | 913 | +0.068 | +355.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 913 | +0.068 | +355.28€ | 0 | 10 |
| ✅ GBM_LATE_60M#SOL | 888 | +0.043 | +237.58€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 888 | +0.043 | +237.58€ | 1 | 13 |
| 🚫 GBM_LATE_60M_FADE | 513 | -0.242 | -19.32€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 513 | -0.242 | -19.32€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 194 | -0.235 | -11.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 194 | -0.235 | -11.07€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 181 | -0.221 | -1.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 181 | -0.221 | -1.28€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 138 | -0.271 | -6.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 138 | -0.271 | -6.96€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1303 | +0.087 | +339.06€ | 0 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1303 | +0.087 | +339.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 499 | +0.085 | +106.21€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 499 | +0.085 | +106.21€ | 0 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 477 | +0.062 | +79.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 477 | +0.062 | +79.64€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 327 | +0.126 | +153.22€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 327 | +0.126 | +153.22€ | 1 | 13 |
| ✅ LATE_WINDOW_5MIN | 141 | +0.255 | +122.89€ | 0 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 141 | +0.255 | +122.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 141 | +0.255 | +122.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 141 | +0.255 | +122.89€ | 0 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3099 | +0.099 | +767.19€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3099 | +0.099 | +767.19€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3099 | +0.099 | +767.19€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3099 | +0.099 | +767.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 451 | -0.065 | -30.21€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 451 | -0.065 | -30.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 129 | -0.019 | +0.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 129 | -0.019 | +0.68€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 73 | -0.087 | -8.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 73 | -0.087 | -8.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 168 | -0.029 | -5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 168 | -0.029 | -5.75€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_5M | 3282 | +0.020 | +88.74€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3282 | +0.020 | +88.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 159 | +0.015 | -3.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 159 | +0.015 | -3.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 583 | +0.032 | +44.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 583 | +0.032 | +44.16€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1175 | +0.033 | +36.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1175 | +0.033 | +36.06€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 744 | +0.011 | +0.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 744 | +0.011 | +0.71€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 418 | +0.007 | +16.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 418 | +0.007 | +16.59€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1543 | -0.043 | -29.43€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1543 | -0.043 | -29.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 436 | -0.036 | -12.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 436 | -0.036 | -12.54€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 517 | -0.018 | +3.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 517 | -0.018 | +3.72€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 590 | -0.069 | -20.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 590 | -0.069 | -20.62€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 6247 | -0.025 | +2.73€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 2978 | -0.032 | -42.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 3269 | -0.020 | +44.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 179 | -0.014 | +4.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 87 | +0.028 | +9.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 92 | -0.053 | -5.09€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1555 | -0.015 | +20.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 744 | -0.019 | +0.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 811 | -0.012 | +20.31€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 698 | -0.029 | -0.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 355 | -0.041 | -9.46€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 343 | -0.016 | +8.82€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1292 | -0.038 | -42.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 597 | -0.054 | -46.02€ | 3 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 695 | -0.024 | +3.10€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1219 | -0.018 | +23.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 590 | -0.022 | +11.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 629 | -0.015 | +11.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1304 | -0.031 | -1.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 605 | -0.037 | -8.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 699 | -0.026 | +6.21€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 43187 | -0.002 | +2072.24€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 43187 | -0.002 | +2072.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 7727 | +0.025 | +1001.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 7727 | +0.025 | +1001.63€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6332 | -0.034 | -116.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6332 | -0.034 | -116.62€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 7845 | +0.022 | +772.68€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 7845 | +0.022 | +772.68€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6163 | -0.050 | -169.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6163 | -0.050 | -169.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7288 | -0.005 | +240.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7288 | -0.005 | +240.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 7832 | +0.014 | +343.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 7832 | +0.014 | +343.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6360 | -0.060 | -156.16€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6360 | -0.060 | -156.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1221 | +0.000 | -14.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1221 | +0.000 | -14.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1613 | -0.078 | -39.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1613 | -0.078 | -39.11€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 743 | -0.121 | -32.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 743 | -0.121 | -32.92€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1874 | -0.079 | -41.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1874 | -0.079 | -41.89€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M | 3359 | +0.004 | -2.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3359 | +0.004 | -2.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 128 | -0.038 | -1.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 128 | -0.038 | -1.27€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 138 | +0.000 | -1.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 138 | +0.000 | -1.83€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1322 | +0.005 | +5.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1322 | +0.005 | +5.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1390 | +0.007 | +0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1390 | +0.007 | +0.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 189 | -0.008 | -5.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 107855 | -0.074 | +1739.59€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 107855 | -0.074 | +1739.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 18638 | -0.074 | +982.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 18638 | -0.074 | +982.35€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 16310 | -0.099 | -907.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 16310 | -0.099 | -907.93€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 18913 | -0.066 | +1086.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 18913 | -0.066 | +1086.48€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 15849 | -0.095 | -474.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 15849 | -0.095 | -474.99€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 19444 | -0.053 | +404.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 19444 | -0.053 | +404.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 18701 | -0.065 | +649.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 18701 | -0.065 | +649.18€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8565 | -0.033 | -178.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8565 | -0.033 | -178.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 996 | -0.017 | -19.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 996 | -0.017 | -19.84€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1960 | -0.045 | -21.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1960 | -0.045 | -21.69€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2562 | -0.027 | -45.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2562 | -0.027 | -45.40€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1142 | -0.050 | -24.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1142 | -0.050 | -24.50€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 897 | -0.032 | -34.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 897 | -0.032 | -34.56€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1496 | +0.119 | +584.21€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1360 | +0.126 | +571.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 317 | +0.143 | +165.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 317 | +0.143 | +165.79€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 270 | +0.110 | +83.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 270 | +0.110 | +83.77€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 274 | +0.127 | +122.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 274 | +0.127 | +122.07€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 243 | +0.149 | +130.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 243 | +0.149 | +130.57€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 256 | +0.093 | +69.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 256 | +0.093 | +69.42€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1154 | -0.021 | -24.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1154 | -0.021 | -24.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 222 | -0.018 | -0.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 222 | -0.018 | -0.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 192 | -0.005 | +5.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 192 | -0.005 | +5.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 299 | -0.038 | -19.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 299 | -0.038 | -19.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 243 | -0.002 | -1.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 243 | -0.002 | -1.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 198 | -0.035 | -8.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 198 | -0.035 | -8.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 829 | -0.070 | -36.17€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 382 | -0.120 | -76.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 293 | -0.154 | -66.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 295 | -0.032 | +27.22€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 209 | -0.026 | +27.73€ | 2 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 152 | -0.019 | +13.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 122 | -0.024 | +8.23€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 624 | -0.086 | -30.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 995 | -0.206 | -51.65€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 405 | -0.205 | -36.64€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 349 | -0.209 | -36.92€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 338 | -0.215 | -28.27€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 292 | -0.225 | -33.96€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 252 | -0.193 | +13.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 233 | -0.189 | +10.12€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 874 | -0.210 | -60.77€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 414 | +0.397 | +398.12€ | 0 | 14 |
| ✅ RESOLUTION_SNIPER#BTC | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 53 | +0.118 | +46.13€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 104 | +0.377 | +93.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 104 | +0.377 | +93.44€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 257 | +0.458 | +258.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 257 | +0.458 | +258.55€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 414 | +0.397 | +398.12€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 661 | +0.032 | +33.06€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 661 | +0.032 | +33.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 296 | +0.024 | +3.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 51 | -0.009 | -4.63€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 51 | -0.009 | -4.63€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 68 | +0.000 | +0.45€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 68 | +0.000 | +0.45€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 246 | +0.060 | +33.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 246 | +0.060 | +33.80€ | 0 | 6 |
| ✅ STREAK_FADE_5M | 3362 | -0.021 | -129.02€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3362 | -0.021 | -129.02€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 586 | -0.025 | -25.10€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 586 | -0.025 | -25.10€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 160 | -0.043 | -14.37€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 160 | -0.043 | -14.37€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1565 | -0.016 | -52.03€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1565 | -0.016 | -52.03€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 94 | -0.052 | -9.37€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 94 | -0.052 | -9.37€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 39 | -0.085 | -3.98€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 39 | -0.085 | -3.98€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 55 | -0.026 | -5.39€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 55 | -0.026 | -5.39€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10231 | +0.019 | +106.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10231 | +0.019 | +106.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2648 | +0.021 | +27.27€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2588 | +0.023 | +44.50€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2588 | +0.023 | +44.50€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2880 | +0.009 | -1.07€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2880 | +0.009 | -1.07€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2115 | +0.023 | +35.76€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2115 | +0.023 | +35.76€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9319 | +0.013 | -44.20€ | 1 | 0 |
| ✅ STRUCT_NO_15M#15min | 9319 | +0.013 | -44.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3711 | +0.019 | -1.89€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3711 | +0.019 | -1.89€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3603 | +0.011 | -28.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3603 | +0.011 | -28.25€ | 1 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2005 | +0.008 | -14.06€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2005 | +0.008 | -14.06€ | 1 | 0 |
| ✅ UPDOWN_GBM | 67621 | +0.052 | +5865.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 16853 | +0.085 | +3826.26€ | 0 | 12 |
| ✅ UPDOWN_GBM#240min | 2228 | +0.007 | +14.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 44472 | +0.046 | +1963.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 3840 | +0.008 | +62.69€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6818 | +0.089 | +1072.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1543 | +0.158 | +694.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 13529 | +0.054 | +1128.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2088 | +0.090 | +506.86€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 570 | +0.012 | +7.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 9074 | +0.058 | +565.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1714 | +0.006 | +45.94€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 83 | -0.076 | +2.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8043 | +0.066 | +843.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1529 | +0.149 | +607.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6436 | +0.047 | +237.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 14899 | +0.042 | +905.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 3871 | +0.061 | +540.73€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 564 | +0.009 | +10.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 9080 | +0.041 | +340.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1308 | +0.011 | +10.99€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 76 | -0.103 | +2.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 14838 | +0.028 | +632.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4026 | +0.035 | +346.19€ | 0 | 8 |
| ✅ UPDOWN_GBM#SOL#240min | 551 | -0.003 | -0.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9376 | +0.030 | +286.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 818 | +0.006 | +5.75€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#daily | 67 | -0.138 | -5.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 9492 | +0.062 | +1284.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 3796 | +0.103 | +1130.42€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5308 | +0.036 | +154.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 226 | -0.105 | +0.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 768 | +0.364 | +276.14€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 768 | +0.364 | +276.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 409 | +0.361 | +139.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 409 | +0.361 | +139.61€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 359 | +0.364 | +136.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 359 | +0.364 | +136.52€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 18079 | -0.024 | +4370.80€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 18079 | -0.024 | +4370.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1674 | -0.056 | +500.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3077 | -0.110 | +133.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3077 | -0.110 | +133.90€ | 5 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 926 | +0.220 | +767.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2091 | +0.215 | +1336.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2091 | +0.215 | +1336.15€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5127 | -0.063 | +696.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5127 | -0.063 | +696.05€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5184 | -0.064 | +936.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5184 | -0.064 | +936.25€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 201 | +0.037 | +7.46€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 201 | +0.037 | +7.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 201 | +0.037 | +7.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 201 | +0.037 | +7.46€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1274 | +0.292 | +1071.39€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1274 | +0.292 | +1071.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 690 | +0.288 | +544.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 690 | +0.288 | +544.58€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 584 | +0.297 | +526.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 584 | +0.297 | +526.81€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 790 | -0.112 | -82.51€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 790 | -0.112 | -82.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 236 | -0.088 | -18.91€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 236 | -0.088 | -18.91€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 84 | -0.151 | -7.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 84 | -0.151 | -7.62€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 87 | -0.185 | -6.62€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 87 | -0.185 | -6.62€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3240 | +0.303 | +1556.41€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1176 | +0.255 | +157.29€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1242 | +0.297 | +548.00€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 822 | +0.379 | +851.11€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.014 n=830 — no justifica filtro, seguir monitorizando
  - _Datos_: n=830 IC=+0.014 PNL=+32.09€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 672 celda(s) pasan gate riguroso completo de 2585 evaluadas (n>=40) y 3568 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=4026 IC=+0.035 PNL=+346.19€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1242/15 IC=+0.297 PNL=+548.00€ | BTC: n=1176/15 IC=+0.255 PNL=+157.29€ | SOL: n=822/15 IC=+0.379 PNL=+851.11€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=712/60 | contraria IC=+0.203 n=742 | gap=-0.063 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=415, boost estimado=+0.010. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1307/40 IC=+0.011 PNL=+10.50€ | BTC#60min: n=1713/40 IC=+0.006 PNL=+45.47€ | SOL#60min: n=817/40 IC=+0.007 PNL=+6.26€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=489562 | tras_1loss IC=+0.092 n=373756 | tras_2loss IC=+0.061 n=152446/40 | gap=-0.013 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.216 > 0.08 con n=622 PNL=+498.63€
  - _Datos_: n=622 IC=+0.216 PNL=+498.63€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.193 > 0.08 con n=699 PNL=+468.50€
  - _Datos_: n=699 IC=+0.193 PNL=+468.50€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.189 > 0.08 con n=59 PNL=+35.04€
  - _Datos_: n=59 IC=+0.189 PNL=+35.04€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=2644 PNL=+1463.94€
  - _Datos_: n=2644 IC=+0.332 PNL=+1463.94€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=553 IC=+0.073 PNL=+61.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=553 IC=+0.073 PNL=+61.77€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=74 IC=+0.171 PNL=+45.37€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=74 IC=+0.171 PNL=+45.37€

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
  - _Estado_: 1/20 ops en el filtro definido (IC actual=+0.008 PNL=+1.96€)
  - _Datos_: n=1 IC=+0.008 PNL=+1.96€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=2601 IC=+0.009 PNL=+9.42€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2601 IC=+0.009 PNL=+9.42€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1236 IC=+0.005 PNL=+52.80€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1236 IC=+0.005 PNL=+52.80€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=830 IC=+0.014 PNL=+32.09€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=830 IC=+0.014 PNL=+32.09€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.192 > 0.1 con n=4052 PNL=+2743.85€
  - _Datos_: n=4052 IC=+0.192 PNL=+2743.85€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2088 IC=+0.090 PNL=+506.86€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2088 IC=+0.090 PNL=+506.86€

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
  - _Estado_: n=873 IC=+0.041 PNL=+87.65€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=873 IC=+0.041 PNL=+87.65€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=96 IC=+0.031 PNL=+3.09€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=96 IC=+0.031 PNL=+3.09€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.255 n=141) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=141 IC=+0.255 PNL=+122.89€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.127 > 0.02 con n=863 PNL=+362.40€
  - _Datos_: n=863 IC=+0.127 PNL=+362.40€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=202 IC=-0.083 PNL=+23.24€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=202 IC=-0.083 PNL=+23.24€

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
  - _Estado_: n=25980 IC=+0.074 PNL=+3846.96€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=25980 IC=+0.074 PNL=+3846.96€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.135 < -0.1 con n=395 PNL=+50.26€
  - _Datos_: n=395 IC=-0.135 PNL=+50.26€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=2864 IC=+0.065 PNL=+347.74€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2864 IC=+0.065 PNL=+347.74€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=123 IC=-0.116 PNL=+2.24€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=123 IC=-0.116 PNL=+2.24€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.1 con n=679 PNL=+176.27€
  - _Datos_: n=679 IC=+0.115 PNL=+176.27€

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
  - _Estado_: n=27360 IC=-0.135 PNL=+2041.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=27360 IC=-0.135 PNL=+2041.28€

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
  - _Estado_: n=2739 IC=+0.138 PNL=+1631.85€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=2739 IC=+0.138 PNL=+1631.85€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=6993 IC=+0.046 PNL=+531.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=6993 IC=+0.046 PNL=+531.74€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.090 > 0.08 con n=3034 PNL=+1607.17€
  - _Datos_: n=3034 IC=+0.090 PNL=+1607.17€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=2799 PNL=-216.74€
  - _Datos_: n=2799 IC=-0.224 PNL=-216.74€

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
  - _Estado_: n=59 IC=-0.008 PNL=+5.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=59 IC=-0.008 PNL=+5.77€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.097 n=1572) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1572 IC=+0.097 PNL=+334.71€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.413 n=525) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=525 IC=+0.413 PNL=+753.32€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=12353 IC=+0.185 PNL=-1273.67€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=12353 IC=+0.185 PNL=-1273.67€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.1 con n=205 PNL=+128.93€
  - _Datos_: n=205 IC=+0.210 PNL=+128.93€
