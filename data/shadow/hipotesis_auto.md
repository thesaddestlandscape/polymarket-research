# Hipótesis automáticas — 2026-11-14 14:16 UTC
_Generado por shadow_postmortem.py sobre 1333446 resoluciones (PNL=+184339.11€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=705)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=1023)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.125)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.187 (n=324)

  - _Acción_: Kelly boost +0.94€ cuando `n_total_lado` > 62.0 (IC base=+0.125)

- **PATRÓN** `banda_hit_calibrado` > `0.8128` → IC=+0.274 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8128 (IC base=+0.125)

- **PATRÓN** `banda_z` > `8.502` → IC=+0.193 (n=324)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.502 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.143 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=1056)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.125)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.302 (n=165)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=500)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=888)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.127)

- **PATRÓN** `n_total_lado` > `65.0` → IC=+0.185 (n=281)

  - _Acción_: Kelly boost +0.93€ cuando `n_total_lado` > 65.0 (IC base=+0.127)

- **PATRÓN** `banda_hit_calibrado` > `0.8124` → IC=+0.276 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8124 (IC base=+0.127)

- **PATRÓN** `banda_z` > `8.831` → IC=+0.208 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.831 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.136 (n=757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 8.0 (IC base=+0.127)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=956)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `3094.8458` → IC=+0.129 (n=748)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 3094.8458 (IC base=+0.127)

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
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=109)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=108)

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

- **PATRÓN** `py_entrada` > `0.495` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` > 0.495 (IC base=+0.153)

- **PATRÓN** `n_ballena_banda` > `26.0` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `n_ballena_banda` > 26.0 (IC base=+0.153)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.153)

- **PATRÓN** `banda_hit_calibrado` > `0.6072` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `banda_hit_calibrado` > 0.6072 (IC base=+0.153)

- **PATRÓN** `banda_z` > `2.517` → IC=+0.227 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.517 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.225 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2738.3784` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2738.3784 (IC base=+0.153)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `131.82` → IC=-0.217 (n=12086)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.82
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=36258)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `125.1` → IC=-0.257 (n=1214)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 125.1
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=3645)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.68` → IC=-0.279 (n=1231)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.68
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3696)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `116.37` → IC=-0.165 (n=3308)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 116.37
  - _Potencial_: sin este filtro IC_bueno=-0.000 (n=9924)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `152.03` → IC=-0.238 (n=3296)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 152.03
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=9888)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `127.97` → IC=-0.266 (n=2274)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.97
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=6822)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=28454)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `8183.4685` → IC=+0.157 (n=2356)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 8183.4685 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=24582)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.131 (n=29959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=22491)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=8430)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6456.6331` → IC=+0.142 (n=3267)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6456.6331 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2690)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `16321.0855` → IC=+0.180 (n=698)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 16321.0855 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1912)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.295` → IC=+0.312 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.295 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2742)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16073.2055` → IC=+0.184 (n=708)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16073.2055 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.168 (n=621)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.076)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.147 (n=1459)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.44 (IC base=+0.085)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.171 (n=5152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.172 (n=4588)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 15.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.376 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.207 (n=2458)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=2866)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.141 (n=659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.254 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=1130)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.251 (n=957)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.157 (n=738)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `libro_liquidez` < `955.8819` → IC=-0.121 (n=159)

  - _Acción_: SKIP cuando `libro_liquidez` < 955.8819
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=325)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.165 (n=467)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.55 (IC base=+0.048)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.142 (n=490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.251 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.122)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` < `7.0` → IC=-0.257 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.254 (n=116)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=24686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=20856)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.229 (n=7809)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.195)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=5627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.178 (n=5582)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` < 0.74 (IC base=+0.168)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.212 (n=3374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2249)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.247 (n=1664)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.208)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=5504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=4670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.176 (n=5650)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.73 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.184 (n=4314)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` > 0.71 (IC base=+0.175)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.253 (n=3898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.252)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.364 (n=1483)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.252)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.252)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=5391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.189 (n=4567)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 15.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1802)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.186)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=982)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=976)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.438 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4649.4982` → IC=+0.442 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4649.4982 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.440 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.446 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12510.8319` → IC=+0.444 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12510.8319 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.431 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.424)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.428 (n=387)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.424)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.443 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.424)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.430 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.424)

- **PATRÓN** `libro_liquidez` > `4814.8438` → IC=+0.431 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4814.8438 (IC base=+0.424)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.401 (n=149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.398)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.404 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.398)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.413 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.398)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `14.0` → IC=-0.324 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=37)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=36)

- **FILTRO** `libro_liquidez` < `3014.3014` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 3014.3014
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=35)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.205 (n=32258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=32457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.199)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.186 (n=4820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=10360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.206 (n=6899)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=13507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=4525)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.183 (n=13537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.197 (n=11478)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4516)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.254 (n=7460)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `hora_utc` > `3.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=12286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4682)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.202 (n=5370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=5360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.240 (n=6745)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=11645)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=12355)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.41` → IC=+0.139 (n=14193)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.41 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=5678)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.144 (n=5587)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=7147)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `4.03` → IC=+0.141 (n=7066)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 4.03 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=5967)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.138 (n=7504)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.95 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `3.09` → IC=+0.138 (n=7126)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 3.09 (IC base=+0.116)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.305 (n=1416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.284 (n=953)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.281)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.367 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.281)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.315 (n=690)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.299 (n=1013)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.295)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.295)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.369 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.347)

- **PATRÓN** `py_entrada` > `0.745` → IC=+0.393 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.745 (IC base=+0.347)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.347)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.378 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.347)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.440 (n=966)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.437 (n=315)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.433)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.442 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.433)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.449 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.439 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.439 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.421 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.397 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.407)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.447 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.407)

### FAVORITO_CONFIRMADO_SOL_ALTACONVICCION
- **FILTRO** `hora_utc` < `5.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=109)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.265 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=67)

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=69)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.233 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

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

- **FILTRO** `hora_utc` > `10.0` → IC=-0.265 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=67)

- **FILTRO** `py_entrada` > `0.715` → IC=-0.351 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.715
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=68)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.242 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=69)

