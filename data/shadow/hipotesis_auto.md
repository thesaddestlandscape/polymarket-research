# Hipótesis automáticas — 2026-11-16 22:16 UTC
_Generado por shadow_postmortem.py sobre 1368985 resoluciones (PNL=+190158.53€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=729)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.196 (n=1050)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `61.0` → IC=+0.172 (n=346)

  - _Acción_: Kelly boost +0.86€ cuando `n_total_lado` > 61.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.8127` → IC=+0.266 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8127 (IC base=+0.122)

- **PATRÓN** `banda_z` > `8.409` → IC=+0.195 (n=332)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.409 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.138 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=1084)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=518)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.194 (n=915)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.505 (IC base=+0.124)

- **PATRÓN** `n_total_lado` > `64.0` → IC=+0.181 (n=296)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 64.0 (IC base=+0.124)

- **PATRÓN** `banda_hit_calibrado` > `0.8124` → IC=+0.269 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8124 (IC base=+0.124)

- **PATRÓN** `banda_z` > `8.629` → IC=+0.203 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.629 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.133 (n=783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 8.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=611)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=984)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `8821.377` → IC=+0.133 (n=235)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 8821.377 (IC base=+0.014)

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
- **FILTRO** `restante_s_al_confirmar` < `131.43` → IC=-0.218 (n=12329)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.43
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=36991)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `124.87` → IC=-0.257 (n=1226)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.87
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=3678)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.05` → IC=-0.283 (n=1254)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.05
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3763)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.75` → IC=-0.167 (n=3382)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.75
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=10153)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.87` → IC=-0.239 (n=3363)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.87
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=10089)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.13` → IC=-0.267 (n=2321)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.13
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=6966)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.209 (n=28990)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `8051.1298` → IC=+0.155 (n=2388)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 8051.1298 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.126 (n=25273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=30579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=22985)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8524)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6401.9564` → IC=+0.142 (n=3313)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6401.9564 (IC base=+0.124)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.185 (n=2202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.755` → IC=+0.358 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.755 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=2694)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `16274.6013` → IC=+0.181 (n=700)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 16274.6013 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1917)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2145)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=2749)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16068.6951` → IC=+0.185 (n=709)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16068.6951 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=2303)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=637)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.148 (n=1493)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.44 (IC base=+0.086)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=5274)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.170 (n=4682)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.378 (n=1754)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.205 (n=2515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.199)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=2927)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.145 (n=675)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 15.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.259 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.145 (n=1152)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.074)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.249 (n=972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 7.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.155 (n=744)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.278 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.306 (n=153)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=469)

- **PATRÓN** `py_entrada` > `0.55` → IC=+0.167 (n=469)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.55 (IC base=+0.050)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.135 (n=505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.133 (n=984)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.253 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.201 (n=23995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=21316)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.228 (n=8018)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=5770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.177 (n=5682)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.74 (IC base=+0.166)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=3492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.210 (n=2492)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.249 (n=1714)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.208)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=5634)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=5769)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.182 (n=4427)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4473)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.251 (n=3973)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.363 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.8 (IC base=+0.251)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.251)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=5515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.188 (n=4659)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 15.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.197 (n=1822)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=990)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4669.4566` → IC=+0.441 (n=643)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4669.4566 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.439 (n=407)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.443 (n=418)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `15188.1532` → IC=+0.445 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15188.1532 (IC base=+0.439)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.432 (n=396)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.423)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=393)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.423)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.440 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.423)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.429 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.423)

- **PATRÓN** `libro_liquidez` > `4774.0338` → IC=+0.425 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4774.0338 (IC base=+0.423)

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
- **FILTRO** `py_entrada` > `0.765` → IC=-0.306 (n=34)

  - _Acción_: SKIP cuando `py_entrada` > 0.765
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=19)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=37)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=28484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=33026)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.187 (n=4962)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 18.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=10579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.205 (n=7047)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=13843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=4594)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.223)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.184 (n=13875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.198 (n=11725)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.228 (n=4644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.260 (n=5764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.215 (n=4703)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.256 (n=4767)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.205 (n=4737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.241 (n=6855)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=11927)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=12762)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.31` → IC=+0.140 (n=11072)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.31 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5814)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.142 (n=5777)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=7311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.52` → IC=+0.142 (n=5502)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.52 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=6113)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.136 (n=7733)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `3.05` → IC=+0.136 (n=7321)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.05 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.307 (n=1447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `4010.9878` → IC=+0.295 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4010.9878 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.296 (n=453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.283)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.370 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.283)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.316 (n=706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=1030)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.394 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.296)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=983)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.438 (n=322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.433 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.442 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.450 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.440 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=440)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.441 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.442)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4931` → IC=+0.139 (n=18812)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4931 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.129 (n=19063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=13077)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9761` → IC=+0.246 (n=6271)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9761 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8265` → IC=+0.286 (n=1030)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8265 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.49` → IC=+0.189 (n=9435)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.49 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6963` → IC=+0.269 (n=5098)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6963 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3042` → IC=+0.252 (n=1951)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3042 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7468` → IC=+0.233 (n=4531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7468 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=9237)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4741.9684` → IC=+0.151 (n=6271)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4741.9684 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.123 (n=11845)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0064 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.5641` → IC=+0.145 (n=23676)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5641 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.1691` → IC=+0.194 (n=9592)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1691 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.194 (n=6514)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8585 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.236 (n=2383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `1.4548` → IC=+0.209 (n=16573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4548 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=16492)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.086)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.247 (n=1333)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3745` → IC=+0.213 (n=3998)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3745 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=1945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2675)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9841` → IC=+0.275 (n=1813)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9841 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.469` → IC=+0.275 (n=1785)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.469 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2345` → IC=+0.254 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2345 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4416` → IC=+0.211 (n=3835)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4416 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=4400)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.220 (n=2450)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.248 (n=2385)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0925` → IC=+0.275 (n=1192)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0925 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.242 (n=3723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.252 (n=1641)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.4811` → IC=+0.260 (n=3146)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4811 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.984` → IC=+0.247 (n=3665)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.984 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0709` → IC=+0.245 (n=3080)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0709 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.252 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.447` → IC=+0.243 (n=1140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.447 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.8606` → IC=+0.245 (n=2280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8606 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.243 (n=4096)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1782.84` → IC=+0.243 (n=2383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1782.84 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.242 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.242)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.236 (n=1137)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1124` → IC=+0.248 (n=1496)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1124 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=3564)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.224 (n=2414)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.8983` → IC=+0.257 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8983 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1933` → IC=+0.232 (n=1502)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1933 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.824` → IC=+0.263 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.824 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6982` → IC=+0.231 (n=3034)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6982 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.270 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4471` → IC=+0.248 (n=1118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4471 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.152 (n=3687)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0067 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0802` → IC=+0.160 (n=1227)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0802 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.145 (n=2630)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.3601` → IC=+0.205 (n=2454)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3601 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1442` → IC=+0.150 (n=3602)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1442 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.972` → IC=+0.140 (n=3366)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` < 3.972 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6285` → IC=+0.150 (n=1227)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6285 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0728` → IC=+0.157 (n=1503)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0728 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4413` → IC=+0.142 (n=3553)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4413 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=4784)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.186 (n=1172)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 171.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.204 (n=2832)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4467)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.256 (n=1638)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.966` → IC=+0.282 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.966 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0969` → IC=+0.194 (n=3805)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0969 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3512` → IC=+0.226 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3512 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.7279` → IC=+0.210 (n=1880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7279 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5144)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1997.4956` → IC=+0.203 (n=1414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1997.4956 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.224 (n=3473)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.222 (n=2633)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1789` → IC=+0.234 (n=1738)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1789 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=1501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.229 (n=1788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.274 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.776` → IC=+0.268 (n=429)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.776 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3464` → IC=+0.258 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3464 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1556` → IC=+0.232 (n=2536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1556 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1938)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1977.0484` → IC=+0.224 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1977.0484 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.226 (n=3778)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.171 (n=223)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=5122)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.144 (n=694)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0039 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.240 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1477` → IC=+0.347 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1477 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.5766` → IC=+0.341 (n=892)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5766 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.146` → IC=+0.210 (n=1524)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.146 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` > `1.1121` → IC=+0.356 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1121 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` < `0.1678` → IC=+0.344 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1678 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.3052` → IC=+0.346 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3052 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `1.5524` → IC=+0.356 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5524 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` > `2.2842` → IC=+0.344 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2842 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.346 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.0883` → IC=+0.187 (n=1337)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.0883 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` > `0.3475` → IC=+0.162 (n=654)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.3475 (IC base=+0.057)

- **PATRÓN** `dist_vwap_pct` < `0.1445` → IC=+0.158 (n=2463)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1445 (IC base=+0.057)

- **PATRÓN** `volumen_regimen` < `1.0014` → IC=+0.161 (n=2279)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0014 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.211 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.057)

- **PATRÓN** `volumen_spike_ratio` > `1.5059` → IC=+0.162 (n=2228)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5059 (IC base=+0.057)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.188 (n=152)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=820)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.131 (n=4980)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=2532)

- **FILTRO** `sigma_ewma_delta_pct` > `8.309` → IC=-0.232 (n=812)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.309
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=6700)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.179 (n=335)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.9797` → IC=+0.271 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9797 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.6239` → IC=+0.271 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6239 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.917` → IC=+0.159 (n=227)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.917 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.8502` → IC=+0.268 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8502 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6181` → IC=+0.289 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6181 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0797` → IC=+0.283 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0797 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.290 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5387` → IC=+0.267 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5387 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.277 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.158 (n=2532)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.2 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` < `0.3206` → IC=+0.286 (n=1211)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3206 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` < `0.6963` → IC=+0.294 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6963 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` > `1.043` → IC=+0.290 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.043 (IC base=-0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.0781` → IC=+0.314 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0781 (IC base=-0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.4353` → IC=+0.298 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4353 (IC base=-0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.4113` → IC=+0.293 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4113 (IC base=-0.033)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7937` → IC=-0.157 (n=3847)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7937
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=1983)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.174 (n=1218)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4612)

- **FILTRO** `ibs_20min` > `0.7329` → IC=-0.191 (n=2018)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7329
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=6057)

- **PATRÓN** `ibs_20min` > `0.7937` → IC=+0.138 (n=1983)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7937 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0349` → IC=+0.344 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0349 (IC base=-0.057)

- **PATRÓN** `volumen_regimen` > `0.7071` → IC=+0.317 (n=1048)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7071 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` < `0.1089` → IC=+0.301 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1089 (IC base=-0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.0787` → IC=+0.307 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0787 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` < `1.5902` → IC=+0.303 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5902 (IC base=-0.057)

- **PATRÓN** `volumen_spike_ratio` > `2.5185` → IC=+0.316 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5185 (IC base=-0.057)

- **PATRÓN** `dist_vwap_pct` > `1.0692` → IC=+0.281 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0692 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.275 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.2054` → IC=+0.284 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2054 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.290 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.4755` → IC=+0.266 (n=2248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4755 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4348` → IC=+0.272 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4348 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.191 (n=8208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0109 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8663` → IC=+0.283 (n=11144)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8663 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9582` → IC=+0.297 (n=1713)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9582 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.468` → IC=+0.167 (n=11039)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.468 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6926` → IC=+0.279 (n=8134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6926 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.295 (n=2037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6413` → IC=+0.285 (n=4759)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6413 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.308 (n=13926)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.160 (n=7963)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0105 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.5183` → IC=+0.172 (n=20989)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5183 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.2702` → IC=+0.282 (n=8335)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2702 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` < `0.6971` → IC=+0.280 (n=3530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6971 (IC base=+0.085)

- **PATRÓN** `volumen_regimen` > `1.1877` → IC=+0.286 (n=2676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1877 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` > `0.2941` → IC=+0.330 (n=1770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2941 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.4516` → IC=+0.304 (n=3968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4516 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` > `2.27` → IC=+0.303 (n=5392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.27 (IC base=+0.085)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.311 (n=11869)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.085)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8062` → IC=-0.139 (n=4364)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8062
  - _Potencial_: sin este filtro IC_bueno=+0.303 (n=2249)

- **FILTRO** `ibs_20min` > `0.7085` → IC=-0.237 (n=1474)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=4424)

- **FILTRO** `sigma_ewma_delta_pct` > `4.079` → IC=-0.238 (n=1256)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.079
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=4642)

- **PATRÓN** `ibs_20min` > `0.8062` → IC=+0.303 (n=2249)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8062 (IC base=+0.011)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.969` → IC=+0.184 (n=2204)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 2.969 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.327 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4491` → IC=+0.284 (n=696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4491 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.242` → IC=+0.306 (n=946)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.242 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.317 (n=1472)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.011)

- **PATRÓN** `ibs_20min` < `0.1722` → IC=+0.174 (n=1475)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1722 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` < `0.1512` → IC=+0.392 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1512 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.4238` → IC=+0.415 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4238 (IC base=-0.017)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.382 (n=1222)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1729` → IC=+0.229 (n=1022)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1729 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.1969` → IC=+0.214 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1969 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6955` → IC=+0.221 (n=2148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6955 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.243 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4147` → IC=+0.233 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4147 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` > `2.4623` → IC=+0.214 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4623 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `374.0` → IC=+0.231 (n=2378)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 374.0 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1434` → IC=+0.261 (n=1808)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1434 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` < `0.6815` → IC=+0.251 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6815 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `1.1575` → IC=+0.267 (n=582)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1575 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.305 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.5262` → IC=+0.260 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5262 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1427` → IC=+0.263 (n=767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1427 (IC base=+0.000)

- **PATRÓN** `ballena_activa_n` < `179.0` → IC=+0.284 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 179.0 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.320 (n=1548)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.284)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.294 (n=3425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.284)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.284)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.579` → IC=+0.304 (n=2302)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.579 (IC base=+0.284)

- **PATRÓN** `volumen_pendiente_norm` < `0.1307` → IC=+0.294 (n=3171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1307 (IC base=+0.284)

- **PATRÓN** `volumen_spike_ratio` > `3.2535` → IC=+0.298 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.2535 (IC base=+0.284)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.292 (n=4111)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.284)

- **PATRÓN** `libro_liquidez` > `1999.76` → IC=+0.294 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1999.76 (IC base=+0.284)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.303 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.284)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.333 (n=2097)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.306)

