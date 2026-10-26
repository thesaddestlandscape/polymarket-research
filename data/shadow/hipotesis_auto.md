# Hipótesis automáticas — 2026-10-26 15:38 UTC
_Generado por shadow_postmortem.py sobre 1064741 resoluciones (PNL=+140087.57€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.229 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.136)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.183 (n=301)

  - _Acción_: Kelly boost +0.92€ cuando `n_total_lado` > 64.0 (IC base=+0.136)

- **PATRÓN** `banda_hit_calibrado` > `0.6181` → IC=+0.264 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6181 (IC base=+0.136)

- **PATRÓN** `banda_z` > `8.922` → IC=+0.213 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.922 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.161 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.138 (n=435)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 8.0 (IC base=+0.136)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=972)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `2653.7599` → IC=+0.138 (n=797)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2653.7599 (IC base=+0.136)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.515` → IC=+0.225 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.141)

- **PATRÓN** `n_total_lado` > `68.0` → IC=+0.200 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 68.0 (IC base=+0.141)

- **PATRÓN** `banda_hit_calibrado` > `0.6153` → IC=+0.255 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6153 (IC base=+0.141)

- **PATRÓN** `banda_z` > `9.307` → IC=+0.197 (n=255)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 9.307 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.142 (n=364)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 8.0 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=873)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `9643.6217` → IC=+0.129 (n=208)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 9643.6217 (IC base=+0.015)

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
- **FILTRO** `restante_s_al_confirmar` < `139.37` → IC=-0.210 (n=10634)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 139.37
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=31903)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `127.3` → IC=-0.261 (n=1150)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 127.3
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=3453)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `120.19` → IC=-0.294 (n=1136)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 120.19
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=3409)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `162.28` → IC=-0.233 (n=2831)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 162.28
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=8494)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.92` → IC=-0.265 (n=2053)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.92
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=6160)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.214 (n=23263)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.126 (n=4550)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `8867.9414` → IC=+0.167 (n=2081)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 8867.9414 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=19849)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=35978)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=18570)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.146 (n=7519)

  - _Acción_: Kelly boost +0.73€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `6876.0275` → IC=+0.155 (n=2911)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 6876.0275 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=2096)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.765` → IC=+0.364 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.765 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=2565)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `16451.0129` → IC=+0.186 (n=666)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 16451.0129 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.186 (n=1832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.185 (n=2052)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.285` → IC=+0.317 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.285 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=2627)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `16210.313` → IC=+0.188 (n=678)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 16210.313 (IC base=+0.181)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.173 (n=502)

  - _Acción_: Kelly boost +0.86€ cuando `py_entrada` > 0.61 (IC base=+0.077)

- **PATRÓN** `libro_liquidez` > `6664.4284` → IC=+0.142 (n=132)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6664.4284 (IC base=+0.077)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.140 (n=1196)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.084)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4514)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.163 (n=3835)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.378 (n=1451)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.215 (n=2021)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.350 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.207)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=2352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.207)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=1139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.149 (n=974)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 15.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.262 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=901)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2205.3811` → IC=+0.153 (n=494)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2205.3811 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=879)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.421 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=1324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=693)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.146)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.146)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.153 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.103)

- **PATRÓN** `py_entrada` > `0.56` → IC=+0.189 (n=384)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` > 0.56 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.133 (n=1291)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.244 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.229 (n=149)

- **FILTRO** `py_entrada` > `0.755` → IC=-0.293 (n=138)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=73)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.204 (n=19860)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.201 (n=16898)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=8171)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=2150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.180 (n=4320)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.183 (n=4446)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=3755)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.179)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.222 (n=2448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.225 (n=1646)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.300 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.219)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.186 (n=4484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=3826)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.188 (n=3503)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3853)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.362 (n=1278)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=4393)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.194 (n=2809)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=3253)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.432 (n=832)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.426)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.426 (n=718)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.426)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.439 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.426)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.426)

- **PATRÓN** `libro_liquidez` > `4294.1313` → IC=+0.439 (n=542)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4294.1313 (IC base=+0.426)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.439 (n=340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `20878.8113` → IC=+0.446 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 20878.8113 (IC base=+0.435)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=333)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.431)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.430 (n=329)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.431)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.440 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.431)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.438 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.431)

- **PATRÓN** `libro_liquidez` > `3610.6662` → IC=+0.445 (n=215)

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
  - _Potencial_: sin este filtro IC_bueno=-0.143 (n=12)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=28)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=25731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=26065)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=4433)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=8271)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.199 (n=11661)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=5368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=5297)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.287 (n=3742)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.225)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=4415)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.201 (n=9110)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=5405)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=4150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.219)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.274 (n=3661)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.219)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.207 (n=9893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.262 (n=3825)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=4278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=4316)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.198)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4511)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.198)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=9321)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=9353)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.68` → IC=+0.136 (n=11287)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.68 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.197 (n=4601)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.38 (IC base=+0.119)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.145 (n=4260)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.96 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=5664)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 7.0 (IC base=+0.119)

- **PATRÓN** `lag_apertura_s` < `2.69` → IC=+0.145 (n=4259)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.69 (IC base=+0.119)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=4720)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.136 (n=5093)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.29` → IC=+0.136 (n=5684)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.29 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.313 (n=1178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.385 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.288 (n=799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.361 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5061.412` → IC=+0.290 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5061.412 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.327 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.301 (n=834)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.299)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.395 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.299)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.299 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.299)

- **PATRÓN** `libro_liquidez` > `2123.7732` → IC=+0.330 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2123.7732 (IC base=+0.299)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.339 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.341)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.374 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.341)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.385 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.341)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.344 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.341)

- **PATRÓN** `libro_liquidez` > `745.0217` → IC=+0.372 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 745.0217 (IC base=+0.341)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.452 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.443)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.444 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.443)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.443)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.444 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.443)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.437 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.436 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.935` → IC=+0.441 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.935 (IC base=+0.435)

- **PATRÓN** `libro_liquidez` > `5412.072` → IC=+0.444 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5412.072 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.470 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.452)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.454 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.452)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.454 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.452)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.453 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.452)

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
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=97)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.308 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=59)

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
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=97)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.308 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=94)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.238 (n=59)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=59)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4726` → IC=+0.140 (n=14519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4726 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.126 (n=14664)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 6.0 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=10152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.3776` → IC=+0.166 (n=14518)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.3776 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.7824` → IC=+0.277 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7824 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.367` → IC=+0.261 (n=4137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.367 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.857` → IC=+0.190 (n=5495)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.857 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.2062` → IC=+0.261 (n=4242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2062 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.267 (n=4243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.304` → IC=+0.243 (n=1489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.304 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.3533` → IC=+0.231 (n=4700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3533 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=11857)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `4539.6191` → IC=+0.150 (n=4840)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4539.6191 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.5682` → IC=+0.141 (n=17974)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5682 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.6062` → IC=+0.190 (n=1165)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6062 (IC base=+0.077)

- **PATRÓN** `volumen_regimen` < `0.6973` → IC=+0.189 (n=3136)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 0.6973 (IC base=+0.077)

- **PATRÓN** `volumen_pendiente_norm` > `0.2978` → IC=+0.230 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2978 (IC base=+0.077)

- **PATRÓN** `volumen_spike_ratio` > `2.6946` → IC=+0.207 (n=4034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6946 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.222 (n=11970)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 105.0 (IC base=+0.077)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.205 (n=1052)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.204)

- **PATRÓN** `drift_60min` |x|≤ `0.3502` → IC=+0.208 (n=3146)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3502 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.217 (n=1171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.204)

- **PATRÓN** `ibs_20min` > `0.9834` → IC=+0.281 (n=1426)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9834 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.758` → IC=+0.281 (n=1389)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.758 (IC base=+0.204)

- **PATRÓN** `volumen_pendiente_norm` > `0.2841` → IC=+0.262 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2841 (IC base=+0.204)

- **PATRÓN** `volumen_spike_ratio` > `2.3054` → IC=+0.214 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3054 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=3404)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.204)

- **PATRÓN** `libro_liquidez` > `2055.5077` → IC=+0.208 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2055.5077 (IC base=+0.204)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.224 (n=1923)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.009` → IC=+0.241 (n=2666)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.009 (IC base=+0.239)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.244 (n=1212)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.0875` → IC=+0.276 (n=892)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0875 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.246 (n=2459)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.258 (n=2667)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5417 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` < `0.096` → IC=+0.242 (n=2402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.096 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.260 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` < `1.4471` → IC=+0.240 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4471 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.7246` → IC=+0.244 (n=842)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7246 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=3023)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `1557.7372` → IC=+0.242 (n=2382)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1557.7372 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.241 (n=962)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.239)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.240 (n=865)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.229)

- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.229 (n=1175)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.1059` → IC=+0.257 (n=1140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1059 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=2708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` > `0.9373` → IC=+0.271 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9373 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.1869` → IC=+0.238 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1869 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.268` → IC=+0.270 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.268 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `0.6224` → IC=+0.233 (n=2591)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6224 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.276 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `2.4384` → IC=+0.260 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4384 (IC base=+0.229)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.151 (n=2712)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0059 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.0756` → IC=+0.166 (n=903)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0756 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=1013)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `ibs_20min` < `0.5915` → IC=+0.180 (n=2383)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` < 0.5915 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.948` → IC=+0.145 (n=440)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 10.948 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.105` → IC=+0.136 (n=2468)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 4.105 (IC base=+0.131)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.141 (n=2708)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2068 (IC base=+0.131)

- **PATRÓN** `volumen_pendiente_norm` > `0.0957` → IC=+0.159 (n=985)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0957 (IC base=+0.131)

- **PATRÓN** `volumen_spike_ratio` < `2.4589` → IC=+0.141 (n=2586)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4589 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `211.0` → IC=+0.173 (n=1119)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 211.0 (IC base=+0.131)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.220 (n=1098)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.265 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.195` → IC=+0.275 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.195 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0965` → IC=+0.199 (n=2931)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` < 0.0965 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3522` → IC=+0.217 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3522 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7037` → IC=+0.210 (n=1450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7037 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.199 (n=3922)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1942.2684` → IC=+0.202 (n=1491)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1942.2684 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.223 (n=2620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.1747` → IC=+0.235 (n=1310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1747 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0286` → IC=+0.272 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0286 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.235` → IC=+0.259 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.235 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3488` → IC=+0.265 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3488 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.743` → IC=+0.225 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.743 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.221 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `1926.76` → IC=+0.220 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1926.76 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.220 (n=2497)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.138 (n=161)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=3971)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.163 (n=576)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0037 (IC base=+0.057)

- **PATRÓN** `ibs_20min` > `0.9523` → IC=+0.233 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9523 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.1401` → IC=+0.336 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1401 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.3359` → IC=+0.333 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3359 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.174` → IC=+0.196 (n=1242)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 5.174 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` < `0.8653` → IC=+0.333 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8653 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` > `1.2404` → IC=+0.352 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2404 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.0775` → IC=+0.335 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0775 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.3037` → IC=+0.340 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3037 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.4129` → IC=+0.357 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4129 (IC base=+0.057)

- **PATRÓN** `ballena_activa_n` < `144.0` → IC=+0.338 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 144.0 (IC base=+0.057)

- **PATRÓN** `ibs_20min` < `0.0932` → IC=+0.179 (n=1034)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.0932 (IC base=+0.038)

- **PATRÓN** `dist_vwap_pct` > `0.7306` → IC=+0.152 (n=234)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.7306 (IC base=+0.038)

- **PATRÓN** `volumen_regimen` < `0.8399` → IC=+0.149 (n=1256)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.8399 (IC base=+0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.2872` → IC=+0.203 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2872 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` < `1.7863` → IC=+0.137 (n=1207)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.7863 (IC base=+0.038)

- **PATRÓN** `volumen_spike_ratio` > `2.173` → IC=+0.157 (n=821)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.173 (IC base=+0.038)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.175 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=607)

- **FILTRO** `ibs_20min` > `0.2143` → IC=-0.134 (n=3879)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2143
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=1921)

- **FILTRO** `sigma_ewma_delta_pct` > `8.597` → IC=-0.233 (n=617)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.597
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=5183)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.172 (n=245)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.7632 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `1.0126` → IC=+0.285 (n=77)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0126 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.099` → IC=+0.131 (n=223)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 3.099 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `0.8709` → IC=+0.267 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8709 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `1.0233` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0233 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1558` → IC=+0.283 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1558 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4948` → IC=+0.293 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4948 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.269 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.270 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 37.0 (IC base=+0.026)

- **PATRÓN** `ibs_20min` < `0.2143` → IC=+0.149 (n=1921)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2143 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` > `0.2693` → IC=+0.279 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2693 (IC base=-0.040)

- **PATRÓN** `volumen_regimen` < `0.6948` → IC=+0.299 (n=356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6948 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` < `0.1046` → IC=+0.287 (n=666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1046 (IC base=-0.040)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.287 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=-0.040)

- **PATRÓN** `volumen_spike_ratio` < `2.4326` → IC=+0.303 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4326 (IC base=-0.040)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6015` → IC=-0.185 (n=1078)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6015
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3236)

- **FILTRO** `ibs_20min` < `0.76` → IC=-0.154 (n=2839)

  - _Acción_: SKIP cuando `ibs_20min` < 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=1475)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.166 (n=1036)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=3278)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.203 (n=1529)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=4638)

- **PATRÓN** `dist_vwap_pct` > `0.7157` → IC=+0.344 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7157 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` < `0.2438` → IC=+0.310 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2438 (IC base=-0.065)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.322 (n=688)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.065)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.308 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.317 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=-0.065)

- **PATRÓN** `volumen_spike_ratio` > `2.17` → IC=+0.315 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.17 (IC base=-0.065)

