# Hipótesis automáticas — 2026-10-24 05:55 UTC
_Generado por shadow_postmortem.py sobre 1032237 resoluciones (PNL=+135607.00€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=630)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.229 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.135)

- **PATRÓN** `n_total_lado` > `55.0` → IC=+0.176 (n=396)

  - _Acción_: Kelly boost +0.88€ cuando `n_total_lado` > 55.0 (IC base=+0.135)

- **PATRÓN** `banda_hit_calibrado` > `0.624` → IC=+0.267 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.624 (IC base=+0.135)

- **PATRÓN** `banda_z` > `9.021` → IC=+0.213 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.021 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.135)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.139 (n=424)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.149 (n=952)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.135)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.225 (n=718)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.140)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.197 (n=252)

  - _Acción_: Kelly boost +0.98€ cuando `n_total_lado` > 68.0 (IC base=+0.140)

- **PATRÓN** `banda_hit_calibrado` > `0.6159` → IC=+0.257 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6159 (IC base=+0.140)

- **PATRÓN** `banda_z` > `7.64` → IC=+0.190 (n=337)

  - _Acción_: Kelly boost +0.95€ cuando `banda_z` > 7.64 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=271)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.142 (n=353)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 8.0 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=853)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `3094.168` → IC=+0.140 (n=664)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3094.168 (IC base=+0.140)

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
- **FILTRO** `restante_s_al_confirmar` < `141.51` → IC=-0.201 (n=10416)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 141.51
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=31250)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.66` → IC=-0.256 (n=1138)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.66
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3415)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.27` → IC=-0.290 (n=1119)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.27
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=3362)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.38` → IC=-0.204 (n=2772)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.38
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8317)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.39` → IC=-0.275 (n=2005)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.39
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=6018)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.213 (n=22612)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=4452)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `8951.4631` → IC=+0.170 (n=2034)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 8951.4631 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.129 (n=19372)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=34763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.228 (n=18089)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=7376)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7018.3548` → IC=+0.157 (n=2848)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 7018.3548 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=2065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.187 (n=2019)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.191 (n=2529)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `16445.5093` → IC=+0.193 (n=656)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 16445.5093 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.188 (n=1811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 7.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.186 (n=2022)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` < `0.285` → IC=+0.317 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.285 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=2593)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `16273.4091` → IC=+0.187 (n=668)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16273.4091 (IC base=+0.182)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.171 (n=488)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.080)

- **PATRÓN** `libro_liquidez` > `6765.2427` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 6765.2427 (IC base=+0.080)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1168)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.082)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.163 (n=3719)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 15.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.376 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.218 (n=1956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.350 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.213 (n=2280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1106)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=943)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.143)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.261 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=869)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2210.9325` → IC=+0.158 (n=480)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2210.9325 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.421 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.151 (n=1308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=688)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=866)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.153 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` > `0.56` → IC=+0.191 (n=383)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.56 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=127)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `1192.3838` → IC=+0.133 (n=254)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 1192.3838 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=1138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.123)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=19188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=16300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.235 (n=7891)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.181 (n=4410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=3710)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.184 (n=4331)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.73 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=3614)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.181)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=2440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1555)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.301 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.220)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=4338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=3696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.189 (n=3400)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.360 (n=1231)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=4252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.193 (n=3636)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=3149)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.431 (n=813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.425 (n=709)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4242.4895` → IC=+0.438 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4242.4895 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.443 (n=224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.434)

- **PATRÓN** `libro_liquidez` > `20878.8113` → IC=+0.444 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20878.8113 (IC base=+0.434)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.436 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3610.6662` → IC=+0.443 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3610.6662 (IC base=+0.431)

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
- **FILTRO** `py_entrada` > `0.765` → IC=-0.294 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=27)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=25034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=25156)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=3711)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.187 (n=7977)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=11228)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.186)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.227 (n=3990)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=3630)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=4289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.211 (n=5704)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.231 (n=3506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.224 (n=4016)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.275 (n=3541)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.220)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.209 (n=3577)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3701)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=4160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.199 (n=3600)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 5.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9091)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=9019)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.71` → IC=+0.137 (n=10919)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.71 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=4496)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.145 (n=4121)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.68` → IC=+0.144 (n=4111)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.68 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=4595)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=4898)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.31` → IC=+0.136 (n=5499)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.31 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.310 (n=1158)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.382 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `3795.9272` → IC=+0.292 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3795.9272 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.292 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.357 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `5061.412` → IC=+0.288 (n=337)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5061.412 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.323 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.299 (n=816)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.392 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.298 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.297)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.339 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.340)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.372 (n=84)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.340)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.385 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.340)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.340)

- **PATRÓN** `libro_liquidez` > `761.0655` → IC=+0.371 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 761.0655 (IC base=+0.340)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.447 (n=794)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.444 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.446 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=379)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.438 (n=257)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.438 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.440 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `5392.4277` → IC=+0.443 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5392.4277 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.455 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.451)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.454 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.451)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.452 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.451)

- **PATRÓN** `libro_liquidez` > `1994.4351` → IC=+0.469 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1994.4351 (IC base=+0.451)

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
- **FILTRO** `hora_utc` > `10.0` → IC=-0.283 (n=58)
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
- **FILTRO** `hora_utc` > `10.0` → IC=-0.283 (n=58)
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
- **PATRÓN** `drift_60min` |x|≤ `0.3648` → IC=+0.142 (n=12356)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3648 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.125 (n=14173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=9802)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.3778` → IC=+0.166 (n=14044)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3778 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7995` → IC=+0.275 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7995 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.647` → IC=+0.182 (n=6987)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 3.647 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.617` → IC=+0.265 (n=4095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.617 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3029` → IC=+0.241 (n=1435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3029 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.7354` → IC=+0.231 (n=3337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7354 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.125 (n=11611)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.121)

- **PATRÓN** `libro_liquidez` > `4917.1159` → IC=+0.147 (n=4681)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 4917.1159 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.5679` → IC=+0.142 (n=17331)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5679 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.6152` → IC=+0.188 (n=1145)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.6152 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.6947` → IC=+0.190 (n=3001)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 0.6947 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` > `1.0507` → IC=+0.182 (n=3092)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 1.0507 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.233 (n=1700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.6858` → IC=+0.208 (n=3864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6858 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.222 (n=11447)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.077)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.205 (n=1022)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.3472` → IC=+0.207 (n=3047)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3472 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.212 (n=1482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.208 (n=2044)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.280 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.782` → IC=+0.282 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.782 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.254 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `2.2988` → IC=+0.215 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2988 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2066.52` → IC=+0.207 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2066.52 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.221 (n=1809)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0088` → IC=+0.241 (n=2563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0088 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.239 (n=1167)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.274 (n=855)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.5345` → IC=+0.257 (n=2562)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5345 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.241 (n=2301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2915` → IC=+0.259 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2915 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `1.4425` → IC=+0.241 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4425 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.6935` → IC=+0.243 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6935 (IC base=+0.238)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=2902)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `1458.1` → IC=+0.243 (n=2562)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1458.1 (IC base=+0.238)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.240 (n=1144)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.238)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.239 (n=1109)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.233 (n=1139)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.1056` → IC=+0.256 (n=1103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1056 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=2622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `0.9454` → IC=+0.274 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9454 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.235 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.32` → IC=+0.269 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.32 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` < `1.2306` → IC=+0.229 (n=2507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2306 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.233 (n=2507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.270 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.257 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.151 (n=2595)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0058 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.0755` → IC=+0.167 (n=865)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0755 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` < `0.5923` → IC=+0.184 (n=2281)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.5923 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` < `0.1366` → IC=+0.153 (n=2441)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1366 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.065` → IC=+0.149 (n=422)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 11.065 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.144` → IC=+0.142 (n=2358)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.144 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `1.2041` → IC=+0.142 (n=2591)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.2041 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.1572` → IC=+0.164 (n=703)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1572 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `2.4537` → IC=+0.144 (n=2470)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.4537 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `1.7955` → IC=+0.137 (n=1647)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.7955 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.175 (n=1066)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 214.0 (IC base=+0.134)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.221 (n=1059)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.194 (n=2841)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.183` → IC=+0.271 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.183 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.200 (n=2820)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3513` → IC=+0.211 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3513 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7037` → IC=+0.212 (n=1399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7037 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=3816)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1956.57` → IC=+0.203 (n=1440)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1956.57 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.222 (n=2524)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.234 (n=1263)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.244 (n=1083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.026` → IC=+0.276 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.026 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.3` → IC=+0.261 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.3 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.260 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7347` → IC=+0.226 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7347 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=1469)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1939.2081` → IC=+0.220 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1939.2081 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.220 (n=2351)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.146 (n=156)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=3842)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.162 (n=563)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0037 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.9529` → IC=+0.231 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9529 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1402` → IC=+0.335 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1402 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` < `0.1949` → IC=+0.329 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1949 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.146` → IC=+0.193 (n=1209)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 5.146 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` < `0.858` → IC=+0.334 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.858 (IC base=+0.054)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.351 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` < `0.1672` → IC=+0.331 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1672 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.343 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.054)

- **PATRÓN** `volumen_spike_ratio` < `1.4123` → IC=+0.357 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4123 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `129.0` → IC=+0.334 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 129.0 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.093` → IC=+0.181 (n=1000)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.093 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` > `0.7374` → IC=+0.157 (n=228)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.7374 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.8381` → IC=+0.151 (n=1201)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8381 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` > `1.1677` → IC=+0.140 (n=600)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.1677 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.202 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.776` → IC=+0.142 (n=1153)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.776 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.155` → IC=+0.157 (n=784)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.155 (IC base=+0.038)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.182 (n=108)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=588)

- **FILTRO** `ibs_20min` < `0.2703` → IC=-0.182 (n=174)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2703
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=522)

- **FILTRO** `ibs_20min` > `0.2143` → IC=-0.132 (n=3761)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2143
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=1856)

- **FILTRO** `sigma_ewma_delta_pct` > `8.616` → IC=-0.233 (n=593)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.616
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=5024)

- **PATRÓN** `ibs_20min` > `0.7778` → IC=+0.182 (n=237)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.7778 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `1.0161` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0161 (IC base=+0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.396` → IC=+0.133 (n=246)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 2.396 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` > `1.0359` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0359 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.1597` → IC=+0.276 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1597 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.288 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.264 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.027)

- **PATRÓN** `ibs_20min` < `0.2143` → IC=+0.149 (n=1856)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2143 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2682` → IC=+0.281 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2682 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.7007` → IC=+0.302 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7007 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0805` → IC=+0.296 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0805 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4396` → IC=+0.301 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4396 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6048` → IC=-0.183 (n=1037)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6048
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=3112)

- **FILTRO** `ibs_20min` < `0.7585` → IC=-0.153 (n=2738)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7585
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=1411)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.165 (n=1002)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=3147)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.204 (n=1481)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=4474)