- **FILTRO** `libro_liquidez` < `1798.9075` → IC=-0.233 (n=99)

  - _Acción_: SKIP cuando `libro_liquidez` < 1798.9075
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4848` → IC=+0.139 (n=18341)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4848 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=18547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=12799)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9767` → IC=+0.246 (n=6113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9767 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8011` → IC=+0.282 (n=984)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8011 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.479` → IC=+0.188 (n=9192)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.479 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6957` → IC=+0.269 (n=4944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6957 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3042` → IC=+0.249 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3042 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7483` → IC=+0.234 (n=4409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7483 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=9028)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4681.2666` → IC=+0.150 (n=6113)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4681.2666 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.123 (n=11528)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0063 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.5644` → IC=+0.144 (n=22994)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5644 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.6253` → IC=+0.190 (n=1490)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6253 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `0.8594` → IC=+0.195 (n=6311)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8594 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.235 (n=2315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` > `2.664` → IC=+0.214 (n=5347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.664 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.229 (n=15960)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.085)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3708` → IC=+0.212 (n=3902)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3708 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=1888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9849` → IC=+0.276 (n=1769)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9849 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.445` → IC=+0.277 (n=1740)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.445 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2344` → IC=+0.255 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2344 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4385` → IC=+0.211 (n=3741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4385 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=4333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.221 (n=2502)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.248 (n=1570)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.1973` → IC=+0.265 (n=2307)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1973 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=1289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.251 (n=1595)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.260 (n=3460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5667 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` < `0.0712` → IC=+0.246 (n=2970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0712 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2908` → IC=+0.252 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2908 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.4476` → IC=+0.245 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4476 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `1.8616` → IC=+0.247 (n=2204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8616 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.245 (n=4006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1775.547` → IC=+0.249 (n=2306)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1775.547 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.245 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.243)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.237 (n=1107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1108` → IC=+0.250 (n=1452)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1108 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.225 (n=2354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.8988` → IC=+0.258 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8988 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1866` → IC=+0.234 (n=1447)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1866 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.817` → IC=+0.263 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.817 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6977` → IC=+0.232 (n=2947)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6977 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.271 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.447` → IC=+0.250 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.447 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.154 (n=3552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0065 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0784` → IC=+0.159 (n=1184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0784 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=1322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7053` → IC=+0.172 (n=3551)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.7053 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.981` → IC=+0.141 (n=3242)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.981 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6304` → IC=+0.153 (n=1184)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6304 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0974` → IC=+0.156 (n=1307)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.0974 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.442` → IC=+0.143 (n=3424)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.442 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=4615)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `173.0` → IC=+0.190 (n=1121)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 173.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.206 (n=2760)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.259 (n=1608)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.97` → IC=+0.281 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.97 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.196 (n=3711)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.223 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7278` → IC=+0.211 (n=1834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7278 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5018)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2006.2984` → IC=+0.204 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2006.2984 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.224 (n=3832)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0122 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.1771` → IC=+0.235 (n=1687)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1771 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.227 (n=1742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` < `0.0488` → IC=+0.268 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0488 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.754` → IC=+0.258 (n=411)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.754 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.257 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.1586` → IC=+0.230 (n=2460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1586 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `1986.4584` → IC=+0.226 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1986.4584 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.226 (n=3683)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.221)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.177 (n=215)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=4991)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.150 (n=678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.063)

- **PATRÓN** `ibs_20min` > `0.9435` → IC=+0.238 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9435 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.1419` → IC=+0.341 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1419 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.122` → IC=+0.208 (n=1488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.122 (IC base=+0.063)

- **PATRÓN** `volumen_regimen` > `1.1103` → IC=+0.357 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1103 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` < `0.167` → IC=+0.341 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.167 (IC base=+0.063)

- **PATRÓN** `volumen_pendiente_norm` > `0.3052` → IC=+0.341 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3052 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` < `1.4175` → IC=+0.354 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4175 (IC base=+0.063)

- **PATRÓN** `volumen_spike_ratio` > `2.2842` → IC=+0.343 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2842 (IC base=+0.063)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.343 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.063)

- **PATRÓN** `ibs_20min` < `0.087` → IC=+0.185 (n=1302)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.087 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.3402` → IC=+0.164 (n=620)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.3402 (IC base=+0.055)

- **PATRÓN** `volumen_regimen` < `1.0032` → IC=+0.163 (n=2214)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.0032 (IC base=+0.055)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.210 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` < `1.7651` → IC=+0.155 (n=1616)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.7651 (IC base=+0.055)

- **PATRÓN** `volumen_spike_ratio` > `1.5053` → IC=+0.162 (n=2166)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5053 (IC base=+0.055)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.180 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=793)

- **FILTRO** `ibs_20min` < `0.2667` → IC=-0.174 (n=234)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2667
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=707)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.130 (n=4872)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=2449)

- **FILTRO** `sigma_ewma_delta_pct` > `8.309` → IC=-0.230 (n=790)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.309
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6531)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.180 (n=320)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.9668` → IC=+0.283 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9668 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.266` → IC=+0.141 (n=321)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 2.266 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.8516` → IC=+0.267 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8516 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6233` → IC=+0.290 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6233 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.283 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.290 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.449` → IC=+0.267 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.449 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.276 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.155 (n=2449)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.2 (IC base=-0.035)

- **PATRÓN** `dist_vwap_pct` > `0.2306` → IC=+0.286 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2306 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` < `0.7007` → IC=+0.295 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7007 (IC base=-0.035)

- **PATRÓN** `volumen_regimen` > `1.0529` → IC=+0.284 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0529 (IC base=-0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.0789` → IC=+0.308 (n=492)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0789 (IC base=-0.035)

- **PATRÓN** `volumen_spike_ratio` < `2.4493` → IC=+0.297 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4493 (IC base=-0.035)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7902` → IC=-0.156 (n=3751)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7902
  - _Potencial_: sin este filtro IC_bueno=+0.135 (n=1933)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.172 (n=1198)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4486)

- **FILTRO** `ibs_20min` > `0.7353` → IC=-0.191 (n=1962)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7353
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=5894)

- **PATRÓN** `ibs_20min` > `0.7902` → IC=+0.135 (n=1933)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.7902 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `0.9964` → IC=+0.351 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9964 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` < `0.2509` → IC=+0.300 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2509 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` > `0.7043` → IC=+0.318 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7043 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.1078` → IC=+0.301 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1078 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.17` → IC=+0.303 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.17 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.5796` → IC=+0.304 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5796 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.5185` → IC=+0.312 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5185 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0624` → IC=+0.280 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0624 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` < `0.6409` → IC=+0.272 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6409 (IC base=+0.005)

- **PATRÓN** `volumen_regimen` > `1.2057` → IC=+0.287 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2057 (IC base=+0.005)

- **PATRÓN** `volumen_pendiente_norm` > `0.2844` → IC=+0.289 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2844 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` < `2.4743` → IC=+0.265 (n=2181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4743 (IC base=+0.005)

- **PATRÓN** `volumen_spike_ratio` > `1.4348` → IC=+0.271 (n=2181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4348 (IC base=+0.005)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.196 (n=7963)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0108 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8667` → IC=+0.285 (n=10831)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8667 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9315` → IC=+0.302 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9315 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.468` → IC=+0.169 (n=10720)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 3.468 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6923` → IC=+0.279 (n=7888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6923 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2927` → IC=+0.297 (n=1970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2927 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6429` → IC=+0.286 (n=4623)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6429 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.309 (n=13505)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.157 (n=7711)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0103 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.5192` → IC=+0.172 (n=20349)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5192 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` < `0.6969` → IC=+0.280 (n=3404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6969 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.285 (n=2579)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.329 (n=1718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` < `1.4523` → IC=+0.305 (n=3814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4523 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `2.2774` → IC=+0.304 (n=5187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2774 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.311 (n=11428)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.084)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8036` → IC=-0.137 (n=4238)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8036
  - _Potencial_: sin este filtro IC_bueno=+0.303 (n=2186)

- **FILTRO** `ibs_20min` > `0.7122` → IC=-0.238 (n=1421)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7122
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=4271)

- **FILTRO** `sigma_ewma_delta_pct` > `4.08` → IC=-0.238 (n=1222)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.08
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=4470)

- **PATRÓN** `ibs_20min` > `0.8036` → IC=+0.303 (n=2186)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8036 (IC base=+0.013)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.962` → IC=+0.190 (n=2137)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.962 (IC base=+0.013)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.332 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.284 (n=679)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.013)

- **PATRÓN** `volumen_spike_ratio` > `2.242` → IC=+0.305 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.242 (IC base=+0.013)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.318 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.013)

- **PATRÓN** `ibs_20min` < `0.1731` → IC=+0.172 (n=1424)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1731 (IC base=-0.020)

- **PATRÓN** `volumen_pendiente_norm` < `0.1515` → IC=+0.396 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1515 (IC base=-0.020)

- **PATRÓN** `volumen_spike_ratio` < `1.4268` → IC=+0.420 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4268 (IC base=-0.020)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.393 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.020)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.3005` → IC=+0.226 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3005 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` < `1.1954` → IC=+0.211 (n=2340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1954 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `0.6949` → IC=+0.221 (n=2091)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6949 (IC base=+0.010)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.248 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` < `1.4165` → IC=+0.230 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4165 (IC base=+0.010)

- **PATRÓN** `volumen_spike_ratio` > `2.4708` → IC=+0.214 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4708 (IC base=+0.010)

- **PATRÓN** `ballena_activa_n` < `257.0` → IC=+0.244 (n=1541)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 257.0 (IC base=+0.010)

- **PATRÓN** `volumen_regimen` > `1.0184` → IC=+0.266 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0184 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.306 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5262` → IC=+0.262 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5262 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1503` → IC=+0.264 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1503 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `183.0` → IC=+0.279 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 183.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.323 (n=1510)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.588` → IC=+0.306 (n=2248)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.588 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.296 (n=2931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2535` → IC=+0.298 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2535 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4006)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `2008.8484` → IC=+0.296 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2008.8484 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.305 (n=2046)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.331 (n=2030)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.179` → IC=+0.324 (n=1339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.179 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.327 (n=1164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1489` → IC=+0.318 (n=2029)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1489 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.104` → IC=+0.312 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.104 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.415` → IC=+0.307 (n=3155)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.415 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1991` → IC=+0.307 (n=3005)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1991 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3448` → IC=+0.317 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3448 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.7408` → IC=+0.323 (n=1333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7408 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.308 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1986.7` → IC=+0.315 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1986.7 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.311 (n=2582)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7183` → IC=-0.179 (n=1507)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7183
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=4523)

- **PATRÓN** `dist_vwap_pct` > `0.1466` → IC=+0.237 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1466 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1586` → IC=+0.238 (n=2154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1586 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.1617` → IC=+0.238 (n=2257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1617 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1025` → IC=+0.245 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1025 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.421` → IC=+0.243 (n=2092)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.421 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.256 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.7363` → IC=+0.262 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7363 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` < `1.1877` → IC=+0.264 (n=1556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1877 (IC base=+0.007)

- **PATRÓN** `volumen_regimen` > `0.6165` → IC=+0.257 (n=1555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6165 (IC base=+0.007)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.307 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` < `1.7856` → IC=+0.290 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7856 (IC base=+0.007)

- **PATRÓN** `volumen_spike_ratio` > `2.4276` → IC=+0.280 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4276 (IC base=+0.007)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.284 (n=1519)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.007)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7429` → IC=-0.247 (n=2461)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7429
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2466)

- **FILTRO** `ibs_20min` > `0.6154` → IC=-0.236 (n=1167)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6154
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=3507)

- **FILTRO** `sigma_ewma_delta_pct` > `8.285` → IC=-0.269 (n=534)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.285
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=4140)

- **PATRÓN** `ibs_20min` > `0.7429` → IC=+0.312 (n=2466)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7429 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `1.0465` → IC=+0.354 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0465 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.448` → IC=+0.157 (n=1997)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 2.448 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8384` → IC=+0.346 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8384 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `0.6934` → IC=+0.336 (n=1604)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6934 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.1578` → IC=+0.335 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1578 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2751` → IC=+0.371 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2751 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.4268` → IC=+0.361 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4268 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.355 (n=1559)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.157 (n=3507)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.6154 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.738` → IC=+0.127 (n=3666)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 4.738 (IC base=+0.058)

- **PATRÓN** `volumen_regimen` < `0.6914` → IC=+0.280 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6914 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.0707` → IC=+0.297 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0707 (IC base=+0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.8006` → IC=+0.281 (n=1151)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8006 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.288 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.058)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.359 (n=2272)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2565)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.316 (n=1767)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` > `0.6571` → IC=+0.343 (n=2543)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6571 (IC base=+0.316)

- **PATRÓN** `dist_vwap_pct` > `0.212` → IC=+0.335 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.212 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.813` → IC=+0.337 (n=965)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.813 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `0.6288` → IC=+0.326 (n=2541)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6288 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.349 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `1.5287` → IC=+0.328 (n=2189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5287 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2994.8954` → IC=+0.329 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2994.8954 (IC base=+0.316)

- **PATRÓN** `ballena_activa_n` < `39.0` → IC=+0.342 (n=2295)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 39.0 (IC base=+0.316)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.332 (n=2725)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.315 (n=1327)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.331 (n=2726)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3846 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.608` → IC=+0.324 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.608 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.318 (n=1201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `1.2052` → IC=+0.343 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2052 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.368 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` < `1.4131` → IC=+0.322 (n=848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4131 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `2.1415` → IC=+0.317 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1415 (IC base=+0.315)

- **PATRÓN** `libro_liquidez` > `2981.7056` → IC=+0.317 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2981.7056 (IC base=+0.315)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.222 (n=5892)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1232` → IC=+0.191 (n=7773)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1232 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.184 (n=18345)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5376` → IC=+0.229 (n=17656)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5376 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1624` → IC=+0.205 (n=6612)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1624 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.747` → IC=+0.259 (n=3449)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.747 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1749` → IC=+0.152 (n=11767)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1749 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.152 (n=11766)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6226 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.203 (n=2548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5994` → IC=+0.185 (n=5726)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5994 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.191 (n=16579)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 86.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.193 (n=7689)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0059 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.187 (n=11637)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0079 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.0817` → IC=+0.223 (n=5821)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0817 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=6537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.5257` → IC=+0.240 (n=17445)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5257 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.494` → IC=+0.189 (n=2764)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.494 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.507` → IC=+0.192 (n=15552)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.507 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `1.1834` → IC=+0.165 (n=12399)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1834 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.220 (n=2619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.6283` → IC=+0.196 (n=5544)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6283 (IC base=+0.185)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.200 (n=16405)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.185)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.263 (n=970)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.257 (n=1275)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.9426` → IC=+0.292 (n=1931)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9426 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.46` → IC=+0.328 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.46 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.284 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.8356` → IC=+0.225 (n=1844)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8356 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4352` → IC=+0.226 (n=2765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4352 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3234)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2035.24` → IC=+0.226 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2035.24 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.259 (n=2392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.259 (n=1087)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.0974` → IC=+0.310 (n=1052)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0974 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=2463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=2183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.4403` → IC=+0.274 (n=2389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4403 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.0993` → IC=+0.258 (n=2099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0993 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.302` → IC=+0.273 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.302 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.4466` → IC=+0.276 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4466 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6922` → IC=+0.257 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6922 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.266 (n=1723)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1774.8902` → IC=+0.265 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1774.8902 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.256 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.257)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.196 (n=897)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0032 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.0648` → IC=+0.177 (n=897)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.0648 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2813)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.2579` → IC=+0.205 (n=2686)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2579 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1841` → IC=+0.213 (n=1311)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1841 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.619` → IC=+0.210 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.619 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6259` → IC=+0.134 (n=897)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6259 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` > `1.0504` → IC=+0.134 (n=1218)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.0504 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.168 (n=413)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4059` → IC=+0.134 (n=881)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.4059 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `2.4602` → IC=+0.145 (n=880)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 2.4602 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `396.0` → IC=+0.133 (n=2613)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 396.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.172 (n=2878)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0065 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.2421` → IC=+0.176 (n=2533)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2421 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=1361)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.6098` → IC=+0.210 (n=2878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6098 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.899` → IC=+0.176 (n=538)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.899 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.03` → IC=+0.156 (n=2507)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.03 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2012` → IC=+0.162 (n=2878)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2012 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.2285` → IC=+0.155 (n=3052)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.2285 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.4684` → IC=+0.155 (n=2752)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4684 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.200 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 207.0 (IC base=+0.151)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.224 (n=1996)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2509` → IC=+0.232 (n=1995)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2509 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=3119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.290 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.044` → IC=+0.306 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.044 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.210 (n=2609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.239 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7105` → IC=+0.224 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7105 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3621)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1996.5606` → IC=+0.224 (n=997)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1996.5606 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.246 (n=2659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0119 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.4164` → IC=+0.261 (n=2339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4164 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.279 (n=1017)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0419` → IC=+0.291 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0419 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.888` → IC=+0.277 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.888 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.354` → IC=+0.287 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.354 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7676` → IC=+0.239 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7676 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1788` → IC=+0.251 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1788 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1873.1584` → IC=+0.246 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1873.1584 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.239 (n=1717)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.197 (n=976)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0038 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0786` → IC=+0.182 (n=972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.0786 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=3019)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2458` → IC=+0.189 (n=2914)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2458 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1398` → IC=+0.185 (n=1648)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1398 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.227` → IC=+0.201 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.227 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.8387` → IC=+0.138 (n=1943)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8387 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.169 (n=439)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.8053` → IC=+0.127 (n=1903)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8053 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.5053` → IC=+0.137 (n=952)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5053 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `6876.1912` → IC=+0.198 (n=1321)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6876.1912 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.127 (n=2861)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 125.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.165 (n=2731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0067 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.4035` → IC=+0.148 (n=3103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.4035 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1477)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.6725` → IC=+0.187 (n=3103)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6725 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.209` → IC=+0.141 (n=741)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 9.209 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `0.8521` → IC=+0.151 (n=2070)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8521 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.176 (n=461)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.1981` → IC=+0.132 (n=2594)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.1981 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` > `1.5151` → IC=+0.134 (n=2634)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 1.5151 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6363.1832` → IC=+0.191 (n=1407)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6363.1832 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.158 (n=982)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 48.0 (IC base=+0.131)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.158 (n=1472)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0114 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4706` → IC=+0.205 (n=3255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4706 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.1998` → IC=+0.188 (n=1717)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1998 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.96` → IC=+0.287 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.96 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.0272` → IC=+0.129 (n=2856)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0272 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.122 (n=3309)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.7791` → IC=+0.123 (n=2099)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7791 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2676.0135` → IC=+0.198 (n=1472)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 2676.0135 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.130 (n=1083)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 16.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0119` → IC=+0.144 (n=3394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0119 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.1144` → IC=+0.164 (n=1134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1144 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.136 (n=3462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6489` → IC=+0.220 (n=3394)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6489 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.237` → IC=+0.142 (n=3005)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 2.237 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1765` → IC=+0.127 (n=3395)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1765 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.859` → IC=+0.125 (n=2262)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.859 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1619` → IC=+0.124 (n=3342)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1619 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.151 (n=474)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.139 (n=1071)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.4427` → IC=+0.134 (n=1071)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4427 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2565.6226` → IC=+0.189 (n=1539)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2565.6226 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.129 (n=3209)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 44.0 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.248 (n=2922)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1653` → IC=+0.244 (n=1286)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1653 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2637)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.258 (n=2925)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `1.1272` → IC=+0.237 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1272 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.527` → IC=+0.258 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.527 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.237 (n=2922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6199 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2347` → IC=+0.268 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2347 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.230 (n=2851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4318` → IC=+0.232 (n=2851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4318 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2595.188` → IC=+0.231 (n=1948)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2595.188 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.242 (n=1333)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0123 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0172` → IC=+0.245 (n=2018)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0172 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.5884` → IC=+0.250 (n=3026)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5884 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.252 (n=1476)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=1357)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0385` → IC=+0.301 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0385 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `1.1322` → IC=+0.263 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1322 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.103` → IC=+0.269 (n=579)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.103 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` < `0.8684` → IC=+0.243 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8684 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.243 (n=3026)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.293 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `2.5149` → IC=+0.239 (n=2860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5149 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.241 (n=2555)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.241)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.209 (n=1536)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1358` → IC=+0.172 (n=2023)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1358 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.169 (n=4792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.4241` → IC=+0.202 (n=4104)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4241 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.223` → IC=+0.177 (n=1713)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.223 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.505` → IC=+0.211 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.505 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8604` → IC=+0.167 (n=2763)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8604 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.1935` → IC=+0.163 (n=1382)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1935 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.174 (n=1206)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.5279` → IC=+0.161 (n=1972)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5279 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.809` → IC=+0.160 (n=2988)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 1.809 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.157 (n=5098)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.02 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7348.1594` → IC=+0.186 (n=2083)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7348.1594 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.3824` → IC=+0.176 (n=3342)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.3824 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.139 (n=2197)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 23.0 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.197 (n=1148)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0061 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.3302` → IC=+0.199 (n=1149)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3302 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.217 (n=1035)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.6191` → IC=+0.242 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6191 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.3093` → IC=+0.218 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3093 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.946` → IC=+0.213 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.946 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.6292` → IC=+0.207 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6292 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.2153` → IC=+0.188 (n=1292)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` < 0.2153 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0913` → IC=+0.200 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0913 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `2.1675` → IC=+0.198 (n=991)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1675 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `13750.9538` → IC=+0.192 (n=765)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 13750.9538 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.161 (n=481)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0031 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.2092` → IC=+0.198 (n=634)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.2092 (IC base=+0.080)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.174 (n=623)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 166.0 (IC base=+0.080)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.231 (n=611)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.2101` → IC=+0.157 (n=924)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2101 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=1436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.7829` → IC=+0.268 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7829 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.817` → IC=+0.192 (n=225)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.817 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.884` → IC=+0.207 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.884 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8322` → IC=+0.165 (n=924)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8322 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1605` → IC=+0.155 (n=462)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.1605 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.200 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `1.776` → IC=+0.174 (n=911)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 1.776 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7958.7991` → IC=+0.176 (n=628)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 7958.7991 (IC base=+0.154)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.152 (n=458)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 31.0 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.126 (n=909)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0053 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.0867` → IC=+0.208 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0867 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6774` → IC=+0.132 (n=598)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.6774 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `7848.8621` → IC=+0.151 (n=617)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7848.8621 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `61.0` → IC=+0.121 (n=881)

  - _Acción_: Kelly boost +0.60€ cuando `ballena_activa_n` < 61.0 (IC base=+0.094)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.144 (n=787)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0093 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.159 (n=823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 11.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.189 (n=1055)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5357 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.932` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.932 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.829` → IC=+0.225 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.829 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.0426` → IC=+0.131 (n=1039)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.0426 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.7001` → IC=+0.125 (n=1054)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 0.7001 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.223` → IC=+0.146 (n=207)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.223 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4112` → IC=+0.148 (n=382)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4112 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2751.7394` → IC=+0.159 (n=535)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2751.7394 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5517` → IC=+0.163 (n=1156)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.5517 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `2632.9653` → IC=+0.167 (n=595)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2632.9653 (IC base=+0.082)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0155` → IC=+0.241 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0155 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.212 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9524 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.2419` → IC=+0.192 (n=219)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2419 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.237` → IC=+0.202 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.237 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` > `1.2169` → IC=+0.253 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2169 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0812` → IC=+0.219 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0812 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `2.129` → IC=+0.198 (n=355)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.129 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `1.4102` → IC=+0.196 (n=403)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.4102 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.199 (n=453)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.03 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2705.7218` → IC=+0.217 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2705.7218 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.172 (n=477)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0105 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.5204` → IC=+0.160 (n=418)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5204 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.194 (n=230)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.3415` → IC=+0.161 (n=317)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3415 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.1049` → IC=+0.158 (n=475)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.1049 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `1.1718` → IC=+0.281 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1718 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.954` → IC=+0.157 (n=458)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 2.954 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2353` → IC=+0.173 (n=475)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2353 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.1126` → IC=+0.168 (n=438)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1126 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4792` → IC=+0.210 (n=153)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4792 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.6395` → IC=+0.158 (n=153)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.6395 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.170 (n=461)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 20.0 (IC base=+0.153)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.228 (n=7749)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=24219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.226 (n=23209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4286 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.8834` → IC=+0.213 (n=2677)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8834 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.933` → IC=+0.259 (n=5702)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.933 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2126` → IC=+0.160 (n=15634)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2126 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2407` → IC=+0.209 (n=4170)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2407 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6231` → IC=+0.193 (n=7557)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6231 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.201 (n=21871)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.199 (n=7137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.207 (n=7138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.1469` → IC=+0.203 (n=9421)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1469 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=7997)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.5931` → IC=+0.244 (n=21408)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5931 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.52` → IC=+0.203 (n=19903)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.52 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.7007` → IC=+0.176 (n=6324)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.7007 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.256 (n=2939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.6249` → IC=+0.211 (n=6843)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6249 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.213 (n=20287)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.197)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.275 (n=1236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1791)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8629` → IC=+0.296 (n=2474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8629 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.841` → IC=+0.342 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.841 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2327` → IC=+0.288 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2327 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4492` → IC=+0.232 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4492 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2913` → IC=+0.241 (n=1625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2913 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=4106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2027.569` → IC=+0.238 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2027.569 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.249 (n=2305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.269 (n=3331)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.268)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.269 (n=1511)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.268)

- **PATRÓN** `drift_60min` |x|≤ `0.1233` → IC=+0.295 (n=1465)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1233 (IC base=+0.268)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.269 (n=3457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.268)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.272 (n=3013)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.268)

- **PATRÓN** `ibs_20min` < `0.5508` → IC=+0.286 (n=3330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5508 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` < `0.0977` → IC=+0.270 (n=3031)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0977 (IC base=+0.268)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.290 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` < `1.5659` → IC=+0.272 (n=1408)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5659 (IC base=+0.268)

- **PATRÓN** `volumen_spike_ratio` > `2.6462` → IC=+0.280 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6462 (IC base=+0.268)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.274 (n=2388)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.268)

- **PATRÓN** `libro_liquidez` > `1775.397` → IC=+0.276 (n=2220)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1775.397 (IC base=+0.268)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.278 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.268)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.177 (n=1273)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0032 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.147 (n=1270)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=3969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.1945` → IC=+0.187 (n=3806)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.1945 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.6809` → IC=+0.207 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6809 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.099` → IC=+0.167 (n=608)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.099 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.6354` → IC=+0.155 (n=1269)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6354 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.0679` → IC=+0.144 (n=1726)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0679 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2712` → IC=+0.186 (n=537)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2712 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.1707` → IC=+0.143 (n=3291)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.1707 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.5157` → IC=+0.144 (n=3340)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 1.5157 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `296.0` → IC=+0.153 (n=2462)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 296.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.164 (n=3315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0065 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.0803` → IC=+0.169 (n=1106)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0803 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=1214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `ibs_20min` < `0.6776` → IC=+0.188 (n=3312)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6776 (IC base=+0.141)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.005` → IC=+0.143 (n=2994)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.005 (IC base=+0.141)

- **PATRÓN** `volumen_regimen` < `1.043` → IC=+0.153 (n=2914)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.043 (IC base=+0.141)

- **PATRÓN** `volumen_pendiente_norm` > `0.2206` → IC=+0.192 (n=611)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2206 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` < `2.4301` → IC=+0.147 (n=3202)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4301 (IC base=+0.141)

- **PATRÓN** `volumen_spike_ratio` > `1.7697` → IC=+0.146 (n=2134)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.7697 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=4306)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.166 (n=1057)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 220.0 (IC base=+0.141)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.244 (n=1292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=4056)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=3465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.979` → IC=+0.321 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.979 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.1319` → IC=+0.227 (n=3669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1319 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.3503` → IC=+0.229 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3503 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `2.7432` → IC=+0.242 (n=1716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7432 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=4680)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2005.4352` → IC=+0.240 (n=1290)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2005.4352 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.249 (n=3266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1796` → IC=+0.261 (n=1631)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1796 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1410)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.303 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.032` → IC=+0.304 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.032 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3478` → IC=+0.304 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3478 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1746` → IC=+0.256 (n=2384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1746 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1980.8032` → IC=+0.257 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1980.8032 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.249 (n=3112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.194 (n=1341)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.4358` → IC=+0.146 (n=4017)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.4358 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.8826` → IC=+0.270 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8826 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.169 (n=1776)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.068` → IC=+0.168 (n=607)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.068 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.8574` → IC=+0.155 (n=2678)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8574 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2324` → IC=+0.192 (n=713)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2324 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `1.5144` → IC=+0.156 (n=1729)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5144 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `2.1579` → IC=+0.142 (n=1781)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1579 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `5639.2506` → IC=+0.229 (n=1821)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5639.2506 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.147 (n=2596)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 86.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.171 (n=2968)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0068 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.4435` → IC=+0.159 (n=3373)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4435 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1243)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.7057` → IC=+0.199 (n=3375)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7057 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.826` → IC=+0.150 (n=495)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 10.826 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.029` → IC=+0.153 (n=2947)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.029 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `0.6881` → IC=+0.165 (n=1484)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6881 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.212 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.2041` → IC=+0.152 (n=2870)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.2041 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.5251` → IC=+0.155 (n=2913)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5251 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `6563.2951` → IC=+0.222 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6563.2951 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.173 (n=1104)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 57.0 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.153 (n=1364)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0127 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.148 (n=2880)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.4286` → IC=+0.188 (n=4088)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.4286 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0085` → IC=+0.202 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0085 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.234` → IC=+0.274 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.234 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8738` → IC=+0.133 (n=2721)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8738 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.121 (n=3876)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.4914` → IC=+0.121 (n=3985)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4914 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2725.4543` → IC=+0.242 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2725.4543 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.156 (n=3374)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0109 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1394` → IC=+0.154 (n=1276)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1394 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.6667` → IC=+0.219 (n=3846)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6667 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.039` → IC=+0.154 (n=3707)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.039 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `0.6386` → IC=+0.151 (n=1277)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.6386 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.197 (n=675)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `1.4377` → IC=+0.161 (n=1214)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.4377 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `2623.7268` → IC=+0.214 (n=1276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2623.7268 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.144 (n=3658)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 49.0 (IC base=+0.132)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.259 (n=3733)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.246 (n=3903)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.239)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.242 (n=3347)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` > `0.6146` → IC=+0.272 (n=3333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6146 (IC base=+0.239)

- **PATRÓN** `dist_vwap_pct` > `0.196` → IC=+0.253 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.196 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.11` → IC=+0.289 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.11 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` < `1.2177` → IC=+0.240 (n=3731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2177 (IC base=+0.239)

- **PATRÓN** `volumen_regimen` > `0.6433` → IC=+0.244 (n=3731)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6433 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2395` → IC=+0.256 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2395 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.4995` → IC=+0.256 (n=1217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4995 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `2870.0504` → IC=+0.246 (n=1692)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2870.0504 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.268 (n=1289)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=3637)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.14` → IC=+0.308 (n=1708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.14 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.063` → IC=+0.277 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.063 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.7155` → IC=+0.246 (n=1702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7155 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2132` → IC=+0.264 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2132 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.310 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4324` → IC=+0.248 (n=3653)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4324 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `2973.1101` → IC=+0.248 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2973.1101 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.231 (n=5973)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.5204` → IC=+0.232 (n=6787)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5204 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=6844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_20min` > `0.9286` → IC=+0.259 (n=2263)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9286 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.574` → IC=+0.229 (n=3382)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.574 (IC base=+0.223)

- **PATRÓN** `volumen_regimen` < `0.7032` → IC=+0.233 (n=2132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7032 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.224 (n=6347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=+0.223)

- **PATRÓN** `volumen_pendiente_norm` > `0.1649` → IC=+0.231 (n=1913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1649 (IC base=+0.223)

- **PATRÓN** `volumen_spike_ratio` < `2.2575` → IC=+0.228 (n=5880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.2575 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.227 (n=4903)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `3701.6132` → IC=+0.230 (n=4525)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3701.6132 (IC base=+0.223)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.238 (n=1538)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.5021` → IC=+0.213 (n=4602)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5021 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.209 (n=1765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.215 (n=2066)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_20min` < `0.0881` → IC=+0.215 (n=1534)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0881 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.6719` → IC=+0.211 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6719 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.764` → IC=+0.215 (n=4153)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.764 (IC base=+0.202)

- **PATRÓN** `volumen_regimen` < `1.0952` → IC=+0.208 (n=3821)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0952 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.204 (n=4245)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.202)

- **PATRÓN** `volumen_pendiente_norm` > `0.2231` → IC=+0.207 (n=926)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2231 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` < `1.5327` → IC=+0.206 (n=1996)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5327 (IC base=+0.202)

- **PATRÓN** `volumen_spike_ratio` > `2.1939` → IC=+0.211 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1939 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=6038)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `ballena_activa_n` < `30.0` → IC=+0.227 (n=2022)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 30.0 (IC base=+0.202)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.277 (n=818)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.270)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.272 (n=929)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.298 (n=310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.277 (n=986)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.270)

- **PATRÓN** `ibs_20min` < `0.8318` → IC=+0.279 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.8318 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` < `0.6688` → IC=+0.278 (n=1080)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6688 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.118` → IC=+0.300 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.118 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` < `1.2246` → IC=+0.272 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2246 (IC base=+0.270)

- **PATRÓN** `volumen_regimen` > `0.8784` → IC=+0.292 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8784 (IC base=+0.270)

- **PATRÓN** `volumen_pendiente_norm` > `0.2882` → IC=+0.358 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2882 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.277 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.270)

- **PATRÓN** `volumen_spike_ratio` > `2.1895` → IC=+0.270 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1895 (IC base=+0.270)

- **PATRÓN** `libro_liquidez` > `12915.1097` → IC=+0.279 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12915.1097 (IC base=+0.270)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.263 (n=509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3854` → IC=+0.188 (n=1523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3854 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.180 (n=570)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.197 (n=671)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1382 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.6955` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6955 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.86` → IC=+0.187 (n=1760)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 10.86 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.091` → IC=+0.188 (n=1340)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.091 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` < `0.2705` → IC=+0.177 (n=1798)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.2705 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.194 (n=466)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.4122` → IC=+0.194 (n=505)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4122 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `1.8038` → IC=+0.179 (n=1010)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.8038 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `14605.0565` → IC=+0.177 (n=691)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 14605.0565 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `691.0` → IC=+0.187 (n=1479)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 691.0 (IC base=+0.175)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.238 (n=345)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.5997` → IC=+0.212 (n=1031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5997 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.231 (n=943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.7126` → IC=+0.212 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7126 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.252 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.277` → IC=+0.246 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.277 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2042` → IC=+0.244 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2042 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.7931` → IC=+0.215 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7931 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2777.94` → IC=+0.240 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2777.94 (IC base=+0.209)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.221 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.224 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.300 (n=53)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.228)

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

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.228)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.221 (n=1828)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.4578` → IC=+0.216 (n=1827)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4578 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=638)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` < `0.4751` → IC=+0.218 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4751 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.1447` → IC=+0.211 (n=1827)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1447 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.374` → IC=+0.216 (n=1851)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.374 (IC base=+0.209)

- **PATRÓN** `volumen_regimen` < `0.8663` → IC=+0.217 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8663 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` < `0.1019` → IC=+0.212 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1019 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.1614` → IC=+0.210 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1614 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` < `1.403` → IC=+0.227 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.403 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4939` → IC=+0.210 (n=1597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4939 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=1813)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.242 (n=479)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.49` → IC=+0.220 (n=1432)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.49 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.205 (n=533)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.214 (n=974)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.3949` → IC=+0.201 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3949 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.6121` → IC=+0.208 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6121 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` > `0.6286` → IC=+0.218 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6286 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.261` → IC=+0.204 (n=1307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.261 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `1.2516` → IC=+0.208 (n=1432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2516 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `0.7214` → IC=+0.200 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7214 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.226 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `1.412` → IC=+0.206 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.412 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` > `1.7864` → IC=+0.204 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7864 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `6540.7204` → IC=+0.208 (n=1279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6540.7204 (IC base=+0.200)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.240 (n=514)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.246 (n=1048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.9855` → IC=+0.291 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9855 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.8127` → IC=+0.238 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8127 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.168` → IC=+0.244 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.168 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.701` → IC=+0.248 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.701 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` < `0.1039` → IC=+0.220 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1039 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2722` → IC=+0.224 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2722 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `2.1734` → IC=+0.226 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1734 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `4364.3329` → IC=+0.253 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4364.3329 (IC base=+0.215)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.256 (n=534)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.6329` → IC=+0.248 (n=801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6329 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.236 (n=741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.261 (n=566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.6404` → IC=+0.261 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6404 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.926` → IC=+0.254 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.926 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `0.7541` → IC=+0.244 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7541 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `1.2706` → IC=+0.240 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2706 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` < `0.0822` → IC=+0.247 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0822 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.2105` → IC=+0.265 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2105 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `3869.3685` → IC=+0.254 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3869.3685 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.271 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.235)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.150 (n=778)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0038 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.7482` → IC=+0.184 (n=1491)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7482 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1475` → IC=+0.143 (n=1078)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1475 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.347` → IC=+0.141 (n=494)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 10.347 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.257 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.054)

- **PATRÓN** `volumen_pendiente_norm` > `0.1476` → IC=+0.140 (n=431)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.1476 (IC base=+0.054)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.127 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0054 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.5427` → IC=+0.161 (n=630)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.5427 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.168 (n=323)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.069)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.132 (n=283)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0035 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.0674` → IC=+0.249 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0674 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.151 (n=127)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.046)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` < `0.5264` → IC=-0.121 (n=317)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5264
  - _Potencial_: sin este filtro IC_bueno=+0.165 (n=646)

- **FILTRO** `ibs_20min` > `0.6646` → IC=-0.155 (n=166)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6646
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=499)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.150 (n=332)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0042 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.122 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 15.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.5264` → IC=+0.165 (n=646)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.5264 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.129` → IC=+0.168 (n=344)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.129 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.613` → IC=+0.203 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.613 (IC base=+0.068)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.1087` → IC=+0.261 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1087 (IC base=+0.032)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.72` → IC=+0.138 (n=539)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.72 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.728` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.728 (IC base=+0.027)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.181 (n=334)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0097 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.188 (n=469)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.4857 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.838` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.838 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `1.1082` → IC=+0.196 (n=156)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 1.1082 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.1084` → IC=+0.165 (n=177)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1084 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.5364` → IC=+0.155 (n=146)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.5364 (IC base=+0.086)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.126 (n=220)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.03 (IC base=+0.086)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.302 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=292)

- **FILTRO** `dist_vwap_pct` > `0.2381` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=371)

- **FILTRO** `volumen_regimen` < `0.8582` → IC=-0.306 (n=127)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8582
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=259)

- **FILTRO** `libro_liquidez` < `903.3651` → IC=-0.235 (n=96)

  - _Acción_: SKIP cuando `libro_liquidez` < 903.3651
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=290)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.309 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=187)

- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.310 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=-0.256 (n=223)

- **FILTRO** `dist_vwap_pct` > `0.4388` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4388
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=317)

- **FILTRO** `volumen_pendiente_norm` > `0.0453` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0453
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=216)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `9.679` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.679
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=96)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.297 (n=57)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=57)

- **FILTRO** `ibs_20min` > `0.7502` → IC=-0.265 (n=49)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7502
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=98)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=111)

- **FILTRO** `volumen_spike_ratio` > `1.817` → IC=-0.325 (n=38)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 1.817
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=76)

- **FILTRO** `libro_liquidez` < `5528.1887` → IC=-0.259 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 5528.1887
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=37)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `drift_60min` |x|> `0.1568` → IC=-0.324 (n=32)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1568
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=100)

- **FILTRO** `hora_utc` < `2.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=106)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.368 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=94)

- **FILTRO** `ibs_20min` > `0.7557` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7557
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=98)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.284 (n=72)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.295 (n=115)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.361 (n=34)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=105)

- **FILTRO** `volumen_pendiente_norm` > `0.1196` → IC=-0.265 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1196
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=83)

- **FILTRO** `volumen_spike_ratio` < `1.5847` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.5847
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=87)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=110)

- **FILTRO** `sigma_ewma_delta_pct` > `4.698` → IC=-0.382 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.698
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=45)

- **FILTRO** `volumen_regimen` < `0.914` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.914
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=41)

- **FILTRO** `libro_spread` > `0.05` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.05
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=41)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.250 (n=250)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.191 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 15.0 (IC base=+0.147)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.185 (n=747)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.6757 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.8076` → IC=+0.287 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8076 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.59` → IC=+0.157 (n=406)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 3.59 (IC base=+0.147)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.185 (n=249)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6242 (IC base=+0.147)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.180 (n=557)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.147)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.202 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.749` → IC=+0.144 (n=262)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 8.749 (IC base=+0.031)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.725` → IC=-0.167 (n=73)

  - _Acción_: SKIP cuando `ibs_20min` < 0.725
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=222)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.149 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0065 (IC base=+0.042)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.125 (n=198)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` > 0.7913 (IC base=+0.042)

- **PATRÓN** `dist_vwap_pct` > `0.6315` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6315 (IC base=+0.042)

- **PATRÓN** `ibs_20min` < `0.2413` → IC=+0.145 (n=415)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.2413 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2735` → IC=+0.144 (n=71)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2735 (IC base=+0.087)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1814` → IC=-0.167 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1814
  - _Potencial_: sin este filtro IC_bueno=+0.141 (n=260)

- **PATRÓN** `drift_60min` |x|≤ `0.1025` → IC=+0.133 (n=107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.1025 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.155 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.135 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` > `0.7163` → IC=+0.145 (n=243)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.7163 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.38` → IC=+0.142 (n=252)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 9.38 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1915 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.1814` → IC=+0.141 (n=260)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` < 0.1814 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `2.0546` → IC=+0.154 (n=189)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.0546 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=209)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.619` → IC=+0.209 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.619 (IC base=+0.013)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.0769` → IC=-0.231 (n=102)

  - _Acción_: SKIP cuando `ibs_20min` > 0.0769
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=103)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.286 (n=129)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.282 (n=260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.255)

- **PATRÓN** `ibs_20min` > `0.5882` → IC=+0.281 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5882 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` > `0.7067` → IC=+0.397 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7067 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.797` → IC=+0.341 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.797 (IC base=+0.255)

- **PATRÓN** `volumen_regimen` < `0.5991` → IC=+0.314 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5991 (IC base=+0.255)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` < `1.3986` → IC=+0.346 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3986 (IC base=+0.255)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.295 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.255)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.323 (n=128)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.327)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.327)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.412 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.327)

- **PATRÓN** `drift_60min` |x|≤ `0.7805` → IC=+0.382 (n=83)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7805 (IC base=+0.327)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.389 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.327)

- **PATRÓN** `ballena_activa_n` < `1107.0` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1107.0 (IC base=+0.327)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.290 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.269)

- **PATRÓN** `elapsed_s` > `227.0` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 227.0 (IC base=+0.269)

- **PATRÓN** `drift_15min` |x|≤ `2.2146` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2146 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.313 (n=73)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.269)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.323 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.368 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.269)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.323 (n=128)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3645` → IC=+0.337 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3645 (IC base=+0.327)

- **PATRÓN** `elapsed_s` > `207.7` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 207.7 (IC base=+0.327)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.412 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.327)

- **PATRÓN** `drift_60min` |x|≤ `0.7805` → IC=+0.382 (n=83)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.7805 (IC base=+0.327)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.389 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.327)

- **PATRÓN** `ballena_activa_n` < `1107.0` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1107.0 (IC base=+0.327)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.290 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.269)