- **PATRÓN** `dist_vwap_pct` > `0.8089` → IC=+0.291 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8089 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` < `0.7234` → IC=+0.266 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7234 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `1.0685` → IC=+0.288 (n=783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0685 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.1045` → IC=+0.289 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1045 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `2.1803` → IC=+0.266 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1803 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.266 (n=1602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.211 (n=6344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.3124` → IC=+0.167 (n=19014)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3124 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.9443` → IC=+0.302 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9443 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.58` → IC=+0.164 (n=8524)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 3.58 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `1.1729` → IC=+0.267 (n=7004)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1729 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` > `0.6889` → IC=+0.273 (n=6256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6889 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2403` → IC=+0.282 (n=2099)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2403 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` > `2.6558` → IC=+0.276 (n=3715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6558 (IC base=+0.094)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.301 (n=10733)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 91.0 (IC base=+0.094)

- **PATRÓN** `sigma_h` > `0.0095` → IC=+0.154 (n=6117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0095 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.6514` → IC=+0.146 (n=18343)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.6514 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.704` → IC=+0.265 (n=2584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.704 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1973` → IC=+0.266 (n=1957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1973 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.319 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5813` → IC=+0.294 (n=3744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5813 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.285` → IC=+0.286 (n=3856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.285 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.297 (n=8460)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.5801` → IC=-0.146 (n=2594)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5801
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=2597)

- **FILTRO** `ibs_20min` > `0.7296` → IC=-0.216 (n=1112)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7296
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=3342)

- **FILTRO** `sigma_ewma_delta_pct` > `4.333` → IC=-0.220 (n=969)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.333
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3485)

- **PATRÓN** `ibs_20min` > `0.9256` → IC=+0.327 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9256 (IC base=+0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.911` → IC=+0.220 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.911 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.2302` → IC=+0.316 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2302 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` < `1.4472` → IC=+0.261 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4472 (IC base=+0.027)

- **PATRÓN** `volumen_spike_ratio` > `2.2649` → IC=+0.287 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2649 (IC base=+0.027)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.302 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.027)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.160 (n=1114)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1667 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0751` → IC=+0.413 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0751 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `2.7322` → IC=+0.407 (n=663)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.7322 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.402 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.166` → IC=+0.217 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.166 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1971` → IC=+0.200 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1971 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` > `0.688` → IC=+0.206 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.688 (IC base=+0.021)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.246 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` < `1.4262` → IC=+0.224 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4262 (IC base=+0.021)

- **PATRÓN** `volumen_spike_ratio` > `2.4828` → IC=+0.199 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4828 (IC base=+0.021)

- **PATRÓN** `ballena_activa_n` < `270.0` → IC=+0.236 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 270.0 (IC base=+0.021)

- **PATRÓN** `volumen_regimen` < `1.1716` → IC=+0.233 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1716 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.237 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.273` → IC=+0.299 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.273 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5383` → IC=+0.249 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5383 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1657` → IC=+0.249 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1657 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `197.0` → IC=+0.246 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 197.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.317 (n=914)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.280 (n=2876)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.272)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.313 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.693` → IC=+0.303 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.693 (IC base=+0.272)

- **PATRÓN** `volumen_pendiente_norm` < `0.1311` → IC=+0.283 (n=2531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1311 (IC base=+0.272)

- **PATRÓN** `volumen_spike_ratio` > `1.6037` → IC=+0.277 (n=2649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6037 (IC base=+0.272)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.281 (n=3243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.272)

- **PATRÓN** `libro_liquidez` > `2034.7208` → IC=+0.289 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2034.7208 (IC base=+0.272)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.292 (n=1645)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.272)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.320 (n=1606)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.1774` → IC=+0.313 (n=1059)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1774 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.319 (n=916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.296 (n=836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.294)

- **PATRÓN** `ibs_20min` < `0.375` → IC=+0.295 (n=2410)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.375 (IC base=+0.294)

- **PATRÓN** `ibs_20min` > `0.2697` → IC=+0.302 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2697 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.411` → IC=+0.304 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.411 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` < `0.1967` → IC=+0.294 (n=2362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1967 (IC base=+0.294)

- **PATRÓN** `volumen_pendiente_norm` > `0.342` → IC=+0.308 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.342 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` < `1.7297` → IC=+0.299 (n=1015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7297 (IC base=+0.294)

- **PATRÓN** `volumen_spike_ratio` > `2.6939` → IC=+0.305 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6939 (IC base=+0.294)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.295 (n=1219)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `1927.08` → IC=+0.307 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1927.08 (IC base=+0.294)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.300 (n=1046)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.294)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7357` → IC=-0.186 (n=1163)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7357
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=3492)

- **PATRÓN** `ibs_20min` > `0.8671` → IC=+0.168 (n=1123)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8671 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.1505` → IC=+0.235 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1505 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.3632` → IC=+0.233 (n=1569)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3632 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0079` → IC=+0.239 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0079 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` > `0.665` → IC=+0.232 (n=1423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.665 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.234 (n=1681)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.026)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.243 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.026)

- **PATRÓN** `volumen_spike_ratio` < `2.4657` → IC=+0.239 (n=1540)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4657 (IC base=+0.026)

- **PATRÓN** `ballena_activa_n` < `120.0` → IC=+0.253 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 120.0 (IC base=+0.026)

- **PATRÓN** `volumen_regimen` < `1.0289` → IC=+0.244 (n=969)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0289 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` < `0.1017` → IC=+0.249 (n=1019)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1017 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.296 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.794` → IC=+0.275 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.794 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.4427` → IC=+0.259 (n=350)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4427 (IC base=-0.000)

- **PATRÓN** `ballena_activa_n` < `122.0` → IC=+0.263 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 122.0 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7551` → IC=-0.225 (n=1989)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7551
  - _Potencial_: sin este filtro IC_bueno=+0.311 (n=1992)

- **FILTRO** `ibs_20min` > `0.64` → IC=-0.234 (n=961)

  - _Acción_: SKIP cuando `ibs_20min` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=2913)

- **FILTRO** `sigma_ewma_delta_pct` > `8.415` → IC=-0.248 (n=447)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.415
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=3427)

- **PATRÓN** `ibs_20min` > `0.7551` → IC=+0.311 (n=1992)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7551 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `0.2123` → IC=+0.342 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2123 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.415` → IC=+0.188 (n=623)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 9.415 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` < `0.8488` → IC=+0.336 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8488 (IC base=+0.043)

- **PATRÓN** `volumen_regimen` > `0.6999` → IC=+0.333 (n=1322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6999 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.330 (n=1530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=+0.043)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.353 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.043)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.351 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.043)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.347 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.043)

- **PATRÓN** `ibs_20min` < `0.64` → IC=+0.125 (n=2913)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.64 (IC base=+0.036)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.267 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` < `0.1592` → IC=+0.241 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1592 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.255 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=+0.036)

- **PATRÓN** `volumen_spike_ratio` < `2.4456` → IC=+0.252 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4456 (IC base=+0.036)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.268 (n=1306)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 50.0 (IC base=+0.036)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.353 (n=1848)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.309)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=798)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.309)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.318 (n=987)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.309)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.346 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.76 (IC base=+0.309)

- **PATRÓN** `dist_vwap_pct` > `0.2036` → IC=+0.334 (n=1152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2036 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.847` → IC=+0.329 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.847 (IC base=+0.309)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.072` → IC=+0.310 (n=2355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.072 (IC base=+0.309)

- **PATRÓN** `volumen_regimen` > `0.8634` → IC=+0.328 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8634 (IC base=+0.309)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.350 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.309)

- **PATRÓN** `volumen_spike_ratio` > `1.4307` → IC=+0.320 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4307 (IC base=+0.309)

- **PATRÓN** `libro_liquidez` > `2955.9488` → IC=+0.309 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2955.9488 (IC base=+0.309)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.343 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.309)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.342 (n=1463)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.310)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.318 (n=848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.310)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.311 (n=1078)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.310)

- **PATRÓN** `ibs_20min` < `0.3725` → IC=+0.333 (n=2194)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3725 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.621` → IC=+0.325 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.621 (IC base=+0.310)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.091` → IC=+0.311 (n=2608)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.091 (IC base=+0.310)

- **PATRÓN** `volumen_regimen` < `0.722` → IC=+0.315 (n=966)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.722 (IC base=+0.310)

- **PATRÓN** `volumen_regimen` > `1.2246` → IC=+0.341 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2246 (IC base=+0.310)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.360 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` < `1.4153` → IC=+0.322 (n=673)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4153 (IC base=+0.310)

- **PATRÓN** `volumen_spike_ratio` > `2.1396` → IC=+0.312 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1396 (IC base=+0.310)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.227 (n=4692)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0866` → IC=+0.199 (n=4690)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.0866 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=14575)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5544` → IC=+0.234 (n=14068)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5544 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1624` → IC=+0.209 (n=5584)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1624 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.281` → IC=+0.257 (n=3676)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.281 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1861` → IC=+0.165 (n=9334)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.1861 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.6224` → IC=+0.162 (n=9333)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 0.6224 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.205 (n=2032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.4506` → IC=+0.178 (n=4556)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.4506 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.61` → IC=+0.191 (n=4554)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.61 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `91.0` → IC=+0.197 (n=12983)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 91.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.184 (n=13601)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0111 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.0795` → IC=+0.226 (n=4537)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0795 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=5061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` < `0.5085` → IC=+0.239 (n=13597)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5085 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.908` → IC=+0.197 (n=2204)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 9.908 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.651` → IC=+0.185 (n=12036)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.651 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `1.1874` → IC=+0.166 (n=9691)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1874 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.2964` → IC=+0.225 (n=2021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2964 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.6529` → IC=+0.189 (n=4275)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6529 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.195 (n=12567)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 97.0 (IC base=+0.182)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.225 (n=788)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.3361` → IC=+0.235 (n=2354)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3361 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=870)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1596)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `0.9342` → IC=+0.296 (n=1569)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9342 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.834` → IC=+0.330 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.834 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.2811` → IC=+0.282 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2811 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` < `1.8402` → IC=+0.218 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8402 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.221 (n=2235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.234 (n=2568)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.234 (n=1427)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 13.0 (IC base=+0.221)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.269 (n=832)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.254)

- **PATRÓN** `drift_60min` |x|≤ `0.0656` → IC=+0.311 (n=612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0656 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.260 (n=1894)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` < `0.0265` → IC=+0.302 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0265 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` < `0.1008` → IC=+0.260 (n=1611)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1008 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.3017` → IC=+0.281 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3017 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.4444` → IC=+0.276 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4444 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.7435` → IC=+0.258 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7435 (IC base=+0.254)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.257 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.254)