- **PATRÓN** `drift_60min` |x|≤ `0.1828` → IC=+0.323 (n=1384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1828 (IC base=+0.306)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.323 (n=1209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.306)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.306)

- **PATRÓN** `ibs_20min` > `0.1497` → IC=+0.316 (n=2096)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1497 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.119` → IC=+0.316 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.119 (IC base=+0.306)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.414` → IC=+0.306 (n=3254)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.414 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` < `0.1982` → IC=+0.306 (n=3116)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1982 (IC base=+0.306)

- **PATRÓN** `volumen_pendiente_norm` > `0.3444` → IC=+0.318 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3444 (IC base=+0.306)

- **PATRÓN** `volumen_spike_ratio` > `2.7493` → IC=+0.320 (n=1379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7493 (IC base=+0.306)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.307 (n=1546)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.306)

- **PATRÓN** `libro_liquidez` > `1875.9894` → IC=+0.311 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1875.9894 (IC base=+0.306)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.310 (n=2708)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.306)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7157` → IC=-0.180 (n=1548)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7157
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=4646)

- **PATRÓN** `dist_vwap_pct` > `0.152` → IC=+0.237 (n=1114)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.152 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.3643` → IC=+0.237 (n=2213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3643 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1628` → IC=+0.237 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1628 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.595` → IC=+0.234 (n=2224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.595 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.236 (n=2333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.247 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.4162` → IC=+0.241 (n=2159)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4162 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.4951` → IC=+0.236 (n=1929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4951 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.253 (n=2207)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.0916` → IC=+0.154 (n=1549)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.0916 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` > `0.7749` → IC=+0.260 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7749 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` < `0.162` → IC=+0.261 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.162 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `1.1864` → IC=+0.264 (n=1609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1864 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.6158` → IC=+0.258 (n=1608)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6158 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.304 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.7842` → IC=+0.288 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7842 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.4256` → IC=+0.278 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4256 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.284 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.009)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7447` → IC=-0.248 (n=2535)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7447
  - _Potencial_: sin este filtro IC_bueno=+0.313 (n=2539)

- **FILTRO** `ibs_20min` > `0.6129` → IC=-0.236 (n=1198)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6129
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=3615)

- **FILTRO** `sigma_ewma_delta_pct` > `8.264` → IC=-0.267 (n=551)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.264
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=4262)

