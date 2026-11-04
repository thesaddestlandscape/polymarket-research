# Hipótesis automáticas — 2026-11-04 18:40 UTC
_Generado por shadow_postmortem.py sobre 1193389 resoluciones (PNL=+162373.13€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=685)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.201 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.132)

- **PATRÓN** `n_total_lado` > `63.0` → IC=+0.183 (n=314)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 63.0 (IC base=+0.132)

- **PATRÓN** `banda_hit_calibrado` > `0.6154` → IC=+0.248 (n=622)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6154 (IC base=+0.132)

- **PATRÓN** `banda_z` > `8.701` → IC=+0.206 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.701 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.132 (n=672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.132)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.147 (n=1015)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `3349.2237` → IC=+0.133 (n=622)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3349.2237 (IC base=+0.132)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.505` → IC=+0.199 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.505 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.186 (n=272)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 66.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.8135` → IC=+0.271 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8135 (IC base=+0.136)

- **PATRÓN** `banda_z` > `9.021` → IC=+0.208 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.021 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=292)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=915)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.136)

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
- **FILTRO** `restante_s_al_confirmar` < `134.8` → IC=-0.217 (n=11330)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 134.8
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=33992)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.27` → IC=-0.254 (n=1177)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.27
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=3531)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `116.98` → IC=-0.310 (n=1169)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.98
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3510)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `118.43` → IC=-0.159 (n=3095)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 118.43
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=9288)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `156.49` → IC=-0.239 (n=3061)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 156.49
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9184)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `131.44` → IC=-0.255 (n=2157)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.44
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=6473)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.211 (n=25884)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `8516.7687` → IC=+0.160 (n=2248)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 8516.7687 (IC base=+0.105)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=22132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=26980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=20419)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=7991)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6740.9632` → IC=+0.149 (n=3085)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 6740.9632 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=2075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2663)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `9415.8912` → IC=+0.181 (n=1853)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 9415.8912 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.187 (n=1892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.183 (n=2118)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2712)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `16106.2132` → IC=+0.185 (n=700)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16106.2132 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=2077)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.173 (n=563)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.142 (n=1321)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.44 (IC base=+0.081)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=4985)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.168 (n=4219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 15.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.376 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.214 (n=2240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` < `0.27` → IC=+0.345 (n=811)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.27 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=2603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=1269)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.150 (n=1082)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.259 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.144 (n=1405)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.02 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.160 (n=154)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.070)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.257 (n=923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.148 (n=1383)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=714)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.286 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `947.2335` → IC=-0.128 (n=154)

  - _Acción_: SKIP cuando `libro_liquidez` < 947.2335
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=313)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.160 (n=454)

  - _Acción_: Kelly boost +0.80€ cuando `py_entrada` > 0.55 (IC base=+0.049)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=1175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.121)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.121)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `10.0` → IC=-0.297 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=22248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=18836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.228 (n=9254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.198)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=5071)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.176 (n=5053)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 18.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4829)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.175 (n=4241)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.214 (n=2903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.216 (n=1936)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.290 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.211)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=4984)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.180 (n=4233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.178 (n=5154)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=3885)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=4244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.250 (n=3603)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.249)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.356 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.79 (IC base=+0.249)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=4898)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=4164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.191 (n=3640)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.187)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.429 (n=919)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=972)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4440.8454` → IC=+0.444 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4440.8454 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.444 (n=376)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.459 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_liquidez` > `12430.0394` → IC=+0.448 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12430.0394 (IC base=+0.440)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.431 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4649.4982` → IC=+0.443 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4649.4982 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.399 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.396)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.403 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.396)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.412 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.396)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=29003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.243 (n=29299)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.183 (n=11570)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.182 (n=9261)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 12.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=13219)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=12173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=4156)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=12197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.199 (n=10267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.289 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=7)

- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=6104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.223 (n=4643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.270 (n=4094)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `3176.5987` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3176.5987
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=11083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.258 (n=4272)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=4827)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=4813)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.244 (n=5056)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=10394)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=10750)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.54` → IC=+0.137 (n=12687)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.54 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5072)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=4860)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=6365)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.63` → IC=+0.144 (n=4786)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.63 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=5322)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=5890)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `2.23` → IC=+0.138 (n=4832)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.23 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.308 (n=1304)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=877)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.368 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.302 (n=927)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.393 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.299)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.300 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.299)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.443 (n=891)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=859)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.436 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.441 (n=286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.435 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.443 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.465 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.448)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.450 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.448)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.448)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.449 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.448)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4743` → IC=+0.138 (n=16378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4743 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=16572)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=11410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3735` → IC=+0.165 (n=16378)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.3735 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7962` → IC=+0.281 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7962 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.551` → IC=+0.184 (n=8185)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 3.551 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6962` → IC=+0.265 (n=4337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6962 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.304` → IC=+0.246 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.304 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.739` → IC=+0.232 (n=3914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.739 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=8230)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4701.9625` → IC=+0.145 (n=5460)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4701.9625 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.122 (n=10194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.006 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.6796` → IC=+0.132 (n=23128)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.6796 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.6109` → IC=+0.190 (n=1409)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6109 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.162` → IC=+0.189 (n=7876)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.162 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `0.8624` → IC=+0.192 (n=5473)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8624 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.228 (n=2025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `1.4565` → IC=+0.205 (n=13954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4565 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.227 (n=13858)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.080)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3653` → IC=+0.210 (n=3509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3653 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.223 (n=1701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.985` → IC=+0.280 (n=1591)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.985 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.566` → IC=+0.280 (n=1561)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.566 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.262 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.212 (n=3361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.223 (n=3841)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2064.2` → IC=+0.212 (n=1170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2064.2 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.223 (n=3170)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 28.0 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.243 (n=3054)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.0896` → IC=+0.274 (n=1018)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0896 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.252 (n=1125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.4695` → IC=+0.260 (n=2687)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4695 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0944` → IC=+0.246 (n=2758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0944 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.253 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.4444` → IC=+0.247 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4444 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.8593` → IC=+0.244 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8593 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=3498)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1522.82` → IC=+0.246 (n=2728)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1522.82 (IC base=+0.241)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.230 (n=1956)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.0813` → IC=+0.261 (n=977)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0813 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=3059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=2079)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9138` → IC=+0.263 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9138 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1875` → IC=+0.232 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1875 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.5298` → IC=+0.227 (n=3173)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5298 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.02` → IC=+0.260 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.02 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.2269` → IC=+0.224 (n=2923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2269 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.227 (n=2923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.270 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4271` → IC=+0.252 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4271 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.150 (n=3088)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0062 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0777` → IC=+0.152 (n=1031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.0777 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.143 (n=2192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.7115` → IC=+0.167 (n=3089)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.7115 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1377` → IC=+0.144 (n=2941)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1377 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.729` → IC=+0.132 (n=498)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 10.729 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.01` → IC=+0.134 (n=2830)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 4.01 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.135 (n=3088)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 1.2032 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.150 (n=1129)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.1371` → IC=+0.136 (n=2608)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 2.1371 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=4005)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.166 (n=1274)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 204.0 (IC base=+0.128)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.214 (n=1682)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=3894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.267 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.095` → IC=+0.276 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.095 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0976` → IC=+0.197 (n=3312)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0976 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3536` → IC=+0.218 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3536 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7283` → IC=+0.210 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7283 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=4460)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1389.4706` → IC=+0.197 (n=3703)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 1389.4706 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.224 (n=2973)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.235 (n=1487)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.222 (n=1537)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` < `0.0404` → IC=+0.271 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0404 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.038` → IC=+0.263 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.038 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.3492` → IC=+0.257 (n=487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3492 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `1.7603` → IC=+0.218 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7603 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.226 (n=2160)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1698)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `1919.8432` → IC=+0.223 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1919.8432 (IC base=+0.219)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.223 (n=3202)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.219)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.161 (n=187)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=4460)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.161 (n=633)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0038 (IC base=+0.058)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.234 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.1397` → IC=+0.337 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1397 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` < `0.5346` → IC=+0.333 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5346 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.077` → IC=+0.202 (n=1382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.077 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` > `1.2478` → IC=+0.356 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2478 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` < `0.0777` → IC=+0.334 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0777 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.334 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.340 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.2749` → IC=+0.339 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2749 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.337 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 143.0 (IC base=+0.058)

- **PATRÓN** `ibs_20min` < `0.092` → IC=+0.182 (n=1162)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.092 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.7332` → IC=+0.162 (n=291)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.7332 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` < `0.1391` → IC=+0.145 (n=2023)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1391 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8356` → IC=+0.158 (n=1453)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8356 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.204 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.7746` → IC=+0.149 (n=1398)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.7746 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` > `2.153` → IC=+0.158 (n=951)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.153 (IC base=+0.046)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.187 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=698)

- **FILTRO** `ibs_20min` < `0.2647` → IC=-0.173 (n=206)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2647
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=624)

- **FILTRO** `ibs_20min` > `0.2051` → IC=-0.131 (n=4379)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2051
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=2158)

- **FILTRO** `sigma_ewma_delta_pct` > `8.405` → IC=-0.226 (n=706)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.405
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=5831)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.179 (n=285)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.017)

- **PATRÓN** `dist_vwap_pct` > `0.9658` → IC=+0.267 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9658 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.045` → IC=+0.158 (n=194)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 5.045 (IC base=+0.017)

- **PATRÓN** `volumen_regimen` > `1.0267` → IC=+0.293 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0267 (IC base=+0.017)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.282 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` < `2.4693` → IC=+0.280 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4693 (IC base=+0.017)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.264 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.017)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.267 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.017)

- **PATRÓN** `ibs_20min` < `0.2051` → IC=+0.154 (n=2158)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.2051 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` > `0.217` → IC=+0.285 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.217 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` < `0.4923` → IC=+0.281 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4923 (IC base=-0.037)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.309 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.695 (IC base=-0.037)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.295 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=-0.037)

- **PATRÓN** `volumen_spike_ratio` < `2.1446` → IC=+0.305 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1446 (IC base=-0.037)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7786` → IC=-0.154 (n=3277)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7786
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=1689)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.167 (n=1126)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=3840)

- **FILTRO** `ibs_20min` > `0.746` → IC=-0.199 (n=1740)

  - _Acción_: SKIP cuando `ibs_20min` > 0.746
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=5221)

