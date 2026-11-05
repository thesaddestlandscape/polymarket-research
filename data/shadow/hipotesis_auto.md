# Hipótesis automáticas — 2026-11-05 22:59 UTC
_Generado por shadow_postmortem.py sobre 1210322 resoluciones (PNL=+165223.07€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=690)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.201 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.184 (n=315)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 63.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.6153` → IC=+0.246 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6153 (IC base=+0.132)

- **PATRÓN** `banda_z` > `8.673` → IC=+0.206 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.673 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=1022)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3366.1467` → IC=+0.135 (n=625)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3366.1467 (IC base=+0.132)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.293 (n=167)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=488)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.200 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.135)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.187 (n=273)

  - _Acción_: Kelly boost +0.94€ cuando `n_total_lado` > 66.0 (IC base=+0.135)

- **PATRÓN** `banda_hit_calibrado` > `0.8133` → IC=+0.269 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8133 (IC base=+0.135)

- **PATRÓN** `banda_z` > `9.021` → IC=+0.208 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.021 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=922)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.135)

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
- **FILTRO** `ballenas_wallet_edge_medio` < `2.833` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `ballenas_wallet_edge_medio` < 2.833
  - _Potencial_: sin este filtro IC_bueno=+0.375 (n=6)

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.495 (IC base=+0.162)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.162)

- **PATRÓN** `n_total_lado` > `43.0` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 43.0 (IC base=+0.162)

- **PATRÓN** `banda_hit_calibrado` > `0.6068` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `banda_hit_calibrado` > 0.6068 (IC base=+0.162)

- **PATRÓN** `banda_z` > `2.495` → IC=+0.231 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.495 (IC base=+0.162)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.729` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `ballenas_wallet_edge_medio` > 0.729 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.269 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.214 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `2453.7234` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2453.7234 (IC base=+0.162)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `134.55` → IC=-0.217 (n=11427)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 134.55
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=34292)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `126.72` → IC=-0.251 (n=1183)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 126.72
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3549)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `117.01` → IC=-0.305 (n=1181)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 117.01
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3546)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `118.1` → IC=-0.163 (n=3129)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 118.1
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=9387)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `156.47` → IC=-0.234 (n=3094)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.47
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=9285)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.52` → IC=-0.255 (n=2166)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.52
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=6498)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.211 (n=26194)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `8481.6762` → IC=+0.161 (n=2260)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8481.6762 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=22565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=27282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=20689)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=8031)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6720.2889` → IC=+0.148 (n=3100)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 6720.2889 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=2078)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2666)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `9416.0594` → IC=+0.181 (n=1855)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 9416.0594 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2123)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2720)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16097.2039` → IC=+0.183 (n=702)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16097.2039 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=2099)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.172 (n=572)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.144 (n=1338)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.44 (IC base=+0.083)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.167 (n=4772)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.167 (n=4251)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.214 (n=2265)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` < `0.27` → IC=+0.344 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.27 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=2630)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=1283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.148 (n=1094)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.255 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=1041)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.160 (n=154)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.073)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.257 (n=928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1293)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=1388)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=716)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.147)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `947.2335` → IC=-0.128 (n=154)

  - _Acción_: SKIP cuando `libro_liquidez` < 947.2335
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=314)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=454)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.048)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=1177)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.121)

- **PATRÓN** `py_entrada` < `0.33` → IC=+0.234 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.33 (IC base=+0.121)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=22537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.199 (n=19038)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.227 (n=9377)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.197)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=4864)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.175 (n=5110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4873)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.175 (n=4294)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=2956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=1967)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.288 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.210)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5046)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.179 (n=4278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=5218)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.185 (n=3934)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.256 (n=4285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=3630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.795` → IC=+0.365 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.795 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.249)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.192 (n=4208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=3686)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.428 (n=929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=921)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `3177.3107` → IC=+0.436 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3177.3107 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.449 (n=254)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.456 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12485.1016` → IC=+0.446 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12485.1016 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.429 (n=366)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.426 (n=362)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.435 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.423)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `4669.4566` → IC=+0.434 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4669.4566 (IC base=+0.423)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.399 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.397)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.403 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.397)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.413 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.397)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

- **FILTRO** `libro_liquidez` < `6112.397` → IC=-0.300 (n=33)

  - _Acción_: SKIP cuando `libro_liquidez` < 6112.397
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=17)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=25370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.242 (n=29660)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.190 (n=4398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=9365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=13410)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=6131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4200)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=4356)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.198 (n=10430)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=6195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=4701)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.270 (n=4131)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `3176.5987` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3176.5987
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.213 (n=4204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.257 (n=4320)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.203 (n=4918)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=4874)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=5116)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=10553)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=10951)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.35` → IC=+0.139 (n=9759)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.35 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5155)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4963)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.126 (n=6442)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.61` → IC=+0.143 (n=4853)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.61 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=5398)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.136 (n=6664)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.23` → IC=+0.139 (n=4904)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.23 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.308 (n=1319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.388 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=889)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.367 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.319 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=937)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.394 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.297 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.362 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.339)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.388 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.339)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.368 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.339)

- **PATRÓN** `libro_liquidez` > `720.8183` → IC=+0.371 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 720.8183 (IC base=+0.339)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.443 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.439)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.440 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.439)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=423)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.432)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.435 (n=290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.431 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.438 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.432)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.465 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.448 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.447)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.447 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.447)