- **PATRÓN** `ibs_20min` > `0.7447` → IC=+0.313 (n=2539)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7447 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.2233` → IC=+0.343 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2233 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.439` → IC=+0.157 (n=2059)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.439 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.835` → IC=+0.346 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.835 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `0.6908` → IC=+0.335 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6908 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.335 (n=1916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.274` → IC=+0.364 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.274 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.427` → IC=+0.362 (n=601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.427 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.353 (n=1617)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.6129` → IC=+0.159 (n=3615)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.6129 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.3229` → IC=+0.271 (n=1914)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3229 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.726` → IC=+0.129 (n=3772)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 4.726 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.6914` → IC=+0.279 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6914 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.0701` → IC=+0.297 (n=742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0701 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.7975` → IC=+0.281 (n=1196)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7975 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.289 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.060)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.356 (n=2347)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.318 (n=2651)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.316 (n=2758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` > `0.6524` → IC=+0.341 (n=2624)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6524 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `0.2136` → IC=+0.334 (n=1396)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2136 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.841` → IC=+0.335 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.841 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.0499` → IC=+0.341 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0499 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2827` → IC=+0.345 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2827 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `1.5318` → IC=+0.327 (n=2264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5318 (IC base=+0.314)

- **PATRÓN** `libro_liquidez` > `2995.6878` → IC=+0.328 (n=875)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2995.6878 (IC base=+0.314)

- **PATRÓN** `ballena_activa_n` < `32.0` → IC=+0.338 (n=2078)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 32.0 (IC base=+0.314)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.333 (n=2820)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.315)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.316 (n=2825)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.315)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.316 (n=2827)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.315)

- **PATRÓN** `ibs_20min` < `0.384` → IC=+0.332 (n=2821)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.384 (IC base=+0.315)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.299` → IC=+0.328 (n=522)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.299 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` < `0.7185` → IC=+0.318 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7185 (IC base=+0.315)

- **PATRÓN** `volumen_regimen` > `1.2063` → IC=+0.343 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2063 (IC base=+0.315)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.371 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` < `1.4118` → IC=+0.322 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4118 (IC base=+0.315)

- **PATRÓN** `volumen_spike_ratio` > `2.1412` → IC=+0.318 (n=1195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1412 (IC base=+0.315)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.220 (n=6030)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1243` → IC=+0.192 (n=7957)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1243 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=18808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5377` → IC=+0.229 (n=18084)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5377 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1645` → IC=+0.205 (n=6814)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1645 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.991` → IC=+0.254 (n=4733)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.991 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.152 (n=12061)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1753 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6222` → IC=+0.151 (n=12061)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` > 0.6222 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.206 (n=2622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5992` → IC=+0.185 (n=5868)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5992 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.191 (n=17022)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 86.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.192 (n=7909)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.006 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.187 (n=11979)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.083` → IC=+0.222 (n=5987)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.083 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=6751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.248 (n=15829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.492` → IC=+0.191 (n=2840)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.492 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.507` → IC=+0.193 (n=15994)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 2.507 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `1.1858` → IC=+0.166 (n=12751)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1858 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.221 (n=2694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.6294` → IC=+0.197 (n=5713)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6294 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.201 (n=16929)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.186)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.262 (n=989)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.0749` → IC=+0.258 (n=989)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0749 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.233 (n=3093)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.226 (n=2008)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.9427` → IC=+0.291 (n=1976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9427 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.479` → IC=+0.325 (n=973)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.479 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2317` → IC=+0.279 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2317 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `1.8356` → IC=+0.225 (n=1888)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8356 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.226 (n=2832)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.259 (n=2472)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.267 (n=1650)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.256)

- **PATRÓN** `drift_60min` |x|≤ `0.0983` → IC=+0.309 (n=1088)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0983 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=2553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.263 (n=2254)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.256)

- **PATRÓN** `ibs_20min` < `0.4423` → IC=+0.274 (n=2474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4423 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.957` → IC=+0.261 (n=2438)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.957 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` < `0.0729` → IC=+0.258 (n=2058)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0729 (IC base=+0.256)

- **PATRÓN** `volumen_pendiente_norm` > `0.3008` → IC=+0.274 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3008 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` < `1.4466` → IC=+0.271 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4466 (IC base=+0.256)

- **PATRÓN** `volumen_spike_ratio` > `2.6858` → IC=+0.259 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6858 (IC base=+0.256)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.264 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.256)

- **PATRÓN** `libro_liquidez` > `1782.98` → IC=+0.260 (n=1648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1782.98 (IC base=+0.256)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.254 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.256)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.195 (n=919)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0032 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.0652` → IC=+0.175 (n=919)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0652 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=2888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.2597` → IC=+0.205 (n=2757)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2597 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1871` → IC=+0.213 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1871 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.619` → IC=+0.209 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.619 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.6238` → IC=+0.134 (n=919)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6238 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` > `1.0491` → IC=+0.133 (n=1250)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.0491 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.170 (n=425)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.7731` → IC=+0.131 (n=1808)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.7731 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `2.4599` → IC=+0.142 (n=904)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4599 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `394.0` → IC=+0.133 (n=2679)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 394.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.179 (n=2607)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0058 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.2463` → IC=+0.173 (n=2607)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2463 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=1411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.152)

- **PATRÓN** `ibs_20min` < `0.4532` → IC=+0.223 (n=2607)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4532 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.885` → IC=+0.177 (n=553)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 10.885 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.025` → IC=+0.157 (n=2585)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.025 (IC base=+0.152)

- **PATRÓN** `volumen_regimen` < `1.2016` → IC=+0.162 (n=2962)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2016 (IC base=+0.152)

- **PATRÓN** `volumen_pendiente_norm` < `0.2285` → IC=+0.154 (n=3152)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.2285 (IC base=+0.152)

- **PATRÓN** `volumen_spike_ratio` < `2.4713` → IC=+0.155 (n=2836)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4713 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `206.0` → IC=+0.198 (n=1220)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 206.0 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.223 (n=2041)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.2521` → IC=+0.232 (n=2040)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2521 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=3198)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=1621)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.044` → IC=+0.307 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.044 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.242 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.71` → IC=+0.224 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.71 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3706)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1991.5584` → IC=+0.220 (n=1020)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1991.5584 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.247 (n=2410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.2476` → IC=+0.270 (n=1826)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2476 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.277 (n=1051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.04` → IC=+0.294 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.04 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.896` → IC=+0.280 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.896 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3536` → IC=+0.289 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3536 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` < `1.7675` → IC=+0.241 (n=1166)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7675 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1802` → IC=+0.252 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1802 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `1871.1484` → IC=+0.247 (n=1242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1871.1484 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.239 (n=1806)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.195 (n=996)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.180 (n=996)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3094)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.245` → IC=+0.189 (n=2988)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.245 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1435` → IC=+0.188 (n=1694)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1435 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.186` → IC=+0.204 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.186 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8386` → IC=+0.137 (n=1992)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8386 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.177 (n=450)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.519` → IC=+0.126 (n=1288)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.519 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5053` → IC=+0.137 (n=976)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5053 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6891.5439` → IC=+0.196 (n=1355)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6891.5439 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.126 (n=2941)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 125.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.164 (n=2811)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0069 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4144` → IC=+0.150 (n=3195)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4144 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6713` → IC=+0.189 (n=3195)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6713 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.164` → IC=+0.158 (n=3259)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.164 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.499` → IC=+0.141 (n=1097)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 6.499 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.151 (n=2130)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8509 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.177 (n=478)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.1878` → IC=+0.134 (n=2675)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1878 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4105` → IC=+0.136 (n=3038)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4105 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6480.0421` → IC=+0.193 (n=1449)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6480.0421 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.152 (n=1011)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.169 (n=1109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0127 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3420)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.4722` → IC=+0.204 (n=3326)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4722 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.2027` → IC=+0.187 (n=1769)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2027 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.014` → IC=+0.286 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.014 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1636` → IC=+0.130 (n=3325)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1636 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1624` → IC=+0.122 (n=3393)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1624 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.7825` → IC=+0.124 (n=2152)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.7825 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2687.1156` → IC=+0.195 (n=1508)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2687.1156 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=1116)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 16.0 (IC base=+0.119)

- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.142 (n=3485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0121 (IC base=+0.123)

- **PATRÓN** `drift_60min` |x|≤ `0.1164` → IC=+0.165 (n=1162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1164 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` < `0.4878` → IC=+0.239 (n=3068)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4878 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.237` → IC=+0.145 (n=3082)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 2.237 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `1.1787` → IC=+0.129 (n=3485)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1787 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.8594` → IC=+0.127 (n=2323)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` > 0.8594 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` < `0.1619` → IC=+0.127 (n=3436)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1619 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.146 (n=487)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.4338` → IC=+0.145 (n=1101)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4338 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.4432` → IC=+0.135 (n=1101)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` > 2.4432 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `2590.1864` → IC=+0.192 (n=1580)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2590.1864 (IC base=+0.123)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.130 (n=3306)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 44.0 (IC base=+0.123)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.247 (n=2995)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1669` → IC=+0.241 (n=1317)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1669 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2699)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6646` → IC=+0.256 (n=2993)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6646 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1821` → IC=+0.232 (n=1832)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1821 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8039` → IC=+0.227 (n=3093)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8039 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.534` → IC=+0.258 (n=1378)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.534 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.236 (n=2993)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2348` → IC=+0.266 (n=562)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2348 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4697` → IC=+0.228 (n=2921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4697 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4339` → IC=+0.230 (n=2921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4339 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2600.356` → IC=+0.232 (n=1995)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2600.356 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.242 (n=1369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0122 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.017` → IC=+0.247 (n=2073)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.017 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.6053` → IC=+0.249 (n=3111)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6053 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.251 (n=1527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1391)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0364` → IC=+0.302 (n=1369)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0364 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `1.1517` → IC=+0.252 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1517 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.101` → IC=+0.272 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.101 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` < `0.87` → IC=+0.241 (n=2074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.87 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` > `1.0462` → IC=+0.247 (n=1410)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0462 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.2818` → IC=+0.297 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2818 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.838` → IC=+0.239 (n=1961)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.838 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `1.5489` → IC=+0.241 (n=2628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5489 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `2960.6154` → IC=+0.241 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2960.6154 (IC base=+0.241)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.208 (n=1578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1396` → IC=+0.172 (n=2079)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1396 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.4215` → IC=+0.201 (n=4219)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4215 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2285` → IC=+0.176 (n=1764)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2285 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.538` → IC=+0.210 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.538 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8605` → IC=+0.168 (n=2848)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8605 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.1939` → IC=+0.163 (n=1424)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` > 1.1939 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.1567` → IC=+0.175 (n=1239)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.1567 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.5264` → IC=+0.160 (n=2028)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5264 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.806` → IC=+0.159 (n=3071)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.806 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=4021)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7287.1688` → IC=+0.190 (n=2141)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7287.1688 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.3836` → IC=+0.177 (n=3443)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.3836 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.140 (n=2271)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 23.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.199 (n=1162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0062 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.1037` → IC=+0.226 (n=512)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1037 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.220 (n=1048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.6189` → IC=+0.245 (n=774)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6189 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.3129` → IC=+0.222 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3129 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.946` → IC=+0.218 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.946 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.878` → IC=+0.203 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.878 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0909` → IC=+0.204 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0909 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1671` → IC=+0.201 (n=1003)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1671 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `13747.0284` → IC=+0.195 (n=774)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 13747.0284 (IC base=+0.187)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.158 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0032 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.2095` → IC=+0.196 (n=639)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.2095 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `167.0` → IC=+0.172 (n=626)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 167.0 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.234 (n=634)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1293` → IC=+0.158 (n=632)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1293 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.174 (n=1493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.7791` → IC=+0.266 (n=652)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7791 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.5928` → IC=+0.193 (n=307)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.5928 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.907` → IC=+0.207 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.907 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.8339` → IC=+0.170 (n=958)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.8339 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` > `1.1627` → IC=+0.155 (n=479)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.1627 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2177` → IC=+0.200 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2177 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.4672` → IC=+0.186 (n=472)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4672 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `7910.2404` → IC=+0.180 (n=652)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 7910.2404 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.123 (n=958)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0054 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.0884` → IC=+0.206 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0884 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `0.6764` → IC=+0.137 (n=631)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6764 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `7750.0884` → IC=+0.155 (n=650)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 7750.0884 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.131 (n=622)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 42.0 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.147 (n=826)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0094 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.138 (n=1172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.5333` → IC=+0.183 (n=1109)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5333 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.9822` → IC=+0.152 (n=208)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.9822 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.884` → IC=+0.224 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.884 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `1.0426` → IC=+0.129 (n=1088)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0426 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.1558` → IC=+0.141 (n=329)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.1558 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `1.4101` → IC=+0.146 (n=399)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4101 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2766.3903` → IC=+0.150 (n=561)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2766.3903 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.36` → IC=+0.193 (n=911)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.36 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `2667.8187` → IC=+0.163 (n=619)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 2667.8187 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.129 (n=613)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 13.0 (IC base=+0.084)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0157` → IC=+0.238 (n=292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0157 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.224 (n=208)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `0.9524` → IC=+0.211 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9524 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.93` → IC=+0.196 (n=110)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.93 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` < `0.559` → IC=+0.186 (n=434)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.559 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.495` → IC=+0.199 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.495 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` > `1.2169` → IC=+0.250 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2169 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.218 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `2.1215` → IC=+0.197 (n=361)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1215 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.199 (n=459)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.03 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `2696.9888` → IC=+0.218 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2696.9888 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.169 (n=485)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` > 0.0105 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.3406` → IC=+0.163 (n=324)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.3406 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.196 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` < `0.3415` → IC=+0.163 (n=324)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3415 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.1` → IC=+0.157 (n=485)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.1 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.268 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.969` → IC=+0.153 (n=122)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 4.969 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.009` → IC=+0.153 (n=468)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.009 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.2424` → IC=+0.172 (n=485)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 1.2424 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.1134` → IC=+0.168 (n=450)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.1134 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.193 (n=86)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4792` → IC=+0.196 (n=156)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4792 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.6321` → IC=+0.165 (n=156)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.6321 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.169 (n=466)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 20.0 (IC base=+0.151)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.226 (n=7946)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=24888)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.9688` → IC=+0.303 (n=7948)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9688 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9061` → IC=+0.216 (n=2780)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9061 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.935` → IC=+0.260 (n=5848)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.935 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.8685` → IC=+0.163 (n=10707)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8685 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2407` → IC=+0.212 (n=4281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2407 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6218` → IC=+0.193 (n=7758)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6218 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.200 (n=22447)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 101.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.198 (n=7362)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0053 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.208 (n=7361)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1498` → IC=+0.202 (n=9714)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1498 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=8276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.253 (n=19427)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.1851` → IC=+0.181 (n=14092)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1851 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.515` → IC=+0.204 (n=20499)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.515 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0527` → IC=+0.173 (n=13030)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.0527 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2928` → IC=+0.256 (n=3032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2928 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.6212` → IC=+0.211 (n=7061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6212 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=20947)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.198)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.274 (n=1270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.3702` → IC=+0.235 (n=3800)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3702 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8626` → IC=+0.295 (n=2533)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8626 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.859` → IC=+0.340 (n=905)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.859 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.233` → IC=+0.286 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.233 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4492` → IC=+0.234 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4492 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2917` → IC=+0.240 (n=1666)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2917 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.248 (n=4170)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2019.92` → IC=+0.238 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2019.92 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.248 (n=2404)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.267 (n=3444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.269 (n=2296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1251` → IC=+0.294 (n=1515)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1251 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.267 (n=3578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=3107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.4663` → IC=+0.287 (n=3029)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4663 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.042` → IC=+0.269 (n=3586)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.042 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.1613` → IC=+0.268 (n=3481)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1613 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` > `0.2909` → IC=+0.286 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2909 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` < `1.5664` → IC=+0.272 (n=1457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5664 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.278 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2435)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1782.62` → IC=+0.270 (n=2295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1782.62 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.278 (n=1119)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.266)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.175 (n=1306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0032 (IC base=+0.140)

- **PATRÓN** `drift_60min` |x|≤ `0.08` → IC=+0.151 (n=1303)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.08 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=4079)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `ibs_20min` > `0.1945` → IC=+0.188 (n=3907)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1945 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.3304` → IC=+0.201 (n=1241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3304 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.302` → IC=+0.168 (n=817)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.302 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` < `0.6351` → IC=+0.157 (n=1303)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6351 (IC base=+0.140)

- **PATRÓN** `volumen_regimen` > `1.0679` → IC=+0.144 (n=1772)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0679 (IC base=+0.140)

- **PATRÓN** `volumen_pendiente_norm` > `0.2718` → IC=+0.188 (n=552)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2718 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.144 (n=3379)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.140)

- **PATRÓN** `volumen_spike_ratio` > `1.5145` → IC=+0.146 (n=3430)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5145 (IC base=+0.140)

- **PATRÓN** `ballena_activa_n` < `239.0` → IC=+0.161 (n=1666)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 239.0 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.171 (n=3021)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0815` → IC=+0.171 (n=1144)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0815 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=2424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.6803` → IC=+0.189 (n=3430)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6803 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1459` → IC=+0.158 (n=3369)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1459 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.981` → IC=+0.144 (n=3108)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.981 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.0413` → IC=+0.152 (n=3018)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0413 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2205` → IC=+0.196 (n=627)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2205 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4286` → IC=+0.146 (n=3319)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4286 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7677` → IC=+0.148 (n=2212)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7677 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=4458)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.164 (n=1091)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 217.0 (IC base=+0.142)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.238 (n=1325)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=4166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=3545)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=1477)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.985` → IC=+0.321 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.985 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1312` → IC=+0.224 (n=3765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1312 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.3496` → IC=+0.232 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3496 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.7431` → IC=+0.240 (n=1761)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7431 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.230 (n=4802)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1996.5606` → IC=+0.239 (n=1323)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1996.5606 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.250 (n=3365)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1813` → IC=+0.260 (n=1682)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1813 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.263 (n=1457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1737)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.303 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.029` → IC=+0.308 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.029 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3471` → IC=+0.303 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3471 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1714` → IC=+0.257 (n=2460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1714 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1887)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1971.202` → IC=+0.253 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1971.202 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.249 (n=3193)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.193 (n=1376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.147 (n=3631)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.8808` → IC=+0.270 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8808 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1436` → IC=+0.168 (n=2049)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1436 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.175` → IC=+0.167 (n=833)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.175 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.153 (n=2751)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8567 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.200 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5159` → IC=+0.156 (n=1776)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.5159 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.1549` → IC=+0.143 (n=1828)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.1549 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `5708.2817` → IC=+0.233 (n=1871)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5708.2817 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.145 (n=2680)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 86.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.168 (n=3475)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.008 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4496` → IC=+0.160 (n=3476)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4496 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=1283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.7038` → IC=+0.201 (n=3475)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7038 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1611` → IC=+0.164 (n=3288)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1611 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.018` → IC=+0.154 (n=3034)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.018 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8545` → IC=+0.162 (n=2317)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8545 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2932` → IC=+0.211 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2932 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1955` → IC=+0.154 (n=2959)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1955 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5242` → IC=+0.157 (n=3003)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5242 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `6687.9914` → IC=+0.220 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6687.9914 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.165 (n=2293)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 89.0 (IC base=+0.150)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.153 (n=1400)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0129 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.147 (n=2970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.255 (n=2805)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0308` → IC=+0.202 (n=686)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0308 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.245` → IC=+0.272 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.245 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8737` → IC=+0.133 (n=2797)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8737 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.123 (n=528)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.489` → IC=+0.121 (n=4093)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.489 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2749.8` → IC=+0.234 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2749.8 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.157 (n=3460)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0111 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.1416` → IC=+0.153 (n=1309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1416 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.169 (n=1859)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.242 (n=3460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5417 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.048` → IC=+0.157 (n=3805)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.048 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1903` → IC=+0.141 (n=3927)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1903 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2296` → IC=+0.200 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2296 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4353` → IC=+0.165 (n=1247)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4353 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2641.0193` → IC=+0.215 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2641.0193 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.147 (n=3767)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 49.0 (IC base=+0.135)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.258 (n=3833)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.245 (n=4012)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.242 (n=2560)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.6157` → IC=+0.271 (n=3424)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6157 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.1988` → IC=+0.251 (n=1943)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1988 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.1` → IC=+0.291 (n=677)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.1 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `1.2201` → IC=+0.239 (n=3833)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2201 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6435` → IC=+0.243 (n=3834)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6435 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2395` → IC=+0.258 (n=668)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2395 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.4972` → IC=+0.255 (n=1251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4972 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `2870.7742` → IC=+0.245 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2870.7742 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.267 (n=1328)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.248 (n=3750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.244 (n=4001)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.1358` → IC=+0.309 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1358 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.047` → IC=+0.280 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.047 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.244 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7156 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `1.2146` → IC=+0.264 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2146 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2848` → IC=+0.309 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2848 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4285` → IC=+0.248 (n=3765)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4285 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `2971.2126` → IC=+0.246 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2971.2126 (IC base=+0.244)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.232 (n=6178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.53` → IC=+0.233 (n=7018)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.53 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=7069)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9291` → IC=+0.261 (n=2341)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9291 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.938` → IC=+0.225 (n=5742)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.938 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.568` → IC=+0.231 (n=3493)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.568 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.231 (n=2185)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7053 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.8779` → IC=+0.224 (n=3311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8779 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.225 (n=6563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.232 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4471` → IC=+0.236 (n=2302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4471 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=5045)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `3701.6132` → IC=+0.231 (n=4678)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3701.6132 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.234 (n=1634)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.5229` → IC=+0.217 (n=4870)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5229 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.218 (n=1625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=2186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.6118` → IC=+0.211 (n=4285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6118 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.6919` → IC=+0.216 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6919 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.4334` → IC=+0.203 (n=4799)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4334 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.772` → IC=+0.220 (n=4407)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.772 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.2467` → IC=+0.208 (n=4487)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2467 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.209 (n=4502)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `1.5315` → IC=+0.209 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5315 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.1885` → IC=+0.217 (n=2175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1885 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.232 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.206)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.277 (n=824)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.269)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.271 (n=939)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.300 (n=313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.278 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.269 (n=940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.1406` → IC=+0.294 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1406 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` < `0.6768` → IC=+0.277 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6768 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` < `1.2303` → IC=+0.273 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2303 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `0.8791` → IC=+0.291 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8791 (IC base=+0.269)

- **PATRÓN** `volumen_pendiente_norm` > `0.2881` → IC=+0.346 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2881 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` < `2.4907` → IC=+0.276 (n=931)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4907 (IC base=+0.269)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.269 (n=422)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.269)

- **PATRÓN** `libro_liquidez` > `12881.3725` → IC=+0.281 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12881.3725 (IC base=+0.269)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.265 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.3869` → IC=+0.188 (n=1531)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3869 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=566)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.179 (n=571)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.197 (n=674)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.1382 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.7` → IC=+0.188 (n=139)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.7 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.835` → IC=+0.187 (n=1770)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 10.835 (IC base=+0.175)

- **PATRÓN** `volumen_regimen` < `1.0909` → IC=+0.188 (n=1347)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_regimen` < 1.0909 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` < `0.2705` → IC=+0.178 (n=1807)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` < 0.2705 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.193 (n=467)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` < `1.4122` → IC=+0.192 (n=508)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4122 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `1.8038` → IC=+0.179 (n=1015)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.8038 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `14600.5038` → IC=+0.175 (n=694)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 14600.5038 (IC base=+0.175)

- **PATRÓN** `ballena_activa_n` < `694.0` → IC=+0.188 (n=1486)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 694.0 (IC base=+0.175)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.238 (n=345)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.3088` → IC=+0.212 (n=688)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3088 (IC base=+0.209)

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

- **PATRÓN** `ibs_20min` > `0.7468` → IC=+0.259 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7468 (IC base=+0.228)

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
- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.222 (n=1891)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.4649` → IC=+0.218 (n=1890)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4649 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=673)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.472` → IC=+0.221 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.472 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.1473` → IC=+0.212 (n=1890)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1473 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.4059` → IC=+0.221 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4059 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.314` → IC=+0.217 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.314 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.8665` → IC=+0.217 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8665 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1013` → IC=+0.213 (n=1747)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1013 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.0749` → IC=+0.210 (n=796)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0749 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.3967` → IC=+0.231 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3967 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.243 (n=501)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.5009` → IC=+0.221 (n=1501)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5009 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.209 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.215 (n=1073)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.0867` → IC=+0.210 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0867 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.6674` → IC=+0.216 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6674 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.4175` → IC=+0.204 (n=1614)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4175 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.345` → IC=+0.209 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.345 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2537` → IC=+0.211 (n=1501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2537 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.7209` → IC=+0.204 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7209 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.228 (n=616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.51` → IC=+0.207 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.51 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.7739` → IC=+0.206 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7739 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `7795.6157` → IC=+0.213 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7795.6157 (IC base=+0.203)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.206 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 96.0 (IC base=+0.203)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.236 (n=536)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.220 (n=552)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.238 (n=1233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.217 (n=1110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.9863` → IC=+0.297 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9863 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.8369` → IC=+0.252 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8369 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.202` → IC=+0.251 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.202 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.6393` → IC=+0.250 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6393 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` < `0.106` → IC=+0.221 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.106 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2737` → IC=+0.228 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2737 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `2.1635` → IC=+0.225 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1635 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.225 (n=1433)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `4166.9791` → IC=+0.240 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4166.9791 (IC base=+0.216)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.241 (n=867)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.253 (n=578)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.6698` → IC=+0.256 (n=867)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6698 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.242 (n=797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.262 (n=606)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.267 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.5779` → IC=+0.241 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5779 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.981` → IC=+0.263 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.981 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` < `0.9122` → IC=+0.250 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9122 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.1044` → IC=+0.254 (n=775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1044 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1932` → IC=+0.267 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1932 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.241 (n=1126)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `3950.0252` → IC=+0.266 (n=578)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3950.0252 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `33.0` → IC=+0.276 (n=756)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 33.0 (IC base=+0.241)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.151 (n=798)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0039 (IC base=+0.054)

- **PATRÓN** `ibs_20min` > `0.7446` → IC=+0.184 (n=1534)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.7446 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.1519` → IC=+0.144 (n=1117)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1519 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.361` → IC=+0.137 (n=505)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 10.361 (IC base=+0.054)

- **PATRÓN** `ibs_20min` < `0.617` → IC=+0.143 (n=1657)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.617 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1474` → IC=+0.144 (n=448)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.1474 (IC base=+0.057)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.120 (n=667)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0055 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.5427` → IC=+0.160 (n=647)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.5427 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1276` → IC=+0.170 (n=334)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1276 (IC base=+0.068)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.127 (n=298)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0036 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.0659` → IC=+0.245 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0659 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2164` → IC=+0.154 (n=131)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2164 (IC base=+0.048)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.536` → IC=-0.137 (n=235)

  - _Acción_: SKIP cuando `ibs_20min` > 0.536
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=457)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.153 (n=344)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0043 (IC base=+0.068)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.124 (n=392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.068)

- **PATRÓN** `ibs_20min` > `0.9304` → IC=+0.259 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9304 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1316` → IC=+0.167 (n=358)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1316 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.623` → IC=+0.193 (n=161)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.623 (IC base=+0.068)

- **PATRÓN** `ibs_20min` < `0.105` → IC=+0.266 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.105 (IC base=+0.035)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.9778` → IC=+0.193 (n=278)

  - _Acción_: Kelly boost +0.96€ cuando `ibs_20min` > 0.9778 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.475` → IC=+0.136 (n=278)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.475 (IC base=+0.029)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.169 (n=351)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0098 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.1837` → IC=+0.249 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1837 (IC base=+0.091)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.982` → IC=+0.280 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.982 (IC base=+0.091)

- **PATRÓN** `volumen_regimen` > `1.1084` → IC=+0.201 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1084 (IC base=+0.091)

- **PATRÓN** `volumen_pendiente_norm` > `0.1605` → IC=+0.167 (n=130)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1605 (IC base=+0.091)

- **PATRÓN** `volumen_spike_ratio` > `1.4597` → IC=+0.136 (n=462)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4597 (IC base=+0.091)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.135 (n=242)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.03 (IC base=+0.091)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `7.0` → IC=-0.302 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=294)

- **FILTRO** `dist_vwap_pct` > `0.2422` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2422
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=373)

- **FILTRO** `volumen_regimen` < `0.8583` → IC=-0.308 (n=128)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8583
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=260)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.303 (n=211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=132)

- **FILTRO** `dist_vwap_pct` > `0.4497` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4497
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=324)

- **FILTRO** `sigma_ewma_delta_pct` > `9.539` → IC=-0.306 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.539
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=314)

- **FILTRO** `volumen_pendiente_norm` > `0.046` → IC=-0.375 (n=30)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.046
  - _Potencial_: sin este filtro IC_bueno=-0.255 (n=222)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `9.679` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.679
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=97)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.297 (n=57)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

- **FILTRO** `dist_vwap_pct` < `0.091` → IC=-0.282 (n=108)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.091
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=39)

- **FILTRO** `volumen_regimen` > `0.805` → IC=-0.316 (n=36)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=111)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `hora_utc` < `2.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=106)

- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.471 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=99)

- **FILTRO** `volumen_regimen` < `0.7435` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7435
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=99)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.368 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=98)

- **FILTRO** `ibs_20min` > `0.7492` → IC=-0.386 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7492
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=101)

- **FILTRO** `volumen_spike_ratio` < `1.442` → IC=-0.385 (n=24)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.442
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=75)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.293 (n=119)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `drift_60min` |x|> `0.2366` → IC=-0.361 (n=34)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2366
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `volumen_pendiente_norm` > `0.1196` → IC=-0.265 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1196
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=84)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=111)

- **FILTRO** `sigma_ewma_delta_pct` > `4.649` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.649
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=46)

- **FILTRO** `volumen_regimen` < `0.9169` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9169
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=42)

- **FILTRO** `libro_spread` > `0.05` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.05
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=43)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2457` → IC=-0.148 (n=305)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2457
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=919)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.239 (n=351)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.196 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 16.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` > `0.68` → IC=+0.188 (n=773)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.68 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.8341` → IC=+0.306 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8341 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.4` → IC=+0.176 (n=183)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.4 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.192 (n=258)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 0.6244 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.183 (n=578)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `1.3986` → IC=+0.205 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3986 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.855` → IC=+0.126 (n=271)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` > 8.855 (IC base=+0.029)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7302` → IC=-0.171 (n=74)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7302
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=225)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.162 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0066 (IC base=+0.048)

- **PATRÓN** `ibs_20min` > `0.7302` → IC=+0.121 (n=225)

  - _Acción_: Kelly boost +0.61€ cuando `ibs_20min` > 0.7302 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.6482` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6482 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.251` → IC=+0.141 (n=424)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.251 (IC base=+0.080)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.15` → IC=-0.129 (n=149)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=291)

- **PATRÓN** `drift_60min` |x|≤ `0.1051` → IC=+0.131 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.1051 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.135 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.7163` → IC=+0.152 (n=248)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` > 0.7163 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` < `0.1019` → IC=+0.154 (n=203)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1019 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.38` → IC=+0.147 (n=256)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 9.38 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 0.6249 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `1.1915` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 1.1915 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` < `1.7318` → IC=+0.178 (n=147)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.7318 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=214)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.689` → IC=+0.167 (n=79)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 10.689 (IC base=+0.007)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2308` → IC=-0.268 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2308
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=166)

- **FILTRO** `volumen_regimen` < `0.9345` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9345
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=110)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.277 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.276 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.283 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6842 (IC base=+0.254)

- **PATRÓN** `dist_vwap_pct` > `0.7481` → IC=+0.389 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7481 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.344 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.254)

- **PATRÓN** `volumen_regimen` < `0.6106` → IC=+0.306 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6106 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.092` → IC=+0.307 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.092 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.333 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.3472` → IC=+0.283 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3472 (IC base=+0.254)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.338 (n=152)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.344 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.339)

