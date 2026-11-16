# Hipótesis automáticas — 2026-11-16 11:17 UTC
_Generado por shadow_postmortem.py sobre 1362187 resoluciones (PNL=+189353.30€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.5` → IC=-0.317 (n=195)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=727)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.195 (n=1041)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.505 (IC base=+0.122)

- **PATRÓN** `n_total_lado` > `62.0` → IC=+0.183 (n=329)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 62.0 (IC base=+0.122)

- **PATRÓN** `banda_hit_calibrado` > `0.8128` → IC=+0.269 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8128 (IC base=+0.122)

- **PATRÓN** `banda_z` > `8.435` → IC=+0.195 (n=329)

  - _Acción_: Kelly boost +0.97€ cuando `banda_z` > 8.435 (IC base=+0.122)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.137 (n=364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 17.0 (IC base=+0.122)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.135 (n=1076)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.122)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.280 (n=171)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=516)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.193 (n=906)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.505 (IC base=+0.123)

- **PATRÓN** `n_total_lado` > `65.0` → IC=+0.179 (n=285)

  - _Acción_: Kelly boost +0.90€ cuando `n_total_lado` > 65.0 (IC base=+0.123)

- **PATRÓN** `banda_hit_calibrado` > `0.8125` → IC=+0.267 (n=388)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8125 (IC base=+0.123)

- **PATRÓN** `banda_z` > `8.7` → IC=+0.204 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 8.7 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.132 (n=773)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.125 (n=608)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=976)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `8821.377` → IC=+0.136 (n=234)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 8821.377 (IC base=+0.014)

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
- **FILTRO** `restante_s_al_confirmar` < `131.52` → IC=-0.218 (n=12279)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 131.52
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=36843)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `124.95` → IC=-0.256 (n=1224)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 124.95
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3672)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `115.28` → IC=-0.278 (n=1247)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.28
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=3744)

### BALLENAS_TARDIAS#ETH#5min
- **FILTRO** `restante_s_al_confirmar` < `115.91` → IC=-0.167 (n=3368)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 115.91
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=10107)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `151.8` → IC=-0.239 (n=3348)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 151.8
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=10050)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `128.32` → IC=-0.267 (n=2313)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.32
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=6939)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.208 (n=28894)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `8088.1574` → IC=+0.155 (n=2380)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 8088.1574 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.127 (n=25068)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=30579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.224 (n=22870)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=8508)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `6405.8588` → IC=+0.143 (n=3303)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 6405.8588 (IC base=+0.124)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.185 (n=1914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 7.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=2144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.178)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.328 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=2746)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `16068.6951` → IC=+0.185 (n=709)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 16068.6951 (IC base=+0.178)

### FAVORITO_CONFIRMADO#BTC#60min
- **FILTRO** `py_entrada` < `0.55` → IC=-0.335 (n=95)

  - _Acción_: SKIP cuando `py_entrada` < 0.55
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=2294)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.168 (n=633)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.074)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.149 (n=1486)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.44 (IC base=+0.087)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.170 (n=5244)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 6.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.171 (n=4665)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` > `0.77` → IC=+0.375 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.77 (IC base=+0.167)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.206 (n=2500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.332 (n=968)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.203 (n=2916)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.145 (n=671)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 15.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.143 (n=1206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.259 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=1146)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.156 (n=155)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.075)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.250 (n=970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.227)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.420 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.145 (n=1442)
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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.138 (n=501)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.127 (n=903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 11.0 (IC base=+0.123)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.254 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.123)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.755` → IC=-0.299 (n=152)

  - _Acción_: SKIP cuando `py_entrada` > 0.755
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=25156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=21239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 15.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.227 (n=7967)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.338 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `4915.142` → IC=+0.338 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4915.142 (IC base=+0.194)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=5737)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.74` → IC=+0.177 (n=5665)

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

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.213 (n=3461)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.212 (n=2307)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.248 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.72 (IC base=+0.208)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.182 (n=5601)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.176 (n=4749)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.174)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.175 (n=5741)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.73 (IC base=+0.174)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.183 (n=4404)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` > 0.71 (IC base=+0.174)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.257 (n=4445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.252 (n=3958)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.251)

- **PATRÓN** `py_entrada` > `0.8` → IC=+0.364 (n=1512)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=5484)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.191 (n=3482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.192 (n=4064)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.430 (n=995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.425)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.427 (n=987)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.425)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.437 (n=1001)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.425)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.425)

- **PATRÓN** `libro_liquidez` > `4649.4982` → IC=+0.441 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4649.4982 (IC base=+0.425)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.438 (n=404)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.439)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.442 (n=415)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.439)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.439)

- **PATRÓN** `libro_liquidez` > `12497.2329` → IC=+0.445 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12497.2329 (IC base=+0.439)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=32928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.239 (n=32900)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.200)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.187 (n=4926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 18.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=10566)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.205 (n=7009)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.177)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.226 (n=13761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.286 (n=4574)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.184 (n=13790)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 7.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.72` → IC=+0.198 (n=11675)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.72 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.855` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.855
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.229 (n=4609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=5296)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.254 (n=7571)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.218)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **FILTRO** `py_entrada` < `0.775` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=10)

- **FILTRO** `libro_liquidez` < `3197.0694` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 3197.0694
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.208 (n=12520)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.255 (n=4752)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.204)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=5481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=5470)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.241 (n=6834)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=11856)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.139 (n=12663)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.31` → IC=+0.140 (n=10983)

  - _Acción_: Kelly boost +0.70€ cuando `lag_apertura_s` < 2.31 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=5779)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.116)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.142 (n=5729)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.96 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.124 (n=7311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.116)

- **PATRÓN** `lag_apertura_s` < `2.53` → IC=+0.142 (n=5475)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 2.53 (IC base=+0.116)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=6077)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.115)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.136 (n=7681)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.95 (IC base=+0.115)