- **PATRÓN** `libro_liquidez` > `2330.8635` → IC=+0.456 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2330.8635 (IC base=+0.447)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.417 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.404)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.404)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=91)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.386 (n=42)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.134 (n=91)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4753` → IC=+0.138 (n=16616)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4753 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=16827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=11549)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3728` → IC=+0.165 (n=16615)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3728 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.8048` → IC=+0.281 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8048 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.548` → IC=+0.185 (n=8295)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.548 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6972` → IC=+0.265 (n=4404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6972 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.3036` → IC=+0.249 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3036 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.7361` → IC=+0.233 (n=3973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7361 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=8312)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4696.3122` → IC=+0.145 (n=5539)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4696.3122 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.122 (n=10354)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.5653` → IC=+0.143 (n=20684)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5653 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.6203` → IC=+0.189 (n=1427)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6203 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1631` → IC=+0.189 (n=8038)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1631 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.195 (n=3681)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.6973 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.228 (n=2060)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `1.4568` → IC=+0.204 (n=14227)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4568 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.226 (n=14135)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.080)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3654` → IC=+0.211 (n=3559)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3654 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.224 (n=1733)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2381)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9851` → IC=+0.278 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9851 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.568` → IC=+0.281 (n=1581)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.568 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.263 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.213 (n=3408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.224 (n=3895)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2058.8048` → IC=+0.212 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2058.8048 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.223 (n=3229)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.242 (n=3110)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.245 (n=1411)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0089 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.275 (n=1037)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=1157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.244 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.556` → IC=+0.259 (n=3110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.556 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.245 (n=2812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.249 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4444` → IC=+0.249 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4444 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.8597` → IC=+0.243 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8597 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=3559)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1777.8328` → IC=+0.249 (n=2073)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1777.8328 (IC base=+0.241)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.229 (n=2614)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.0815` → IC=+0.260 (n=990)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0815 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.226 (n=2105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9124` → IC=+0.259 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9124 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1883` → IC=+0.233 (n=1381)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1883 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.537` → IC=+0.225 (n=3224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.537 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.994` → IC=+0.263 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.994 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.226` → IC=+0.223 (n=2968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.226 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.227 (n=2968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.272 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `1.4` → IC=+0.223 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `2.425` → IC=+0.251 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.425 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.151 (n=3137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0063 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0777` → IC=+0.151 (n=1046)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0777 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.144 (n=2236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.7104` → IC=+0.168 (n=3136)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.7104 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.139` → IC=+0.145 (n=3000)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.139 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.727` → IC=+0.130 (n=506)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 10.727 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.001` → IC=+0.135 (n=2874)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.001 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.2012` → IC=+0.135 (n=3136)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2012 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.152 (n=1146)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.138 (n=3011)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=4070)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.166 (n=1296)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 204.0 (IC base=+0.129)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.213 (n=1704)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3953)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.095` → IC=+0.277 (n=820)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.095 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.195 (n=3366)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3528` → IC=+0.220 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3528 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7252` → IC=+0.210 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7252 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=4533)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2035.0984` → IC=+0.202 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2035.0984 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.223 (n=3033)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.1768` → IC=+0.235 (n=1516)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1768 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.221 (n=1562)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` < `0.0415` → IC=+0.270 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0415 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.005` → IC=+0.262 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.005 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.253 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.7627` → IC=+0.221 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7627 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.224 (n=2203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `1916.24` → IC=+0.222 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1916.24 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.221 (n=3285)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.218)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.163 (n=188)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=4526)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.157 (n=639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0038 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.9436` → IC=+0.233 (n=638)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9436 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.1401` → IC=+0.338 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1401 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` < `0.7852` → IC=+0.334 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7852 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.077` → IC=+0.202 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.077 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` > `1.2478` → IC=+0.353 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2478 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` < `0.1669` → IC=+0.333 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1669 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.3014` → IC=+0.335 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3014 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.4207` → IC=+0.342 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4207 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.2709` → IC=+0.341 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2709 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.336 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.0921` → IC=+0.182 (n=1179)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.0921 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `0.7534` → IC=+0.159 (n=297)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.7534 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` < `0.1401` → IC=+0.146 (n=2065)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1401 (IC base=+0.047)

- **PATRÓN** `volumen_regimen` < `0.8348` → IC=+0.156 (n=1481)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8348 (IC base=+0.047)

- **PATRÓN** `volumen_pendiente_norm` > `0.2812` → IC=+0.208 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2812 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` < `1.7747` → IC=+0.147 (n=1425)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.7747 (IC base=+0.047)

- **PATRÓN** `volumen_spike_ratio` > `1.5172` → IC=+0.151 (n=1909)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.5172 (IC base=+0.047)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.189 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=708)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.178 (n=209)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=632)

- **FILTRO** `ibs_20min` > `0.2022` → IC=-0.132 (n=4446)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2022
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=2191)

- **FILTRO** `sigma_ewma_delta_pct` > `8.397` → IC=-0.225 (n=719)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.397
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=5918)

- **PATRÓN** `ibs_20min` > `0.7558` → IC=+0.174 (n=286)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.7558 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` > `0.9797` → IC=+0.275 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9797 (IC base=+0.016)

- **PATRÓN** `dist_vwap_pct` < `0.6239` → IC=+0.262 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6239 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.053` → IC=+0.157 (n=196)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 5.053 (IC base=+0.016)

- **PATRÓN** `volumen_regimen` > `0.6265` → IC=+0.277 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6265 (IC base=+0.016)

- **PATRÓN** `volumen_pendiente_norm` < `0.0797` → IC=+0.282 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0797 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` < `2.4693` → IC=+0.279 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4693 (IC base=+0.016)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.267 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.016)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.266 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.016)

- **PATRÓN** `ibs_20min` < `0.2022` → IC=+0.158 (n=2191)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.2022 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` > `0.219` → IC=+0.288 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.219 (IC base=-0.036)

- **PATRÓN** `dist_vwap_pct` < `0.4923` → IC=+0.281 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4923 (IC base=-0.036)

- **PATRÓN** `volumen_regimen` < `0.6993` → IC=+0.309 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6993 (IC base=-0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.08` → IC=+0.299 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.08 (IC base=-0.036)

- **PATRÓN** `volumen_spike_ratio` < `2.1597` → IC=+0.302 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1597 (IC base=-0.036)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7794` → IC=-0.153 (n=3334)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7794
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=1719)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.167 (n=1134)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=3919)

- **FILTRO** `ibs_20min` > `0.7453` → IC=-0.199 (n=1767)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7453
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=5302)

- **PATRÓN** `ibs_20min` > `0.7794` → IC=+0.122 (n=1719)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.7794 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `1.0349` → IC=+0.359 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0349 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` < `0.249` → IC=+0.306 (n=834)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.249 (IC base=-0.059)

- **PATRÓN** `volumen_regimen` > `0.7065` → IC=+0.321 (n=853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7065 (IC base=-0.059)

- **PATRÓN** `volumen_pendiente_norm` < `0.1064` → IC=+0.308 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1064 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` < `1.5779` → IC=+0.308 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5779 (IC base=-0.059)

- **PATRÓN** `volumen_spike_ratio` > `2.5237` → IC=+0.321 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5237 (IC base=-0.059)

- **PATRÓN** `dist_vwap_pct` > `0.8002` → IC=+0.274 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8002 (IC base=-0.000)

- **PATRÓN** `dist_vwap_pct` < `0.2214` → IC=+0.263 (n=1995)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2214 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` < `0.722` → IC=+0.271 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.722 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` > `1.0638` → IC=+0.284 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0638 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.1708` → IC=+0.285 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1708 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `2.1776` → IC=+0.266 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1776 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.270 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4406 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.198 (n=7198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0105 (IC base=+0.089)

- **PATRÓN** `ibs_20min` > `0.8723` → IC=+0.287 (n=9774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8723 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.9538` → IC=+0.303 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9538 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.518` → IC=+0.168 (n=9652)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.518 (IC base=+0.089)

- **PATRÓN** `volumen_regimen` > `0.693` → IC=+0.275 (n=7069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.693 (IC base=+0.089)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.291 (n=1791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.089)

- **PATRÓN** `volumen_spike_ratio` > `2.6487` → IC=+0.283 (n=4180)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6487 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.307 (n=12158)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.089)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.159 (n=6932)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0101 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.6431` → IC=+0.152 (n=20791)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.6431 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.2575` → IC=+0.278 (n=6896)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2575 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `0.7011` → IC=+0.281 (n=2987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7011 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `1.1926` → IC=+0.277 (n=2261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1926 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2943` → IC=+0.323 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2943 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `1.4554` → IC=+0.302 (n=3327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4554 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `2.2768` → IC=+0.297 (n=4525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2768 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.307 (n=9942)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.080)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8018` → IC=-0.124 (n=3868)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8018
  - _Potencial_: sin este filtro IC_bueno=+0.296 (n=1994)

- **FILTRO** `ibs_20min` > `0.7206` → IC=-0.231 (n=1287)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7206
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=3863)

- **FILTRO** `sigma_ewma_delta_pct` > `4.169` → IC=-0.231 (n=1108)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.169
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=4042)

- **PATRÓN** `ibs_20min` > `0.9341` → IC=+0.337 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9341 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.049` → IC=+0.188 (n=1962)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.049 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.325 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` < `1.4484` → IC=+0.277 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4484 (IC base=+0.019)

- **PATRÓN** `volumen_spike_ratio` > `2.2395` → IC=+0.299 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2395 (IC base=+0.019)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.315 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.019)

- **PATRÓN** `ibs_20min` < `0.1714` → IC=+0.162 (n=1289)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1714 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.0716` → IC=+0.406 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0716 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4222` → IC=+0.428 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4222 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.399 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1233` → IC=+0.220 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1233 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.206 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.195 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.208 (n=2101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.247 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.417` → IC=+0.228 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.417 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.4426` → IC=+0.206 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4426 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `265.0` → IC=+0.241 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 265.0 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.253 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1327 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `0.6219` → IC=+0.248 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6219 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.313 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5307` → IC=+0.252 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5307 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.261 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.261 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 214.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.319 (n=2035)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.290 (n=3052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1658)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.638` → IC=+0.300 (n=2023)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.638 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.293 (n=2670)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `1.6038` → IC=+0.287 (n=2958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6038 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.290 (n=3646)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `2035.0984` → IC=+0.296 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2035.0984 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.305 (n=1917)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.320 (n=2447)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.320 (n=1207)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.325 (n=1054)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.304 (n=1235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` < `0.0132` → IC=+0.303 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0132 (IC base=+0.302)

- **PATRÓN** `ibs_20min` > `0.1388` → IC=+0.312 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1388 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.269` → IC=+0.311 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.269 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` < `0.1989` → IC=+0.302 (n=2695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1989 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.307 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `1.7516` → IC=+0.303 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7516 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `2.7242` → IC=+0.315 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7242 (IC base=+0.302)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.304 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `1917.7208` → IC=+0.312 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.7208 (IC base=+0.302)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.308 (n=2310)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.302)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7282` → IC=-0.181 (n=1342)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7282
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=4030)

- **PATRÓN** `ibs_20min` > `0.8519` → IC=+0.166 (n=1316)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8519 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.1489` → IC=+0.233 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1489 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.3636` → IC=+0.232 (n=1844)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3636 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1628` → IC=+0.233 (n=1894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1628 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6716` → IC=+0.232 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6716 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.1619` → IC=+0.234 (n=1986)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1619 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.240 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4563` → IC=+0.236 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4563 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.254 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 116.0 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.7503` → IC=+0.256 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7503 (IC base=+0.005)

- **PATRÓN** `dist_vwap_pct` < `0.3545` → IC=+0.246 (n=1485)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3545 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.252 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.308 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `1.793` → IC=+0.281 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.793 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `2.4323` → IC=+0.269 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4323 (IC base=+0.005)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.278 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 100.0 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7451` → IC=-0.241 (n=2232)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7451
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2233)

- **FILTRO** `ibs_20min` > `0.625` → IC=-0.230 (n=1070)

  - _Acción_: SKIP cuando `ibs_20min` > 0.625
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=3211)

- **FILTRO** `sigma_ewma_delta_pct` > `8.311` → IC=-0.251 (n=492)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.311
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=3789)

- **PATRÓN** `ibs_20min` > `0.7451` → IC=+0.312 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7451 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `1.0638` → IC=+0.356 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0638 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.479` → IC=+0.152 (n=1811)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 2.479 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8458` → IC=+0.340 (n=1090)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8458 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6974` → IC=+0.334 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6974 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.333 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.358 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.4314` → IC=+0.361 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4314 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.354 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 45.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.625` → IC=+0.149 (n=3211)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.625 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.3066` → IC=+0.263 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3066 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.748` → IC=+0.120 (n=3362)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` < 4.748 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.290 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.695 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.282 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `2.4345` → IC=+0.270 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4345 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.285 (n=1541)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.054)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.358 (n=2041)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1082)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` > `0.669` → IC=+0.345 (n=2284)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.669 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` > `0.2098` → IC=+0.340 (n=1275)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2098 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.806` → IC=+0.332 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.806 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `0.8714` → IC=+0.333 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8714 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.345 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `1.4298` → IC=+0.326 (n=2198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4298 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2972.8106` → IC=+0.326 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2972.8106 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.344 (n=2032)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.315)

- **PATRÓN** `sigma_h` > `0.0154` → IC=+0.347 (n=1619)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0154 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.322 (n=1239)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` < `0.38` → IC=+0.335 (n=2429)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.38 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` < `0.2391` → IC=+0.321 (n=2334)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2391 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.621` → IC=+0.331 (n=898)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.621 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` < `0.7189` → IC=+0.321 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7189 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `1.2089` → IC=+0.343 (n=809)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2089 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.23` → IC=+0.361 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.23 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` < `1.4117` → IC=+0.326 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4117 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `2.1375` → IC=+0.316 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1375 (IC base=+0.315)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.225 (n=5362)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.1227` → IC=+0.193 (n=7076)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1227 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=16691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.5393` → IC=+0.232 (n=16078)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5393 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.164` → IC=+0.206 (n=6276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.164 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.896` → IC=+0.259 (n=3142)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.896 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.1857` → IC=+0.156 (n=10703)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1857 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `0.6264` → IC=+0.155 (n=10703)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6264 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.209 (n=2325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6076` → IC=+0.191 (n=5210)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6076 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.195 (n=15005)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 89.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.191 (n=6932)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0057 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.0804` → IC=+0.220 (n=5236)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0804 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=7524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` < `0.5208` → IC=+0.239 (n=15703)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5208 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `0.1823` → IC=+0.177 (n=11289)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.1823 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.648` → IC=+0.192 (n=2508)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.648 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.559` → IC=+0.188 (n=13969)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.559 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.1802` → IC=+0.165 (n=11183)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1802 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2936` → IC=+0.216 (n=2343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2936 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6308` → IC=+0.189 (n=4969)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6308 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.198 (n=14680)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 93.0 (IC base=+0.183)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.227 (n=888)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1047` → IC=+0.258 (n=1166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1047 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=2764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1793)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.8089` → IC=+0.274 (n=2368)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8089 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.601` → IC=+0.329 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.601 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.292 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.8326` → IC=+0.223 (n=1683)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8326 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.227 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=2924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.257 (n=2142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.256 (n=971)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0974` → IC=+0.306 (n=941)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0974 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.261 (n=2209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.260 (n=1016)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.0471` → IC=+0.301 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0471 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.259 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.274 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4445` → IC=+0.282 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4445 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.7098` → IC=+0.260 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7098 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=2457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1779.9298` → IC=+0.265 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1779.9298 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.255 (n=2047)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 31.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.198 (n=823)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0031 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0652` → IC=+0.179 (n=818)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0652 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=2570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` > `0.2666` → IC=+0.209 (n=2452)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2666 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1866` → IC=+0.213 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1866 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.761` → IC=+0.207 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.761 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6959` → IC=+0.144 (n=1079)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6959 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` > `1.0614` → IC=+0.138 (n=1112)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0614 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.182 (n=379)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `1.5013` → IC=+0.141 (n=1060)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5013 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `2.4674` → IC=+0.150 (n=803)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.4674 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `403.0` → IC=+0.138 (n=2379)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 403.0 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.172 (n=2595)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0063 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.2389` → IC=+0.168 (n=2281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2389 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=1243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` < `0.6089` → IC=+0.206 (n=2593)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6089 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.995` → IC=+0.177 (n=487)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.995 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.032` → IC=+0.150 (n=2266)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.032 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.160 (n=2593)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2032 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.149 (n=2247)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `2.452` → IC=+0.150 (n=2468)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.452 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.186 (n=1061)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 213.0 (IC base=+0.146)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.233 (n=1235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.211)

- **PATRÓN** `drift_60min` |x|≤ `0.3961` → IC=+0.224 (n=2398)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3961 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.232 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.211)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.295 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.161` → IC=+0.305 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.161 (IC base=+0.211)

- **PATRÓN** `volumen_pendiente_norm` > `0.3544` → IC=+0.235 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3544 (IC base=+0.211)

- **PATRÓN** `volumen_spike_ratio` > `2.7154` → IC=+0.224 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7154 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=3284)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1922.1952` → IC=+0.222 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1922.1952 (IC base=+0.211)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.246 (n=2100)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.4174` → IC=+0.261 (n=2097)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4174 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.282 (n=914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.0323` → IC=+0.289 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0323 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.158` → IC=+0.279 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.158 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.3581` → IC=+0.282 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3581 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.7663` → IC=+0.243 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7663 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.245 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1911.1684` → IC=+0.251 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1911.1684 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.244 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.238)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.207 (n=883)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.0789` → IC=+0.191 (n=880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.0789 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` > `0.2619` → IC=+0.195 (n=2637)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` > 0.2619 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.1416` → IC=+0.188 (n=1564)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1416 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.378` → IC=+0.203 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.378 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `0.8476` → IC=+0.141 (n=1760)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8476 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` > `1.1852` → IC=+0.136 (n=879)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.1852 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.180 (n=395)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.8246` → IC=+0.133 (n=1721)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8246 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` > `2.5287` → IC=+0.156 (n=861)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5287 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `6919.7421` → IC=+0.197 (n=1196)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6919.7421 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.141 (n=2579)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 130.0 (IC base=+0.135)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.167 (n=2461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0066 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3985` → IC=+0.146 (n=2797)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3985 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6735` → IC=+0.187 (n=2797)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6735 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1607` → IC=+0.157 (n=2805)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1607 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.329` → IC=+0.145 (n=672)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.329 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.155 (n=1865)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8521 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.175 (n=419)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.2038` → IC=+0.132 (n=2330)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.2038 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4181` → IC=+0.129 (n=2647)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4181 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `6344.3973` → IC=+0.191 (n=1268)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 6344.3973 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.150 (n=876)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 50.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.169 (n=1333)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0112 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.160 (n=1411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 15.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.4717` → IC=+0.209 (n=2940)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4717 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.2015` → IC=+0.190 (n=1620)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.2015 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.146` → IC=+0.290 (n=621)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.146 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.175` → IC=+0.133 (n=2940)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.175 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.7041` → IC=+0.124 (n=2626)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7041 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1632` → IC=+0.130 (n=2994)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1632 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4362` → IC=+0.135 (n=951)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4362 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=3069)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2667.202` → IC=+0.200 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2667.202 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.149 (n=1225)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 20.0 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.143 (n=3063)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0118 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.162 (n=1021)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=3138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6442` → IC=+0.219 (n=3062)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6442 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.2138` → IC=+0.146 (n=2973)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2138 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.298` → IC=+0.139 (n=2701)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 2.298 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.174` → IC=+0.130 (n=3062)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.174 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.123 (n=3003)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2742` → IC=+0.134 (n=419)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2742 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4321` → IC=+0.133 (n=962)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4321 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `1.7939` → IC=+0.125 (n=1924)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.7939 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2911.9343` → IC=+0.195 (n=1021)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2911.9343 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.126 (n=2852)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 45.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.250 (n=2390)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1655` → IC=+0.241 (n=1177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1655 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=2775)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=2413)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.259 (n=2677)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1809` → IC=+0.235 (n=1687)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1809 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8225` → IC=+0.227 (n=2744)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8225 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.578` → IC=+0.253 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.578 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6261` → IC=+0.234 (n=2675)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6261 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2353` → IC=+0.270 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2353 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8143` → IC=+0.235 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8143 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2841.8146` → IC=+0.233 (n=1213)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2841.8146 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.241 (n=1205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.249 (n=1243)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.5667` → IC=+0.246 (n=2734)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5667 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1350)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1213)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.4398` → IC=+0.264 (n=2734)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4398 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `1.1261` → IC=+0.255 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1261 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.196` → IC=+0.265 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.196 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8636` → IC=+0.244 (n=1823)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8636 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.641` → IC=+0.242 (n=2733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.641 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.288 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `2.5291` → IC=+0.235 (n=2569)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5291 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.4348` → IC=+0.240 (n=2568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4348 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.211 (n=1384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.1323` → IC=+0.180 (n=1820)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.1323 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.175 (n=4345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `0.439` → IC=+0.208 (n=3696)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.439 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.8314` → IC=+0.190 (n=662)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.8314 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.667` → IC=+0.208 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.667 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `0.8632` → IC=+0.177 (n=2511)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.8632 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `1.1944` → IC=+0.171 (n=1255)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` > 1.1944 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.173 (n=1665)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.171 (n=1774)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 1.5317 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.166 (n=4636)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `2162.745` → IC=+0.174 (n=4137)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2162.745 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.170 (n=2972)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.3846 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.133 (n=1918)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 26.0 (IC base=+0.092)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.196 (n=1115)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0061 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3283` → IC=+0.195 (n=1114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.3283 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.212 (n=1007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.2116` → IC=+0.209 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2116 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.3098` → IC=+0.215 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3098 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.956` → IC=+0.203 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.956 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.190 (n=744)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.8803 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.189 (n=438)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `2.1853` → IC=+0.191 (n=961)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 2.1853 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `15844.7122` → IC=+0.194 (n=505)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 15844.7122 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `159.0` → IC=+0.184 (n=483)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 159.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.166 (n=453)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0031 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.1939` → IC=+0.199 (n=596)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1939 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.144 (n=355)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.175 (n=583)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 160.0 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.248 (n=565)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.2101` → IC=+0.186 (n=857)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.2101 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=1343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.8149` → IC=+0.269 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8149 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.8414` → IC=+0.194 (n=217)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.8414 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.2103` → IC=+0.179 (n=1146)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.2103 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.884` → IC=+0.221 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.884 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.194 (n=857)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8342 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `1.1591` → IC=+0.179 (n=428)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.1591 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.212 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.5247` → IC=+0.182 (n=558)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.5247 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `1.7865` → IC=+0.192 (n=844)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.7865 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.0976` → IC=+0.185 (n=423)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.0976 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `5242.1024` → IC=+0.135 (n=844)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 5242.1024 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.122 (n=543)

  - _Acción_: Kelly boost +0.61€ cuando `ballena_activa_n` < 42.0 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.155 (n=447)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.167 (n=724)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 11.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4643` → IC=+0.185 (n=1015)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.4643 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.9822` → IC=+0.193 (n=174)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.9822 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.989` → IC=+0.234 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.989 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.0501` → IC=+0.135 (n=893)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.0501 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.7037` → IC=+0.133 (n=908)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 0.7037 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2267` → IC=+0.156 (n=190)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.2267 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4223` → IC=+0.136 (n=328)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4223 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `1.802` → IC=+0.125 (n=654)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.802 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=1068)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2718.5359` → IC=+0.170 (n=461)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2718.5359 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.3636` → IC=+0.185 (n=734)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.3636 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `2589.7365` → IC=+0.147 (n=499)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2589.7365 (IC base=+0.060)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.017` → IC=+0.239 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.017 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `0.725` → IC=+0.218 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.725 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` > `0.2222` → IC=+0.217 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2222 (IC base=+0.191)

- **PATRÓN** `dist_vwap_pct` < `1.1958` → IC=+0.193 (n=398)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 1.1958 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.385` → IC=+0.217 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.385 (IC base=+0.191)

- **PATRÓN** `volumen_regimen` > `1.1751` → IC=+0.250 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1751 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` < `0.1049` → IC=+0.205 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1049 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` < `2.1265` → IC=+0.215 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1265 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `1.4232` → IC=+0.200 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4232 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.201 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `2591.9144` → IC=+0.223 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2591.9144 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.203 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2963` → IC=+0.158 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2963 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.168 (n=338)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.5 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `1.2117` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.2117 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.183 (n=102)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.189` → IC=+0.145 (n=342)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.189 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.8733` → IC=+0.185 (n=255)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.8733 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.1126` → IC=+0.157 (n=351)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1126 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5142` → IC=+0.202 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5142 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.6655` → IC=+0.185 (n=122)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6655 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.160 (n=363)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 20.0 (IC base=+0.145)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.231 (n=7008)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=21944)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4324` → IC=+0.229 (n=21026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4324 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8997` → IC=+0.215 (n=2551)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8997 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.021` → IC=+0.255 (n=5145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.021 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2171` → IC=+0.161 (n=14136)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2171 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2412` → IC=+0.208 (n=3784)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2412 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6176` → IC=+0.193 (n=6837)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6176 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.202 (n=19665)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 105.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.197 (n=8496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0059 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.200 (n=6423)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4832` → IC=+0.196 (n=19260)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4832 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=7221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5909` → IC=+0.243 (n=19269)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5909 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.1801` → IC=+0.175 (n=11989)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1801 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.512` → IC=+0.198 (n=2607)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.512 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.428` → IC=+0.197 (n=18763)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 3.428 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.7036` → IC=+0.175 (n=5692)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.7036 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.249 (n=2633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.6258` → IC=+0.203 (n=6131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6258 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.208 (n=18135)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.193)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2273)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.8625` → IC=+0.301 (n=2254)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8625 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.633` → IC=+0.339 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.633 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.294 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.2779` → IC=+0.242 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2779 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.250 (n=3688)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2055.3409` → IC=+0.237 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2055.3409 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.257 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.268 (n=2996)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.123` → IC=+0.291 (n=1317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.123 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=2711)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.4554` → IC=+0.292 (n=2633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4554 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.1599` → IC=+0.268 (n=3006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1599 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.289` → IC=+0.285 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.289 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.268 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.653` → IC=+0.275 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.653 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.267 (n=3427)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1779.3496` → IC=+0.275 (n=1994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1779.3496 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.275 (n=1023)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.180 (n=1153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0031 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.149 (n=1148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=3592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.2046` → IC=+0.189 (n=3444)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2046 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1829` → IC=+0.191 (n=1510)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1829 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.232` → IC=+0.161 (n=552)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.232 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6362` → IC=+0.157 (n=1148)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6362 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.2316` → IC=+0.139 (n=1148)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.2316 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2707` → IC=+0.181 (n=490)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2707 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1536` → IC=+0.142 (n=2973)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1536 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5137` → IC=+0.140 (n=3018)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5137 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `304.0` → IC=+0.150 (n=2216)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 304.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.162 (n=2933)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0793` → IC=+0.170 (n=977)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0793 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=1082)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.6828` → IC=+0.186 (n=2931)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6828 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` < `0.1415` → IC=+0.152 (n=2814)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1415 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.044` → IC=+0.141 (n=1395)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 3.044 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.03` → IC=+0.138 (n=2658)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.03 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.147 (n=2932)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1917 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2184` → IC=+0.193 (n=542)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2184 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.409` → IC=+0.142 (n=2821)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.409 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.7688` → IC=+0.141 (n=1881)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7688 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=3806)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `228.0` → IC=+0.153 (n=919)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 228.0 (IC base=+0.138)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.243 (n=2337)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3678)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=3132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.106` → IC=+0.322 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.106 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.226 (n=3136)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7369` → IC=+0.238 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7369 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=4220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1928.6136` → IC=+0.236 (n=1591)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1928.6136 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.247 (n=2935)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1797` → IC=+0.262 (n=1468)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1797 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.303 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.235` → IC=+0.301 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.235 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3489` → IC=+0.303 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3489 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1698` → IC=+0.253 (n=2135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1698 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.248 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1912.76` → IC=+0.253 (n=1511)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1912.76 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.247 (n=2770)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.195 (n=1210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0037 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4338` → IC=+0.147 (n=3627)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4338 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=3768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8935` → IC=+0.275 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8935 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1967` → IC=+0.168 (n=1686)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1967 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.985` → IC=+0.159 (n=1615)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.985 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8612` → IC=+0.153 (n=2418)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8612 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2329` → IC=+0.186 (n=642)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2329 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5199` → IC=+0.154 (n=1561)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5199 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.178` → IC=+0.145 (n=1607)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.178 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5476.0442` → IC=+0.229 (n=1644)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5476.0442 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.149 (n=2344)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 90.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.166 (n=2686)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0067 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4405` → IC=+0.149 (n=3047)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4405 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=1125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.5819` → IC=+0.207 (n=2681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5819 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1533` → IC=+0.153 (n=2817)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1533 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.022` → IC=+0.155 (n=606)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.022 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.077` → IC=+0.142 (n=2654)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.077 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.69` → IC=+0.158 (n=1341)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.69 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.210 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.2114` → IC=+0.142 (n=2588)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.2114 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5362` → IC=+0.148 (n=2627)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5362 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `6331.5198` → IC=+0.215 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6331.5198 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.151 (n=2008)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 93.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.151 (n=1668)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0112 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=2602)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4314` → IC=+0.192 (n=3673)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4314 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0297` → IC=+0.204 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0297 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.363` → IC=+0.269 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.363 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.8775` → IC=+0.133 (n=2450)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8775 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.123 (n=3483)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.4818` → IC=+0.122 (n=3587)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4818 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=3841)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2719.215` → IC=+0.241 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2719.215 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.132 (n=1184)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 20.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.156 (n=3059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0108 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.1374` → IC=+0.153 (n=1158)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1374 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.66` → IC=+0.216 (n=3472)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.66 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.2199` → IC=+0.144 (n=3115)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2199 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.075` → IC=+0.151 (n=3361)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.075 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6385` → IC=+0.157 (n=1158)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6385 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2252` → IC=+0.176 (n=606)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2252 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4331` → IC=+0.159 (n=1097)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.4331 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2630.7334` → IC=+0.210 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2630.7334 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.140 (n=3331)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 51.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.260 (n=3032)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.243 (n=3547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.241 (n=3043)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.615` → IC=+0.273 (n=3033)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.615 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.1938` → IC=+0.254 (n=1806)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1938 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.223` → IC=+0.285 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.223 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `1.2206` → IC=+0.240 (n=3394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2206 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6448` → IC=+0.242 (n=3394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6448 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.239` → IC=+0.261 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.239 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.4995` → IC=+0.258 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4995 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `2966.5706` → IC=+0.247 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2966.5706 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.264 (n=1163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.6231` → IC=+0.241 (n=3488)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6231 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.245 (n=3296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.52` → IC=+0.271 (n=3489)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.52 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` < `0.8539` → IC=+0.243 (n=3975)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8539 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.14` → IC=+0.279 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.14 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` > `1.2146` → IC=+0.261 (n=1163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2146 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.302 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `1.4345` → IC=+0.243 (n=3279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4345 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.239 (n=3243)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.240)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5765)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.244 (n=1986)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.5053` → IC=+0.226 (n=5933)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5053 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=2145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9347` → IC=+0.256 (n=1977)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9347 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.4291` → IC=+0.221 (n=4326)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4291 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.569` → IC=+0.225 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.569 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.7092` → IC=+0.230 (n=1928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7092 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.8843` → IC=+0.219 (n=2920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8843 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.219 (n=5532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.1652` → IC=+0.224 (n=1677)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1652 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `1.4524` → IC=+0.227 (n=1947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4524 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=4638)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `3754.865` → IC=+0.227 (n=3954)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3754.865 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.237 (n=1449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.212 (n=4336)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=1457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.214 (n=1918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.6132` → IC=+0.205 (n=3815)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6132 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6592` → IC=+0.209 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6592 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.785` → IC=+0.211 (n=3890)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.785 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.0954` → IC=+0.206 (n=3637)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0954 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.202 (n=3995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.200 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5315` → IC=+0.203 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5315 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1849` → IC=+0.208 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1849 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5765)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `65.0` → IC=+0.214 (n=2845)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 65.0 (IC base=+0.199)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.276 (n=814)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.297 (n=309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.279 (n=925)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.8328` → IC=+0.278 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.8328 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` < `0.6679` → IC=+0.277 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6679 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.300 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `0.8749` → IC=+0.288 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8749 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.351 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `1.8139` → IC=+0.271 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8139 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1895` → IC=+0.269 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1895 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `12909.5134` → IC=+0.279 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12909.5134 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.189 (n=1519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.184 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.138` → IC=+0.197 (n=668)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.138 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.315` → IC=+0.198 (n=1488)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.315 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.0915` → IC=+0.188 (n=1336)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0915 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1519` → IC=+0.195 (n=463)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1519 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `1.4126` → IC=+0.194 (n=504)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4126 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.1703` → IC=+0.180 (n=685)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.1703 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.179 (n=689)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `686.0` → IC=+0.188 (n=1473)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 686.0 (IC base=+0.176)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.233 (n=301)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.5907` → IC=+0.207 (n=903)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5907 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.233 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.245 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.463` → IC=+0.248 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.463 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.2068` → IC=+0.233 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2068 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.8037` → IC=+0.208 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8037 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.209 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.286 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.216` → IC=+0.258 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.216 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.971` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.971 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `2.3165` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.3165 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.7721` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7721 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.218 (n=1624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.4542` → IC=+0.213 (n=1624)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4542 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` < `0.4996` → IC=+0.216 (n=1083)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4996 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.8555` → IC=+0.206 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8555 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.3956` → IC=+0.215 (n=1626)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3956 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.529` → IC=+0.210 (n=1649)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.529 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` < `0.7067` → IC=+0.211 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7067 (IC base=+0.204)

- **PATRÓN** `volumen_regimen` > `1.2249` → IC=+0.204 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2249 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` < `0.1029` → IC=+0.209 (n=1494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1029 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` < `2.4535` → IC=+0.212 (n=1590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4535 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1689)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.243 (n=450)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.4865` → IC=+0.222 (n=1348)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4865 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.212 (n=508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.218 (n=914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.748` → IC=+0.204 (n=1348)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.748 (IC base=+0.202)

- **PATRÓN** `ibs_20min` > `0.0909` → IC=+0.206 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0909 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.6238` → IC=+0.218 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6238 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.2204` → IC=+0.202 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2204 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.352` → IC=+0.206 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.352 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `0.6394` → IC=+0.230 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6394 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.0741` → IC=+0.228 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0741 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `2.1876` → IC=+0.208 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1876 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `1.7831` → IC=+0.203 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7831 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `6470.4651` → IC=+0.206 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6470.4651 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.203 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 98.0 (IC base=+0.202)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.223 (n=630)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.234 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.7706` → IC=+0.236 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7706 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.208` → IC=+0.222 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.208 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.6421` → IC=+0.244 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6421 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.206 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.079` → IC=+0.203 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.079 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.1444` → IC=+0.203 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1444 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `1.4745` → IC=+0.203 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4745 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.207 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `4323.865` → IC=+0.241 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4323.865 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.203 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.237 (n=459)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.5959` → IC=+0.239 (n=688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5959 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.222 (n=641)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.250 (n=478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.6479` → IC=+0.248 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6479 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.5347` → IC=+0.224 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5347 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.791` → IC=+0.235 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.791 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` < `1.0973` → IC=+0.225 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0973 (IC base=+0.221)

- **PATRÓN** `volumen_regimen` > `1.2815` → IC=+0.228 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2815 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` < `0.0825` → IC=+0.238 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0825 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.5641` → IC=+0.261 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5641 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `3792.9162` → IC=+0.235 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3792.9162 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.259 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.221)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.149 (n=699)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0037 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.188 (n=1349)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.75 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1492` → IC=+0.138 (n=1013)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1492 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.476` → IC=+0.146 (n=444)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.476 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.265 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.1439` → IC=+0.132 (n=373)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.1439 (IC base=+0.048)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5272` → IC=-0.125 (n=281)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5272
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=572)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.125 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0051 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5272` → IC=+0.167 (n=572)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.5272 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1218` → IC=+0.166 (n=312)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1218 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.281 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.167 (n=109)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.050)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.53` → IC=-0.124 (n=285)

  - _Acción_: SKIP cuando `ibs_20min` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.172 (n=581)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.125 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0051 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.53` → IC=+0.172 (n=581)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.53 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1273` → IC=+0.174 (n=326)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1273 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.677` → IC=+0.203 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.677 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.270 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.593` → IC=+0.227 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.593 (IC base=+0.027)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.200 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.729` → IC=+0.141 (n=154)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 8.729 (IC base=+0.022)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.148 (n=350)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0112 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.169 (n=367)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.4857 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2779` → IC=+0.122 (n=371)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2779 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.070)

- **PATRÓN** `volumen_regimen` > `1.0862` → IC=+0.164 (n=123)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.0862 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.446` → IC=+0.123 (n=340)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` > 1.446 (IC base=+0.070)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.300 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=266)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=339)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.309 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=171)

- **FILTRO** `dist_vwap_pct` > `0.4617` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4617
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=302)

- **FILTRO** `sigma_ewma_delta_pct` > `9.86` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.86
  - _Potencial_: sin este filtro IC_bueno=-0.280 (n=294)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=202)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.280 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=59)

- **FILTRO** `volumen_regimen` < `0.8856` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8856
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=81)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=74)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.300 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=73)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.232 (n=110)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.469 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=90)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.365 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=88)

- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.407 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=82)

- **FILTRO** `volumen_spike_ratio` < `1.7371` → IC=-0.370 (n=44)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.7371
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=45)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.309 (n=108)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=109)

- **FILTRO** `volumen_pendiente_norm` > `0.1362` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1362
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=72)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=98)

- **FILTRO** `sigma_h` < `0.0107` → IC=-0.329 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=37)

- **FILTRO** `volumen_regimen` < `0.9051` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9051
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=35)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2374` → IC=-0.162 (n=258)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2374
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=777)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.218 (n=303)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.193 (n=346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.178 (n=666)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6757 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.8192` → IC=+0.281 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8192 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.656` → IC=+0.151 (n=368)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.656 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.649` → IC=+0.141 (n=677)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 8.649 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.174 (n=222)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6249 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` < `0.2094` → IC=+0.162 (n=623)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` < 0.2094 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.3876` → IC=+0.182 (n=187)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.3876 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.136` → IC=+0.122 (n=684)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.136 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.855` → IC=+0.161 (n=228)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 8.855 (IC base=+0.039)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7782` → IC=-0.140 (n=87)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7782
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=177)

- **PATRÓN** `ibs_20min` > `0.7782` → IC=+0.120 (n=177)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` > 0.7782 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.6267` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6267 (IC base=+0.034)

- **PATRÓN** `ibs_20min` < `0.215` → IC=+0.164 (n=361)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.215 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.706` → IC=+0.134 (n=110)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 9.706 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2254` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2254 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.1034` → IC=+0.145 (n=150)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1034 (IC base=+0.096)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1248` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1248
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=217)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.142 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0042 (IC base=+0.116)

- **PATRÓN** `drift_60min` |x|≤ `0.1946` → IC=+0.122 (n=146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.1946 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.116)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.155 (n=195)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.8015 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.146 (n=176)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.634` → IC=+0.140 (n=226)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 9.634 (IC base=+0.116)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.167 (n=73)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6244 (IC base=+0.116)

- **PATRÓN** `volumen_pendiente_norm` < `0.1248` → IC=+0.158 (n=217)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1248 (IC base=+0.116)

- **PATRÓN** `volumen_spike_ratio` < `2.1181` → IC=+0.151 (n=167)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.1181 (IC base=+0.116)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=187)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.689` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.689 (IC base=+0.019)

- **PATRÓN** `volumen_pendiente_norm` > `0.2228` → IC=+0.130 (n=52)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` > 0.2228 (IC base=+0.019)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=122)

- **FILTRO** `dist_vwap_pct` > `0.1813` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1813
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=143)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.294 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.278 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.240)

- **PATRÓN** `dist_vwap_pct` > `0.6973` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6973 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.352 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.240)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.291 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.313 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.4721` → IC=+0.330 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4721 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.977` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.977 (IC base=-0.071)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=100)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.325)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.325)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.325)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.372 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.325)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.395 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.325)

- **PATRÓN** `ballena_activa_n` < `1220.0` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1220.0 (IC base=+0.325)

- **PATRÓN** `drift_ventana_pct` |x|> `0.345` → IC=+0.278 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.345 (IC base=+0.248)

- **PATRÓN** `elapsed_s` < `203.0` → IC=+0.254 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.0 (IC base=+0.248)

- **PATRÓN** `drift_15min` |x|≤ `1.234` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.234 (IC base=+0.248)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.287 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.248)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.248)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.336 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.248)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.314 (n=100)

- **PATRÓN** `drift_ventana_pct` |x|> `0.349` → IC=+0.333 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.349 (IC base=+0.325)

- **PATRÓN** `elapsed_s` > `187.1` → IC=+0.373 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.1 (IC base=+0.325)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.429 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.325)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.372 (n=76)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.325)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.395 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.325)

- **PATRÓN** `ballena_activa_n` < `1220.0` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1220.0 (IC base=+0.325)

- **PATRÓN** `drift_ventana_pct` |x|> `0.345` → IC=+0.278 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.345 (IC base=+0.248)

- **PATRÓN** `elapsed_s` < `203.0` → IC=+0.254 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.0 (IC base=+0.248)

- **PATRÓN** `drift_15min` |x|≤ `1.234` → IC=+0.344 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.234 (IC base=+0.248)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.287 (n=59)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.248)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.314 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.248)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.336 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.248)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=240)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=240)

- **FILTRO** `libro_liquidez` < `6623.9156` → IC=-0.146 (n=128)

  - _Acción_: SKIP cuando `libro_liquidez` < 6623.9156
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=128)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=635)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=96)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4139.65` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `liq_usd_total` < 4139.65
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.139 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 6.0 (IC base=+0.053)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3893)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=127)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=84)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=114)