- **PATRÓN** `libro_liquidez` > `1553.753` → IC=+0.256 (n=1639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1553.753 (IC base=+0.254)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.260 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 9.0 (IC base=+0.254)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.211 (n=708)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.064` → IC=+0.193 (n=709)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.064 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=2224)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.325` → IC=+0.219 (n=2120)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.325 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1873` → IC=+0.219 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1873 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.182` → IC=+0.217 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.182 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6932` → IC=+0.165 (n=933)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6932 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.188 (n=331)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.4144` → IC=+0.170 (n=695)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` < 1.4144 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.4896` → IC=+0.165 (n=693)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4896 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `224.0` → IC=+0.162 (n=901)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 224.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.174 (n=2229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0059 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2331` → IC=+0.176 (n=1960)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2331 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.186 (n=1062)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.207 (n=2227)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.361` → IC=+0.192 (n=426)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.361 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.197` → IC=+0.147 (n=1930)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 4.197 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` < `1.2068` → IC=+0.163 (n=2227)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 1.2068 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.0933` → IC=+0.151 (n=1908)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` < 0.0933 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.148 (n=682)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.4989` → IC=+0.153 (n=2106)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4989 (IC base=+0.148)

- **PATRÓN** `ballena_activa_n` < `223.0` → IC=+0.181 (n=900)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 223.0 (IC base=+0.148)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.233 (n=1085)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.395` → IC=+0.221 (n=2098)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.395 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.297 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.325` → IC=+0.305 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.325 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.212 (n=2064)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.230 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.7659` → IC=+0.211 (n=1021)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7659 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7115` → IC=+0.224 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7115 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.216 (n=2838)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1931.0684` → IC=+0.224 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1931.0684 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0116` → IC=+0.242 (n=2072)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0116 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.4243` → IC=+0.255 (n=1823)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4243 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.277 (n=784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0184` → IC=+0.296 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0184 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.38` → IC=+0.275 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.38 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3589` → IC=+0.289 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3589 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.75` → IC=+0.233 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.75 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1568` → IC=+0.239 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1568 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.234 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1917.6478` → IC=+0.240 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1917.6478 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.238 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.200 (n=1008)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0779` → IC=+0.199 (n=763)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0779 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.155 (n=2371)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.2958` → IC=+0.207 (n=2289)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2958 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1419` → IC=+0.196 (n=1363)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1419 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.618` → IC=+0.201 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.618 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.0218` → IC=+0.152 (n=2014)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0218 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6143` → IC=+0.145 (n=2289)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 0.6143 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.175 (n=931)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.8277` → IC=+0.145 (n=1496)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.8277 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.5215` → IC=+0.167 (n=748)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5215 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `7277.355` → IC=+0.194 (n=1038)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 7277.355 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `135.0` → IC=+0.152 (n=2226)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 135.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.156 (n=2418)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0073 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.3937` → IC=+0.146 (n=2417)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3937 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=1145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.6789` → IC=+0.187 (n=2417)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6789 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.562` → IC=+0.154 (n=593)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 9.562 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.8568` → IC=+0.159 (n=1612)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8568 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.3002` → IC=+0.197 (n=367)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.3002 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` < `1.8106` → IC=+0.137 (n=1516)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.8106 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `2.5645` → IC=+0.138 (n=758)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5645 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6806.7886` → IC=+0.188 (n=1096)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 6806.7886 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.134 (n=1970)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 113.0 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.179 (n=1165)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0106 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=1811)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.4839` → IC=+0.216 (n=2566)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4839 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1935` → IC=+0.192 (n=1460)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.1935 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.39` → IC=+0.285 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.39 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `1.175` → IC=+0.138 (n=2566)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.175 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.132 (n=2617)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.5481` → IC=+0.143 (n=1096)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 1.5481 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.128 (n=2679)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.02 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `2685.4936` → IC=+0.209 (n=1164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2685.4936 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `18.0` → IC=+0.152 (n=803)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 18.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.143 (n=2644)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.011 (IC base=+0.122)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.175 (n=881)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.141 (n=2699)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.6145` → IC=+0.222 (n=2643)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6145 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.442` → IC=+0.137 (n=2339)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 2.442 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `1.1848` → IC=+0.131 (n=2643)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 1.1848 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1649` → IC=+0.127 (n=2567)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1649 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.141 (n=363)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.442` → IC=+0.132 (n=825)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.442 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` > `2.456` → IC=+0.132 (n=824)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.456 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2571.9695` → IC=+0.187 (n=1198)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2571.9695 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.128 (n=2449)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 48.0 (IC base=+0.122)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.249 (n=2108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1693` → IC=+0.239 (n=1038)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1693 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.227 (n=2438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2128)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.6604` → IC=+0.258 (n=2359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6604 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1804` → IC=+0.230 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1804 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.4706` → IC=+0.225 (n=2128)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4706 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.656` → IC=+0.254 (n=1067)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.656 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.1704` → IC=+0.226 (n=2360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1704 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.232 (n=2359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2308` → IC=+0.266 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2308 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `2.461` → IC=+0.228 (n=2300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.461 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `1.8029` → IC=+0.231 (n=1532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8029 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=3071)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2557.1634` → IC=+0.228 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2557.1634 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0127` → IC=+0.234 (n=1058)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0127 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0226` → IC=+0.244 (n=1092)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0226 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0876` → IC=+0.260 (n=802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0876 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.233)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.234 (n=1076)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.43` → IC=+0.261 (n=2409)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.43 (IC base=+0.233)

- **PATRÓN** `dist_vwap_pct` > `0.2997` → IC=+0.243 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2997 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.326` → IC=+0.271 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.326 (IC base=+0.233)

- **PATRÓN** `volumen_regimen` > `0.6419` → IC=+0.237 (n=2405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6419 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.284 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `2.527` → IC=+0.229 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.527 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `1.4366` → IC=+0.236 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4366 (IC base=+0.233)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.207 (n=1559)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.185)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.193 (n=1181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0091 (IC base=+0.185)

- **PATRÓN** `drift_60min` |x|≤ `0.1295` → IC=+0.207 (n=1559)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1295 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=3556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.4911` → IC=+0.220 (n=3164)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4911 (IC base=+0.185)

- **PATRÓN** `dist_vwap_pct` > `0.7875` → IC=+0.205 (n=537)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7875 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.588` → IC=+0.215 (n=1537)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.588 (IC base=+0.185)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.206 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.185)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.193 (n=1274)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` < `1.4286` → IC=+0.196 (n=1149)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4286 (IC base=+0.185)

- **PATRÓN** `volumen_spike_ratio` > `2.4932` → IC=+0.187 (n=1149)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.4932 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.192 (n=3994)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.02 (IC base=+0.185)

- **PATRÓN** `libro_liquidez` > `2632.5087` → IC=+0.189 (n=3164)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2632.5087 (IC base=+0.185)

- **PATRÓN** `ibs_20min` < `0.6052` → IC=+0.127 (n=3418)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` < 0.6052 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.205 (n=428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.0989` → IC=+0.242 (n=424)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0989 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.216 (n=881)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.6402` → IC=+0.245 (n=641)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6402 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.3064` → IC=+0.205 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3064 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.068` → IC=+0.206 (n=416)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.068 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.647` → IC=+0.188 (n=1018)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 6.647 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.8759` → IC=+0.211 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8759 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0712` → IC=+0.192 (n=384)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0712 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.1928` → IC=+0.199 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1928 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `14710.2002` → IC=+0.194 (n=641)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 14710.2002 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.205 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 162.0 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.120 (n=1175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0058 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.6382` → IC=+0.143 (n=1033)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6382 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.1613` → IC=+0.145 (n=311)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1613 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `162.0` → IC=+0.175 (n=503)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 162.0 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.241 (n=750)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.207)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.208 (n=375)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.207)

- **PATRÓN** `drift_60min` |x|≤ `0.1256` → IC=+0.226 (n=494)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1256 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=1172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.207)

- **PATRÓN** `ibs_20min` > `0.379` → IC=+0.248 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.379 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` > `0.3577` → IC=+0.209 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3577 (IC base=+0.207)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.211 (n=1005)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.207)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.884` → IC=+0.246 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.884 (IC base=+0.207)

- **PATRÓN** `volumen_regimen` < `1.0196` → IC=+0.215 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0196 (IC base=+0.207)

- **PATRÓN** `volumen_pendiente_norm` > `0.1598` → IC=+0.235 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1598 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` < `1.4273` → IC=+0.214 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4273 (IC base=+0.207)

- **PATRÓN** `volumen_spike_ratio` > `1.7865` → IC=+0.220 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7865 (IC base=+0.207)

- **PATRÓN** `ibs_20min` < `0.112` → IC=+0.155 (n=375)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.112 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `8478.3955` → IC=+0.144 (n=510)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 8478.3955 (IC base=+0.065)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **FILTRO** `ibs_20min` > `0.7083` → IC=-0.168 (n=332)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7083
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=1000)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.202 (n=293)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.202 (n=792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.279 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.9532` → IC=+0.245 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9532 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.1` → IC=+0.245 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.1 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` < `0.8875` → IC=+0.197 (n=586)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8875 (IC base=+0.173)

- **PATRÓN** `volumen_regimen` > `0.7107` → IC=+0.180 (n=785)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 0.7107 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2298` → IC=+0.195 (n=165)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2298 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.195 (n=283)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.1499` → IC=+0.177 (n=385)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.1499 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=908)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `3007.4561` → IC=+0.192 (n=293)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3007.4561 (IC base=+0.173)

- **PATRÓN** `ibs_20min` < `0.3902` → IC=+0.146 (n=668)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.3902 (IC base=+0.036)

- **PATRÓN** `libro_liquidez` > `2614.2777` → IC=+0.137 (n=453)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2614.2777 (IC base=+0.036)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0242` → IC=+0.161 (n=222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0242 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.180 (n=223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0071 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.254` → IC=+0.180 (n=148)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.254 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 16.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.194 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 8.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.183 (n=200)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.56 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.3016` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3016 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `1.1494` → IC=+0.158 (n=255)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 1.1494 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.251` → IC=+0.188 (n=190)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.251 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` > `0.6182` → IC=+0.165 (n=222)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6182 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2439` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.2439 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.4605` → IC=+0.221 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4605 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` > `2.5669` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.5669 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.178 (n=259)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.03 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `2666.351` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 2666.351 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.149 (n=257)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.01 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.139 (n=181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 10.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.133 (n=257)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.6 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `1.1744` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1744 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.9046` → IC=+0.132 (n=172)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.9046 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `1.0671` → IC=+0.130 (n=117)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` > 1.0671 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.3609` → IC=+0.134 (n=110)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.3609 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.132 (n=237)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 19.0 (IC base=+0.119)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.232 (n=6128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=19121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4432` → IC=+0.231 (n=18366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4432 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.8858` → IC=+0.210 (n=2211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8858 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.184` → IC=+0.254 (n=4482)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.184 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.2206` → IC=+0.168 (n=12321)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2206 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.241` → IC=+0.207 (n=3325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.241 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.619` → IC=+0.194 (n=5961)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.619 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.203 (n=17016)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 109.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.195 (n=7373)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0057 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3746` → IC=+0.192 (n=14746)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3746 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.210 (n=6206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5882` → IC=+0.241 (n=16758)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5882 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.736` → IC=+0.202 (n=2321)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.736 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.523` → IC=+0.192 (n=16233)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 3.523 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6326` → IC=+0.167 (n=3768)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6326 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.292` → IC=+0.253 (n=2274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.292 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.6339` → IC=+0.200 (n=5305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6339 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.235 (n=5293)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3504` → IC=+0.231 (n=2984)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3504 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.242 (n=1438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=2015)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `0.9694` → IC=+0.322 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9694 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.3` → IC=+0.351 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.3 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2828` → IC=+0.293 (n=390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2828 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` < `1.4463` → IC=+0.231 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4463 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.2967` → IC=+0.239 (n=1302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2967 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=3212)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `2054.47` → IC=+0.234 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2054.47 (IC base=+0.230)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.256 (n=1841)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.230)

- **PATRÓN** `sigma_h` < `0.009` → IC=+0.268 (n=2567)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.009 (IC base=+0.264)

- **PATRÓN** `drift_60min` |x|≤ `0.1186` → IC=+0.289 (n=1130)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1186 (IC base=+0.264)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.271 (n=2362)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.264)

- **PATRÓN** `ibs_20min` < `0.5224` → IC=+0.289 (n=2567)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5224 (IC base=+0.264)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.005` → IC=+0.266 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.005 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` < `0.0964` → IC=+0.267 (n=2317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0964 (IC base=+0.264)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.288 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` < `1.5696` → IC=+0.267 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5696 (IC base=+0.264)

- **PATRÓN** `volumen_spike_ratio` > `2.6922` → IC=+0.277 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6922 (IC base=+0.264)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.265 (n=2917)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.264)

- **PATRÓN** `libro_liquidez` > `1787.14` → IC=+0.268 (n=1711)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1787.14 (IC base=+0.264)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.272 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.264)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.194 (n=992)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0029 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.1041` → IC=+0.161 (n=1311)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1041 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=3099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.2351` → IC=+0.201 (n=2976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2351 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.3208` → IC=+0.201 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3208 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.562` → IC=+0.162 (n=626)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.562 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.181` → IC=+0.150 (n=2748)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` < 4.181 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `0.6306` → IC=+0.175 (n=992)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6306 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` > `1.0768` → IC=+0.149 (n=1349)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0768 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.151 (n=2659)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.185 (n=427)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `2.1754` → IC=+0.156 (n=2565)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1754 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `1.5331` → IC=+0.153 (n=2603)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.5331 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `234.0` → IC=+0.180 (n=952)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 234.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.163 (n=2537)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0059 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.0778` → IC=+0.180 (n=846)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0778 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` < `0.692` → IC=+0.191 (n=2534)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.692 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.12` → IC=+0.156 (n=419)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.12 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.377` → IC=+0.141 (n=2554)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 6.377 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `1.1995` → IC=+0.151 (n=2533)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1995 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2196` → IC=+0.200 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2196 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.4364` → IC=+0.145 (n=2428)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4364 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.7828` → IC=+0.148 (n=1619)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7828 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=3287)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `264.0` → IC=+0.153 (n=1035)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 264.0 (IC base=+0.140)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.259 (n=1021)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.224 (n=2749)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.249` → IC=+0.323 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.249 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1312` → IC=+0.227 (n=2877)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1312 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `3.1781` → IC=+0.241 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1781 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3639)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1941.6984` → IC=+0.239 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1941.6984 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.246 (n=2542)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1778` → IC=+0.260 (n=1271)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1778 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=1085)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0443` → IC=+0.303 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0443 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.796` → IC=+0.292 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.796 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3466` → IC=+0.310 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3466 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1416` → IC=+0.250 (n=1839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1416 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.246 (n=1465)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1922.1432` → IC=+0.249 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1922.1432 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.248 (n=1794)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.200 (n=1055)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.4234` → IC=+0.156 (n=3163)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.4234 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=3282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` > `0.2358` → IC=+0.188 (n=3163)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2358 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1417` → IC=+0.169 (n=1639)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1417 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.03` → IC=+0.159 (n=1428)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.03 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.0551` → IC=+0.156 (n=2784)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0551 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2333` → IC=+0.189 (n=560)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2333 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `1.524` → IC=+0.158 (n=1359)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.524 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `2.1813` → IC=+0.150 (n=1400)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1813 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `5505.6409` → IC=+0.231 (n=1434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5505.6409 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.164 (n=1362)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 71.0 (IC base=+0.144)

- **PATRÓN** `sigma_h` < `0.0076` → IC=+0.153 (n=2641)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0076 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.4356` → IC=+0.139 (n=2641)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4356 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.130)

- **PATRÓN** `ibs_20min` < `0.7335` → IC=+0.184 (n=2641)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7335 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.249` → IC=+0.159 (n=529)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.249 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.167` → IC=+0.131 (n=2298)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 3.167 (IC base=+0.130)

- **PATRÓN** `volumen_regimen` < `0.6927` → IC=+0.147 (n=1162)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.6927 (IC base=+0.130)

- **PATRÓN** `volumen_pendiente_norm` > `0.2961` → IC=+0.221 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2961 (IC base=+0.130)

- **PATRÓN** `volumen_spike_ratio` > `1.5382` → IC=+0.139 (n=2272)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` > 1.5382 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `6553.9493` → IC=+0.212 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6553.9493 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.133 (n=1722)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 98.0 (IC base=+0.130)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.159 (n=1451)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0105 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.155 (n=2251)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 11.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.4368` → IC=+0.197 (n=3195)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4368 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `1.0247` → IC=+0.206 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0247 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.59` → IC=+0.264 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.59 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.8799` → IC=+0.142 (n=2130)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8799 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.123 (n=3329)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `2.4849` → IC=+0.124 (n=3121)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.4849 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.126 (n=3323)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.02 (IC base=+0.122)

- **PATRÓN** `libro_liquidez` > `2729.846` → IC=+0.245 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2729.846 (IC base=+0.122)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.138 (n=1064)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 23.0 (IC base=+0.122)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.154 (n=2677)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0102 (IC base=+0.115)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.149 (n=1015)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.128 (n=3139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 5.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.6627` → IC=+0.209 (n=3041)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6627 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.212` → IC=+0.137 (n=2921)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.212 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.6396` → IC=+0.143 (n=1014)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.6396 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.163 (n=523)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.115)

- **PATRÓN** `volumen_spike_ratio` < `1.4384` → IC=+0.148 (n=955)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4384 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2591.9948` → IC=+0.197 (n=1014)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2591.9948 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `45.0` → IC=+0.129 (n=2508)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 45.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0138` → IC=+0.257 (n=2672)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0138 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=3117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.243 (n=1993)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` > `0.6113` → IC=+0.273 (n=2670)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6113 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.1902` → IC=+0.249 (n=1592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1902 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.761` → IC=+0.272 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.761 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` < `1.2221` → IC=+0.240 (n=2990)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2221 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `0.6405` → IC=+0.238 (n=2988)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6405 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.235` → IC=+0.253 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.235 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1492` → IC=+0.249 (n=1321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1492 (IC base=+0.235)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2939.5218` → IC=+0.235 (n=996)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2939.5218 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.258 (n=1030)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.242 (n=2912)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.5157` → IC=+0.268 (n=3089)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5157 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.257` → IC=+0.276 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.257 (IC base=+0.235)

- **PATRÓN** `volumen_regimen` > `1.226` → IC=+0.262 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.226 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.2836` → IC=+0.299 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2836 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `1.4297` → IC=+0.237 (n=2885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4297 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.233 (n=2836)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 35.0 (IC base=+0.235)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.195 (n=5180)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.245 (n=1794)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.5084` → IC=+0.222 (n=5376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5084 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.230 (n=1935)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `0.9407` → IC=+0.253 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9407 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` > `0.6891` → IC=+0.212 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6891 (IC base=+0.212)

- **PATRÓN** `dist_vwap_pct` < `0.4272` → IC=+0.214 (n=3847)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4272 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.916` → IC=+0.220 (n=886)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.916 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.597` → IC=+0.213 (n=4789)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.597 (IC base=+0.212)

- **PATRÓN** `volumen_regimen` < `0.7068` → IC=+0.223 (n=1719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7068 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.213 (n=5029)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.220 (n=1513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` < `1.4541` → IC=+0.219 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4541 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.5922` → IC=+0.212 (n=1764)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5922 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.217 (n=4116)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `3720.1334` → IC=+0.221 (n=3584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3720.1334 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.242 (n=1304)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.3855` → IC=+0.215 (n=3429)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3855 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=1307)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.210 (n=1732)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` < `0.1859` → IC=+0.207 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1859 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.6629` → IC=+0.200 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6629 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.238` → IC=+0.191 (n=3576)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.238 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.829` → IC=+0.204 (n=3491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.829 (IC base=+0.193)

- **PATRÓN** `volumen_regimen` < `1.0967` → IC=+0.201 (n=3256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0967 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.197 (n=3572)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2233` → IC=+0.197 (n=792)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2233 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` < `1.5356` → IC=+0.199 (n=1690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5356 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `1.8175` → IC=+0.199 (n=2560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8175 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=5180)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.206 (n=2561)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.193)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.279 (n=725)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.0824` → IC=+0.290 (n=274)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0824 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.270 (n=866)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.4738` → IC=+0.284 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4738 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.651` → IC=+0.272 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.651 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` < `1.2271` → IC=+0.268 (n=822)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2271 (IC base=+0.262)

- **PATRÓN** `volumen_regimen` > `0.8786` → IC=+0.282 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8786 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.2917` → IC=+0.352 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2917 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.8179` → IC=+0.269 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8179 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `1.434` → IC=+0.261 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.434 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `16079.3165` → IC=+0.272 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16079.3165 (IC base=+0.262)

- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.251 (n=617)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.2856` → IC=+0.192 (n=1230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.2856 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.221 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.196 (n=518)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.1385` → IC=+0.202 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1385 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.603` → IC=+0.180 (n=633)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.603 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.6851` → IC=+0.196 (n=123)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6851 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.372` → IC=+0.202 (n=1372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.372 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.091` → IC=+0.194 (n=1229)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 1.091 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.1536` → IC=+0.197 (n=430)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1536 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `2.5013` → IC=+0.185 (n=1389)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` < 2.5013 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.1732` → IC=+0.185 (n=630)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.1732 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `14799.0504` → IC=+0.183 (n=633)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14799.0504 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `684.0` → IC=+0.190 (n=1351)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 684.0 (IC base=+0.178)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.195 (n=277)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0064 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.220 (n=376)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.195)

- **PATRÓN** `drift_60min` |x|≤ `0.5887` → IC=+0.205 (n=829)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5887 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=296)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` < `0.7037` → IC=+0.196 (n=554)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.7037 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.242 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.494` → IC=+0.238 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.494 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.2095` → IC=+0.238 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2095 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `1.8273` → IC=+0.202 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8273 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `2541.2134` → IC=+0.220 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2541.2134 (IC base=+0.195)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.200 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.238 (n=59)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.305 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.009 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.295 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.232 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` > `0.216` → IC=+0.271 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.216 (IC base=+0.237)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.445` → IC=+0.293 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.445 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.6123` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.6123 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `1.7721` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7721 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `2388.306` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2388.306 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.237)

### GBM_LATE_5M#ETH#5min
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.212 (n=1414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.458` → IC=+0.205 (n=1412)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.458 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=504)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.5186` → IC=+0.210 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5186 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.8757` → IC=+0.200 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8757 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.2131` → IC=+0.207 (n=1253)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2131 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8776` → IC=+0.199 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8776 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.2249` → IC=+0.206 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2249 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.1051` → IC=+0.200 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1051 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.1634` → IC=+0.198 (n=418)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.1634 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.4559` → IC=+0.204 (n=1383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4559 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=1447)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.204 (n=1150)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3855` → IC=+0.217 (n=1012)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3855 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.197 (n=768)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.4077` → IC=+0.192 (n=767)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` < 0.4077 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.6238` → IC=+0.191 (n=522)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.6238 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.6561` → IC=+0.193 (n=203)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.6561 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.2233` → IC=+0.190 (n=1109)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2233 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.388` → IC=+0.194 (n=1046)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 4.388 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6391` → IC=+0.220 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6391 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` > `0.721` → IC=+0.186 (n=1028)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.721 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.215 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1956` → IC=+0.195 (n=991)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 2.1956 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `1.7867` → IC=+0.190 (n=750)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 1.7867 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `6591.2804` → IC=+0.197 (n=1150)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6591.2804 (IC base=+0.187)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.206 (n=692)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.203 (n=814)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.260 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.7405` → IC=+0.240 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7405 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.23` → IC=+0.200 (n=425)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.23 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.7016` → IC=+0.230 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7016 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.195 (n=707)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.5649` → IC=+0.191 (n=335)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.5649 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.4815` → IC=+0.195 (n=254)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.4815 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=917)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `4300.4118` → IC=+0.227 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4300.4118 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.196 (n=773)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 52.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.217 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.206)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.208 (n=193)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.4982` → IC=+0.230 (n=509)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4982 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.242 (n=394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.7308` → IC=+0.232 (n=580)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7308 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.512` → IC=+0.212 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.512 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.3065` → IC=+0.208 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3065 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `0.7555` → IC=+0.216 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7555 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` > `0.9331` → IC=+0.211 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9331 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.225 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.2075` → IC=+0.239 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2075 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `3249.4269` → IC=+0.219 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3249.4269 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.250 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 29.0 (IC base=+0.206)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.152 (n=811)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0041 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.3871` → IC=+0.135 (n=1748)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.3871 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1458` → IC=+0.144 (n=897)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1458 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.93` → IC=+0.151 (n=385)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 10.93 (IC base=+0.066)

- **PATRÓN** `ibs_20min` < `0.04` → IC=+0.260 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.04 (IC base=+0.050)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.041` → IC=+0.175 (n=167)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 10.041 (IC base=+0.050)

- **PATRÓN** `volumen_pendiente_norm` > `0.1468` → IC=+0.157 (n=295)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` > 0.1468 (IC base=+0.050)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5135` → IC=-0.124 (n=251)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5135
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=512)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.129 (n=605)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0057 (IC base=+0.084)

- **PATRÓN** `ibs_20min` > `0.5135` → IC=+0.189 (n=512)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5135 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.1218` → IC=+0.169 (n=285)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1218 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.0639` → IC=+0.284 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0639 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.192 (n=89)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.060)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.141 (n=402)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.005 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.140 (n=295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 15.0 (IC base=+0.088)

- **PATRÓN** `ibs_20min` > `0.3981` → IC=+0.168 (n=570)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3981 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.1258` → IC=+0.186 (n=288)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1258 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.09` → IC=+0.222 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.09 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.0296` → IC=+0.248 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0296 (IC base=+0.016)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.617` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.617 (IC base=+0.016)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7297` → IC=+0.145 (n=404)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.7297 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.4676` → IC=+0.133 (n=208)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.4676 (IC base=+0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.115` → IC=+0.141 (n=129)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.115 (IC base=+0.027)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.148 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0111 (IC base=+0.076)

- **PATRÓN** `ibs_20min` < `0.15` → IC=+0.223 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.15 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` < `0.1685` → IC=+0.135 (n=250)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1685 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.377` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.377 (IC base=+0.076)

- **PATRÓN** `volumen_regimen` > `1.0982` → IC=+0.208 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0982 (IC base=+0.076)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.195 (n=80)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.076)

- **PATRÓN** `volumen_spike_ratio` > `1.8346` → IC=+0.167 (n=157)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 1.8346 (IC base=+0.076)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.331 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=259)

- **FILTRO** `dist_vwap_pct` > `0.2348` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2348
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=311)

- **FILTRO** `volumen_regimen` < `0.7732` → IC=-0.298 (n=82)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7732
  - _Potencial_: sin este filtro IC_bueno=-0.177 (n=246)

- **FILTRO** `libro_liquidez` < `903.6493` → IC=-0.214 (n=82)

  - _Acción_: SKIP cuando `libro_liquidez` < 903.6493
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=246)

- **FILTRO** `drift_60min` |x|> `0.1933` → IC=-0.331 (n=69)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1933
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=210)

- **FILTRO** `dist_vwap_pct` > `0.3644` → IC=-0.406 (n=30)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3644
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=255)