- **PATRÓN** `dist_vwap_pct` > `1.1071` → IC=+0.345 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1071 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2465` → IC=+0.306 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2465 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` < `1.1407` → IC=+0.300 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1407 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.6988` → IC=+0.317 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6988 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.1004` → IC=+0.303 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1004 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0719` → IC=+0.305 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0719 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.4081` → IC=+0.320 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4081 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.8376` → IC=+0.311 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8376 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.8193` → IC=+0.285 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8193 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` < `0.7166` → IC=+0.265 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7166 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `1.066` → IC=+0.284 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.066 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.1683` → IC=+0.291 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1683 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `2.1803` → IC=+0.263 (n=1346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1803 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `1.4259` → IC=+0.266 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4259 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.210 (n=6151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.3148` → IC=+0.168 (n=18406)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3148 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.9588` → IC=+0.302 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9588 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.163 (n=8260)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `1.172` → IC=+0.264 (n=6793)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.172 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` > `0.688` → IC=+0.271 (n=6070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.688 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` < `0.1068` → IC=+0.264 (n=10426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1068 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.275 (n=2032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` < `1.4598` → IC=+0.265 (n=3605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4598 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `2.6516` → IC=+0.273 (n=3604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6516 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.297 (n=10385)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.095)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.156 (n=5934)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0094 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.6545` → IC=+0.145 (n=17763)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.6545 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.7034` → IC=+0.266 (n=2485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7034 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1959` → IC=+0.266 (n=1882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1959 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2947` → IC=+0.316 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2947 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.58` → IC=+0.291 (n=3589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.58 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2709` → IC=+0.287 (n=3698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2709 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.296 (n=8088)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5801` → IC=-0.138 (n=2516)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5801
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=2516)

- **FILTRO** `ibs_20min` > `0.7347` → IC=-0.215 (n=1071)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7347
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=3216)

- **FILTRO** `sigma_ewma_delta_pct` > `4.329` → IC=-0.213 (n=934)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.329
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=3353)

- **PATRÓN** `ibs_20min` > `0.9222` → IC=+0.320 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9222 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.954` → IC=+0.218 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.954 (IC base=+0.028)

- **PATRÓN** `volumen_pendiente_norm` > `0.2299` → IC=+0.306 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2299 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.255 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.028)

- **PATRÓN** `volumen_spike_ratio` > `2.2635` → IC=+0.282 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2635 (IC base=+0.028)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.288 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.028)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.160 (n=1073)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1667 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.416 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.6552` → IC=+0.406 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.6552 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.403 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1153` → IC=+0.215 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1153 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1961` → IC=+0.196 (n=1803)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 1.1961 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.6848` → IC=+0.203 (n=1611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6848 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` < `0.0748` → IC=+0.195 (n=1654)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0748 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.2774` → IC=+0.236 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2774 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.218 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4267 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.5021` → IC=+0.195 (n=592)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.5021 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `270.0` → IC=+0.231 (n=1180)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 270.0 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1706` → IC=+0.232 (n=1186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1706 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.236 (n=1185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.297 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.536` → IC=+0.243 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.536 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.1623` → IC=+0.254 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1623 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `198.0` → IC=+0.247 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 198.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.313 (n=887)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.278 (n=2791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.312 (n=1415)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.678` → IC=+0.301 (n=861)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.678 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.282 (n=2454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `1.6099` → IC=+0.274 (n=2573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6099 (IC base=+0.270)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.281 (n=3175)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `2042.8984` → IC=+0.288 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2042.8984 (IC base=+0.270)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.290 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 18.0 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.326 (n=1061)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1789` → IC=+0.312 (n=1027)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1789 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.294 (n=818)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.293)

- **PATRÓN** `ibs_20min` < `0.3724` → IC=+0.295 (n=2336)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3724 (IC base=+0.293)

- **PATRÓN** `ibs_20min` > `0.2637` → IC=+0.300 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2637 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.445` → IC=+0.307 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.445 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` < `0.1967` → IC=+0.293 (n=2288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1967 (IC base=+0.293)

- **PATRÓN** `volumen_pendiente_norm` > `0.3414` → IC=+0.305 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3414 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` < `1.7259` → IC=+0.299 (n=983)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7259 (IC base=+0.293)

- **PATRÓN** `volumen_spike_ratio` > `2.6641` → IC=+0.304 (n=1013)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6641 (IC base=+0.293)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `1937.7951` → IC=+0.308 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1937.7951 (IC base=+0.293)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.296 (n=1466)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.293)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7366` → IC=-0.184 (n=1123)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7366
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=3370)

- **PATRÓN** `ibs_20min` > `0.8731` → IC=+0.169 (n=1075)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8731 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.1533` → IC=+0.234 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1533 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.2144` → IC=+0.227 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2144 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` < `1.0079` → IC=+0.237 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0079 (IC base=+0.027)

- **PATRÓN** `volumen_regimen` > `0.6645` → IC=+0.230 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6645 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.1634` → IC=+0.234 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1634 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.237 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.4598` → IC=+0.236 (n=1480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4598 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `121.0` → IC=+0.253 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 121.0 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` < `0.1967` → IC=+0.237 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1967 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` < `1.1864` → IC=+0.243 (n=1044)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1864 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.251 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.293 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.793` → IC=+0.277 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.793 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.4337` → IC=+0.257 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4337 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `124.0` → IC=+0.262 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 124.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7576` → IC=-0.220 (n=1934)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7576
  - _Potencial_: sin este filtro IC_bueno=+0.308 (n=1937)

- **FILTRO** `ibs_20min` > `0.6429` → IC=-0.233 (n=937)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6429
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=2834)

- **FILTRO** `sigma_ewma_delta_pct` > `8.456` → IC=-0.243 (n=437)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.456
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=3334)

- **PATRÓN** `ibs_20min` > `0.7576` → IC=+0.308 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7576 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.2143` → IC=+0.339 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2143 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.441` → IC=+0.185 (n=605)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.441 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` < `0.8478` → IC=+0.334 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8478 (IC base=+0.044)

- **PATRÓN** `volumen_regimen` > `0.7018` → IC=+0.330 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7018 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` < `0.1588` → IC=+0.325 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1588 (IC base=+0.044)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.345 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.044)

- **PATRÓN** `volumen_spike_ratio` < `1.4408` → IC=+0.351 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4408 (IC base=+0.044)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.342 (n=1247)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.044)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.122 (n=2834)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` < 0.6429 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.264 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` < `0.102` → IC=+0.243 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.102 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.0777` → IC=+0.254 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0777 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` < `2.4411` → IC=+0.248 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4411 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `1.5523` → IC=+0.241 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5523 (IC base=+0.034)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.269 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 51.0 (IC base=+0.034)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.350 (n=1804)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.310 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.316 (n=961)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.338 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.307)

- **PATRÓN** `dist_vwap_pct` > `0.2086` → IC=+0.332 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2086 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.847` → IC=+0.327 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.847 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.11` → IC=+0.308 (n=2296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.11 (IC base=+0.307)

- **PATRÓN** `volumen_regimen` > `0.6275` → IC=+0.315 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6275 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.345 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `1.4298` → IC=+0.318 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4298 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `2961.5744` → IC=+0.312 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2961.5744 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.341 (n=1753)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.307)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.339 (n=1429)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.318 (n=833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.307 (n=1047)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.3684` → IC=+0.331 (n=2140)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3684 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.320 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.307)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.313 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.307)

- **PATRÓN** `volumen_regimen` > `1.2242` → IC=+0.338 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2242 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.2841` → IC=+0.358 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2841 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.317 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.139` → IC=+0.312 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.139 (IC base=+0.307)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.224 (n=4534)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0869` → IC=+0.202 (n=4540)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0869 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=14090)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.557` → IC=+0.234 (n=13599)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.557 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1637` → IC=+0.208 (n=5459)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1637 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.323` → IC=+0.257 (n=3558)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.323 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1862` → IC=+0.165 (n=9026)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1862 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.6224` → IC=+0.163 (n=9026)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6224 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2929` → IC=+0.204 (n=1976)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2929 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6089` → IC=+0.192 (n=4400)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6089 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `1957.3172` → IC=+0.179 (n=12149)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 1957.3172 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.196 (n=12531)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 93.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.185 (n=11560)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0093 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.228 (n=4378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.213 (n=6248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.5045` → IC=+0.238 (n=13126)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5045 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.954` → IC=+0.197 (n=2132)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 9.954 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.66` → IC=+0.183 (n=11610)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.66 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1824` → IC=+0.165 (n=9361)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1824 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.226 (n=1952)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6404` → IC=+0.189 (n=4122)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6404 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.194 (n=12094)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 98.0 (IC base=+0.181)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.231 (n=763)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.235 (n=2278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.225 (n=1542)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9309` → IC=+0.293 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9309 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.858` → IC=+0.327 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.858 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.278 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.218 (n=2162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=2484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.227 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.253 (n=1774)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.262 (n=806)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.251)

- **PATRÓN** `drift_60min` |x|≤ `0.0663` → IC=+0.311 (n=591)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0663 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.255 (n=1821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=849)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.251)

- **PATRÓN** `ibs_20min` < `0.3084` → IC=+0.276 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3084 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` < `0.1007` → IC=+0.255 (n=1547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1007 (IC base=+0.251)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.285 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` < `1.4419` → IC=+0.273 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4419 (IC base=+0.251)

- **PATRÓN** `volumen_spike_ratio` > `2.7246` → IC=+0.257 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7246 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.255 (n=2009)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.251)

- **PATRÓN** `libro_liquidez` > `1587.224` → IC=+0.258 (n=1583)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1587.224 (IC base=+0.251)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.256 (n=736)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.251)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.219 (n=685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0646` → IC=+0.192 (n=684)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0646 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=2153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3282` → IC=+0.220 (n=2052)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3282 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1345` → IC=+0.214 (n=1217)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1345 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.252` → IC=+0.221 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.252 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6921` → IC=+0.163 (n=903)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.6921 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.190 (n=324)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4131` → IC=+0.173 (n=671)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.4131 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.4971` → IC=+0.166 (n=671)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.4971 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `418.0` → IC=+0.154 (n=1975)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 418.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.174 (n=2152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0059 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.2348` → IC=+0.174 (n=1893)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2348 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.192 (n=1027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 15.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` < `0.6153` → IC=+0.209 (n=2150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6153 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.45` → IC=+0.195 (n=408)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 11.45 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.2052` → IC=+0.163 (n=2150)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2052 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.0699` → IC=+0.152 (n=1750)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0699 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.4922` → IC=+0.155 (n=2030)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4922 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `225.0` → IC=+0.183 (n=868)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 225.0 (IC base=+0.149)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.237 (n=766)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.394` → IC=+0.221 (n=2022)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.394 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.325` → IC=+0.303 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.325 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.0983` → IC=+0.213 (n=1980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0983 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3513` → IC=+0.227 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3513 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.7659` → IC=+0.212 (n=982)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7659 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7115` → IC=+0.226 (n=1011)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7115 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.218 (n=2757)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1943.141` → IC=+0.225 (n=1042)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1943.141 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.242 (n=1995)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0115 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.2467` → IC=+0.265 (n=1330)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2467 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0151` → IC=+0.300 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0151 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.408` → IC=+0.274 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.408 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3585` → IC=+0.284 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3585 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7487` → IC=+0.235 (n=840)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7487 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1556` → IC=+0.239 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1556 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1930.7184` → IC=+0.241 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1930.7184 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.235 (n=1283)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.166 (n=2215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0075 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0769` → IC=+0.202 (n=739)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0769 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.3033` → IC=+0.208 (n=2214)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3033 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1441` → IC=+0.195 (n=1337)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1441 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.753` → IC=+0.201 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.753 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0228` → IC=+0.152 (n=1949)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0228 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6154` → IC=+0.146 (n=2214)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 0.6154 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1028` → IC=+0.171 (n=907)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1028 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.824` → IC=+0.146 (n=1448)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.824 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5084` → IC=+0.164 (n=724)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5084 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `7477.9714` → IC=+0.191 (n=1004)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7477.9714 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `136.0` → IC=+0.151 (n=2153)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 136.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.157 (n=2336)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0072 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.3911` → IC=+0.144 (n=2336)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3911 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.169 (n=1115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6819` → IC=+0.186 (n=2337)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6819 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.791` → IC=+0.151 (n=821)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 6.791 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8548` → IC=+0.156 (n=1558)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8548 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2997` → IC=+0.196 (n=353)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2997 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.8095` → IC=+0.136 (n=1463)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8095 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.421` → IC=+0.130 (n=2194)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.421 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7156.4491` → IC=+0.190 (n=1059)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7156.4491 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.135 (n=1892)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 114.0 (IC base=+0.128)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.179 (n=1128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0104 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4366` → IC=+0.127 (n=2181)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4366 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.4865` → IC=+0.217 (n=2479)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4865 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1947` → IC=+0.191 (n=1430)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1947 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.466` → IC=+0.282 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.466 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.141 (n=2479)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1741 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.1602` → IC=+0.132 (n=2521)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1602 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.436` → IC=+0.148 (n=803)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.436 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2588)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2724.2295` → IC=+0.210 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2724.2295 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.154 (n=805)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 19.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.142 (n=2547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0109 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1087` → IC=+0.172 (n=849)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1087 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.142 (n=2596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6087` → IC=+0.221 (n=2545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6087 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.762` → IC=+0.127 (n=389)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 8.762 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.456` → IC=+0.136 (n=2246)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 2.456 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1785` → IC=+0.131 (n=2545)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1785 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1648` → IC=+0.126 (n=2472)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1648 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2754` → IC=+0.149 (n=343)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2754 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4428` → IC=+0.129 (n=793)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.4428 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.140 (n=793)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2603.7393` → IC=+0.184 (n=1154)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2603.7393 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.129 (n=2073)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 41.0 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.247 (n=2038)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.1721` → IC=+0.242 (n=1005)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1721 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2053)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.258 (n=2288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1837` → IC=+0.229 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1837 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.4797` → IC=+0.224 (n=2053)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4797 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.643` → IC=+0.251 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.643 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `1.1717` → IC=+0.224 (n=2281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1717 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.232 (n=2281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.265 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.4642` → IC=+0.227 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4642 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` > `1.8082` → IC=+0.232 (n=1481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8082 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.225 (n=2973)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `2578.2802` → IC=+0.226 (n=1521)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2578.2802 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.234 (n=1026)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.231)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.241 (n=1057)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.231)

- **PATRÓN** `drift_60min` |x|≤ `0.0889` → IC=+0.263 (n=778)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0889 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.232 (n=1039)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` < `0.4271` → IC=+0.260 (n=2331)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4271 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.2997` → IC=+0.242 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2997 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.305` → IC=+0.265 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.305 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `0.8673` → IC=+0.234 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8673 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` > `0.6376` → IC=+0.236 (n=2331)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6376 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.288 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` > `1.4377` → IC=+0.234 (n=2174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4377 (IC base=+0.231)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.231)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.205 (n=1526)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.191 (n=1151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.009 (IC base=+0.183)

- **PATRÓN** `drift_60min` |x|≤ `0.1296` → IC=+0.203 (n=1519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1296 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=1705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4909` → IC=+0.219 (n=3082)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4909 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7948` → IC=+0.205 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7948 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.605` → IC=+0.212 (n=1492)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.605 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.204 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` > `0.6933` → IC=+0.186 (n=2778)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6933 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0998` → IC=+0.190 (n=1238)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.0998 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.4272` → IC=+0.193 (n=1119)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4272 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.4806` → IC=+0.187 (n=1119)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4806 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.190 (n=3899)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `2665.5936` → IC=+0.189 (n=3082)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2665.5936 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.130 (n=1253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0039 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.7222` → IC=+0.121 (n=3758)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.7222 (IC base=+0.084)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.210 (n=419)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.0989` → IC=+0.238 (n=418)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0989 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.212 (n=866)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.6393` → IC=+0.240 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6393 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.3064` → IC=+0.203 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3064 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.073` → IC=+0.202 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.073 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.633` → IC=+0.185 (n=1006)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 6.633 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.8739` → IC=+0.210 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8739 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.0925` → IC=+0.186 (n=912)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` < 0.0925 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.187 (n=375)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `2.1959` → IC=+0.195 (n=818)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1959 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `14694.0598` → IC=+0.188 (n=633)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 14694.0598 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `161.0` → IC=+0.203 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 161.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.131 (n=1139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0057 (IC base=+0.105)

- **PATRÓN** `ibs_20min` < `0.6342` → IC=+0.155 (n=1002)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.6342 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` > `0.1612` → IC=+0.159 (n=303)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.1612 (IC base=+0.105)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.171 (n=494)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 160.0 (IC base=+0.105)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.241 (n=721)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.212 (n=359)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.1256` → IC=+0.225 (n=474)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1256 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=1125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.3797` → IC=+0.252 (n=961)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3797 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.7982` → IC=+0.210 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7982 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2089` → IC=+0.215 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2089 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.907` → IC=+0.244 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.907 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.0228` → IC=+0.213 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0228 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` > `1.1584` → IC=+0.212 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1584 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.2659` → IC=+0.242 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2659 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.220 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4208 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7736` → IC=+0.217 (n=708)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7736 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.1094` → IC=+0.163 (n=363)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.1094 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `5472.4764` → IC=+0.128 (n=726)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 5472.4764 (IC base=+0.066)

- **PATRÓN** `ballena_activa_n` < `43.0` → IC=+0.121 (n=462)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 43.0 (IC base=+0.066)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.193 (n=291)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0109 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.197 (n=779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.9658` → IC=+0.247 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9658 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.092` → IC=+0.239 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.092 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8875` → IC=+0.193 (n=578)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8875 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` > `0.714` → IC=+0.176 (n=774)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` > 0.714 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.2307` → IC=+0.193 (n=164)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2307 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.190 (n=279)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.1532` → IC=+0.172 (n=379)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 2.1532 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.180 (n=893)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3010.8204` → IC=+0.191 (n=289)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 3010.8204 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.5714` → IC=+0.129 (n=852)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.5714 (IC base=+0.050)

- **PATRÓN** `libro_liquidez` > `2641.0193` → IC=+0.147 (n=437)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 2641.0193 (IC base=+0.050)

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

- **PATRÓN** `ibs_20min` > `0.4` → IC=+0.176 (n=220)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.4 (IC base=+0.152)

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

- **PATRÓN** `sigma_h` > `0.0228` → IC=+0.175 (n=115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0228 (IC base=+0.115)

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
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.228 (n=5915)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=18445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4449` → IC=+0.231 (n=17726)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4449 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.9057` → IC=+0.214 (n=2147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9057 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.203` → IC=+0.253 (n=4331)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.203 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.2206` → IC=+0.169 (n=11887)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2206 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2403` → IC=+0.205 (n=3218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2403 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6146` → IC=+0.196 (n=5752)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6146 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1948.2131` → IC=+0.184 (n=15835)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 1948.2131 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.209 (n=14416)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.196 (n=7101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0056 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.3757` → IC=+0.193 (n=14197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3757 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=6022)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.5855` → IC=+0.242 (n=16134)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5855 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.771` → IC=+0.205 (n=2245)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.771 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.534` → IC=+0.192 (n=15604)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 3.534 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `0.6316` → IC=+0.168 (n=3628)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6316 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2912` → IC=+0.253 (n=2192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2912 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `2.625` → IC=+0.200 (n=5099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.625 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.235 (n=5162)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.189)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.232 (n=970)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.3463` → IC=+0.231 (n=2887)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3463 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.239 (n=1400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.231 (n=1948)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.353 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.293 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.225 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `2.2926` → IC=+0.241 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2926 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=3105)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2065.6` → IC=+0.232 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2065.6 (IC base=+0.228)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.253 (n=1731)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.267 (n=2469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.263)

- **PATRÓN** `drift_60min` |x|≤ `0.1182` → IC=+0.286 (n=1087)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1182 (IC base=+0.263)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=2266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` < `0.5152` → IC=+0.288 (n=2468)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5152 (IC base=+0.263)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.045` → IC=+0.266 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.045 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` < `0.0959` → IC=+0.265 (n=2214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0959 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.286 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.266 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` > `2.6599` → IC=+0.275 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6599 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2800)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `1458.1` → IC=+0.268 (n=2466)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1458.1 (IC base=+0.263)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.271 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.263)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.201 (n=961)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.164 (n=1264)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=2992)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.242` → IC=+0.203 (n=2873)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.242 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1837` → IC=+0.197 (n=1326)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1837 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.469` → IC=+0.162 (n=469)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.469 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.174` → IC=+0.151 (n=2648)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.174 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6306` → IC=+0.176 (n=959)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6306 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.153 (n=2563)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.180 (n=414)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1754` → IC=+0.159 (n=2475)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.1754 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5314` → IC=+0.154 (n=2512)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5314 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `237.0` → IC=+0.182 (n=920)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 237.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=2427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.3251` → IC=+0.157 (n=2427)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3251 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=905)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.6939` → IC=+0.196 (n=2427)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.6939 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.222` → IC=+0.154 (n=403)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.222 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.433` → IC=+0.145 (n=2444)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 6.433 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.154 (n=2427)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1917 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2189` → IC=+0.205 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2189 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.149 (n=2322)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7825` → IC=+0.153 (n=1548)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7825 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=3150)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `243.0` → IC=+0.159 (n=749)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 243.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.255 (n=987)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2644)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.242` → IC=+0.320 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.242 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.229 (n=2769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `3.1781` → IC=+0.243 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1781 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=3541)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1955.5029` → IC=+0.239 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1955.5029 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.245 (n=2451)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.261 (n=1226)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1054)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.037` → IC=+0.308 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.037 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.522` → IC=+0.296 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.522 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3465` → IC=+0.305 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3465 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1416` → IC=+0.250 (n=1771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1416 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.246 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1935.0406` → IC=+0.252 (n=1263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1935.0406 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.254 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.202 (n=1021)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4203` → IC=+0.158 (n=3049)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4203 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=3162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.2442` → IC=+0.191 (n=3049)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.2442 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1424` → IC=+0.171 (n=1602)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1424 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.035` → IC=+0.158 (n=1382)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 3.035 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0567` → IC=+0.158 (n=2683)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 1.0567 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.187 (n=404)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5223` → IC=+0.162 (n=1310)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5223 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1723` → IC=+0.153 (n=1349)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.1723 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `5709.9986` → IC=+0.239 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5709.9986 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.165 (n=1297)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 72.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.154 (n=2547)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0075 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4355` → IC=+0.140 (n=2546)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4355 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=932)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.7339` → IC=+0.186 (n=2546)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7339 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.1491` → IC=+0.145 (n=2338)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1491 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.13` → IC=+0.164 (n=388)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.13 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.143` → IC=+0.133 (n=2213)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.143 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.6141` → IC=+0.147 (n=849)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.6141 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.219 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.4258` → IC=+0.138 (n=2451)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4258 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6831.7439` → IC=+0.212 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6831.7439 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.134 (n=1649)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 99.0 (IC base=+0.131)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.161 (n=1394)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0104 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.44` → IC=+0.200 (n=3073)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.44 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.048` → IC=+0.208 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.048 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.645` → IC=+0.262 (n=779)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.645 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `0.883` → IC=+0.145 (n=2049)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.883 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.125 (n=3198)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.278` → IC=+0.127 (n=397)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.278 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.568` → IC=+0.131 (n=1321)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.568 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.1858` → IC=+0.124 (n=1361)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 2.1858 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=3197)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2758.2723` → IC=+0.242 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2758.2723 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.145 (n=960)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 23.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.152 (n=2568)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0101 (IC base=+0.117)

- **PATRÓN** `drift_60min` |x|≤ `0.1348` → IC=+0.154 (n=972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1348 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.130 (n=3001)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.6556` → IC=+0.213 (n=2916)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6556 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.22` → IC=+0.137 (n=2799)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.22 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6413` → IC=+0.144 (n=972)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6413 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2244` → IC=+0.169 (n=499)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2244 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.150 (n=914)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2638.5742` → IC=+0.201 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2638.5742 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.132 (n=2411)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 46.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.254 (n=2586)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=3014)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.236 (n=2596)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` > `0.6106` → IC=+0.273 (n=2584)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6106 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.1923` → IC=+0.249 (n=1554)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1923 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.271 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` < `1.2248` → IC=+0.239 (n=2893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2248 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.6392` → IC=+0.236 (n=2892)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6392 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.258 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.4773` → IC=+0.249 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4773 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=3760)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2949.7028` → IC=+0.238 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2949.7028 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.254 (n=999)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.240 (n=2820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.267 (n=2995)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.223` → IC=+0.272 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.223 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `1.227` → IC=+0.258 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.227 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.301 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `1.4285` → IC=+0.235 (n=2791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4285 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.230 (n=2716)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.233)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=5078)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.245 (n=1760)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.5066` → IC=+0.220 (n=5271)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5066 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.228 (n=1909)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9411` → IC=+0.253 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9411 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.7009` → IC=+0.213 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7009 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.4337` → IC=+0.212 (n=3748)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4337 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.93` → IC=+0.217 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.93 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.577` → IC=+0.212 (n=4693)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.577 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.224 (n=1678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.212 (n=4926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.1665` → IC=+0.219 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1665 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.454` → IC=+0.220 (n=1730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.454 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.8457` → IC=+0.210 (n=3459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8457 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=4020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `3710.0405` → IC=+0.220 (n=3514)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3710.0405 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.240 (n=1276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.3882` → IC=+0.214 (n=3362)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3882 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.211 (n=1702)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.1857` → IC=+0.208 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1857 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6733` → IC=+0.202 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6733 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.2396` → IC=+0.191 (n=3491)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2396 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.812` → IC=+0.203 (n=3434)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.812 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.095` → IC=+0.202 (n=3192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.095 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.197 (n=3506)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.197 (n=771)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5338` → IC=+0.198 (n=1657)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5338 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.1925` → IC=+0.202 (n=1706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1925 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=5078)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.209 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.193)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.275 (n=677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.0849` → IC=+0.295 (n=256)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0849 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.272 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.260 (n=770)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.4896` → IC=+0.280 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4896 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.051` → IC=+0.275 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.051 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.268 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2151 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `0.8676` → IC=+0.272 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8676 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.343 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.8216` → IC=+0.268 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8216 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `16312.8746` → IC=+0.275 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16312.8746 (IC base=+0.260)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.254 (n=588)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.1108` → IC=+0.207 (n=588)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1108 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.222 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.198 (n=491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.207 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1409 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.177 (n=605)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.6084 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.7021` → IC=+0.181 (n=117)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.7021 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.391` → IC=+0.195 (n=1317)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 6.391 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.191 (n=1334)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` < 1.2212 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1534` → IC=+0.199 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1534 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `2.5013` → IC=+0.183 (n=1327)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 2.5013 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.1667` → IC=+0.187 (n=602)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.1667 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14916.9219` → IC=+0.187 (n=605)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14916.9219 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `692.0` → IC=+0.188 (n=1288)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 692.0 (IC base=+0.176)

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
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.214 (n=1227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.1476` → IC=+0.210 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1476 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.5186` → IC=+0.209 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5186 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.7587` → IC=+0.200 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7587 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.105` → IC=+0.205 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.105 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.875` → IC=+0.200 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.875 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.2263` → IC=+0.204 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2263 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.1047` → IC=+0.200 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1047 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.204 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=1427)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.240 (n=382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3872` → IC=+0.218 (n=1004)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3872 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.201 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.199 (n=763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.3986` → IC=+0.195 (n=761)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3986 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.6238` → IC=+0.192 (n=517)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.6238 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.6607` → IC=+0.198 (n=200)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6607 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6391` → IC=+0.221 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6391 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `0.7208` → IC=+0.188 (n=1019)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 0.7208 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.212 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1925` → IC=+0.195 (n=982)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1925 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.7842` → IC=+0.192 (n=744)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 1.7842 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `6672.577` → IC=+0.198 (n=1140)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6672.577 (IC base=+0.187)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.205 (n=690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.208 (n=748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.259 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.7405` → IC=+0.240 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7405 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.236` → IC=+0.199 (n=423)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 2.236 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.7016` → IC=+0.229 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7016 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.195 (n=705)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.5649` → IC=+0.191 (n=334)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` < 1.5649 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.8151` → IC=+0.191 (n=506)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.8151 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=914)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `4301.4058` → IC=+0.226 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4301.4058 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.195 (n=771)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 52.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.216 (n=385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.208 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.4993` → IC=+0.231 (n=508)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4993 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.246 (n=392)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.235 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.5149` → IC=+0.212 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5149 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.3065` → IC=+0.211 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3065 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `1.1288` → IC=+0.212 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1288 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` > `0.9335` → IC=+0.211 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9335 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.1067` → IC=+0.228 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1067 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `2.2063` → IC=+0.243 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2063 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `3019.8404` → IC=+0.225 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3019.8404 (IC base=+0.208)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.252 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.208)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.156 (n=782)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0041 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.3906` → IC=+0.141 (n=1684)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.3906 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1482` → IC=+0.145 (n=872)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1482 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.907` → IC=+0.148 (n=489)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.907 (IC base=+0.070)

- **PATRÓN** `volumen_pendiente_norm` > `0.2746` → IC=+0.148 (n=234)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2746 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.031` → IC=+0.264 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.031 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.304` → IC=+0.167 (n=157)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 10.304 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.146` → IC=+0.158 (n=276)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.146 (IC base=+0.054)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.134 (n=586)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0057 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.3574` → IC=+0.170 (n=555)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.3574 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.1276` → IC=+0.166 (n=279)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1276 (IC base=+0.090)

- **PATRÓN** `ibs_20min` < `0.0617` → IC=+0.280 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0617 (IC base=+0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.2135` → IC=+0.198 (n=84)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2135 (IC base=+0.066)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.128 (n=512)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.006 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.8234` → IC=+0.245 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8234 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1258` → IC=+0.188 (n=280)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1258 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.124` → IC=+0.232 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.124 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.106` → IC=+0.238 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.106 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.023)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7308` → IC=+0.155 (n=387)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` > 0.7308 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.7321` → IC=+0.148 (n=140)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.7321 (IC base=+0.029)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.234` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 9.234 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2775` → IC=+0.134 (n=80)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2775 (IC base=+0.029)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.152 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0108 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.1176` → IC=+0.230 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1176 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.1685` → IC=+0.136 (n=223)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1685 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.474` → IC=+0.329 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.474 (IC base=+0.073)

- **PATRÓN** `volumen_regimen` > `1.0763` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` > 1.0763 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1499` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1499 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `2.1886` → IC=+0.149 (n=186)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.1886 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` > `1.4913` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.4913 (IC base=+0.073)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.137 (n=213)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.06 (IC base=+0.073)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1888` → IC=-0.302 (n=79)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1888
  - _Potencial_: sin este filtro IC_bueno=-0.165 (n=240)

- **FILTRO** `dist_vwap_pct` > `0.2321` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2321
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=304)

- **FILTRO** `volumen_regimen` < `0.7708` → IC=-0.305 (n=80)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7708
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=241)

- **FILTRO** `drift_60min` |x|> `0.1933` → IC=-0.326 (n=67)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1933
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=204)

- **FILTRO** `ibs_20min` > `0.5495` → IC=-0.336 (n=138)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5495
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=139)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=258)

- **FILTRO** `sigma_ewma_delta_pct` > `10.358` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.358
  - _Potencial_: sin este filtro IC_bueno=-0.287 (n=251)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=160)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.2175` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2175
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=50)

- **FILTRO** `volumen_spike_ratio` > `1.5538` → IC=-0.351 (n=45)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.5538
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=47)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.466 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=81)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=82)

- **FILTRO** `ibs_20min` > `0.538` → IC=-0.387 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` > 0.538
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=53)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.350 (n=18)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=54)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.291 (n=89)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 1.0 (IC base=-0.154)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=96)

- **FILTRO** `dist_vwap_pct` > `0.0599` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0599
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=88)

- **FILTRO** `volumen_spike_ratio` > `2.3459` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3459
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=59)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.316 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=33)

- **FILTRO** `dist_vwap_pct` < `0.2328` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2328
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.184 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0076 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.158 (n=574)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.6667 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.5394` → IC=+0.238 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5394 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.654` → IC=+0.134 (n=129)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 10.654 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.6187` → IC=+0.179 (n=191)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6187 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1521` → IC=+0.150 (n=478)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.1521 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.3996` → IC=+0.179 (n=157)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.3996 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.1415` → IC=+0.145 (n=579)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.1415 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.085` → IC=+0.172 (n=193)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.085 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `3239.2397` → IC=+0.128 (n=439)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 3239.2397 (IC base=+0.055)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6991` → IC=-0.178 (n=57)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6991
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=174)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.165 (n=204)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0035 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.140 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 12.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.152 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 6.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.1681` → IC=+0.193 (n=307)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.1681 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.168` → IC=+0.160 (n=95)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 10.168 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `1.0363` → IC=+0.167 (n=139)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 1.0363 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.07` → IC=+0.139 (n=242)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.07 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `2.5115` → IC=+0.157 (n=275)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 2.5115 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4397` → IC=+0.143 (n=275)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.4397 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `5398.7573` → IC=+0.146 (n=204)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 5398.7573 (IC base=+0.129)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=182)

- **FILTRO** `ibs_20min` > `0.1696` → IC=-0.151 (n=107)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1696
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=208)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.122 (n=191)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0061 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.105)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.147 (n=171)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.8015 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.0908` → IC=+0.136 (n=160)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.0908 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.022` → IC=+0.146 (n=142)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 3.022 (IC base=+0.105)

- **PATRÓN** `volumen_regimen` < `0.6141` → IC=+0.182 (n=64)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6141 (IC base=+0.105)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.105)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.176 (n=109)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.224 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.014)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2391` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2391
  - _Potencial_: sin este filtro IC_bueno=+0.048 (n=102)

- **FILTRO** `dist_vwap_pct` > `0.1696` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1696
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=116)

- **FILTRO** `volumen_regimen` < `0.9796` → IC=-0.133 (n=77)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9796
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=77)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.283 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.288 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.258 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.396 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.152` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.152 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.276 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.0973` → IC=+0.297 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0973 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.4815` → IC=+0.357 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4815 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.058)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.318 (n=75)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.234)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.234)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.255 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.264 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.234)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.318 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.234)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.318 (n=75)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.266 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.234)