- **PATRÓN** `elapsed_s` > `208.3` → IC=+0.402 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.3 (IC base=+0.339)

- **PATRÓN** `drift_15min` |x|≤ `2.2981` → IC=+0.360 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2981 (IC base=+0.339)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.385 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.339)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.387 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.339)

- **PATRÓN** `ballena_activa_n` < `1054.0` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1054.0 (IC base=+0.339)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3492` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3492 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `2.3232` → IC=+0.333 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3232 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.8756` → IC=+0.316 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8756 (IC base=+0.289)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.338 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.386 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.289)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.338 (n=152)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3474` → IC=+0.344 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3474 (IC base=+0.339)

- **PATRÓN** `elapsed_s` > `208.3` → IC=+0.402 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.3 (IC base=+0.339)

- **PATRÓN** `drift_15min` |x|≤ `2.2981` → IC=+0.360 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.2981 (IC base=+0.339)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.385 (n=120)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.339)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.387 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.339)

- **PATRÓN** `ballena_activa_n` < `1054.0` → IC=+0.405 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1054.0 (IC base=+0.339)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3492` → IC=+0.310 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3492 (IC base=+0.289)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.289)

- **PATRÓN** `drift_15min` |x|≤ `2.3232` → IC=+0.333 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3232 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.8756` → IC=+0.316 (n=112)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.8756 (IC base=+0.289)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.338 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.289)

- **PATRÓN** `ballena_activa_n` < `1342.0` → IC=+0.386 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1342.0 (IC base=+0.289)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1496)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2854.854` → IC=+0.134 (n=757)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2854.854 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1496)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.5 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `2854.854` → IC=+0.134 (n=757)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2854.854 (IC base=+0.098)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=263)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=263)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=1146)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.190 (n=56)

  - _Acción_: Kelly boost +0.95€ cuando `liq_n` > 2.0 (IC base=+0.074)

- **PATRÓN** `liq_usd_total` > `1200.92` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1200.92 (IC base=+0.074)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.074)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `11682.4811` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `libro_liquidez` < 11682.4811
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=105)

### LIQUIDACIONES_15M#DOGE#15min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.141 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=47)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=69)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.214 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.058)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `1802.5` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_usd_total` < 1802.5
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `py_entrada` < `0.415` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.415
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=45)

- **PATRÓN** `liq_usd_total` > `5115.78` → IC=+0.122 (n=141)

  - _Acción_: Kelly boost +0.61€ cuando `liq_usd_total` > 5115.78 (IC base=+0.051)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=264)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4105)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=196)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.273 (n=64)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=153)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.278 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=183)