- **PATRÓN** `elapsed_s` > `227.0` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 227.0 (IC base=+0.269)

- **PATRÓN** `drift_15min` |x|≤ `2.2146` → IC=+0.327 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2146 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.6484` → IC=+0.313 (n=73)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6484 (IC base=+0.269)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.323 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.269)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.368 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.269)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=1479)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.097)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.125 (n=1479)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.097)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=255)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=255)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=1047)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 2.0 (IC base=+0.073)

- **PATRÓN** `liq_usd_total` > `1042.48` → IC=+0.238 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1042.48 (IC base=+0.073)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.188 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 5.0 (IC base=+0.073)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.03 (IC base=+0.073)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.180 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=46)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.300 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.021)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `1802.5` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_usd_total` < 1802.5
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=40)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.177 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=30)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=23)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=262)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=4009)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=176)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=133)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=163)

- **FILTRO** `ballena_activa_n` > `50.0` → IC=-0.199 (n=81)

  - _Acción_: SKIP cuando `ballena_activa_n` > 50.0
  - _Potencial_: sin este filtro IC_bueno=+0.226 (n=82)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.226 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=-0.028)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.121 (n=275)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.237)

- **PATRÓN** `liq_usd_total` > `2217.29` → IC=+0.354 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 2217.29 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.262 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.232 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.233 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2536.225` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2536.225 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.269 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.237)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1615)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1569)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=734)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=478)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=459)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.142 (n=205)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.020)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1043)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=1043)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1350)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1350)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=304)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=304)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.132 (n=104)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=215)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=371)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=420)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=311)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=413)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=413)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=258)

- **FILTRO** `libro_liquidez` < `564.286` → IC=-0.143 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 564.286
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=333)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=387)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.141 (n=37)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=81)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.517` → IC=-0.132 (n=150)

  - _Acción_: SKIP cuando `py_entrada` < 0.517
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=51)