- **PATRÓN** `ibs_20min` > `0.7786` → IC=+0.121 (n=1689)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` > 0.7786 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` > `1.0308` → IC=+0.356 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0308 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` < `0.2486` → IC=+0.305 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2486 (IC base=-0.060)

- **PATRÓN** `volumen_regimen` > `0.7048` → IC=+0.317 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7048 (IC base=-0.060)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.304 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=-0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.0772` → IC=+0.305 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0772 (IC base=-0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.5757` → IC=+0.307 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5757 (IC base=-0.060)

- **PATRÓN** `volumen_spike_ratio` > `2.5237` → IC=+0.318 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5237 (IC base=-0.060)

- **PATRÓN** `dist_vwap_pct` > `0.7922` → IC=+0.278 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7922 (IC base=-0.000)

- **PATRÓN** `dist_vwap_pct` < `0.2214` → IC=+0.265 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2214 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` < `0.722` → IC=+0.273 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.722 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` > `1.0635` → IC=+0.286 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0635 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.1703` → IC=+0.286 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1703 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `2.1777` → IC=+0.268 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1777 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.272 (n=1870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4406 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.199 (n=7087)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.090)

- **PATRÓN** `ibs_20min` > `0.873` → IC=+0.288 (n=9626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.873 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.6789` → IC=+0.299 (n=2050)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6789 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.529` → IC=+0.168 (n=9499)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.529 (IC base=+0.090)

- **PATRÓN** `volumen_regimen` > `0.6924` → IC=+0.275 (n=6969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6924 (IC base=+0.090)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.289 (n=2342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.090)

- **PATRÓN** `volumen_spike_ratio` > `2.6516` → IC=+0.283 (n=4121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6516 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.307 (n=11968)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.090)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.157 (n=6819)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.01 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.6443` → IC=+0.151 (n=20457)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.6443 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.2553` → IC=+0.276 (n=6762)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2553 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` < `0.7016` → IC=+0.280 (n=2933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7016 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `1.1928` → IC=+0.275 (n=2221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1928 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.324 (n=1460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `1.5759` → IC=+0.300 (n=4302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5759 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `2.2809` → IC=+0.297 (n=4432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2809 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `73.0` → IC=+0.307 (n=9716)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 73.0 (IC base=+0.080)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8011` → IC=-0.121 (n=3807)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8011
  - _Potencial_: sin este filtro IC_bueno=+0.294 (n=1964)

- **FILTRO** `ibs_20min` > `0.7217` → IC=-0.230 (n=1261)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7217
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=3789)

- **FILTRO** `sigma_ewma_delta_pct` > `4.181` → IC=-0.228 (n=1090)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.181
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=3960)

- **PATRÓN** `ibs_20min` > `0.934` → IC=+0.336 (n=1443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.934 (IC base=+0.020)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.059` → IC=+0.190 (n=1931)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.059 (IC base=+0.020)

- **PATRÓN** `volumen_pendiente_norm` > `0.2278` → IC=+0.326 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2278 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4467` → IC=+0.279 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4467 (IC base=+0.020)

- **PATRÓN** `volumen_spike_ratio` > `2.2386` → IC=+0.297 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2386 (IC base=+0.020)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.314 (n=1257)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.020)

- **PATRÓN** `ibs_20min` < `0.1723` → IC=+0.160 (n=1263)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1723 (IC base=-0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1514` → IC=+0.405 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1514 (IC base=-0.026)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.428 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=-0.026)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.402 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=-0.026)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1233` → IC=+0.221 (n=1039)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1233 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.207 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1954 (IC base=+0.013)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.209 (n=1849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2783` → IC=+0.246 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2783 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.4174` → IC=+0.231 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4174 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `266.0` → IC=+0.240 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 266.0 (IC base=+0.013)

- **PATRÓN** `dist_vwap_pct` < `0.1295` → IC=+0.250 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1295 (IC base=-0.004)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.245 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=-0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.309 (n=181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.5317` → IC=+0.249 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5317 (IC base=-0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.1544` → IC=+0.259 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1544 (IC base=-0.004)

- **PATRÓN** `ballena_activa_n` < `213.0` → IC=+0.258 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 213.0 (IC base=-0.004)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.324 (n=1365)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.290 (n=3010)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.281)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.323 (n=1633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.632` → IC=+0.301 (n=1994)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.632 (IC base=+0.281)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.293 (n=2634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.281)

- **PATRÓN** `volumen_spike_ratio` > `1.6075` → IC=+0.287 (n=2917)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6075 (IC base=+0.281)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.290 (n=3591)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `2038.5634` → IC=+0.295 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2038.5634 (IC base=+0.281)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.305 (n=1873)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.281)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.321 (n=2403)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.1781` → IC=+0.321 (n=1186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1781 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.328 (n=1026)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.304 (n=1217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` < `0.0124` → IC=+0.303 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0124 (IC base=+0.302)

- **PATRÓN** `ibs_20min` > `0.1385` → IC=+0.312 (n=1793)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1385 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.32` → IC=+0.313 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.32 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` < `0.1982` → IC=+0.303 (n=2644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1982 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.3446` → IC=+0.309 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3446 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `1.7435` → IC=+0.302 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7435 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `2.7263` → IC=+0.315 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7263 (IC base=+0.302)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.305 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.302)

- **PATRÓN** `libro_liquidez` > `1922.16` → IC=+0.313 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1922.16 (IC base=+0.302)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.309 (n=2251)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.302)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7286` → IC=-0.181 (n=1321)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7286
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=3967)

- **PATRÓN** `ibs_20min` > `0.8542` → IC=+0.166 (n=1293)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.8542 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1479` → IC=+0.230 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1479 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.3631` → IC=+0.234 (n=1805)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3631 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1635` → IC=+0.232 (n=1859)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1635 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6704` → IC=+0.232 (n=1661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6704 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.234 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.237 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `2.4586` → IC=+0.235 (n=1801)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4586 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.254 (n=1841)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 117.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.35` → IC=+0.245 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.35 (IC base=+0.004)

- **PATRÓN** `volumen_regimen` < `1.0163` → IC=+0.252 (n=1162)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0163 (IC base=+0.004)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.308 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` < `1.7888` → IC=+0.281 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7888 (IC base=+0.004)

- **PATRÓN** `volumen_spike_ratio` > `2.4323` → IC=+0.266 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4323 (IC base=+0.004)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.277 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.004)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7455` → IC=-0.242 (n=2199)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7455
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2199)

- **FILTRO** `ibs_20min` > `0.6279` → IC=-0.232 (n=1055)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6279
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=3166)

- **FILTRO** `sigma_ewma_delta_pct` > `8.314` → IC=-0.253 (n=483)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.314
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=3738)

- **PATRÓN** `ibs_20min` > `0.7455` → IC=+0.313 (n=2199)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7455 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.2166` → IC=+0.348 (n=930)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2166 (IC base=+0.035)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.482` → IC=+0.153 (n=1773)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 2.482 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.341 (n=1074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `0.6974` → IC=+0.335 (n=1438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6974 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` < `0.1582` → IC=+0.335 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1582 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.361 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.4333` → IC=+0.363 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4333 (IC base=+0.035)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.355 (n=1405)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.035)

- **PATRÓN** `ibs_20min` < `0.6279` → IC=+0.146 (n=3166)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.6279 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` < `0.3034` → IC=+0.262 (n=1566)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3034 (IC base=+0.051)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.037` → IC=+0.125 (n=2975)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 3.037 (IC base=+0.051)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.286 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.0706` → IC=+0.277 (n=604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0706 (IC base=+0.051)

- **PATRÓN** `volumen_spike_ratio` < `1.8068` → IC=+0.276 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8068 (IC base=+0.051)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.282 (n=1526)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 48.0 (IC base=+0.051)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.356 (n=2021)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.313)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.315 (n=2285)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.313)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.317 (n=1070)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.313)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.343 (n=2264)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.313)

- **PATRÓN** `dist_vwap_pct` > `0.2066` → IC=+0.338 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2066 (IC base=+0.313)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.814` → IC=+0.331 (n=1094)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.814 (IC base=+0.313)

- **PATRÓN** `volumen_regimen` > `0.8705` → IC=+0.331 (n=1508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8705 (IC base=+0.313)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.345 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.313)

- **PATRÓN** `volumen_spike_ratio` > `1.43` → IC=+0.325 (n=2175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.43 (IC base=+0.313)

- **PATRÓN** `libro_liquidez` > `2968.5542` → IC=+0.318 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2968.5542 (IC base=+0.313)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.343 (n=2002)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.313)

- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.347 (n=1595)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0153 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.323 (n=1211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=1165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.335 (n=2392)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.381 (IC base=+0.315)

- **PATRÓN** `dist_vwap_pct` < `0.2383` → IC=+0.320 (n=2298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2383 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.619` → IC=+0.329 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.619 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` < `0.719` → IC=+0.321 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.719 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `1.2103` → IC=+0.344 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2103 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.366 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` < `1.4118` → IC=+0.324 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4118 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `2.1376` → IC=+0.319 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1376 (IC base=+0.315)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.227 (n=5297)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.0878` → IC=+0.195 (n=5294)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.0878 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=16492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` > `0.5407` → IC=+0.233 (n=15880)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5407 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1637` → IC=+0.206 (n=6213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1637 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.911` → IC=+0.259 (n=3110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.911 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.1863` → IC=+0.156 (n=10574)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.1863 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` > `0.6261` → IC=+0.155 (n=10575)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 0.6261 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.2944` → IC=+0.209 (n=2304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2944 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.6094` → IC=+0.191 (n=5146)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6094 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.196 (n=14788)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 89.0 (IC base=+0.176)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.191 (n=6800)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0057 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.221 (n=5141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=5802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5216` → IC=+0.239 (n=15421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5216 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` < `0.1807` → IC=+0.177 (n=11086)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1807 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.688` → IC=+0.194 (n=2458)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 9.688 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.572` → IC=+0.187 (n=13724)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 2.572 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1813` → IC=+0.165 (n=10990)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1813 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.216 (n=2306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6351` → IC=+0.189 (n=4876)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6351 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `94.0` → IC=+0.197 (n=14407)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 94.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1052` → IC=+0.257 (n=1152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1052 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.229 (n=1771)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.8091` → IC=+0.276 (n=2338)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8091 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.627` → IC=+0.329 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.627 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.293 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.8308` → IC=+0.225 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8308 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4334` → IC=+0.227 (n=2492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4334 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2888)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.258 (n=2096)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.255)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.306 (n=924)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.261 (n=2166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.257 (n=1913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` < `0.4264` → IC=+0.272 (n=2097)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4264 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.259 (n=1837)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.301` → IC=+0.276 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.301 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.4451` → IC=+0.279 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4451 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.7129` → IC=+0.258 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7129 (IC base=+0.255)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.258 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.255)

- **PATRÓN** `libro_liquidez` > `1511.5998` → IC=+0.264 (n=1872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1511.5998 (IC base=+0.255)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.255 (n=1776)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.255)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.199 (n=811)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.003 (IC base=+0.134)

- **PATRÓN** `drift_60min` |x|≤ `0.16` → IC=+0.163 (n=1617)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.16 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.149 (n=2542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `ibs_20min` > `0.2681` → IC=+0.209 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2681 (IC base=+0.134)

- **PATRÓN** `dist_vwap_pct` > `0.1861` → IC=+0.213 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1861 (IC base=+0.134)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.772` → IC=+0.208 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.772 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` < `0.6958` → IC=+0.144 (n=1067)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6958 (IC base=+0.134)

- **PATRÓN** `volumen_regimen` > `1.0621` → IC=+0.139 (n=1100)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0621 (IC base=+0.134)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.181 (n=377)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` < `1.5013` → IC=+0.144 (n=1048)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.5013 (IC base=+0.134)

- **PATRÓN** `volumen_spike_ratio` > `2.4689` → IC=+0.147 (n=794)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4689 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `403.0` → IC=+0.139 (n=2349)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 403.0 (IC base=+0.134)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.171 (n=2551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0063 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.237` → IC=+0.168 (n=2241)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.237 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=1218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6102` → IC=+0.206 (n=2547)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6102 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1459` → IC=+0.172 (n=2641)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1459 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.076` → IC=+0.180 (n=479)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 11.076 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.061` → IC=+0.147 (n=2230)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.061 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.159 (n=2547)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2024 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.094` → IC=+0.149 (n=2206)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.094 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.128` → IC=+0.151 (n=2132)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.128 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `214.0` → IC=+0.184 (n=1044)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 214.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.236 (n=1220)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.3959` → IC=+0.225 (n=2367)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3959 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=978)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.298 (n=1416)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.184` → IC=+0.304 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.184 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.3554` → IC=+0.237 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3554 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7274` → IC=+0.227 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7274 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.217 (n=3237)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1926.5448` → IC=+0.221 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.5448 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.246 (n=2059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.4174` → IC=+0.262 (n=2056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4174 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.282 (n=893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0312` → IC=+0.291 (n=1028)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0312 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.203` → IC=+0.282 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.203 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3584` → IC=+0.285 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3584 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.7646` → IC=+0.241 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7646 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.1786` → IC=+0.247 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1786 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1916.01` → IC=+0.247 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1916.01 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.244 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.239)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.199 (n=1149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0042 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.192 (n=868)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.2661` → IC=+0.198 (n=2603)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.2661 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1413` → IC=+0.187 (n=1552)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1413 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.411` → IC=+0.202 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.411 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.8476` → IC=+0.142 (n=1737)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8476 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` > `1.1857` → IC=+0.140 (n=868)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` > 1.1857 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.181 (n=387)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.8246` → IC=+0.136 (n=1700)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.8246 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `2.5248` → IC=+0.159 (n=850)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5248 (IC base=+0.137)

- **PATRÓN** `libro_liquidez` > `6919.7421` → IC=+0.198 (n=1180)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6919.7421 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `130.0` → IC=+0.143 (n=2539)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 130.0 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.167 (n=2415)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0066 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.3952` → IC=+0.145 (n=2745)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3952 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.164 (n=1313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.6735` → IC=+0.187 (n=2745)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6735 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.156 (n=2742)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.35` → IC=+0.147 (n=663)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 9.35 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.156 (n=1831)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.8521 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2952` → IC=+0.175 (n=411)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2952 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.8013` → IC=+0.132 (n=1731)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8013 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4192` → IC=+0.128 (n=2595)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4192 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `6251.2816` → IC=+0.188 (n=1245)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 6251.2816 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.135 (n=2251)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 108.0 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.172 (n=966)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0125 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.137 (n=2969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4737` → IC=+0.210 (n=2899)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4737 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.2007` → IC=+0.189 (n=1598)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2007 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.146` → IC=+0.292 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.146 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1755` → IC=+0.133 (n=2899)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1755 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.7046` → IC=+0.123 (n=2589)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7046 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1633` → IC=+0.129 (n=2953)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1633 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.137 (n=938)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.124 (n=3023)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2664.3504` → IC=+0.200 (n=1314)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2664.3504 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.143 (n=1256)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 21.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0118` → IC=+0.143 (n=3014)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0118 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1117` → IC=+0.163 (n=1004)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1117 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3081)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.219 (n=3012)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.211` → IC=+0.145 (n=2922)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.211 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.312` → IC=+0.138 (n=2657)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.312 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1765` → IC=+0.129 (n=3012)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1765 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2745` → IC=+0.132 (n=414)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2745 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.5362` → IC=+0.128 (n=1249)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.5362 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4306` → IC=+0.127 (n=946)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 2.4306 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2536.2702` → IC=+0.186 (n=1366)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2536.2702 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.124 (n=2834)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 46.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0131` → IC=+0.250 (n=2367)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0131 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1656` → IC=+0.241 (n=1166)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1656 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=2753)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.230 (n=2389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6656` → IC=+0.259 (n=2649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6656 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1805` → IC=+0.234 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1805 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8265` → IC=+0.227 (n=2717)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8265 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.523` → IC=+0.262 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.523 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6251` → IC=+0.233 (n=2649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6251 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2352` → IC=+0.272 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2352 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.8148` → IC=+0.235 (n=1721)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8148 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2111.062` → IC=+0.229 (n=2649)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2111.062 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.239 (n=1184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0227` → IC=+0.251 (n=1221)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0227 (IC base=+0.238)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.264 (n=896)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.255 (n=1315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.245 (n=1202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` < `0.44` → IC=+0.264 (n=2698)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.44 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.3041` → IC=+0.247 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3041 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.204` → IC=+0.269 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.204 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `0.8647` → IC=+0.242 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8647 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6409` → IC=+0.242 (n=2688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6409 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.288 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` < `2.5331` → IC=+0.235 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5331 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `1.4358` → IC=+0.241 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4358 (IC base=+0.238)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.207 (n=1352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.165)

- **PATRÓN** `drift_60min` |x|≤ `0.1319` → IC=+0.182 (n=1782)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.1319 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.176 (n=4257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 5.0 (IC base=+0.165)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.210 (n=3621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4444 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.8171` → IC=+0.191 (n=654)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.8171 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.556` → IC=+0.196 (n=1714)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.556 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` < `0.8638` → IC=+0.181 (n=2454)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.8638 (IC base=+0.165)

- **PATRÓN** `volumen_regimen` > `1.1944` → IC=+0.174 (n=1227)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` > 1.1944 (IC base=+0.165)

- **PATRÓN** `volumen_pendiente_norm` > `0.0739` → IC=+0.173 (n=1632)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.0739 (IC base=+0.165)

- **PATRÓN** `volumen_spike_ratio` < `1.5353` → IC=+0.171 (n=1736)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.5353 (IC base=+0.165)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.168 (n=4542)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.165)

- **PATRÓN** `libro_liquidez` > `2636.5291` → IC=+0.177 (n=3618)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2636.5291 (IC base=+0.165)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.193 (n=1919)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.2 (IC base=+0.089)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.129 (n=1847)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 26.0 (IC base=+0.089)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.195 (n=1101)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.006 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.101` → IC=+0.231 (n=484)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.101 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.211 (n=995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.2144` → IC=+0.210 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2144 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.3087` → IC=+0.210 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3087 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.4949` → IC=+0.177 (n=1247)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.4949 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.957` → IC=+0.201 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.957 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.399` → IC=+0.178 (n=1158)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 6.399 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `0.8803` → IC=+0.192 (n=734)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.8803 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` < `0.15` → IC=+0.180 (n=1158)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.15 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.186 (n=435)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `2.1906` → IC=+0.191 (n=950)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 2.1906 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `15859.8442` → IC=+0.193 (n=499)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 15859.8442 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.169 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0031 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.1954` → IC=+0.197 (n=588)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1954 (IC base=+0.098)

- **PATRÓN** `volumen_pendiente_norm` > `0.1608` → IC=+0.141 (n=349)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.1608 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `160.0` → IC=+0.175 (n=576)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 160.0 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.243 (n=555)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.2096` → IC=+0.189 (n=837)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.2096 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=1313)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.8185` → IC=+0.272 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8185 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.817` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.817 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.2103` → IC=+0.183 (n=1117)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.2103 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.898` → IC=+0.215 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.898 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8344` → IC=+0.196 (n=837)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` < 0.8344 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `1.1591` → IC=+0.184 (n=419)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.1591 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.208 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.5274` → IC=+0.186 (n=545)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 1.5274 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `1.7866` → IC=+0.194 (n=825)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 1.7866 (IC base=+0.181)

- **PATRÓN** `ibs_20min` < `0.104` → IC=+0.185 (n=411)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.104 (IC base=+0.074)

- **PATRÓN** `libro_liquidez` > `8124.6269` → IC=+0.146 (n=558)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 8124.6269 (IC base=+0.074)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.152 (n=438)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.007 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.170 (n=710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 11.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.47` → IC=+0.190 (n=994)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.47 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.9779` → IC=+0.197 (n=173)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.9779 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.008` → IC=+0.236 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.008 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.0501` → IC=+0.139 (n=875)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.0501 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.135 (n=888)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 0.7047 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2253` → IC=+0.161 (n=184)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2253 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4223` → IC=+0.144 (n=321)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4223 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.7996` → IC=+0.128 (n=640)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.7996 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.132 (n=1049)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2718.5359` → IC=+0.173 (n=451)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2718.5359 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.2105` → IC=+0.214 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2105 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `2847.0357` → IC=+0.157 (n=357)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 2847.0357 (IC base=+0.056)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0165` → IC=+0.240 (n=221)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0165 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.233 (n=155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.7308` → IC=+0.222 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7308 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.3108` → IC=+0.224 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3108 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.349` → IC=+0.217 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.349 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `1.1751` → IC=+0.234 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1751 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.1109` → IC=+0.201 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1109 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `1.8284` → IC=+0.212 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8284 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.5422` → IC=+0.200 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5422 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.194 (n=367)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.03 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `2525.0126` → IC=+0.217 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2525.0126 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.215 (n=163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0239 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2756` → IC=+0.151 (n=239)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.2756 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.202 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.165 (n=317)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.51 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `1.1297` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1297 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.232` → IC=+0.180 (n=98)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.232 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.238` → IC=+0.144 (n=318)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.238 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `0.872` → IC=+0.180 (n=239)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 0.872 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` < `0.113` → IC=+0.152 (n=326)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.113 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.181 (n=67)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `1.537` → IC=+0.201 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.537 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `2.6826` → IC=+0.164 (n=114)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.6826 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.155 (n=340)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 20.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.233 (n=6912)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=21636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.4333` → IC=+0.229 (n=20734)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4333 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.89` → IC=+0.213 (n=2535)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.89 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.028` → IC=+0.254 (n=5082)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.028 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2181` → IC=+0.160 (n=13946)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2181 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2415` → IC=+0.207 (n=3735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2415 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.6203` → IC=+0.194 (n=6742)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.6203 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.202 (n=19389)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.197 (n=8342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0059 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.200 (n=6315)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.4819` → IC=+0.196 (n=18945)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.4819 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=7040)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.5915` → IC=+0.243 (n=18945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5915 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.1792` → IC=+0.175 (n=11783)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` < 0.1792 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.542` → IC=+0.201 (n=2567)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.542 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.436` → IC=+0.197 (n=18455)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 3.436 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `0.6328` → IC=+0.175 (n=4248)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6328 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2916` → IC=+0.251 (n=2590)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2916 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.6273` → IC=+0.203 (n=6027)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6273 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.208 (n=17842)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 93.0 (IC base=+0.193)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.249 (n=1615)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=2244)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8618` → IC=+0.302 (n=2222)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8618 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.651` → IC=+0.338 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.651 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.295 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2784` → IC=+0.240 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2784 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.249 (n=3635)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2061.8302` → IC=+0.235 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2061.8302 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.254 (n=2068)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.269 (n=2945)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.123` → IC=+0.291 (n=1294)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.123 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.270 (n=2707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.267 (n=2671)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.4554` → IC=+0.292 (n=2586)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4554 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0962` → IC=+0.268 (n=2667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0962 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2886` → IC=+0.288 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2886 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.267 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6533` → IC=+0.275 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6533 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.270 (n=2015)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1771.0608` → IC=+0.276 (n=1959)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1771.0608 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.274 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.179 (n=1135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0031 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.148 (n=1132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=3538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.136)

- **PATRÓN** `ibs_20min` > `0.2058` → IC=+0.189 (n=3393)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2058 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.3227` → IC=+0.196 (n=1143)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3227 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.249` → IC=+0.162 (n=543)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.249 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` < `0.6365` → IC=+0.155 (n=1132)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6365 (IC base=+0.136)

- **PATRÓN** `volumen_regimen` > `1.0742` → IC=+0.138 (n=1539)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` > 1.0742 (IC base=+0.136)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.182 (n=488)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` < `2.1556` → IC=+0.142 (n=2930)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1556 (IC base=+0.136)

- **PATRÓN** `volumen_spike_ratio` > `1.5138` → IC=+0.140 (n=2974)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5138 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `306.0` → IC=+0.149 (n=2184)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 306.0 (IC base=+0.136)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.161 (n=2887)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0063 (IC base=+0.137)

- **PATRÓN** `drift_60min` |x|≤ `0.0793` → IC=+0.171 (n=961)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0793 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=1052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` < `0.6828` → IC=+0.185 (n=2883)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6828 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` < `0.1411` → IC=+0.152 (n=2757)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1411 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.045` → IC=+0.144 (n=1371)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 3.045 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `1.1917` → IC=+0.147 (n=2883)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 1.1917 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` > `0.219` → IC=+0.192 (n=533)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.219 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.4123` → IC=+0.144 (n=925)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4123 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.143 (n=1849)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=3742)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `228.0` → IC=+0.153 (n=899)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 228.0 (IC base=+0.137)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.244 (n=2307)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3622)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=3093)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=1289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.115` → IC=+0.321 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.115 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.132` → IC=+0.226 (n=3266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.132 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7403` → IC=+0.239 (n=1529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7403 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=4151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1380.4784` → IC=+0.230 (n=3454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1380.4784 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.247 (n=2887)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.1791` → IC=+0.262 (n=1441)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1791 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=1236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.242 (n=1495)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.0556` → IC=+0.304 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0556 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.291` → IC=+0.302 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.291 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.305 (n=486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `2.1662` → IC=+0.255 (n=2096)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1662 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1660)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1917.7208` → IC=+0.252 (n=1484)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.7208 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.249 (n=2741)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.242)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.195 (n=1194)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0036 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.4332` → IC=+0.148 (n=3578)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4332 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.150 (n=3720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.893` → IC=+0.277 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.893 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.166 (n=1672)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.986` → IC=+0.159 (n=1595)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.986 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.154 (n=2387)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8616 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.186 (n=632)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `1.5194` → IC=+0.155 (n=1539)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5194 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `2.1794` → IC=+0.145 (n=1586)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.1794 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `5436.372` → IC=+0.230 (n=1622)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5436.372 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.149 (n=2312)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 91.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.158 (n=3000)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0077 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.444` → IC=+0.149 (n=3001)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.444 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.166 (n=1098)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.7169` → IC=+0.193 (n=3000)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.7169 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.1522` → IC=+0.152 (n=2766)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1522 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.928` → IC=+0.157 (n=447)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 10.928 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.11` → IC=+0.141 (n=2613)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.11 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6889` → IC=+0.157 (n=1320)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6889 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.212 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.216` → IC=+0.142 (n=2547)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.216 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5364` → IC=+0.147 (n=2585)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5364 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `6321.4176` → IC=+0.214 (n=1000)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6321.4176 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `93.0` → IC=+0.151 (n=1954)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 93.0 (IC base=+0.139)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.149 (n=1647)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0112 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.150 (n=2566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4324` → IC=+0.192 (n=3623)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.4324 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.0228` → IC=+0.203 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0228 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.363` → IC=+0.267 (n=919)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.363 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2159` → IC=+0.125 (n=3622)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 1.2159 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.122 (n=3434)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.101 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.4831` → IC=+0.121 (n=3538)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4831 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.120 (n=3782)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2718.2425` → IC=+0.241 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2718.2425 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.130 (n=1144)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 20.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.155 (n=3008)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0107 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.1372` → IC=+0.153 (n=1140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1372 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.162 (n=1609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 15.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.6607` → IC=+0.216 (n=3418)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6607 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.2188` → IC=+0.144 (n=3063)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.2188 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.078` → IC=+0.151 (n=3304)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.078 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6386` → IC=+0.156 (n=1141)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6386 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2252` → IC=+0.174 (n=596)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2252 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4331` → IC=+0.160 (n=1079)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.4331 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2620.7147` → IC=+0.207 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2620.7147 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `51.0` → IC=+0.140 (n=3263)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 51.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.259 (n=2996)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=3505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.241 (n=3009)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.615` → IC=+0.273 (n=2995)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.615 (IC base=+0.237)

- **PATRÓN** `dist_vwap_pct` > `0.1927` → IC=+0.254 (n=1778)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1927 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.245` → IC=+0.286 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.245 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` < `1.2213` → IC=+0.239 (n=3353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2213 (IC base=+0.237)

- **PATRÓN** `volumen_regimen` > `0.6442` → IC=+0.240 (n=3353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6442 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.2391` → IC=+0.262 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2391 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.5041` → IC=+0.258 (n=1092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5041 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2107.7083` → IC=+0.239 (n=3353)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2107.7083 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0258` → IC=+0.265 (n=1145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0258 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.6217` → IC=+0.241 (n=3435)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6217 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1682)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.521` → IC=+0.273 (n=3434)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.521 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` < `0.2169` → IC=+0.247 (n=3221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2169 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.154` → IC=+0.279 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.154 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` > `1.2152` → IC=+0.263 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2152 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.303 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.432` → IC=+0.243 (n=3226)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.432 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.240 (n=3181)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.241)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=5753)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.244 (n=1986)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.504` → IC=+0.227 (n=5914)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.504 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=2134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9346` → IC=+0.255 (n=1973)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9346 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.4285` → IC=+0.222 (n=4310)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4285 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.579` → IC=+0.226 (n=1938)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.579 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.7088` → IC=+0.229 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7088 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` > `0.8838` → IC=+0.220 (n=2913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8838 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1052` → IC=+0.219 (n=5516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1052 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.1653` → IC=+0.223 (n=1672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1653 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `2.2557` → IC=+0.222 (n=5123)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2557 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=4628)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `3754.865` → IC=+0.227 (n=3943)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3754.865 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.237 (n=1446)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4928` → IC=+0.212 (n=4327)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4928 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=1455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.214 (n=1913)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.6124` → IC=+0.204 (n=3807)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6124 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.6592` → IC=+0.210 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6592 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.782` → IC=+0.211 (n=3882)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.782 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.095` → IC=+0.206 (n=3629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.095 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.201 (n=3984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.0735` → IC=+0.200 (n=1931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0735 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `1.5316` → IC=+0.203 (n=1877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5316 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.1857` → IC=+0.207 (n=1934)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1857 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.200 (n=5753)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `169.0` → IC=+0.212 (n=3746)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 169.0 (IC base=+0.199)

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

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.271 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2212 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `0.8749` → IC=+0.288 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8749 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.351 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.276 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1895` → IC=+0.269 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1895 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `12909.5134` → IC=+0.279 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12909.5134 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.190 (n=1518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.185 (n=564)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 5.0 (IC base=+0.176)

- **PATRÓN** `ibs_20min` < `0.138` → IC=+0.197 (n=668)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.138 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.315` → IC=+0.199 (n=1487)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.315 (IC base=+0.176)

- **PATRÓN** `volumen_regimen` < `1.2377` → IC=+0.185 (n=1518)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.2377 (IC base=+0.176)

- **PATRÓN** `volumen_pendiente_norm` > `0.1521` → IC=+0.194 (n=462)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1521 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` < `2.4929` → IC=+0.182 (n=1510)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.4929 (IC base=+0.176)

- **PATRÓN** `volumen_spike_ratio` > `2.1703` → IC=+0.180 (n=685)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.1703 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.180 (n=688)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.176)

- **PATRÓN** `ballena_activa_n` < `686.0` → IC=+0.188 (n=1473)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 686.0 (IC base=+0.176)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.231 (n=299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.587` → IC=+0.207 (n=897)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.587 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.233 (n=410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.3898` → IC=+0.204 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3898 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.245 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.494` → IC=+0.250 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.494 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0905` → IC=+0.227 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0905 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.8023` → IC=+0.208 (n=799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8023 (IC base=+0.200)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.208 (n=622)

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
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.220 (n=1620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.4542` → IC=+0.214 (n=1620)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4542 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.205)

- **PATRÓN** `ibs_20min` < `0.4996` → IC=+0.218 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4996 (IC base=+0.205)

- **PATRÓN** `ibs_20min` > `0.8568` → IC=+0.207 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8568 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.3956` → IC=+0.217 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3956 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.508` → IC=+0.211 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.508 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.212 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.205)

- **PATRÓN** `volumen_regimen` > `1.2249` → IC=+0.207 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2249 (IC base=+0.205)

- **PATRÓN** `volumen_pendiente_norm` < `0.1032` → IC=+0.210 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1032 (IC base=+0.205)

- **PATRÓN** `volumen_spike_ratio` < `2.4455` → IC=+0.213 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4455 (IC base=+0.205)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1683)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.242 (n=448)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4873` → IC=+0.220 (n=1341)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4873 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.211 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.216 (n=907)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.75` → IC=+0.203 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.75 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.0909` → IC=+0.205 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0909 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6242` → IC=+0.218 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6242 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.351` → IC=+0.205 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.351 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.6387` → IC=+0.231 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6387 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.074` → IC=+0.227 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.074 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.1885` → IC=+0.207 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1885 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.7842` → IC=+0.202 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7842 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `6506.9218` → IC=+0.206 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6506.9218 (IC base=+0.200)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.223 (n=625)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.232 (n=650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.270 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.7666` → IC=+0.239 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7666 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.212` → IC=+0.222 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.212 (IC base=+0.195)

- **PATRÓN** `volumen_regimen` < `0.6428` → IC=+0.243 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6428 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.204 (n=843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.0792` → IC=+0.202 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0792 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` < `2.1469` → IC=+0.202 (n=802)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1469 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.4705` → IC=+0.201 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4705 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `4318.6372` → IC=+0.240 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4318.6372 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.201 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.237 (n=459)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.5971` → IC=+0.241 (n=688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5971 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.223 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.250 (n=478)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.7312` → IC=+0.249 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7312 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.5347` → IC=+0.227 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5347 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.243` → IC=+0.230 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.243 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.791` → IC=+0.235 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.791 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.0973` → IC=+0.227 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0973 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `1.2826` → IC=+0.227 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2826 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` < `0.0825` → IC=+0.240 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0825 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.5701` → IC=+0.264 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5701 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `3262.8742` → IC=+0.237 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3262.8742 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `36.0` → IC=+0.259 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 36.0 (IC base=+0.222)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.150 (n=692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0037 (IC base=+0.055)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.190 (n=1325)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.75 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1492` → IC=+0.142 (n=996)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1492 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.568` → IC=+0.146 (n=436)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.568 (IC base=+0.055)

- **PATRÓN** `ibs_20min` < `0.0508` → IC=+0.264 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0508 (IC base=+0.045)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.52` → IC=-0.125 (n=278)

  - _Acción_: SKIP cuando `ibs_20min` < 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.171 (n=566)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.178 (n=293)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0031 (IC base=+0.073)

- **PATRÓN** `ibs_20min` > `0.52` → IC=+0.171 (n=566)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.52 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.166 (n=309)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.073)

- **PATRÓN** `ibs_20min` < `0.0742` → IC=+0.281 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0742 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.2164` → IC=+0.154 (n=105)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2164 (IC base=+0.050)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.171 (n=141)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=425)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.144 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0041 (IC base=+0.074)

- **PATRÓN** `ibs_20min` > `0.5237` → IC=+0.174 (n=572)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.5237 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.1273` → IC=+0.178 (n=321)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1273 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.717` → IC=+0.204 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.717 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.264 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.019)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9861` → IC=+0.208 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9861 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.728` → IC=+0.145 (n=164)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.728 (IC base=+0.022)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.213` → IC=+0.128 (n=197)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 7.213 (IC base=+0.022)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.149 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0112 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.169 (n=357)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.4857 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2741` → IC=+0.123 (n=361)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.2741 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.067)

- **PATRÓN** `volumen_regimen` > `1.1045` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1045 (IC base=+0.067)

- **PATRÓN** `volumen_pendiente_norm` > `0.1508` → IC=+0.154 (n=105)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.1508 (IC base=+0.067)

- **PATRÓN** `volumen_spike_ratio` > `1.8174` → IC=+0.124 (n=219)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` > 1.8174 (IC base=+0.067)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1871` → IC=-0.295 (n=86)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1871
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=261)

- **FILTRO** `dist_vwap_pct` > `0.2402` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2402
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=334)

- **FILTRO** `libro_liquidez` < `902.1333` → IC=-0.219 (n=87)

  - _Acción_: SKIP cuando `libro_liquidez` < 902.1333
  - _Potencial_: sin este filtro IC_bueno=-0.212 (n=262)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.295 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=242)

- **FILTRO** `dist_vwap_pct` > `0.3644` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3644
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=288)

- **FILTRO** `sigma_ewma_delta_pct` > `9.955` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.955
  - _Potencial_: sin este filtro IC_bueno=-0.282 (n=291)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=199)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_h` < `0.0059` → IC=-0.241 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0059
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=27)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.280 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

- **FILTRO** `volumen_regimen` < `0.8856` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8856
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=80)

- **FILTRO** `sigma_h` < `0.0033` → IC=-0.257 (n=72)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=73)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=96)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=109)

- **FILTRO** `libro_liquidez` < `5514.5282` → IC=-0.255 (n=108)

  - _Acción_: SKIP cuando `libro_liquidez` < 5514.5282
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5777` → IC=-0.468 (n=29)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5777
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=88)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.365 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=87)

- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.407 (n=41)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=81)

- **FILTRO** `volumen_spike_ratio` < `1.7371` → IC=-0.370 (n=44)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.7371
  - _Potencial_: sin este filtro IC_bueno=-0.261 (n=44)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.307 (n=107)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=108)

- **FILTRO** `volumen_regimen` < `0.8232` → IC=-0.314 (n=41)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8232
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=85)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.242 (n=29)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=97)

- **FILTRO** `sigma_h` < `0.0107` → IC=-0.325 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=13)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=36)

- **FILTRO** `dist_vwap_pct` > `0.3005` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3005
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=34)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.25` → IC=-0.152 (n=251)

  - _Acción_: SKIP cuando `ibs_20min` > 0.25
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=755)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.222 (n=217)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.190 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.137)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.176 (n=647)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` > 0.6757 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.7955` → IC=+0.282 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7955 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.624` → IC=+0.146 (n=354)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.624 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.564` → IC=+0.141 (n=661)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 8.564 (IC base=+0.137)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.179 (n=216)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6249 (IC base=+0.137)

- **PATRÓN** `volumen_pendiente_norm` < `0.2099` → IC=+0.161 (n=602)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` < 0.2099 (IC base=+0.137)

- **PATRÓN** `volumen_spike_ratio` < `1.388` → IC=+0.178 (n=181)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.388 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.784` → IC=+0.152 (n=219)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.784 (IC base=+0.035)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7142` → IC=-0.151 (n=64)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7142
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=194)

- **PATRÓN** `dist_vwap_pct` > `0.5848` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5848 (IC base=+0.027)

- **PATRÓN** `ibs_20min` < `0.2252` → IC=+0.165 (n=353)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.2252 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.348` → IC=+0.134 (n=80)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 11.348 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2688` → IC=+0.127 (n=57)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` > 0.2688 (IC base=+0.095)

- **PATRÓN** `volumen_spike_ratio` > `1.7675` → IC=+0.130 (n=214)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 1.7675 (IC base=+0.095)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1257` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1257
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=208)

- **FILTRO** `ibs_20min` > `0.1429` → IC=-0.121 (n=122)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1429
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=237)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.150 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0041 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1946` → IC=+0.129 (n=141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.1946 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.189 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 18.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.130 (n=71)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.798` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` > 0.798 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7699` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.7699 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.0973` → IC=+0.138 (n=172)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.0973 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.479` → IC=+0.153 (n=220)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 9.479 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6244 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `1.1961` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.1961 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1257` → IC=+0.167 (n=208)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.1257 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `2.1187` → IC=+0.156 (n=161)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1187 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=180)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.906` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 10.906 (IC base=+0.007)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=119)

- **FILTRO** `dist_vwap_pct` > `0.1813` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1813
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=140)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.289 (n=173)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.6` → IC=+0.271 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.6973` → IC=+0.381 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6973 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.344 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `0.5849` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5849 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.307 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.4721` → IC=+0.324 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4721 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.977` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.977 (IC base=-0.070)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.306 (n=96)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4 (IC base=+0.320)

- **PATRÓN** `elapsed_s` > `225.0` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 225.0 (IC base=+0.320)

- **PATRÓN** `drift_15min` |x|≤ `1.2521` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2521 (IC base=+0.320)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.368 (n=74)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.320)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.392 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.320)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.320)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `1.234` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.234 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.280 (n=57)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.306 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.239)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.306 (n=96)