- **FILTRO** `ballena_activa_n` > `29.0` → IC=-0.167 (n=91)

  - _Acción_: SKIP cuando `ballena_activa_n` > 29.0
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=92)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.192 (n=92)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 29.0 (IC base=-0.025)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.121 (n=278)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.495 (IC base=+0.023)

### LIQUIDACIONES_5M#DOGE#5min
- **PATRÓN** `liq_n` > `3.0` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 3.0 (IC base=+0.190)

- **PATRÓN** `liq_usd_total` > `345.52` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 345.52 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.228 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.190)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.192 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.190)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.190)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1625)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=1579)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.286 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_5M#SOL#5min
- **FILTRO** `libro_spread` > `0.02` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=735)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=560)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=541)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.139 (n=225)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=+0.005)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=1070)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=1070)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1398)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=1398)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=316)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=316)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=387)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=436)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=318)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=421)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=421)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=394)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.123 (n=3057)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=7983)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.170 (n=101)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=118)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.139 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=124)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.153 (n=47)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=48)

- **FILTRO** `restante_min` < `3.99` → IC=-0.127 (n=65)

  - _Acción_: SKIP cuando `restante_min` < 3.99
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=30)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.141 (n=349)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=870)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.6` → IC=-0.155 (n=282)

  - _Acción_: SKIP cuando `py_entrada` > 0.6
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=793)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.142 (n=378)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.51 (IC base=-0.012)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.130 (n=182)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=407)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.123 (n=621)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=671)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.136 (n=317)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=678)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.131 (n=683)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=367)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.123 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=392)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.132 (n=566)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=642)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.176 (n=8540)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=26885)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=8949)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=27730)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.197 (n=1586)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=4997)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.142 (n=2198)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=4314)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.134 (n=1691)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 1.0 (IC base=+0.039)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.134 (n=3043)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.174 (n=1193)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=3682)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1263)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3874)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.196 (n=1624)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=5043)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.135 (n=2022)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `1742.4335` → IC=+0.124 (n=2236)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1742.4335 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `ibs_20min` < `0.7661` → IC=-0.153 (n=1190)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7661
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=3573)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1284)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=3949)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.161 (n=1639)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=4970)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2448)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2372)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3164)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4116)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1122)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.204 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=366)

- **FILTRO** `drift_20min_pct` |x|> `0.2022` → IC=-0.136 (n=119)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.2022
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=360)

- **FILTRO** `libro_liquidez` < `3246.2924` → IC=-0.181 (n=158)

  - _Acción_: SKIP cuando `libro_liquidez` < 3246.2924
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=321)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=979)

- **FILTRO** `libro_liquidez` < `1991.6564` → IC=-0.139 (n=397)

  - _Acción_: SKIP cuando `libro_liquidez` < 1991.6564
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=809)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=244)

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

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.133 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 17.0 (IC base=+0.029)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.135 (n=24026)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=54551)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=19017)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=59560)

- **FILTRO** `ibs_7min` < `0.2135` → IC=-0.235 (n=19642)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2135
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=58935)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.153 (n=26465)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=52112)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.245 (n=24400)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=73859)

- **FILTRO** `ibs_7min` > `0.28` → IC=-0.183 (n=24472)

  - _Acción_: SKIP cuando `ibs_7min` > 0.28
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=73787)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=3368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10715)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.320 (n=3490)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=10593)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.255 (n=4644)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=9439)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4122)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=12880)

- **FILTRO** `ibs_7min` > `0.7692` → IC=-0.210 (n=4250)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7692
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=12752)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=3161)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=9853)

- **FILTRO** `ibs_7min` < `0.713` → IC=-0.209 (n=3252)

  - _Acción_: SKIP cuando `ibs_7min` < 0.713
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9762)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.201 (n=3245)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9769)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=3028)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10264)

- **FILTRO** `ibs_7min` > `0.2649` → IC=-0.192 (n=3321)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2649
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=9971)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.178 (n=3306)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9986)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=3232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10295)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.325 (n=3216)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=10311)

- **FILTRO** `ibs_7min` < `0.29` → IC=-0.251 (n=4463)

  - _Acción_: SKIP cuando `ibs_7min` < 0.29
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9064)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.170 (n=3352)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10175)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=4319)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=13677)

- **FILTRO** `ibs_7min` > `0.7248` → IC=-0.184 (n=4497)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7248
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=13499)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3162)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9512)

- **FILTRO** `ibs_7min` < `0.7132` → IC=-0.201 (n=3168)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7132
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9506)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.192 (n=3166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9508)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=3053)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=10126)

- **FILTRO** `ibs_7min` > `0.272` → IC=-0.179 (n=3294)

  - _Acción_: SKIP cuando `ibs_7min` > 0.272
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=9885)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.169 (n=3278)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=9901)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.301 (n=3032)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=9516)

- **FILTRO** `ibs_7min` < `0.3` → IC=-0.234 (n=4110)

  - _Acción_: SKIP cuando `ibs_7min` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=8438)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=3074)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9474)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.200 (n=4520)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=14509)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=4103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=8628)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.311 (n=3096)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=9635)

- **FILTRO** `ibs_7min` < `0.7273` → IC=-0.225 (n=4194)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7273
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8537)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.191 (n=3176)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=9555)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.229 (n=4367)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=13394)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1017)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1306)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.161 (n=172)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=636)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=918)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=336)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=453)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=589)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.150 (n=195)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=586)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4304` → IC=+0.145 (n=728)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4304 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `729.2318` → IC=+0.155 (n=700)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 729.2318 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3574.1299` → IC=+0.140 (n=722)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3574.1299 (IC base=+0.126)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.184 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 14.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `498.39` → IC=+0.156 (n=373)

  - _Acción_: Kelly boost +0.78€ cuando `total_vol_5m` < 498.39 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2527.6661` → IC=+0.232 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2527.6661 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.156 (n=254)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 9.0 (IC base=+0.139)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.4372` → IC=+0.164 (n=111)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.82€ cuando `delta_ratio` |x|> 0.4372 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.134 (n=293)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 14.0 (IC base=+0.117)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4168` → IC=+0.170 (n=198)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.85€ cuando `delta_ratio` |x|> 0.4168 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `671.396` → IC=+0.163 (n=262)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 671.396 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.189 (n=104)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 59.0 (IC base=+0.131)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.418` → IC=+0.196 (n=179)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio` |x|> 0.418 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.176 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 5.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `5947.939` → IC=+0.168 (n=236)

  - _Acción_: Kelly boost +0.84€ cuando `total_vol_5m` < 5947.939 (IC base=+0.138)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.133 (n=295)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 14.0 (IC base=+0.101)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.133 (n=205)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.101)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **FILTRO** `pct_vs_K` |x|> `3.395` → IC=-0.160 (n=310)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.395
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=616)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.153 (n=306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0046 (IC base=-0.037)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.2538` → IC=-0.232 (n=69)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.2538
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=211)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.292 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.004)

- **PATRÓN** `pct_vs_K` |x|≤ `1.7678` → IC=+0.205 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `pct_vs_K` |x|≤ 1.7678 (IC base=-0.004)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` < `0.0107` → IC=-0.136 (n=64)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0107
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=25)

- **FILTRO** `T_h` < `243.9505` → IC=-0.182 (n=64)

  - _Acción_: SKIP cuando `T_h` < 243.9505
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=25)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `96.5959` → IC=-0.163 (n=87)

  - _Acción_: SKIP cuando `T_h` < 96.5959
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=88)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `87.9866` → IC=-0.253 (n=411)

  - _Acción_: SKIP cuando `T_h` < 87.9866
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=414)

- **FILTRO** `T_h` > `142.6109` → IC=-0.195 (n=185)

  - _Acción_: SKIP cuando `T_h` > 142.6109
  - _Potencial_: sin este filtro IC_bueno=-0.127 (n=558)

- **FILTRO** `pct_vs_K` |x|> `3.0008` → IC=-0.403 (n=183)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0008
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=560)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `48.8172` → IC=-0.221 (n=202)

  - _Acción_: SKIP cuando `T_h` > 48.8172
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=68)

- **FILTRO** `T_h` > `143.1506` → IC=-0.214 (n=68)

  - _Acción_: SKIP cuando `T_h` > 143.1506
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=206)

- **FILTRO** `pct_vs_K` |x|> `2.4125` → IC=-0.340 (n=92)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.4125
  - _Potencial_: sin este filtro IC_bueno=-0.049 (n=182)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `T_h` < `139.5329` → IC=-0.340 (n=23)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.260 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `T_h` > `144.6658` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `T_h` > 144.6658
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=19)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0093` → IC=-0.325 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0093
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=118)

- **FILTRO** `T_h` < `87.9956` → IC=-0.298 (n=117)

  - _Acción_: SKIP cuando `T_h` < 87.9956
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=119)

- **FILTRO** `sigma_h` < `0.0056` → IC=-0.207 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=169)

- **FILTRO** `pct_vs_K` |x|> `2.0379` → IC=-0.384 (n=110)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0379
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=115)

- **PATRÓN** `pct_vs_K` |x|≤ `2.0379` → IC=+0.124 (n=115)

  - _Acción_: Kelly boost +0.62€ cuando `pct_vs_K` |x|≤ 2.0379 (IC base=-0.126)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` < `0.0095` → IC=-0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `T_h` < `132.3532` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `T_h` < 132.3532
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `T_h` > `109.7804` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `T_h` > 109.7804
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.013` → IC=-0.216 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=154)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.250 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=175)

- **FILTRO** `T_h` > `69.913` → IC=-0.222 (n=156)

  - _Acción_: SKIP cuando `T_h` > 69.913
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=77)

- **FILTRO** `sigma_h` > `0.0152` → IC=-0.314 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0152
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=124)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.291 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=124)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1171` → IC=+0.446 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1171 (IC base=+0.337)

- **PATRÓN** `sigma_h` > `0.013` → IC=+0.360 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.013 (IC base=+0.337)

- **PATRÓN** `T_h` < `0.3491` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3491 (IC base=+0.337)

- **PATRÓN** `T_h` > `0.8789` → IC=+0.379 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8789 (IC base=+0.337)

- **PATRÓN** `dist_50` > `0.4666` → IC=+0.482 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4666 (IC base=+0.337)

- **PATRÓN** `edge` > `0.1005` → IC=+0.426 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1005 (IC base=+0.391)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.412 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.391)

- **PATRÓN** `dist_50` > `0.3717` → IC=+0.440 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3717 (IC base=+0.391)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.391)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1161` → IC=+0.279 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1161 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.261 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.188)

- **PATRÓN** `T_h` > `1.4764` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4764 (IC base=+0.188)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.234 (n=62)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.188)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.466 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.410)

- **PATRÓN** `sigma_h` < `0.0102` → IC=+0.423 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0102 (IC base=+0.410)

- **PATRÓN** `T_h` < `1.2028` → IC=+0.439 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.2028 (IC base=+0.410)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.483 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.410)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1635` → IC=+0.486 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1635 (IC base=+0.439)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.469 (n=63)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.439)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.459 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.439)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.473 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.439)

- **PATRÓN** `edge` > `0.1937` → IC=+0.472 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1937 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.475 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.464)

- **PATRÓN** `T_h` < `0.8072` → IC=+0.458 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.8072 (IC base=+0.464)

- **PATRÓN** `T_h` > `1.486` → IC=+0.481 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.486 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4578` → IC=+0.493 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4578 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `2.0` → IC=+0.485 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 2.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=459)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=500)

- **PATRÓN** `streak_estiramiento` < `0.829` → IC=+0.122 (n=345)

  - _Acción_: Kelly boost +0.61€ cuando `streak_estiramiento` < 0.829 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.146 (n=128)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 14.0 (IC base=+0.054)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=24)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.495 (IC base=+0.037)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `regimen_ma_toques` < `2.0` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `regimen_ma_toques` < 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=200)

- **PATRÓN** `streak_estiramiento` < `0.2031` → IC=+0.155 (n=56)

  - _Acción_: Kelly boost +0.78€ cuando `streak_estiramiento` < 0.2031 (IC base=+0.028)

- **PATRÓN** `streak_estiramiento` < `0.5831` → IC=+0.159 (n=171)

  - _Acción_: Kelly boost +0.79€ cuando `streak_estiramiento` < 0.5831 (IC base=+0.081)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.201 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.081)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=93)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.136 (n=31)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=39)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

### STREAK_FADE_60M
- **FILTRO** `py_entrada` < `0.515` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=25)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1089)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=1307)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5187)

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
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=2997)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.184 (n=1945)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0056 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.227` → IC=+0.156 (n=5837)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.227 (IC base=+0.135)