- **FILTRO** `py_entrada` > `0.52` → IC=-0.127 (n=57)

  - _Acción_: SKIP cuando `py_entrada` > 0.52
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=31)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.142 (n=65)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=23)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.168 (n=257)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=739)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.146 (n=331)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.5 (IC base=-0.011)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.123 (n=576)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=618)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.125 (n=361)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=434)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.131 (n=291)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=633)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=634)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=340)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.41` → IC=-0.157 (n=365)

  - _Acción_: SKIP cuando `py_entrada` < 0.41
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=762)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=2289)

### MOMENTUM_IBS_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=1413)

### MOMENTUM_IBS_15M_BALLENA
- **FILTRO** `py_entrada` < `0.46` → IC=-0.174 (n=8274)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=26229)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.172 (n=8725)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=26992)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.194 (n=1542)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=4864)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.144 (n=2131)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=4199)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1642)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.041)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.126 (n=3226)

  - _Acción_: Kelly boost +0.63€ cuando `py_entrada` < 0.505 (IC base=+0.013)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.173 (n=1153)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=3611)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=1230)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3786)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.198 (n=1585)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=4899)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.135 (n=1967)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.034)

- **PATRÓN** `libro_liquidez` > `1737.7254` → IC=+0.121 (n=2175)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1737.7254 (IC base=+0.034)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.161 (n=1592)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=4842)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2447)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2371)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3123)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4075)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.127 (n=1366)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=2697)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.157 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=437)

- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=447)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.198 (n=336)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1099)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=363)

- **FILTRO** `drift_20min_pct` |x|> `0.2038` → IC=-0.142 (n=118)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2038
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=358)

- **FILTRO** `libro_liquidez` < `3239.0468` → IC=-0.185 (n=157)

  - _Acción_: SKIP cuando `libro_liquidez` < 3239.0468
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=319)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=979)

- **FILTRO** `libro_liquidez` < `1989.4319` → IC=-0.141 (n=396)

  - _Acción_: SKIP cuando `libro_liquidez` < 1989.4319
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=807)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=239)

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
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=93)

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

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `hora_utc` < `8.0` → IC=-0.136 (n=23469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=53015)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=18451)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=58033)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.235 (n=19071)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=57413)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.153 (n=25817)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=50667)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.245 (n=23896)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=71737)

- **FILTRO** `ibs_7min` > `0.2804` → IC=-0.183 (n=23907)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2804
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=71726)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.160 (n=3291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10396)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.319 (n=3381)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=10306)

- **FILTRO** `ibs_7min` < `0.7103` → IC=-0.253 (n=4514)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7103
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=9173)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4017)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12508)

- **FILTRO** `ibs_7min` > `0.7719` → IC=-0.211 (n=4130)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7719
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=12395)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=3078)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9611)

- **FILTRO** `ibs_7min` < `0.7136` → IC=-0.210 (n=3172)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7136
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9517)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.202 (n=3160)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9529)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=2968)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=10000)

- **FILTRO** `ibs_7min` > `0.2655` → IC=-0.194 (n=3240)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=9728)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.180 (n=3241)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=9727)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.167 (n=3146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=9980)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=3126)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=10000)

- **FILTRO** `ibs_7min` < `0.2892` → IC=-0.251 (n=4331)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2892
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=8795)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.202 (n=2551)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=10575)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=4221)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=13289)

- **FILTRO** `ibs_7min` > `0.7268` → IC=-0.183 (n=4377)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7268
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=13133)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=3067)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9288)

- **FILTRO** `ibs_7min` < `0.7136` → IC=-0.199 (n=3087)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7136
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9268)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.190 (n=3084)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=9271)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=2992)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=9861)

- **FILTRO** `ibs_7min` > `0.2723` → IC=-0.179 (n=3213)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2723
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=9640)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.169 (n=3208)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9645)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=2936)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=9287)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.236 (n=4020)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8203)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.219 (n=3002)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9221)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4466)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=14032)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=4008)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=8396)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=2992)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=9412)

- **FILTRO** `ibs_7min` < `0.7308` → IC=-0.223 (n=4092)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7308
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=8312)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.207 (n=2738)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=9666)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.228 (n=4286)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=12993)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1014)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=1303)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.159 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=631)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=910)

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

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=583)

- **FILTRO** `libro_liquidez` < `3304.2295` → IC=-0.151 (n=193)

  - _Acción_: SKIP cuando `libro_liquidez` < 3304.2295
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=582)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4307` → IC=+0.148 (n=705)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio` |x|> 0.4307 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=1402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `422.1109` → IC=+0.160 (n=518)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 422.1109 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3557.6032` → IC=+0.139 (n=704)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3557.6032 (IC base=+0.126)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.177 (n=184)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 14.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `287.685` → IC=+0.164 (n=245)

  - _Acción_: Kelly boost +0.82€ cuando `total_vol_5m` < 287.685 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2520.4138` → IC=+0.234 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2520.4138 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.139 (n=181)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 6.0 (IC base=+0.135)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.136 (n=322)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.141 (n=282)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 14.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.128 (n=390)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.04 (IC base=+0.122)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4162` → IC=+0.175 (n=195)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4162 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `852.6939` → IC=+0.157 (n=292)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 852.6939 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.176 (n=100)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 59.0 (IC base=+0.129)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.3978` → IC=+0.167 (n=262)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.3978 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.172 (n=190)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 12.0 (IC base=+0.141)

- **PATRÓN** `total_vol_5m` < `4621.455` → IC=+0.178 (n=175)

  - _Acción_: Kelly boost +0.89€ cuando `total_vol_5m` < 4621.455 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3720.1604` → IC=+0.155 (n=175)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3720.1604 (IC base=+0.141)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=287)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.099)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=203)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.099)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.3154` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.3154
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=176)

- **FILTRO** `pct_vs_K` |x|> `2.7579` → IC=-0.149 (n=445)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7579
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=446)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.150 (n=295)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0045 (IC base=-0.052)

### PRICE_TARGET_GBM#ETH#atexpiry
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.293 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.007)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7678` → IC=+0.196 (n=90)

  - _Acción_: Kelly boost +0.98€ cuando `pct_vs_K` |x|≤ 1.7678 (IC base=-0.007)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `6.6759` → IC=-0.267 (n=28)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.6759
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=56)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `68.0124` → IC=-0.155 (n=56)

  - _Acción_: SKIP cuando `T_h` < 68.0124
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=115)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0115` → IC=-0.239 (n=603)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0115
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=201)

- **FILTRO** `T_h` > `66.9347` → IC=-0.231 (n=537)

  - _Acción_: SKIP cuando `T_h` > 66.9347
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=267)

- **FILTRO** `T_h` > `143.0075` → IC=-0.229 (n=175)

  - _Acción_: SKIP cuando `T_h` > 143.0075
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=527)

- **FILTRO** `pct_vs_K` |x|> `3.014` → IC=-0.398 (n=174)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.014
  - _Potencial_: sin este filtro IC_bueno=-0.096 (n=528)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` < `60.8769` → IC=-0.219 (n=87)

  - _Acción_: SKIP cuando `T_h` < 60.8769
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=177)