- **PATRÓN** `lag_apertura_s` < `3.06` → IC=+0.136 (n=7281)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.06 (IC base=+0.115)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.306 (n=1437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.389 (n=744)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `3993.0903` → IC=+0.294 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3993.0903 (IC base=+0.293)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.287 (n=968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.282)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.370 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.282)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.315 (n=702)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=1027)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.394 (n=356)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.441 (n=981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.444 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.439 (n=456)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.434)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.438 (n=322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.434)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.433 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.434)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.442 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.434)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.450 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.442)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.440 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.442)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.446 (n=439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.442)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.440 (n=384)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4918` → IC=+0.139 (n=18707)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4918 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=18921)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.126 (n=13052)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 12.0 (IC base=+0.123)

- **PATRÓN** `ibs_20min` > `0.9761` → IC=+0.245 (n=6236)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9761 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.8291` → IC=+0.285 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8291 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.489` → IC=+0.189 (n=9375)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.489 (IC base=+0.123)

- **PATRÓN** `volumen_regimen` > `0.6963` → IC=+0.268 (n=5061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6963 (IC base=+0.123)

- **PATRÓN** `volumen_pendiente_norm` > `0.3043` → IC=+0.250 (n=1935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3043 (IC base=+0.123)

- **PATRÓN** `volumen_spike_ratio` > `2.7479` → IC=+0.233 (n=4503)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7479 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.137 (n=9191)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `4731.3626` → IC=+0.150 (n=6235)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4731.3626 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.124 (n=11795)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0064 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.5641` → IC=+0.146 (n=23551)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5641 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.1691` → IC=+0.194 (n=9539)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.1691 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.8584` → IC=+0.195 (n=6476)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.8584 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.237 (n=2375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `1.4554` → IC=+0.209 (n=16475)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4554 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.230 (n=16397)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 99.0 (IC base=+0.086)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.242 (n=1804)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3742` → IC=+0.213 (n=3977)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3742 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=1929)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.210 (n=2672)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9844` → IC=+0.275 (n=1803)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9844 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.803` → IC=+0.292 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.803 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2345` → IC=+0.254 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2345 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.2998` → IC=+0.218 (n=1730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2998 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=4399)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.221 (n=3647)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.249 (n=2369)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.0923` → IC=+0.277 (n=1186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0923 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=1323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.252 (n=1641)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.4803` → IC=+0.260 (n=3127)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4803 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.983` → IC=+0.247 (n=3644)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.983 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` < `0.0716` → IC=+0.245 (n=3059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0716 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2911` → IC=+0.252 (n=478)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2911 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.4485` → IC=+0.243 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4485 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.8622` → IC=+0.246 (n=2265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8622 (IC base=+0.242)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.245 (n=2531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `1781.58` → IC=+0.246 (n=2368)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.58 (IC base=+0.242)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.244 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.242)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.236 (n=1132)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.112` → IC=+0.247 (n=1486)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.112 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=3536)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.224 (n=2409)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.8981` → IC=+0.257 (n=1125)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8981 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1917` → IC=+0.231 (n=1490)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1917 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.802` → IC=+0.261 (n=491)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.802 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6275` → IC=+0.229 (n=3375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6275 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2781` → IC=+0.267 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2781 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.4471` → IC=+0.247 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4471 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.152 (n=3658)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0067 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0797` → IC=+0.160 (n=1219)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.0797 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=2598)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.3601` → IC=+0.206 (n=2438)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3601 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1435` → IC=+0.150 (n=3583)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.1435 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.974` → IC=+0.141 (n=3343)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.974 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.6279` → IC=+0.151 (n=1220)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` < 0.6279 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.158 (n=1494)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4414` → IC=+0.142 (n=3529)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4414 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.7866` → IC=+0.136 (n=2352)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.7866 (IC base=+0.133)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=4752)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `171.0` → IC=+0.187 (n=1155)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 171.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.209 (n=1407)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.202 (n=4434)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.256 (n=1630)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.965` → IC=+0.283 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.965 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` < `0.0972` → IC=+0.195 (n=3783)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.0972 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.226 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.7296` → IC=+0.211 (n=1869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7296 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.198 (n=5114)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `1999.591` → IC=+0.204 (n=1406)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1999.591 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.225 (n=3458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0112 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.222 (n=2624)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0096 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1786` → IC=+0.235 (n=1728)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1786 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=1488)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.229 (n=1788)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` < `0.0476` → IC=+0.273 (n=1313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0476 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.785` → IC=+0.267 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.785 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.3469` → IC=+0.258 (n=572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3469 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `2.1586` → IC=+0.231 (n=2523)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1586 (IC base=+0.222)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.224 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1875.538` → IC=+0.225 (n=1781)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1875.538 (IC base=+0.222)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.227 (n=3753)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 23.0 (IC base=+0.222)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=220)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=5104)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.145 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0039 (IC base=+0.064)

- **PATRÓN** `ibs_20min` > `0.9422` → IC=+0.238 (n=689)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9422 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1473` → IC=+0.346 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1473 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` < `0.5749` → IC=+0.342 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5749 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.142` → IC=+0.210 (n=1515)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.142 (IC base=+0.064)

- **PATRÓN** `volumen_regimen` > `1.2486` → IC=+0.360 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2486 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` < `0.1682` → IC=+0.344 (n=672)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1682 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.3061` → IC=+0.345 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3061 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` < `1.5524` → IC=+0.355 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5524 (IC base=+0.064)

- **PATRÓN** `volumen_spike_ratio` > `2.2887` → IC=+0.343 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2887 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.345 (n=825)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 142.0 (IC base=+0.064)

- **PATRÓN** `ibs_20min` < `0.0884` → IC=+0.186 (n=1332)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.0884 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.3485` → IC=+0.161 (n=652)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.3485 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.1444` → IC=+0.157 (n=2452)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1444 (IC base=+0.056)

- **PATRÓN** `volumen_regimen` < `1.0017` → IC=+0.160 (n=2267)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0017 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.2795` → IC=+0.211 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2795 (IC base=+0.056)

- **PATRÓN** `volumen_spike_ratio` > `1.5054` → IC=+0.162 (n=2217)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.5054 (IC base=+0.056)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.186 (n=151)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=813)

- **FILTRO** `ibs_20min` < `0.2703` → IC=-0.175 (n=241)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2703
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=723)

- **FILTRO** `ibs_20min` > `0.2` → IC=-0.130 (n=4956)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2
  - _Potencial_: sin este filtro IC_bueno=+0.157 (n=2517)

- **FILTRO** `sigma_ewma_delta_pct` > `8.298` → IC=-0.232 (n=808)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.298
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=6665)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.180 (n=332)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.75 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` > `0.9803` → IC=+0.279 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9803 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.6326` → IC=+0.270 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6326 (IC base=+0.023)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.928` → IC=+0.146 (n=292)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 2.928 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `0.8516` → IC=+0.266 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8516 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6202` → IC=+0.287 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6202 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0791` → IC=+0.281 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0791 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.288 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `1.5342` → IC=+0.265 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5342 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.275 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.023)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.157 (n=2517)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.2 (IC base=-0.033)

- **PATRÓN** `dist_vwap_pct` < `0.3226` → IC=+0.286 (n=1203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3226 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` < `0.695` → IC=+0.296 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.695 (IC base=-0.033)

- **PATRÓN** `volumen_regimen` > `1.0412` → IC=+0.289 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0412 (IC base=-0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.0781` → IC=+0.313 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0781 (IC base=-0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.4394` → IC=+0.298 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4394 (IC base=-0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.4113` → IC=+0.292 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4113 (IC base=-0.033)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `ibs_20min` < `0.7922` → IC=-0.159 (n=3826)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7922
  - _Potencial_: sin este filtro IC_bueno=+0.138 (n=1972)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.175 (n=1213)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=4585)

- **FILTRO** `ibs_20min` > `0.7333` → IC=-0.190 (n=2005)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=6026)

- **PATRÓN** `ibs_20min` > `0.7922` → IC=+0.138 (n=1972)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7922 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` > `1.0492` → IC=+0.341 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0492 (IC base=-0.058)

- **PATRÓN** `volumen_regimen` > `0.7071` → IC=+0.317 (n=1038)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7071 (IC base=-0.058)

- **PATRÓN** `volumen_pendiente_norm` < `0.1085` → IC=+0.301 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1085 (IC base=-0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.302` → IC=+0.308 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.302 (IC base=-0.058)

- **PATRÓN** `volumen_spike_ratio` < `1.5855` → IC=+0.305 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5855 (IC base=-0.058)

- **PATRÓN** `volumen_spike_ratio` > `2.516` → IC=+0.311 (n=379)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.516 (IC base=-0.058)

- **PATRÓN** `dist_vwap_pct` > `1.0731` → IC=+0.281 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0731 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` < `0.6413` → IC=+0.276 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6413 (IC base=+0.006)

- **PATRÓN** `volumen_regimen` > `1.2033` → IC=+0.286 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2033 (IC base=+0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.293 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.4677` → IC=+0.266 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4677 (IC base=+0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.434` → IC=+0.273 (n=2233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.434 (IC base=+0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.192 (n=8150)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0109 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.8657` → IC=+0.284 (n=11085)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8657 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.9621` → IC=+0.297 (n=1707)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9621 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.472` → IC=+0.168 (n=10965)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 3.472 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `0.6925` → IC=+0.278 (n=8085)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6925 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.295 (n=2025)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.6429` → IC=+0.286 (n=4729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6429 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.309 (n=13827)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 89.0 (IC base=+0.087)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.161 (n=7914)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0104 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.5182` → IC=+0.173 (n=20870)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.5182 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.2704` → IC=+0.283 (n=8279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2704 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.6966` → IC=+0.280 (n=3508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6966 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` > `1.1874` → IC=+0.286 (n=2657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1874 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2942` → IC=+0.330 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2942 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `1.452` → IC=+0.304 (n=3939)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.452 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` > `2.2727` → IC=+0.304 (n=5356)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2727 (IC base=+0.086)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.312 (n=11784)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.086)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.8041` → IC=-0.139 (n=4341)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8041
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=2237)

- **FILTRO** `ibs_20min` > `0.7085` → IC=-0.238 (n=1464)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7085
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=4394)

- **FILTRO** `sigma_ewma_delta_pct` > `4.078` → IC=-0.238 (n=1248)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.078
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=4610)

- **PATRÓN** `ibs_20min` > `0.8041` → IC=+0.304 (n=2237)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8041 (IC base=+0.012)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.965` → IC=+0.185 (n=2190)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 2.965 (IC base=+0.012)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.326 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` < `1.4503` → IC=+0.285 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4503 (IC base=+0.012)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.306 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.012)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.319 (n=1458)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.012)

- **PATRÓN** `ibs_20min` < `0.1723` → IC=+0.174 (n=1465)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.1723 (IC base=-0.017)

- **PATRÓN** `volumen_pendiente_norm` < `0.1519` → IC=+0.392 (n=1225)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1519 (IC base=-0.017)

- **PATRÓN** `volumen_spike_ratio` < `1.4272` → IC=+0.414 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4272 (IC base=-0.017)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.383 (n=1205)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 21.0 (IC base=-0.017)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1727` → IC=+0.227 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1727 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` < `1.1969` → IC=+0.213 (n=2393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1969 (IC base=+0.011)

- **PATRÓN** `volumen_regimen` > `0.6953` → IC=+0.221 (n=2138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6953 (IC base=+0.011)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.241 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.011)

- **PATRÓN** `volumen_spike_ratio` < `1.4151` → IC=+0.233 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4151 (IC base=+0.011)

- **PATRÓN** `ballena_activa_n` < `256.0` → IC=+0.246 (n=1575)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 256.0 (IC base=+0.011)

- **PATRÓN** `dist_vwap_pct` < `0.1427` → IC=+0.262 (n=1797)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1427 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `1.0185` → IC=+0.265 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0185 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2697` → IC=+0.309 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2697 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5272` → IC=+0.261 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5272 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1501` → IC=+0.265 (n=760)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1501 (IC base=+0.001)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.279 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.320 (n=1540)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.285)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.295 (n=3395)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.285)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.285)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.584` → IC=+0.306 (n=2287)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.584 (IC base=+0.285)

- **PATRÓN** `volumen_pendiente_norm` < `0.1311` → IC=+0.295 (n=3150)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1311 (IC base=+0.285)

- **PATRÓN** `volumen_spike_ratio` > `1.6035` → IC=+0.290 (n=3297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6035 (IC base=+0.285)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.293 (n=4083)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.285)

- **PATRÓN** `libro_liquidez` > `2001.4024` → IC=+0.295 (n=1131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2001.4024 (IC base=+0.285)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.305 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.285)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.334 (n=2085)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.1824` → IC=+0.324 (n=1377)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1824 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.326 (n=1196)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.307)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.310 (n=1423)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.0254` → IC=+0.307 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0254 (IC base=+0.307)

- **PATRÓN** `ibs_20min` > `0.1496` → IC=+0.317 (n=2085)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1496 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.122` → IC=+0.316 (n=372)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.122 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.412` → IC=+0.307 (n=3235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.412 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` < `0.1982` → IC=+0.307 (n=3096)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1982 (IC base=+0.307)

- **PATRÓN** `volumen_pendiente_norm` > `0.3447` → IC=+0.318 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3447 (IC base=+0.307)

- **PATRÓN** `volumen_spike_ratio` > `2.751` → IC=+0.319 (n=1371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.751 (IC base=+0.307)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.307 (n=1545)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.307)

- **PATRÓN** `libro_liquidez` > `1877.2368` → IC=+0.311 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1877.2368 (IC base=+0.307)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.311 (n=2688)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=+0.307)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7157` → IC=-0.182 (n=1539)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7157
  - _Potencial_: sin este filtro IC_bueno=+0.072 (n=4624)

- **PATRÓN** `dist_vwap_pct` > `0.1518` → IC=+0.235 (n=1108)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1518 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.3648` → IC=+0.237 (n=2199)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3648 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` < `1.1628` → IC=+0.238 (n=2212)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1628 (IC base=+0.022)

- **PATRÓN** `volumen_regimen` > `0.595` → IC=+0.233 (n=2211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.595 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` < `0.163` → IC=+0.236 (n=2320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.163 (IC base=+0.022)

- **PATRÓN** `volumen_pendiente_norm` > `0.1032` → IC=+0.246 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1032 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` < `2.4198` → IC=+0.241 (n=2147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4198 (IC base=+0.022)

- **PATRÓN** `volumen_spike_ratio` > `1.4963` → IC=+0.236 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4963 (IC base=+0.022)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.253 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` > `0.7784` → IC=+0.257 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7784 (IC base=+0.009)

- **PATRÓN** `dist_vwap_pct` < `0.1622` → IC=+0.260 (n=1600)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1622 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` < `1.1864` → IC=+0.264 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1864 (IC base=+0.009)

- **PATRÓN** `volumen_regimen` > `0.6158` → IC=+0.257 (n=1601)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6158 (IC base=+0.009)

- **PATRÓN** `volumen_pendiente_norm` > `0.2829` → IC=+0.303 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2829 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` < `1.5176` → IC=+0.296 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5176 (IC base=+0.009)

- **PATRÓN** `volumen_spike_ratio` > `2.426` → IC=+0.277 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.426 (IC base=+0.009)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.284 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.009)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7436` → IC=-0.247 (n=2524)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7436
  - _Potencial_: sin este filtro IC_bueno=+0.312 (n=2524)

- **FILTRO** `ibs_20min` > `0.6129` → IC=-0.235 (n=1192)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6129
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=3593)

- **FILTRO** `sigma_ewma_delta_pct` > `8.266` → IC=-0.269 (n=547)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.266
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=4238)

- **PATRÓN** `ibs_20min` > `0.7436` → IC=+0.312 (n=2524)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7436 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `1.0733` → IC=+0.348 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0733 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.441` → IC=+0.156 (n=2046)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 2.441 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` < `0.8357` → IC=+0.346 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8357 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `0.6908` → IC=+0.335 (n=1646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6908 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.0986` → IC=+0.335 (n=1739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0986 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2747` → IC=+0.367 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2747 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `1.4267` → IC=+0.361 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4267 (IC base=+0.033)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.353 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.6129` → IC=+0.159 (n=3593)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` < 0.6129 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` < `0.3234` → IC=+0.271 (n=1899)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3234 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.723` → IC=+0.130 (n=3750)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 4.723 (IC base=+0.060)

- **PATRÓN** `volumen_regimen` < `0.6909` → IC=+0.281 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6909 (IC base=+0.060)

- **PATRÓN** `volumen_pendiente_norm` > `0.0703` → IC=+0.296 (n=738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0703 (IC base=+0.060)

- **PATRÓN** `volumen_spike_ratio` < `1.7983` → IC=+0.281 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7983 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.288 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.060)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.356 (n=2327)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.314)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.317 (n=2625)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.314)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.314 (n=1818)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.314)

- **PATRÓN** `ibs_20min` > `0.6552` → IC=+0.340 (n=2604)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6552 (IC base=+0.314)

- **PATRÓN** `dist_vwap_pct` > `0.5444` → IC=+0.338 (n=954)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5444 (IC base=+0.314)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.826` → IC=+0.335 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.826 (IC base=+0.314)

- **PATRÓN** `volumen_regimen` > `1.0501` → IC=+0.342 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0501 (IC base=+0.314)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.343 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.314)

- **PATRÓN** `volumen_spike_ratio` > `1.5298` → IC=+0.327 (n=2247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5298 (IC base=+0.314)

- **PATRÓN** `libro_liquidez` > `2993.2446` → IC=+0.326 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2993.2446 (IC base=+0.314)

- **PATRÓN** `ballena_activa_n` < `38.0` → IC=+0.338 (n=2328)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 38.0 (IC base=+0.314)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.333 (n=2807)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0093 (IC base=+0.316)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.320 (n=1417)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.316)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.317 (n=2816)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.316)

- **PATRÓN** `ibs_20min` < `0.3846` → IC=+0.333 (n=2807)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3846 (IC base=+0.316)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.621` → IC=+0.327 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.621 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` < `0.7184` → IC=+0.317 (n=1234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7184 (IC base=+0.316)

- **PATRÓN** `volumen_regimen` > `1.2057` → IC=+0.345 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2057 (IC base=+0.316)

- **PATRÓN** `volumen_pendiente_norm` > `0.2825` → IC=+0.371 (n=393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2825 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` < `1.4114` → IC=+0.322 (n=873)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4114 (IC base=+0.316)

- **PATRÓN** `volumen_spike_ratio` > `2.1403` → IC=+0.319 (n=1187)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1403 (IC base=+0.316)

- **PATRÓN** `libro_liquidez` > `2975.8314` → IC=+0.318 (n=935)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2975.8314 (IC base=+0.316)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.220 (n=6007)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.172)

- **PATRÓN** `drift_60min` |x|≤ `0.1239` → IC=+0.192 (n=7922)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.1239 (IC base=+0.172)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=18683)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 5.0 (IC base=+0.172)

- **PATRÓN** `ibs_20min` > `0.5373` → IC=+0.229 (n=17992)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5373 (IC base=+0.172)

- **PATRÓN** `dist_vwap_pct` > `0.1643` → IC=+0.204 (n=6781)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1643 (IC base=+0.172)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.759` → IC=+0.258 (n=3519)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.759 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` < `1.1754` → IC=+0.151 (n=12001)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.1754 (IC base=+0.172)

- **PATRÓN** `volumen_regimen` > `0.6222` → IC=+0.151 (n=12000)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 0.6222 (IC base=+0.172)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.205 (n=2606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.172)

- **PATRÓN** `volumen_spike_ratio` > `2.5992` → IC=+0.184 (n=5837)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.5992 (IC base=+0.172)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.191 (n=16922)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 86.0 (IC base=+0.172)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.192 (n=7876)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.006 (IC base=+0.187)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.188 (n=11930)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.008 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.0829` → IC=+0.222 (n=5962)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0829 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=6698)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.4` → IC=+0.249 (n=15761)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.501` → IC=+0.191 (n=2834)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 9.501 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.506` → IC=+0.194 (n=15918)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 2.506 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `1.1858` → IC=+0.167 (n=12697)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 1.1858 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.294` → IC=+0.222 (n=2684)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.294 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6309` → IC=+0.197 (n=5686)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6309 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.201 (n=16845)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.187)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.263 (n=985)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.0748` → IC=+0.260 (n=985)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0748 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=3073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=2005)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9429` → IC=+0.291 (n=1966)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9429 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.476` → IC=+0.326 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.476 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2316` → IC=+0.280 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2316 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.8356` → IC=+0.225 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8356 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.227 (n=2817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=3279)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.259 (n=2461)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.257)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.257 (n=1115)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.257)

- **PATRÓN** `drift_60min` |x|≤ `0.0984` → IC=+0.311 (n=1083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0984 (IC base=+0.257)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.259 (n=2537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.257)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.263 (n=2246)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.257)

- **PATRÓN** `ibs_20min` < `0.4419` → IC=+0.275 (n=2460)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4419 (IC base=+0.257)

- **PATRÓN** `sigma_ewma_delta_pct` < `1.953` → IC=+0.262 (n=2425)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 1.953 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` < `0.0731` → IC=+0.259 (n=2047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0731 (IC base=+0.257)

- **PATRÓN** `volumen_pendiente_norm` > `0.3012` → IC=+0.273 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3012 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` < `1.4471` → IC=+0.273 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4471 (IC base=+0.257)

- **PATRÓN** `volumen_spike_ratio` > `2.6917` → IC=+0.261 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6917 (IC base=+0.257)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.264 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.257)

- **PATRÓN** `libro_liquidez` > `1781.599` → IC=+0.262 (n=1640)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.599 (IC base=+0.257)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.258 (n=801)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 6.0 (IC base=+0.257)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.195 (n=918)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0032 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.0647` → IC=+0.176 (n=914)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0647 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.146 (n=2868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.2597` → IC=+0.204 (n=2742)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2597 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1867` → IC=+0.213 (n=1345)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1867 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.618` → IC=+0.207 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.618 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `0.6238` → IC=+0.133 (n=914)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.6238 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` > `1.0495` → IC=+0.133 (n=1243)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.0495 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` > `0.2773` → IC=+0.167 (n=421)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2773 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.7731` → IC=+0.131 (n=1798)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.7731 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` > `2.4602` → IC=+0.141 (n=899)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` > 2.4602 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `395.0` → IC=+0.133 (n=2669)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 395.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.179 (n=2597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0058 (IC base=+0.153)

- **PATRÓN** `drift_60min` |x|≤ `0.2462` → IC=+0.175 (n=2596)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.2462 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=1400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.153)

- **PATRÓN** `ibs_20min` < `0.6117` → IC=+0.211 (n=2950)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6117 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.899` → IC=+0.176 (n=551)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.899 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.023` → IC=+0.158 (n=2574)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 4.023 (IC base=+0.153)

- **PATRÓN** `volumen_regimen` < `1.2025` → IC=+0.163 (n=2950)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.2025 (IC base=+0.153)

- **PATRÓN** `volumen_pendiente_norm` < `0.2285` → IC=+0.155 (n=3137)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.2285 (IC base=+0.153)

- **PATRÓN** `volumen_spike_ratio` < `2.4718` → IC=+0.156 (n=2824)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.4718 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `207.0` → IC=+0.200 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 207.0 (IC base=+0.153)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.01` → IC=+0.223 (n=2032)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.2518` → IC=+0.232 (n=2029)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2518 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=3174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.288 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.04` → IC=+0.307 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.04 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.209 (n=2655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.3513` → IC=+0.239 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3513 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `2.7115` → IC=+0.224 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7115 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.214 (n=3685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1992.3784` → IC=+0.221 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1992.3784 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.248 (n=2402)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0109 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.2473` → IC=+0.270 (n=1818)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2473 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=1042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0409` → IC=+0.295 (n=1200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0409 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.906` → IC=+0.279 (n=360)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.906 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3545` → IC=+0.289 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3545 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.7689` → IC=+0.243 (n=1161)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7689 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1827` → IC=+0.252 (n=1758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1827 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `1967.0984` → IC=+0.249 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1967.0984 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.241 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.195 (n=995)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0038 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.0794` → IC=+0.180 (n=993)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.0794 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3075)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` > `0.2448` → IC=+0.188 (n=2973)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.2448 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.1429` → IC=+0.186 (n=1687)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.1429 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.186` → IC=+0.203 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.186 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.838` → IC=+0.137 (n=1983)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.838 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.176 (n=448)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.52` → IC=+0.127 (n=1282)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.52 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.137 (n=971)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `6877.2097` → IC=+0.198 (n=1348)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 6877.2097 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.126 (n=2924)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 125.0 (IC base=+0.126)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.164 (n=2799)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0068 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.4133` → IC=+0.150 (n=3180)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.4133 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.6713` → IC=+0.189 (n=3181)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` < 0.6713 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.164` → IC=+0.158 (n=3242)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.164 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.195` → IC=+0.141 (n=756)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 9.195 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `0.8509` → IC=+0.151 (n=2120)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8509 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.178 (n=476)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.189` → IC=+0.134 (n=2660)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.189 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.5144` → IC=+0.136 (n=2701)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.5144 (IC base=+0.133)

- **PATRÓN** `libro_liquidez` > `6416.0381` → IC=+0.191 (n=1442)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6416.0381 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.154 (n=1003)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 48.0 (IC base=+0.133)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.169 (n=1103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0127 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.134 (n=3398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.4719` → IC=+0.204 (n=3309)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4719 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.2029` → IC=+0.187 (n=1762)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.2029 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.01` → IC=+0.287 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.01 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.1636` → IC=+0.129 (n=3309)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1636 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` < `0.1626` → IC=+0.122 (n=3374)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1626 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.783` → IC=+0.124 (n=2142)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 1.783 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2682.0548` → IC=+0.196 (n=1500)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 2682.0548 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.129 (n=1107)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 16.0 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.143 (n=3471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.012 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.1161` → IC=+0.164 (n=1157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.1161 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=3542)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` < `0.4875` → IC=+0.240 (n=3054)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4875 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.231` → IC=+0.146 (n=3069)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` < 2.231 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.1777` → IC=+0.130 (n=3470)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1777 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` > `0.859` → IC=+0.127 (n=2313)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 0.859 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.1623` → IC=+0.127 (n=3420)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1623 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.149 (n=485)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.4343` → IC=+0.145 (n=1096)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.4343 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.4432` → IC=+0.136 (n=1096)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4432 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2584.7011` → IC=+0.191 (n=1573)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2584.7011 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.131 (n=3287)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 44.0 (IC base=+0.124)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.247 (n=2980)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.1667` → IC=+0.240 (n=1312)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1667 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=3095)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2689)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `0.6656` → IC=+0.257 (n=2978)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6656 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.1821` → IC=+0.231 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1821 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.8067` → IC=+0.227 (n=3077)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.8067 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.534` → IC=+0.257 (n=1368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.534 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.236 (n=2978)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2347` → IC=+0.264 (n=558)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2347 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` < `2.4665` → IC=+0.228 (n=2906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4665 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4333` → IC=+0.229 (n=2906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4333 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2597.937` → IC=+0.232 (n=1985)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2597.937 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.244 (n=1364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0123 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.017` → IC=+0.247 (n=2066)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.017 (IC base=+0.242)

- **PATRÓN** `drift_60min` |x|≤ `0.6053` → IC=+0.250 (n=3098)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6053 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1515)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.248 (n=1391)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.242)

- **PATRÓN** `ibs_20min` < `0.0364` → IC=+0.302 (n=1364)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0364 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `1.1554` → IC=+0.250 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1554 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.121` → IC=+0.271 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.121 (IC base=+0.242)

- **PATRÓN** `volumen_regimen` > `1.0462` → IC=+0.249 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0462 (IC base=+0.242)

- **PATRÓN** `volumen_pendiente_norm` > `0.2813` → IC=+0.296 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2813 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` < `1.8377` → IC=+0.239 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8377 (IC base=+0.242)

- **PATRÓN** `volumen_spike_ratio` > `1.5486` → IC=+0.243 (n=2616)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5486 (IC base=+0.242)

- **PATRÓN** `libro_liquidez` > `2960.0954` → IC=+0.243 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2960.0954 (IC base=+0.242)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.208 (n=1566)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.156)

- **PATRÓN** `drift_60min` |x|≤ `0.1386` → IC=+0.172 (n=2067)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.1386 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4893)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.156)

- **PATRÓN** `ibs_20min` > `0.4225` → IC=+0.201 (n=4196)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4225 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.2285` → IC=+0.175 (n=1757)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.2285 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.538` → IC=+0.209 (n=768)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.538 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` < `0.8615` → IC=+0.167 (n=2832)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8615 (IC base=+0.156)

- **PATRÓN** `volumen_regimen` > `1.1957` → IC=+0.163 (n=1415)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 1.1957 (IC base=+0.156)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.174 (n=1232)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` < `1.5279` → IC=+0.160 (n=2015)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 1.5279 (IC base=+0.156)

- **PATRÓN** `volumen_spike_ratio` > `1.8077` → IC=+0.159 (n=3053)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.8077 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=4004)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `7284.4682` → IC=+0.189 (n=2130)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 7284.4682 (IC base=+0.156)

- **PATRÓN** `ibs_20min` < `0.3836` → IC=+0.176 (n=3421)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.3836 (IC base=+0.099)

- **PATRÓN** `ballena_activa_n` < `23.0` → IC=+0.140 (n=2246)

  - _Acción_: Kelly boost +0.70€ cuando `ballena_activa_n` < 23.0 (IC base=+0.099)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.210 (n=773)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.3322` → IC=+0.202 (n=1157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3322 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.219 (n=1042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` > `0.6198` → IC=+0.244 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6198 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.3129` → IC=+0.222 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3129 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.949` → IC=+0.215 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.949 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.629` → IC=+0.211 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.629 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` < `0.2151` → IC=+0.190 (n=1303)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.2151 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.0911` → IC=+0.202 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0911 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` < `2.1675` → IC=+0.200 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1675 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `1.4033` → IC=+0.188 (n=1135)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 1.4033 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `13741.2485` → IC=+0.193 (n=771)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 13741.2485 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.158 (n=484)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0032 (IC base=+0.077)

- **PATRÓN** `ibs_20min` < `0.2095` → IC=+0.196 (n=637)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.2095 (IC base=+0.077)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.174 (n=623)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 166.0 (IC base=+0.077)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.232 (n=629)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.128` → IC=+0.159 (n=628)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.128 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=1481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `ibs_20min` > `0.7794` → IC=+0.268 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7794 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.5928` → IC=+0.192 (n=306)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.5928 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.907` → IC=+0.205 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.907 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` < `0.8342` → IC=+0.168 (n=952)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.8342 (IC base=+0.154)

- **PATRÓN** `volumen_regimen` > `1.1643` → IC=+0.157 (n=476)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` > 1.1643 (IC base=+0.154)

- **PATRÓN** `volumen_pendiente_norm` > `0.2192` → IC=+0.201 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2192 (IC base=+0.154)

- **PATRÓN** `volumen_spike_ratio` > `2.4732` → IC=+0.186 (n=469)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.4732 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `7908.6344` → IC=+0.181 (n=648)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 7908.6344 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.125 (n=947)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0054 (IC base=+0.098)

- **PATRÓN** `ibs_20min` < `0.0885` → IC=+0.206 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0885 (IC base=+0.098)

- **PATRÓN** `volumen_regimen` < `0.6765` → IC=+0.136 (n=625)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.6765 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `7705.2266` → IC=+0.152 (n=644)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 7705.2266 (IC base=+0.098)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.132 (n=612)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 42.0 (IC base=+0.098)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.146 (n=817)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0094 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.140 (n=1155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.5357` → IC=+0.187 (n=1094)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.5357 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.9868` → IC=+0.152 (n=208)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.9868 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.866` → IC=+0.221 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.866 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.0462` → IC=+0.130 (n=1078)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.0462 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.224` → IC=+0.145 (n=215)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.224 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4112` → IC=+0.150 (n=395)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4112 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2758.0268` → IC=+0.153 (n=555)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 2758.0268 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5517` → IC=+0.164 (n=1188)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.5517 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `2649.2301` → IC=+0.166 (n=612)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2649.2301 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `13.0` → IC=+0.129 (n=602)

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
- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.226 (n=7911)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0126 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.191 (n=24708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.9688` → IC=+0.303 (n=7903)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9688 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.9073` → IC=+0.216 (n=2770)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9073 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.933` → IC=+0.260 (n=5811)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.933 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `1.2138` → IC=+0.160 (n=15969)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2138 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.2408` → IC=+0.211 (n=4256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2408 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.622` → IC=+0.192 (n=7715)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.622 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.200 (n=22359)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 102.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.199 (n=7326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0053 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.208 (n=7320)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.1494` → IC=+0.202 (n=9659)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1494 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=8203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` < `0.4857` → IC=+0.253 (n=19324)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4857 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` < `0.1851` → IC=+0.181 (n=14014)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.1851 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.512` → IC=+0.204 (n=20388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.512 (IC base=+0.198)

- **PATRÓN** `volumen_regimen` < `1.0526` → IC=+0.173 (n=12963)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 1.0526 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.257 (n=3022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `2.622` → IC=+0.212 (n=7023)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.622 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `90.0` → IC=+0.214 (n=20828)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 90.0 (IC base=+0.198)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` > `0.0109` → IC=+0.275 (n=1262)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0109 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.253 (n=1830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` > `0.8629` → IC=+0.296 (n=2519)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8629 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.854` → IC=+0.342 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.854 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2331` → IC=+0.285 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2331 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4492` → IC=+0.233 (n=1220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4492 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.2917` → IC=+0.240 (n=1658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2917 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=4169)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2020.865` → IC=+0.238 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2020.865 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.249 (n=2377)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.267 (n=3424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.267)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.270 (n=2284)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0078 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1245` → IC=+0.294 (n=1506)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1245 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.268 (n=3550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=3094)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_20min` < `0.4663` → IC=+0.288 (n=3011)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4663 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.037` → IC=+0.269 (n=3568)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.037 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.269 (n=3460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.267)

- **PATRÓN** `volumen_pendiente_norm` > `0.2913` → IC=+0.286 (n=474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2913 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.273 (n=1448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.267)

- **PATRÓN** `volumen_spike_ratio` > `2.6495` → IC=+0.280 (n=1097)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6495 (IC base=+0.267)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.271 (n=2434)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.267)

- **PATRÓN** `libro_liquidez` > `1781.287` → IC=+0.272 (n=2281)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1781.287 (IC base=+0.267)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.279 (n=1098)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.267)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.176 (n=1297)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0032 (IC base=+0.139)

- **PATRÓN** `drift_60min` |x|≤ `0.0799` → IC=+0.150 (n=1297)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.0799 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.152 (n=4050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` > `0.1948` → IC=+0.188 (n=3885)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.1948 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.3291` → IC=+0.200 (n=1232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3291 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.079` → IC=+0.167 (n=619)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.079 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` < `0.6354` → IC=+0.156 (n=1296)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 0.6354 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.0681` → IC=+0.143 (n=1762)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` > 1.0681 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2716` → IC=+0.185 (n=547)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2716 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.1664` → IC=+0.143 (n=3360)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 2.1664 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5157` → IC=+0.146 (n=3411)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5157 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `295.0` → IC=+0.155 (n=2517)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 295.0 (IC base=+0.139)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.171 (n=3000)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0058 (IC base=+0.142)

- **PATRÓN** `drift_60min` |x|≤ `0.0813` → IC=+0.171 (n=1136)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0813 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.168 (n=1254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 17.0 (IC base=+0.142)

- **PATRÓN** `ibs_20min` < `0.6801` → IC=+0.189 (n=3408)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` < 0.6801 (IC base=+0.142)

- **PATRÓN** `dist_vwap_pct` < `0.1456` → IC=+0.158 (n=3350)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1456 (IC base=+0.142)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.997` → IC=+0.144 (n=3085)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 3.997 (IC base=+0.142)

- **PATRÓN** `volumen_regimen` < `1.0418` → IC=+0.152 (n=2999)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 1.0418 (IC base=+0.142)

- **PATRÓN** `volumen_pendiente_norm` > `0.2207` → IC=+0.198 (n=624)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2207 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` < `2.4286` → IC=+0.147 (n=3297)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 2.4286 (IC base=+0.142)

- **PATRÓN** `volumen_spike_ratio` > `1.7688` → IC=+0.149 (n=2199)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.7688 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.143 (n=4429)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.166 (n=1077)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 217.0 (IC base=+0.142)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.237 (n=1790)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.235 (n=4134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=3530)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.985` → IC=+0.322 (n=878)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.985 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` < `0.1317` → IC=+0.225 (n=3744)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1317 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.3503` → IC=+0.232 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3503 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.7503` → IC=+0.241 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7503 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.231 (n=4773)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `1998.2464` → IC=+0.240 (n=1315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1998.2464 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.250 (n=3345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0111 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.1813` → IC=+0.260 (n=1674)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1813 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=1445)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=1737)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.0625` → IC=+0.303 (n=1272)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0625 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.038` → IC=+0.307 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.038 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.3478` → IC=+0.304 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3478 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.1747` → IC=+0.256 (n=2447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1747 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.249 (n=1886)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1972.2784` → IC=+0.253 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1972.2784 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.250 (n=3170)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.245)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.193 (n=1376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0038 (IC base=+0.138)

- **PATRÓN** `drift_60min` |x|≤ `0.3436` → IC=+0.149 (n=3613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.3436 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.151 (n=4255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` > `0.8808` → IC=+0.269 (n=1368)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8808 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.1433` → IC=+0.167 (n=2039)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1433 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.064` → IC=+0.168 (n=618)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.064 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` < `0.8567` → IC=+0.153 (n=2738)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_regimen` < 0.8567 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.199 (n=552)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `1.5155` → IC=+0.155 (n=1766)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.5155 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `2.156` → IC=+0.143 (n=1819)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` > 2.156 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `5684.967` → IC=+0.231 (n=1861)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5684.967 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `86.0` → IC=+0.145 (n=2661)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 86.0 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.168 (n=3458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.008 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4487` → IC=+0.160 (n=3458)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.4487 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=1273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` < `0.7037` → IC=+0.201 (n=3458)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7037 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.1609` → IC=+0.163 (n=3273)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.1609 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.014` → IC=+0.154 (n=3018)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.014 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.8545` → IC=+0.162 (n=2306)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.8545 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2938` → IC=+0.209 (n=442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2938 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1993` → IC=+0.154 (n=2943)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 2.1993 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5249` → IC=+0.157 (n=2988)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5249 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `6645.4854` → IC=+0.222 (n=1153)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6645.4854 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `89.0` → IC=+0.165 (n=2278)

  - _Acción_: Kelly boost +0.82€ cuando `ballena_activa_n` < 89.0 (IC base=+0.150)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.153 (n=1390)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0129 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.146 (n=2939)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 11.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` > `0.7` → IC=+0.255 (n=2787)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.0324` → IC=+0.202 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0324 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.245` → IC=+0.272 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.245 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8739` → IC=+0.133 (n=2782)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` < 0.8739 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.127 (n=523)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` < `2.4871` → IC=+0.122 (n=4070)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.4871 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `2739.2749` → IC=+0.237 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2739.2749 (IC base=+0.117)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.157 (n=3440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.011 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.1415` → IC=+0.153 (n=1304)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1415 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.168 (n=1843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 15.0 (IC base=+0.135)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.242 (n=3443)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5417 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.042` → IC=+0.157 (n=3787)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.042 (IC base=+0.135)

- **PATRÓN** `volumen_regimen` < `1.1903` → IC=+0.141 (n=3909)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1903 (IC base=+0.135)

- **PATRÓN** `volumen_pendiente_norm` > `0.2299` → IC=+0.199 (n=689)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2299 (IC base=+0.135)

- **PATRÓN** `volumen_spike_ratio` < `1.4363` → IC=+0.165 (n=1241)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4363 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `2635.8438` → IC=+0.211 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2635.8438 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.146 (n=3745)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 49.0 (IC base=+0.135)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.258 (n=3812)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.238)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.244 (n=3981)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.238)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.243 (n=2556)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.238)

- **PATRÓN** `ibs_20min` > `0.6154` → IC=+0.270 (n=3405)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6154 (IC base=+0.238)

- **PATRÓN** `dist_vwap_pct` > `0.199` → IC=+0.250 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.199 (IC base=+0.238)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.1` → IC=+0.290 (n=671)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.1 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` < `1.2203` → IC=+0.239 (n=3811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2203 (IC base=+0.238)

- **PATRÓN** `volumen_regimen` > `0.6435` → IC=+0.243 (n=3811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6435 (IC base=+0.238)

- **PATRÓN** `volumen_pendiente_norm` > `0.2393` → IC=+0.256 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2393 (IC base=+0.238)

- **PATRÓN** `volumen_spike_ratio` > `2.4955` → IC=+0.252 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4955 (IC base=+0.238)

- **PATRÓN** `libro_liquidez` > `2982.5888` → IC=+0.245 (n=1273)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2982.5888 (IC base=+0.238)

- **PATRÓN** `sigma_h` > `0.0254` → IC=+0.268 (n=1320)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0254 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.249 (n=3723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.1364` → IC=+0.309 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1364 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.056` → IC=+0.279 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.056 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` < `0.7156` → IC=+0.245 (n=1742)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7156 (IC base=+0.245)

- **PATRÓN** `volumen_regimen` > `1.2139` → IC=+0.266 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2139 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.310 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `1.4276` → IC=+0.249 (n=3745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4276 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `2970.224` → IC=+0.248 (n=1319)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2970.224 (IC base=+0.245)

### GBM_LATE_5M
- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.232 (n=6162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.5297` → IC=+0.233 (n=7004)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5297 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=7048)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.9291` → IC=+0.262 (n=2334)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9291 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.4455` → IC=+0.226 (n=4955)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4455 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.568` → IC=+0.231 (n=3488)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.568 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.231 (n=2178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.8779` → IC=+0.225 (n=3299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8779 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.1043` → IC=+0.225 (n=6547)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1043 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.165` → IC=+0.232 (n=1972)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.165 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4471` → IC=+0.235 (n=2297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4471 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.228 (n=5028)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2589.868` → IC=+0.228 (n=7002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2589.868 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.235 (n=1616)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0045 (IC base=+0.206)

- **PATRÓN** `drift_60min` |x|≤ `0.5185` → IC=+0.217 (n=4848)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5185 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.215 (n=1883)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=2186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.206)

- **PATRÓN** `ibs_20min` < `0.6109` → IC=+0.210 (n=4266)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6109 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` > `0.6926` → IC=+0.216 (n=815)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6926 (IC base=+0.206)

- **PATRÓN** `dist_vwap_pct` < `0.2497` → IC=+0.202 (n=4363)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2497 (IC base=+0.206)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.774` → IC=+0.220 (n=4389)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.774 (IC base=+0.206)

- **PATRÓN** `volumen_regimen` < `1.0946` → IC=+0.211 (n=3929)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0946 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` < `0.0982` → IC=+0.209 (n=4483)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0982 (IC base=+0.206)

- **PATRÓN** `volumen_pendiente_norm` > `0.2235` → IC=+0.207 (n=970)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2235 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` < `1.5304` → IC=+0.209 (n=2102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5304 (IC base=+0.206)

- **PATRÓN** `volumen_spike_ratio` > `2.1901` → IC=+0.217 (n=2165)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1901 (IC base=+0.206)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.232 (n=2129)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 27.0 (IC base=+0.206)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.277 (n=824)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.300 (n=313)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.269 (n=940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.269)

- **PATRÓN** `ibs_20min` < `0.1406` → IC=+0.294 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1406 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.122` → IC=+0.290 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.122 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` < `1.2303` → IC=+0.273 (n=937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2303 (IC base=+0.269)

- **PATRÓN** `volumen_regimen` > `1.0873` → IC=+0.274 (n=427)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0873 (IC base=+0.269)

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

- **PATRÓN** `drift_60min` |x|≤ `0.5997` → IC=+0.212 (n=1031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5997 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.235 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.209)

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

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.295 (n=42)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.228)

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
- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.221 (n=1884)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.4639` → IC=+0.217 (n=1882)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4639 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.236 (n=672)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.4724` → IC=+0.221 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4724 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.1473` → IC=+0.212 (n=1881)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1473 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` < `0.4028` → IC=+0.221 (n=1896)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4028 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.314` → IC=+0.216 (n=1909)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.314 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.8646` → IC=+0.218 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8646 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` < `0.1013` → IC=+0.212 (n=1738)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1013 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.0749` → IC=+0.210 (n=795)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0749 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.3969` → IC=+0.229 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3969 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4922` → IC=+0.210 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4922 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=1879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.244 (n=498)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.4985` → IC=+0.220 (n=1493)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4985 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.209 (n=568)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.218 (n=998)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.0863` → IC=+0.208 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.0863 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.6674` → IC=+0.217 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6674 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.4169` → IC=+0.203 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4169 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.34` → IC=+0.209 (n=1368)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.34 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `1.2516` → IC=+0.211 (n=1493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2516 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.7194` → IC=+0.204 (n=1334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7194 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.0715` → IC=+0.226 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0715 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.51` → IC=+0.206 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.51 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.7743` → IC=+0.206 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7743 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `7792.286` → IC=+0.213 (n=995)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7792.286 (IC base=+0.203)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0086` → IC=+0.237 (n=535)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0086 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0122` → IC=+0.226 (n=549)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0122 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.240 (n=1223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `0.9872` → IC=+0.297 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9872 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` > `0.8376` → IC=+0.253 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8376 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.202` → IC=+0.251 (n=653)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.202 (IC base=+0.218)

- **PATRÓN** `volumen_regimen` < `0.6403` → IC=+0.251 (n=404)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6403 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.224 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2736` → IC=+0.228 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2736 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` < `2.1576` → IC=+0.226 (n=1036)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1576 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.227 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `4394.0844` → IC=+0.253 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4394.0844 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0138` → IC=+0.241 (n=854)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0138 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.0105` → IC=+0.253 (n=569)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0105 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.6578` → IC=+0.253 (n=853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6578 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.243 (n=779)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.241)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.262 (n=606)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.266 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.5875` → IC=+0.247 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5875 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.981` → IC=+0.263 (n=805)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.981 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` < `0.6704` → IC=+0.256 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6704 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` < `0.0822` → IC=+0.257 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0822 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.2044` → IC=+0.268 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2044 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.242 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `3930.2197` → IC=+0.269 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3930.2197 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `34.0` → IC=+0.276 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 34.0 (IC base=+0.241)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.150 (n=793)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.7446` → IC=+0.183 (n=1523)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.7446 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.1519` → IC=+0.144 (n=1107)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.1519 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.6174` → IC=+0.145 (n=1644)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6174 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.1474` → IC=+0.145 (n=446)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1474 (IC base=+0.059)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.124 (n=661)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0055 (IC base=+0.066)

- **PATRÓN** `ibs_20min` > `0.5412` → IC=+0.158 (n=642)

  - _Acción_: Kelly boost +0.79€ cuando `ibs_20min` > 0.5412 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1249` → IC=+0.169 (n=330)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.1249 (IC base=+0.066)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.129 (n=292)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0036 (IC base=+0.051)

- **PATRÓN** `ibs_20min` < `0.0689` → IC=+0.250 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0689 (IC base=+0.051)

- **PATRÓN** `volumen_pendiente_norm` > `0.2164` → IC=+0.154 (n=131)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2164 (IC base=+0.051)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.5412` → IC=-0.134 (n=233)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5412
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=455)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.150 (n=338)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0042 (IC base=+0.067)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.124 (n=386)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 15.0 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.9304` → IC=+0.257 (n=335)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9304 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1316` → IC=+0.166 (n=354)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1316 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.623` → IC=+0.189 (n=159)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.623 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.105` → IC=+0.265 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.105 (IC base=+0.035)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.7196` → IC=+0.139 (n=552)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.7196 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.7456` → IC=+0.153 (n=191)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.7456 (IC base=+0.029)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.171 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0098 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.1818` → IC=+0.251 (n=327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1818 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.903` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.903 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` > `1.1082` → IC=+0.203 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1082 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.1089` → IC=+0.165 (n=183)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1089 (IC base=+0.092)

- **PATRÓN** `volumen_spike_ratio` > `2.5569` → IC=+0.158 (n=153)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.5569 (IC base=+0.092)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.136 (n=237)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.03 (IC base=+0.092)

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

- **FILTRO** `ibs_20min` > `0.6985` → IC=-0.310 (n=114)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6985
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=224)

- **FILTRO** `dist_vwap_pct` > `0.4428` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4428
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=318)

- **FILTRO** `sigma_ewma_delta_pct` > `9.683` → IC=-0.300 (n=28)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.683
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=310)

- **FILTRO** `volumen_pendiente_norm` > `0.0448` → IC=-0.379 (n=31)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=-0.252 (n=216)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `9.679` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.679
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=97)

- **FILTRO** `volumen_regimen` < `1.2266` → IC=-0.297 (n=57)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2266
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=58)

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
- **FILTRO** `ibs_20min` < `0.5872` → IC=-0.471 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5872
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=99)

- **FILTRO** `volumen_regimen` < `0.7435` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7435
  - _Potencial_: sin este filtro IC_bueno=-0.144 (n=99)

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
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=106)

- **FILTRO** `volumen_pendiente_norm` > `0.1196` → IC=-0.265 (n=32)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1196
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=84)

- **FILTRO** `libro_spread` > `0.06` → IC=-0.250 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.06
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=111)

- **FILTRO** `sigma_ewma_delta_pct` > `2.394` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.394
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=40)

- **FILTRO** `volumen_regimen` < `0.9169` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9169
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=41)

- **FILTRO** `libro_spread` > `0.05` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.05
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=42)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.2459` → IC=-0.147 (n=304)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2459
  - _Potencial_: sin este filtro IC_bueno=+0.087 (n=916)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.240 (n=348)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.195 (n=349)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 16.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.68` → IC=+0.186 (n=766)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.68 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.8398` → IC=+0.306 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8398 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.392` → IC=+0.169 (n=182)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 10.392 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6243` → IC=+0.194 (n=256)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` < 0.6243 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.183 (n=575)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.3961` → IC=+0.203 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3961 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.855` → IC=+0.131 (n=269)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.855 (IC base=+0.029)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.7302` → IC=-0.171 (n=74)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7302
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=224)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.154 (n=76)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0065 (IC base=+0.047)

- **PATRÓN** `ibs_20min` > `0.7934` → IC=+0.134 (n=200)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` > 0.7934 (IC base=+0.047)

- **PATRÓN** `dist_vwap_pct` > `0.6482` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6482 (IC base=+0.047)

- **PATRÓN** `ibs_20min` < `0.251` → IC=+0.141 (n=422)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.251 (IC base=+0.080)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `ibs_20min` > `0.15` → IC=-0.129 (n=149)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=290)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.133 (n=246)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0028 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.136 (n=108)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.135 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` > `0.7163` → IC=+0.149 (n=246)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.7163 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.0986` → IC=+0.150 (n=201)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` < 0.0986 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.38` → IC=+0.144 (n=254)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 9.38 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.6244` → IC=+0.179 (n=82)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_regimen` < 0.6244 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `1.1883` → IC=+0.155 (n=82)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` > 1.1883 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1803` → IC=+0.145 (n=263)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.1803 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.7295` → IC=+0.173 (n=145)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.7295 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=211)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `1699.8582` → IC=+0.161 (n=246)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 1699.8582 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.659` → IC=+0.175 (n=78)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 10.659 (IC base=+0.008)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.2308` → IC=-0.268 (n=54)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2308
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=165)

- **FILTRO** `volumen_regimen` < `0.9283` → IC=-0.149 (n=109)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9283
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=110)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.283 (n=136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0103 (IC base=+0.254)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.275 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.254)

- **PATRÓN** `ibs_20min` > `0.6053` → IC=+0.279 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6053 (IC base=+0.254)

- **PATRÓN** `dist_vwap_pct` > `0.4722` → IC=+0.379 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4722 (IC base=+0.254)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.832` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.832 (IC base=+0.254)

- **PATRÓN** `volumen_regimen` < `0.6106` → IC=+0.314 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6106 (IC base=+0.254)

- **PATRÓN** `volumen_pendiente_norm` > `0.0951` → IC=+0.302 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0951 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` < `1.4822` → IC=+0.324 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4822 (IC base=+0.254)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.281 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.254)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.341 (n=149)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3649` → IC=+0.346 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3649 (IC base=+0.331)

- **PATRÓN** `elapsed_s` > `208.3` → IC=+0.397 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.3 (IC base=+0.331)

- **PATRÓN** `drift_15min` |x|≤ `2.3858` → IC=+0.354 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3858 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.380 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.331)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.382 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.331)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.331)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.307 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.292)

- **PATRÓN** `drift_15min` |x|≤ `2.3232` → IC=+0.339 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3232 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.6946` → IC=+0.326 (n=84)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6946 (IC base=+0.292)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.341 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `1335.0` → IC=+0.384 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1335.0 (IC base=+0.292)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.341 (n=149)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3649` → IC=+0.346 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3649 (IC base=+0.331)

- **PATRÓN** `elapsed_s` > `208.3` → IC=+0.397 (n=76)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 208.3 (IC base=+0.331)

- **PATRÓN** `drift_15min` |x|≤ `2.3858` → IC=+0.354 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3858 (IC base=+0.331)

- **PATRÓN** `drift_60min` |x|≤ `0.9778` → IC=+0.380 (n=115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9778 (IC base=+0.331)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.382 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.331)

- **PATRÓN** `ballena_activa_n` < `1071.0` → IC=+0.402 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1071.0 (IC base=+0.331)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3495` → IC=+0.307 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3495 (IC base=+0.292)

- **PATRÓN** `elapsed_s` > `229.9` → IC=+0.364 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 229.9 (IC base=+0.292)

- **PATRÓN** `drift_15min` |x|≤ `2.3232` → IC=+0.339 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3232 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.6946` → IC=+0.326 (n=84)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6946 (IC base=+0.292)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.341 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `1335.0` → IC=+0.384 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1335.0 (IC base=+0.292)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1491)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.097)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` > `0.5` → IC=+0.123 (n=1491)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.5 (IC base=+0.097)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=259)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=259)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1125)

### LIQUIDACIONES_15M#BNB#15min
- **PATRÓN** `liq_n` > `2.0` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `liq_n` > 2.0 (IC base=+0.083)

- **PATRÓN** `liq_usd_total` > `1200.92` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `liq_usd_total` > 1200.92 (IC base=+0.083)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.083)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.127 (n=81)

  - _Acción_: Kelly boost +0.63€ cuando `libro_spread` < 0.03 (IC base=+0.083)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `12324.2702` → IC=-0.152 (n=44)

  - _Acción_: SKIP cuando `libro_liquidez` < 12324.2702
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=92)

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

- **PATRÓN** `liq_usd_total` > `5115.78` → IC=+0.121 (n=138)

  - _Acción_: Kelly boost +0.61€ cuando `liq_usd_total` > 5115.78 (IC base=+0.050)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.192 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=4094)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.124 (n=277)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.495 (IC base=+0.024)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=1623)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=1577)

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
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=552)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=533)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.137 (n=224)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=+0.005)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1063)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=1063)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1389)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=1389)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=313)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=313)

- **FILTRO** `py_entrada` < `0.43` → IC=-0.132 (n=104)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=224)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.136 (n=64)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=385)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=434)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=316)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=419)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=419)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=392)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.123 (n=3017)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=7920)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.167 (n=100)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=118)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.135 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=124)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.167 (n=46)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=47)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.267 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=65)

### LIQUIDACIONES_DEPTH_FASE0#BTC#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.144 (n=344)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=861)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.121 (n=484)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=577)

- **PATRÓN** `py_entrada` < `0.51` → IC=+0.144 (n=374)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.51 (IC base=-0.013)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.128 (n=181)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=404)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=615)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=664)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.135 (n=310)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=673)

### LIQUIDACIONES_DEPTH_FASE0#XRP#15min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.131 (n=675)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=366)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.123 (n=173)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=383)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.132 (n=560)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=640)

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
- **FILTRO** `py_entrada` < `0.46` → IC=-0.177 (n=8493)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=26743)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.170 (n=8889)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=27613)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.197 (n=1576)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=4971)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.143 (n=2182)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=4299)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.136 (n=1680)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.134 (n=3032)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.5 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.44` → IC=-0.176 (n=1185)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=3669)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.179 (n=1250)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3860)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` > `0.62` → IC=-0.196 (n=1615)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=5019)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.136 (n=2009)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 1.0 (IC base=+0.033)

- **PATRÓN** `libro_liquidez` > `1741.6122` → IC=+0.123 (n=2223)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1741.6122 (IC base=+0.033)

### MOMENTUM_IBS_15M_BALLENA#ETH#15min
- **FILTRO** `py_entrada` > `0.575` → IC=-0.177 (n=1278)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=3935)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.485` → IC=-0.163 (n=1628)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=4943)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2448)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.162 (n=772)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2372)