- **PATRÓN** `drift_ventana_pct` |x|> `0.4` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.4 (IC base=+0.320)

- **PATRÓN** `elapsed_s` > `225.0` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 225.0 (IC base=+0.320)

- **PATRÓN** `drift_15min` |x|≤ `1.2521` → IC=+0.414 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.2521 (IC base=+0.320)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.368 (n=74)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.320)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.392 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.320)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.320)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.282 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `1.234` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.234 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.280 (n=57)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.306 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.239)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=239)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=239)

- **FILTRO** `libro_liquidez` < `2998.5952` → IC=-0.177 (n=63)

  - _Acción_: SKIP cuando `libro_liquidez` < 2998.5952
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=192)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=605)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11321.3584` → IC=-0.167 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 11321.3584
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=95)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `4139.65` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `liq_usd_total` < 4139.65
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=30)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.172 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 6.0 (IC base=+0.058)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `ballena_activa_n` > `14.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3883)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=118)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=118)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.121 (n=270)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1585)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1539)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=723)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=440)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=421)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.147 (n=185)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=954)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=954)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.128 (n=294)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=740)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1133)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1133)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=260)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=260)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.141 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=322)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=369)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=293)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=386)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=386)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=231)

- **FILTRO** `libro_liquidez` < `657.5195` → IC=-0.133 (n=137)

  - _Acción_: SKIP cuando `libro_liquidez` < 657.5195
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=279)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=322)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.145 (n=29)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=71)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.181 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=87)