- **FILTRO** `ballena_activa_n` > `33.0` → IC=-0.178 (n=85)

  - _Acción_: SKIP cuando `ballena_activa_n` > 33.0
  - _Potencial_: sin este filtro IC_bueno=+0.210 (n=29)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.141 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=143)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=22)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `libro_liquidez` < `13988.6712` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 13988.6712
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

- **FILTRO** `ballena_activa_n` > `558.0` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `ballena_activa_n` > 558.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=272)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1588)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1542)

- **FILTRO** `liq_n` < `3.0` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `liq_n` < 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `liq_usd_total` < `6520.36` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 6520.36
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `ballena_activa_n` > `133.0` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `ballena_activa_n` > 133.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=724)

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
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=441)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=422)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.149 (n=186)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=960)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=960)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1155)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=1155)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=263)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=263)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.138 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=200)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.146 (n=63)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=326)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=374)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=295)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=387)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=387)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=232)

- **FILTRO** `libro_liquidez` < `657.5195` → IC=-0.133 (n=137)

  - _Acción_: SKIP cuando `libro_liquidez` < 657.5195
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=280)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=329)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.59` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=69)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.188 (n=75)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=87)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.180 (n=73)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=89)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.241 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=56)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.47` → IC=+0.146 (n=235)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.47 (IC base=-0.009)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.137 (n=265)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=543)