- **FILTRO** `py_entrada` > `0.575` → IC=-0.180 (n=973)

  - _Acción_: SKIP cuando `py_entrada` > 0.575
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3156)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=4108)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=1116)

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
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=807)

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
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=54118)

- **FILTRO** `py_entrada` < `0.32` → IC=-0.299 (n=18893)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=59251)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.235 (n=19529)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=58615)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.152 (n=26321)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=51823)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.245 (n=24304)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.008 (n=73464)

- **FILTRO** `ibs_7min` > `0.28` → IC=-0.183 (n=24379)

  - _Acción_: SKIP cuando `ibs_7min` > 0.28
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=73389)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=3368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=10619)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.320 (n=3467)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=10520)

- **FILTRO** `ibs_7min` < `0.7097` → IC=-0.255 (n=4612)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7097
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=9375)

- **FILTRO** `py_entrada` > `0.72` → IC=-0.279 (n=4106)

  - _Acción_: SKIP cuando `py_entrada` > 0.72
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=12806)

- **FILTRO** `ibs_7min` > `0.7708` → IC=-0.211 (n=4227)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7708
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=12685)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=3139)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=9806)

- **FILTRO** `ibs_7min` < `0.7135` → IC=-0.209 (n=3236)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7135
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=9709)

- **FILTRO** `ballena_activa_n` > `156.0` → IC=-0.201 (n=3228)

  - _Acción_: SKIP cuando `ballena_activa_n` > 156.0
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=9717)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.266 (n=3013)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=10222)