- **FILTRO** `T_h` > `143.4358` → IC=-0.227 (n=64)

  - _Acción_: SKIP cuando `T_h` > 143.4358
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=195)

- **FILTRO** `pct_vs_K` |x|> `1.0313` → IC=-0.270 (n=194)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.0313
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=65)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0089` → IC=-0.241 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `T_h` > `144.6658` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 144.6658
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0089` → IC=-0.319 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=115)

- **FILTRO** `T_h` < `69.3259` → IC=-0.292 (n=75)

  - _Acción_: SKIP cuando `T_h` < 69.3259
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=154)

- **FILTRO** `sigma_h` > `0.0094` → IC=-0.333 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0094
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=160)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.209 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=159)

- **PATRÓN** `pct_vs_K` |x|≤ `0.9248` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `pct_vs_K` |x|≤ 0.9248 (IC base=-0.145)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `T_h` > `145.2755` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `T_h` > 145.2755
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0084` → IC=-0.241 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=170)

- **FILTRO** `T_h` > `64.3086` → IC=-0.219 (n=169)

  - _Acción_: SKIP cuando `T_h` > 64.3086
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=57)

- **FILTRO** `sigma_h` > `0.0139` → IC=-0.315 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=102)

- **FILTRO** `sigma_h` < `0.0104` → IC=-0.269 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0104
  - _Potencial_: sin este filtro IC_bueno=-0.141 (n=104)

- **FILTRO** `T_h` < `89.2641` → IC=-0.209 (n=101)

  - _Acción_: SKIP cuando `T_h` < 89.2641
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=53)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1186` → IC=+0.452 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1186 (IC base=+0.330)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.386 (n=77)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.330)

- **PATRÓN** `T_h` < `0.3392` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3392 (IC base=+0.330)

- **PATRÓN** `T_h` > `0.4307` → IC=+0.357 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4307 (IC base=+0.330)

- **PATRÓN** `dist_50` > `0.4692` → IC=+0.482 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4692 (IC base=+0.330)

- **PATRÓN** `edge` > `0.1005` → IC=+0.427 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1005 (IC base=+0.389)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.408 (n=183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.389)

- **PATRÓN** `T_h` < `0.7218` → IC=+0.418 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7218 (IC base=+0.389)

- **PATRÓN** `T_h` > `1.4833` → IC=+0.393 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4833 (IC base=+0.389)

- **PATRÓN** `dist_50` > `0.366` → IC=+0.441 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.366 (IC base=+0.389)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.410 (n=333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.389)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1161` → IC=+0.274 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1161 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.259 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.200 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.171)

- **PATRÓN** `T_h` > `1.4847` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4847 (IC base=+0.171)

- **PATRÓN** `dist_50` > `0.322` → IC=+0.294 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.322 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.226 (n=60)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.171)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.464 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.407)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.421 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.407)

- **PATRÓN** `T_h` < `1.2415` → IC=+0.436 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2415 (IC base=+0.407)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.407)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.407)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.175` → IC=+0.486 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.175 (IC base=+0.436)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.468 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.436)

- **PATRÓN** `T_h` > `0.5264` → IC=+0.452 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.5264 (IC base=+0.436)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.471 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.436)

- **PATRÓN** `edge` > `0.2005` → IC=+0.471 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.463)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.474 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.463)

- **PATRÓN** `T_h` < `0.8021` → IC=+0.457 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8021 (IC base=+0.463)

- **PATRÓN** `T_h` > `1.4857` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4857 (IC base=+0.463)

- **PATRÓN** `dist_50` > `0.4578` → IC=+0.493 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4578 (IC base=+0.463)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.463)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=449)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=491)

- **PATRÓN** `streak_estiramiento` < `0.8175` → IC=+0.127 (n=338)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.8175 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.124 (n=251)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 29.0 (IC base=+0.060)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **PATRÓN** `ballena_activa_n` < `58.0` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 58.0 (IC base=+0.078)

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
- **FILTRO** `regimen_ma_toques` < `2.0` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `regimen_ma_toques` < 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=190)

- **PATRÓN** `streak_estiramiento` < `0.2021` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `streak_estiramiento` < 0.2021 (IC base=+0.030)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.145 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.093)

- **PATRÓN** `streak_estiramiento` < `0.5637` → IC=+0.173 (n=166)

  - _Acción_: Kelly boost +0.86€ cuando `streak_estiramiento` < 0.5637 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.156 (n=161)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 31.0 (IC base=+0.093)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=92)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=52)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=37)

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