- **FILTRO** `py_entrada` > `0.53` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` > 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=28)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.51` → IC=+0.133 (n=292)

  - _Acción_: Kelly boost +0.66€ cuando `py_entrada` < 0.51 (IC base=-0.007)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.143 (n=253)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=522)

- **FILTRO** `profundidad_ratio` < `62.0` → IC=-0.123 (n=255)

  - _Acción_: SKIP cuando `profundidad_ratio` < 62.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=520)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.130 (n=309)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=332)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.174 (n=133)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=574)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.124 (n=469)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=255)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.141 (n=104)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=329)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.124 (n=424)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=428)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.173 (n=7258)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=23384)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.174 (n=7776)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=23782)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.46` → IC=-0.185 (n=1405)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=4247)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.147 (n=1872)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=3730)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.135 (n=1479)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.043)

- **PATRÓN** `libro_liquidez` > `1864.6786` → IC=+0.139 (n=1413)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1864.6786 (IC base=+0.043)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.124 (n=2875)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.505 (IC base=+0.012)

- **PATRÓN** `libro_liquidez` > `1134.9556` → IC=+0.152 (n=1905)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1134.9556 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.170 (n=1005)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=3306)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.180 (n=1104)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3354)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=1386)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4345)

- **PATRÓN** `ibs_20min` > `0.9644` → IC=+0.133 (n=1921)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.9644 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `1352.3556` → IC=+0.121 (n=2825)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1352.3556 (IC base=+0.036)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.155 (n=1406)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=4277)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2427)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2351)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=2936)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=3888)

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
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=350)

- **FILTRO** `drift_20min_pct` |x|> `0.1569` → IC=-0.148 (n=157)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1569
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=306)

- **FILTRO** `libro_liquidez` < `3195.1545` → IC=-0.182 (n=152)

  - _Acción_: SKIP cuando `libro_liquidez` < 3195.1545
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=311)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=963)

- **FILTRO** `libro_liquidez` < `1813.405` → IC=-0.164 (n=245)

  - _Acción_: SKIP cuando `libro_liquidez` < 1813.405
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=737)

- **FILTRO** `ibs_20min` > `0.8824` → IC=-0.137 (n=576)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8824
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=580)

- **FILTRO** `ballena_activa_n` > `31.0` → IC=-0.211 (n=278)

  - _Acción_: SKIP cuando `ballena_activa_n` > 31.0
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=869)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=234)

### MOMENTUM_IBS_5M#BNB#5min
- **FILTRO** `hora_utc` > `17.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=44)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 17.0 (IC base=+0.024)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=20898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=47082)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=16105)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=51875)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.231 (n=16948)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=51032)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.151 (n=22511)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=45469)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.244 (n=21238)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=63873)