- **FILTRO** `ibs_7min` > `0.2649` → IC=-0.192 (n=3308)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2649
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=9927)

- **FILTRO** `ballena_activa_n` > `152.0` → IC=-0.178 (n=3292)

  - _Acción_: SKIP cuando `ballena_activa_n` > 152.0
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=9943)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.166 (n=3232)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=10215)

- **FILTRO** `py_entrada` < `0.3` → IC=-0.324 (n=3199)

  - _Acción_: SKIP cuando `py_entrada` < 0.3
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=10248)

- **FILTRO** `ibs_7min` < `0.2895` → IC=-0.251 (n=4436)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2895
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=9011)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.170 (n=3342)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=10105)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.260 (n=4303)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=13598)

- **FILTRO** `ibs_7min` > `0.7251` → IC=-0.183 (n=4475)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7251
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=13426)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.264 (n=3143)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=9473)

- **FILTRO** `ibs_7min` < `0.7135` → IC=-0.200 (n=3154)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7135
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=9462)

- **FILTRO** `ballena_activa_n` > `24.0` → IC=-0.192 (n=3148)

  - _Acción_: SKIP cuando `ballena_activa_n` > 24.0
  - _Potencial_: sin este filtro IC_bueno=-0.080 (n=9468)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.258 (n=3043)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=10070)