- **FILTRO** `sigma_ewma_delta_pct` > `10.138` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.138
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=259)

- **FILTRO** `volumen_pendiente_norm` > `0.057` → IC=-0.380 (n=23)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.057
  - _Potencial_: sin este filtro IC_bueno=-0.285 (n=175)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `volumen_regimen` < `1.1869` → IC=-0.288 (n=50)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.1869
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=51)

- **FILTRO** `sigma_h` > `0.0043` → IC=-0.318 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=97)

- **FILTRO** `volumen_regimen` > `0.8276` → IC=-0.348 (n=31)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8276
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=97)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.5786` → IC=-0.466 (n=27)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5786
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=83)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=87)

- **FILTRO** `ibs_20min` > `0.7162` → IC=-0.397 (n=37)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7162
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=72)

- **FILTRO** `volumen_spike_ratio` > `2.2319` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.2319
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=51)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.302 (n=94)

- **PATRÓN** `ibs_20min` > `0.9883` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9883 (IC base=-0.161)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.400 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=99)

- **FILTRO** `dist_vwap_pct` > `0.0608` → IC=-0.250 (n=26)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0608
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=91)

- **FILTRO** `volumen_regimen` < `0.7506` → IC=-0.339 (n=29)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7506
  - _Potencial_: sin este filtro IC_bueno=-0.189 (n=88)

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

- **FILTRO** `sigma_ewma_delta_pct` > `2.758` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.758
  - _Potencial_: sin este filtro IC_bueno=-0.306 (n=29)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1415` → IC=-0.121 (n=304)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1415
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=591)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.204 (n=194)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.163 (n=583)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.6667 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` > `0.5388` → IC=+0.240 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5388 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.658` → IC=+0.128 (n=318)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 3.658 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.636` → IC=+0.127 (n=430)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 2.636 (IC base=+0.122)

- **PATRÓN** `volumen_regimen` < `0.6187` → IC=+0.184 (n=194)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6187 (IC base=+0.122)

- **PATRÓN** `volumen_pendiente_norm` < `0.1513` → IC=+0.157 (n=488)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1513 (IC base=+0.122)

- **PATRÓN** `volumen_spike_ratio` < `1.5041` → IC=+0.179 (n=210)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5041 (IC base=+0.122)

- **PATRÓN** `ibs_20min` < `0.1415` → IC=+0.136 (n=591)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` < 0.1415 (IC base=+0.049)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.023` → IC=+0.167 (n=196)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.023 (IC base=+0.049)

- **PATRÓN** `libro_liquidez` > `3242.4514` → IC=+0.122 (n=448)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 3242.4514 (IC base=+0.049)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7036` → IC=-0.183 (n=58)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7036
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=175)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.156 (n=210)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0036 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.131 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 12.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.145 (n=119)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 6.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.1684` → IC=+0.181 (n=315)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` < 0.1684 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.2516` → IC=+0.136 (n=363)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2516 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.132` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 10.132 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `1.0304` → IC=+0.169 (n=143)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 1.0304 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.07` → IC=+0.127 (n=250)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.07 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2688` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2688 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `1.7861` → IC=+0.149 (n=189)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 1.7861 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `5390.0556` → IC=+0.137 (n=210)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 5390.0556 (IC base=+0.120)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=185)

- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.140 (n=109)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=212)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.126 (n=193)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0061 (IC base=+0.110)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.126 (n=129)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.110)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.151 (n=173)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.8015 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` < `0.0943` → IC=+0.138 (n=161)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.0943 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.169` → IC=+0.145 (n=201)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 9.169 (IC base=+0.110)

- **PATRÓN** `volumen_regimen` < `0.6141` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 0.6141 (IC base=+0.110)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.110)

- **PATRÓN** `volumen_spike_ratio` < `1.7963` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.7963 (IC base=+0.110)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.128 (n=162)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1618.25` → IC=+0.167 (n=193)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 1618.25 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.828` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.828 (IC base=+0.008)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2391` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2391
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=103)

- **FILTRO** `dist_vwap_pct` > `0.1699` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1699
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=117)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.288 (n=97)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.292 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.231)

- **PATRÓN** `ibs_20min` > `0.6111` → IC=+0.263 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6111 (IC base=+0.231)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.398 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.08` → IC=+0.336 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.08 (IC base=+0.231)

- **PATRÓN** `volumen_regimen` < `0.7917` → IC=+0.279 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7917 (IC base=+0.231)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.292 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.231)