- **FILTRO** `profundidad_ratio` < `63.9` → IC=-0.127 (n=266)

  - _Acción_: SKIP cuando `profundidad_ratio` < 63.9
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=542)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.126 (n=319)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=341)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.176 (n=137)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=598)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.122 (n=490)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=262)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.158 (n=109)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=336)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.129 (n=443)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=443)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.172 (n=7390)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=23681)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.174 (n=7894)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=24183)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.184 (n=1427)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=4306)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.147 (n=1901)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=3795)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.124 (n=2929)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.169 (n=1023)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=3334)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.179 (n=1128)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=3405)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.204 (n=1409)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=4415)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.133 (n=1950)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9643 (IC base=+0.035)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.58` → IC=-0.181 (n=1070)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=3509)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.152 (n=1436)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4335)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2428)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2352)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=2960)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3912)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=352)

- **FILTRO** `drift_20min_pct` |x|> `0.1569` → IC=-0.144 (n=158)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1569
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=307)

- **FILTRO** `libro_liquidez` < `3201.9988` → IC=-0.184 (n=153)

  - _Acción_: SKIP cuando `libro_liquidez` < 3201.9988
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=312)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=964)

- **FILTRO** `libro_liquidez` < `1813.405` → IC=-0.164 (n=245)

  - _Acción_: SKIP cuando `libro_liquidez` < 1813.405
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=738)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.211 (n=278)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=878)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=237)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

- **FILTRO** `drift_7min_pct` |x|> `0.0725` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.0725
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **PATRÓN** `drift_7min_pct` |x|≤ `0.0331` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `drift_7min_pct` |x|≤ 0.0331 (IC base=-0.026)

### MOMENTUM_IBS_5M#BTC#5min
- **FILTRO** `hora_utc` > `18.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=91)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 15.0 (IC base=+0.024)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=21158)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=47837)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=16432)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=52563)