- **PATRÓN** `drift_15min` |x|≤ `1.0812` → IC=+0.135 (n=5835)

  - _Acción_: Kelly boost +0.68€ cuando `drift_15min` |x|≤ 1.0812 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1329` → IC=+0.149 (n=2410)

  - _Acción_: Kelly boost +0.74€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1329 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.146 (n=5402)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.5676` → IC=+0.215 (n=5212)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5676 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.139` → IC=+0.124 (n=2730)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.139 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.5442` → IC=+0.122 (n=5597)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.5442 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.27` → IC=+0.237 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.27 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3236)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4435.293` → IC=+0.171 (n=1945)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4435.293 (IC base=+0.135)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=2306)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.218 (n=832)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0572` → IC=+0.250 (n=278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0572 (IC base=+0.202)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2673` → IC=+0.228 (n=277)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2673 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2259` → IC=+0.211 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2259 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.231 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.272 (n=832)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.3824` → IC=+0.223 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3824 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.5302` → IC=+0.205 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5302 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.336` → IC=+0.297 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.336 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `14103.4716` → IC=+0.226 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14103.4716 (IC base=+0.202)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.144 (n=1049)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0072 (IC base=+0.131)

- **PATRÓN** `drift_60min` |x|≤ `0.1091` → IC=+0.147 (n=700)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1091 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.138 (n=961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 6.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.131 (n=1051)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 16.0 (IC base=+0.131)

- **PATRÓN** `ibs_15` > `0.4895` → IC=+0.216 (n=1049)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4895 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.1205` → IC=+0.149 (n=656)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1205 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.997` → IC=+0.285 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.997 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `6053.4281` → IC=+0.170 (n=476)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6053.4281 (IC base=+0.131)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.7619` → IC=+0.134 (n=785)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.67€ cuando `ibs_15` > 0.7619 (IC base=+0.051)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0144` → IC=+0.146 (n=654)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0144 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.150 (n=1485)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0124 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2327` → IC=+0.174 (n=1487)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2327 (IC base=+0.143)

- **PATRÓN** `delta_ratio_macro` |x|> `0.058` → IC=+0.144 (n=1486)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio_macro` |x|> 0.058 (IC base=+0.143)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.093` → IC=+0.198 (n=462)

  - _Acción_: Kelly boost +0.99€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.093 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.151 (n=1367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.143)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.213 (n=1327)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.204` → IC=+0.158 (n=674)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.204 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.616` → IC=+0.183 (n=339)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 17.616 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2931.7854` → IC=+0.188 (n=674)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2931.7854 (IC base=+0.143)

- **PATRÓN** `ibs_15` < `0.1143` → IC=+0.148 (n=1140)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` < 0.1143 (IC base=+0.069)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1105` → IC=+0.365 (n=511)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1105 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.379 (n=510)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1351` → IC=+0.380 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1351 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.374 (n=809)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7906` → IC=+0.395 (n=766)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7906 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.382 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.963` → IC=+0.397 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.963 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=933)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3887.2465` → IC=+0.376 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3887.2465 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` > `0.0051` → IC=+0.404 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0051 (IC base=+0.362)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.365 (n=124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.362)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2196` → IC=+0.376 (n=167)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2196 (IC base=+0.362)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1441` → IC=+0.399 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1441 (IC base=+0.362)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.381 (n=342)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.362)

- **PATRÓN** `ibs_15` > `0.8112` → IC=+0.384 (n=369)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8112 (IC base=+0.362)

- **PATRÓN** `dist_vwap_pct` > `0.2485` → IC=+0.388 (n=168)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2485 (IC base=+0.362)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.163` → IC=+0.392 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.163 (IC base=+0.362)

- **PATRÓN** `libro_liquidez` > `8157.6321` → IC=+0.384 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8157.6321 (IC base=+0.362)

- **PATRÓN** `ballena_activa_n` < `487.0` → IC=+0.402 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 487.0 (IC base=+0.362)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.370 (n=397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.385 (n=180)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.366)

- **PATRÓN** `drift_60min` |x|≤ `0.1063` → IC=+0.373 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1063 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1291` → IC=+0.384 (n=265)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1291 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2969` → IC=+0.375 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2969 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.372 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.8152` → IC=+0.399 (n=355)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8152 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.159` → IC=+0.377 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.159 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` < `0.6387` → IC=+0.368 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6387 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.973` → IC=+0.395 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.973 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `4204.0039` → IC=+0.379 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4204.0039 (IC base=+0.366)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.205 (n=2828)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2829)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=2418)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3239)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.215 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.086)

- **PATRÓN** `ibs_15` > `0.6307` → IC=+0.276 (n=1266)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6307 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.201 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.086)

- **PATRÓN** `dist_vwap_pct` < `0.5648` → IC=+0.199 (n=1342)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.5648 (IC base=-0.086)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2304` → IC=+0.273 (n=1767)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2304 (IC base=-0.001)

- **PATRÓN** `ibs_15` < `0.371` → IC=+0.286 (n=5299)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.371 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` > `0.6721` → IC=+0.274 (n=765)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6721 (IC base=-0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` < `0.0039` → IC=-0.216 (n=917)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0039
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2758)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.188 (n=1707)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1968)

- **FILTRO** `sigma_ewma_delta_pct` > `22.099` → IC=-0.253 (n=521)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.099
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=3154)

- **FILTRO** `libro_liquidez` < `10195.3998` → IC=-0.194 (n=1212)

  - _Acción_: SKIP cuando `libro_liquidez` < 10195.3998
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=2463)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.145 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0031 (IC base=+0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.283 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.067)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.145` → IC=+0.270 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.145 (IC base=+0.067)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.316 (n=450)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1043` → IC=+0.277 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1043 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` < `0.5105` → IC=+0.282 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5105 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.895` → IC=+0.152 (n=228)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 21.895 (IC base=+0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0742` → IC=+0.227 (n=75)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0742 (IC base=-0.184)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0902` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0902 (IC base=-0.184)

- **PATRÓN** `ibs_15` < `0.6255` → IC=+0.292 (n=75)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.6255 (IC base=-0.184)

- **PATRÓN** `dist_vwap_pct` < `0.0453` → IC=+0.303 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0453 (IC base=-0.184)

- **PATRÓN** `ballena_activa_n` < `393.0` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 393.0 (IC base=-0.184)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=825)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.160 (n=556)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.006 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.164 (n=557)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3014` → IC=+0.195 (n=496)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3014 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.163 (n=452)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5684` → IC=+0.240 (n=632)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5684 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6301` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6301 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.4449` → IC=+0.147 (n=669)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.4449 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.262 (n=120)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=825)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7306.8584` → IC=+0.161 (n=287)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7306.8584 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.259 (n=922)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.4585` → IC=+0.244 (n=2095)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4585 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.8002` → IC=+0.256 (n=1844)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.8002 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2069` → IC=+0.268 (n=950)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2069 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.244 (n=1432)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3866` → IC=+0.273 (n=2095)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3866 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.3906` → IC=+0.267 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3906 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.394` → IC=+0.247 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.394 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1928` → IC=-0.283 (n=335)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1928
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=1007)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.275 (n=456)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=886)

- **FILTRO** `drift_15min` |x|> `0.9478` → IC=-0.301 (n=335)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9478
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1007)

- **FILTRO** `sigma_ewma_delta_pct` > `6.105` → IC=-0.206 (n=297)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.105
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=1045)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.205)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.205)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.205)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.205)

- **PATRÓN** `ibs_15` < `0.38` → IC=+0.299 (n=912)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.38 (IC base=-0.027)

- **PATRÓN** `dist_vwap_pct` < `0.4621` → IC=+0.252 (n=981)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4621 (IC base=-0.027)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1191` → IC=-0.264 (n=807)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1191
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=808)

- **FILTRO** `drift_15min` |x|> `1.2899` → IC=-0.278 (n=403)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2899
  - _Potencial_: sin este filtro IC_bueno=-0.202 (n=1212)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=1594)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.221)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.221)

- **PATRÓN** `delta_ratio_macro` |x|> `0.052` → IC=+0.282 (n=1265)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.052 (IC base=-0.011)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.296 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3284` → IC=+0.297 (n=1265)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3284 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.7641` → IC=+0.338 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7641 (IC base=-0.011)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.144 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0068 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.150 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.286 (n=26)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 116.0 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.049)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.144 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0068 (IC base=+0.097)

- **PATRÓN** `drift_60min` |x|≤ `0.1106` → IC=+0.150 (n=38)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1106 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.7315` → IC=+0.161 (n=57)

  - _Acción_: Kelly boost +0.81€ cuando `drift_15min` |x|≤ 0.7315 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.235` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.235 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.8358` → IC=+0.286 (n=26)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8358 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` < `0.0949` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0949 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.113` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 13.113 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 116.0 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1943` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1943 (IC base=+0.049)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.297 (n=471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.281)

- **PATRÓN** `drift_60min` |x|≤ `0.0527` → IC=+0.310 (n=471)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0527 (IC base=+0.281)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0688` → IC=+0.281 (n=1412)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0688 (IC base=+0.281)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2213` → IC=+0.289 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2213 (IC base=+0.281)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.293 (n=1469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.281)

- **PATRÓN** `ibs_15` > `0.8378` → IC=+0.308 (n=1413)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8378 (IC base=+0.281)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.310 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.281)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.835` → IC=+0.384 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.835 (IC base=+0.281)

- **PATRÓN** `libro_liquidez` > `13088.9696` → IC=+0.297 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13088.9696 (IC base=+0.281)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.303 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.275)

- **PATRÓN** `drift_60min` |x|≤ `0.076` → IC=+0.300 (n=328)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.076 (IC base=+0.275)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2694` → IC=+0.280 (n=248)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2694 (IC base=+0.275)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.282 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.275)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.300 (n=687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.275)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.299 (n=746)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.275)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.310 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.275)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.6` → IC=+0.392 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.6 (IC base=+0.275)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.276 (n=964)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.275)

- **PATRÓN** `libro_liquidez` > `15670.1365` → IC=+0.313 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15670.1365 (IC base=+0.275)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.294 (n=668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0501` → IC=+0.318 (n=223)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0501 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.065` → IC=+0.290 (n=668)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.065 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1008` → IC=+0.309 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1008 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.297 (n=642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.287 (n=473)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.846` → IC=+0.316 (n=668)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.846 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2798` → IC=+0.312 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2798 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.12` → IC=+0.377 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.12 (IC base=+0.287)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.126` → IC=-0.156 (n=94)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.126
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=289)

- **FILTRO** `ballena_activa_n` > `46.0` → IC=-0.137 (n=235)

  - _Acción_: SKIP cuando `ballena_activa_n` > 46.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=116)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.212 (n=123)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=374)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.182 (n=124)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=373)

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

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2148` → IC=-0.219 (n=30)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2148
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=30)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1177` → IC=-0.167 (n=16)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1177
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=50)

- **FILTRO** `sigma_h` < `0.0055` → IC=-0.328 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0055
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `sigma_h` < `0.0074` → IC=-0.167 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0074
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=29)

- **FILTRO** `drift_60min` |x|> `0.2763` → IC=-0.214 (n=19)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2763
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=38)

- **FILTRO** `ballena_activa_n` > `42.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `ballena_activa_n` > 42.0
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=36)

- **FILTRO** `sigma_h` < `0.0057` → IC=-0.210 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0057
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=30)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0863` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0863
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

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
- **PATRÓN** `ratio` < `0.9695` → IC=+0.331 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9695 (IC base=+0.139)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.356 (n=3076)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0187` → IC=+0.389 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0187 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9922` → IC=+0.195 (n=267)

  - _Acción_: Kelly boost +0.98€ cuando `ratio` < 0.9922 (IC base=+0.088)

- **PATRÓN** `T_h` > `109.882` → IC=+0.322 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.882 (IC base=+0.304)