- **PATRÓN** `volumen_spike_ratio` < `1.48` → IC=+0.361 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.48 (IC base=+0.231)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.060)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=80)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.324)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.324)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.324)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.392 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.324)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.324)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.237)

- **PATRÓN** `elapsed_s` > `187.9` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.9 (IC base=+0.237)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `2.3682` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3682 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.304 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.237)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.237)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.317 (n=80)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3447` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3447 (IC base=+0.324)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.324)

- **PATRÓN** `drift_15min` |x|≤ `1.0104` → IC=+0.457 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0104 (IC base=+0.324)

- **PATRÓN** `drift_60min` |x|≤ `0.9647` → IC=+0.392 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9647 (IC base=+0.324)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.413 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.324)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.237)

- **PATRÓN** `elapsed_s` > `187.9` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 187.9 (IC base=+0.237)

- **PATRÓN** `elapsed_s` < `216.8` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 216.8 (IC base=+0.237)

- **PATRÓN** `drift_15min` |x|≤ `2.3682` → IC=+0.306 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3682 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.6424` → IC=+0.304 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6424 (IC base=+0.237)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.317 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `1814.0` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1814.0 (IC base=+0.237)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2921.7454` → IC=+0.136 (n=460)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2921.7454 (IC base=+0.099)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2921.7454` → IC=+0.136 (n=460)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2921.7454 (IC base=+0.099)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=208)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.125 (n=70)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=154)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=208)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=436)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12409.8631` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 12409.8631
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=72)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `ballena_activa_n` > `63.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 63.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **PATRÓN** `liq_n` > `5.0` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `liq_n` > 5.0 (IC base=+0.060)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=3679)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=112)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=69)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=99)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=112)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.133 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.104 (n=132)

### LIQUIDACIONES_5M#BTC#5min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=21)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.120 (n=256)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.495 (IC base=+0.020)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1411)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1365)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=712)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=720)

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
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=439)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=420)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.145 (n=184)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.495 (IC base=+0.021)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=881)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=881)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=275)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=686)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=936)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=936)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=229)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=229)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.141 (n=76)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=168)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=306)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=273)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.120 (n=77)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=263)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=364)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=364)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=209)

- **FILTRO** `libro_liquidez` < `641.5292` → IC=-0.136 (n=130)

  - _Acción_: SKIP cuando `libro_liquidez` < 641.5292
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=264)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=275)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=203)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `restante_min` < `9.67` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `restante_min` < 9.67
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=75)

- **FILTRO** `lag_apertura_s` > `330.19` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `lag_apertura_s` > 330.19
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=76)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=44)

- **FILTRO** `restante_min` < `10.75` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `restante_min` < 10.75
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=45)

- **FILTRO** `lag_apertura_s` > `367.5` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `lag_apertura_s` > 367.5
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=50)

- **PATRÓN** `py_entrada` < `0.58` → IC=+0.130 (n=44)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.58 (IC base=+0.000)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.130 (n=71)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=37)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.227 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=22)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.174 (n=170)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.46 (IC base=+0.020)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.133 (n=175)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=206)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.48` → IC=-0.121 (n=381)

  - _Acción_: SKIP cuando `py_entrada` < 0.48
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=216)

- **FILTRO** `profundidad_ratio` < `43.3` → IC=-0.149 (n=149)

  - _Acción_: SKIP cuando `profundidad_ratio` < 43.3
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=448)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.129 (n=238)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=259)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.164 (n=105)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=452)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` > `0.61` → IC=-0.122 (n=88)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=268)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.141 (n=151)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=542)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=6708)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=20342)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.177 (n=6731)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=21098)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.191 (n=1211)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3755)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.177 (n=1154)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=3796)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1305)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.042)

- **PATRÓN** `libro_liquidez` > `1051.9682` → IC=+0.137 (n=2483)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1051.9682 (IC base=+0.042)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.128 (n=2322)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1314.6843` → IC=+0.150 (n=1683)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1314.6843 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.184 (n=958)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2993)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.205 (n=1189)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=3879)

- **PATRÓN** `ibs_20min` > `0.9653` → IC=+0.127 (n=1687)

  - _Acción_: Kelly boost +0.63€ cuando `ibs_20min` > 0.9653 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1761.8924` → IC=+0.122 (n=1687)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 1761.8924 (IC base=+0.037)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.155 (n=1217)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=3749)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2408)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=2332)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.189 (n=911)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=2800)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3690)

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
  - _Potencial_: sin este filtro IC_bueno=-0.101 (n=339)

- **FILTRO** `drift_20min_pct` |x|> `0.2067` → IC=-0.140 (n=112)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2067
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=340)

- **FILTRO** `libro_liquidez` < `3183.3406` → IC=-0.182 (n=149)

  - _Acción_: SKIP cuando `libro_liquidez` < 3183.3406
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=303)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=944)

- **FILTRO** `libro_liquidez` < `1786.4389` → IC=-0.161 (n=240)

  - _Acción_: SKIP cuando `libro_liquidez` < 1786.4389
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=723)

- **FILTRO** `ibs_20min` > `0.8917` → IC=-0.130 (n=533)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8917
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=535)

- **FILTRO** `libro_liquidez` < `2096.6661` → IC=-0.167 (n=352)

  - _Acción_: SKIP cuando `libro_liquidez` < 2096.6661
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=716)

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
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=90)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.138 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 17.0 (IC base=+0.030)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.132 (n=18599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=41536)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.296 (n=13945)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=46190)

- **FILTRO** `ibs_7min` < `0.2308` → IC=-0.231 (n=14993)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2308
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=45142)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.153 (n=20429)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=39706)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=18619)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=56867)

- **FILTRO** `ibs_7min` > `0.2847` → IC=-0.180 (n=18867)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2847
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=56619)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.152 (n=2620)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7964)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=2560)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=8024)

- **FILTRO** `ibs_7min` < `0.7121` → IC=-0.247 (n=3491)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7121
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=7093)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.148 (n=2594)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7990)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.276 (n=3105)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=-0.004 (n=9955)

- **FILTRO** `ibs_7min` > `0.7716` → IC=-0.212 (n=3264)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7716
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9796)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.129 (n=2416)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=7667)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2380)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7703)

- **FILTRO** `ibs_7min` < `0.7202` → IC=-0.205 (n=2520)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7202
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=7563)

- **FILTRO** `ballena_activa_n` > `155.0` → IC=-0.193 (n=2512)

  - _Acción_: SKIP cuando `ballena_activa_n` > 155.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=7571)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.259 (n=2543)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=7759)

- **FILTRO** `ibs_7min` > `0.2655` → IC=-0.191 (n=2573)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2655
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=7729)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.180 (n=2560)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7742)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.162 (n=2475)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=7602)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=2485)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=7592)

- **FILTRO** `ibs_7min` < `0.2941` → IC=-0.249 (n=3325)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2941
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=6752)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2271)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7806)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.258 (n=3245)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=10624)

- **FILTRO** `ibs_7min` > `0.7308` → IC=-0.178 (n=3467)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7308
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=10402)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.125 (n=3192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6566)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=2343)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7415)

- **FILTRO** `ibs_7min` < `0.723` → IC=-0.196 (n=2439)

  - _Acción_: SKIP cuando `ibs_7min` < 0.723
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=7319)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.190 (n=2420)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=7338)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.260 (n=2306)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=7865)

- **FILTRO** `ibs_7min` > `0.2749` → IC=-0.172 (n=2542)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2749
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7629)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.172 (n=2514)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=7657)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=2419)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=7371)

- **FILTRO** `ibs_7min` < `0.7143` → IC=-0.224 (n=3213)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7143
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=6577)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.221 (n=2331)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=7459)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.193 (n=3511)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=10958)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.297 (n=2370)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=7473)

- **FILTRO** `ibs_7min` < `0.1912` → IC=-0.225 (n=2459)

  - _Acción_: SKIP cuando `ibs_7min` < 0.1912
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7384)

- **FILTRO** `ballena_activa_n` > `9.0` → IC=-0.198 (n=2365)

  - _Acción_: SKIP cuando `ballena_activa_n` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=7478)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.222 (n=3351)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=10264)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.160 (n=301)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=1003)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1289)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.122 (n=215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=524)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.156 (n=158)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=581)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=860)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.122 (n=220)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=279)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=332)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=449)

- **FILTRO** `libro_liquidez` < `3257.9143` → IC=-0.156 (n=181)

  - _Acción_: SKIP cuando `libro_liquidez` < 3257.9143
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=544)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.139 (n=1266)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.131 (n=1156)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 14.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `3902.42` → IC=+0.146 (n=843)

  - _Acción_: Kelly boost +0.73€ cuando `total_vol_5m` < 3902.42 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3502.4912` → IC=+0.145 (n=573)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3502.4912 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.140 (n=412)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 10.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4382` → IC=+0.140 (n=98)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.4382 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.183 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 14.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `371.372` → IC=+0.144 (n=259)

  - _Acción_: Kelly boost +0.72€ cuando `total_vol_5m` < 371.372 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `2530.2591` → IC=+0.200 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2530.2591 (IC base=+0.134)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.130 (n=263)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.115)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.136 (n=234)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 14.0 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.125 (n=315)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.04 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `2019.6106` → IC=+0.127 (n=234)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 2019.6106 (IC base=+0.115)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.187 (n=164)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.185 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `381.6269` → IC=+0.209 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 381.6269 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `7573.3328` → IC=+0.145 (n=164)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 7573.3328 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `60.0` → IC=+0.191 (n=82)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 60.0 (IC base=+0.138)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4326` → IC=+0.228 (n=101)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4326 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.151)

- **PATRÓN** `total_vol_5m` < `4761.643` → IC=+0.189 (n=149)

  - _Acción_: Kelly boost +0.94€ cuando `total_vol_5m` < 4761.643 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `3106.4902` → IC=+0.172 (n=199)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 3106.4902 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.163 (n=93)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 28.0 (IC base=+0.151)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.145 (n=167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 10.0 (IC base=+0.105)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=160)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3557.0392` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3557.0392 (IC base=+0.105)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.284 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

- **FILTRO** `T_h` > `129.5348` → IC=-0.197 (n=176)

  - _Acción_: SKIP cuando `T_h` > 129.5348
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=530)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.176 (n=177)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0036 (IC base=-0.079)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.296 (n=52)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=157)

- **FILTRO** `T_h` > `87.9866` → IC=-0.259 (n=52)

  - _Acción_: SKIP cuando `T_h` > 87.9866
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=157)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.282 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.031)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0105` → IC=-0.180 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0105
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=47)

- **FILTRO** `pct_vs_K` |x|> `9.1619` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.1619
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=53)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.013` → IC=-0.265 (n=32)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=97)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.186 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0061 (IC base=-0.103)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.237 (n=427)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.110 (n=221)

- **FILTRO** `T_h` > `66.1685` → IC=-0.204 (n=485)

  - _Acción_: SKIP cuando `T_h` > 66.1685
  - _Potencial_: sin este filtro IC_bueno=-0.161 (n=163)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.238 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=420)

- **FILTRO** `pct_vs_K` |x|> `3.2846` → IC=-0.429 (n=138)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.2846
  - _Potencial_: sin este filtro IC_bueno=-0.148 (n=421)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0081` → IC=-0.194 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=55)

- **FILTRO** `T_h` > `71.159` → IC=-0.192 (n=141)

  - _Acción_: SKIP cuando `T_h` > 71.159
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=72)

- **FILTRO** `T_h` > `73.0783` → IC=-0.255 (n=149)

  - _Acción_: SKIP cuando `T_h` > 73.0783
  - _Potencial_: sin este filtro IC_bueno=-0.217 (n=51)

- **FILTRO** `pct_vs_K` |x|> `2.9643` → IC=-0.422 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9643
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=151)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` < `0.0085` → IC=-0.250 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0096` → IC=-0.323 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0096
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=64)

- **FILTRO** `T_h` > `69.4221` → IC=-0.266 (n=139)

  - _Acción_: SKIP cuando `T_h` > 69.4221
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=47)

- **FILTRO** `sigma_h` > `0.0091` → IC=-0.344 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=131)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.227 (n=42)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=132)

- **PATRÓN** `pct_vs_K` |x|≤ `0.7672` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `pct_vs_K` |x|≤ 0.7672 (IC base=-0.176)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0099` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `T_h` > `126.9278` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `T_h` > 126.9278
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0081` → IC=-0.287 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=136)

- **FILTRO** `T_h` > `71.5479` → IC=-0.201 (n=135)

  - _Acción_: SKIP cuando `T_h` > 71.5479
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=46)

- **FILTRO** `sigma_h` > `0.0152` → IC=-0.375 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0152
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=93)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.286 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=83)

- **FILTRO** `T_h` > `33.8406` → IC=-0.266 (n=92)

  - _Acción_: SKIP cuando `T_h` > 33.8406
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=31)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1208` → IC=+0.468 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1208 (IC base=+0.337)

- **PATRÓN** `sigma_h` < `0.0128` → IC=+0.359 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0128 (IC base=+0.337)

- **PATRÓN** `T_h` > `0.7452` → IC=+0.386 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7452 (IC base=+0.337)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.479 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.337)

- **PATRÓN** `edge` > `0.1005` → IC=+0.437 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1005 (IC base=+0.411)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.437 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.411)

- **PATRÓN** `T_h` < `0.6127` → IC=+0.439 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6127 (IC base=+0.411)