- **PATRÓN** `elapsed_s` > `182.9` → IC=+0.246 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 182.9 (IC base=+0.234)

- **PATRÓN** `elapsed_s` < `203.6` → IC=+0.255 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 203.6 (IC base=+0.234)

- **PATRÓN** `drift_15min` |x|≤ `2.3354` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3354 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.264 (n=70)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.234)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.318 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.234)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2933.9421` → IC=+0.134 (n=440)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2933.9421 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2933.9421` → IC=+0.134 (n=440)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2933.9421 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=204)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=203)

- **FILTRO** `libro_liquidez` < `5529.6254` → IC=-0.176 (n=109)

  - _Acción_: SKIP cuando `libro_liquidez` < 5529.6254
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=110)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=394)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=76)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=66)

- **PATRÓN** `liq_n` > `6.0` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `liq_n` > 6.0 (IC base=+0.000)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `hora_utc` < `10.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **PATRÓN** `liq_n` > `5.0` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 5.0 (IC base=+0.052)

- **PATRÓN** `liq_usd_total` > `1039.23` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `liq_usd_total` > 1039.23 (IC base=+0.052)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=3628)

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
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=132)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1374)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1328)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=709)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=436)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=417)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.145 (n=181)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.020)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=870)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=870)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=898)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=898)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=229)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=229)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.129 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=176)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.141 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=168)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=262)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=286)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=267)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.120 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=248)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=359)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=359)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=204)

- **FILTRO** `libro_liquidez` < `632.1854` → IC=-0.131 (n=128)

  - _Acción_: SKIP cuando `libro_liquidez` < 632.1854
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=261)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=272)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=200)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `10.75` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `restante_min` < 10.75
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=42)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.58 (IC base=+0.016)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.123 (n=67)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=35)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `restante_min` < `3.93` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `restante_min` < 3.93
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=34)

- **FILTRO** `lag_apertura_s` > `64.36` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `lag_apertura_s` > 64.36
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.167 (n=166)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.46 (IC base=+0.016)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.156 (n=62)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=290)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=152)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.167 (n=118)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=246)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.5 (IC base=+0.056)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.125 (n=355)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=203)

- **FILTRO** `profundidad_ratio` < `43.3` → IC=-0.160 (n=139)

  - _Acción_: SKIP cuando `profundidad_ratio` < 43.3
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=419)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.196 (n=90)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=376)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.160 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=425)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.132 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=512)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=6455)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=19606)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.176 (n=6478)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20348)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.191 (n=1168)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3604)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.177 (n=1109)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3674)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1253)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `1200.799` → IC=+0.137 (n=2386)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1200.799 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.127 (n=2239)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1402.4318` → IC=+0.150 (n=1627)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1402.4318 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.150 (n=906)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=2869)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.179 (n=924)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2877)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.203 (n=1138)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=3753)