- **FILTRO** `ibs_7min` > `0.2722` → IC=-0.179 (n=3278)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2722
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=9835)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.169 (n=3260)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=9853)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.302 (n=3008)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=9478)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.235 (n=4115)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=8371)

- **FILTRO** `ballena_activa_n` > `12.0` → IC=-0.218 (n=3057)

  - _Acción_: SKIP cuando `ballena_activa_n` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=9429)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.199 (n=4505)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=14427)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.133 (n=4103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=8560)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.312 (n=3072)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=9591)

- **FILTRO** `ibs_7min` < `0.7288` → IC=-0.223 (n=4178)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7288
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=8485)

- **FILTRO** `ballena_activa_n` > `8.0` → IC=-0.191 (n=3161)

  - _Acción_: SKIP cuando `ballena_activa_n` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=9502)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.228 (n=4350)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=13325)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=121)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.163 (n=304)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=1015)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=1304)

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
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=334)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=451)

- **FILTRO** `py_entrada` > `0.58` → IC=-0.216 (n=192)

  - _Acción_: SKIP cuando `py_entrada` > 0.58
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=588)

- **FILTRO** `libro_liquidez` < `3306.2556` → IC=-0.150 (n=195)

  - _Acción_: SKIP cuando `libro_liquidez` < 3306.2556
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=585)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.4305` → IC=+0.146 (n=719)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.4305 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.130 (n=1432)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 14.0 (IC base=+0.126)

- **PATRÓN** `total_vol_5m` < `721.291` → IC=+0.155 (n=696)

  - _Acción_: Kelly boost +0.77€ cuando `total_vol_5m` < 721.291 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `3568.0852` → IC=+0.141 (n=717)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3568.0852 (IC base=+0.126)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.182 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.138)

- **PATRÓN** `total_vol_5m` < `377.422` → IC=+0.160 (n=327)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 377.422 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `2524.1916` → IC=+0.230 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2524.1916 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `6.0` → IC=+0.142 (n=185)

  - _Acción_: Kelly boost +0.71€ cuando `ballena_activa_n` < 6.0 (IC base=+0.138)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.133 (n=328)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.138 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 14.0 (IC base=+0.120)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4165` → IC=+0.175 (n=198)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.88€ cuando `delta_ratio` |x|> 0.4165 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=275)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `total_vol_5m` < `657.7094` → IC=+0.162 (n=261)

  - _Acción_: Kelly boost +0.81€ cuando `total_vol_5m` < 657.7094 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `59.0` → IC=+0.189 (n=104)

  - _Acción_: Kelly boost +0.94€ cuando `ballena_activa_n` < 59.0 (IC base=+0.132)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.418` → IC=+0.194 (n=178)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.97€ cuando `delta_ratio` |x|> 0.418 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.176 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 5.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `5947.939` → IC=+0.171 (n=235)

  - _Acción_: Kelly boost +0.85€ cuando `total_vol_5m` < 5947.939 (IC base=+0.139)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.136 (n=281)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 13.0 (IC base=+0.100)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=204)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.100)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `6.3582` → IC=-0.218 (n=83)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 6.3582
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=163)

- **FILTRO** `pct_vs_K` |x|> `3.3889` → IC=-0.170 (n=310)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3889
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=605)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.151 (n=302)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0045 (IC base=-0.040)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `4.205` → IC=-0.229 (n=68)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.205
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=207)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.296 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.002)

- **PATRÓN** `pct_vs_K` |x|≤ `1.73` → IC=+0.199 (n=91)

  - _Acción_: Kelly boost +0.99€ cuando `pct_vs_K` |x|≤ 1.73 (IC base=-0.002)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.01` → IC=-0.156 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=59)