- **FILTRO** `ibs_7min` < `0.2203` → IC=-0.232 (n=17246)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2203
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=51749)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.152 (n=22772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=46223)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.243 (n=21594)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=64811)

- **FILTRO** `ibs_7min` > `0.2835` → IC=-0.183 (n=21598)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2835
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=64807)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.155 (n=2978)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=9270)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=3002)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=9246)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.251 (n=4040)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=8208)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.151 (n=2738)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=9510)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3594)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=11345)

- **FILTRO** `ibs_7min` > `0.7748` → IC=-0.212 (n=3734)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7748
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=11205)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.260 (n=2754)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=8760)

- **FILTRO** `ibs_7min` < `0.7155` → IC=-0.208 (n=2877)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7155
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8637)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.197 (n=2861)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8653)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2681)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9072)

- **FILTRO** `ibs_7min` > `0.2655` → IC=-0.195 (n=2936)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8817)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.180 (n=2938)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8815)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.165 (n=2829)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=8893)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=2783)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=8939)

- **FILTRO** `ibs_7min` < `0.2857` → IC=-0.250 (n=3855)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=7867)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.200 (n=2425)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9297)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.258 (n=3804)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=12004)

- **FILTRO** `ibs_7min` > `0.7321` → IC=-0.183 (n=3950)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7321
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=11858)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=2752)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=8411)

- **FILTRO** `ibs_7min` < `0.7172` → IC=-0.193 (n=2790)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7172
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=8373)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.188 (n=2751)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=8412)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.257 (n=2677)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8968)

- **FILTRO** `ibs_7min` > `0.2744` → IC=-0.174 (n=2907)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2744
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8738)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.169 (n=2878)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8767)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=2602)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=8492)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.229 (n=3660)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7434)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.219 (n=2768)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=8326)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.197 (n=4047)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=12667)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.129 (n=3600)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=7654)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=2649)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8605)

- **FILTRO** `ibs_7min` < `0.17` → IC=-0.230 (n=2812)

  - _Acción_: SKIP cuando `ibs_7min` < 0.17
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8442)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2539)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=8715)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.233 (n=3621)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=11925)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1007)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1293)

- **FILTRO** `py_entrada` > `0.54` → IC=-0.142 (n=191)

  - _Acción_: SKIP cuando `py_entrada` > 0.54
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=575)

- **FILTRO** `libro_liquidez` < `10485.7689` → IC=-0.153 (n=191)

  - _Acción_: SKIP cuando `libro_liquidez` < 10485.7689
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=575)

### MOMENTUM_IBS_5M_FADE#DOGE#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=596)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=881)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.123 (n=221)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=333)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=450)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=98)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=670)

- **FILTRO** `libro_liquidez` < `3302.3462` → IC=-0.155 (n=192)

  - _Acción_: SKIP cuando `libro_liquidez` < 3302.3462
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=576)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=394)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.150 (n=650)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.131 (n=735)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.122)

- **PATRÓN** `total_vol_5m` < `421.6695` → IC=+0.162 (n=477)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 421.6695 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `3538.706` → IC=+0.141 (n=649)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3538.706 (IC base=+0.122)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.176 (n=171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 14.0 (IC base=+0.128)

- **PATRÓN** `total_vol_5m` < `380.982` → IC=+0.150 (n=304)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 380.982 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2523.0565` → IC=+0.235 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2523.0565 (IC base=+0.128)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4378` → IC=+0.157 (n=100)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.78€ cuando `delta_ratio` |x|> 0.4378 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.140 (n=259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 14.0 (IC base=+0.117)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4161` → IC=+0.191 (n=179)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.95€ cuando `delta_ratio` |x|> 0.4161 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.146 (n=283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 4.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `657.7094` → IC=+0.165 (n=237)

  - _Acción_: Kelly boost +0.83€ cuando `total_vol_5m` < 657.7094 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 59.0 (IC base=+0.131)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.167 (n=244)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `6100.528` → IC=+0.164 (n=215)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 6100.528 (IC base=+0.139)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.138 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 10.0 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=192)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.095)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.4417` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.4417
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=167)

- **FILTRO** `pct_vs_K` |x|> `3.4199` → IC=-0.193 (n=272)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4199
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=530)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.149 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0044 (IC base=-0.083)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9957` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=179)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.265 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.037)

- **PATRÓN** `pct_vs_K` |x|≤ `1.632` → IC=+0.154 (n=79)

  - _Acción_: Kelly boost +0.77€ cuando `pct_vs_K` |x|≤ 1.632 (IC base=-0.037)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` < `0.01` → IC=-0.136 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=28)

- **FILTRO** `T_h` < `251.7955` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `64.4744` → IC=-0.192 (n=50)

  - _Acción_: SKIP cuando `T_h` < 64.4744
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=102)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.011` → IC=-0.231 (n=552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.011
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=185)

- **FILTRO** `T_h` > `95.6682` → IC=-0.226 (n=367)

  - _Acción_: SKIP cuando `T_h` > 95.6682
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=370)

- **FILTRO** `sigma_h` < `0.0052` → IC=-0.212 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=476)

- **FILTRO** `pct_vs_K` |x|> `3.1007` → IC=-0.412 (n=158)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1007
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=476)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0092` → IC=-0.209 (n=180)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0092
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=60)

- **FILTRO** `T_h` > `87.986` → IC=-0.203 (n=119)

  - _Acción_: SKIP cuando `T_h` > 87.986
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=121)

- **FILTRO** `T_h` > `143.7643` → IC=-0.246 (n=57)

  - _Acción_: SKIP cuando `T_h` > 143.7643
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=174)

- **FILTRO** `pct_vs_K` |x|> `2.5315` → IC=-0.362 (n=78)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.5315
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=153)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0066` → IC=-0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `T_h` > `148.7378` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `T_h` > 148.7378
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.318 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=71)

- **FILTRO** `T_h` > `96.3924` → IC=-0.298 (n=102)

  - _Acción_: SKIP cuando `T_h` > 96.3924
  - _Potencial_: sin este filtro IC_bueno=-0.236 (n=104)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.360 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=146)

- **FILTRO** `sigma_h` < `0.0054` → IC=-0.200 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=146)

- **FILTRO** `T_h` > `57.2342` → IC=-0.233 (n=129)

  - _Acción_: SKIP cuando `T_h` > 57.2342
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=65)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `pct_vs_K` |x|≤ 0.8 (IC base=-0.168)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.292 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.139 (n=156)

- **FILTRO** `T_h` > `69.35` → IC=-0.213 (n=155)

  - _Acción_: SKIP cuando `T_h` > 69.35
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=52)

- **FILTRO** `sigma_h` > `0.0158` → IC=-0.311 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0158
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=106)

- **FILTRO** `sigma_h` < `0.0083` → IC=-0.257 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.213 (n=106)

- **FILTRO** `T_h` > `33.9175` → IC=-0.257 (n=105)

  - _Acción_: SKIP cuando `T_h` > 33.9175
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=36)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1195` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1195 (IC base=+0.341)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.357 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.341)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.397 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.341)

- **PATRÓN** `T_h` > `0.8789` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8789 (IC base=+0.341)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.341)

- **PATRÓN** `edge` > `0.0997` → IC=+0.438 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0997 (IC base=+0.404)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.408 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.404)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.430 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0095 (IC base=+0.404)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.408 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.404)

- **PATRÓN** `dist_50` > `0.376` → IC=+0.445 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.376 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.416 (n=321)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.404)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1021` → IC=+0.300 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1021 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.194)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.194)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.269 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.194)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.464 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.419 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0062` → IC=+0.403 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0062 (IC base=+0.417)

- **PATRÓN** `T_h` < `1.2415` → IC=+0.451 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2415 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.417)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.414 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.175` → IC=+0.485 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.175 (IC base=+0.435)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.467 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.435)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.457 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.435)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.471 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.435)

- **PATRÓN** `edge` > `0.2005` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.462)

- **PATRÓN** `sigma_h` < `0.0162` → IC=+0.473 (n=148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0162 (IC base=+0.462)

- **PATRÓN** `T_h` < `0.8229` → IC=+0.455 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8229 (IC base=+0.462)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.462)

- **PATRÓN** `dist_50` > `0.4597` → IC=+0.492 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4597 (IC base=+0.462)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.467 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.462)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=382)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=463)

- **PATRÓN** `streak_estiramiento` < `0.2936` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.2936 (IC base=+0.029)

- **PATRÓN** `streak_estiramiento` < `0.3661` → IC=+0.218 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3661 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.133 (n=235)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 30.0 (IC base=+0.059)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.495 (IC base=+0.061)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=23)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.2244` → IC=+0.149 (n=55)

  - _Acción_: Kelly boost +0.75€ cuando `streak_estiramiento` < 0.2244 (IC base=+0.035)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.092)

- **PATRÓN** `streak_estiramiento` < `0.5545` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `streak_estiramiento` < 0.5545 (IC base=+0.092)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.160 (n=145)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 31.0 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `2566.5304` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2566.5304 (IC base=+0.092)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=102)