- **PATRÓN** `ibs_20min` > `0.965` → IC=+0.131 (n=1622)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.965 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1478.6384` → IC=+0.122 (n=2384)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1478.6384 (IC base=+0.037)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.157 (n=1177)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=3591)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2407)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2331)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.191 (n=898)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=2740)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=3617)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.257 (n=142)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=430)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=923)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.192 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=304)

- **FILTRO** `libro_liquidez` < `3165.3462` → IC=-0.178 (n=147)

  - _Acción_: SKIP cuando `libro_liquidez` < 3165.3462
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=301)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=943)

- **FILTRO** `libro_liquidez` < `1786.4389` → IC=-0.161 (n=240)

  - _Acción_: SKIP cuando `libro_liquidez` < 1786.4389
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=722)

- **FILTRO** `ibs_20min` > `0.8939` → IC=-0.131 (n=532)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8939
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=534)

- **FILTRO** `libro_liquidez` < `2096.2738` → IC=-0.169 (n=351)

  - _Acción_: SKIP cuando `libro_liquidez` < 2096.2738
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=715)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=233)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=17986)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=40048)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.286 (n=14447)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=43587)

- **FILTRO** `ibs_7min` < `0.2332` → IC=-0.230 (n=14508)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2332
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=43526)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=19119)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=38915)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.241 (n=17911)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=54949)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.183 (n=17973)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=54887)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.150 (n=2895)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7287)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=2437)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=7745)

- **FILTRO** `ibs_7min` < `0.7126` → IC=-0.244 (n=3360)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7126
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6822)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.182 (n=2068)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8114)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.271 (n=3154)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=9484)

- **FILTRO** `ibs_7min` > `0.7692` → IC=-0.211 (n=3156)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=9482)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.129 (n=2357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=7397)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=2296)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=7458)

- **FILTRO** `ibs_7min` < `0.7219` → IC=-0.201 (n=2437)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7219
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7317)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.190 (n=2432)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7322)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.260 (n=2441)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=7500)

- **FILTRO** `ibs_7min` > `0.2664` → IC=-0.194 (n=2485)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2664
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7456)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.181 (n=2472)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7469)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.161 (n=2387)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=7283)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.313 (n=2391)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=7279)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.246 (n=3191)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=6479)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2241)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7429)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.256 (n=3130)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=10292)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.177 (n=3354)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=10068)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.126 (n=3093)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=6350)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=2243)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7200)

- **FILTRO** `ibs_7min` < `0.7243` → IC=-0.192 (n=2360)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7243
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7083)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.191 (n=2293)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7150)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.263 (n=2210)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7586)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.177 (n=2446)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=7350)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.176 (n=2356)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7440)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=2327)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7149)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.222 (n=3084)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=6392)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.218 (n=2273)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7203)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.191 (n=3424)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=10486)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.294 (n=2278)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=7231)

- **FILTRO** `ibs_7min` < `0.2` → IC=-0.224 (n=2374)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=7135)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.199 (n=2332)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=7177)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.219 (n=3220)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9933)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

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
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=503)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=556)

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
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=853)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.475` → IC=-0.122 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=335)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=330)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=447)