- **FILTRO** `T_h` < `243.9505` → IC=-0.182 (n=64)

  - _Acción_: SKIP cuando `T_h` < 243.9505
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=25)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `96.5959` → IC=-0.163 (n=87)

  - _Acción_: SKIP cuando `T_h` < 96.5959
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=87)

### PRICE_TARGET_GBM#SOL#reach
- **FILTRO** `T_h` < `146.0708` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `T_h` < 146.0708
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `87.9882` → IC=-0.246 (n=408)

  - _Acción_: SKIP cuando `T_h` < 87.9882
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=409)

- **FILTRO** `T_h` > `142.6336` → IC=-0.210 (n=181)

  - _Acción_: SKIP cuando `T_h` > 142.6336
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=548)

- **FILTRO** `pct_vs_K` |x|> `3.0033` → IC=-0.400 (n=178)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0033
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=551)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` < `60.8769` → IC=-0.219 (n=87)

  - _Acción_: SKIP cuando `T_h` < 60.8769
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=179)

- **FILTRO** `T_h` > `143.1632` → IC=-0.210 (n=67)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=202)

- **FILTRO** `pct_vs_K` |x|> `1.0921` → IC=-0.234 (n=201)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.0921
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=68)

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
- **FILTRO** `sigma_h` < `0.0092` → IC=-0.324 (n=117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0092
  - _Potencial_: sin este filtro IC_bueno=-0.248 (n=117)

- **FILTRO** `T_h` > `49.8274` → IC=-0.291 (n=175)

  - _Acción_: SKIP cuando `T_h` > 49.8274
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=59)

- **FILTRO** `sigma_h` < `0.0056` → IC=-0.202 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.105 (n=165)

- **FILTRO** `pct_vs_K` |x|> `2.0379` → IC=-0.383 (n=109)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.0379
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=111)

- **PATRÓN** `pct_vs_K` |x|≤ `1.0948` → IC=+0.127 (n=73)

  - _Acción_: Kelly boost +0.63€ cuando `pct_vs_K` |x|≤ 1.0948 (IC base=-0.131)

### PRICE_TARGET_GBM_FADE#ETH#reach
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
- **FILTRO** `sigma_h` > `0.013` → IC=-0.212 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=153)

- **FILTRO** `sigma_h` < `0.0099` → IC=-0.244 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=155)

- **FILTRO** `T_h` > `70.1154` → IC=-0.218 (n=154)

  - _Acción_: SKIP cuando `T_h` > 70.1154
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=77)

- **FILTRO** `sigma_h` < `0.0087` → IC=-0.286 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0087
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=121)

- **FILTRO** `pct_vs_K` |x|> `2.975` → IC=-0.429 (n=54)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.975
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=107)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1186` → IC=+0.454 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1186 (IC base=+0.335)

- **PATRÓN** `sigma_h` > `0.0128` → IC=+0.357 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0128 (IC base=+0.335)

- **PATRÓN** `T_h` < `0.3439` → IC=+0.381 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.3439 (IC base=+0.335)

- **PATRÓN** `T_h` > `0.4704` → IC=+0.361 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4704 (IC base=+0.335)

- **PATRÓN** `dist_50` > `0.4679` → IC=+0.482 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4679 (IC base=+0.335)

- **PATRÓN** `edge` > `0.1` → IC=+0.429 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1 (IC base=+0.392)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.412 (n=191)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.392)

- **PATRÓN** `T_h` < `0.7322` → IC=+0.421 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7322 (IC base=+0.392)

- **PATRÓN** `T_h` > `1.484` → IC=+0.397 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.392)

- **PATRÓN** `dist_50` > `0.3717` → IC=+0.443 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3717 (IC base=+0.392)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.412 (n=339)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.392)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `edge` > `0.1161` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1161 (IC base=+0.188)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.274 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.210 (n=29)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.188)

- **PATRÓN** `T_h` < `0.7285` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.7285 (IC base=+0.188)

- **PATRÓN** `T_h` > `1.4441` → IC=+0.250 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4441 (IC base=+0.188)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.273 (n=42)

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

- **PATRÓN** `T_h` < `0.5167` → IC=+0.433 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5167 (IC base=+0.410)

- **PATRÓN** `dist_50` > `0.4122` → IC=+0.483 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4122 (IC base=+0.410)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.444 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.410)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1745` → IC=+0.486 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1745 (IC base=+0.438)

- **PATRÓN** `sigma_h` < `0.0163` → IC=+0.458 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0163 (IC base=+0.438)

- **PATRÓN** `T_h` > `0.3968` → IC=+0.458 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.3968 (IC base=+0.438)

- **PATRÓN** `dist_50` > `0.3553` → IC=+0.472 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3553 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.438)

- **PATRÓN** `edge` > `0.1954` → IC=+0.471 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1954 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.474 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.464)

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
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=496)

- **PATRÓN** `streak_estiramiento` < `0.8251` → IC=+0.128 (n=342)

  - _Acción_: Kelly boost +0.64€ cuando `streak_estiramiento` < 0.8251 (IC base=+0.059)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.125 (n=254)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 29.0 (IC base=+0.059)

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

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.145 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 10.0 (IC base=+0.090)

- **PATRÓN** `streak_estiramiento` < `0.5763` → IC=+0.165 (n=168)

  - _Acción_: Kelly boost +0.82€ cuando `streak_estiramiento` < 0.5763 (IC base=+0.090)

- **PATRÓN** `ballena_activa_n` < `31.0` → IC=+0.154 (n=163)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 31.0 (IC base=+0.090)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=1088)

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
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=5160)

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
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=2987)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.179 (n=2551)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0065 (IC base=+0.135)

- **PATRÓN** `drift_60min` |x|≤ `0.2266` → IC=+0.157 (n=5800)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.2266 (IC base=+0.135)

- **PATRÓN** `drift_15min` |x|≤ `1.0723` → IC=+0.136 (n=5797)

  - _Acción_: Kelly boost +0.68€ cuando `drift_15min` |x|≤ 1.0723 (IC base=+0.135)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.133` → IC=+0.148 (n=2396)

  - _Acción_: Kelly boost +0.74€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.133 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.147 (n=5352)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 6.0 (IC base=+0.135)

- **PATRÓN** `ibs_15` > `0.569` → IC=+0.216 (n=5179)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.569 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` > `0.139` → IC=+0.125 (n=2710)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.139 (IC base=+0.135)

- **PATRÓN** `dist_vwap_pct` < `0.544` → IC=+0.122 (n=5554)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.544 (IC base=+0.135)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.251` → IC=+0.237 (n=1093)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.251 (IC base=+0.135)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=3228)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `4436.9386` → IC=+0.171 (n=1933)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 4436.9386 (IC base=+0.135)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=2285)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.250 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.254 (n=278)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.203)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2672` → IC=+0.231 (n=277)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2672 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.232 (n=767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.7064` → IC=+0.273 (n=831)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7064 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.3824` → IC=+0.226 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3824 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.5302` → IC=+0.205 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5302 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.343` → IC=+0.300 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.343 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `14141.7548` → IC=+0.226 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14141.7548 (IC base=+0.203)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.144 (n=1044)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0072 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1093` → IC=+0.148 (n=696)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.74€ cuando `drift_60min` |x|≤ 0.1093 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.139 (n=954)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 6.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` > `0.4895` → IC=+0.217 (n=1044)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.4895 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.1202` → IC=+0.150 (n=653)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1202 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.6245` → IC=+0.132 (n=1185)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.6245 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.063` → IC=+0.288 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.063 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6033.789` → IC=+0.170 (n=473)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6033.789 (IC base=+0.132)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `ibs_15` > `0.7619` → IC=+0.131 (n=775)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.65€ cuando `ibs_15` > 0.7619 (IC base=+0.050)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0145` → IC=+0.148 (n=649)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0145 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.149 (n=1475)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0125 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2313` → IC=+0.176 (n=1475)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.2313 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0577` → IC=+0.144 (n=1475)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio_macro` |x|> 0.0577 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0924` → IC=+0.197 (n=457)

  - _Acción_: Kelly boost +0.99€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0924 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.152 (n=1353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.5333` → IC=+0.215 (n=1318)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5333 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.2042` → IC=+0.159 (n=670)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.2042 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.602` → IC=+0.184 (n=245)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 21.602 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2933.4449` → IC=+0.190 (n=669)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2933.4449 (IC base=+0.144)

- **PATRÓN** `ibs_15` < `0.1143` → IC=+0.149 (n=1130)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.1143 (IC base=+0.070)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `drift_60min` |x|≤ `0.1109` → IC=+0.365 (n=511)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1109 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.379 (n=510)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1344` → IC=+0.380 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1344 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.374 (n=808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.7906` → IC=+0.394 (n=765)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7906 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1534` → IC=+0.382 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1534 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.976` → IC=+0.396 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.976 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `3887.2465` → IC=+0.376 (n=684)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1066` → IC=+0.369 (n=265)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1066 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1293` → IC=+0.384 (n=264)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1293 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.296` → IC=+0.374 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.296 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.372 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=185)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.8152` → IC=+0.399 (n=354)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8152 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.159` → IC=+0.376 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.159 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` < `0.6408` → IC=+0.368 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6408 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.356` → IC=+0.392 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.356 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `4202.8422` → IC=+0.379 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4202.8422 (IC base=+0.366)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.205 (n=2816)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2819)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.221 (n=2401)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=3234)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1411` → IC=+0.217 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1411 (IC base=-0.085)

- **PATRÓN** `ibs_15` > `0.6314` → IC=+0.276 (n=1264)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6314 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.201 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.085)

- **PATRÓN** `dist_vwap_pct` < `0.5648` → IC=+0.199 (n=1340)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.5648 (IC base=-0.085)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2308` → IC=+0.273 (n=1756)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2308 (IC base=-0.001)

- **PATRÓN** `ibs_15` < `0.371` → IC=+0.286 (n=5267)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.371 (IC base=-0.001)

- **PATRÓN** `dist_vwap_pct` > `0.6762` → IC=+0.272 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6762 (IC base=-0.001)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0436` → IC=-0.227 (n=2447)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0436
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=1206)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.215 (n=913)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.174 (n=2740)

- **FILTRO** `sigma_ewma_delta_pct` > `22.117` → IC=-0.251 (n=517)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 22.117
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=3136)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.145 (n=345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0031 (IC base=+0.068)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2668` → IC=+0.283 (n=150)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2668 (IC base=+0.068)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.145` → IC=+0.270 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.145 (IC base=+0.068)

- **PATRÓN** `ibs_15` > `0.7593` → IC=+0.316 (n=450)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7593 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` > `0.1043` → IC=+0.277 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1043 (IC base=+0.068)

- **PATRÓN** `dist_vwap_pct` < `0.5105` → IC=+0.282 (n=502)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5105 (IC base=+0.068)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.961` → IC=+0.151 (n=227)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 21.961 (IC base=+0.068)

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
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=823)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.161 (n=555)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.006 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.159` → IC=+0.164 (n=555)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.159 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3014` → IC=+0.196 (n=495)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3014 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.164 (n=450)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 11.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5733` → IC=+0.240 (n=630)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5733 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6362` → IC=+0.161 (n=119)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6362 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` < `0.2678` → IC=+0.147 (n=587)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2678 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.001` → IC=+0.260 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.001 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=823)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `7306.8584` → IC=+0.163 (n=286)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 7306.8584 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.255 (n=1386)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.4581` → IC=+0.245 (n=2078)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4581 (IC base=+0.243)

- **PATRÓN** `drift_15min` |x|≤ `0.7985` → IC=+0.256 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7985 (IC base=+0.243)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2077` → IC=+0.268 (n=942)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2077 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=764)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.243 (n=1428)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.243)

- **PATRÓN** `ibs_15` < `0.3855` → IC=+0.273 (n=2078)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3855 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` > `0.3905` → IC=+0.266 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3905 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.394` → IC=+0.247 (n=902)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.394 (IC base=+0.243)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1915` → IC=-0.276 (n=333)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1915
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=1000)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.273 (n=452)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=881)

- **FILTRO** `drift_15min` |x|> `0.9451` → IC=-0.297 (n=333)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.9451
  - _Potencial_: sin este filtro IC_bueno=-0.172 (n=1000)

- **FILTRO** `sigma_ewma_delta_pct` > `6.088` → IC=-0.205 (n=296)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.088
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=1037)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.188 (n=46)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.203)

- **PATRÓN** `ibs_15` > `0.9231` → IC=+0.380 (n=23)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9231 (IC base=-0.203)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.203)

- **PATRÓN** `ballena_activa_n` < `37.0` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 37.0 (IC base=-0.203)

- **PATRÓN** `ibs_15` < `0.381` → IC=+0.296 (n=908)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.381 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` < `0.4628` → IC=+0.250 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4628 (IC base=-0.026)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1191` → IC=-0.264 (n=802)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1191
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=805)

- **FILTRO** `sigma_h` > `0.0125` → IC=-0.242 (n=1205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0125
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=402)

- **FILTRO** `drift_15min` |x|> `1.2845` → IC=-0.277 (n=401)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.2845
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=1206)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=1587)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.222)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.222)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0719` → IC=+0.283 (n=1123)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0719 (IC base=-0.011)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1183` → IC=+0.296 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1183 (IC base=-0.011)

- **PATRÓN** `ibs_15` < `0.3289` → IC=+0.297 (n=1257)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3289 (IC base=-0.011)

- **PATRÓN** `dist_vwap_pct` > `0.7684` → IC=+0.336 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7684 (IC base=-0.011)

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
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.297 (n=470)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.282 (n=471)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0065 (IC base=+0.282)

- **PATRÓN** `drift_60min` |x|≤ `0.0527` → IC=+0.311 (n=470)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0527 (IC base=+0.282)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2213` → IC=+0.290 (n=862)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2213 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.299 (n=1278)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.282)