- **FILTRO** `ibs_7min` > `0.2838` → IC=-0.183 (n=21270)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2838
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=63841)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.154 (n=2941)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=9112)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.318 (n=2930)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=9123)

- **FILTRO** `ibs_7min` < `0.7103` → IC=-0.249 (n=3975)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7103
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=8078)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.149 (n=2723)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=9330)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.277 (n=3541)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=11178)

- **FILTRO** `ibs_7min` > `0.775` → IC=-0.213 (n=3677)

  - _Acción_: SKIP cuando `ibs_7min` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=11042)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.260 (n=2707)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=8650)

- **FILTRO** `ibs_7min` < `0.7173` → IC=-0.206 (n=2839)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7173
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=8518)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.194 (n=2818)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8539)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2640)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=8941)

- **FILTRO** `ibs_7min` > `0.2655` → IC=-0.192 (n=2894)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8687)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.181 (n=2888)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=8693)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.164 (n=2791)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=8745)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.323 (n=2725)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=8811)

- **FILTRO** `ibs_7min` < `0.2886` → IC=-0.249 (n=3806)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2886
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=7730)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.199 (n=2398)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=9138)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.259 (n=3728)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=11842)

- **FILTRO** `ibs_7min` > `0.7333` → IC=-0.184 (n=3884)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=11686)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2699)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8303)

- **FILTRO** `ibs_7min` < `0.7188` → IC=-0.192 (n=2748)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7188
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=8254)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.187 (n=2729)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=8273)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=2636)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=8840)

- **FILTRO** `ibs_7min` > `0.2747` → IC=-0.173 (n=2867)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2747
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=8609)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.169 (n=2850)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8626)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=2552)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=8392)

- **FILTRO** `ibs_7min` < `0.7059` → IC=-0.228 (n=3589)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7059
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=7355)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.219 (n=2732)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=8212)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.195 (n=3973)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=12483)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=3551)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=7537)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.308 (n=2594)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=8494)

- **FILTRO** `ibs_7min` < `0.1739` → IC=-0.229 (n=2771)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1739
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=8317)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.203 (n=2523)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=8565)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.234 (n=3557)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=11752)

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

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=158)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=604)

- **FILTRO** `libro_liquidez` < `10485.1399` → IC=-0.156 (n=190)

  - _Acción_: SKIP cuando `libro_liquidez` < 10485.1399
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=572)

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
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=880)

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

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=97)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=669)

- **FILTRO** `libro_liquidez` < `3298.5458` → IC=-0.153 (n=191)

  - _Acción_: SKIP cuando `libro_liquidez` < 3298.5458
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=575)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.155 (n=641)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.135 (n=723)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 6.0 (IC base=+0.124)

- **PATRÓN** `total_vol_5m` < `418.1817` → IC=+0.164 (n=471)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 418.1817 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `3540.7982` → IC=+0.140 (n=640)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3540.7982 (IC base=+0.124)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.192 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 14.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `375.759` → IC=+0.154 (n=299)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 375.759 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2527.6661` → IC=+0.230 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2527.6661 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `5.0` → IC=+0.134 (n=129)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 5.0 (IC base=+0.132)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4312` → IC=+0.149 (n=132)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4312 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.139 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 15.0 (IC base=+0.117)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.194 (n=178)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.147 (n=281)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 4.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `506.4056` → IC=+0.174 (n=179)

  - _Acción_: Kelly boost +0.87€ cuando `total_vol_5m` < 506.4056 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `5255.107` → IC=+0.132 (n=267)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 5255.107 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.195 (n=93)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 59.0 (IC base=+0.131)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.398` → IC=+0.168 (n=242)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.84€ cuando `delta_ratio` |x|> 0.398 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.186 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.142)

- **PATRÓN** `total_vol_5m` < `6100.528` → IC=+0.170 (n=213)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 6100.528 (IC base=+0.142)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.122 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 14.0 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=187)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.096)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.4417` → IC=-0.272 (n=55)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.4417
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=167)

- **FILTRO** `pct_vs_K` |x|> `3.42` → IC=-0.194 (n=269)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.42
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=524)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.149 (n=263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0044 (IC base=-0.085)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9952` → IC=-0.233 (n=58)

  - _Acción_: SKIP cuando `T_h` > 87.9952
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=177)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.263 (n=78)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.040)

- **PATRÓN** `pct_vs_K` |x|≤ `1.632` → IC=+0.150 (n=78)

  - _Acción_: Kelly boost +0.75€ cuando `pct_vs_K` |x|≤ 1.632 (IC base=-0.040)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `T_h` < `251.7955` → IC=-0.210 (n=60)

  - _Acción_: SKIP cuando `T_h` < 251.7955
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `91.7077` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `T_h` < 91.7077
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=75)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `sigma_h` < `0.0164` → IC=-0.192 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0164
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0109` → IC=-0.234 (n=546)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0109
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=183)

- **FILTRO** `T_h` > `71.2514` → IC=-0.220 (n=488)

  - _Acción_: SKIP cuando `T_h` > 71.2514
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=241)

- **FILTRO** `sigma_h` < `0.0052` → IC=-0.215 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.209 (n=469)

- **FILTRO** `pct_vs_K` |x|> `3.1226` → IC=-0.418 (n=156)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1226
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=469)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0091` → IC=-0.204 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=60)

- **FILTRO** `T_h` > `87.9866` → IC=-0.208 (n=118)

  - _Acción_: SKIP cuando `T_h` > 87.9866
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=119)

- **FILTRO** `sigma_h` > `0.0069` → IC=-0.297 (n=77)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=150)

- **FILTRO** `T_h` > `143.7867` → IC=-0.241 (n=56)

  - _Acción_: SKIP cuando `T_h` > 143.7867
  - _Potencial_: sin este filtro IC_bueno=-0.234 (n=171)

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
- **FILTRO** `pct_vs_K` |x|> `3.2046` → IC=-0.387 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2046
  - _Potencial_: sin este filtro IC_bueno=-0.199 (n=134)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.357 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=144)

- **FILTRO** `sigma_h` < `0.0054` → IC=-0.194 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.164 (n=144)

- **FILTRO** `T_h` > `57.5396` → IC=-0.229 (n=127)

  - _Acción_: SKIP cuando `T_h` > 57.5396
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=64)

- **PATRÓN** `pct_vs_K` |x|≤ `0.8` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `pct_vs_K` |x|≤ 0.8 (IC base=-0.174)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.292 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=154)

- **FILTRO** `T_h` > `69.913` → IC=-0.216 (n=153)

  - _Acción_: SKIP cuando `T_h` > 69.913
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=52)

- **FILTRO** `sigma_h` > `0.014` → IC=-0.316 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.014
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=92)

- **FILTRO** `sigma_h` < `0.0082` → IC=-0.278 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0082
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=105)

- **FILTRO** `T_h` > `33.8406` → IC=-0.264 (n=104)

  - _Acción_: SKIP cuando `T_h` > 33.8406
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1195` → IC=+0.470 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1195 (IC base=+0.341)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.357 (n=96)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.013 (IC base=+0.341)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.380 (n=73)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.341)

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

- **PATRÓN** `T_h` < `0.6127` → IC=+0.443 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.404)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=372)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=455)

- **PATRÓN** `streak_estiramiento` < `0.293` → IC=+0.167 (n=94)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.293 (IC base=+0.027)

- **PATRÓN** `streak_estiramiento` < `0.3661` → IC=+0.221 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.3661 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 16.0 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `2555.3558` → IC=+0.130 (n=163)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2555.3558 (IC base=+0.060)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.495 (IC base=+0.075)

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
- **FILTRO** `streak_estiramiento` > `0.4315` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4315
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=122)