- **FILTRO** `streak_estiramiento` > `0.6439` → IC=-0.123 (n=59)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.6439
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=20)

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
- **PATRÓN** `streak_estiramiento` < `0.6439` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.6439 (IC base=+0.017)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1083)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1349)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1300)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5086)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.167 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `libro_liquidez` < `6744.0765` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `libro_liquidez` < 6744.0765
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2947)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.185 (n=1882)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0055 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.2232` → IC=+0.159 (n=5643)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.2232 (IC base=+0.139)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3548` → IC=+0.146 (n=5289)

  - _Acción_: Kelly boost +0.73€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3548 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.146 (n=5959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 4.0 (IC base=+0.139)

- **PATRÓN** `ibs_15` > `0.5714` → IC=+0.220 (n=5056)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5714 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.1365` → IC=+0.129 (n=2609)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.1365 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.241 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=3173)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4494.7072` → IC=+0.170 (n=1881)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4494.7072 (IC base=+0.139)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=2194)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.219 (n=819)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.058` → IC=+0.256 (n=273)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.058 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2675` → IC=+0.227 (n=273)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2675 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.229 (n=754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7077` → IC=+0.272 (n=819)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7077 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3751` → IC=+0.225 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3751 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.1096` → IC=+0.204 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1096 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.371` → IC=+0.310 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.371 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1061)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `11832.5463` → IC=+0.219 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11832.5463 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.146 (n=1021)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0071 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.150 (n=681)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.139 (n=934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.134 (n=1024)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 16.0 (IC base=+0.133)

- **PATRÓN** `ibs_15` > `0.4915` → IC=+0.220 (n=1021)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4915 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.151 (n=632)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.063` → IC=+0.283 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.063 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6020.1719` → IC=+0.173 (n=463)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6020.1719 (IC base=+0.133)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.7627` → IC=+0.132 (n=739)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.66€ cuando `ibs_15` > 0.7627 (IC base=+0.052)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0192` → IC=+0.167 (n=953)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0192 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.154 (n=1428)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0126 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.2278` → IC=+0.178 (n=1429)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2278 (IC base=+0.151)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0965` → IC=+0.214 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0965 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.157 (n=1312)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 6.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.156 (n=1259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 14.0 (IC base=+0.151)

- **PATRÓN** `ibs_15` > `0.5354` → IC=+0.224 (n=1276)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5354 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1984` → IC=+0.169 (n=647)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1984 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.676` → IC=+0.192 (n=235)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 21.676 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `2507.6219` → IC=+0.174 (n=1276)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2507.6219 (IC base=+0.151)

- **PATRÓN** `ibs_15` < `0.113` → IC=+0.150 (n=1091)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.113 (IC base=+0.067)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.397 (n=346)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0054 (IC base=+0.364)

- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.365 (n=508)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.378 (n=507)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.134` → IC=+0.380 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.134 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.373 (n=803)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7903` → IC=+0.394 (n=762)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7903 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.381 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.963` → IC=+0.396 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.963 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3882.8993` → IC=+0.374 (n=681)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3882.8993 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.404 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.1523` → IC=+0.362 (n=325)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1523 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2196` → IC=+0.376 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2196 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1436` → IC=+0.399 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1436 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.381 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8078` → IC=+0.384 (n=369)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8078 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.3751` → IC=+0.392 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3751 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.163` → IC=+0.392 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.163 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `8119.484` → IC=+0.384 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8119.484 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.401 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.369 (n=394)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.384 (n=179)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.1074` → IC=+0.368 (n=263)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1074 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1293` → IC=+0.383 (n=262)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1293 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2951` → IC=+0.373 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2951 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.371 (n=394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.371 (n=184)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.764` → IC=+0.394 (n=393)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.764 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1212` → IC=+0.373 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1212 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` < `0.2796` → IC=+0.365 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2796 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.392 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `4202.8422` → IC=+0.379 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4202.8422 (IC base=+0.365)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0075` → IC=-0.201 (n=2780)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0075
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2781)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2360)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=3201)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.215 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.084)

- **PATRÓN** `ibs_15` > `0.6307` → IC=+0.275 (n=1255)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6307 (IC base=-0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.199 (n=731)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.084)

- **PATRÓN** `dist_vwap_pct` < `0.2602` → IC=+0.196 (n=1081)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2602 (IC base=-0.084)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2328` → IC=+0.272 (n=1717)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2328 (IC base=-0.002)

- **PATRÓN** `ibs_15` < `0.3704` → IC=+0.286 (n=5150)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3704 (IC base=-0.002)

- **PATRÓN** `dist_vwap_pct` > `0.6596` → IC=+0.283 (n=709)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6596 (IC base=-0.002)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` < `0.0038` → IC=-0.213 (n=890)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=2677)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.188 (n=1661)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1906)

- **FILTRO** `sigma_ewma_delta_pct` > `22.182` → IC=-0.246 (n=502)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.182
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=3065)

- **FILTRO** `libro_liquidez` < `10287.6416` → IC=-0.196 (n=1177)

  - _Acción_: SKIP cuando `libro_liquidez` < 10287.6416
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=2390)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.149 (n=340)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0031 (IC base=+0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.287 (n=148)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1453` → IC=+0.267 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1453 (IC base=+0.068)

- **PATRÓN** `ibs_15` > `0.7639` → IC=+0.314 (n=444)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7639 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1041` → IC=+0.272 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1041 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2432` → IC=+0.274 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2432 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.133` → IC=+0.148 (n=225)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 22.133 (IC base=+0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.224 (n=74)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.184)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0866` → IC=+0.308 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0866 (IC base=-0.184)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.289 (n=74)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.184)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.184)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.300 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.184)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=819)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.159 (n=552)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0059 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.150 (n=418)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0052 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.163 (n=553)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3014` → IC=+0.196 (n=492)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3014 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.162 (n=448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5684` → IC=+0.239 (n=627)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5684 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6245` → IC=+0.161 (n=116)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6245 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2675` → IC=+0.147 (n=585)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2675 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.001` → IC=+0.258 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.001 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=819)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7295.1819` → IC=+0.162 (n=285)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 7295.1819 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.255 (n=1339)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.3588` → IC=+0.247 (n=1767)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3588 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7869` → IC=+0.258 (n=1767)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7869 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2099` → IC=+0.268 (n=911)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2099 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.256 (n=735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3844` → IC=+0.273 (n=2008)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3844 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.3802` → IC=+0.276 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3802 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.405` → IC=+0.250 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.405 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.23` → IC=+0.249 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.23 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1877` → IC=-0.271 (n=325)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1877
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=978)

- **FILTRO** `sigma_h` > `0.0105` → IC=-0.237 (n=443)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=860)

- **FILTRO** `drift_60min` |x|> `0.1723` → IC=-0.271 (n=443)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1723
  - _Potencial_: sin este filtro IC_bueno=-0.166 (n=860)

- **FILTRO** `drift_15min` |x|> `0.921` → IC=-0.286 (n=325)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.921
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=978)

- **FILTRO** `sigma_ewma_delta_pct` > `16.92` → IC=-0.136 (n=690)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 16.92
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=5519)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.202)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.202)

- **PATRÓN** `dist_vwap_pct` < `0.1327` → IC=+0.167 (n=55)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1327 (IC base=-0.202)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.297 (n=883)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.028)

- **PATRÓN** `dist_vwap_pct` > `0.6964` → IC=+0.245 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6964 (IC base=-0.028)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0155` → IC=-0.249 (n=1062)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0155
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=524)

- **FILTRO** `drift_60min` |x|> `0.1536` → IC=-0.248 (n=395)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1536
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=1191)

- **FILTRO** `drift_15min` |x|> `1.2687` → IC=-0.281 (n=396)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2687
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=1190)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=1566)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.220)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1678` → IC=+0.282 (n=559)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1678 (IC base=-0.013)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1185` → IC=+0.300 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1185 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3273` → IC=+0.296 (n=1233)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3273 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.7602` → IC=+0.336 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7602 (IC base=-0.013)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.143 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0065 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1891` → IC=+0.125 (n=54)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.1891 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8407` → IC=+0.315 (n=25)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8407 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 49.0 (IC base=+0.103)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.143 (n=54)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0065 (IC base=+0.103)

- **PATRÓN** `drift_60min` |x|≤ `0.1891` → IC=+0.125 (n=54)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.1891 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.161 (n=54)

  - _Acción_: Kelly boost +0.80€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.103)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2386` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2386 (IC base=+0.103)

- **PATRÓN** `ibs_15` > `0.8407` → IC=+0.315 (n=25)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8407 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.1207` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1207 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 49.0 (IC base=+0.103)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.298 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0033 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.283 (n=464)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0064 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0712` → IC=+0.309 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0712 (IC base=+0.282)

- **PATRÓN** `delta_ratio_macro` |x|> `0.152` → IC=+0.284 (n=927)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.152 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2216` → IC=+0.290 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2216 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.295 (n=1444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8379` → IC=+0.310 (n=1391)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8379 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.311 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.932` → IC=+0.386 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.932 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13139.6259` → IC=+0.300 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13139.6259 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.304 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.304 (n=324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.275)

- **PATRÓN** `drift_15min` |x|≤ `0.3845` → IC=+0.275 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3845 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.282 (n=246)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2304` → IC=+0.281 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2304 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.293 (n=773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.9195` → IC=+0.325 (n=490)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9195 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2534` → IC=+0.314 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2534 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.742` → IC=+0.390 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.742 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=951)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `15745.2501` → IC=+0.314 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15745.2501 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.293 (n=656)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.290 (n=437)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.309 (n=438)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0654` → IC=+0.290 (n=656)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0654 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1008` → IC=+0.312 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1008 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.290 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.8466` → IC=+0.318 (n=656)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8466 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2787` → IC=+0.318 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2787 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.243` → IC=+0.374 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.243 (IC base=+0.289)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.156 (n=94)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=285)

- **FILTRO** `ballena_activa_n` > `32.0` → IC=-0.130 (n=260)

  - _Acción_: SKIP cuando `ballena_activa_n` > 32.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=87)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.212 (n=123)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=371)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.180 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=371)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1387` → IC=-0.143 (n=54)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1387
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=165)

- **FILTRO** `sigma_h` < `0.0059` → IC=-0.167 (n=43)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0059
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

- **FILTRO** `ballena_activa_n` > `595.0` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 595.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.2529` → IC=-0.147 (n=32)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2529
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=32)

- **FILTRO** `sigma_h` < `0.0054` → IC=-0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `drift_60min` |x|> `0.2521` → IC=-0.200 (n=18)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2521
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=37)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `sigma_h` < `0.0057` → IC=-0.210 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=30)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0863
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### WEEKLY_PRICE
- **PATRÓN** `ratio` < `0.9701` → IC=+0.367 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9701 (IC base=+0.158)

- **PATRÓN** `T_h` > `117.6267` → IC=+0.356 (n=2921)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 117.6267 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0204` → IC=+0.389 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0204 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9933` → IC=+0.241 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9933 (IC base=+0.115)

- **PATRÓN** `T_h` > `111.9558` → IC=+0.320 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9558 (IC base=+0.302)

- **PATRÓN** `ratio` > `1.0177` → IC=+0.370 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0177 (IC base=+0.302)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9841` → IC=+0.394 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9841 (IC base=+0.205)