- **FILTRO** `streak_len` > `5.0` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=110)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.210 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=51)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `volumen_racha` > `3677.1957` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_racha` > 3677.1957
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

- **FILTRO** `libro_liquidez` < `3449.8988` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 3449.8988
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

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
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.045)

- **PATRÓN** `volumen_racha` < `16919.513` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 16919.513 (IC base=+0.045)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1057)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1338)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1293)

### STRUCT_NO_15M
- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=4649)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=2684)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.189 (n=2134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.216` → IC=+0.165 (n=4846)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.216 (IC base=+0.151)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3548` → IC=+0.160 (n=4497)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3548 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.161 (n=4479)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 6.0 (IC base=+0.151)

- **PATRÓN** `ibs_15` > `0.4924` → IC=+0.217 (n=4846)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4924 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1339` → IC=+0.143 (n=2336)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1339 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.7048` → IC=+0.138 (n=4725)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.7048 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.566` → IC=+0.263 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.566 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=2883)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4688.8455` → IC=+0.172 (n=1616)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 4688.8455 (IC base=+0.151)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1876)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.225 (n=747)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.0597` → IC=+0.257 (n=249)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0597 (IC base=+0.201)

- **PATRÓN** `drift_15min` |x|≤ `0.3804` → IC=+0.201 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3804 (IC base=+0.201)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2662` → IC=+0.217 (n=249)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2662 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.222 (n=778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.201)

- **PATRÓN** `ibs_15` > `0.7086` → IC=+0.276 (n=747)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7086 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3789` → IC=+0.218 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3789 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.5257` → IC=+0.205 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5257 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.708` → IC=+0.307 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.708 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `14769.4491` → IC=+0.221 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14769.4491 (IC base=+0.201)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `ibs_15` > `0.4703` → IC=-0.162 (n=261)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.4703
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=786)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.152 (n=916)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0069 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.152 (n=610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.135)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1417` → IC=+0.139 (n=610)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.1417 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2841` → IC=+0.140 (n=739)

  - _Acción_: Kelly boost +0.70€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2841 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.141 (n=834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.137 (n=962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 17.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.4943` → IC=+0.219 (n=915)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4943 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.150 (n=575)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.6301` → IC=+0.136 (n=1042)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.6301 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.929` → IC=+0.290 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.929 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `5837.0711` → IC=+0.164 (n=415)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 5837.0711 (IC base=+0.135)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.6111` → IC=+0.137 (n=857)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` > 0.6111 (IC base=+0.062)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0197` → IC=+0.183 (n=771)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0197 (IC base=+0.173)

- **PATRÓN** `sigma_h` > `0.0231` → IC=+0.181 (n=524)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0231 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.216` → IC=+0.184 (n=1156)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.216 (IC base=+0.173)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3581` → IC=+0.201 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3581 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.176 (n=1061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 6.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.180 (n=1031)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 14.0 (IC base=+0.173)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.260 (n=1034)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.193 (n=659)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.029` → IC=+0.229 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.029 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `2953.6818` → IC=+0.207 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2953.6818 (IC base=+0.173)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.157 (n=935)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.384 (n=240)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.363)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.363 (n=480)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.377 (n=479)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1077` → IC=+0.383 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1077 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.372 (n=761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7904` → IC=+0.393 (n=720)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7904 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.382 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.159` → IC=+0.399 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.159 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.366 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `9931.1033` → IC=+0.378 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9931.1033 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.369 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1599` → IC=+0.371 (n=238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1599 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.396 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.381 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.386 (n=358)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3736` → IC=+0.389 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3736 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.166` → IC=+0.389 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.166 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `9173.8264` → IC=+0.376 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9173.8264 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `414.0` → IC=+0.390 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 414.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.365 (n=362)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.380 (n=164)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.365 (n=243)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.371 (n=323)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2951` → IC=+0.375 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2951 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.366 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.362)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.369 (n=166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8869` → IC=+0.414 (n=241)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8869 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.373 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` < `0.6569` → IC=+0.365 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6569 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.577` → IC=+0.410 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.577 (IC base=+0.362)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `4072.0973` → IC=+0.380 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4072.0973 (IC base=+0.362)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0103` → IC=-0.221 (n=1738)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=3375)

- **FILTRO** `drift_15min` |x|> `0.9084` → IC=-0.140 (n=1277)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9084
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3835)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=2115)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=2998)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.222 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.077)

- **PATRÓN** `ibs_15` > `0.6285` → IC=+0.280 (n=1174)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6285 (IC base=-0.077)

- **PATRÓN** `dist_vwap_pct` > `0.1107` → IC=+0.202 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1107 (IC base=-0.077)

- **PATRÓN** `dist_vwap_pct` < `0.5693` → IC=+0.202 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5693 (IC base=-0.077)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2357` → IC=+0.269 (n=1540)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2357 (IC base=-0.005)

- **PATRÓN** `ibs_15` < `0.3684` → IC=+0.284 (n=4625)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3684 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` > `0.6626` → IC=+0.281 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6626 (IC base=-0.005)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0322` → IC=-0.221 (n=2413)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0322
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=805)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.218 (n=804)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2414)

- **FILTRO** `sigma_ewma_delta_pct` > `22.42` → IC=-0.258 (n=461)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.42
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=2757)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.145 (n=409)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0035 (IC base=+0.073)

- **PATRÓN** `ibs_15` > `0.7591` → IC=+0.327 (n=402)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7591 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.279 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.4975` → IC=+0.287 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4975 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.633` → IC=+0.148 (n=211)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 22.633 (IC base=+0.073)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.230 (n=72)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.185)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.185)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.311 (n=72)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.185)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.185)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.360 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=-0.185)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=767)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.157 (n=589)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0065 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.182 (n=259)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.202 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.163 (n=422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5733` → IC=+0.242 (n=588)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5733 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1135` → IC=+0.152 (n=366)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1135 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.2773` → IC=+0.150 (n=549)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.2773 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=767)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5050.7283` → IC=+0.157 (n=392)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 5050.7283 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.263 (n=770)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.3595` → IC=+0.244 (n=1539)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3595 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7812` → IC=+0.257 (n=1539)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7812 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2165` → IC=+0.265 (n=793)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2165 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3774` → IC=+0.275 (n=1749)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3774 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6228` → IC=+0.267 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6228 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.302` → IC=+0.248 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.302 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1726` → IC=-0.256 (n=400)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1726
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=777)

- **FILTRO** `drift_15min` |x|> `0.9075` → IC=-0.280 (n=294)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9075
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=883)

- **FILTRO** `sigma_ewma_delta_pct` > `6.283` → IC=-0.204 (n=272)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.283
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=905)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=-0.192)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` > `0.2752` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.2752 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.192)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.232 (n=788)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=-0.030)

- **PATRÓN** `ibs_15` < `0.3902` → IC=+0.296 (n=788)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3902 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` > `0.6848` → IC=+0.232 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6848 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` < `0.1974` → IC=+0.247 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1974 (IC base=-0.030)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1502` → IC=-0.228 (n=358)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1502
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=1076)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.238 (n=708)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=726)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.212)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.212)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.119` → IC=+0.290 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.119 (IC base=-0.021)

- **PATRÓN** `ibs_15` < `0.1358` → IC=+0.310 (n=707)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1358 (IC base=-0.021)

- **PATRÓN** `dist_vwap_pct` > `0.7641` → IC=+0.337 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7641 (IC base=-0.021)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.146 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0062 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.146 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.375` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.375 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2558` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2558 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.370 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4193` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4193 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3511.4523` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3511.4523 (IC base=+0.103)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.146 (n=46)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0062 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1919` → IC=+0.146 (n=46)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1919 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.375` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.375 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2558` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2558 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.370 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4193` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.4193 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.0951` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0951 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3511.4523` → IC=+0.125 (n=46)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 3511.4523 (IC base=+0.103)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.290 (n=1277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.284)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.313 (n=564)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.284)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1516` → IC=+0.289 (n=852)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1516 (IC base=+0.284)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2235` → IC=+0.294 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2235 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=1318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.284)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.312 (n=1277)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.284)

- **PATRÓN** `dist_vwap_pct` > `0.2703` → IC=+0.316 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2703 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.164` → IC=+0.389 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.164 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `13414.309` → IC=+0.306 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13414.309 (IC base=+0.284)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.312 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.0593` → IC=+0.321 (n=227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0593 (IC base=+0.277)

- **PATRÓN** `drift_15min` |x|≤ `0.3847` → IC=+0.282 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3847 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3931` → IC=+0.283 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3931 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.299 (n=710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.8292` → IC=+0.302 (n=679)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8292 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2523` → IC=+0.311 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2523 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` < `0.5501` → IC=+0.278 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5501 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.964` → IC=+0.389 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.964 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `15932.6308` → IC=+0.312 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15932.6308 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.305 (n=598)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.310 (n=399)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1432` → IC=+0.295 (n=399)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1432 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1019` → IC=+0.334 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1019 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.304 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.291)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8494` → IC=+0.320 (n=598)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8494 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2899` → IC=+0.318 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2899 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` < `0.6633` → IC=+0.291 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6633 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.379` → IC=+0.389 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.379 (IC base=+0.291)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0933` → IC=-0.150 (n=241)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0933
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=81)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=369)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.183 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=367)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.14` → IC=-0.148 (n=52)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.14
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=156)

- **FILTRO** `sigma_h` < `0.0053` → IC=-0.184 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=20)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2127` → IC=-0.233 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2127
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.311` → IC=-0.143 (n=40)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.311
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

- **FILTRO** `sigma_h` < `0.0047` → IC=-0.326 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.306` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.306
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0094` → IC=-0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=32)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0863
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
- **PATRÓN** `ratio` < `0.9702` → IC=+0.397 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9702 (IC base=+0.181)

- **PATRÓN** `T_h` > `119.444` → IC=+0.354 (n=2673)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 119.444 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.021` → IC=+0.383 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.021 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9936` → IC=+0.150 (n=252)

  - _Acción_: Kelly boost +0.75€ cuando `T_h` > 111.9936 (IC base=+0.143)

- **PATRÓN** `ratio` < `0.9932` → IC=+0.272 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9932 (IC base=+0.143)

- **PATRÓN** `T_h` > `111.9838` → IC=+0.315 (n=953)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.300)

- **PATRÓN** `ratio` > `1.0178` → IC=+0.356 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0178 (IC base=+0.300)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `85.7585` → IC=+0.227 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 85.7585 (IC base=+0.227)

- **PATRÓN** `ratio` < `0.985` → IC=+0.423 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.985 (IC base=+0.227)

- **PATRÓN** `T_h` > `111.9969` → IC=+0.354 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.321)