- **PATRÓN** `streak_estiramiento` < `0.3805` → IC=+0.120 (n=106)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.3805 (IC base=+0.030)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.128 (n=154)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.096)

- **PATRÓN** `streak_estiramiento` < `0.555` → IC=+0.171 (n=150)

  - _Acción_: Kelly boost +0.86€ cuando `streak_estiramiento` < 0.555 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.167 (n=142)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 31.0 (IC base=+0.096)

- **PATRÓN** `libro_liquidez` > `2555.3558` → IC=+0.140 (n=112)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 2555.3558 (IC base=+0.096)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=100)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=109)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=36)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=50)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1054)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1336)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4594)

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
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2652)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.188 (n=2082)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.006 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2143` → IC=+0.168 (n=4737)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2143 (IC base=+0.154)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3545` → IC=+0.163 (n=4385)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3545 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.165 (n=4377)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.221 (n=4739)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1329` → IC=+0.145 (n=2266)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.1329 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.692` → IC=+0.140 (n=4591)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.692 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.641` → IC=+0.264 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.641 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=2842)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `4814.9511` → IC=+0.177 (n=1578)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 4814.9511 (IC base=+0.154)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1828)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.223 (n=738)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0597` → IC=+0.254 (n=246)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0597 (IC base=+0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.222 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.224 (n=769)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.7103` → IC=+0.277 (n=738)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7103 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.376` → IC=+0.221 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.376 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.5198` → IC=+0.207 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5198 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.778` → IC=+0.314 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.778 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `14792.3098` → IC=+0.224 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14792.3098 (IC base=+0.203)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.155 (n=903)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0069 (IC base=+0.136)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.151 (n=602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.136)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1428` → IC=+0.137 (n=602)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.1428 (IC base=+0.136)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1286` → IC=+0.142 (n=364)

  - _Acción_: Kelly boost +0.71€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1286 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.142 (n=826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 6.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.139 (n=950)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.136)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.223 (n=903)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.1197` → IC=+0.148 (n=567)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1197 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.629` → IC=+0.138 (n=1028)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.629 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.997` → IC=+0.290 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.997 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `5812.1498` → IC=+0.165 (n=410)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 5812.1498 (IC base=+0.136)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8649` → IC=+0.186 (n=412)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.8649 (IC base=+0.066)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0249` → IC=+0.179 (n=1113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0249 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.187 (n=1113)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0128 (IC base=+0.176)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.216 (n=371)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.176)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3533` → IC=+0.204 (n=1010)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3533 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.180 (n=1022)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.183 (n=997)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 14.0 (IC base=+0.176)

- **PATRÓN** `ibs_15` > `0.4651` → IC=+0.244 (n=1116)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4651 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.509` → IC=+0.210 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.509 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.942` → IC=+0.224 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.942 (IC base=+0.176)

- **PATRÓN** `libro_liquidez` > `2947.677` → IC=+0.212 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2947.677 (IC base=+0.176)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.163 (n=910)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.82€ cuando `ibs_15` < 0.1111 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.384 (n=239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1506` → IC=+0.379 (n=477)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1506 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1386` → IC=+0.382 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1386 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.372 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7883` → IC=+0.394 (n=716)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7883 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1523` → IC=+0.384 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1523 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.219` → IC=+0.399 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.219 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `9974.3192` → IC=+0.381 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9974.3192 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.369 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1584` → IC=+0.371 (n=238)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1584 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1464` → IC=+0.388 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1464 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.381 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.386 (n=357)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3743` → IC=+0.389 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3743 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.244` → IC=+0.388 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.244 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `8157.6321` → IC=+0.383 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8157.6321 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.402 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.370 (n=359)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.376 (n=239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.1078` → IC=+0.364 (n=240)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1078 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.376 (n=321)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.381 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.368 (n=361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.373 (n=163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.8123` → IC=+0.401 (n=321)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8123 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1215` → IC=+0.376 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1215 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.6628` → IC=+0.367 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6628 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.534` → IC=+0.408 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.534 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4067.0691` → IC=+0.385 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4067.0691 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.225 (n=1715)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=3330)

- **FILTRO** `drift_15min` |x|> `0.9075` → IC=-0.140 (n=1260)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9075
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=3784)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=2076)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2969)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1404` → IC=+0.224 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1404 (IC base=-0.076)

- **PATRÓN** `ibs_15` > `0.6306` → IC=+0.280 (n=1164)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6306 (IC base=-0.076)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.201 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.076)

- **PATRÓN** `dist_vwap_pct` < `0.5662` → IC=+0.202 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5662 (IC base=-0.076)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2357` → IC=+0.268 (n=1512)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2357 (IC base=-0.005)

- **PATRÓN** `ibs_15` < `0.3679` → IC=+0.284 (n=4536)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3679 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` > `0.6531` → IC=+0.279 (n=640)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6531 (IC base=-0.005)

- **PATRÓN** `dist_vwap_pct` < `0.1657` → IC=+0.249 (n=3331)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1657 (IC base=-0.005)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0322` → IC=-0.221 (n=2377)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0322
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=793)

- **FILTRO** `sigma_h` < `0.0037` → IC=-0.214 (n=792)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2378)

- **FILTRO** `sigma_ewma_delta_pct` > `22.577` → IC=-0.264 (n=456)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.577
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=2714)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.149 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0034 (IC base=+0.075)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.267 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.075)

- **PATRÓN** `ibs_15` > `0.7609` → IC=+0.327 (n=397)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7609 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.281 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.4928` → IC=+0.286 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4928 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.802` → IC=+0.144 (n=209)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 22.802 (IC base=+0.075)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0674` → IC=+0.240 (n=71)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0674 (IC base=-0.185)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0839` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0839 (IC base=-0.185)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.322 (n=71)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.185)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.185)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.306 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 381.0 (IC base=-0.185)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.156 (n=762)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.158 (n=585)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0065 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.157` → IC=+0.165 (n=515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.157 (IC base=+0.149)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3048` → IC=+0.202 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3048 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.164 (n=420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5749` → IC=+0.243 (n=585)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5749 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1135` → IC=+0.150 (n=364)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1135 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1597` → IC=+0.153 (n=453)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1597 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.267 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=762)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `5052.7931` → IC=+0.156 (n=390)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 5052.7931 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.257 (n=1140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.3573` → IC=+0.244 (n=1504)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3573 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.7761` → IC=+0.256 (n=1504)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7761 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2178` → IC=+0.263 (n=775)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2178 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.244 (n=643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.3771` → IC=+0.274 (n=1709)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3771 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.6155` → IC=+0.271 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6155 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.354` → IC=+0.247 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.354 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.183` → IC=-0.253 (n=289)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.183
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=871)

- **FILTRO** `drift_60min` |x|> `0.1726` → IC=-0.255 (n=394)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1726
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=766)

- **FILTRO** `drift_15min` |x|> `0.9075` → IC=-0.283 (n=289)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9075
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=871)

- **FILTRO** `sigma_ewma_delta_pct` > `6.283` → IC=-0.206 (n=270)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.283
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=890)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.193)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.193)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.193)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.196 (n=21)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 29.0 (IC base=-0.193)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0653` → IC=+0.232 (n=774)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0653 (IC base=-0.030)

- **PATRÓN** `ibs_15` < `0.3913` → IC=+0.298 (n=775)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3913 (IC base=-0.030)

- **PATRÓN** `dist_vwap_pct` < `0.4549` → IC=+0.242 (n=830)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4549 (IC base=-0.030)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.1499` → IC=-0.231 (n=351)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1499
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=1055)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.242 (n=685)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=721)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.213)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.213)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1175` → IC=+0.272 (n=686)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1175 (IC base=-0.022)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.291 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.022)

- **PATRÓN** `ibs_15` < `0.1346` → IC=+0.308 (n=687)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.1346 (IC base=-0.022)

- **PATRÓN** `dist_vwap_pct` > `0.7546` → IC=+0.340 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7546 (IC base=-0.022)

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
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.291 (n=1264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.312 (n=558)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.290 (n=842)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2237` → IC=+0.294 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2237 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=1308)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8395` → IC=+0.314 (n=1265)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8395 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.313 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.34` → IC=+0.387 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.34 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `13449.5003` → IC=+0.307 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13449.5003 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.311 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.278)

- **PATRÓN** `drift_60min` |x|≤ `0.0596` → IC=+0.315 (n=225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0596 (IC base=+0.278)

- **PATRÓN** `drift_15min` |x|≤ `0.3855` → IC=+0.280 (n=225)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3855 (IC base=+0.278)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3948` → IC=+0.284 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3948 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.300 (n=703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.278)

- **PATRÓN** `ibs_15` > `0.83` → IC=+0.303 (n=672)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.83 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.2522` → IC=+0.309 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2522 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.15` → IC=+0.388 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.15 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.279 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `15946.6772` → IC=+0.319 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15946.6772 (IC base=+0.278)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.308 (n=592)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.311 (n=395)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0665` → IC=+0.296 (n=592)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0665 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.101` → IC=+0.338 (n=183)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.101 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.299 (n=540)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8494` → IC=+0.323 (n=592)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8494 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.310 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` < `0.4611` → IC=+0.292 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4611 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.388 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `drift_60min` |x|> `0.2656` → IC=-0.130 (n=90)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2656
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=273)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.159 (n=89)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=274)

- **FILTRO** `ballena_activa_n` > `34.0` → IC=-0.129 (n=246)

  - _Acción_: SKIP cuando `ballena_activa_n` > 34.0
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=85)

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
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

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
- **PATRÓN** `ratio` < `0.9701` → IC=+0.396 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9701 (IC base=+0.182)

- **PATRÓN** `T_h` > `118.8029` → IC=+0.353 (n=2646)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 118.8029 (IC base=+0.335)

- **PATRÓN** `ratio` > `1.0204` → IC=+0.379 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0204 (IC base=+0.335)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9936` → IC=+0.145 (n=249)

  - _Acción_: Kelly boost +0.73€ cuando `T_h` > 111.9936 (IC base=+0.143)

- **PATRÓN** `ratio` < `0.979` → IC=+0.320 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.979 (IC base=+0.143)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.314 (n=947)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.300)

- **PATRÓN** `ratio` > `1.0178` → IC=+0.355 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0178 (IC base=+0.300)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9849` → IC=+0.422 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.228)

- **PATRÓN** `T_h` > `111.9969` → IC=+0.352 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.320)