- **PATRÓN** `dist_50` > `0.3765` → IC=+0.445 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3765 (IC base=+0.411)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.471 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.411)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1506` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1506 (IC base=+0.205)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.281 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.205)

- **PATRÓN** `T_h` < `1.484` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.484 (IC base=+0.205)

- **PATRÓN** `dist_50` > `0.346` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.346 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.281 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.205)

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
- **PATRÓN** `edge` > `0.1745` → IC=+0.485 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1745 (IC base=+0.433)

- **PATRÓN** `sigma_h` < `0.0154` → IC=+0.466 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0154 (IC base=+0.433)

- **PATRÓN** `T_h` > `0.4292` → IC=+0.455 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4292 (IC base=+0.433)

- **PATRÓN** `dist_50` > `0.3691` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3691 (IC base=+0.433)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.433)

- **PATRÓN** `edge` > `0.2005` → IC=+0.469 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.2005 (IC base=+0.461)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.473 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.461)

- **PATRÓN** `T_h` < `0.8279` → IC=+0.455 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8279 (IC base=+0.461)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.461)

- **PATRÓN** `dist_50` > `0.4597` → IC=+0.492 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4597 (IC base=+0.461)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.466 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.461)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=340)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=409)

- **PATRÓN** `streak_estiramiento` < `0.3778` → IC=+0.126 (n=113)

  - _Acción_: Kelly boost +0.63€ cuando `streak_estiramiento` < 0.3778 (IC base=+0.010)

- **PATRÓN** `streak_estiramiento` < `0.829` → IC=+0.134 (n=277)

  - _Acción_: Kelly boost +0.67€ cuando `streak_estiramiento` < 0.829 (IC base=+0.058)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.138 (n=219)

  - _Acción_: Kelly boost +0.69€ cuando `ballena_activa_n` < 34.0 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `2502.8663` → IC=+0.138 (n=147)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 2502.8663 (IC base=+0.058)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=29)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `streak_estiramiento` > `0.4416` → IC=-0.222 (n=34)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.4416
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=106)

- **PATRÓN** `streak_estiramiento` < `0.2115` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `streak_estiramiento` < 0.2115 (IC base=+0.013)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.137 (n=133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.103)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.123 (n=104)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.103)

- **PATRÓN** `streak_estiramiento` < `0.437` → IC=+0.199 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.437 (IC base=+0.103)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.182 (n=124)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 34.0 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `2230.4824` → IC=+0.141 (n=129)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2230.4824 (IC base=+0.103)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=98)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=107)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=34)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=1042)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1335)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1244)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=1292)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` > `6.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=4246)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=14)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2373)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.191 (n=1300)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0048 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.187 (n=1300)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0121 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.1772` → IC=+0.186 (n=3432)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1772 (IC base=+0.170)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1911` → IC=+0.170 (n=1770)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio_macro` |x|> 0.1911 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=3603)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=3608)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.170)

- **PATRÓN** `ibs_15` > `0.54` → IC=+0.242 (n=3900)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.54 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.1291` → IC=+0.166 (n=1885)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1291 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.491` → IC=+0.155 (n=3556)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.491 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.303` → IC=+0.257 (n=1006)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.303 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `4618.1478` → IC=+0.184 (n=1300)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4618.1478 (IC base=+0.170)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1576)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.223 (n=670)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.258 (n=225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.258` → IC=+0.229 (n=223)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.258 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.227 (n=701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.206)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.272 (n=670)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.2377` → IC=+0.224 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2377 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.537` → IC=+0.299 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.537 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.208 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `libro_liquidez` > `8140.6057` → IC=+0.217 (n=670)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8140.6057 (IC base=+0.206)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.159 (n=793)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0067 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.159 (n=529)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.143)

- **PATRÓN** `drift_15min` |x|≤ `0.3986` → IC=+0.144 (n=265)

  - _Acción_: Kelly boost +0.72€ cuando `drift_15min` |x|≤ 0.3986 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1412` → IC=+0.153 (n=529)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.1412 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1262` → IC=+0.155 (n=317)

  - _Acción_: Kelly boost +0.78€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1262 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.152 (n=726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.146 (n=828)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.5173` → IC=+0.232 (n=793)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5173 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.161 (n=490)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.208` → IC=+0.270 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.208 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `5960.612` → IC=+0.163 (n=360)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 5960.612 (IC base=+0.143)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.8837` → IC=+0.240 (n=310)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8837 (IC base=+0.087)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=497)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.087)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `15.781` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 15.781 (IC base=+0.000)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0241` → IC=+0.231 (n=288)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0241 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1304` → IC=+0.222 (n=577)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1304 (IC base=+0.198)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3415` → IC=+0.224 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3415 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.198 (n=787)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.208 (n=773)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.198)

- **PATRÓN** `ibs_15` > `0.5294` → IC=+0.274 (n=865)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5294 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.213 (n=490)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.961` → IC=+0.228 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.961 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2955.9488` → IC=+0.293 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2955.9488 (IC base=+0.198)

- **PATRÓN** `ibs_15` < `0.1089` → IC=+0.167 (n=793)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.1089 (IC base=+0.070)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0057` → IC=+0.393 (n=223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0057 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1493` → IC=+0.381 (n=444)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1493 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1386` → IC=+0.388 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1386 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.377 (n=671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.400 (n=667)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1529` → IC=+0.384 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1529 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.159` → IC=+0.391 (n=219)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.159 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=810)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3860.1806` → IC=+0.373 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3860.1806 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.364 (n=300)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.397 (n=114)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.360)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.362 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.373 (n=155)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1436` → IC=+0.390 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1436 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=341)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.386 (n=341)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.1089` → IC=+0.375 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1089 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.166` → IC=+0.383 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.166 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `8065.6565` → IC=+0.383 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8065.6565 (IC base=+0.360)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.400 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.360)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.369 (n=327)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0063 (IC base=+0.370)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.387 (n=148)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.370)

- **PATRÓN** `drift_60min` |x|≤ `0.1062` → IC=+0.368 (n=218)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1062 (IC base=+0.370)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0833` → IC=+0.384 (n=292)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0833 (IC base=+0.370)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.387 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.370)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.393 (n=157)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.370)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.381 (n=149)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.370)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.412 (n=327)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.370)

- **PATRÓN** `dist_vwap_pct` > `0.4613` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4613 (IC base=+0.370)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.372 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.370)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.399 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.370)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.375 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.370)

- **PATRÓN** `libro_liquidez` > `4045.1116` → IC=+0.400 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4045.1116 (IC base=+0.370)

- **PATRÓN** `ballena_activa_n` < `153.0` → IC=+0.379 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 153.0 (IC base=+0.370)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.175 (n=2266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2268)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.214 (n=1763)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2771)

- **FILTRO** `libro_liquidez` < `4246.7655` → IC=-0.154 (n=2992)

  - _Acción_: SKIP cuando `libro_liquidez` < 4246.7655
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=1542)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.279 (n=1099)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6314 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.204 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.068)

- **PATRÓN** `dist_vwap_pct` < `0.2672` → IC=+0.197 (n=939)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2672 (IC base=-0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2296` → IC=+0.273 (n=1290)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2296 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3684` → IC=+0.284 (n=3868)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3684 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.6509` → IC=+0.276 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6509 (IC base=-0.011)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0336` → IC=-0.223 (n=2078)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0336
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=694)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.230 (n=693)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=2079)

- **FILTRO** `sigma_ewma_delta_pct` > `23.072` → IC=-0.269 (n=400)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.072
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=2372)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.162 (n=273)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0029 (IC base=+0.085)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.328 (n=364)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.281 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.3693` → IC=+0.285 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3693 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.254` → IC=+0.143 (n=239)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 19.254 (IC base=+0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1026` → IC=+0.226 (n=60)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1026 (IC base=-0.192)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1323` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1323 (IC base=-0.192)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.312 (n=67)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.192)

- **PATRÓN** `dist_vwap_pct` < `0.0415` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0415 (IC base=-0.192)

- **PATRÓN** `ballena_activa_n` < `288.0` → IC=+0.372 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 288.0 (IC base=-0.192)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=720)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.163 (n=488)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.160 (n=369)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0049 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0722` → IC=+0.191 (n=244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0722 (IC base=+0.152)

- **PATRÓN** `drift_15min` |x|≤ `0.4011` → IC=+0.152 (n=185)

  - _Acción_: Kelly boost +0.76€ cuando `drift_15min` |x|≤ 0.4011 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.195 (n=427)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.5867` → IC=+0.245 (n=554)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5867 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.4686` → IC=+0.164 (n=144)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.4686 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1597` → IC=+0.156 (n=434)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1597 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.257 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=720)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `9553.1781` → IC=+0.158 (n=185)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 9553.1781 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.252 (n=1456)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0078 (IC base=+0.247)

- **PATRÓN** `drift_15min` |x|≤ `0.7722` → IC=+0.259 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7722 (IC base=+0.247)

- **PATRÓN** `delta_ratio_macro` |x|> `0.154` → IC=+0.268 (n=971)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.154 (IC base=+0.247)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.249 (n=1299)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.247)

- **PATRÓN** `ibs_15` < `0.3777` → IC=+0.279 (n=1456)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3777 (IC base=+0.247)

- **PATRÓN** `dist_vwap_pct` > `0.6145` → IC=+0.266 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6145 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.392` → IC=+0.252 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.392 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.457` → IC=+0.252 (n=1523)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.457 (IC base=+0.247)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0106` → IC=-0.229 (n=260)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0106
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=782)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.249 (n=353)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.157 (n=689)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.279 (n=260)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=782)

- **FILTRO** `sigma_ewma_delta_pct` > `6.65` → IC=-0.201 (n=239)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.65
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=803)

- **FILTRO** `sigma_ewma_delta_pct` > `17.704` → IC=-0.147 (n=551)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.704
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=4374)

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

- **PATRÓN** `ibs_15` < `0.3824` → IC=+0.289 (n=648)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3824 (IC base=-0.037)

- **PATRÓN** `dist_vwap_pct` < `0.2566` → IC=+0.234 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2566 (IC base=-0.037)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.253 (n=617)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=618)

- **FILTRO** `drift_60min` |x|> `0.1514` → IC=-0.216 (n=308)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1514
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=927)

- **FILTRO** `sigma_ewma_delta_pct` > `7.426` → IC=-0.211 (n=386)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.426
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=849)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.211)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0695` → IC=+0.276 (n=797)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0695 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1174` → IC=+0.295 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1174 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.137` → IC=+0.317 (n=595)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.137 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7845` → IC=+0.353 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7845 (IC base=-0.025)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.200 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.082)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.155 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.082)

- **PATRÓN** `drift_15min` |x|≤ `0.3976` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3976 (IC base=+0.082)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.082)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.357 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.0974` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.0974 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `3810.744` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3810.744 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1533` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1533 (IC base=+0.054)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.200 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.082)

- **PATRÓN** `drift_60min` |x|≤ `0.1094` → IC=+0.155 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1094 (IC base=+0.082)

- **PATRÓN** `drift_15min` |x|≤ `0.3976` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.3976 (IC base=+0.082)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.082)

- **PATRÓN** `ibs_15` > `0.8357` → IC=+0.357 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8357 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.0974` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.0974 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `3810.744` → IC=+0.132 (n=36)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 3810.744 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` > `0.1533` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1533 (IC base=+0.054)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.289 (n=1166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.285)

- **PATRÓN** `drift_60min` |x|≤ `0.0538` → IC=+0.318 (n=389)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0538 (IC base=+0.285)

- **PATRÓN** `delta_ratio_macro` |x|> `0.149` → IC=+0.287 (n=777)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.149 (IC base=+0.285)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.224` → IC=+0.295 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.224 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.301 (n=1211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.285)

- **PATRÓN** `ibs_15` > `0.8388` → IC=+0.316 (n=1166)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8388 (IC base=+0.285)

- **PATRÓN** `dist_vwap_pct` > `0.2676` → IC=+0.318 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2676 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.453` → IC=+0.381 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.453 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `12071.9003` → IC=+0.302 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12071.9003 (IC base=+0.285)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.310 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.277)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.287 (n=284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.277)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.315 (n=209)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.277)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2643` → IC=+0.281 (n=208)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2643 (IC base=+0.277)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3892` → IC=+0.282 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3892 (IC base=+0.277)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.298 (n=656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.277)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.304 (n=625)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.277)

- **PATRÓN** `dist_vwap_pct` > `0.2523` → IC=+0.315 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2523 (IC base=+0.277)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.55` → IC=+0.374 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.55 (IC base=+0.277)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.278 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `16111.0352` → IC=+0.320 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16111.0352 (IC base=+0.277)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.305 (n=541)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0066 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1075` → IC=+0.313 (n=361)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1075 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1451` → IC=+0.296 (n=361)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1451 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1019` → IC=+0.333 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1019 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.310 (n=520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.293 (n=491)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8494` → IC=+0.325 (n=541)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8494 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.320 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.387` → IC=+0.377 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.387 (IC base=+0.292)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1254` → IC=-0.163 (n=87)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1254
  - _Potencial_: sin este filtro IC_bueno=-0.099 (n=262)

- **FILTRO** `ballena_activa_n` > `40.0` → IC=-0.136 (n=237)

  - _Acción_: SKIP cuando `ballena_activa_n` > 40.0
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=80)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.211 (n=119)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=367)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.183 (n=121)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=365)

- **FILTRO** `drift_15min` |x|> `0.3093` → IC=-0.139 (n=242)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3093
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=244)

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
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=153)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2203` → IC=-0.129 (n=95)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2203
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=96)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2065` → IC=-0.259 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2065
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=28)

- **FILTRO** `ballena_activa_n` > `595.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 595.0
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=32)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1149` → IC=-0.206 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1149
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=45)