- **PATRÓN** `ibs_15` > `0.8377` → IC=+0.310 (n=1410)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8377 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.312 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.851` → IC=+0.386 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.851 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `13088.9696` → IC=+0.299 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13088.9696 (IC base=+0.282)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.303 (n=328)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0035 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.0763` → IC=+0.304 (n=329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0763 (IC base=+0.276)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2692` → IC=+0.284 (n=248)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2692 (IC base=+0.276)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.282 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.301 (n=686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.276)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.300 (n=745)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2555` → IC=+0.312 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2555 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.686` → IC=+0.391 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.686 (IC base=+0.276)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.277 (n=963)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `15684.0606` → IC=+0.316 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15684.0606 (IC base=+0.276)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.295 (n=666)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0499` → IC=+0.321 (n=222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0499 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0654` → IC=+0.290 (n=666)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0654 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1008` → IC=+0.309 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1008 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=639)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.289 (n=472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.8455` → IC=+0.317 (n=666)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8455 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2797` → IC=+0.315 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2797 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` < `0.6422` → IC=+0.288 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6422 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.128` → IC=+0.376 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.128 (IC base=+0.288)

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
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=372)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.180 (n=123)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=372)

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

- **FILTRO** `sigma_h` < `0.006` → IC=-0.174 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=15)

- **FILTRO** `ballena_activa_n` > `595.0` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 595.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=35)

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

- **FILTRO** `sigma_h` < `0.0054` → IC=-0.321 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0054
  - _Potencial_: sin este filtro IC_bueno=-0.318 (n=9)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0773` → IC=-0.243 (n=33)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0773
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

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
- **PATRÓN** `ratio` < `0.9696` → IC=+0.337 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9696 (IC base=+0.143)

- **PATRÓN** `T_h` > `115.2222` → IC=+0.356 (n=3055)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 115.2222 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0189` → IC=+0.390 (n=550)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0189 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `ratio` < `0.9922` → IC=+0.206 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9922 (IC base=+0.095)

- **PATRÓN** `T_h` > `110.2068` → IC=+0.321 (n=1099)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.2068 (IC base=+0.302)

- **PATRÓN** `ratio` > `1.0159` → IC=+0.376 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0159 (IC base=+0.302)

### WEEKLY_PRICE#ETH
- **PATRÓN** `ratio` < `0.9833` → IC=+0.378 (n=277)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9833 (IC base=+0.195)

- **PATRÓN** `T_h` > `111.9957` → IC=+0.353 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9957 (IC base=+0.323)