- **PATRÓN** `T_h` > `111.9965` → IC=+0.356 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9965 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0289` → IC=+0.406 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0289 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0624` → IC=+0.417 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0624 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5714 sube el IC de +0.139 a +0.220 en UPDOWN_GBM#15min (n=5056). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7077 sube el IC de +0.202 a +0.272 en UPDOWN_GBM#BTC#15min (n=819). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4915 sube el IC de +0.133 a +0.220 en UPDOWN_GBM#ETH#15min (n=1021). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5354 sube el IC de +0.151 a +0.224 en UPDOWN_GBM#XRP#15min (n=1276). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.113 sube el IC de +0.067 a +0.150 en UPDOWN_GBM#XRP#15min (n=1091). Ya aplicado como kelly_boost=+0.75€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6307 sube el IC de -0.084 a +0.275 en UPDOWN_GBM_15M_TARDIO (n=1255). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3704 sube el IC de -0.002 a +0.286 en UPDOWN_GBM_15M_TARDIO (n=5150). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7639 sube el IC de +0.068 a +0.314 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=444). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.184 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5684 sube el IC de +0.146 a +0.239 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=627). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3844 sube el IC de +0.244 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2008). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.202 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.028 a +0.297 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=883). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.220 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3273 sube el IC de -0.013 a +0.296 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1233). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8407 sube el IC de +0.103 a +0.315 en UPDOWN_GBM_ETH_15M_HORA7 (n=25). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8407 sube el IC de +0.103 a +0.315 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=25). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8379 sube el IC de +0.282 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1391). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.9195 sube el IC de +0.275 a +0.325 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=490). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8466 sube el IC de +0.289 a +0.318 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=656). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7903 sube el IC de +0.364 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=762). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8078 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.764 sube el IC de +0.365 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=393). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2190 | +0.083 | +226.09€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2190 | +0.083 | +226.09€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1780 | +0.083 | +187.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1780 | +0.083 | +187.55€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 94 | +0.125 | +28.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 94 | +0.125 | +28.08€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1162 | -0.019 | +72.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1162 | -0.019 | +72.68€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 888 | -0.036 | +57.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 888 | -0.036 | +57.40€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 183 | +0.062 | +18.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 183 | +0.062 | +18.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 84 | -0.023 | -6.94€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 84 | -0.023 | -6.94€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 48344 | -0.084 | -6244.34€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3046 | +0.078 | -308.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 45298 | -0.095 | -5936.34€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4859 | -0.111 | -814.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4859 | -0.111 | -814.07€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3046 | +0.078 | -308.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3046 | +0.078 | -308.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4927 | -0.103 | -944.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4927 | -0.103 | -944.01€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13232 | -0.042 | -1297.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13232 | -0.042 | -1297.38€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13184 | -0.111 | -1372.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13184 | -0.111 | -1372.15€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9096 | -0.134 | -1508.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9096 | -0.134 | -1508.73€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 50918 | -0.012 | +2810.74€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 13151 | +0.004 | +1500.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 37767 | -0.018 | +1310.19€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 50918 | -0.012 | +2810.74€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 13151 | +0.004 | +1500.54€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 37767 | -0.018 | +1310.19€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 193771 | +0.113 | -8061.82€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22126 | +0.180 | -698.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 891 | +0.014 | -72.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 159709 | +0.105 | -6879.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11045 | +0.093 | -411.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 26467 | +0.102 | -1883.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 79 | -0.179 | +10.89€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 26373 | +0.104 | -1882.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 36602 | +0.124 | -626.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5621 | +0.178 | -240.88€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 26437 | +0.120 | -197.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4502 | +0.080 | -166.34€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 26516 | +0.098 | -1926.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 90 | -0.109 | +14.44€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 26411 | +0.099 | -1929.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 41407 | +0.123 | -868.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10384 | +0.179 | -250.86€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 26857 | +0.106 | -542.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4154 | +0.102 | -66.77€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 36282 | +0.111 | -1623.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5860 | +0.199 | -247.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 794 | +0.040 | -18.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 27239 | +0.096 | -1178.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2389 | +0.103 | -178.53€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO#XRP | 26497 | +0.107 | -1133.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 92 | -0.117 | +15.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 26392 | +0.108 | -1149.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 31444 | +0.192 | -2221.52€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 31444 | +0.192 | -2221.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7120 | +0.167 | -759.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7120 | +0.167 | -759.97€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4590 | +0.196 | -180.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4590 | +0.196 | -180.96€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 6980 | +0.174 | -621.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 6980 | +0.174 | -621.43€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5822 | +0.252 | -199.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5822 | +0.252 | -199.54€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6853 | +0.185 | -473.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6853 | +0.185 | -473.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1264 | +0.426 | -46.08€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1264 | +0.426 | -46.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 525 | +0.439 | -4.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 525 | +0.439 | -4.54€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 512 | +0.424 | -19.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 512 | +0.424 | -19.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 111193 | +0.199 | -8267.70€ | 3 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 111193 | +0.199 | -8267.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 19240 | +0.177 | -2239.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 19240 | +0.177 | -2239.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 17931 | +0.224 | -610.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 17931 | +0.224 | -610.40€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 19092 | +0.180 | -2038.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 19092 | +0.180 | -2038.48€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 18074 | +0.218 | -722.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 18074 | +0.218 | -722.03€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 18355 | +0.203 | -1157.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 18355 | +0.203 | -1157.33€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 18501 | +0.196 | -1499.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 18501 | +0.196 | -1499.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 43000 | +0.117 | +353.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 43000 | +0.117 | +353.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 21409 | +0.117 | +207.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 21409 | +0.117 | +207.25€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 21591 | +0.116 | +145.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 21591 | +0.116 | +145.88€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2643 | +0.292 | -20.87€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2643 | +0.292 | -20.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1206 | +0.281 | -32.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1206 | +0.281 | -32.42€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1295 | +0.295 | +4.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1295 | +0.295 | +4.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1217 | +0.437 | -8.44€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1217 | +0.437 | -8.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 581 | +0.433 | -9.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 581 | +0.433 | -9.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 584 | +0.440 | -0.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 584 | +0.440 | -0.12€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1966 | +0.067 | -90.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1241 | +0.078 | -26.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1532 | +0.074 | -45.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1241 | +0.078 | -26.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 87303 | +0.101 | -2031.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7049 | +0.097 | +157.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 80254 | +0.101 | -2188.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 47699 | +0.105 | -451.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7049 | +0.097 | +157.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 40650 | +0.107 | -609.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 18616 | +0.109 | -93.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 18616 | +0.109 | -93.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 20988 | +0.082 | -1485.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 20988 | +0.082 | -1485.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 59286 | +0.101 | +33214.78€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 59286 | +0.101 | +33214.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 9813 | +0.226 | +8476.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 9813 | +0.226 | +8476.82€ | 0 | 20 |
| ✅ GBM_LATE_15M#BTC | 9131 | +0.177 | +7239.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9131 | +0.177 | +7239.07€ | 0 | 20 |
| ✅ GBM_LATE_15M#DOGE | 10628 | +0.207 | +8407.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10628 | +0.207 | +8407.29€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 7912 | +0.058 | +2597.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 7912 | +0.058 | +2597.90€ | 1 | 16 |
| ✅ GBM_LATE_15M#SOL | 8262 | -0.028 | +2163.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8262 | -0.028 | +2163.04€ | 4 | 15 |
| ✅ GBM_LATE_15M#XRP | 13540 | -0.021 | +4330.65€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13540 | -0.021 | +4330.65€ | 3 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 62679 | +0.086 | +36470.96€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 62679 | +0.086 | +36470.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 12116 | -0.002 | +6455.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 12116 | -0.002 | +6455.95€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 13486 | +0.005 | +3629.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 13486 | +0.005 | +3629.14€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8497 | +0.295 | +9723.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8497 | +0.295 | +9723.60€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 11960 | +0.015 | +3746.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 11960 | +0.015 | +3746.56€ | 1 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9601 | +0.045 | +4319.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9601 | +0.045 | +4319.76€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7019 | +0.315 | +8595.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7019 | +0.315 | +8595.95€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 46797 | +0.179 | +38779.01€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 46797 | +0.179 | +38779.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7047 | +0.240 | +6571.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7047 | +0.240 | +6571.81€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7417 | +0.140 | +5537.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7417 | +0.140 | +5537.84€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7531 | +0.224 | +6532.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7531 | +0.224 | +6532.89€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8022 | +0.129 | +6209.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8022 | +0.129 | +6209.70€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 8851 | +0.120 | +6709.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 8851 | +0.120 | +6709.04€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 7929 | +0.234 | +7217.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 7929 | +0.234 | +7217.73€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 12808 | +0.126 | +6475.28€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 12808 | +0.126 | +6475.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 662 | +0.161 | +433.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 662 | +0.161 | +433.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3449 | +0.126 | +1877.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3449 | +0.126 | +1877.50€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3659 | +0.125 | +1782.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3659 | +0.125 | +1782.12€ | 0 | 17 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3323 | +0.099 | +1328.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3323 | +0.099 | +1328.22€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1208 | +0.169 | +762.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1208 | +0.169 | +762.77€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 59486 | +0.189 | +49242.96€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 59486 | +0.189 | +49242.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9382 | +0.250 | +9086.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9382 | +0.250 | +9086.60€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9489 | +0.139 | +6673.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9489 | +0.139 | +6673.49€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10098 | +0.235 | +9142.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10098 | +0.235 | +9142.72€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 9851 | +0.143 | +7335.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 9851 | +0.143 | +7335.41€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10542 | +0.124 | +7543.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10542 | +0.124 | +7543.23€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10124 | +0.242 | +9461.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10124 | +0.242 | +9461.52€ | 0 | 20 |
| ✅ GBM_LATE_5M | 15184 | +0.214 | +12556.56€ | 0 | 25 |
| ✅ GBM_LATE_5M#5min | 15184 | +0.214 | +12556.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1480 | +0.246 | +1399.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1480 | +0.246 | +1399.04€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3268 | +0.211 | +2815.73€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3268 | +0.211 | +2815.73€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4343 | +0.205 | +3286.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4343 | +0.205 | +3286.09€ | 0 | 26 |
| ✅ GBM_LATE_5M#SOL | 2624 | +0.223 | +2306.16€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2624 | +0.223 | +2306.16€ | 0 | 23 |
| ✅ GBM_LATE_5M#XRP | 2016 | +0.209 | +1589.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2016 | +0.209 | +1589.43€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5319 | +0.053 | +1448.11€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 5319 | +0.053 | +1448.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1838 | +0.058 | +548.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1838 | +0.058 | +548.81€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1698 | +0.053 | +542.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1698 | +0.053 | +542.66€ | 2 | 7 |
| ✅ GBM_LATE_60M#SOL | 1783 | +0.049 | +356.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1783 | +0.049 | +356.65€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 723 | -0.250 | -35.51€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 723 | -0.250 | -35.51€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 261 | -0.253 | -19.53€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 261 | -0.253 | -19.53€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 262 | -0.242 | -6.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 262 | -0.242 | -6.68€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 200 | -0.253 | -9.31€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 200 | -0.253 | -9.31€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2185 | +0.084 | +553.12€ | 0 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2185 | +0.084 | +553.12€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 847 | +0.071 | +192.82€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 847 | +0.071 | +192.82€ | 1 | 5 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 756 | +0.057 | +151.76€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 756 | +0.057 | +151.76€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 582 | +0.137 | +208.54€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 582 | +0.137 | +208.54€ | 1 | 9 |
| ✅ LATE_WINDOW_5MIN | 270 | +0.298 | +308.59€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 270 | +0.298 | +308.59€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 270 | +0.298 | +308.59€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 270 | +0.298 | +308.59€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4448 | +0.097 | +1008.42€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4448 | +0.097 | +1008.42€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4448 | +0.097 | +1008.42€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4448 | +0.097 | +1008.42€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1339 | +0.009 | +51.61€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1339 | +0.009 | +51.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 116 | +0.068 | +17.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 116 | +0.068 | +17.64€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 289 | +0.002 | +10.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 289 | +0.002 | +10.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 79 | -0.031 | -0.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 79 | -0.031 | -0.05€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 328 | +0.024 | +20.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 328 | +0.024 | +20.72€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 330 | -0.009 | +3.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 330 | -0.009 | +3.61€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 197 | +0.003 | -1.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 197 | +0.003 | -1.27€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4291 | +0.018 | +155.95€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4291 | +0.018 | +155.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 827 | +0.015 | +40.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 827 | +0.015 | +40.58€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 275 | +0.052 | +56.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 275 | +0.052 | +56.91€ | 0 | 7 |
| ✅ LIQUIDACIONES_5M#ETH | 1667 | +0.019 | +28.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1667 | +0.019 | +28.62€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 775 | +0.012 | +3.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 775 | +0.012 | +3.41€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 508 | +0.014 | +31.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 508 | +0.014 | +31.57€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2488 | -0.033 | -6.22€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2488 | -0.033 | -6.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 754 | -0.032 | -11.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 754 | -0.032 | -11.99€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 889 | -0.011 | +19.29€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 889 | -0.011 | +19.29€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 845 | -0.057 | -13.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 845 | -0.057 | -13.52€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 16823 | -0.033 | -196.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 8109 | -0.034 | -105.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 8714 | -0.031 | -90.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 593 | -0.058 | -40.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 304 | -0.036 | -4.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 289 | -0.081 | -35.43€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4421 | -0.027 | -30.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2107 | -0.024 | +4.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2314 | -0.030 | -35.65€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1611 | -0.031 | +6.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 822 | -0.038 | -10.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 789 | -0.023 | +16.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 3809 | -0.034 | -67.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1820 | -0.033 | -27.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1989 | -0.034 | -39.61€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3229 | -0.022 | +48.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1563 | -0.029 | -2.23€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1666 | -0.015 | +51.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3160 | -0.045 | -113.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1493 | -0.051 | -64.83€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1667 | -0.041 | -48.34€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 70220 | -0.000 | +3813.30€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 70220 | -0.000 | +3813.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 12736 | +0.027 | +1754.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 12736 | +0.027 | +1754.16€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9780 | -0.037 | -144.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9780 | -0.037 | -144.41€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 12876 | +0.025 | +1450.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 12876 | +0.025 | +1450.35€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9742 | -0.052 | -246.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9742 | -0.052 | -246.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 11980 | -0.004 | +345.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 11980 | -0.004 | +345.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13106 | +0.019 | +654.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13106 | +0.019 | +654.53€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7240 | -0.053 | -110.75€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7240 | -0.053 | -110.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1262 | -0.002 | -14.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1262 | -0.002 | -14.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2007 | -0.061 | -20.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2007 | -0.061 | -20.97€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 810 | -0.119 | -35.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 810 | -0.119 | -35.34€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2205 | -0.067 | -12.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2205 | -0.067 | -12.66€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 863 | -0.018 | -27.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 863 | -0.018 | -27.52€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3381 | +0.003 | +0.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3381 | +0.003 | +0.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 197 | +0.007 | -1.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 197 | +0.007 | -1.76€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 172117 | -0.078 | +2275.13€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 172117 | -0.078 | +2275.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 30212 | -0.077 | +1721.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 30212 | -0.077 | +1721.37€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 25657 | -0.101 | -1253.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 25657 | -0.101 | -1253.38€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 30636 | -0.068 | +1519.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 30636 | -0.068 | +1519.65€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 25208 | -0.099 | -829.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 25208 | -0.099 | -829.97€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 30721 | -0.059 | +252.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 30721 | -0.059 | +252.89€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 29683 | -0.069 | +864.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 29683 | -0.069 | +864.57€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9115 | -0.035 | -184.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9115 | -0.035 | -184.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2120 | -0.047 | -28.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2120 | -0.047 | -28.53€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2661 | -0.025 | -35.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2661 | -0.025 | -35.39€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1275 | -0.064 | -31.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1275 | -0.064 | -31.66€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1042 | -0.036 | -37.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1042 | -0.036 | -37.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2206 | +0.121 | +891.20€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2070 | +0.126 | +878.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 488 | +0.135 | +239.29€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 488 | +0.135 | +239.29€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 427 | +0.122 | +157.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 427 | +0.122 | +157.18€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#ETH | 389 | +0.129 | +180.25€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 389 | +0.129 | +180.25€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 349 | +0.141 | +178.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 349 | +0.141 | +178.93€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#XRP | 417 | +0.099 | +122.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 417 | +0.099 | +122.96€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2281 | -0.016 | -11.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2281 | -0.016 | -11.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 410 | +0.012 | +24.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 410 | +0.012 | +24.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 422 | -0.040 | -20.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 422 | -0.040 | -20.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 566 | -0.041 | -33.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 566 | -0.041 | -33.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 463 | +0.005 | +9.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 463 | +0.005 | +9.61€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 420 | -0.009 | +8.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 420 | -0.009 | +8.40€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1192 | -0.058 | +15.92€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 550 | -0.094 | -50.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 429 | -0.103 | -29.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 121 | -0.061 | -20.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 417 | -0.018 | +43.32€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 302 | +0.000 | +51.32€ | 0 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 115 | -0.064 | -8.00€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 225 | -0.042 | +23.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 189 | -0.034 | +21.21€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 920 | -0.055 | +42.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 272 | -0.066 | -26.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1506 | -0.202 | -80.95€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 593 | -0.198 | -41.43€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 523 | -0.195 | -36.98€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#reach | 70 | -0.208 | -4.45€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 503 | -0.207 | -38.60€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 441 | -0.218 | -45.74€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 62 | -0.125 | +7.14€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 410 | -0.199 | -0.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 380 | -0.196 | -3.07€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 30 | -0.219 | +2.15€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1344 | -0.204 | -85.79€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 162 | -0.183 | +4.84€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 548 | +0.373 | +506.59€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 116 | +0.144 | +89.63€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 116 | +0.144 | +89.63€ | 0 | 6 |
| ✅ RESOLUTION_SNIPER#ETH | 125 | +0.366 | +104.29€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 125 | +0.366 | +104.29€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 307 | +0.458 | +312.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 307 | +0.458 | +312.67€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 548 | +0.373 | +506.59€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 978 | +0.039 | +80.59€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 978 | +0.039 | +80.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 75 | +0.019 | +1.57€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 75 | +0.019 | +1.57€ | 1 | 1 |
| ✅ STREAK_FADE_15M#SOL | 83 | +0.018 | +6.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 83 | +0.018 | +6.06€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 461 | +0.064 | +70.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 461 | +0.064 | +70.62€ | 1 | 4 |
| ✅ STREAK_FADE_5M | 3594 | -0.023 | -142.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3594 | -0.023 | -142.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 619 | -0.028 | -27.08€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 619 | -0.028 | -27.08€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 172 | -0.046 | -15.31€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 172 | -0.046 | -15.31€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1676 | -0.019 | -60.21€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1676 | -0.019 | -60.21€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 121 | -0.053 | -14.40€ | 6 | 0 |
| ✅ STREAK_FADE_60M#60min | 121 | -0.053 | -14.40€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 44 | -0.087 | -4.62€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 44 | -0.087 | -4.62€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 77 | -0.032 | -9.78€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 77 | -0.032 | -9.78€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11561 | +0.014 | +74.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11561 | +0.014 | +74.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3046 | +0.016 | +32.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3046 | +0.016 | +32.71€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2934 | +0.009 | -2.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2934 | +0.009 | -2.53€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2586 | +0.014 | +19.79€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2586 | +0.014 | +19.79€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12399 | +0.018 | -3.77€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12399 | +0.018 | -3.77€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5105 | +0.021 | +3.66€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5105 | +0.021 | +3.66€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4313 | +0.018 | -2.54€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4313 | +0.018 | -2.54€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2981 | +0.014 | -4.89€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2981 | +0.014 | -4.89€ | 1 | 0 |
| ✅ UPDOWN_GBM | 112057 | +0.060 | +10641.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 27292 | +0.078 | +5446.44€ | 0 | 9 |
| ✅ UPDOWN_GBM#240min | 3262 | -0.001 | +35.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 74467 | +0.062 | +5051.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6657 | -0.003 | +116.65€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 9520 | +0.103 | +1717.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1782 | +0.163 | +818.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 7648 | +0.091 | +900.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 25482 | +0.058 | +2270.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3665 | +0.079 | +825.61€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 938 | -0.001 | +19.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 17775 | +0.068 | +1348.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2966 | -0.005 | +74.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 138 | -0.064 | +3.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 12234 | +0.075 | +1339.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1761 | +0.154 | +738.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 10387 | +0.063 | +601.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 26502 | +0.049 | +1871.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6430 | +0.071 | +991.37€ | 0 | 8 |
| ✅ UPDOWN_GBM#ETH#240min | 908 | +0.004 | +15.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16584 | +0.052 | +822.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2454 | +0.000 | +41.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 126 | -0.109 | +0.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 23647 | +0.040 | +1338.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7389 | +0.032 | +452.14€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 843 | -0.011 | +4.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14065 | +0.052 | +890.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1237 | -0.002 | +0.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 113 | -0.143 | -9.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 14670 | +0.073 | +2106.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6265 | +0.093 | +1619.97€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8008 | +0.062 | +488.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 377 | -0.104 | -6.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1015 | +0.364 | +377.14€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1015 | +0.364 | +377.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 491 | +0.362 | +172.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 491 | +0.362 | +172.01€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 524 | +0.365 | +205.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 524 | +0.365 | +205.13€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 26397 | -0.020 | +6580.70€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 26397 | -0.020 | +6580.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 4923 | -0.115 | +278.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 4923 | -0.115 | +278.45€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1071 | +0.222 | +899.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3513 | +0.221 | +2257.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3513 | +0.221 | +2257.11€ | 1 | 20 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7512 | -0.058 | +1121.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7512 | -0.058 | +1121.06€ | 5 | 5 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7397 | -0.058 | +1463.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7397 | -0.058 | +1463.03€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 326 | +0.061 | +33.64€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 326 | +0.061 | +33.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 326 | +0.061 | +33.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 326 | +0.061 | +33.64€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1854 | +0.282 | +1560.33€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1854 | +0.282 | +1560.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 980 | +0.275 | +772.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 980 | +0.275 | +772.09€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 874 | +0.289 | +788.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 874 | +0.289 | +788.24€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 873 | -0.114 | -87.23€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 873 | -0.114 | -87.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 277 | -0.081 | -20.93€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 277 | -0.081 | -20.93€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 99 | -0.183 | -12.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 99 | -0.183 | -12.98€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 114 | -0.172 | -3.97€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 114 | -0.172 | -3.97€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 4833 | +0.300 | +2158.68€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1845 | +0.255 | +236.16€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1869 | +0.294 | +788.42€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1119 | +0.381 | +1134.11€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.021 n=1368 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1368 IC=+0.021 PNL=+67.39€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 837 celda(s) pasan gate riguroso completo de 2946 evaluadas (n>=40) y 4063 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.032 < 0.08 — monitorear
  - _Datos_: n=7384 IC=+0.032 PNL=+449.88€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1869/15 IC=+0.294 PNL=+788.42€ | BTC: n=1845/15 IC=+0.255 PNL=+236.16€ | SOL: n=1119/15 IC=+0.381 PNL=+1134.11€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=1079/60 | contraria IC=+0.183 n=1135 | gap=-0.043 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=605, boost estimado=+0.011. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2452/40 IC=+0.000 PNL=+41.26€ | BTC#60min: n=2964/40 IC=-0.005 PNL=+74.48€ | SOL#60min: n=1237/40 IC=-0.002 PNL=+0.88€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.045 n=758173 | tras_1loss IC=+0.101 n=574466 | tras_2loss IC=+0.071 n=229306/40 | gap=-0.027 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.08 con n=1121 PNL=+691.25€
  - _Datos_: n=1121 IC=+0.165 PNL=+691.25€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.135 > 0.08 con n=1328 PNL=+633.88€
  - _Datos_: n=1328 IC=+0.135 PNL=+633.88€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.126 > 0.08 con n=89 PNL=+36.54€
  - _Datos_: n=89 IC=+0.126 PNL=+36.54€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=3938 PNL=+2192.14€
  - _Datos_: n=3938 IC=+0.335 PNL=+2192.14€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1134 IC=+0.066 PNL=+113.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1134 IC=+0.066 PNL=+113.60€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=108 IC=+0.173 PNL=+68.06€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=108 IC=+0.173 PNL=+68.06€