- **FILTRO** `libro_liquidez` < `3257.9143` → IC=-0.156 (n=181)

  - _Acción_: SKIP cuando `libro_liquidez` < 3257.9143
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=543)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.139 (n=1223)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.139 (n=541)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 5.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `437.371` → IC=+0.158 (n=407)

  - _Acción_: Kelly boost +0.79€ cuando `total_vol_5m` < 437.371 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3566.692` → IC=+0.147 (n=554)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 3566.692 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.149 (n=417)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 11.0 (IC base=+0.131)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4385` → IC=+0.139 (n=95)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4385 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.191 (n=137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 14.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `371.804` → IC=+0.148 (n=251)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 371.804 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2387.2349` → IC=+0.187 (n=129)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2387.2349 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.157 (n=100)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 6.0 (IC base=+0.138)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3988` → IC=+0.140 (n=251)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.3988 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.140 (n=226)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 14.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.132 (n=302)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.04 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2328.6506` → IC=+0.139 (n=167)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2328.6506 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.141 (n=165)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 12.0 (IC base=+0.122)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.191 (n=160)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.96€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.153 (n=249)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 4.0 (IC base=+0.140)

- **PATRÓN** `total_vol_5m` < `385.7846` → IC=+0.222 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 385.7846 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `7599.7355` → IC=+0.142 (n=160)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7599.7355 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.188 (n=107)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 69.0 (IC base=+0.140)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4318` → IC=+0.230 (n=98)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4318 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.153)

- **PATRÓN** `total_vol_5m` < `4909.564` → IC=+0.185 (n=144)

  - _Acción_: Kelly boost +0.92€ cuando `total_vol_5m` < 4909.564 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `3200.0566` → IC=+0.170 (n=192)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 3200.0566 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 26.0 (IC base=+0.153)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.141 (n=157)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 10.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=149)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `3568.9496` → IC=+0.145 (n=105)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3568.9496 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.9794` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.9794
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=139)

- **FILTRO** `sigma_h` > `0.0073` → IC=-0.327 (n=171)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0073
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=515)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.151 (n=227)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0042 (IC base=-0.084)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0054` → IC=-0.248 (n=101)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=103)

- **FILTRO** `T_h` > `87.9901` → IC=-0.250 (n=50)

  - _Acción_: SKIP cuando `T_h` > 87.9901
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=154)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.296 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.034)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0062` → IC=-0.232 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `pct_vs_K` |x|> `9.8932` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.8932
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0137` → IC=-0.250 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0137
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=93)

- **FILTRO** `T_h` < `61.0064` → IC=-0.143 (n=40)

  - _Acción_: SKIP cuando `T_h` < 61.0064
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=83)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.227 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=-0.108)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.232 (n=416)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=215)

- **FILTRO** `T_h` > `87.0918` → IC=-0.203 (n=422)

  - _Acción_: SKIP cuando `T_h` > 87.0918
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=209)

- **FILTRO** `pct_vs_K` |x|> `2.8988` → IC=-0.403 (n=184)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.8988
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=360)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `71.159` → IC=-0.186 (n=138)

  - _Acción_: SKIP cuando `T_h` > 71.159
  - _Potencial_: sin este filtro IC_bueno=-0.120 (n=69)

- **FILTRO** `pct_vs_K` |x|> `2.7791` → IC=-0.368 (n=51)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7791
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=156)

- **FILTRO** `T_h` > `73.0783` → IC=-0.269 (n=145)

  - _Acción_: SKIP cuando `T_h` > 73.0783
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=49)

- **FILTRO** `pct_vs_K` |x|> `2.9778` → IC=-0.439 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9778
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=147)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.007` → IC=-0.285 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=91)

- **FILTRO** `T_h` > `69.4221` → IC=-0.261 (n=136)

  - _Acción_: SKIP cuando `T_h` > 69.4221
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=46)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.364 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=128)

- **FILTRO** `T_h` > `57.7851` → IC=-0.272 (n=112)

  - _Acción_: SKIP cuando `T_h` > 57.7851
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=58)

- **PATRÓN** `pct_vs_K` |x|≤ `0.7672` → IC=+0.167 (n=43)

  - _Acción_: Kelly boost +0.83€ cuando `pct_vs_K` |x|≤ 0.7672 (IC base=-0.180)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.008` → IC=-0.278 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=132)

- **FILTRO** `T_h` > `87.9882` → IC=-0.206 (n=117)

  - _Acción_: SKIP cuando `T_h` > 87.9882
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=58)

- **FILTRO** `sigma_h` > `0.0152` → IC=-0.375 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0152
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=91)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.281 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=82)

- **FILTRO** `T_h` > `63.9197` → IC=-0.290 (n=60)

  - _Acción_: SKIP cuando `T_h` > 63.9197
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=61)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1236` → IC=+0.477 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1236 (IC base=+0.344)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.359 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.344)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.396 (n=65)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.344)

- **PATRÓN** `T_h` < `0.3604` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3604 (IC base=+0.344)

- **PATRÓN** `T_h` > `0.7606` → IC=+0.381 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7606 (IC base=+0.344)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.344)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.359 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.344)

- **PATRÓN** `edge` > `0.0992` → IC=+0.443 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.0992 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.436 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.417)

- **PATRÓN** `T_h` > `1.484` → IC=+0.422 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.3767` → IC=+0.452 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3767 (IC base=+0.417)

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
- **PATRÓN** `edge` > `0.1884` → IC=+0.484 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1884 (IC base=+0.441)

- **PATRÓN** `sigma_h` < `0.0164` → IC=+0.468 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0164 (IC base=+0.441)

- **PATRÓN** `T_h` > `0.4292` → IC=+0.452 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4292 (IC base=+0.441)

- **PATRÓN** `dist_50` > `0.3553` → IC=+0.468 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3553 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.439 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.441)

- **PATRÓN** `edge` > `0.2005` → IC=+0.479 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.466)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.479 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.466)

- **PATRÓN** `T_h` > `1.4874` → IC=+0.480 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4874 (IC base=+0.466)

- **PATRÓN** `dist_50` > `0.4658` → IC=+0.492 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4658 (IC base=+0.466)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.473 (n=145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.466)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=327)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=399)

- **PATRÓN** `streak_estiramiento` < `0.3906` → IC=+0.122 (n=109)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.3906 (IC base=+0.006)

- **PATRÓN** `streak_estiramiento` < `0.836` → IC=+0.127 (n=269)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.836 (IC base=+0.052)

- **PATRÓN** `libro_liquidez` > `2507.3405` → IC=+0.137 (n=144)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2507.3405 (IC base=+0.052)

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
- **PATRÓN** `streak_estiramiento` < `0.2204` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `streak_estiramiento` < 0.2204 (IC base=+0.007)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.095)