- **PATRÓN** `ratio` > `1.0298` → IC=+0.398 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0298 (IC base=+0.320)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0625` → IC=+0.426 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0625 (IC base=+0.398)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.154 a +0.221 en UPDOWN_GBM#15min (n=4739). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7103 sube el IC de +0.203 a +0.277 en UPDOWN_GBM#BTC#15min (n=738). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.136 a +0.223 en UPDOWN_GBM#ETH#15min (n=903). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8649 sube el IC de +0.066 a +0.186 en UPDOWN_GBM#SOL#15min (n=412). Ya aplicado como kelly_boost=+0.93€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.4651 sube el IC de +0.176 a +0.244 en UPDOWN_GBM#XRP#15min (n=1116). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.067 a +0.163 en UPDOWN_GBM#XRP#15min (n=910). Ya aplicado como kelly_boost=+0.82€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6306 sube el IC de -0.076 a +0.280 en UPDOWN_GBM_15M_TARDIO (n=1164). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3679 sube el IC de -0.005 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=4536). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7609 sube el IC de +0.075 a +0.327 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=397). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.185 a +0.322 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=71). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5749 sube el IC de +0.149 a +0.243 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=585). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3771 sube el IC de +0.242 a +0.274 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1709). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.193 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3913 sube el IC de -0.030 a +0.298 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=775). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.213 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.1346 sube el IC de -0.022 a +0.308 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=687). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.103 a +0.370 en UPDOWN_GBM_ETH_15M_HORA7 (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.103 a +0.370 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8395 sube el IC de +0.285 a +0.314 en UPDOWN_GBM_IBS_ALTO (n=1265). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.83 sube el IC de +0.278 a +0.303 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=672). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8494 sube el IC de +0.293 a +0.323 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=592). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7883 sube el IC de +0.364 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=716). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=357). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8123 sube el IC de +0.365 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=321). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2123 | +0.086 | +234.68€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2123 | +0.086 | +234.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1718 | +0.087 | +195.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1718 | +0.087 | +195.39€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 90 | +0.130 | +28.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 90 | +0.130 | +28.32€ | 1 | 10 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 985 | -0.019 | +78.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 985 | -0.019 | +78.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 753 | -0.039 | +54.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 753 | -0.039 | +54.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 154 | +0.083 | +26.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 154 | +0.083 | +26.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 72 | -0.027 | -4.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 72 | -0.027 | -4.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 45322 | -0.085 | -5604.04€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2677 | +0.055 | -283.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 42645 | -0.094 | -5320.64€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4708 | -0.111 | -764.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4708 | -0.111 | -764.01€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2677 | +0.055 | -283.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2677 | +0.055 | -283.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4679 | -0.117 | -911.71€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4679 | -0.117 | -911.71€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 12383 | -0.038 | -1114.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 12383 | -0.038 | -1114.36€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 12245 | -0.114 | -1194.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 12245 | -0.114 | -1194.63€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8630 | -0.124 | -1335.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8630 | -0.124 | -1335.91€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 44966 | -0.013 | +3057.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 11610 | +0.005 | +1585.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 33356 | -0.019 | +1472.73€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 44966 | -0.013 | +3057.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 11610 | +0.005 | +1585.14€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 33356 | -0.019 | +1472.73€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 175406 | +0.113 | -7168.53€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 20975 | +0.180 | -649.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 797 | +0.001 | -75.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 143489 | +0.106 | -6068.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 10145 | +0.092 | -374.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 23777 | +0.105 | -1572.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 71 | -0.158 | +15.94€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 23691 | +0.106 | -1576.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 33475 | +0.124 | -566.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5563 | +0.180 | -221.52€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 23760 | +0.120 | -179.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4110 | +0.078 | -142.67€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 23827 | +0.099 | -1701.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 83 | -0.112 | +7.08€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 23729 | +0.100 | -1697.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 37429 | +0.124 | -739.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 9513 | +0.178 | -212.23€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 24128 | +0.106 | -463.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3776 | +0.101 | -55.62€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 33095 | +0.112 | -1528.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5663 | +0.199 | -250.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 700 | +0.029 | -21.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 24473 | +0.096 | -1079.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2259 | +0.102 | -176.51€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 23803 | +0.107 | -1060.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 82 | -0.107 | +11.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 23708 | +0.107 | -1071.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 28389 | +0.194 | -1871.83€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 28389 | +0.194 | -1871.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 6411 | +0.175 | -594.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 6411 | +0.175 | -594.99€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3968 | +0.198 | -139.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3968 | +0.198 | -139.00€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6324 | +0.177 | -540.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6324 | +0.177 | -540.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5373 | +0.249 | -194.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5373 | +0.249 | -194.40€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6234 | +0.186 | -416.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6234 | +0.186 | -416.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1184 | +0.426 | -43.15€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1184 | +0.426 | -43.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 483 | +0.440 | -3.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 483 | +0.440 | -3.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 477 | +0.425 | -17.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 477 | +0.425 | -17.25€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 210 | +0.396 | -18.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 210 | +0.396 | -18.74€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 99986 | +0.201 | -7235.23€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 99986 | +0.201 | -7235.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 17228 | +0.181 | -1881.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 17228 | +0.181 | -1881.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 16127 | +0.225 | -515.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 16127 | +0.225 | -515.13€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 17157 | +0.181 | -1801.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 17157 | +0.181 | -1801.45€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 16262 | +0.218 | -650.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 16262 | +0.218 | -650.74€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 16538 | +0.203 | -1061.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 16538 | +0.203 | -1061.44€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 16674 | +0.197 | -1324.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 16674 | +0.197 | -1324.60€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 38413 | +0.116 | +255.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 38413 | +0.116 | +255.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 19125 | +0.117 | +173.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 19125 | +0.117 | +173.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 19288 | +0.115 | +81.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 19288 | +0.115 | +81.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2435 | +0.294 | -4.11€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2435 | +0.294 | -4.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1114 | +0.281 | -25.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1114 | +0.281 | -25.96€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1186 | +0.299 | +18.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1186 | +0.299 | +18.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 135 | +0.339 | +3.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 135 | +0.339 | +3.85€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1120 | +0.441 | +3.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1120 | +0.441 | +3.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 537 | +0.435 | -6.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 537 | +0.435 | -6.54€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 533 | +0.448 | +8.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 533 | +0.448 | +8.44€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 50 | +0.404 | +1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 50 | +0.404 | +1.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1873 | +0.068 | -82.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1148 | +0.082 | -17.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1439 | +0.076 | -36.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1148 | +0.082 | -17.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 77416 | +0.100 | -1872.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 6232 | +0.095 | +125.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 71184 | +0.101 | -1997.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 42377 | +0.105 | -423.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 6232 | +0.095 | +125.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 36145 | +0.107 | -548.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 16310 | +0.109 | -94.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 16310 | +0.109 | -94.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 18729 | +0.082 | -1354.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 18729 | +0.082 | -1354.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 2 | 4 |
| ✅ GBM_LATE_15M | 52673 | +0.098 | +28983.14€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 52673 | +0.098 | +28983.14€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 8748 | +0.224 | +7499.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 8748 | +0.224 | +7499.17€ | 0 | 21 |
| ✅ GBM_LATE_15M#BTC | 8013 | +0.175 | +6229.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 8013 | +0.175 | +6229.54€ | 0 | 24 |
| ✅ GBM_LATE_15M#DOGE | 9440 | +0.206 | +7403.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 9440 | +0.206 | +7403.13€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 7178 | +0.050 | +2202.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7178 | +0.050 | +2202.40€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 7367 | -0.031 | +1903.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 7367 | -0.031 | +1903.62€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 11927 | -0.025 | +3745.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 11927 | -0.025 | +3745.29€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 55580 | +0.085 | +31968.71€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 55580 | +0.085 | +31968.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 10821 | -0.002 | +5777.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 10821 | -0.002 | +5777.17€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 11890 | +0.004 | +3098.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 11890 | +0.004 | +3098.88€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 7593 | +0.291 | +8562.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 7593 | +0.291 | +8562.57€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 10456 | +0.014 | +3160.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 10456 | +0.014 | +3160.43€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 8619 | +0.043 | +3816.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 8619 | +0.043 | +3816.89€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 6201 | +0.314 | +7552.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 6201 | +0.314 | +7552.77€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 41732 | +0.179 | +34419.55€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 41732 | +0.179 | +34419.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6283 | +0.239 | +5846.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6283 | +0.239 | +5846.62€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 6628 | +0.140 | +4874.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 6628 | +0.140 | +4874.31€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 6699 | +0.225 | +5812.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 6699 | +0.225 | +5812.65€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 7129 | +0.133 | +5567.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 7129 | +0.133 | +5567.06€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 7878 | +0.121 | +5902.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 7878 | +0.121 | +5902.13€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7115 | +0.232 | +6416.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7115 | +0.232 | +6416.78€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 11185 | +0.126 | +5564.96€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 11185 | +0.126 | +5564.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 463 | +0.158 | +306.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 463 | +0.158 | +306.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3246 | +0.134 | +1789.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3246 | +0.134 | +1789.66€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 491 | +0.153 | +259.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3314 | +0.128 | +1631.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3314 | +0.128 | +1631.16€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2752 | +0.090 | +1026.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2752 | +0.090 | +1026.88€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 919 | +0.165 | +550.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 919 | +0.165 | +550.38€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 52899 | +0.186 | +43221.86€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 52899 | +0.186 | +43221.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 8361 | +0.249 | +8059.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 8361 | +0.249 | +8059.55€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 8367 | +0.136 | +5718.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 8367 | +0.136 | +5718.59€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 8969 | +0.233 | +8044.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 8969 | +0.233 | +8044.98€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 8769 | +0.139 | +6422.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 8769 | +0.139 | +6422.61€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 9385 | +0.123 | +6648.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 9385 | +0.123 | +6648.23€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 9048 | +0.239 | +8327.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 9048 | +0.239 | +8327.90€ | 0 | 21 |
| ✅ GBM_LATE_5M | 13653 | +0.210 | +11075.63€ | 1 | 27 |
| ✅ GBM_LATE_5M#5min | 13653 | +0.210 | +11075.63€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1054 | +0.246 | +1000.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3256 | +0.211 | +2806.84€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3256 | +0.211 | +2806.84€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1274 | +0.202 | +976.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1274 | +0.202 | +976.73€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 3946 | +0.203 | +2967.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3946 | +0.203 | +2967.42€ | 0 | 25 |
| ✅ GBM_LATE_5M#SOL | 2165 | +0.207 | +1789.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2165 | +0.207 | +1789.15€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1958 | +0.209 | +1535.21€ | 0 | 0 |
| ✅ GBM_LATE_60M | 4604 | +0.051 | +1217.01€ | 0 | 5 |
| ✅ GBM_LATE_60M#60min | 4604 | +0.051 | +1217.01€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1627 | +0.062 | +501.47€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1627 | +0.062 | +501.47€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1489 | +0.052 | +435.56€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1489 | +0.052 | +435.56€ | 1 | 5 |
| ✅ GBM_LATE_60M#SOL | 1488 | +0.038 | +279.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1488 | +0.038 | +279.97€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 667 | -0.250 | -35.29€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 667 | -0.250 | -35.29€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 251 | -0.251 | -20.27€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 251 | -0.251 | -20.27€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 239 | -0.247 | -7.78€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 239 | -0.247 | -7.78€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 177 | -0.249 | -7.24€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 177 | -0.249 | -7.24€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1868 | +0.082 | +474.81€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1868 | +0.082 | +474.81€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 728 | +0.071 | +173.00€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 728 | +0.071 | +173.00€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 640 | +0.058 | +114.26€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 640 | +0.058 | +114.26€ | 2 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 500 | +0.128 | +187.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 500 | +0.128 | +187.55€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 211 | +0.279 | +225.02€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 211 | +0.279 | +225.02€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 211 | +0.279 | +225.02€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 211 | +0.279 | +225.02€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4172 | +0.097 | +955.43€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4172 | +0.097 | +955.43€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4172 | +0.097 | +955.43€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4172 | +0.097 | +955.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 881 | -0.013 | +13.48€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 881 | -0.013 | +13.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 32 | -0.029 | -1.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 32 | -0.029 | -1.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 253 | -0.018 | +3.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 253 | -0.018 | +3.68€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 29 | -0.145 | -4.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 242 | +0.029 | +20.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 242 | +0.029 | +20.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 271 | +0.002 | +5.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 271 | +0.002 | +5.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 54 | -0.161 | -9.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 54 | -0.161 | -9.89€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4107 | +0.016 | +98.71€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 4107 | +0.016 | +98.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 197 | +0.033 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 197 | +0.033 | +0.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 822 | +0.015 | +39.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 822 | +0.015 | +39.25€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 217 | -0.002 | -0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 217 | -0.002 | -0.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1637 | +0.019 | +27.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1637 | +0.019 | +27.76€ | 6 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 764 | +0.012 | +2.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 764 | +0.012 | +2.20€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 470 | +0.015 | +29.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 470 | +0.015 | +29.46€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2182 | -0.035 | -16.80€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2182 | -0.035 | -16.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 659 | -0.023 | -6.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 659 | -0.023 | -6.81€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 770 | -0.014 | +11.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 770 | -0.014 | +11.36€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 753 | -0.066 | -21.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 753 | -0.066 | -21.35€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 13339 | -0.032 | -120.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 6387 | -0.035 | -104.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 6952 | -0.029 | -16.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 477 | -0.047 | -22.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 242 | -0.012 | +7.30€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 235 | -0.082 | -29.42€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 3483 | -0.024 | +6.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1654 | -0.023 | +6.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1829 | -0.024 | +0.27€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1340 | -0.024 | +25.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 681 | -0.032 | +0.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 659 | -0.016 | +25.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3006 | -0.037 | -74.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1416 | -0.042 | -55.30€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1590 | -0.033 | -19.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2559 | -0.029 | -4.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1237 | -0.037 | -21.81€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1322 | -0.023 | +17.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2474 | -0.040 | -51.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1157 | -0.049 | -41.35€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1317 | -0.033 | -10.21€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 62200 | +0.000 | +3404.09€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 62200 | +0.000 | +3404.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 11254 | +0.028 | +1540.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 11254 | +0.028 | +1540.33€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 8769 | -0.036 | -98.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 8769 | -0.036 | -98.82€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 11381 | +0.025 | +1238.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 11381 | +0.025 | +1238.88€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 8678 | -0.050 | -171.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 8678 | -0.050 | -171.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 10564 | -0.004 | +301.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 10564 | -0.004 | +301.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 11554 | +0.018 | +594.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 11554 | +0.018 | +594.39€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7033 | -0.055 | -117.16€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7033 | -0.055 | -117.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1242 | -0.002 | -15.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1242 | -0.002 | -15.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1928 | -0.067 | -30.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1928 | -0.067 | -30.33€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 70 | +0.000 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 70 | +0.000 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 797 | -0.119 | -34.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 797 | -0.119 | -34.54€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2138 | -0.068 | -11.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2138 | -0.068 | -11.69€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3375 | +0.003 | -2.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3375 | +0.003 | -2.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 132 | -0.037 | -1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 132 | -0.037 | -1.23€ | 2 | 1 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 153091 | -0.077 | +2188.20€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 153091 | -0.077 | +2188.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 26772 | -0.078 | +1499.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 26772 | -0.078 | +1499.91€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 22938 | -0.100 | -1059.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 22938 | -0.100 | -1059.54€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 27106 | -0.069 | +1273.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 27106 | -0.069 | +1273.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 22478 | -0.097 | -626.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 22478 | -0.097 | -626.27€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 27400 | -0.058 | +318.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 27400 | -0.058 | +318.12€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 26397 | -0.070 | +782.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 26397 | -0.070 | +782.62€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8984 | -0.035 | -186.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8984 | -0.035 | -186.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2070 | -0.047 | -29.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2070 | -0.047 | -29.48€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2631 | -0.026 | -39.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2631 | -0.026 | -39.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1266 | -0.065 | -32.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1266 | -0.065 | -32.98€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1006 | -0.032 | -33.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1006 | -0.032 | -33.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2017 | +0.120 | +800.00€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 1881 | +0.124 | +787.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 452 | +0.132 | +216.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 452 | +0.132 | +216.95€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 387 | +0.117 | +134.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 387 | +0.117 | +134.20€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 356 | +0.131 | +168.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 356 | +0.131 | +168.15€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 322 | +0.142 | +165.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 322 | +0.142 | +165.86€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 364 | +0.096 | +102.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 364 | +0.096 | +102.25€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1937 | -0.016 | -16.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1937 | -0.016 | -16.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 368 | +0.013 | +22.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 368 | +0.013 | +22.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 349 | -0.033 | -13.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 349 | -0.033 | -13.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 490 | -0.045 | -35.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 490 | -0.045 | -35.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 392 | -0.003 | -0.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 392 | -0.003 | -0.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 338 | -0.003 | +11.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 338 | -0.003 | +11.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1082 | -0.082 | -56.57€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 498 | -0.114 | -79.57€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 386 | -0.131 | -61.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 112 | -0.053 | -18.46€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 380 | -0.042 | +18.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 269 | -0.028 | +27.62€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 111 | -0.075 | -9.44€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 204 | -0.078 | +4.82€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 168 | -0.076 | +2.99€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 823 | -0.087 | -30.50€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 259 | -0.067 | -26.07€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1354 | -0.209 | -85.90€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 531 | -0.209 | -47.81€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 464 | -0.208 | -43.50€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 67 | -0.210 | -4.31€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 452 | -0.211 | -38.72€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 394 | -0.222 | -45.62€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 58 | -0.133 | +6.91€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 371 | -0.202 | +0.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 344 | -0.199 | -1.77€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 27 | -0.224 | +2.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1202 | -0.211 | -90.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 152 | -0.188 | +5.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 516 | +0.386 | +476.17€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 94 | +0.167 | +63.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 94 | +0.167 | +63.15€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 122 | +0.371 | +105.56€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 122 | +0.371 | +105.56€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#SOL | 300 | +0.457 | +307.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 300 | +0.457 | +307.46€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 516 | +0.386 | +476.17€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 865 | +0.046 | +82.26€ | 2 | 4 |
| ✅ STREAK_FADE_15M#15min | 865 | +0.046 | +82.26€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 323 | +0.032 | +9.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 323 | +0.032 | +9.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 70 | +0.014 | +1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 70 | +0.014 | +1.64€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 389 | +0.068 | +65.22€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 389 | +0.068 | +65.22€ | 1 | 5 |
| ✅ STREAK_FADE_5M | 3543 | -0.023 | -142.88€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3543 | -0.023 | -142.88€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 604 | -0.030 | -27.91€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 604 | -0.030 | -27.91€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 169 | -0.038 | -13.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 169 | -0.038 | -13.78€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1643 | -0.020 | -60.99€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1643 | -0.020 | -60.99€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 116 | -0.042 | -10.16€ | 2 | 0 |
| ✅ STREAK_FADE_60M#60min | 116 | -0.042 | -10.16€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 72 | -0.013 | -5.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 72 | -0.013 | -5.54€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11447 | +0.014 | +74.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11447 | +0.014 | +74.22€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2985 | +0.018 | +23.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2985 | +0.018 | +23.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2971 | +0.018 | +36.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2971 | +0.018 | +36.53€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2912 | +0.009 | -2.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2912 | +0.009 | -2.81€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2579 | +0.013 | +17.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2579 | +0.013 | +17.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 11076 | +0.015 | -34.19€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 11076 | +0.015 | -34.19€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4613 | +0.021 | +2.05€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4613 | +0.021 | +2.05€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3777 | +0.011 | -25.37€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3777 | +0.011 | -25.37€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2686 | +0.011 | -10.87€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2686 | +0.011 | -10.87€ | 1 | 0 |
| ✅ UPDOWN_GBM | 96585 | +0.059 | +9164.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 23576 | +0.082 | +5027.00€ | 0 | 10 |
| ✅ UPDOWN_GBM#240min | 2955 | +0.001 | +31.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 63992 | +0.059 | +4008.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 5724 | +0.001 | +98.83€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 8040 | +0.103 | +1468.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1780 | +0.164 | +821.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 6170 | +0.088 | +648.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 22077 | +0.057 | +1926.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3185 | +0.082 | +729.84€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 827 | +0.003 | +15.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 15379 | +0.065 | +1109.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2564 | -0.002 | +66.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 122 | -0.065 | +4.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 10386 | +0.077 | +1208.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 8539 | +0.062 | +471.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 22914 | +0.049 | +1584.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 5610 | +0.072 | +851.78€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 798 | +0.005 | +16.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 14296 | +0.050 | +688.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2097 | +0.004 | +25.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 113 | -0.100 | +2.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 20696 | +0.038 | +1145.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 6139 | +0.034 | +431.59€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 757 | -0.010 | +3.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 12636 | +0.047 | +710.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1063 | +0.003 | +7.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 101 | -0.141 | -7.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 12470 | +0.072 | +1832.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 5101 | +0.099 | +1453.86€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6972 | +0.056 | +380.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 336 | -0.101 | +0.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 954 | +0.364 | +345.11€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 954 | +0.364 | +345.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 476 | +0.362 | +165.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 476 | +0.362 | +165.49€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 478 | +0.365 | +179.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 478 | +0.365 | +179.62€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 23555 | -0.021 | +5845.38€ | 3 | 8 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 23555 | -0.021 | +5845.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4390 | -0.113 | +231.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4390 | -0.113 | +231.12€ | 3 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3057 | +0.219 | +1954.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3057 | +0.219 | +1954.21€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 6645 | -0.059 | +985.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 6645 | -0.059 | +985.47€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 6411 | -0.064 | +1213.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 6411 | -0.064 | +1213.54€ | 2 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 281 | +0.062 | +26.33€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 281 | +0.062 | +26.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 281 | +0.062 | +26.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 281 | +0.062 | +26.33€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1685 | +0.285 | +1415.55€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1685 | +0.285 | +1415.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 896 | +0.278 | +702.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 896 | +0.278 | +702.40€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 789 | +0.293 | +713.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 789 | +0.293 | +713.14€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 851 | -0.113 | -84.27€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 851 | -0.113 | -84.27€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 264 | -0.083 | -20.26€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 264 | -0.083 | -20.26€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 94 | -0.167 | -10.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 94 | -0.167 | -10.43€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 110 | -0.179 | -4.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 110 | -0.179 | -4.23€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4380 | +0.302 | +2025.13€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1656 | +0.259 | +218.05€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1686 | +0.296 | +734.22€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1038 | +0.381 | +1072.86€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.024 n=1182 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1182 IC=+0.024 PNL=+60.55€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 786 celda(s) pasan gate riguroso completo de 2835 evaluadas (n>=40) y 3944 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=6136 IC=+0.034 PNL=+431.12€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1686/15 IC=+0.296 PNL=+734.22€ | BTC: n=1656/15 IC=+0.259 PNL=+218.05€ | SOL: n=1038/15 IC=+0.381 PNL=+1072.86€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.145 n=1010/60 | contraria IC=+0.186 n=1063 | gap=-0.041 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=552, boost estimado=+0.013. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2095/40 IC=+0.004 PNL=+25.12€ | BTC#60min: n=2563/40 IC=-0.002 PNL=+66.94€ | SOL#60min: n=1062/40 IC=+0.004 PNL=+7.82€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.046 n=678063 | tras_1loss IC=+0.099 n=514468 | tras_2loss IC=+0.068 n=206502/40 | gap=-0.022 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=939 PNL=+619.74€
  - _Datos_: n=939 IC=+0.175 PNL=+619.74€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.149 > 0.08 con n=1128 PNL=+577.14€
  - _Datos_: n=1128 IC=+0.149 PNL=+577.14€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.167 > 0.08 con n=76 PNL=+40.16€
  - _Datos_: n=76 IC=+0.167 PNL=+40.16€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=3572 PNL=+1984.90€
  - _Datos_: n=3572 IC=+0.333 PNL=+1984.90€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=963 IC=+0.069 PNL=+97.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=963 IC=+0.069 PNL=+97.37€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=100 IC=+0.186 PNL=+68.50€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=100 IC=+0.186 PNL=+68.50€

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
  - _Estado_: n=3839 IC=+0.004 PNL=-7.05€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3839 IC=+0.004 PNL=-7.05€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1881 IC=-0.004 PNL=+106.93€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1881 IC=-0.004 PNL=+106.93€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1182 IC=+0.024 PNL=+60.55€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1182 IC=+0.024 PNL=+60.55€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.154 > 0.1 con n=6308 PNL=+3455.56€
  - _Datos_: n=6308 IC=+0.154 PNL=+3455.56€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3182 IC=+0.082 PNL=+730.36€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3182 IC=+0.082 PNL=+730.36€

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
  - _Estado_: n=1220 IC=+0.038 PNL=+104.45€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1220 IC=+0.038 PNL=+104.45€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=158 IC=-0.006 PNL=-1.60€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=158 IC=-0.006 PNL=-1.60€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.279 n=211) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=211 IC=+0.279 PNL=+225.02€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=1181 PNL=+495.85€
  - _Datos_: n=1181 IC=+0.124 PNL=+495.85€

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
  - _Estado_: n=39238 IC=+0.075 PNL=+5593.56€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=39238 IC=+0.075 PNL=+5593.56€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.133 < -0.1 con n=699 PNL=+103.66€
  - _Datos_: n=699 IC=-0.133 PNL=+103.66€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3615 IC=+0.067 PNL=+464.53€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3615 IC=+0.067 PNL=+464.53€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=176 IC=-0.124 PNL=-3.24€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=176 IC=-0.124 PNL=-3.24€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.1 con n=1010 PNL=+264.34€
  - _Datos_: n=1010 IC=+0.105 PNL=+264.34€

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
  - _Estado_: n=40155 IC=-0.136 PNL=+2726.58€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=40155 IC=-0.136 PNL=+2726.58€

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
  - _Estado_: n=4114 IC=+0.128 PNL=+2658.48€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4114 IC=+0.128 PNL=+2658.48€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=9888 IC=+0.059 PNL=+878.54€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=9888 IC=+0.059 PNL=+878.54€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.099 > 0.08 con n=4272 PNL=+2372.39€
  - _Datos_: n=4272 IC=+0.099 PNL=+2372.39€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=4333 PNL=-360.19€
  - _Datos_: n=4333 IC=-0.220 PNL=-360.19€

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
  - _Estado_: n=88 IC=+0.044 PNL=+15.50€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=88 IC=+0.044 PNL=+15.50€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2117) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2117 IC=+0.096 PNL=+427.27€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.412 n=658) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=658 IC=+0.412 PNL=+952.95€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=17219 IC=+0.181 PNL=-1881.46€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=17219 IC=+0.181 PNL=-1881.46€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.229 > 0.1 con n=271 PNL=+187.30€
  - _Datos_: n=271 IC=+0.229 PNL=+187.30€