- **PATRÓN** `ratio` > `1.0312` → IC=+0.399 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0312 (IC base=+0.321)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0788` → IC=+0.425 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.4924 sube el IC de +0.151 a +0.217 en UPDOWN_GBM#15min (n=4846). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7086 sube el IC de +0.201 a +0.276 en UPDOWN_GBM#BTC#15min (n=747). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4943 sube el IC de +0.135 a +0.219 en UPDOWN_GBM#ETH#15min (n=915). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de +0.173 a +0.260 en UPDOWN_GBM#XRP#15min (n=1034). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.157 en UPDOWN_GBM#XRP#15min (n=935). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6285 sube el IC de -0.077 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1174). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3684 sube el IC de -0.005 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=4625). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7591 sube el IC de +0.073 a +0.327 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=402). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.185 a +0.311 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=72). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5733 sube el IC de +0.149 a +0.242 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=588). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3774 sube el IC de +0.244 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1749). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.192 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3902 sube el IC de -0.030 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=788). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.212 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1358 sube el IC de -0.021 a +0.310 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=707). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.103 a +0.370 en UPDOWN_GBM_ETH_15M_HORA7 (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.103 a +0.370 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.284 a +0.312 en UPDOWN_GBM_IBS_ALTO (n=1277). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8292 sube el IC de +0.277 a +0.302 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=679). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8494 sube el IC de +0.291 a +0.320 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=598). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7904 sube el IC de +0.363 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=720). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=358). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8869 sube el IC de +0.362 a +0.414 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=241). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2135 | +0.086 | +240.16€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2135 | +0.086 | +240.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1730 | +0.087 | +200.88€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1730 | +0.087 | +200.88€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1019 | -0.020 | +73.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1019 | -0.020 | +73.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 780 | -0.036 | +56.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 780 | -0.036 | +56.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 158 | +0.069 | +22.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 158 | +0.069 | +22.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 75 | -0.045 | -7.61€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 75 | -0.045 | -7.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 45719 | -0.085 | -5667.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2701 | +0.055 | -291.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 43018 | -0.094 | -5376.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4732 | -0.109 | -766.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4732 | -0.109 | -766.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2701 | +0.055 | -291.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2701 | +0.055 | -291.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4727 | -0.114 | -917.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4727 | -0.114 | -917.88€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12516 | -0.041 | -1160.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12516 | -0.041 | -1160.55€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12379 | -0.111 | -1186.22€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12379 | -0.111 | -1186.22€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8664 | -0.124 | -1344.70€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8664 | -0.124 | -1344.70€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 45685 | -0.013 | +3015.89€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 11783 | +0.004 | +1571.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 33902 | -0.018 | +1444.03€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 45685 | -0.013 | +3015.89€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 11783 | +0.004 | +1571.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 33902 | -0.018 | +1444.03€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 177586 | +0.113 | -7301.36€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 21099 | +0.180 | -661.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 809 | +0.002 | -77.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 145442 | +0.106 | -6181.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10236 | +0.092 | -380.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 24103 | +0.104 | -1618.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 72 | -0.162 | +14.77€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 24016 | +0.105 | -1621.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 33854 | +0.125 | -557.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5574 | +0.179 | -219.23€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 24083 | +0.120 | -171.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4155 | +0.079 | -144.98€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 24152 | +0.098 | -1734.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 83 | -0.112 | +7.08€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 24054 | +0.099 | -1730.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 37893 | +0.123 | -782.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9607 | +0.177 | -229.50€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 24455 | +0.106 | -486.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3819 | +0.102 | -58.18€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 33457 | +0.112 | -1534.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5680 | +0.199 | -244.76€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 712 | +0.029 | -23.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 24803 | +0.096 | -1088.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2262 | +0.102 | -177.43€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 24127 | +0.106 | -1074.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 83 | -0.112 | +10.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 24031 | +0.107 | -1083.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 28747 | +0.194 | -1922.61€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 28747 | +0.194 | -1922.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6494 | +0.175 | -610.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6494 | +0.175 | -610.34€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4037 | +0.197 | -148.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4037 | +0.197 | -148.68€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6402 | +0.176 | -553.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6402 | +0.176 | -553.17€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5423 | +0.249 | -201.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5423 | +0.249 | -201.31€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6312 | +0.186 | -422.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6312 | +0.186 | -422.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1195 | +0.425 | -46.25€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1195 | +0.425 | -46.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 490 | +0.439 | -4.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 490 | +0.439 | -4.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 480 | +0.423 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 480 | +0.423 | -19.00€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 211 | +0.397 | -18.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 211 | +0.397 | -18.65€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 101329 | +0.200 | -7370.36€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 101329 | +0.200 | -7370.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 17464 | +0.181 | -1923.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 17464 | +0.181 | -1923.05€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 16337 | +0.225 | -529.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 16337 | +0.225 | -529.30€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 17391 | +0.180 | -1836.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 17391 | +0.180 | -1836.80€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 16469 | +0.218 | -654.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 16469 | +0.218 | -654.90€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 16763 | +0.203 | -1065.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 16763 | +0.203 | -1065.83€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 16905 | +0.196 | -1360.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 16905 | +0.196 | -1360.49€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 38967 | +0.116 | +289.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 38967 | +0.116 | +289.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 19402 | +0.117 | +188.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 19402 | +0.117 | +188.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 19565 | +0.115 | +100.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 19565 | +0.115 | +100.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2463 | +0.292 | -13.53€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2463 | +0.292 | -13.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1128 | +0.281 | -29.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1128 | +0.281 | -29.11€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1200 | +0.297 | +11.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1200 | +0.297 | +11.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 135 | +0.339 | +3.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 135 | +0.339 | +3.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1134 | +0.439 | -1.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1134 | +0.439 | -1.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 544 | +0.432 | -10.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 544 | +0.432 | -10.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 540 | +0.447 | +7.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 540 | +0.447 | +7.28€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 50 | +0.404 | +1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 50 | +0.404 | +1.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1885 | +0.067 | -87.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1160 | +0.079 | -23.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1451 | +0.074 | -42.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1160 | +0.079 | -23.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 78611 | +0.101 | -1852.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6337 | +0.096 | +132.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 72274 | +0.101 | -1984.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 43024 | +0.105 | -420.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6337 | +0.096 | +132.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 36687 | +0.107 | -552.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 16588 | +0.109 | -77.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 16588 | +0.109 | -77.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 18999 | +0.082 | -1354.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 18999 | +0.082 | -1354.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ GBM_LATE_15M | 53491 | +0.098 | +29474.66€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 53491 | +0.098 | +29474.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8889 | +0.225 | +7639.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8889 | +0.225 | +7639.24€ | 0 | 22 |
| ✅ GBM_LATE_15M#BTC | 8138 | +0.175 | +6323.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8138 | +0.175 | +6323.63€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 9600 | +0.205 | +7506.33€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9600 | +0.205 | +7506.33€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7264 | +0.051 | +2253.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7264 | +0.051 | +2253.93€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7478 | -0.030 | +1938.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7478 | -0.030 | +1938.04€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 12122 | -0.025 | +3813.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 12122 | -0.025 | +3813.49€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 56465 | +0.085 | +32562.26€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 56465 | +0.085 | +32562.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 11012 | -0.002 | +5853.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 11012 | -0.002 | +5853.56€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 12079 | +0.005 | +3171.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 12079 | +0.005 | +3171.92€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7712 | +0.291 | +8693.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7712 | +0.291 | +8693.53€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 10635 | +0.014 | +3263.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 10635 | +0.014 | +3263.09€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8746 | +0.044 | +3912.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8746 | +0.044 | +3912.29€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6281 | +0.315 | +7667.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6281 | +0.315 | +7667.87€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 42372 | +0.179 | +35060.70€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 42372 | +0.179 | +35060.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6384 | +0.239 | +5944.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6384 | +0.239 | +5944.35€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6725 | +0.140 | +4977.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6725 | +0.140 | +4977.05€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6808 | +0.224 | +5882.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6808 | +0.224 | +5882.52€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7244 | +0.132 | +5681.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7244 | +0.132 | +5681.41€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8001 | +0.121 | +6068.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8001 | +0.121 | +6068.45€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7210 | +0.232 | +6506.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7210 | +0.232 | +6506.91€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 11448 | +0.127 | +5751.98€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 11448 | +0.127 | +5751.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 468 | +0.157 | +308.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3290 | +0.134 | +1818.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3290 | +0.134 | +1818.81€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3400 | +0.129 | +1700.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3400 | +0.129 | +1700.08€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2820 | +0.091 | +1064.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2820 | +0.091 | +1064.78€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 979 | +0.168 | +599.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 979 | +0.168 | +599.65€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 53708 | +0.186 | +44011.16€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 53708 | +0.186 | +44011.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8496 | +0.249 | +8199.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8496 | +0.249 | +8199.85€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8498 | +0.137 | +5830.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8498 | +0.137 | +5830.85€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 9117 | +0.233 | +8164.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 9117 | +0.233 | +8164.67€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8897 | +0.139 | +6573.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8897 | +0.139 | +6573.93€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9525 | +0.124 | +6789.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9525 | +0.124 | +6789.56€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9175 | +0.239 | +8452.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9175 | +0.239 | +8452.31€ | 0 | 21 |
| ✅ GBM_LATE_5M | 13688 | +0.210 | +11087.42€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 13688 | +0.210 | +11087.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3257 | +0.211 | +2804.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3257 | +0.211 | +2804.80€ | 0 | 24 |
| ✅ GBM_LATE_5M#DOGE | 1282 | +0.203 | +984.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1282 | +0.203 | +984.65€ | 0 | 16 |
| ✅ GBM_LATE_5M#ETH | 3961 | +0.203 | +2968.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3961 | +0.203 | +2968.45€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 2175 | +0.207 | +1792.12€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2175 | +0.207 | +1792.12€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1959 | +0.209 | +1537.13€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4690 | +0.051 | +1237.12€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 4690 | +0.051 | +1237.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1652 | +0.061 | +494.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1652 | +0.061 | +494.13€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1516 | +0.053 | +446.60€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1516 | +0.053 | +446.60€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1522 | +0.039 | +296.39€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1522 | +0.039 | +296.39€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 675 | -0.252 | -38.02€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 675 | -0.252 | -38.02€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 253 | -0.253 | -21.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 253 | -0.253 | -21.29€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 243 | -0.251 | -9.82€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 243 | -0.251 | -9.82€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 179 | -0.246 | -6.91€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 179 | -0.246 | -6.91€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1922 | +0.085 | +501.98€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1922 | +0.085 | +501.98€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 745 | +0.074 | +187.07€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 745 | +0.074 | +187.07€ | 1 | 6 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 664 | +0.062 | +122.54€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 664 | +0.062 | +122.54€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 513 | +0.131 | +192.37€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 513 | +0.131 | +192.37€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 218 | +0.286 | +238.71€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 218 | +0.286 | +238.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 218 | +0.286 | +238.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 218 | +0.286 | +238.71€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4210 | +0.097 | +962.93€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4210 | +0.097 | +962.93€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4210 | +0.097 | +962.93€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4210 | +0.097 | +962.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 912 | -0.013 | +11.62€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 912 | -0.013 | +11.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 43 | +0.011 | +0.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 43 | +0.011 | +0.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 255 | -0.018 | +3.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 255 | -0.018 | +3.81€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 251 | +0.026 | +18.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 251 | +0.026 | +18.32€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 278 | -0.004 | +3.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 278 | -0.004 | +3.84€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 56 | -0.155 | -9.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 56 | -0.155 | -9.87€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4126 | +0.017 | +115.24€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4126 | +0.017 | +115.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 200 | +0.025 | -1.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 200 | +0.025 | -1.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 824 | +0.016 | +41.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 824 | +0.016 | +41.61€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 226 | +0.013 | +12.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 226 | +0.013 | +12.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1640 | +0.020 | +29.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1640 | +0.020 | +29.40€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 765 | +0.011 | +1.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 765 | +0.011 | +1.69€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 471 | +0.016 | +30.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 471 | +0.016 | +30.81€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2210 | -0.034 | -13.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2210 | -0.034 | -13.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 667 | -0.028 | -9.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 667 | -0.028 | -9.81€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 782 | -0.009 | +16.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 782 | -0.009 | +16.43€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 761 | -0.064 | -19.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 761 | -0.064 | -19.82€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 13824 | -0.032 | -137.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 6620 | -0.036 | -115.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 7204 | -0.029 | -22.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 493 | -0.051 | -27.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 250 | -0.020 | +3.05€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 243 | -0.084 | -30.96€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3611 | -0.025 | -5.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1720 | -0.023 | +7.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1891 | -0.027 | -12.52€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1380 | -0.028 | +15.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 701 | -0.035 | -3.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 679 | -0.020 | +19.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3124 | -0.036 | -68.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1468 | -0.041 | -52.68€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1656 | -0.031 | -15.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2659 | -0.027 | +10.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1284 | -0.036 | -18.74€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1375 | -0.019 | +29.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2557 | -0.042 | -62.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1197 | -0.051 | -50.36€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1360 | -0.033 | -12.06€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M | 14662 | -0.012 | -218.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M#15min | 14662 | -0.012 | -218.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 578 | -0.010 | -0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 578 | -0.010 | -0.50€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 63148 | +0.000 | +3460.16€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 63148 | +0.000 | +3460.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 11429 | +0.028 | +1562.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 11429 | +0.028 | +1562.39€ | 2 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8890 | -0.035 | -81.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8890 | -0.035 | -81.19€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 11558 | +0.025 | +1257.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 11558 | +0.025 | +1257.07€ | 1 | 1 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8801 | -0.050 | -187.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8801 | -0.050 | -187.72€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 10729 | -0.004 | +310.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 10729 | -0.004 | +310.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 11741 | +0.018 | +599.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 11741 | +0.018 | +599.24€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7058 | -0.055 | -115.64€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7058 | -0.055 | -115.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1244 | -0.002 | -15.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1936 | -0.066 | -27.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1936 | -0.066 | -27.91€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 70 | +0.000 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 70 | +0.000 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 799 | -0.119 | -34.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 799 | -0.119 | -34.39€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2148 | -0.068 | -12.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2148 | -0.068 | -12.31€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 861 | -0.017 | -26.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 861 | -0.017 | -26.50€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3376 | +0.004 | -1.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3376 | +0.004 | -1.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 195 | +0.008 | -2.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 195 | +0.008 | -2.19€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 192 | -0.010 | -2.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 155400 | -0.077 | +2265.73€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 155400 | -0.077 | +2265.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 27187 | -0.077 | +1548.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 27187 | -0.077 | +1548.97€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 23267 | -0.100 | -1115.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 23267 | -0.100 | -1115.43€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 27530 | -0.068 | +1336.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 27530 | -0.068 | +1336.42€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 22808 | -0.097 | -624.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 22808 | -0.097 | -624.36€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 27808 | -0.058 | +333.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 27808 | -0.058 | +333.43€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 26800 | -0.070 | +786.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 26800 | -0.070 | +786.70€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8995 | -0.035 | -184.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8995 | -0.035 | -184.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2074 | -0.047 | -29.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2074 | -0.047 | -29.41€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2632 | -0.025 | -38.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2632 | -0.025 | -38.48€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1268 | -0.065 | -32.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1268 | -0.065 | -32.88€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1010 | -0.031 | -32.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1010 | -0.031 | -32.49€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 2042 | +0.118 | +795.42€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1906 | +0.122 | +782.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 460 | +0.128 | +212.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 460 | +0.128 | +212.40€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 392 | +0.117 | +135.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 392 | +0.117 | +135.00€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 358 | +0.131 | +168.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 358 | +0.131 | +168.11€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 325 | +0.139 | +163.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 325 | +0.139 | +163.78€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 371 | +0.095 | +103.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 371 | +0.095 | +103.54€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1984 | -0.018 | -26.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1984 | -0.018 | -26.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 375 | +0.017 | +25.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 375 | +0.017 | +25.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 361 | -0.043 | -21.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 361 | -0.043 | -21.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 499 | -0.045 | -36.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 499 | -0.045 | -36.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 400 | -0.005 | -2.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 400 | -0.005 | -2.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 349 | -0.007 | +7.85€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 349 | -0.007 | +7.85€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1091 | -0.081 | -56.39€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 502 | -0.113 | -79.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 390 | -0.130 | -61.36€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 383 | -0.040 | +18.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 272 | -0.025 | +27.98€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 206 | -0.077 | +4.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 170 | -0.076 | +3.06€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 832 | -0.085 | -30.32€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1371 | -0.209 | -88.38€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 538 | -0.209 | -49.00€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 471 | -0.208 | -44.69€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 458 | -0.211 | -39.08€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 400 | -0.221 | -45.99€ | 5 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 375 | -0.203 | -0.31€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 348 | -0.200 | -2.71€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1219 | -0.211 | -93.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 516 | +0.386 | +476.17€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 94 | +0.167 | +63.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 94 | +0.167 | +63.15€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 122 | +0.371 | +105.56€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 122 | +0.371 | +105.56€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 300 | +0.457 | +307.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 300 | +0.457 | +307.46€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 516 | +0.386 | +476.17€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 883 | +0.046 | +82.18€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 883 | +0.046 | +82.18€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 331 | +0.035 | +11.75€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 331 | +0.035 | +11.75€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 71 | +0.007 | +0.21€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 71 | +0.007 | +0.21€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 398 | +0.068 | +64.16€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 398 | +0.068 | +64.16€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3557 | -0.024 | -143.76€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3557 | -0.024 | -143.76€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 608 | -0.029 | -27.82€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 608 | -0.029 | -27.82€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 170 | -0.041 | -14.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 170 | -0.041 | -14.29€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1652 | -0.020 | -61.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1652 | -0.020 | -61.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 116 | -0.042 | -10.16€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 116 | -0.042 | -10.16€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 72 | -0.013 | -5.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 72 | -0.013 | -5.54€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11458 | +0.014 | +72.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11458 | +0.014 | +72.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2986 | +0.017 | +22.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2986 | +0.017 | +22.84€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2978 | +0.017 | +36.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2978 | +0.017 | +36.12€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2915 | +0.008 | -3.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2915 | +0.008 | -3.30€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11217 | +0.017 | -18.43€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 11217 | +0.017 | -18.43€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4668 | +0.022 | +8.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4668 | +0.022 | +8.54€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3831 | +0.013 | -19.59€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3831 | +0.013 | -19.59€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2718 | +0.013 | -7.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2718 | +0.013 | -7.39€ | 1 | 0 |
| ✅ UPDOWN_GBM | 98450 | +0.059 | +9342.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 24036 | +0.082 | +5083.72€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 2994 | +0.001 | +30.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 65244 | +0.059 | +4125.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5833 | +0.001 | +104.80€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8232 | +0.103 | +1495.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1781 | +0.164 | +820.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6361 | +0.088 | +677.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 22467 | +0.057 | +1960.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3240 | +0.081 | +735.43€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 840 | +0.002 | +14.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 15650 | +0.066 | +1139.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2613 | -0.003 | +66.27€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 124 | -0.064 | +4.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 10622 | +0.077 | +1226.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 8775 | +0.062 | +488.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 23343 | +0.049 | +1637.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5715 | +0.072 | +892.53€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 812 | +0.005 | +16.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 14560 | +0.050 | +696.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2141 | +0.004 | +29.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 115 | -0.098 | +2.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 21048 | +0.038 | +1159.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6293 | +0.033 | +423.11€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 769 | -0.010 | +3.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 12805 | +0.048 | +731.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1079 | +0.005 | +9.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 102 | -0.144 | -7.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 12736 | +0.072 | +1865.33€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5246 | +0.098 | +1474.01€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 7093 | +0.057 | +392.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 341 | -0.101 | -0.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 959 | +0.363 | +343.34€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 959 | +0.363 | +343.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 477 | +0.362 | +166.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 477 | +0.362 | +166.14€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 482 | +0.362 | +177.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 482 | +0.362 | +177.20€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 23910 | -0.020 | +5960.92€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 23910 | -0.020 | +5960.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4456 | -0.114 | +251.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4456 | -0.114 | +251.68€ | 3 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3115 | +0.220 | +2006.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3115 | +0.220 | +2006.71€ | 1 | 18 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6750 | -0.059 | +1010.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6750 | -0.059 | +1010.99€ | 3 | 9 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6537 | -0.063 | +1230.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6537 | -0.063 | +1230.50€ | 2 | 5 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 286 | +0.066 | +27.72€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 286 | +0.066 | +27.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 286 | +0.066 | +27.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 286 | +0.066 | +27.72€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1702 | +0.284 | +1428.32€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1702 | +0.284 | +1428.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 905 | +0.277 | +706.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 905 | +0.277 | +706.70€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 797 | +0.291 | +721.61€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 797 | +0.291 | +721.61€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 852 | -0.114 | -84.78€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 852 | -0.114 | -84.78€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 264 | -0.083 | -20.26€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 264 | -0.083 | -20.26€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 95 | -0.170 | -10.94€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 95 | -0.170 | -10.94€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 110 | -0.179 | -4.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 110 | -0.179 | -4.23€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4426 | +0.303 | +2047.57€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1675 | +0.260 | +225.23€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1704 | +0.296 | +742.47€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 1047 | +0.381 | +1079.87€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.021 n=1218 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1218 IC=+0.021 PNL=+55.98€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 795 celda(s) pasan gate riguroso completo de 2845 evaluadas (n>=40) y 3961 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=6287 IC=+0.033 PNL=+425.27€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1704/15 IC=+0.296 PNL=+742.47€ | BTC: n=1675/15 IC=+0.260 PNL=+225.23€ | SOL: n=1047/15 IC=+0.381 PNL=+1079.87€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.145 n=1014/60 | contraria IC=+0.186 n=1069 | gap=-0.042 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=556, boost estimado=+0.013. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2139/40 IC=+0.004 PNL=+29.25€ | BTC#60min: n=2611/40 IC=-0.003 PNL=+66.30€ | SOL#60min: n=1079/40 IC=+0.005 PNL=+9.27€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.046 n=687744 | tras_1loss IC=+0.099 n=521714 | tras_2loss IC=+0.069 n=209213/40 | gap=-0.023 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.173 > 0.08 con n=961 PNL=+626.36€
  - _Datos_: n=961 IC=+0.173 PNL=+626.36€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.146 > 0.08 con n=1141 PNL=+586.99€
  - _Datos_: n=1141 IC=+0.146 PNL=+586.99€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.151 > 0.08 con n=81 PNL=+38.57€
  - _Datos_: n=81 IC=+0.151 PNL=+38.57€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=3608 PNL=+2009.91€
  - _Datos_: n=3608 IC=+0.333 PNL=+2009.91€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=982 IC=+0.068 PNL=+97.49€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=982 IC=+0.068 PNL=+97.49€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=102 IC=+0.173 PNL=+64.42€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=102 IC=+0.173 PNL=+64.42€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 6/15 ops en el filtro definido (IC actual=+0.075 PNL=+7.10€)
  - _Datos_: n=6 IC=+0.075 PNL=+7.10€

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
  - _Estado_: n=3901 IC=+0.002 PNL=-12.45€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3901 IC=+0.002 PNL=-12.45€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1928 IC=-0.002 PNL=+117.27€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1928 IC=-0.002 PNL=+117.27€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1218 IC=+0.021 PNL=+55.98€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1218 IC=+0.021 PNL=+55.98€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.152 > 0.1 con n=6454 PNL=+3502.90€
  - _Datos_: n=6454 IC=+0.152 PNL=+3502.90€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3235 IC=+0.081 PNL=+734.15€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3235 IC=+0.081 PNL=+734.15€

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
  - _Estado_: n=1248 IC=+0.038 PNL=+103.28€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1248 IC=+0.038 PNL=+103.28€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=161 IC=-0.009 PNL=-2.08€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=161 IC=-0.009 PNL=-2.08€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.286 n=218) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=218 IC=+0.286 PNL=+238.71€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.02 con n=1197 PNL=+479.74€
  - _Datos_: n=1197 IC=+0.119 PNL=+479.74€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=251 IC=-0.117 PNL=+7.41€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=251 IC=-0.117 PNL=+7.41€

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
  - _Estado_: n=40011 IC=+0.074 PNL=+5682.24€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=40011 IC=+0.074 PNL=+5682.24€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.134 < -0.1 con n=708 PNL=+103.52€
  - _Datos_: n=708 IC=-0.134 PNL=+103.52€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3702 IC=+0.066 PNL=+465.07€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3702 IC=+0.066 PNL=+465.07€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=178 IC=-0.117 PNL=-2.26€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=178 IC=-0.117 PNL=-2.26€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.101 > 0.1 con n=1034 PNL=+263.99€
  - _Datos_: n=1034 IC=+0.101 PNL=+263.99€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 6/20 ops en el filtro definido (IC actual=-0.075 PNL=-1.82€)
  - _Datos_: n=6 IC=-0.075 PNL=-1.82€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=40766 IC=-0.137 PNL=+2675.74€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=40766 IC=-0.137 PNL=+2675.74€

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
  - _Estado_: n=4178 IC=+0.129 PNL=+2699.24€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4178 IC=+0.129 PNL=+2699.24€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=10079 IC=+0.058 PNL=+883.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=10079 IC=+0.058 PNL=+883.77€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.100 > 0.08 con n=4325 PNL=+2416.11€
  - _Datos_: n=4325 IC=+0.100 PNL=+2416.11€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=4406 PNL=-360.40€
  - _Datos_: n=4406 IC=-0.220 PNL=-360.40€

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
  - _Estado_: n=93 IC=+0.037 PNL=+13.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=93 IC=+0.037 PNL=+13.28€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2137) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2137 IC=+0.096 PNL=+430.46€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.413 n=662) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=662 IC=+0.413 PNL=+960.71€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=17454 IC=+0.181 PNL=-1918.62€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=17454 IC=+0.181 PNL=-1918.62€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.1 con n=273 PNL=+187.33€
  - _Datos_: n=273 IC=+0.227 PNL=+187.33€