- **PATRÓN** `ratio` > `1.0158` → IC=+0.378 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0158 (IC base=+0.304)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9831` → IC=+0.372 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9831 (IC base=+0.194)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.354 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.322)

- **PATRÓN** `ratio` > `1.0263` → IC=+0.406 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0263 (IC base=+0.322)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0398` → IC=+0.416 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0398 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5676 sube el IC de +0.135 a +0.215 en UPDOWN_GBM#15min (n=5212). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.202 a +0.272 en UPDOWN_GBM#BTC#15min (n=832). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4895 sube el IC de +0.131 a +0.216 en UPDOWN_GBM#ETH#15min (n=1049). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.143 a +0.213 en UPDOWN_GBM#XRP#15min (n=1327). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6307 sube el IC de -0.086 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1266). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.371 sube el IC de -0.001 a +0.286 en UPDOWN_GBM_15M_TARDIO (n=5299). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.067 a +0.316 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=450). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.184 a +0.292 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=75). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5684 sube el IC de +0.146 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=632). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3866 sube el IC de +0.243 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2095). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.205 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.38 sube el IC de -0.027 a +0.299 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=912). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.221 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3284 sube el IC de -0.011 a +0.297 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1265). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.097 a +0.286 en UPDOWN_GBM_ETH_15M_HORA7 (n=26). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.097 a +0.286 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=26). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8378 sube el IC de +0.281 a +0.308 en UPDOWN_GBM_IBS_ALTO (n=1413). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.275 a +0.299 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=746). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.846 sube el IC de +0.287 a +0.316 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=668). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7906 sube el IC de +0.365 a +0.395 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=766). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8152 sube el IC de +0.366 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=355). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2249 | +0.082 | +222.58€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2249 | +0.082 | +222.58€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1839 | +0.083 | +184.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1839 | +0.083 | +184.04€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 94 | +0.125 | +28.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 94 | +0.125 | +28.08€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1255 | -0.017 | +71.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1255 | -0.017 | +71.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 964 | -0.033 | +51.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 964 | -0.033 | +51.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 199 | +0.057 | +23.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 199 | +0.057 | +23.21€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 49320 | -0.085 | -6296.14€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3125 | +0.084 | -303.12€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 46195 | -0.097 | -5993.03€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4904 | -0.111 | -829.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4904 | -0.111 | -829.13€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3125 | +0.084 | -303.12€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3125 | +0.084 | -303.12€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 5017 | -0.107 | -951.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 5017 | -0.107 | -951.04€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13535 | -0.043 | -1308.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13535 | -0.043 | -1308.88€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13452 | -0.113 | -1378.57€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13452 | -0.113 | -1378.57€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9287 | -0.138 | -1525.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9287 | -0.138 | -1525.41€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 52395 | -0.012 | +2730.33€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 13511 | +0.004 | +1474.78€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 38884 | -0.017 | +1255.55€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 52395 | -0.012 | +2730.33€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 13511 | +0.004 | +1474.78€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 38884 | -0.017 | +1255.55€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 198237 | +0.112 | -8356.20€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22426 | +0.179 | -727.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 917 | +0.015 | -73.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 163621 | +0.105 | -7133.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11273 | +0.094 | -421.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 27113 | +0.102 | -1959.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 81 | -0.175 | +14.04€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 27017 | +0.103 | -1961.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 37357 | +0.123 | -643.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5634 | +0.177 | -239.07€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 27084 | +0.119 | -209.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4597 | +0.080 | -173.63€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 27161 | +0.098 | -1979.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 91 | -0.113 | +13.93€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 27055 | +0.099 | -1982.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 42382 | +0.123 | -913.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10611 | +0.178 | -277.72€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 27518 | +0.105 | -561.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4241 | +0.103 | -65.96€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 37082 | +0.111 | -1681.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5915 | +0.198 | -252.73€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 820 | +0.040 | -19.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 27912 | +0.095 | -1228.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2435 | +0.104 | -182.00€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 27142 | +0.107 | -1178.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 94 | -0.125 | +13.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 27035 | +0.107 | -1192.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 32203 | +0.191 | -2319.00€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 32203 | +0.191 | -2319.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7296 | +0.165 | -806.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7296 | +0.165 | -806.30€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4738 | +0.197 | -180.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4738 | +0.197 | -180.77€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7139 | +0.173 | -647.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7139 | +0.173 | -647.34€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5948 | +0.251 | -210.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5948 | +0.251 | -210.46€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 7003 | +0.184 | -487.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 7003 | +0.184 | -487.89€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1286 | +0.425 | -47.61€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1286 | +0.425 | -47.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 538 | +0.439 | -5.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 538 | +0.439 | -5.10€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 521 | +0.423 | -20.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 521 | +0.423 | -20.27€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 113853 | +0.199 | -8372.31€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 113853 | +0.199 | -8372.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 19713 | +0.177 | -2289.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 19713 | +0.177 | -2289.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 18359 | +0.223 | -621.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 18359 | +0.223 | -621.88€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 19543 | +0.180 | -2059.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 19543 | +0.180 | -2059.28€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 18508 | +0.217 | -742.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 18508 | +0.217 | -742.63€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 18796 | +0.204 | -1157.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 18796 | +0.204 | -1157.10€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 18934 | +0.197 | -1501.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 18934 | +0.197 | -1501.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 44126 | +0.116 | +304.31€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 44126 | +0.116 | +304.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 21967 | +0.116 | +187.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 21967 | +0.116 | +187.91€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 22159 | +0.115 | +116.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 22159 | +0.115 | +116.40€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2693 | +0.293 | -10.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2693 | +0.293 | -10.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1231 | +0.283 | -27.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1231 | +0.283 | -27.07€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1320 | +0.296 | +9.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1320 | +0.296 | +9.42€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1240 | +0.438 | -5.56€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1240 | +0.438 | -5.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 591 | +0.434 | -8.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 591 | +0.434 | -8.35€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 597 | +0.442 | +1.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 597 | +0.442 | +1.38€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1984 | +0.067 | -92.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1259 | +0.078 | -27.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1550 | +0.073 | -46.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1259 | +0.078 | -27.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 89725 | +0.100 | -2055.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7252 | +0.096 | +152.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 82473 | +0.101 | -2208.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 49005 | +0.105 | -472.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7252 | +0.096 | +152.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 41753 | +0.106 | -625.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 19183 | +0.109 | -87.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 19183 | +0.109 | -87.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 21537 | +0.082 | -1495.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 21537 | +0.082 | -1495.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 60949 | +0.101 | +34100.97€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 60949 | +0.101 | +34100.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10096 | +0.225 | +8694.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10096 | +0.225 | +8694.88€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 9435 | +0.177 | +7457.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9435 | +0.177 | +7457.78€ | 0 | 21 |
| ✅ GBM_LATE_15M#DOGE | 10918 | +0.207 | +8622.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10918 | +0.207 | +8622.07€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 8111 | +0.059 | +2687.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8111 | +0.059 | +2687.84€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 8484 | -0.027 | +2207.29€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8484 | -0.027 | +2207.29€ | 3 | 17 |
| ✅ GBM_LATE_15M#XRP | 13905 | -0.020 | +4431.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13905 | -0.020 | +4431.11€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 64576 | +0.086 | +37571.76€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 64576 | +0.086 | +37571.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 12511 | -0.002 | +6608.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 12511 | -0.002 | +6608.68€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 13876 | +0.006 | +3777.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 13876 | +0.006 | +3777.79€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8742 | +0.294 | +9982.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8742 | +0.294 | +9982.09€ | 0 | 22 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 12302 | +0.016 | +3876.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 12302 | +0.016 | +3876.59€ | 1 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9887 | +0.046 | +4459.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9887 | +0.046 | +4459.91€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7258 | +0.315 | +8866.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7258 | +0.315 | +8866.69€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 48058 | +0.179 | +39826.31€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 48058 | +0.179 | +39826.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7247 | +0.240 | +6747.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7247 | +0.240 | +6747.66€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7624 | +0.141 | +5673.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7624 | +0.141 | +5673.53€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7730 | +0.224 | +6711.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7730 | +0.224 | +6711.41€ | 0 | 19 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8242 | +0.130 | +6389.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8242 | +0.130 | +6389.71€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9079 | +0.121 | +6908.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9079 | +0.121 | +6908.25€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8136 | +0.234 | +7395.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8136 | +0.234 | +7395.76€ | 0 | 27 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 13182 | +0.126 | +6693.95€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 13182 | +0.126 | +6693.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 670 | +0.162 | +441.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 670 | +0.162 | +441.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3482 | +0.126 | +1882.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3482 | +0.126 | +1882.62€ | 0 | 13 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3825 | +0.127 | +1914.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3825 | +0.127 | +1914.34€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3468 | +0.100 | +1395.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3468 | +0.100 | +1395.79€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1230 | +0.167 | +768.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1230 | +0.167 | +768.64€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 61189 | +0.189 | +50621.50€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 61189 | +0.189 | +50621.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9655 | +0.249 | +9317.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9655 | +0.249 | +9317.19€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9781 | +0.141 | +6892.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9781 | +0.141 | +6892.05€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10381 | +0.234 | +9363.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10381 | +0.234 | +9363.77€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10134 | +0.144 | +7575.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10134 | +0.144 | +7575.98€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10826 | +0.126 | +7771.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10826 | +0.126 | +7771.35€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10412 | +0.241 | +9701.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10412 | +0.241 | +9701.16€ | 0 | 21 |
| ✅ GBM_LATE_5M | 15848 | +0.217 | +13233.17€ | 0 | 26 |
| ✅ GBM_LATE_5M#5min | 15848 | +0.217 | +13233.17€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1792 | +0.250 | +1722.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1792 | +0.250 | +1722.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3288 | +0.211 | +2826.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3288 | +0.211 | +2826.97€ | 0 | 28 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4520 | +0.207 | +3467.27€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4520 | +0.207 | +3467.27€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 2777 | +0.227 | +2466.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2777 | +0.227 | +2466.60€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5498 | +0.055 | +1489.83€ | 0 | 6 |
| ✅ GBM_LATE_60M#60min | 5498 | +0.055 | +1489.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1897 | +0.058 | +549.16€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1897 | +0.058 | +549.16€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1754 | +0.055 | +559.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1754 | +0.055 | +559.07€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1847 | +0.053 | +381.60€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1847 | +0.053 | +381.60€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 731 | -0.250 | -37.37€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 731 | -0.250 | -37.37€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 262 | -0.254 | -20.04€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 262 | -0.254 | -20.04€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 266 | -0.242 | -7.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 266 | -0.242 | -7.48€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 203 | -0.251 | -9.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 203 | -0.251 | -9.85€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2254 | +0.086 | +570.18€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2254 | +0.086 | +570.18€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 863 | +0.069 | +194.25€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 863 | +0.069 | +194.25€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 770 | +0.057 | +148.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 770 | +0.057 | +148.86€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 621 | +0.144 | +227.08€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 621 | +0.144 | +227.08€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 328 | +0.315 | +397.54€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 328 | +0.315 | +397.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 328 | +0.315 | +397.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 328 | +0.315 | +397.54€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4520 | +0.097 | +1027.09€ | 0 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4520 | +0.097 | +1027.09€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4520 | +0.097 | +1027.09€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4520 | +0.097 | +1027.09€ | 0 | 2 |
| ✅ LIQUIDACIONES_15M | 1446 | +0.011 | +62.53€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1446 | +0.011 | +62.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 147 | +0.070 | +23.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 147 | +0.070 | +23.56€ | 0 | 3 |
| ✅ LIQUIDACIONES_15M#BTC | 298 | -0.003 | +9.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 298 | -0.003 | +9.54€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 94 | +0.010 | +7.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 94 | +0.010 | +7.08€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 341 | +0.022 | +19.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 341 | +0.022 | +19.62€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 335 | -0.010 | +3.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 335 | -0.010 | +3.37€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 231 | +0.006 | -0.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 231 | +0.006 | -0.63€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4407 | +0.016 | +150.93€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4407 | +0.016 | +150.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 830 | +0.016 | +41.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 830 | +0.016 | +41.95€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 295 | +0.049 | +56.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 295 | +0.049 | +56.07€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1677 | +0.019 | +28.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1677 | +0.019 | +28.74€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 776 | +0.013 | +3.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 776 | +0.013 | +3.99€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 590 | +0.000 | +25.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 590 | +0.000 | +25.33€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2563 | -0.032 | -2.47€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2563 | -0.032 | -2.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 782 | -0.032 | -12.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 782 | -0.032 | -12.35€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 921 | -0.009 | +21.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 921 | -0.009 | +21.69€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 860 | -0.056 | -11.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 860 | -0.056 | -11.81€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 18172 | -0.032 | -191.63€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 8768 | -0.035 | -141.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 9404 | -0.030 | -49.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 644 | -0.056 | -38.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 330 | -0.036 | -4.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 314 | -0.076 | -34.04€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4783 | -0.027 | -31.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2270 | -0.024 | -0.18€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2513 | -0.030 | -30.81€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1722 | -0.032 | +1.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 878 | -0.043 | -24.20€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 844 | -0.020 | +26.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4124 | -0.031 | -47.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1979 | -0.030 | -16.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2145 | -0.032 | -30.53€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3490 | -0.023 | +49.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1696 | -0.031 | -8.38€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1794 | -0.015 | +57.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3409 | -0.047 | -125.81€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1615 | -0.055 | -87.81€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1794 | -0.040 | -38.00€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 72104 | -0.000 | +3954.30€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 72104 | -0.000 | +3954.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13095 | +0.027 | +1839.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13095 | +0.027 | +1839.40€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 10012 | -0.038 | -142.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 10012 | -0.038 | -142.45€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 13241 | +0.025 | +1496.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 13241 | +0.025 | +1496.11€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9996 | -0.053 | -262.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9996 | -0.053 | -262.60€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12301 | -0.004 | +349.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12301 | -0.004 | +349.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13459 | +0.019 | +674.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13459 | +0.019 | +674.78€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7282 | -0.053 | -112.83€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7282 | -0.053 | -112.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2030 | -0.061 | -23.12€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2030 | -0.061 | -23.12€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 813 | -0.118 | -34.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 813 | -0.118 | -34.55€ | 6 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2209 | -0.068 | -13.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2209 | -0.068 | -13.60€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 868 | -0.018 | -27.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 868 | -0.018 | -27.95€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3382 | +0.004 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3382 | +0.004 | +1.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 133 | -0.033 | -0.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 133 | -0.033 | -0.70€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 198 | +0.010 | -0.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 198 | +0.010 | -0.55€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1326 | +0.006 | +6.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1326 | +0.006 | +6.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1391 | +0.007 | -0.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 195 | -0.013 | -1.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 176836 | -0.077 | +2586.81€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 176836 | -0.077 | +2586.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 31085 | -0.076 | +1854.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 31085 | -0.076 | +1854.43€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 26306 | -0.101 | -1245.79€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 26306 | -0.101 | -1245.79€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 31523 | -0.067 | +1571.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 31523 | -0.067 | +1571.47€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 25853 | -0.099 | -848.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 25853 | -0.099 | -848.61€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 31577 | -0.058 | +313.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 31577 | -0.058 | +313.31€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 30492 | -0.068 | +942.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 30492 | -0.068 | +942.00€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9168 | -0.035 | -180.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9168 | -0.035 | -180.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2129 | -0.047 | -28.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2129 | -0.047 | -28.86€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2669 | -0.024 | -33.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2669 | -0.024 | -33.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1284 | -0.063 | -30.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1284 | -0.063 | -30.59€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1069 | -0.034 | -35.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1069 | -0.034 | -35.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2257 | +0.121 | +914.15€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2121 | +0.126 | +901.56€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 497 | +0.139 | +252.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 497 | +0.139 | +252.93€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 442 | +0.117 | +154.71€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 442 | +0.117 | +154.71€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 396 | +0.131 | +185.95€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 396 | +0.131 | +185.95€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 357 | +0.138 | +178.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 357 | +0.138 | +178.57€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 429 | +0.101 | +129.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 429 | +0.101 | +129.41€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2354 | -0.021 | -34.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2354 | -0.021 | -34.02€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 424 | +0.009 | +22.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 424 | +0.009 | +22.39€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 435 | -0.049 | -29.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 435 | -0.049 | -29.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 578 | -0.047 | -41.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 578 | -0.047 | -41.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 481 | +0.003 | +7.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 481 | +0.003 | +7.68€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 436 | -0.014 | +7.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 436 | -0.014 | +7.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1239 | -0.050 | +84.08€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 575 | -0.081 | -5.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 446 | -0.080 | +17.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 435 | -0.017 | +58.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 314 | +0.003 | +67.13€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 229 | -0.033 | +31.58€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 193 | -0.023 | +29.75€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 953 | -0.041 | +114.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 286 | -0.076 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1568 | -0.192 | -51.16€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 615 | -0.182 | -20.13€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 544 | -0.179 | -16.22€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 71 | -0.199 | -3.91€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 524 | -0.202 | -34.86€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 461 | -0.211 | -41.49€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 63 | -0.131 | +6.63€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 429 | -0.191 | +3.83€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 398 | -0.188 | +2.19€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 31 | -0.227 | +1.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1403 | -0.193 | -55.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 165 | -0.183 | +4.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 571 | +0.376 | +521.70€ | 0 | 9 |
| ✅ RESOLUTION_SNIPER#BTC | 125 | +0.161 | +96.83€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 125 | +0.161 | +96.83€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#ETH | 130 | +0.371 | +107.64€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 130 | +0.371 | +107.64€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 316 | +0.459 | +317.22€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 316 | +0.459 | +317.22€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#sniper | 571 | +0.376 | +521.70€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 997 | +0.035 | +73.59€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 997 | +0.035 | +73.59€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 76 | +0.013 | +0.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 76 | +0.013 | +0.02€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 84 | +0.023 | +7.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 84 | +0.023 | +7.13€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 478 | +0.056 | +64.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 478 | +0.056 | +64.10€ | 1 | 3 |
| ✅ STREAK_FADE_5M | 3613 | -0.023 | -142.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3613 | -0.023 | -142.17€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1127 | -0.023 | -40.20€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 621 | -0.026 | -25.98€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 621 | -0.026 | -25.98€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 174 | -0.045 | -15.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 174 | -0.045 | -15.30€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1691 | -0.019 | -60.68€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1691 | -0.019 | -60.68€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 125 | -0.035 | -12.61€ | 3 | 0 |
| ✅ STREAK_FADE_60M#60min | 125 | -0.035 | -12.61€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 46 | -0.062 | -3.71€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 46 | -0.062 | -3.71€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 79 | -0.018 | -8.89€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 79 | -0.018 | -8.89€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 11587 | +0.014 | +70.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11587 | +0.014 | +70.37€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3063 | +0.015 | +30.24€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3063 | +0.015 | +30.24€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2936 | +0.008 | -3.55€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2936 | +0.008 | -3.55€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2593 | +0.014 | +19.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2593 | +0.014 | +19.31€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12681 | +0.018 | -2.37€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12681 | +0.018 | -2.37€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5206 | +0.020 | +2.02€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5206 | +0.020 | +2.02€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4444 | +0.018 | -0.74€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4444 | +0.018 | -0.74€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3031 | +0.014 | -3.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3031 | +0.014 | -3.65€ | 1 | 0 |
| ✅ UPDOWN_GBM | 115587 | +0.060 | +10884.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 28166 | +0.078 | +5524.57€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 3338 | -0.000 | +39.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 76794 | +0.062 | +5206.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6897 | -0.002 | +124.24€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 10030 | +0.101 | +1764.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1782 | +0.163 | +818.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8158 | +0.089 | +947.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 26183 | +0.057 | +2307.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3799 | +0.079 | +845.20€ | 0 | 11 |
| ✅ UPDOWN_GBM#BTC#240min | 966 | -0.001 | +19.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 18209 | +0.067 | +1361.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3067 | -0.005 | +79.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 142 | -0.069 | +2.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 12684 | +0.074 | +1356.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1763 | +0.154 | +737.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 10835 | +0.062 | +619.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 27195 | +0.050 | +1919.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6648 | +0.072 | +1021.25€ | 0 | 8 |
| ✅ UPDOWN_GBM#ETH#240min | 934 | +0.005 | +15.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16930 | +0.052 | +842.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2552 | +0.000 | +40.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 131 | -0.109 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 24279 | +0.041 | +1396.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7660 | +0.033 | +469.92€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 865 | -0.010 | +9.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14359 | +0.053 | +923.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1278 | +0.001 | +4.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 117 | -0.147 | -10.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 15214 | +0.073 | +2141.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6514 | +0.091 | +1631.66€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8303 | +0.062 | +511.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 390 | -0.107 | -8.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1021 | +0.365 | +382.19€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1021 | +0.365 | +382.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 492 | +0.362 | +172.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 492 | +0.362 | +172.46€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 529 | +0.366 | +209.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 529 | +0.366 | +209.74€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 27093 | -0.019 | +6718.64€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 27093 | -0.019 | +6718.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5053 | -0.116 | +270.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5053 | -0.116 | +270.17€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1072 | +0.223 | +901.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1072 | +0.223 | +901.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3635 | +0.220 | +2329.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3635 | +0.220 | +2329.72€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7734 | -0.058 | +1137.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7734 | -0.058 | +1137.89€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7618 | -0.056 | +1517.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7618 | -0.056 | +1517.85€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 339 | +0.060 | +34.14€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 339 | +0.060 | +34.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 339 | +0.060 | +34.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 339 | +0.060 | +34.14€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1883 | +0.281 | +1582.43€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1883 | +0.281 | +1582.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 993 | +0.275 | +786.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 993 | +0.275 | +786.85€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 890 | +0.287 | +795.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 890 | +0.287 | +795.59€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 880 | -0.116 | -89.79€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 880 | -0.116 | -89.79€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 279 | -0.080 | -20.94€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 279 | -0.080 | -20.94€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 102 | -0.192 | -14.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 102 | -0.192 | -14.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 116 | -0.178 | -4.99€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 116 | -0.178 | -4.99€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 5040 | +0.296 | +2219.56€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1944 | +0.251 | +255.93€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1950 | +0.290 | +813.95€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1146 | +0.382 | +1149.68€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.022 n=1422 — no justifica filtro, seguir monitorizando
  - _Datos_: n=1422 IC=+0.022 PNL=+67.76€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 843 celda(s) pasan gate riguroso completo de 2991 evaluadas (n>=40) y 4108 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=7654 IC=+0.033 PNL=+467.07€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1950/15 IC=+0.290 PNL=+813.95€ | BTC: n=1944/15 IC=+0.251 PNL=+255.93€ | SOL: n=1146/15 IC=+0.382 PNL=+1149.68€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.136 n=1096/60 | contraria IC=+0.182 n=1152 | gap=-0.046 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=617, boost estimado=+0.009. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=2550/40 IC=+0.000 PNL=+40.43€ | BTC#60min: n=3065/40 IC=-0.005 PNL=+79.35€ | SOL#60min: n=1278/40 IC=+0.001 PNL=+4.45€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.044 n=778414 | tras_1loss IC=+0.101 n=589688 | tras_2loss IC=+0.072 n=235056/40 | gap=-0.028 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.157 > 0.08 con n=1151 PNL=+674.90€
  - _Datos_: n=1151 IC=+0.157 PNL=+674.90€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.132 > 0.08 con n=1382 PNL=+650.73€
  - _Datos_: n=1382 IC=+0.132 PNL=+650.73€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.120 > 0.08 con n=90 PNL=+34.62€
  - _Datos_: n=90 IC=+0.120 PNL=+34.62€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=4113 PNL=+2306.74€
  - _Datos_: n=4113 IC=+0.334 PNL=+2306.74€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=1179 IC=+0.062 PNL=+114.20€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1179 IC=+0.062 PNL=+114.20€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=109 IC=+0.176 PNL=+69.98€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=109 IC=+0.176 PNL=+69.98€

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
  - _Estado_: n=4535 IC=-0.004 PNL=-38.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4535 IC=-0.004 PNL=-38.77€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=2358 IC=+0.003 PNL=+163.00€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=2358 IC=+0.003 PNL=+163.00€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=1422 IC=+0.022 PNL=+67.76€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=1422 IC=+0.022 PNL=+67.76€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.135 > 0.1 con n=7775 PNL=+3727.96€
  - _Datos_: n=7775 IC=+0.135 PNL=+3727.96€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=3797 IC=+0.079 PNL=+846.22€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=3797 IC=+0.079 PNL=+846.22€

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
  - _Estado_: n=1526 IC=+0.043 PNL=+129.66€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=1526 IC=+0.043 PNL=+129.66€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=193 IC=-0.023 PNL=-5.24€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=193 IC=-0.023 PNL=-5.24€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.315 n=328) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=328 IC=+0.315 PNL=+397.54€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.119 > 0.02 con n=1316 PNL=+533.68€
  - _Datos_: n=1316 IC=+0.119 PNL=+533.68€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=275 IC=-0.128 PNL=+0.99€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=275 IC=-0.128 PNL=+0.99€

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
  - _Estado_: n=47414 IC=+0.070 PNL=+6302.11€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=47414 IC=+0.070 PNL=+6302.11€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=791 PNL=+114.05€
  - _Datos_: n=791 IC=-0.137 PNL=+114.05€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=4531 IC=+0.069 PNL=+578.60€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=4531 IC=+0.069 PNL=+578.60€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=198 IC=-0.085 PNL=+1.70€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=198 IC=-0.085 PNL=+1.70€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=1220 IC=+0.096 PNL=+298.32€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1220 IC=+0.096 PNL=+298.32€

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
  - _Estado_: n=46252 IC=-0.137 PNL=+2863.65€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=46252 IC=-0.137 PNL=+2863.65€

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
  - _Estado_: n=4904 IC=+0.133 PNL=+3305.31€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=4904 IC=+0.133 PNL=+3305.31€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=11981 IC=+0.057 PNL=+1014.99€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11981 IC=+0.057 PNL=+1014.99€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.102 > 0.08 con n=4982 PNL=+2817.72€
  - _Datos_: n=4982 IC=+0.102 PNL=+2817.72€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.222 < -0.1 con n=5030 PNL=-447.22€
  - _Datos_: n=5030 IC=-0.222 PNL=-447.22€

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
  - _Estado_: n=124 IC=+0.064 PNL=+22.76€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=124 IC=+0.064 PNL=+22.76€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.096 n=2294) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=2294 IC=+0.096 PNL=+460.01€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.415 n=691) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=691 IC=+0.415 PNL=+1013.51€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=19703 IC=+0.177 PNL=-2286.61€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=19703 IC=+0.177 PNL=-2286.61€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.234 > 0.1 con n=321 PNL=+226.17€
  - _Datos_: n=321 IC=+0.234 PNL=+226.17€