- **PATRÓN** `ratio` > `1.0277` → IC=+0.404 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0277 (IC base=+0.323)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.0624` → IC=+0.417 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.0624 (IC base=+0.397)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.569 sube el IC de +0.135 a +0.216 en UPDOWN_GBM#15min (n=5179). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7064 sube el IC de +0.203 a +0.273 en UPDOWN_GBM#BTC#15min (n=831). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.4895 sube el IC de +0.132 a +0.217 en UPDOWN_GBM#ETH#15min (n=1044). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5333 sube el IC de +0.144 a +0.215 en UPDOWN_GBM#XRP#15min (n=1318). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6314 sube el IC de -0.085 a +0.276 en UPDOWN_GBM_15M_TARDIO (n=1264). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.371 sube el IC de -0.001 a +0.286 en UPDOWN_GBM_15M_TARDIO (n=5267). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7593 sube el IC de +0.068 a +0.316 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=450). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.6255 sube el IC de -0.184 a +0.289 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=74). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.5733 sube el IC de +0.146 a +0.240 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=630). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3855 sube el IC de +0.243 a +0.273 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=2078). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.9231 sube el IC de -0.203 a +0.380 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=23). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.381 sube el IC de -0.026 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=908). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.222 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3289 sube el IC de -0.011 a +0.297 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=1257). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.097 a +0.286 en UPDOWN_GBM_ETH_15M_HORA7 (n=26). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8358 sube el IC de +0.097 a +0.286 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=26). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8377 sube el IC de +0.282 a +0.310 en UPDOWN_GBM_IBS_ALTO (n=1410). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.276 a +0.300 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=745). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8455 sube el IC de +0.288 a +0.317 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=666). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.7906 sube el IC de +0.365 a +0.394 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=765). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8112 sube el IC de +0.362 a +0.384 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=369). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.8152 sube el IC de +0.366 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=354). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 2237 | +0.082 | +220.55€ | 1 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 2237 | +0.082 | +220.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1827 | +0.082 | +182.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1827 | +0.082 | +182.01€ | 1 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 285 | +0.068 | +10.79€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 285 | +0.068 | +10.79€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 94 | +0.125 | +28.08€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 94 | +0.125 | +28.08€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 1240 | -0.016 | +72.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 1240 | -0.016 | +72.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#DOGE#15min | 7 | +0.019 | +3.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 950 | -0.033 | +51.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 950 | -0.033 | +51.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 198 | +0.060 | +24.28€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 198 | +0.060 | +24.28€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 85 | -0.017 | -6.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 49122 | -0.085 | -6308.87€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 3110 | +0.083 | -304.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 46012 | -0.096 | -6004.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4896 | -0.110 | -820.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4896 | -0.110 | -820.56€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 3110 | +0.083 | -304.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 3110 | +0.083 | -304.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4991 | -0.105 | -936.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4991 | -0.105 | -936.92€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 13475 | -0.043 | -1323.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 13475 | -0.043 | -1323.51€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 13398 | -0.113 | -1393.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 13398 | -0.113 | -1393.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 9252 | -0.137 | -1530.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 9252 | -0.137 | -1530.37€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 52115 | -0.012 | +2760.71€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 13443 | +0.004 | +1478.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 38672 | -0.017 | +1282.23€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 52115 | -0.012 | +2760.71€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 13443 | +0.004 | +1478.47€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 38672 | -0.017 | +1282.23€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 197375 | +0.112 | -8302.55€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#15min | 22370 | +0.180 | -715.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 911 | +0.015 | -73.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 162868 | +0.105 | -7105.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 11226 | +0.094 | -409.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 26991 | +0.102 | -1946.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 81 | -0.175 | +14.04€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 26895 | +0.103 | -1948.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 37211 | +0.123 | -659.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5631 | +0.178 | -236.56€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 26961 | +0.119 | -229.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 4577 | +0.081 | -171.29€ | 1 | 2 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 27038 | +0.098 | -1970.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 91 | -0.113 | +13.93€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 26932 | +0.099 | -1973.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 42192 | +0.123 | -899.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 10566 | +0.178 | -269.95€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 27391 | +0.105 | -557.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 4223 | +0.103 | -62.93€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL | 36924 | +0.111 | -1657.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5907 | +0.198 | -250.46€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 814 | +0.040 | -19.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 27777 | +0.095 | -1213.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2426 | +0.105 | -174.79€ | 1 | 4 |
| ✅ FAVORITO_CONFIRMADO#XRP | 27019 | +0.107 | -1169.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 94 | -0.125 | +13.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 26912 | +0.108 | -1183.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 32047 | +0.191 | -2310.42€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 32047 | +0.191 | -2310.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 7263 | +0.165 | -799.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 7263 | +0.165 | -799.16€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 4707 | +0.196 | -183.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 4707 | +0.196 | -183.93€ | 3 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 7106 | +0.173 | -643.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 7106 | +0.173 | -643.77€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 5920 | +0.251 | -205.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 5920 | +0.251 | -205.81€ | 0 | 4 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 6972 | +0.183 | -491.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 6972 | +0.183 | -491.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1283 | +0.425 | -47.96€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1283 | +0.425 | -47.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 535 | +0.439 | -5.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 535 | +0.439 | -5.45€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 521 | +0.423 | -20.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 521 | +0.423 | -20.27€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 213 | +0.398 | -18.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 213 | +0.398 | -18.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 113341 | +0.199 | -8334.07€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 113341 | +0.199 | -8334.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 19625 | +0.177 | -2276.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 19625 | +0.177 | -2276.50€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 18277 | +0.224 | -617.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 18277 | +0.224 | -617.12€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 19458 | +0.180 | -2055.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 19458 | +0.180 | -2055.41€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 18423 | +0.217 | -736.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 18423 | +0.217 | -736.29€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 18707 | +0.204 | -1151.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 18707 | +0.204 | -1151.13€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 18851 | +0.197 | -1497.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 18851 | +0.197 | -1497.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 43911 | +0.116 | +312.04€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 43911 | +0.116 | +312.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 21860 | +0.116 | +194.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 21860 | +0.116 | +194.34€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 22051 | +0.115 | +117.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 22051 | +0.115 | +117.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2683 | +0.293 | -14.44€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2683 | +0.293 | -14.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 1225 | +0.282 | -28.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 1225 | +0.282 | -28.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1316 | +0.296 | +7.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1316 | +0.296 | +7.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 142 | +0.347 | +6.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 142 | +0.347 | +6.73€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 1238 | +0.438 | -5.78€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 1238 | +0.438 | -5.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 590 | +0.434 | -8.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 590 | +0.434 | -8.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 596 | +0.442 | +1.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 596 | +0.442 | +1.30€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 52 | +0.407 | +1.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 52 | +0.407 | +1.41€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1983 | +0.067 | -91.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 725 | +0.046 | -64.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1258 | +0.079 | -26.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 82 | +0.107 | +3.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1549 | +0.074 | -45.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 291 | +0.053 | -19.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1258 | +0.079 | -26.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 352 | +0.025 | -48.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 89267 | +0.100 | -2049.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 7215 | +0.096 | +157.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 82052 | +0.101 | -2206.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 48763 | +0.105 | -469.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 7215 | +0.096 | +157.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 41548 | +0.106 | -626.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 19073 | +0.109 | -87.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 19073 | +0.109 | -87.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 21431 | +0.082 | -1492.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 21431 | +0.082 | -1492.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 914 | +0.186 | -109.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 914 | +0.186 | -109.27€ | 5 | 4 |
| ✅ GBM_LATE_15M | 60615 | +0.101 | +33950.38€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 60615 | +0.101 | +33950.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 10038 | +0.225 | +8661.14€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 10038 | +0.225 | +8661.14€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 9375 | +0.177 | +7414.19€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 9375 | +0.177 | +7414.19€ | 0 | 22 |
| ✅ GBM_LATE_15M#DOGE | 10859 | +0.207 | +8594.77€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 10859 | +0.207 | +8594.77€ | 0 | 21 |
| ✅ GBM_LATE_15M#ETH | 8077 | +0.059 | +2669.65€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 8077 | +0.059 | +2669.65€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 8437 | -0.027 | +2202.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 8437 | -0.027 | +2202.83€ | 4 | 17 |
| ✅ GBM_LATE_15M#XRP | 13829 | -0.021 | +4407.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 13829 | -0.021 | +4407.78€ | 3 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 64205 | +0.086 | +37401.05€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 64205 | +0.086 | +37401.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 12436 | -0.002 | +6584.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 12436 | -0.002 | +6584.21€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 13798 | +0.006 | +3754.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 13798 | +0.006 | +3754.09€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 8690 | +0.295 | +9952.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 8690 | +0.295 | +9952.48€ | 0 | 23 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 12237 | +0.016 | +3848.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 12237 | +0.016 | +3848.29€ | 1 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 9833 | +0.046 | +4439.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 9833 | +0.046 | +4439.59€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 7211 | +0.315 | +8822.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 7211 | +0.315 | +8822.39€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 47827 | +0.179 | +39691.29€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 47827 | +0.179 | +39691.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 7211 | +0.240 | +6732.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 7211 | +0.240 | +6732.90€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 7587 | +0.141 | +5646.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 7587 | +0.141 | +5646.12€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 7690 | +0.225 | +6704.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 7690 | +0.225 | +6704.96€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 8203 | +0.130 | +6354.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 8203 | +0.130 | +6354.91€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 9037 | +0.121 | +6881.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 9037 | +0.121 | +6881.47€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 8099 | +0.234 | +7370.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 8099 | +0.234 | +7370.95€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 13103 | +0.126 | +6644.29€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 13103 | +0.126 | +6644.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 669 | +0.162 | +439.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 669 | +0.162 | +439.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 3472 | +0.126 | +1877.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 3472 | +0.126 | +1877.38€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 507 | +0.158 | +290.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 3795 | +0.126 | +1882.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 3795 | +0.126 | +1882.72€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 3430 | +0.100 | +1384.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 3430 | +0.100 | +1384.94€ | 0 | 12 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 1230 | +0.167 | +768.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 1230 | +0.167 | +768.64€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 60853 | +0.189 | +50369.92€ | 0 | 20 |
| ✅ GBM_LATE_15M_TARDIO#15min | 60853 | +0.189 | +50369.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 9599 | +0.250 | +9279.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 9599 | +0.250 | +9279.38€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 9723 | +0.140 | +6848.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 9723 | +0.140 | +6848.14€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 10324 | +0.235 | +9336.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 10324 | +0.235 | +9336.39€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 10082 | +0.143 | +7530.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 10082 | +0.143 | +7530.31€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 10771 | +0.126 | +7724.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 10771 | +0.126 | +7724.40€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 10354 | +0.241 | +9651.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 10354 | +0.241 | +9651.30€ | 0 | 20 |
| ✅ GBM_LATE_5M | 15798 | +0.217 | +13200.79€ | 0 | 27 |
| ✅ GBM_LATE_5M#5min | 15798 | +0.217 | +13200.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 1792 | +0.250 | +1722.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 1792 | +0.250 | +1722.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 3288 | +0.211 | +2826.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 3288 | +0.211 | +2826.97€ | 0 | 25 |
| ✅ GBM_LATE_5M#DOGE | 1453 | +0.210 | +1160.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1453 | +0.210 | +1160.11€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 4498 | +0.207 | +3441.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 4498 | +0.207 | +3441.42€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 2749 | +0.228 | +2460.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 2749 | +0.228 | +2460.08€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 2018 | +0.209 | +1589.76€ | 0 | 0 |
| ✅ GBM_LATE_60M | 5460 | +0.056 | +1472.07€ | 0 | 5 |
| ✅ GBM_LATE_60M#60min | 5460 | +0.056 | +1472.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1883 | +0.059 | +550.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1883 | +0.059 | +550.11€ | 0 | 6 |
| ✅ GBM_LATE_60M#ETH | 1741 | +0.054 | +541.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1741 | +0.054 | +541.21€ | 1 | 6 |
| ✅ GBM_LATE_60M#SOL | 1836 | +0.053 | +380.74€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1836 | +0.053 | +380.74€ | 0 | 9 |
| 🚫 GBM_LATE_60M_FADE | 726 | -0.250 | -36.05€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 726 | -0.250 | -36.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 262 | -0.254 | -20.04€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 262 | -0.254 | -20.04€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 262 | -0.242 | -6.68€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 262 | -0.242 | -6.68€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 202 | -0.250 | -9.34€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 202 | -0.250 | -9.34€ | 6 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 2241 | +0.085 | +563.97€ | 1 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 2241 | +0.085 | +563.97€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 860 | +0.068 | +191.54€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 860 | +0.068 | +191.54€ | 1 | 4 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 766 | +0.056 | +148.78€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 766 | +0.056 | +148.78€ | 1 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 615 | +0.142 | +223.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 615 | +0.142 | +223.65€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 318 | +0.312 | +382.90€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 318 | +0.312 | +382.90€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 318 | +0.312 | +382.90€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 318 | +0.312 | +382.90€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 4499 | +0.097 | +1017.32€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 4499 | +0.097 | +1017.32€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 4499 | +0.097 | +1017.32€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 4499 | +0.097 | +1017.32€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 1421 | +0.014 | +67.52€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 1421 | +0.014 | +67.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 143 | +0.079 | +26.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 143 | +0.079 | +26.33€ | 0 | 4 |
| ✅ LIQUIDACIONES_15M#BTC | 292 | +0.000 | +10.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 292 | +0.000 | +10.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 94 | +0.010 | +7.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 94 | +0.010 | +7.08€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#ETH | 336 | +0.021 | +19.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 336 | +0.021 | +19.04€ | 2 | 1 |
| ✅ LIQUIDACIONES_15M#SOL | 333 | -0.010 | +3.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 333 | -0.010 | +3.09€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 223 | +0.016 | +1.51€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 223 | +0.016 | +1.51€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M | 4396 | +0.016 | +153.17€ | 5 | 1 |
| ✅ LIQUIDACIONES_5M#5min | 4396 | +0.016 | +153.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 239 | +0.006 | -5.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 829 | +0.016 | +43.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 829 | +0.016 | +43.09€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 295 | +0.049 | +56.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 295 | +0.049 | +56.07€ | 0 | 5 |
| ✅ LIQUIDACIONES_5M#ETH | 1675 | +0.019 | +29.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1675 | +0.019 | +29.76€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 776 | +0.013 | +3.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 776 | +0.013 | +3.99€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 582 | +0.000 | +25.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 582 | +0.000 | +25.40€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 2547 | -0.032 | -4.45€ | 4 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 2547 | -0.032 | -4.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 777 | -0.032 | -12.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 777 | -0.032 | -12.02€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 914 | -0.010 | +20.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 914 | -0.010 | +20.84€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 856 | -0.057 | -13.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 856 | -0.057 | -13.27€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 17965 | -0.032 | -184.93€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 8660 | -0.034 | -111.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 9305 | -0.031 | -73.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 636 | -0.055 | -37.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 325 | -0.035 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 311 | -0.075 | -33.59€ | 4 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 4727 | -0.028 | -43.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 2241 | -0.024 | -2.34€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 2486 | -0.031 | -41.50€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 1706 | -0.030 | +8.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 870 | -0.040 | -17.35€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 836 | -0.020 | +25.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 4073 | -0.031 | -41.26€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 1954 | -0.028 | -5.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 2119 | -0.033 | -35.57€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 3447 | -0.022 | +51.88€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 1673 | -0.029 | +0.90€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 1774 | -0.016 | +50.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 3376 | -0.046 | -122.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 1597 | -0.053 | -82.88€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 1779 | -0.040 | -39.31€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 71738 | +0.000 | +3936.76€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 71738 | +0.000 | +3936.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 13028 | +0.027 | +1820.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 13028 | +0.027 | +1820.95€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 9964 | -0.038 | -144.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 9964 | -0.038 | -144.72€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 13171 | +0.026 | +1497.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 13171 | +0.026 | +1497.56€ | 1 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 9950 | -0.053 | -258.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 9950 | -0.053 | -258.37€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 12239 | -0.004 | +354.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 12239 | -0.004 | +354.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 13386 | +0.019 | +666.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 13386 | +0.019 | +666.48€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 7274 | -0.053 | -111.98€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 7274 | -0.053 | -111.98€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1269 | -0.001 | -13.75€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 2024 | -0.062 | -23.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 2024 | -0.062 | -23.28€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 93 | -0.016 | +0.13€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 813 | -0.118 | -34.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 813 | -0.118 | -34.55€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 2207 | -0.067 | -12.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 2207 | -0.067 | -12.58€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 175912 | -0.077 | +2528.76€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 175912 | -0.077 | +2528.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 30899 | -0.077 | +1843.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 30899 | -0.077 | +1843.45€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 26180 | -0.100 | -1220.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 26180 | -0.100 | -1220.62€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 31348 | -0.067 | +1540.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 31348 | -0.067 | +1540.08€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 25729 | -0.099 | -847.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 25729 | -0.099 | -847.01€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 31418 | -0.059 | +293.81€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 31418 | -0.059 | +293.81€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 30338 | -0.069 | +919.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 30338 | -0.069 | +919.06€ | 5 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 9156 | -0.035 | -178.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 9156 | -0.035 | -178.67€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1008 | -0.017 | -19.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1008 | -0.017 | -19.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 2127 | -0.046 | -27.84€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 2127 | -0.046 | -27.84€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1009 | -0.021 | -31.94€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1009 | -0.021 | -31.94€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2669 | -0.024 | -33.87€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2669 | -0.024 | -33.87€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1281 | -0.063 | -30.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1281 | -0.063 | -30.25€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 1062 | -0.034 | -35.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 1062 | -0.034 | -35.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 2243 | +0.122 | +910.93€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#5min | 2107 | +0.126 | +898.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 495 | +0.138 | +249.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 495 | +0.138 | +249.01€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 437 | +0.120 | +156.83€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 437 | +0.120 | +156.83€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#ETH | 395 | +0.132 | +187.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 395 | +0.132 | +187.99€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#SOL | 355 | +0.139 | +178.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 355 | +0.139 | +178.65€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#XRP | 425 | +0.100 | +125.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 425 | +0.100 | +125.86€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 2337 | -0.021 | -33.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 2337 | -0.021 | -33.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 421 | +0.011 | +23.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 421 | +0.011 | +23.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 433 | -0.049 | -30.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 433 | -0.049 | -30.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 576 | -0.045 | -39.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 576 | -0.045 | -39.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 473 | +0.003 | +7.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 473 | +0.003 | +7.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 434 | -0.016 | +5.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 434 | -0.016 | +5.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 1228 | -0.052 | +65.56€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 570 | -0.086 | -18.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 441 | -0.087 | +5.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 129 | -0.080 | -23.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 430 | -0.016 | +54.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 309 | +0.005 | +63.47€ | 1 | 2 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 121 | -0.069 | -8.75€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 228 | -0.035 | +29.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 192 | -0.026 | +27.55€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 36 | -0.079 | +1.84€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 942 | -0.044 | +96.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 286 | -0.076 | -30.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 1546 | -0.194 | -57.75€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 606 | -0.186 | -23.88€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 535 | -0.183 | -19.98€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 71 | -0.199 | -3.91€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 517 | -0.203 | -36.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 454 | -0.213 | -42.69€ | 4 | 1 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 63 | -0.131 | +6.63€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 423 | -0.194 | +2.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 392 | -0.190 | +0.56€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 31 | -0.227 | +1.64€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 1381 | -0.196 | -62.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 165 | -0.183 | +4.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 565 | +0.377 | +517.90€ | 0 | 11 |
| ✅ RESOLUTION_SNIPER#BTC | 122 | +0.161 | +95.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 122 | +0.161 | +95.11€ | 0 | 7 |
| ✅ RESOLUTION_SNIPER#ETH | 130 | +0.371 | +107.64€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 130 | +0.371 | +107.64€ | 0 | 5 |
| ✅ RESOLUTION_SNIPER#SOL | 313 | +0.459 | +315.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 313 | +0.459 | +315.15€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 565 | +0.377 | +517.90€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 993 | +0.038 | +80.38€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 993 | +0.038 | +80.38€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 359 | +0.015 | +2.34€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 76 | +0.013 | +0.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 76 | +0.013 | +0.02€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 84 | +0.023 | +7.13€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 84 | +0.023 | +7.13€ | 2 | 1 |
| ✅ STREAK_FADE_15M#XRP | 474 | +0.061 | +70.90€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 474 | +0.061 | +70.90€ | 1 | 4 |
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
| ✅ STREAK_MOM_5M | 11585 | +0.014 | +70.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 11585 | +0.014 | +70.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2995 | +0.018 | +24.38€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 3062 | +0.015 | +29.72€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 3062 | +0.015 | +29.72€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2935 | +0.008 | -3.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2935 | +0.008 | -3.04€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2593 | +0.014 | +19.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2593 | +0.014 | +19.31€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 12617 | +0.018 | -2.88€ | 4 | 0 |
| ✅ STRUCT_NO_15M#15min | 12617 | +0.018 | -2.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 5179 | +0.020 | +2.18€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 5179 | +0.020 | +2.18€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 4417 | +0.018 | -2.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 4417 | +0.018 | -2.55€ | 4 | 0 |
| ✅ STRUCT_NO_15M#SOL | 3021 | +0.014 | -2.51€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 3021 | +0.014 | -2.51€ | 1 | 0 |
| ✅ UPDOWN_GBM | 114913 | +0.060 | +10880.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 27995 | +0.078 | +5522.78€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 3321 | -0.001 | +35.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 76364 | +0.062 | +5209.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 6847 | -0.002 | +123.09€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 9946 | +0.102 | +1761.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1782 | +0.163 | +818.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 90 | -0.011 | -2.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 8074 | +0.089 | +944.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 26044 | +0.057 | +2319.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 3775 | +0.080 | +849.15€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 960 | -0.001 | +19.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 18123 | +0.067 | +1371.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 3046 | -0.005 | +77.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 140 | -0.070 | +2.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 12595 | +0.075 | +1360.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1763 | +0.154 | +737.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 86 | +0.023 | -0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 10746 | +0.062 | +623.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 27046 | +0.050 | +1918.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 6605 | +0.072 | +1022.02€ | 0 | 8 |
| ✅ UPDOWN_GBM#ETH#240min | 928 | +0.005 | +15.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 16852 | +0.052 | +840.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 2532 | +0.000 | +40.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 129 | -0.111 | -0.02€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 24160 | +0.041 | +1379.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 7605 | +0.033 | +459.50€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#240min | 860 | -0.010 | +5.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 14311 | +0.053 | +920.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 1269 | +0.001 | +5.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 115 | -0.150 | -10.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 15120 | +0.073 | +2142.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 6465 | +0.092 | +1635.57€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 397 | +0.006 | -1.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 8258 | +0.062 | +508.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 384 | -0.109 | -8.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 1020 | +0.365 | +380.98€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 1020 | +0.365 | +380.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 492 | +0.362 | +172.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 492 | +0.362 | +172.46€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 528 | +0.366 | +208.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 528 | +0.366 | +208.53€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 26949 | -0.019 | +6717.14€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 26949 | -0.019 | +6717.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1981 | -0.051 | +561.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 5028 | -0.115 | +274.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 5028 | -0.115 | +274.46€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 1072 | +0.223 | +901.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 1072 | +0.223 | +901.85€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 3610 | +0.220 | +2314.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 3610 | +0.220 | +2314.47€ | 1 | 19 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 7687 | -0.057 | +1146.02€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 7687 | -0.057 | +1146.02€ | 4 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 7571 | -0.056 | +1519.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 7571 | -0.056 | +1519.19€ | 4 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 339 | +0.060 | +34.14€ | 0 | 9 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 339 | +0.060 | +34.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 339 | +0.060 | +34.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 339 | +0.060 | +34.14€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1879 | +0.282 | +1587.34€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1879 | +0.282 | +1587.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 992 | +0.276 | +788.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 992 | +0.276 | +788.89€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 887 | +0.288 | +798.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 887 | +0.288 | +798.45€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 878 | -0.115 | -88.77€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 878 | -0.115 | -88.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 278 | -0.079 | -20.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 278 | -0.079 | -20.43€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 101 | -0.189 | -14.00€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 101 | -0.189 | -14.00€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 116 | -0.178 | -4.99€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 116 | -0.178 | -4.99€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 2 | 0 |
| ✅ WEEKLY_PRICE | 4988 | +0.297 | +2211.10€ | 0 | 3 |
| ✅ WEEKLY_PRICE#BTC | 1922 | +0.252 | +250.69€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 1929 | +0.291 | +816.22€ | 0 | 3 |
| ✅ WEEKLY_PRICE#SOL | 1137 | +0.382 | +1144.18€ | 0 | 1 |