- **FILTRO** `drift_15min` |x|> `0.1605` → IC=-0.340 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.1605
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0081` → IC=-0.177 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0081
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `drift_60min` |x|> `0.2521` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2521
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=30)

- **FILTRO** `ballena_activa_n` > `25.0` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `ballena_activa_n` > 25.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `drift_15min` |x|> `0.2309` → IC=-0.225 (n=38)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.2309
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

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
- **PATRÓN** `T_h` > `103.3918` → IC=+0.186 (n=466)

  - _Acción_: Kelly boost +0.93€ cuando `T_h` > 103.3918 (IC base=+0.180)

- **PATRÓN** `ratio` < `0.973` → IC=+0.396 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.180)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.353 (n=2378)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.334)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.377 (n=387)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.334)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `109.5528` → IC=+0.164 (n=218)

  - _Acción_: Kelly boost +0.82€ cuando `T_h` > 109.5528 (IC base=+0.144)

- **PATRÓN** `ratio` < `0.9838` → IC=+0.304 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9838 (IC base=+0.144)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.306 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.294)

- **PATRÓN** `ratio` > `1.0432` → IC=+0.413 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0432 (IC base=+0.294)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.232 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.225)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.398 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.225)

- **PATRÓN** `T_h` > `111.9952` → IC=+0.351 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9952 (IC base=+0.321)

- **PATRÓN** `ratio` > `1.0322` → IC=+0.389 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0322 (IC base=+0.321)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0788` → IC=+0.439 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0788 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.54 sube el IC de +0.170 a +0.242 en UPDOWN_GBM#15min (n=3900). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.206 a +0.272 en UPDOWN_GBM#BTC#15min (n=670). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5173 sube el IC de +0.143 a +0.232 en UPDOWN_GBM#ETH#15min (n=793). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8837 sube el IC de +0.087 a +0.240 en UPDOWN_GBM#SOL#15min (n=310). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5294 sube el IC de +0.198 a +0.274 en UPDOWN_GBM#XRP#15min (n=865). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1089 sube el IC de +0.070 a +0.167 en UPDOWN_GBM#XRP#15min (n=793). Ya aplicado como kelly_boost=+0.83€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6314 sube el IC de -0.068 a +0.279 en UPDOWN_GBM_15M_TARDIO (n=1099). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3684 sube el IC de -0.011 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=3868). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.085 a +0.328 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=364). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.192 a +0.312 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=67). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5867 sube el IC de +0.152 a +0.245 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=554). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3777 sube el IC de +0.247 a +0.279 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1456). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3824 sube el IC de -0.037 a +0.289 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=648). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.211 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.137 sube el IC de -0.025 a +0.317 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=595). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.082 a +0.357 en UPDOWN_GBM_ETH_15M_HORA7 (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8357 sube el IC de +0.082 a +0.357 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=19). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8388 sube el IC de +0.285 a +0.316 en UPDOWN_GBM_IBS_ALTO (n=1166). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.277 a +0.304 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=625). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8494 sube el IC de +0.292 a +0.325 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=541). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.365 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=667). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.360 a +0.386 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=341). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.370 a +0.412 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=327). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2017 | +0.090 | +217.46€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2017 | +0.090 | +217.46€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1625 | +0.094 | +188.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1625 | +0.094 | +188.73€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 284 | +0.070 | +11.30€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 284 | +0.070 | +11.30€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 809 | -0.008 | +88.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 809 | -0.008 | +88.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 6 | +0.000 | +1.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 618 | -0.034 | +55.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 618 | -0.034 | +55.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 149 | +0.089 | +26.84€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 42537 | -0.084 | -5424.67€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2461 | +0.053 | -272.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 40076 | -0.092 | -5152.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4603 | -0.117 | -759.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4603 | -0.117 | -759.79€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2461 | +0.053 | -272.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2461 | +0.053 | -272.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4545 | -0.113 | -873.83€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4545 | -0.113 | -873.83€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 11390 | -0.026 | -1192.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 11390 | -0.026 | -1192.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 11325 | -0.115 | -985.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 11325 | -0.115 | -985.68€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 8213 | -0.127 | -1340.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 8213 | -0.127 | -1340.39€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 39079 | -0.014 | +3236.73€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 10091 | +0.005 | +1636.29€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 28988 | -0.020 | +1600.43€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 39079 | -0.014 | +3236.73€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 10091 | +0.005 | +1636.29€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 28988 | -0.020 | +1600.43€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 157671 | +0.115 | -6282.74€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 19646 | +0.181 | -654.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 703 | -0.009 | -72.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 128014 | +0.107 | -5229.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 9308 | +0.097 | -325.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 21219 | +0.107 | -1305.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 64 | -0.167 | +8.75€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 21140 | +0.109 | -1302.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 30344 | +0.126 | -480.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5372 | +0.183 | -209.76€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 21206 | +0.120 | -133.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3724 | +0.080 | -114.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 21273 | +0.099 | -1490.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 79 | -0.117 | -4.10€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 21179 | +0.100 | -1474.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 33568 | +0.124 | -646.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 8621 | +0.177 | -196.12€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 21510 | +0.107 | -400.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3425 | +0.102 | -41.76€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 30023 | +0.115 | -1427.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5437 | +0.198 | -261.69€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 606 | +0.021 | -18.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 21821 | +0.096 | -977.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2159 | +0.119 | -169.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 21244 | +0.107 | -932.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 73 | -0.100 | +7.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 21158 | +0.108 | -940.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 25416 | +0.196 | -1573.34€ | 2 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 25416 | +0.196 | -1573.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5765 | +0.179 | -494.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5765 | +0.179 | -494.24€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 3374 | +0.203 | -84.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 3374 | +0.203 | -84.67€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5699 | +0.179 | -469.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5699 | +0.179 | -469.86€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4889 | +0.248 | -172.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4889 | +0.248 | -172.78€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5610 | +0.188 | -365.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5610 | +0.188 | -365.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1083 | +0.426 | -37.88€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1083 | +0.426 | -37.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 432 | +0.435 | -6.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 432 | +0.435 | -6.99€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 430 | +0.431 | -10.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 430 | +0.431 | -10.03€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 207 | +0.400 | -17.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 207 | +0.400 | -17.00€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 89120 | +0.201 | -6361.97€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 89120 | +0.201 | -6361.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 15322 | +0.185 | -1596.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 15322 | +0.185 | -1596.87€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 14386 | +0.225 | -474.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 14386 | +0.225 | -474.48€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 15281 | +0.180 | -1614.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 15281 | +0.180 | -1614.54€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 14488 | +0.218 | -575.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 14488 | +0.218 | -575.09€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 14775 | +0.203 | -944.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 14775 | +0.203 | -944.48€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 14868 | +0.198 | -1156.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 14868 | +0.198 | -1156.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 34189 | +0.117 | +249.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 34189 | +0.117 | +249.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 17003 | +0.119 | +202.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 17003 | +0.119 | +202.77€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 17186 | +0.114 | +46.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 17186 | +0.114 | +46.73€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2206 | +0.293 | -8.48€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2206 | +0.293 | -8.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1013 | +0.279 | -29.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1013 | +0.279 | -29.24€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1069 | +0.299 | +17.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1069 | +0.299 | +17.64€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 124 | +0.341 | +3.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 124 | +0.341 | +3.12€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1014 | +0.443 | +7.11€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1014 | +0.443 | +7.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 493 | +0.435 | -5.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 493 | +0.435 | -5.33€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 474 | +0.452 | +11.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 474 | +0.452 | +11.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 47 | +0.398 | +0.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 47 | +0.398 | +0.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1757 | +0.069 | -75.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 692 | +0.045 | -64.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1065 | +0.085 | -11.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1341 | +0.076 | -34.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 276 | +0.043 | -23.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1065 | +0.085 | -11.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 334 | +0.030 | -44.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 334 | +0.030 | -44.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 68123 | +0.101 | -1634.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 5500 | +0.091 | +65.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 62623 | +0.102 | -1699.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 37380 | +0.106 | -388.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 5500 | +0.091 | +65.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 31880 | +0.108 | -453.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 14174 | +0.110 | -56.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 14174 | +0.110 | -56.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 16569 | +0.083 | -1189.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 16569 | +0.083 | -1189.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 899 | +0.192 | -110.13€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 899 | +0.192 | -110.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 899 | +0.192 | -110.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 899 | +0.192 | -110.13€ | 3 | 4 |
| ✅ GBM_LATE_15M | 46587 | +0.096 | +24722.26€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 46587 | +0.096 | +24722.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7748 | +0.221 | +6525.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7748 | +0.221 | +6525.97€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 7063 | +0.179 | +5454.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 7063 | +0.179 | +5454.47€ | 0 | 20 |
| ✅ GBM_LATE_15M#DOGE | 8351 | +0.204 | +6477.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 8351 | +0.204 | +6477.49€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 6425 | +0.045 | +1867.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 6425 | +0.045 | +1867.04€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 6519 | -0.033 | +1408.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 6519 | -0.033 | +1408.23€ | 3 | 15 |
| ✅ GBM_LATE_15M#XRP | 10481 | -0.029 | +2989.06€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 10481 | -0.029 | +2989.06€ | 4 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 49807 | +0.085 | +27471.32€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 49807 | +0.085 | +27471.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 9645 | +0.001 | +4890.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 9645 | +0.001 | +4890.98€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 10623 | +0.009 | +2649.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 10623 | +0.009 | +2649.42€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6856 | +0.282 | +7475.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6856 | +0.282 | +7475.74€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 9146 | +0.013 | +2341.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 9146 | +0.013 | +2341.95€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7855 | +0.040 | +3289.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7855 | +0.040 | +3289.95€ | 3 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5682 | +0.310 | +6823.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5682 | +0.310 | +6823.27€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 36884 | +0.181 | +30191.87€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 36884 | +0.181 | +30191.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5581 | +0.235 | +5092.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5581 | +0.235 | +5092.65€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5795 | +0.149 | +4326.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5795 | +0.149 | +4326.02€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5940 | +0.221 | +5064.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5940 | +0.221 | +5064.28€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 6273 | +0.137 | +4888.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 6273 | +0.137 | +4888.50€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6944 | +0.124 | +5182.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6944 | +0.124 | +5182.44€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 6351 | +0.229 | +5638.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 6351 | +0.229 | +5638.00€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9900 | +0.129 | +4803.38€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9900 | +0.129 | +4803.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 448 | +0.162 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 448 | +0.162 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2846 | +0.136 | +1563.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2846 | +0.136 | +1563.16€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 474 | +0.151 | +244.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 474 | +0.151 | +244.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2992 | +0.136 | +1436.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2992 | +0.136 | +1436.83€ | 0 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2503 | +0.100 | +968.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2503 | +0.100 | +968.01€ | 1 | 14 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 637 | +0.135 | +299.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 637 | +0.135 | +299.81€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 46823 | +0.185 | +37782.73€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#15min | 46823 | +0.185 | +37782.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 7398 | +0.246 | +7024.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 7398 | +0.246 | +7024.16€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 7344 | +0.145 | +5074.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 7344 | +0.145 | +5074.78€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7929 | +0.232 | +7047.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7929 | +0.232 | +7047.96€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 7737 | +0.138 | +5550.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 7737 | +0.138 | +5550.64€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 8313 | +0.119 | +5763.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 8313 | +0.119 | +5763.18€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 8102 | +0.235 | +7322.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 8102 | +0.235 | +7322.01€ | 0 | 20 |
| ✅ GBM_LATE_5M | 12362 | +0.204 | +9722.99€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 12362 | +0.204 | +9722.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1037 | +0.245 | +978.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2956 | +0.209 | +2541.81€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2956 | +0.209 | +2541.81€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1183 | +0.198 | +885.27€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1183 | +0.198 | +885.27€ | 0 | 22 |
| ✅ GBM_LATE_5M#ETH | 3415 | +0.192 | +2387.31€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3415 | +0.192 | +2387.31€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 1818 | +0.192 | +1400.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1818 | +0.192 | +1400.35€ | 0 | 25 |
| ✅ GBM_LATE_5M#XRP | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1953 | +0.209 | +1529.48€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3946 | +0.060 | +1178.38€ | 0 | 7 |
| ✅ GBM_LATE_60M#60min | 3946 | +0.060 | +1178.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1432 | +0.074 | +481.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1432 | +0.074 | +481.30€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1279 | +0.061 | +416.67€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1279 | +0.061 | +416.67€ | 0 | 7 |
| ✅ GBM_LATE_60M#SOL | 1235 | +0.042 | +280.42€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1235 | +0.042 | +280.42€ | 0 | 10 |
| 🚫 GBM_LATE_60M_FADE | 613 | -0.250 | -27.41€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 613 | -0.250 | -27.41€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 229 | -0.249 | -16.24€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 229 | -0.249 | -16.24€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 219 | -0.238 | -2.09€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 219 | -0.238 | -2.09€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 165 | -0.261 | -9.07€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 165 | -0.261 | -9.07€ | 7 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1669 | +0.083 | +412.48€ | 1 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1669 | +0.083 | +412.48€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 652 | +0.078 | +150.29€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 652 | +0.078 | +150.29€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 578 | +0.053 | +91.44€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 578 | +0.053 | +91.44€ | 2 | 12 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 439 | +0.128 | +170.76€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 439 | +0.128 | +170.76€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 180 | +0.280 | +180.52€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 180 | +0.280 | +180.52€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 180 | +0.280 | +180.52€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 180 | +0.280 | +180.52€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3718 | +0.101 | +900.38€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3718 | +0.101 | +900.38€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3718 | +0.101 | +900.38€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3718 | +0.101 | +900.38€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 681 | -0.026 | -9.37€ | 4 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 681 | -0.026 | -9.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 6 | -0.037 | -1.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 210 | -0.019 | +1.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 210 | -0.019 | +1.33€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 27 | -0.155 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 157 | +0.022 | +5.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 157 | +0.022 | +5.97€ | 1 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 229 | -0.011 | -0.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 229 | -0.011 | -0.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 3897 | +0.015 | +89.30€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3897 | +0.015 | +89.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 185 | +0.029 | -0.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 185 | +0.029 | -0.77€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 807 | +0.012 | +33.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 807 | +0.012 | +33.73€ | 2 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 214 | -0.005 | -1.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 214 | -0.005 | -1.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1461 | +0.021 | +28.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1461 | +0.021 | +28.09€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 761 | +0.011 | +1.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 761 | +0.011 | +1.65€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 469 | +0.014 | +28.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 469 | +0.014 | +28.18€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1912 | -0.038 | -26.36€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1912 | -0.038 | -26.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 565 | -0.027 | -10.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 565 | -0.027 | -10.72€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 663 | -0.014 | +7.65€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 663 | -0.014 | +7.65€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 684 | -0.070 | -23.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 684 | -0.070 | -23.30€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 10561 | -0.029 | -33.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 5035 | -0.035 | -85.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 5526 | -0.023 | +51.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 327 | -0.041 | -13.42€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 166 | -0.012 | +3.17€ | 5 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 161 | -0.071 | -16.60€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2704 | -0.015 | +50.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1280 | -0.020 | +7.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1424 | -0.011 | +42.08€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1125 | -0.029 | +6.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 570 | -0.038 | -9.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 555 | -0.019 | +15.64€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 2336 | -0.039 | -63.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1094 | -0.048 | -54.46€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1242 | -0.031 | -9.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 2052 | -0.023 | +18.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 989 | -0.030 | -3.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1063 | -0.017 | +21.87€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 2017 | -0.038 | -31.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 936 | -0.047 | -29.32€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1081 | -0.031 | -1.68€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 54879 | -0.000 | +2778.95€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 54879 | -0.000 | +2778.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 9916 | +0.026 | +1267.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 9916 | +0.026 | +1267.31€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7838 | -0.034 | -121.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7838 | -0.034 | -121.40€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 10029 | +0.024 | +1030.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 10029 | +0.024 | +1030.64€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 7700 | -0.047 | -141.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 7700 | -0.047 | -141.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 9293 | -0.005 | +256.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 9293 | -0.005 | +256.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 10103 | +0.017 | +487.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 10103 | +0.017 | +487.92€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6816 | -0.057 | -152.27€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6816 | -0.057 | -152.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1234 | -0.002 | -17.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1234 | -0.002 | -17.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1845 | -0.072 | -38.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1845 | -0.072 | -38.30€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 62 | -0.031 | -1.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 62 | -0.031 | -1.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 786 | -0.121 | -34.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 786 | -0.121 | -34.88€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2031 | -0.071 | -34.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2031 | -0.071 | -34.12€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 858 | -0.016 | -26.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 858 | -0.016 | -26.02€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3371 | +0.004 | +0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3371 | +0.004 | +0.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 132 | -0.037 | -1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 132 | -0.037 | -1.23€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 193 | +0.013 | -0.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 193 | +0.013 | -0.26€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 191 | -0.008 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 191 | -0.008 | -2.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 135621 | -0.077 | +1661.35€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 135621 | -0.077 | +1661.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 23644 | -0.078 | +1213.36€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 23644 | -0.078 | +1213.36€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 20385 | -0.101 | -1047.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 20385 | -0.101 | -1047.58€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 23946 | -0.068 | +1197.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 23946 | -0.068 | +1197.62€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 19929 | -0.098 | -631.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 19929 | -0.098 | -631.16€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 24259 | -0.058 | +313.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 24259 | -0.058 | +313.73€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 23458 | -0.069 | +615.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 23458 | -0.069 | +615.39€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8884 | -0.034 | -179.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8884 | -0.034 | -179.97€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1002 | -0.017 | -19.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1002 | -0.017 | -19.42€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2043 | -0.047 | -28.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2043 | -0.047 | -28.58€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2611 | -0.026 | -40.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2611 | -0.026 | -40.03€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1224 | -0.058 | -28.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1224 | -0.058 | -28.88€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 995 | -0.030 | -31.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 995 | -0.030 | -31.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1821 | +0.124 | +746.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1685 | +0.129 | +734.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 391 | +0.134 | +189.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 391 | +0.134 | +189.95€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 349 | +0.115 | +118.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 349 | +0.115 | +118.49€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 327 | +0.138 | +162.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 327 | +0.138 | +162.46€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 296 | +0.151 | +163.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 296 | +0.151 | +163.02€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 322 | +0.105 | +100.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 322 | +0.105 | +100.11€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1669 | -0.017 | -27.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1669 | -0.017 | -27.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 313 | -0.002 | +8.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 313 | -0.002 | +8.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 300 | -0.026 | -4.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 300 | -0.026 | -4.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 423 | -0.053 | -42.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 423 | -0.053 | -42.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 358 | +0.008 | +4.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 358 | +0.008 | +4.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 275 | -0.002 | +6.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 275 | -0.002 | +6.16€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 970 | -0.072 | -46.61€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 450 | -0.108 | -79.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 348 | -0.134 | -65.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 102 | -0.019 | -14.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 341 | -0.031 | +25.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 243 | -0.018 | +28.58€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 98 | -0.060 | -3.59€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 179 | -0.058 | +7.84€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 147 | -0.064 | +3.96€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 32 | -0.029 | +3.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 738 | -0.082 | -32.83€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 232 | -0.038 | -13.79€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1207 | -0.205 | -70.52€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 471 | -0.206 | -43.88€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 413 | -0.208 | -43.15€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 58 | -0.183 | -0.74€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 409 | -0.208 | -33.13€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 360 | -0.218 | -39.63€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 49 | -0.128 | +6.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 327 | -0.199 | +6.49€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 304 | -0.196 | +3.78€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 23 | -0.220 | +2.71€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 1077 | -0.209 | -79.00€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 130 | -0.174 | +8.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 482 | +0.391 | +465.93€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#BTC | 80 | +0.171 | +63.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 80 | +0.171 | +63.15€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 110 | +0.366 | +102.82€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 110 | +0.366 | +102.82€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 292 | +0.456 | +299.97€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 292 | +0.456 | +299.97€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 482 | +0.391 | +465.93€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 787 | +0.036 | +62.02€ | 2 | 4 |
| ✅ STREAK_FADE_15M#15min | 787 | +0.036 | +62.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 307 | +0.021 | +2.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 307 | +0.021 | +2.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 64 | +0.000 | +0.08€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 64 | +0.000 | +0.08€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 78 | +0.000 | +3.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 78 | +0.000 | +3.29€ | 2 | 0 |
| ✅ STREAK_FADE_15M#XRP | 338 | +0.065 | +55.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 338 | +0.065 | +55.78€ | 1 | 6 |
| ✅ STREAK_FADE_5M | 3531 | -0.023 | -143.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3531 | -0.023 | -143.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 597 | -0.031 | -28.59€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 597 | -0.031 | -28.59€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 168 | -0.041 | -14.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 168 | -0.041 | -14.30€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1639 | -0.019 | -59.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1639 | -0.019 | -59.97€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 103 | -0.052 | -9.27€ | 6 | 0 |
| ✅ STREAK_FADE_60M#60min | 103 | -0.052 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 60 | -0.016 | -4.20€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 60 | -0.016 | -4.20€ | 0 | 2 |
| ✅ STREAK_MOM_5M | 11286 | +0.015 | +73.52€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11286 | +0.015 | +73.52€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2873 | +0.020 | +27.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2873 | +0.020 | +27.86€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2928 | +0.016 | +31.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2928 | +0.016 | +31.41€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2907 | +0.008 | -3.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2907 | +0.008 | -3.40€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2578 | +0.014 | +17.65€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2578 | +0.014 | +17.65€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 10295 | +0.014 | -46.77€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 10295 | +0.014 | -46.77€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4265 | +0.019 | -4.09€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4265 | +0.019 | -4.09€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3623 | +0.010 | -28.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3623 | +0.010 | -28.56€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2407 | +0.009 | -14.13€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2407 | +0.009 | -14.13€ | 1 | 0 |
| ✅ UPDOWN_GBM | 83037 | +0.055 | +7446.41€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 20311 | +0.084 | +4423.34€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2647 | +0.003 | +30.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 54811 | +0.052 | +2906.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4975 | +0.004 | +90.87€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6853 | +0.089 | +1075.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5200 | +0.070 | +378.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 18811 | +0.056 | +1618.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2754 | +0.087 | +644.24€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 730 | +0.005 | +12.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 12983 | +0.063 | +895.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 2238 | +0.001 | +63.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 106 | -0.074 | +2.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8784 | +0.071 | +930.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 7151 | +0.055 | +321.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 19599 | +0.046 | +1322.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4929 | +0.071 | +759.07€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 704 | +0.007 | +18.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 12083 | +0.046 | +525.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1785 | +0.007 | +17.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 98 | -0.110 | +1.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 18128 | +0.035 | +970.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 5176 | +0.035 | +428.66€ | 0 | 2 |
| ✅ UPDOWN_GBM#SOL#240min | 670 | -0.009 | +2.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11243 | +0.041 | +536.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 952 | +0.006 | +10.02€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 87 | -0.140 | -7.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10860 | +0.067 | +1530.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4321 | +0.104 | +1282.33€ | 0 | 10 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 6151 | +0.045 | +248.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 291 | -0.107 | -3.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 889 | +0.365 | +325.56€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 889 | +0.365 | +325.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 454 | +0.360 | +153.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 454 | +0.360 | +153.43€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 435 | +0.370 | +172.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 435 | +0.370 | +172.12€ | 0 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO | 20913 | -0.024 | +4928.50€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 20913 | -0.024 | +4928.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3860 | -0.114 | +140.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3860 | -0.114 | +140.75€ | 3 | 10 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2678 | +0.221 | +1748.15€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2678 | +0.221 | +1748.15€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5967 | -0.064 | +755.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5967 | -0.064 | +755.13€ | 5 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5742 | -0.065 | +1011.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5742 | -0.065 | +1011.21€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 253 | +0.061 | +24.66€ | 0 | 8 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 253 | +0.061 | +24.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 253 | +0.061 | +24.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 253 | +0.061 | +24.66€ | 0 | 8 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1554 | +0.285 | +1297.19€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1554 | +0.285 | +1297.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 833 | +0.277 | +646.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 833 | +0.277 | +646.32€ | 0 | 11 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 721 | +0.292 | +650.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 721 | +0.292 | +650.87€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 835 | -0.113 | -83.76€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 835 | -0.113 | -83.76€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 258 | -0.085 | -20.19€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 258 | -0.085 | -20.19€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 92 | -0.170 | -10.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 92 | -0.170 | -10.61€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 102 | -0.173 | -3.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 102 | -0.173 | -3.61€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 3901 | +0.301 | +1808.61€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1456 | +0.255 | +172.69€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1497 | +0.295 | +652.47€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 948 | +0.380 | +983.45€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.023 n=1035 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1035 IC=+0.023 PNL=+44.98€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 737 celda(s) pasan gate riguroso completo de 2756 evaluadas (n>=40) y 3827 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.036 < 0.08 — monitorear
  - _Datos_: n=5172 IC=+0.036 PNL=+425.82€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1497/15 IC=+0.295 PNL=+652.47€ | BTC: n=1456/15 IC=+0.255 PNL=+172.69€ | SOL: n=948/15 IC=+0.380 PNL=+983.45€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.140 n=849/60 | contraria IC=+0.190 n=887 | gap=-0.049 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=500, boost estimado=+0.017. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1784/40 IC=+0.007 PNL=+17.07€ | BTC#60min: n=2236/40 IC=+0.001 PNL=+63.31€ | SOL#60min: n=952/40 IC=+0.006 PNL=+10.02€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.047 n=604526 | tras_1loss IC=+0.096 n=459305 | tras_2loss IC=+0.066 n=185419/40 | gap=-0.019 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.193 > 0.08 con n=806 PNL=+595.92€
  - _Datos_: n=806 IC=+0.193 PNL=+595.92€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.08 con n=912 PNL=+510.53€
  - _Datos_: n=912 IC=+0.165 PNL=+510.53€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.162 > 0.08 con n=69 PNL=+34.91€
  - _Datos_: n=69 IC=+0.162 PNL=+34.91€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.332 > 0.1 con n=3185 PNL=+1757.53€
  - _Datos_: n=3185 IC=+0.332 PNL=+1757.53€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=784 IC=+0.071 PNL=+83.57€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=784 IC=+0.071 PNL=+83.57€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=91 IC=+0.188 PNL=+62.81€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=91 IC=+0.188 PNL=+62.81€

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
  - _Estado_: n=3343 IC=+0.006 PNL=+5.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3343 IC=+0.006 PNL=+5.26€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1629 IC=-0.000 PNL=+85.15€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1629 IC=-0.000 PNL=+85.15€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1035 IC=+0.023 PNL=+44.98€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1035 IC=+0.023 PNL=+44.98€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.170 > 0.1 con n=5197 PNL=+3128.30€
  - _Datos_: n=5197 IC=+0.170 PNL=+3128.30€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2750 IC=+0.088 PNL=+646.28€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2750 IC=+0.088 PNL=+646.28€

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
  - _Estado_: n=1064 IC=+0.039 PNL=+90.04€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1064 IC=+0.039 PNL=+90.04€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=136 IC=+0.000 PNL=-0.19€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=136 IC=+0.000 PNL=-0.19€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.280 n=180) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=180 IC=+0.280 PNL=+180.52€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.02 con n=1055 PNL=+442.99€
  - _Datos_: n=1055 IC=+0.124 PNL=+442.99€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=226 IC=-0.097 PNL=+16.29€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=226 IC=-0.097 PNL=+16.29€

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
  - _Estado_: n=32965 IC=+0.073 PNL=+4715.26€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=32965 IC=+0.073 PNL=+4715.26€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.133 < -0.1 con n=567 PNL=+77.98€
  - _Datos_: n=567 IC=-0.133 PNL=+77.98€

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
  - _Estado_: n=155 IC=-0.105 PNL=+2.13€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=155 IC=-0.105 PNL=+2.13€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.112 > 0.1 con n=876 PNL=+235.70€
  - _Datos_: n=876 IC=+0.112 PNL=+235.70€

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
  - _Estado_: n=35508 IC=-0.135 PNL=+2635.61€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=35508 IC=-0.135 PNL=+2635.61€

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
  - _Estado_: n=3607 IC=+0.132 PNL=+2252.06€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3607 IC=+0.132 PNL=+2252.06€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=8542 IC=+0.053 PNL=+687.26€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8542 IC=+0.053 PNL=+687.26€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.096 > 0.08 con n=3807 PNL=+2103.42€
  - _Datos_: n=3807 IC=+0.096 PNL=+2103.42€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.223 < -0.1 con n=3725 PNL=-333.78€
  - _Datos_: n=3725 IC=-0.223 PNL=-333.78€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.103 n=1876) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1876 IC=+0.103 PNL=+413.10€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.409 n=606) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=606 IC=+0.409 PNL=+867.68€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=15312 IC=+0.185 PNL=-1596.34€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=15312 IC=+0.185 PNL=-1596.34€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.227 > 0.1 con n=243 PNL=+166.17€
  - _Datos_: n=243 IC=+0.227 PNL=+166.17€