**⏳ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: 30
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 7/15 ops en el filtro definido (IC actual=+0.097 PNL=+9.02€)
  - _Datos_: n=7 IC=+0.097 PNL=+9.02€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 3/20 ops en el filtro definido (IC actual=-0.015 PNL=-2.12€)
  - _Datos_: n=3 IC=-0.015 PNL=-2.12€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: 07h sigue en ORDER_FLOW_BLACKLIST_HOURS -- mientras siga ahí, nunca genera fila para volver a evaluarse (26-Ago, triage candidatas estancadas)

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=4407 IC=-0.003 PNL=-34.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4407 IC=-0.003 PNL=-34.28€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2246 IC=-0.002 PNL=+150.90€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2246 IC=-0.002 PNL=+150.90€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1368 IC=+0.021 PNL=+67.39€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1368 IC=+0.021 PNL=+67.39€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.139 > 0.1 con n=7520 PNL=+3715.81€
  - _Datos_: n=7520 IC=+0.139 PNL=+3715.81€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3664 IC=+0.079 PNL=+826.12€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3664 IC=+0.079 PNL=+826.12€

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
  - _Estado_: n=1469 IC=+0.039 PNL=+116.17€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1469 IC=+0.039 PNL=+116.17€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=187 IC=-0.034 PNL=-7.31€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=187 IC=-0.034 PNL=-7.31€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.298 n=270) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=270 IC=+0.298 PNL=+308.59€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.118 > 0.02 con n=1290 PNL=+519.23€
  - _Datos_: n=1290 IC=+0.118 PNL=+519.23€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=263 IC=-0.115 PNL=+6.39€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=263 IC=-0.115 PNL=+6.39€

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
  - _Estado_: n=46042 IC=+0.071 PNL=+6250.34€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=46042 IC=+0.071 PNL=+6250.34€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.135 < -0.1 con n=779 PNL=+116.29€
  - _Datos_: n=779 IC=-0.135 PNL=+116.29€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4358 IC=+0.067 PNL=+544.65€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4358 IC=+0.067 PNL=+544.65€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=194 IC=-0.087 PNL=+1.19€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=194 IC=-0.087 PNL=+1.19€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.101 > 0.1 con n=1166 PNL=+297.43€
  - _Datos_: n=1166 IC=+0.101 PNL=+297.43€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 7/20 ops en el filtro definido (IC actual=-0.058 PNL=-1.16€)
  - _Datos_: n=7 IC=-0.058 PNL=-1.16€
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: PY_MKT_MAX_BUY_NO_ETH15=0.55 en shadow_predict.py hace RETURN NONE (bloquea generación, no solo decisión) -- nunca podrá acumular n mientras siga activo. Haría falta un logger separado sin el filtro para monitorear de verdad (no construido, 26-Ago)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=44973 IC=-0.137 PNL=+2784.52€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=44973 IC=-0.137 PNL=+2784.52€

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
  - _Estado_: n=4732 IC=+0.133 PNL=+3207.75€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4732 IC=+0.133 PNL=+3207.75€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=11644 IC=+0.057 PNL=+1012.91€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11644 IC=+0.057 PNL=+1012.91€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=4869 PNL=+2742.88€
  - _Datos_: n=4869 IC=+0.102 PNL=+2742.88€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.220 < -0.1 con n=4904 PNL=-417.70€
  - _Datos_: n=4904 IC=-0.220 PNL=-417.70€

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
  - _Estado_: n=116 IC=+0.051 PNL=+20.54€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=116 IC=+0.051 PNL=+20.54€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2257) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2257 IC=+0.096 PNL=+452.08€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=688) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=688 IC=+0.414 PNL=+1006.56€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=19232 IC=+0.177 PNL=-2236.11€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=19232 IC=+0.177 PNL=-2236.11€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.233 > 0.1 con n=309 PNL=+217.16€
  - _Datos_: n=309 IC=+0.233 PNL=+217.16€