- **PATRÓN** `streak_estiramiento` < `0.437` → IC=+0.192 (n=105)

  - _Acción_: Kelly boost +0.96€ cuando `streak_estiramiento` < 0.437 (IC base=+0.095)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 35.0 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `2186.8766` → IC=+0.143 (n=138)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2186.8766 (IC base=+0.095)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=97)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=106)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=34)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=33)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `hora_utc` < `11.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.140 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=1036)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1332)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1218)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=1257)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `19.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=27)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=4152)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `19.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=27)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2323)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.191 (n=1686)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0054 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.188 (n=1278)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0121 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.188 (n=3372)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.172)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3485` → IC=+0.178 (n=3493)

  - _Acción_: Kelly boost +0.89€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3485 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=3546)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.174 (n=3537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 15.0 (IC base=+0.172)

- **PATRÓN** `ibs_15` > `0.5417` → IC=+0.246 (n=3836)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5417 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1298` → IC=+0.167 (n=1844)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1298 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` < `0.3175` → IC=+0.157 (n=3072)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.3175 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.4` → IC=+0.259 (n=988)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.4 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `4629.3821` → IC=+0.189 (n=1278)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 4629.3821 (IC base=+0.172)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=1525)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.254 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.213)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.214 (n=295)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.0587` → IC=+0.263 (n=217)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0587 (IC base=+0.213)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.235 (n=217)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.233 (n=680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.213)

- **PATRÓN** `ibs_15` > `0.7193` → IC=+0.281 (n=650)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7193 (IC base=+0.213)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.229 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.294 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=844)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `8520.5321` → IC=+0.222 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8520.5321 (IC base=+0.213)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.185 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0035 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.161 (n=509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1416` → IC=+0.152 (n=509)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1416 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1262` → IC=+0.149 (n=303)

  - _Acción_: Kelly boost +0.75€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1262 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.149 (n=796)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5365` → IC=+0.239 (n=762)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5365 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.162 (n=471)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.827` → IC=+0.277 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.827 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `6251.2816` → IC=+0.161 (n=346)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 6251.2816 (IC base=+0.145)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `23.781` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.781
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=385)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8831` → IC=+0.243 (n=305)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8831 (IC base=+0.087)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=487)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.087)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.781` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 15.781 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0241` → IC=+0.228 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0241 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1304` → IC=+0.222 (n=576)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1304 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3415` → IC=+0.224 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3415 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.208 (n=772)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.274 (n=864)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.213 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.324` → IC=+0.230 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.324 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2955.9488` → IC=+0.293 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2955.9488 (IC base=+0.198)

- **PATRÓN** `ibs_15` < `0.1089` → IC=+0.167 (n=793)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.1089 (IC base=+0.070)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.390 (n=298)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.384 (n=438)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1392` → IC=+0.389 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1392 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=661)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7872` → IC=+0.401 (n=657)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7872 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1521` → IC=+0.382 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1521 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.390 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3851.736` → IC=+0.374 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3851.736 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `344.0` → IC=+0.380 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 344.0 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.366 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.362)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.404 (n=112)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.368 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.383 (n=152)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.395 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.380 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.391 (n=336)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.1089` → IC=+0.377 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1089 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.365` → IC=+0.381 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.365 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `8041.1866` → IC=+0.388 (n=336)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8041.1866 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `497.0` → IC=+0.402 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 497.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.375 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.367)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.385 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.367)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.366 (n=215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.367)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0842` → IC=+0.382 (n=287)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0842 (IC base=+0.367)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.385 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.367)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.392 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.367)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.378 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.367)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.410 (n=321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.388 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.367)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.370 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.367)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.408` → IC=+0.397 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.408 (IC base=+0.367)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.373 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.367)

- **PATRÓN** `libro_liquidez` > `4019.374` → IC=+0.399 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4019.374 (IC base=+0.367)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.377 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.367)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.175 (n=2247)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=2249)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=1761)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2735)

- **FILTRO** `libro_liquidez` < `4239.822` → IC=-0.154 (n=2967)

  - _Acción_: SKIP cuando `libro_liquidez` < 4239.822
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1529)

- **PATRÓN** `ibs_15` > `0.6332` → IC=+0.280 (n=1088)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6332 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1115` → IC=+0.206 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1115 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.197 (n=928)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.271 (n=1263)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3665` → IC=+0.284 (n=3785)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3665 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.6614` → IC=+0.278 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6614 (IC base=-0.011)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.212 (n=668)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=2006)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.230 (n=668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=2006)

- **FILTRO** `sigma_ewma_delta_pct` > `23.313` → IC=-0.266 (n=386)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.313
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=2288)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=66)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=2608)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.168 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0028 (IC base=+0.093)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1458` → IC=+0.273 (n=240)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1458 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.126 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 15.0 (IC base=+0.093)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.332 (n=360)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.282 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` < `0.3703` → IC=+0.288 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3703 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.813` → IC=+0.140 (n=184)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 23.813 (IC base=+0.093)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.227 (n=64)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.300 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.192)

- **PATRÓN** `ibs_15` < `0.6128` → IC=+0.318 (n=64)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6128 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.0415` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0415 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=-0.192)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=711)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.163 (n=481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.159 (n=364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0049 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0721` → IC=+0.187 (n=241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.0721 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2962` → IC=+0.193 (n=421)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2962 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.5959` → IC=+0.248 (n=546)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5959 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.4686` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.4686 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.153 (n=430)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.387` → IC=+0.252 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.387 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=711)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `5211.9622` → IC=+0.156 (n=364)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 5211.9622 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=1403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.246)

- **PATRÓN** `drift_15min` |x|≤ `0.7706` → IC=+0.259 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7706 (IC base=+0.246)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1554` → IC=+0.263 (n=935)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1554 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.247 (n=1245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.246)

- **PATRÓN** `ibs_15` < `0.3774` → IC=+0.279 (n=1404)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3774 (IC base=+0.246)

- **PATRÓN** `dist_vwap_pct` > `0.1547` → IC=+0.262 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1547 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.392` → IC=+0.254 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.392 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.411` → IC=+0.251 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.411 (IC base=+0.246)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0106` → IC=-0.232 (n=259)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=781)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.251 (n=352)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=688)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.282 (n=259)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=781)

- **FILTRO** `sigma_ewma_delta_pct` > `6.65` → IC=-0.201 (n=239)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.65
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=801)

- **FILTRO** `sigma_ewma_delta_pct` > `17.769` → IC=-0.147 (n=545)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.769
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4338)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.189)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.189)

- **PATRÓN** `dist_vwap_pct` < `0.1292` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1292 (IC base=-0.189)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.189)

- **PATRÓN** `delta_ratio_macro` |x|> `0.082` → IC=+0.227 (n=559)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.082 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.3714` → IC=+0.291 (n=624)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3714 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.2583` → IC=+0.238 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2583 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.253 (n=617)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=618)

- **FILTRO** `drift_15min` |x|> `0.7503` → IC=-0.250 (n=617)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7503
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=618)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.211)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0695` → IC=+0.277 (n=796)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0695 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1174` → IC=+0.295 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1174 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.137` → IC=+0.317 (n=595)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.137 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.786` → IC=+0.353 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.786 (IC base=-0.025)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.167 (n=25)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.3976` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `drift_15min` |x|≤ 0.3976 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 59.0 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.045)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0037 (IC base=+0.088)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.167 (n=25)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.088)

- **PATRÓN** `drift_15min` |x|≤ `0.3976` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `drift_15min` |x|≤ 0.3976 (IC base=+0.088)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.220 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.8489` → IC=+0.342 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8489 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 59.0 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.198` → IC=+0.121 (n=64)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.198 (IC base=+0.045)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.300 (n=379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0541` → IC=+0.322 (n=379)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0541 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2411` → IC=+0.304 (n=380)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2411 (IC base=+0.290)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2244` → IC=+0.302 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2244 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.306 (n=1181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.8389` → IC=+0.319 (n=1136)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8389 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2713` → IC=+0.326 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2713 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.638` → IC=+0.379 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.638 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `12139.6` → IC=+0.308 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12139.6 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.310 (n=203)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.302 (n=276)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.320 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.304 (n=202)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8631` → IC=+0.315 (n=543)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8631 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.1479` → IC=+0.319 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1479 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.701` → IC=+0.378 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.701 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `16178.7073` → IC=+0.329 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16178.7073 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.304 (n=529)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0524` → IC=+0.321 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0524 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.298 (n=529)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1029` → IC=+0.323 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1029 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.313 (n=511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.298 (n=478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8494` → IC=+0.325 (n=529)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8494 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.321 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.375 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.132 (n=85)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=259)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1232` → IC=-0.155 (n=85)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1232
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=259)

- **FILTRO** `ballena_activa_n` > `43.0` → IC=-0.133 (n=232)

  - _Acción_: SKIP cuando `ballena_activa_n` > 43.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=80)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=365)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.180 (n=120)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=364)

- **FILTRO** `drift_15min` |x|> `0.4386` → IC=-0.151 (n=164)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4386
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=320)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1342` → IC=-0.154 (n=50)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1342
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=151)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2377` → IC=-0.125 (n=94)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2377
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=95)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2021` → IC=-0.250 (n=26)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2021
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=27)

- **FILTRO** `ballena_activa_n` > `528.0` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `ballena_activa_n` > 528.0
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=24)

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
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.075` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.075
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

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
- **PATRÓN** `T_h` > `87.7391` → IC=+0.194 (n=502)

  - _Acción_: Kelly boost +0.97€ cuando `T_h` > 87.7391 (IC base=+0.189)

- **PATRÓN** `ratio` < `0.973` → IC=+0.407 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.189)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.354 (n=2295)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.376 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `109.5528` → IC=+0.181 (n=208)

  - _Acción_: Kelly boost +0.90€ cuando `T_h` > 109.5528 (IC base=+0.157)

- **PATRÓN** `ratio` < `0.9838` → IC=+0.323 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9838 (IC base=+0.157)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.306 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.295)

- **PATRÓN** `ratio` > `1.0451` → IC=+0.407 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0451 (IC base=+0.295)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.236 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.229)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.397 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.229)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.352 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.335 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0788` → IC=+0.439 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.172 a +0.246 en UPDOWN_GBM#15min (n=3836). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7193 sube el IC de +0.213 a +0.281 en UPDOWN_GBM#BTC#15min (n=650). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5365 sube el IC de +0.145 a +0.239 en UPDOWN_GBM#ETH#15min (n=762). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8831 sube el IC de +0.087 a +0.243 en UPDOWN_GBM#SOL#15min (n=305). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.198 a +0.274 en UPDOWN_GBM#XRP#15min (n=864). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1089 sube el IC de +0.070 a +0.167 en UPDOWN_GBM#XRP#15min (n=793). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6332 sube el IC de -0.068 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1088). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3665 sube el IC de -0.011 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=3785). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.093 a +0.332 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=360). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6128 sube el IC de -0.192 a +0.318 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=64). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5959 sube el IC de +0.152 a +0.248 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=546). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3774 sube el IC de +0.246 a +0.279 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1404). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3714 sube el IC de -0.038 a +0.291 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=624). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.211 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.137 sube el IC de -0.025 a +0.317 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=595). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.088 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7 (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8489 sube el IC de +0.088 a +0.342 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=17). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8389 sube el IC de +0.290 a +0.319 en UPDOWN_GBM_IBS_ALTO (n=1136). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8631 sube el IC de +0.285 a +0.315 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=543). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8494 sube el IC de +0.295 a +0.325 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=529). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7872 sube el IC de +0.365 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=657). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.362 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=336). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.367 a +0.410 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1988 | +0.090 | +209.12€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1988 | +0.090 | +209.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1596 | +0.093 | +180.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1596 | +0.093 | +180.39€ | 0 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 772 | -0.005 | +85.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 772 | -0.005 | +85.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 581 | -0.032 | +52.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 581 | -0.032 | +52.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 41666 | -0.082 | -5157.72€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2362 | +0.045 | -268.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 39304 | -0.089 | -4889.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4553 | -0.114 | -781.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4553 | -0.114 | -781.39€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2362 | +0.045 | -268.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2362 | +0.045 | -268.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4481 | -0.110 | -877.82€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4481 | -0.110 | -877.82€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11158 | -0.022 | -1089.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11158 | -0.022 | -1089.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11089 | -0.108 | -810.59€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11089 | -0.108 | -810.59€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8023 | -0.132 | -1330.02€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8023 | -0.132 | -1330.02€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 37510 | -0.015 | +3240.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 9694 | +0.004 | +1637.82€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 27816 | -0.021 | +1602.83€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 37510 | -0.015 | +3240.65€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 9694 | +0.004 | +1637.82€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 27816 | -0.021 | +1602.83€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 152799 | +0.115 | -6071.55€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 19248 | +0.182 | -616.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 679 | -0.013 | -72.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 123807 | +0.107 | -5039.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9065 | +0.097 | -342.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 20525 | +0.108 | -1258.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 62 | -0.156 | +10.44€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 20448 | +0.109 | -1256.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 29466 | +0.127 | -480.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5296 | +0.185 | -206.34€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 20509 | +0.120 | -130.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3619 | +0.081 | -121.46€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 20581 | +0.100 | -1421.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 78 | -0.113 | -2.92€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 20488 | +0.101 | -1407.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 32510 | +0.124 | -598.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8369 | +0.177 | -172.38€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 20796 | +0.107 | -367.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3333 | +0.101 | -49.69€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 29168 | +0.115 | -1387.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5372 | +0.198 | -249.09€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 582 | +0.019 | -18.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 21101 | +0.096 | -948.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2113 | +0.119 | -171.35€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 20549 | +0.107 | -925.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 71 | -0.103 | +3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 20465 | +0.108 | -929.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 24591 | +0.197 | -1484.77€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 24591 | +0.197 | -1484.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5583 | +0.181 | -460.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5583 | +0.181 | -460.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3211 | +0.202 | -80.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3211 | +0.202 | -80.13€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5520 | +0.180 | -443.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5520 | +0.180 | -443.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4761 | +0.248 | -167.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4761 | +0.248 | -167.64€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5437 | +0.188 | -347.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5437 | +0.188 | -347.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1061 | +0.426 | -38.44€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1061 | +0.426 | -38.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 422 | +0.434 | -8.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 422 | +0.434 | -8.15€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 418 | +0.431 | -9.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 418 | +0.431 | -9.42€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 207 | +0.400 | -17.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 207 | +0.400 | -17.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 86195 | +0.201 | -6132.29€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 86195 | +0.201 | -6132.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 14809 | +0.186 | -1518.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 14809 | +0.186 | -1518.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13916 | +0.225 | -465.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13916 | +0.225 | -465.97€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 14770 | +0.181 | -1551.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 14770 | +0.181 | -1551.35€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 14014 | +0.219 | -546.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 14014 | +0.219 | -546.86€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 14303 | +0.202 | -927.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 14303 | +0.202 | -927.27€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 14383 | +0.198 | -1122.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 14383 | +0.198 | -1122.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 33064 | +0.117 | +207.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 33064 | +0.117 | +207.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 16441 | +0.119 | +176.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 16441 | +0.119 | +176.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 16623 | +0.114 | +31.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 16623 | +0.114 | +31.22€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2161 | +0.292 | -9.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2161 | +0.292 | -9.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 991 | +0.281 | -24.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 991 | +0.281 | -24.86€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1047 | +0.297 | +12.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1047 | +0.297 | +12.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 123 | +0.340 | +2.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 123 | +0.340 | +2.44€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 994 | +0.443 | +6.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 994 | +0.443 | +6.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 483 | +0.436 | -4.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 483 | +0.436 | -4.51€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 464 | +0.451 | +10.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 464 | +0.451 | +10.53€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 47 | +0.398 | +0.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 47 | +0.398 | +0.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1718 | +0.069 | -73.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 668 | +0.043 | -63.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1050 | +0.086 | -9.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 77 | +0.108 | +3.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 77 | +0.108 | +3.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1317 | +0.077 | -32.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 267 | +0.043 | -22.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1050 | +0.086 | -9.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 324 | +0.028 | -43.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 324 | +0.028 | -43.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 65632 | +0.101 | -1605.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5301 | +0.092 | +65.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 60331 | +0.102 | -1670.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 36055 | +0.105 | -390.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5301 | +0.092 | +65.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 30754 | +0.108 | -455.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 13597 | +0.110 | -67.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 13597 | +0.110 | -67.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 15980 | +0.083 | -1147.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 15980 | +0.083 | -1147.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 899 | +0.192 | -110.13€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 899 | +0.192 | -110.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 899 | +0.192 | -110.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 899 | +0.192 | -110.13€ | 1 | 4 |
| ✅ GBM_LATE_15M | 44980 | +0.095 | +23768.57€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 44980 | +0.095 | +23768.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7477 | +0.219 | +6238.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7477 | +0.219 | +6238.72€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6796 | +0.180 | +5241.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6796 | +0.180 | +5241.22€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 8053 | +0.205 | +6258.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8053 | +0.205 | +6258.17€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 6237 | +0.044 | +1800.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6237 | +0.044 | +1800.76€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 6313 | -0.032 | +1375.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6313 | -0.032 | +1375.53€ | 4 | 12 |
| ✅ GBM_LATE_15M#XRP | 10104 | -0.030 | +2854.16€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 10104 | -0.030 | +2854.16€ | 4 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 48223 | +0.085 | +26491.75€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 48223 | +0.085 | +26491.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9319 | +0.002 | +4733.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9319 | +0.002 | +4733.00€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 10269 | +0.010 | +2519.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 10269 | +0.010 | +2519.25€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6659 | +0.281 | +7222.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6659 | +0.281 | +7222.42€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8791 | +0.013 | +2221.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8791 | +0.013 | +2221.21€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7642 | +0.039 | +3196.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7642 | +0.039 | +3196.27€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5543 | +0.307 | +6599.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5543 | +0.307 | +6599.60€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 35633 | +0.180 | +29009.68€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 35633 | +0.180 | +29009.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5399 | +0.232 | +4854.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5399 | +0.232 | +4854.60€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5601 | +0.150 | +4157.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5601 | +0.150 | +4157.76€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5722 | +0.222 | +4899.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5722 | +0.222 | +4899.93€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6066 | +0.137 | +4645.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6066 | +0.137 | +4645.50€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6697 | +0.125 | +5028.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6697 | +0.125 | +5028.56€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6148 | +0.227 | +5423.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6148 | +0.227 | +5423.33€ | 0 | 28 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9610 | +0.131 | +4683.05€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9610 | +0.131 | +4683.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 409 | +0.154 | +256.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 409 | +0.154 | +256.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2783 | +0.141 | +1560.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2783 | +0.141 | +1560.66€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 467 | +0.150 | +239.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2885 | +0.136 | +1372.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2885 | +0.136 | +1372.42€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2439 | +0.106 | +972.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2439 | +0.106 | +972.66€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 627 | +0.133 | +281.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 627 | +0.133 | +281.63€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 45144 | +0.186 | +36367.85€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 45144 | +0.186 | +36367.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7137 | +0.244 | +6720.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7137 | +0.244 | +6720.36€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7065 | +0.147 | +4876.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7065 | +0.147 | +4876.81€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7650 | +0.232 | +6821.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7650 | +0.232 | +6821.84€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7459 | +0.139 | +5331.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7459 | +0.139 | +5331.00€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7984 | +0.121 | +5578.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7984 | +0.121 | +5578.51€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7849 | +0.233 | +7039.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7849 | +0.233 | +7039.33€ | 0 | 20 |
| ✅ GBM_LATE_5M | 12120 | +0.203 | +9507.16€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 12120 | +0.203 | +9507.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2801 | +0.207 | +2398.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2801 | +0.207 | +2398.37€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1167 | +0.196 | +861.83€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1167 | +0.196 | +861.83€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3374 | +0.193 | +2369.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3374 | +0.193 | +2369.03€ | 0 | 24 |
| ✅ GBM_LATE_5M#SOL | 1813 | +0.193 | +1399.69€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1813 | +0.193 | +1399.69€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 1928 | +0.208 | +1499.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1928 | +0.208 | +1499.48€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3770 | +0.064 | +1170.04€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3770 | +0.064 | +1170.04€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1383 | +0.080 | +469.73€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1383 | +0.080 | +469.73€ | 0 | 5 |
| ✅ GBM_LATE_60M#ETH | 1222 | +0.067 | +417.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1222 | +0.067 | +417.30€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 1165 | +0.042 | +283.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1165 | +0.042 | +283.01€ | 0 | 13 |
| 🚫 GBM_LATE_60M_FADE | 598 | -0.245 | -21.25€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 598 | -0.245 | -21.25€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 224 | -0.248 | -15.19€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 224 | -0.248 | -15.19€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 212 | -0.229 | +1.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 212 | -0.229 | +1.48€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 162 | -0.256 | -7.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 162 | -0.256 | -7.54€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1640 | +0.084 | +418.21€ | 0 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1640 | +0.084 | +418.21€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 639 | +0.082 | +157.85€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 639 | +0.082 | +157.85€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 569 | +0.055 | +92.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 569 | +0.055 | +92.03€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 432 | +0.124 | +168.33€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 432 | +0.124 | +168.33€ | 3 | 9 |
| ✅ LATE_WINDOW_5MIN | 174 | +0.278 | +172.56€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 174 | +0.278 | +172.56€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 174 | +0.278 | +172.56€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 174 | +0.278 | +172.56€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3571 | +0.102 | +882.27€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3571 | +0.102 | +882.27€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3571 | +0.102 | +882.27€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3571 | +0.102 | +882.27€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 634 | -0.025 | -9.63€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 634 | -0.025 | -9.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 189 | -0.003 | +4.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 189 | -0.003 | +4.17€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 135 | +0.011 | +3.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 135 | +0.011 | +3.04€ | 2 | 2 |
| ✅ LIQUIDACIONES_15M#SOL | 225 | -0.011 | -1.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 225 | -0.011 | -1.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 3840 | +0.014 | +81.06€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3840 | +0.014 | +81.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 185 | +0.029 | -0.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 185 | +0.029 | -0.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 798 | +0.006 | +28.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 798 | +0.006 | +28.40€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 209 | -0.007 | -2.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 209 | -0.007 | -2.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1424 | +0.021 | +26.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1424 | +0.021 | +26.65€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 758 | +0.012 | +2.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 758 | +0.012 | +2.16€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 466 | +0.013 | +26.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 466 | +0.013 | +26.92€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1863 | -0.039 | -28.07€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1863 | -0.039 | -28.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 545 | -0.028 | -10.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 545 | -0.028 | -10.89€ | 6 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 642 | -0.019 | +4.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 642 | -0.019 | +4.38€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 676 | -0.068 | -21.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 676 | -0.068 | -21.56€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 9958 | -0.027 | +7.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4727 | -0.034 | -73.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 5231 | -0.021 | +81.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 310 | -0.035 | -7.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 158 | -0.006 | +5.22€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 152 | -0.065 | -13.06€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2536 | -0.018 | +25.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1197 | -0.022 | +0.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1339 | -0.015 | +25.05€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1072 | -0.029 | +4.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 539 | -0.043 | -16.11€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 533 | -0.014 | +20.58€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2200 | -0.036 | -48.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1024 | -0.047 | -49.67€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1176 | -0.027 | +1.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1933 | -0.019 | +36.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 929 | -0.029 | -2.62€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1004 | -0.009 | +39.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1907 | -0.033 | -2.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 880 | -0.040 | -11.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1027 | -0.028 | +8.40€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 52887 | +0.000 | +2710.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 52887 | +0.000 | +2710.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9555 | +0.026 | +1227.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9555 | +0.026 | +1227.85€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7576 | -0.033 | -101.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7576 | -0.033 | -101.76€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9659 | +0.024 | +1012.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9659 | +0.024 | +1012.98€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7425 | -0.048 | -143.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7425 | -0.048 | -143.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8948 | -0.004 | +265.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8948 | -0.004 | +265.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9724 | +0.016 | +449.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9724 | +0.016 | +449.59€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6742 | -0.057 | -147.27€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6742 | -0.057 | -147.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1232 | -0.002 | -16.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1232 | -0.002 | -16.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1782 | -0.072 | -35.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1782 | -0.072 | -35.52€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 61 | -0.024 | -0.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 61 | -0.024 | -0.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 782 | -0.120 | -33.99€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 782 | -0.120 | -33.99€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2028 | -0.071 | -34.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2028 | -0.071 | -34.84€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 857 | -0.016 | -25.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 857 | -0.016 | -25.51€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 130894 | -0.077 | +1677.86€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 130894 | -0.077 | +1677.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 22820 | -0.076 | +1155.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 22820 | -0.076 | +1155.70€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 19695 | -0.101 | -1048.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 19695 | -0.101 | -1048.57€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 23092 | -0.068 | +1221.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 23092 | -0.068 | +1221.40€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 19239 | -0.098 | -647.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 19239 | -0.098 | -647.97€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 23386 | -0.057 | +342.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 23386 | -0.057 | +342.31€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 22662 | -0.068 | +654.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 22662 | -0.068 | +654.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8814 | -0.035 | -187.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8814 | -0.035 | -187.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1997 | -0.047 | -26.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1997 | -0.047 | -26.59€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2604 | -0.027 | -43.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2604 | -0.027 | -43.23€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1221 | -0.059 | -29.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1221 | -0.059 | -29.86€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 981 | -0.032 | -36.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 981 | -0.032 | -36.84€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1763 | +0.126 | +733.89€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1627 | +0.131 | +721.30€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 379 | +0.138 | +190.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 379 | +0.138 | +190.59€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 334 | +0.122 | +121.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 334 | +0.122 | +121.09€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#ETH | 320 | +0.140 | +160.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 320 | +0.140 | +160.31€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 286 | +0.153 | +159.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 286 | +0.153 | +159.41€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 308 | +0.100 | +89.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 308 | +0.100 | +89.90€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1598 | -0.019 | -28.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1598 | -0.019 | -28.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 307 | -0.005 | +7.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 307 | -0.005 | +7.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 279 | -0.027 | -3.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 279 | -0.027 | -3.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 407 | -0.050 | -37.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 407 | -0.050 | -37.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 344 | +0.003 | +1.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 344 | +0.003 | +1.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 261 | -0.006 | +2.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 261 | -0.006 | +2.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 937 | -0.074 | -50.60€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 436 | -0.112 | -80.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 340 | -0.140 | -67.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 329 | -0.032 | +23.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 238 | -0.021 | +25.94€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 172 | -0.058 | +6.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 141 | -0.066 | +2.00€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 719 | -0.087 | -39.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1175 | -0.206 | -70.86€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 458 | -0.209 | -43.58€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 401 | -0.212 | -43.35€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 400 | -0.206 | -31.19€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 352 | -0.217 | -38.20€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 317 | -0.199 | +3.91€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 296 | -0.195 | +1.79€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1049 | -0.210 | -79.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 126 | -0.172 | +8.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 462 | +0.397 | +440.30€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 69 | +0.162 | +55.45€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 69 | +0.162 | +55.45€ | 0 | 2 |
| ✅ RESOLUTION_SNIPER#ETH | 110 | +0.366 | +102.82€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 110 | +0.366 | +102.82€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 283 | +0.461 | +282.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 283 | +0.461 | +282.03€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 462 | +0.397 | +440.30€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 764 | +0.031 | +49.15€ | 2 | 3 |
| ✅ STREAK_FADE_15M#15min | 764 | +0.031 | +49.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 307 | +0.021 | +2.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 307 | +0.021 | +2.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 63 | -0.008 | -1.05€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 63 | -0.008 | -1.05€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 77 | -0.006 | +1.97€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 77 | -0.006 | +1.97€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 317 | +0.058 | +45.37€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 317 | +0.058 | +45.37€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3450 | -0.022 | -135.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3450 | -0.022 | -135.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1060 | -0.021 | -35.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1060 | -0.021 | -35.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 594 | -0.029 | -27.06€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 594 | -0.029 | -27.06€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 167 | -0.038 | -13.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 167 | -0.038 | -13.79€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1629 | -0.019 | -58.95€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1629 | -0.019 | -58.95€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 103 | -0.052 | -9.27€ | 6 | 0 |
| ✅ STREAK_FADE_60M#60min | 103 | -0.052 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 60 | -0.016 | -4.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 60 | -0.016 | -4.20€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11167 | +0.015 | +82.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11167 | +0.015 | +82.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2838 | +0.020 | +29.50€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2838 | +0.020 | +29.50€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2911 | +0.017 | +32.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2911 | +0.017 | +32.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2901 | +0.008 | -3.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2901 | +0.008 | -3.48€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2517 | +0.016 | +23.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2517 | +0.016 | +23.83€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10149 | +0.013 | -47.88€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10149 | +0.013 | -47.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4171 | +0.018 | -5.87€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4171 | +0.018 | -5.87€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3621 | +0.010 | -28.64€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3621 | +0.010 | -28.64€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2357 | +0.009 | -13.38€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2357 | +0.009 | -13.38€ | 1 | 0 |
| ✅ UPDOWN_GBM | 81081 | +0.055 | +7232.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 20028 | +0.083 | +4354.33€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2580 | +0.004 | +26.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 53372 | +0.051 | +2759.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4814 | +0.006 | +94.54€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 17943 | +0.056 | +1542.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2655 | +0.089 | +636.81€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 705 | +0.008 | +11.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 12325 | +0.062 | +825.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2154 | +0.004 | +64.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 104 | -0.066 | +3.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8708 | +0.070 | +924.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7075 | +0.054 | +315.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 18948 | +0.046 | +1252.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4806 | +0.069 | +714.55€ | 0 | 10 |
| ✅ UPDOWN_GBM#ETH#240min | 683 | +0.007 | +16.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 11655 | +0.045 | +499.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1708 | +0.009 | +19.87€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 96 | -0.102 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 17832 | +0.034 | +922.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5116 | +0.035 | +413.65€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 649 | -0.008 | +1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11030 | +0.040 | +502.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 952 | +0.006 | +10.02€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 85 | -0.132 | -6.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10797 | +0.066 | +1517.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4320 | +0.104 | +1280.29€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6089 | +0.043 | +236.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 285 | -0.099 | -0.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 875 | +0.365 | +321.86€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 875 | +0.365 | +321.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 447 | +0.362 | +153.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 447 | +0.362 | +153.72€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 428 | +0.367 | +168.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 428 | +0.367 | +168.13€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 20663 | -0.024 | +4885.45€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 20663 | -0.024 | +4885.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3735 | -0.111 | +155.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3735 | -0.111 | +155.47€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2598 | +0.220 | +1702.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2598 | +0.220 | +1702.13€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5923 | -0.065 | +741.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5923 | -0.065 | +741.69€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5741 | -0.065 | +1012.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5741 | -0.065 | +1012.89€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 245 | +0.055 | +17.28€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 245 | +0.055 | +17.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 245 | +0.055 | +17.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 245 | +0.055 | +17.28€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1514 | +0.290 | +1291.17€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1514 | +0.290 | +1291.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 809 | +0.285 | +648.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 809 | +0.285 | +648.48€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 705 | +0.295 | +642.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 705 | +0.295 | +642.69€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 828 | -0.112 | -82.31€ | 6 | 0 |
| ✅ UPDOWN_OU_5M#5min | 828 | -0.112 | -82.31€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 254 | -0.082 | -19.18€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 254 | -0.082 | -19.18€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 89 | -0.170 | -10.17€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 89 | -0.170 | -10.17€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 102 | -0.173 | -3.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 102 | -0.173 | -3.61€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3773 | +0.304 | +1780.85€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1392 | +0.258 | +173.63€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1451 | +0.299 | +650.45€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 930 | +0.380 | +956.77€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.025 n=1018 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1018 IC=+0.025 PNL=+46.53€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 728 celda(s) pasan gate riguroso completo de 2737 evaluadas (n>=40) y 3799 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.035 < 0.08 — monitorear
  - _Datos_: n=5116 IC=+0.035 PNL=+413.65€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1451/15 IC=+0.299 PNL=+650.45€ | BTC: n=1392/15 IC=+0.258 PNL=+173.63€ | SOL: n=930/15 IC=+0.380 PNL=+956.77€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.142 n=826/60 | contraria IC=+0.192 n=859 | gap=-0.050 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=488, boost estimado=+0.016. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1707/40 IC=+0.009 PNL=+20.38€ | BTC#60min: n=2153/40 IC=+0.004 PNL=+65.16€ | SOL#60min: n=952/40 IC=+0.006 PNL=+10.02€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.047 n=586283 | tras_1loss IC=+0.096 n=445154 | tras_2loss IC=+0.066 n=179767/40 | gap=-0.018 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.193 > 0.08 con n=796 PNL=+583.53€
  - _Datos_: n=796 IC=+0.193 PNL=+583.53€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.08 con n=901 PNL=+497.77€
  - _Datos_: n=901 IC=+0.165 PNL=+497.77€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.08 con n=66 PNL=+33.08€
  - _Datos_: n=66 IC=+0.162 PNL=+33.08€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=3080 PNL=+1709.94€
  - _Datos_: n=3080 IC=+0.334 PNL=+1709.94€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=746 IC=+0.070 PNL=+80.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=746 IC=+0.070 PNL=+80.82€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=89 IC=+0.181 PNL=+58.85€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=89 IC=+0.181 PNL=+58.85€

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
  - _Estado_: n=3233 IC=+0.009 PNL=+13.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3233 IC=+0.009 PNL=+13.44€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1579 IC=+0.001 PNL=+82.12€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1579 IC=+0.001 PNL=+82.12€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1018 IC=+0.025 PNL=+46.53€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1018 IC=+0.025 PNL=+46.53€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.172 > 0.1 con n=5109 PNL=+3086.06€
  - _Datos_: n=5109 IC=+0.172 PNL=+3086.06€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2655 IC=+0.089 PNL=+636.81€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2655 IC=+0.089 PNL=+636.81€

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
  - _Estado_: n=1033 IC=+0.037 PNL=+87.58€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1033 IC=+0.037 PNL=+87.58€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=130 IC=+0.008 PNL=+0.90€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=130 IC=+0.008 PNL=+0.90€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.278 n=174) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=174 IC=+0.278 PNL=+172.56€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=1018 PNL=+427.17€
  - _Datos_: n=1018 IC=+0.124 PNL=+427.17€

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
  - _Estado_: n=32022 IC=+0.074 PNL=+4607.10€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=32022 IC=+0.074 PNL=+4607.10€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.139 < -0.1 con n=532 PNL=+69.03€
  - _Datos_: n=532 IC=-0.139 PNL=+69.03€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3169 IC=+0.070 PNL=+417.35€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3169 IC=+0.070 PNL=+417.35€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=152 IC=-0.097 PNL=+3.71€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=152 IC=-0.097 PNL=+3.71€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.1 con n=856 PNL=+232.22€
  - _Datos_: n=856 IC=+0.112 PNL=+232.22€

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
  - _Estado_: n=34327 IC=-0.134 PNL=+2729.40€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=34327 IC=-0.134 PNL=+2729.40€

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
  - _Estado_: n=3452 IC=+0.134 PNL=+2162.96€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3452 IC=+0.134 PNL=+2162.96€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=8331 IC=+0.053 PNL=+670.17€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8331 IC=+0.053 PNL=+670.17€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.095 > 0.08 con n=3671 PNL=+2027.24€
  - _Datos_: n=3671 IC=+0.095 PNL=+2027.24€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.224 < -0.1 con n=3573 PNL=-311.71€
  - _Datos_: n=3573 IC=-0.224 PNL=-311.71€

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
  - _Estado_: n=74 IC=+0.026 PNL=+9.96€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=74 IC=+0.026 PNL=+9.96€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.103 n=1810) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1810 IC=+0.103 PNL=+398.81€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.410 n=588) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=588 IC=+0.410 PNL=+841.00€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=14800 IC=+0.186 PNL=-1512.79€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=14800 IC=+0.186 PNL=-1512.79€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.221 > 0.1 con n=238 PNL=+157.70€
  - _Datos_: n=238 IC=+0.221 PNL=+157.70€
