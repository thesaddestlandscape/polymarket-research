# Hipótesis automáticas — 2026-10-17 18:07 UTC
_Generado por shadow_postmortem.py sobre 940887 resoluciones (PNL=+121478.72€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.261 (n=178)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=608)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.240 (n=749)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.137)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.187 (n=273)

  - _Acción_: Kelly boost +0.94€ cuando `n_total_lado` > 66.0 (IC base=+0.137)

- **PATRÓN** `banda_hit_calibrado` > `0.8012` → IC=+0.274 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8012 (IC base=+0.137)

- **PATRÓN** `banda_z` > `9.381` → IC=+0.195 (n=267)

  - _Acción_: Kelly boost +0.98€ cuando `banda_z` > 9.381 (IC base=+0.137)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.727` → IC=+0.137 (n=716)

  - _Acción_: Kelly boost +0.68€ cuando `ballenas_wallet_edge_medio` > 0.727 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.140 (n=534)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 11.0 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=867)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.137)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.152 (n=429)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 98.0 (IC base=+0.137)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.275 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.55 (IC base=+0.143)

- **PATRÓN** `n_total_lado` > `47.0` → IC=+0.183 (n=449)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 47.0 (IC base=+0.143)

- **PATRÓN** `banda_hit_calibrado` > `0.6183` → IC=+0.268 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6183 (IC base=+0.143)

- **PATRÓN** `banda_z` > `9.782` → IC=+0.224 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.782 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=235)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=768)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `101.0` → IC=+0.151 (n=396)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 101.0 (IC base=+0.143)

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
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=104)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=103)

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
- **PATRÓN** `n_ballena_banda` > `25.0` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `n_ballena_banda` > 25.0 (IC base=+0.141)

- **PATRÓN** `n_total_lado` > `38.0` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 38.0 (IC base=+0.141)

- **PATRÓN** `banda_z` > `2.495` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 2.495 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `2518.5859` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2518.5859 (IC base=+0.141)

### BALLENAS_TARDIAS
- **FILTRO** `restante_s_al_confirmar` < `143.13` → IC=-0.204 (n=9766)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.13
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=29299)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `130.45` → IC=-0.265 (n=1109)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 130.45
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=3328)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.61` → IC=-0.288 (n=1070)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.61
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3213)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.83` → IC=-0.206 (n=2560)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.83
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=7680)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.32` → IC=-0.283 (n=1899)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.32
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=5697)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.211 (n=20817)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=4231)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `9216.4419` → IC=+0.179 (n=1903)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9216.4419 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=17571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=21381)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=16370)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=7041)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7182.7035` → IC=+0.160 (n=2719)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7182.7035 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=2000)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=1959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2454)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `16325.2152` → IC=+0.204 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16325.2152 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.192 (n=1757)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 7.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.190 (n=1964)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.186)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=2514)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `16122.9185` → IC=+0.197 (n=648)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16122.9185 (IC base=+0.186)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.166 (n=456)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `6860.5651` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6860.5651 (IC base=+0.079)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.140 (n=1082)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.089)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=4052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.160 (n=2765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 12.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.223 (n=1795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.360 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.218 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1014)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=868)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.262 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.139 (n=793)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `1861.9688` → IC=+0.147 (n=646)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1861.9688 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4449.086` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4449.086 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.411 (n=1159)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1280)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=673)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=848)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.173 (n=337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 7.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.350 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3371.7925` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3371.7925 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.251 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.127)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=17530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=14901)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=7254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=4055)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.179 (n=3842)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3940)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.177 (n=1584)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.73 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=2008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.232 (n=1335)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.310 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.224)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=3987)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.185 (n=3397)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=3131)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3470)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.353 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.248)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=3910)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2501)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.196 (n=1341)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` > 0.73 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.431 (n=751)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.427)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.427)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.427)

- **PATRÓN** `libro_liquidez` > `12834.5263` → IC=+0.444 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12834.5263 (IC base=+0.427)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.450 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.436)

- **PATRÓN** `libro_liquidez` > `11667.7741` → IC=+0.447 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11667.7741 (IC base=+0.436)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.446 (n=203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `4387.5246` → IC=+0.439 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4387.5246 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.407 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.400)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.398 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.400)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.414 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.400)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.77` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.77
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=22591)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=22917)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=9028)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=10146)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=9567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=4657)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.284 (n=3321)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=3868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.209 (n=5184)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.179)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.230 (n=4767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=3634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.277 (n=3233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=8713)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.260 (n=3381)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3752)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.198 (n=3809)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=3947)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=8212)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=8092)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.41` → IC=+0.137 (n=7507)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.41 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=4068)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=4103)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=4942)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.79` → IC=+0.145 (n=3730)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.79 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=4144)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=4417)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.26` → IC=+0.135 (n=3793)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.26 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1596)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.291 (n=1348)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.377 (n=551)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.290)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=723)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.280 (n=624)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.349 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `5415.9223` → IC=+0.289 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5415.9223 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.298 (n=761)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.294)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.294)

- **PATRÓN** `libro_liquidez` > `2100.1274` → IC=+0.308 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2100.1274 (IC base=+0.294)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.440 (n=615)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=837)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=354)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.436)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.442 (n=239)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.436)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.436)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.442 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.436)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.451 (n=348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.447)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.448 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.447)

- **PATRÓN** `libro_liquidez` > `2142.5668` → IC=+0.455 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2142.5668 (IC base=+0.447)

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
- **FILTRO** `hora_utc` < `5.0` → IC=-0.283 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=92)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.340 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=90)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

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
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=92)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.340 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=90)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.250 (n=58)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=55)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4779` → IC=+0.135 (n=12677)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.4779 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.120 (n=13286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 18.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.245 (n=4229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.7954` → IC=+0.266 (n=717)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7954 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.3728` → IC=+0.255 (n=3493)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3728 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.937` → IC=+0.188 (n=4791)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.937 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2041` → IC=+0.254 (n=3646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2041 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.6193` → IC=+0.261 (n=3646)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6193 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.302` → IC=+0.235 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.302 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.3398` → IC=+0.226 (n=4075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3398 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=10778)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5667` → IC=+0.141 (n=15670)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5667 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1544` → IC=+0.185 (n=5685)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1544 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `1.1914` → IC=+0.179 (n=6064)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.1914 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0507` → IC=+0.179 (n=2749)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0507 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2948` → IC=+0.229 (n=1512)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2948 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.676` → IC=+0.205 (n=3437)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.676 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `108.0` → IC=+0.219 (n=10159)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 108.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.213 (n=926)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.3473` → IC=+0.199 (n=2768)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.3473 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=1337)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.200 (n=1856)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` > `0.9773` → IC=+0.277 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9773 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.021` → IC=+0.282 (n=1208)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.021 (IC base=+0.194)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.245 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.194)

- **PATRÓN** `volumen_spike_ratio` > `2.2768` → IC=+0.208 (n=1194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2768 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.208 (n=2935)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `2088.2932` → IC=+0.212 (n=923)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2088.2932 (IC base=+0.194)

- **PATRÓN** `ballena_activa_n` < `15.0` → IC=+0.208 (n=1686)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 15.0 (IC base=+0.194)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.239 (n=2325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.239 (n=1053)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.236)

- **PATRÓN** `drift_60min` |x|≤ `0.0878` → IC=+0.267 (n=775)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0878 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=846)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.236)

- **PATRÓN** `ibs_20min` < `0.5193` → IC=+0.257 (n=2323)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5193 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` < `0.0937` → IC=+0.239 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0937 (IC base=+0.236)

- **PATRÓN** `volumen_pendiente_norm` > `0.2849` → IC=+0.246 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2849 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` < `1.437` → IC=+0.240 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.437 (IC base=+0.236)

- **PATRÓN** `volumen_spike_ratio` > `2.6424` → IC=+0.241 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6424 (IC base=+0.236)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.239 (n=2590)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `1561.8016` → IC=+0.243 (n=2322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1561.8016 (IC base=+0.236)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.241 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.236)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.240 (n=998)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.226 (n=1025)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1069` → IC=+0.258 (n=993)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1069 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.236 (n=2257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.957` → IC=+0.274 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.957 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.233 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.3427` → IC=+0.226 (n=2171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3427 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.408` → IC=+0.265 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.408 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `1.2317` → IC=+0.227 (n=2257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2317 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6213` → IC=+0.230 (n=2257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6213 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.255 (n=316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.5126` → IC=+0.227 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5126 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.4308` → IC=+0.255 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4308 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.151 (n=2316)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0752` → IC=+0.169 (n=772)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.0752 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7291` → IC=+0.176 (n=2316)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7291 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1329` → IC=+0.155 (n=2157)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1329 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.077` → IC=+0.151 (n=376)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 11.077 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.213` → IC=+0.141 (n=2117)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.213 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.199` → IC=+0.141 (n=2316)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.199 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0963` → IC=+0.161 (n=847)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0963 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4537` → IC=+0.142 (n=2197)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4537 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.415` → IC=+0.137 (n=2196)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.415 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `219.0` → IC=+0.171 (n=937)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 219.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.216 (n=958)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=3018)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.195 (n=2579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=1096)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.305` → IC=+0.269 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.305 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.197 (n=2538)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.211 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.6928` → IC=+0.210 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6928 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=3416)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1853.821` → IC=+0.200 (n=1916)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1853.821 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.223 (n=2263)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.606` → IC=+0.221 (n=2570)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.606 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.246 (n=959)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.011` → IC=+0.274 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.011 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.457` → IC=+0.247 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.457 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.257 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` < `1.7265` → IC=+0.216 (n=1072)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7265 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7268` → IC=+0.227 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7268 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2063.3256` → IC=+0.229 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2063.3256 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.219 (n=2105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=145)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=3484)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.160 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0036 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.9556` → IC=+0.226 (n=512)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9556 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1359` → IC=+0.324 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1359 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.7574` → IC=+0.330 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7574 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.087` → IC=+0.186 (n=1100)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.087 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.333 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.349 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2251 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.3004` → IC=+0.341 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3004 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `1.4081` → IC=+0.339 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4081 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` > `2.2467` → IC=+0.321 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2467 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.333 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0952` → IC=+0.168 (n=908)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0952 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.3254` → IC=+0.140 (n=443)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.3254 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1308` → IC=+0.134 (n=1452)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1308 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8486` → IC=+0.145 (n=1061)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8486 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.194 (n=207)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `2.1545` → IC=+0.151 (n=691)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1545 (IC base=+0.034)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.163 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=527)

- **FILTRO** `ibs_20min` < `0.2759` → IC=-0.205 (n=154)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2759
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=469)

- **FILTRO** `ibs_20min` > `0.2187` → IC=-0.131 (n=3427)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2187
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=1689)

- **FILTRO** `sigma_ewma_delta_pct` > `8.659` → IC=-0.236 (n=535)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.659
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=4581)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.182 (n=212)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.7857 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `1.0167` → IC=+0.270 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0167 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.6239` → IC=+0.257 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6239 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.1` → IC=+0.150 (n=198)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 3.1 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `0.992` → IC=+0.297 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.992 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.0778` → IC=+0.277 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0778 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.1989` → IC=+0.278 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1989 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.2187` → IC=+0.150 (n=1689)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2187 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` > `0.1923` → IC=+0.276 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1923 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.4351` → IC=+0.274 (n=776)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4351 (IC base=-0.038)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.303 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=-0.038)

- **PATRÓN** `volumen_pendiente_norm` > `0.0801` → IC=+0.300 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0801 (IC base=-0.038)

- **PATRÓN** `volumen_spike_ratio` < `2.4034` → IC=+0.302 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4034 (IC base=-0.038)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6214` → IC=-0.178 (n=924)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6214
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2775)

- **FILTRO** `ibs_20min` < `0.7394` → IC=-0.149 (n=2441)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7394
  - _Potencial_: sin este filtro IC_bueno=+0.085 (n=1258)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.165 (n=928)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2771)

- **FILTRO** `ibs_20min` > `0.7527` → IC=-0.204 (n=1345)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7527
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4036)

- **PATRÓN** `dist_vwap_pct` > `0.7478` → IC=+0.330 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7478 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2585` → IC=+0.298 (n=529)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2585 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.7077` → IC=+0.312 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7077 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1011` → IC=+0.299 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1011 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4138` → IC=+0.318 (n=201)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4138 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8402` → IC=+0.296 (n=401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8402 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.8152` → IC=+0.272 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8152 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0704` → IC=+0.280 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0704 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1026` → IC=+0.277 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1026 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1803` → IC=+0.261 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1803 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4259` → IC=+0.261 (n=1341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4259 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.205 (n=5577)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.3243` → IC=+0.168 (n=16719)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3243 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.967` → IC=+0.299 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.967 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.623` → IC=+0.159 (n=7495)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.623 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1724` → IC=+0.259 (n=6141)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1724 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6892` → IC=+0.265 (n=5486)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6892 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.273 (n=1830)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4596` → IC=+0.257 (n=3276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4596 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6368` → IC=+0.267 (n=3275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6368 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.291 (n=9401)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.162 (n=5379)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0092 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.6605` → IC=+0.145 (n=16126)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6605 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2425` → IC=+0.261 (n=5023)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2425 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1945` → IC=+0.264 (n=1693)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1945 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2934` → IC=+0.315 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2934 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.5781` → IC=+0.286 (n=3189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5781 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2631` → IC=+0.281 (n=3282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2631 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.291 (n=7159)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3699` → IC=-0.173 (n=1523)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3699
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=3093)

- **FILTRO** `ibs_20min` > `0.7455` → IC=-0.209 (n=962)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7455
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=2890)

- **FILTRO** `sigma_ewma_delta_pct` > `4.492` → IC=-0.203 (n=844)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.492
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=3008)

- **PATRÓN** `ibs_20min` > `0.9142` → IC=+0.303 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9142 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.052` → IC=+0.212 (n=817)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.052 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.295 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.4454` → IC=+0.238 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4454 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.268 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.270 (n=1014)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.030)

- **PATRÓN** `ibs_20min` < `0.1605` → IC=+0.162 (n=964)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1605 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.0738` → IC=+0.413 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0738 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.4877` → IC=+0.403 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4877 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.397 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1138` → IC=+0.210 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1138 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.195` → IC=+0.186 (n=1620)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.195 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6813` → IC=+0.195 (n=1447)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.6813 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.217 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4254` → IC=+0.212 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4254 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.4515` → IC=+0.191 (n=532)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4515 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.237 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 220.0 (IC base=+0.023)

- **PATRÓN** `dist_vwap_pct` < `0.1131` → IC=+0.231 (n=1043)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1131 (IC base=+0.000)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.234 (n=1041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=+0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.2721` → IC=+0.289 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2721 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.5351` → IC=+0.233 (n=436)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5351 (IC base=+0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1651` → IC=+0.249 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1651 (IC base=+0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.305 (n=818)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.263)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.269 (n=2578)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=1287)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.263)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.714` → IC=+0.294 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.714 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.275 (n=2126)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.270 (n=2367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.274 (n=2901)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `1979.26` → IC=+0.284 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.26 (IC base=+0.263)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.328 (n=957)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.1822` → IC=+0.307 (n=929)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1822 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.320 (n=810)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.3689` → IC=+0.293 (n=2112)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3689 (IC base=+0.291)

- **PATRÓN** `ibs_20min` > `0.2564` → IC=+0.298 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2564 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.641` → IC=+0.314 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.641 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.1969` → IC=+0.289 (n=2057)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1969 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.3404` → IC=+0.309 (n=334)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3404 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.7249` → IC=+0.300 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7249 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `2.6617` → IC=+0.301 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6617 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2058.44` → IC=+0.313 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2058.44 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.288 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.291)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7385` → IC=-0.183 (n=1004)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7385
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=3020)

- **PATRÓN** `ibs_20min` > `0.8815` → IC=+0.168 (n=946)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.8815 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1518` → IC=+0.230 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1518 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3676` → IC=+0.230 (n=1269)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3676 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0122` → IC=+0.243 (n=1154)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0122 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6697` → IC=+0.227 (n=1172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6697 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1031` → IC=+0.251 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1031 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.3975` → IC=+0.248 (n=423)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3975 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `105.0` → IC=+0.264 (n=1132)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 105.0 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3327` → IC=+0.228 (n=986)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3327 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.0392` → IC=+0.234 (n=798)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0392 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1036` → IC=+0.244 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1036 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.292 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.264 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7982 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4337` → IC=+0.254 (n=286)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4337 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.254 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.76` → IC=-0.210 (n=1762)

  - _Acción_: SKIP cuando `ibs_20min` < 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.302 (n=1768)

- **FILTRO** `ibs_20min` > `0.65` → IC=-0.236 (n=868)

  - _Acción_: SKIP cuando `ibs_20min` > 0.65
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=2607)

- **FILTRO** `sigma_ewma_delta_pct` > `8.538` → IC=-0.237 (n=398)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.538
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=3077)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.302 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.76 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.336 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.605` → IC=+0.176 (n=553)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.605 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8456` → IC=+0.331 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8456 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.628` → IC=+0.319 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.628 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1588` → IC=+0.318 (n=1375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1588 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.357 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4413` → IC=+0.343 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4413 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.335 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.5484` → IC=+0.143 (n=2294)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5484 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.4629` → IC=+0.248 (n=1215)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4629 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.262 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.2193` → IC=+0.241 (n=1274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2193 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0756` → IC=+0.255 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0756 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4125` → IC=+0.251 (n=1087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4125 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.268 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.031)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.343 (n=1683)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.312 (n=903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.298)

- **PATRÓN** `ibs_20min` > `0.6516` → IC=+0.330 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6516 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.2098` → IC=+0.326 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2098 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.778` → IC=+0.319 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.778 (IC base=+0.298)

- **PATRÓN** `volumen_regimen` > `0.6275` → IC=+0.308 (n=1884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6275 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.340 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` > `1.4244` → IC=+0.309 (n=1804)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4244 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `2650.804` → IC=+0.315 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2650.804 (IC base=+0.298)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.332 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.298)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.332 (n=1335)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.300)

- **PATRÓN** `drift_60min` |x|≤ `0.1879` → IC=+0.304 (n=880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1879 (IC base=+0.300)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.311 (n=777)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.300)

- **PATRÓN** `ibs_20min` < `0.37` → IC=+0.325 (n=2000)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.37 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.541` → IC=+0.313 (n=743)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.541 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.078` → IC=+0.301 (n=2376)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.078 (IC base=+0.300)

- **PATRÓN** `volumen_regimen` < `0.7188` → IC=+0.305 (n=880)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7188 (IC base=+0.300)

- **PATRÓN** `volumen_regimen` > `1.224` → IC=+0.330 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.224 (IC base=+0.300)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.352 (n=275)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.308 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` > `2.1346` → IC=+0.304 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1346 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `2420.4144` → IC=+0.303 (n=1786)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2420.4144 (IC base=+0.300)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.183 (n=4106)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0048 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.223 (n=4104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0865` → IC=+0.201 (n=4096)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0865 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=12778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5588` → IC=+0.233 (n=12288)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5588 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1656` → IC=+0.208 (n=5043)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1656 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.309` → IC=+0.257 (n=2422)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.309 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1915` → IC=+0.168 (n=8150)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1915 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.6265` → IC=+0.163 (n=8148)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6265 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.203 (n=1792)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6026` → IC=+0.189 (n=3968)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6026 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2001.581` → IC=+0.183 (n=10976)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2001.581 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.196 (n=11199)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 96.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.186 (n=7941)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0069 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.08` → IC=+0.224 (n=3970)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.08 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=4457)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.235 (n=11948)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` < `0.1751` → IC=+0.174 (n=8425)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1751 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.062` → IC=+0.196 (n=1951)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.062 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.71` → IC=+0.179 (n=10472)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 2.71 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.163 (n=8494)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1817 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2926` → IC=+0.225 (n=1755)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2926 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.6297` → IC=+0.186 (n=3719)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6297 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.196 (n=9601)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 66.0 (IC base=+0.178)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.233 (n=690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.3312` → IC=+0.228 (n=2056)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3312 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=2159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.220 (n=1389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` > `0.9263` → IC=+0.291 (n=1372)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9263 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.053` → IC=+0.332 (n=645)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.053 (IC base=+0.210)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.269 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` < `1.8383` → IC=+0.204 (n=1294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8383 (IC base=+0.210)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.210 (n=1941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.210)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.222 (n=2200)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `2014.24` → IC=+0.216 (n=932)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2014.24 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.247 (n=1615)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.246)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.255 (n=733)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.246)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.299 (n=711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.250 (n=1648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=786)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` < `0.0125` → IC=+0.292 (n=711)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0125 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` < `0.0996` → IC=+0.248 (n=1407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0996 (IC base=+0.246)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.280 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` < `1.4284` → IC=+0.265 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4284 (IC base=+0.246)

- **PATRÓN** `volumen_spike_ratio` > `2.6589` → IC=+0.246 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6589 (IC base=+0.246)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.251 (n=1807)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.246)

- **PATRÓN** `libro_liquidez` > `1549.0376` → IC=+0.257 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1549.0376 (IC base=+0.246)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.250 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.246)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.217 (n=616)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1604` → IC=+0.183 (n=1232)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1604 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.171 (n=1952)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.343` → IC=+0.224 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.343 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.217 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.433` → IC=+0.222 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.433 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6893` → IC=+0.166 (n=813)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.6893 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.185 (n=293)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.413` → IC=+0.178 (n=604)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.413 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.4944` → IC=+0.160 (n=603)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.4944 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `423.0` → IC=+0.159 (n=1770)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 423.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.170 (n=1955)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.2346` → IC=+0.173 (n=1719)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2346 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.204 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.545` → IC=+0.199 (n=373)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.545 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `1.2065` → IC=+0.161 (n=1954)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2065 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.0933` → IC=+0.147 (n=1645)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0933 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1584` → IC=+0.147 (n=602)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.1584 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `2.4989` → IC=+0.151 (n=1834)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4989 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `1.4225` → IC=+0.147 (n=1833)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4225 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `203.0` → IC=+0.175 (n=588)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 203.0 (IC base=+0.145)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.233 (n=945)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.212)

- **PATRÓN** `drift_60min` |x|≤ `0.3945` → IC=+0.225 (n=1833)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3945 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=750)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.212)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.212)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.477` → IC=+0.296 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.477 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.211 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.212)

- **PATRÓN** `volumen_pendiente_norm` > `0.353` → IC=+0.227 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.353 (IC base=+0.212)

- **PATRÓN** `volumen_spike_ratio` > `2.7073` → IC=+0.229 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7073 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=2472)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1978.5409` → IC=+0.223 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.5409 (IC base=+0.212)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.246 (n=1578)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1424` → IC=+0.270 (n=789)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1424 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.279 (n=687)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0025` → IC=+0.298 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0025 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.541` → IC=+0.276 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.541 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3531` → IC=+0.277 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3531 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7398` → IC=+0.235 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7398 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.151` → IC=+0.237 (n=1139)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.151 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2057.52` → IC=+0.245 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2057.52 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.230 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.173 (n=1993)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0074 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4058` → IC=+0.166 (n=1993)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4058 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2074)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3118` → IC=+0.212 (n=1993)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3118 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1413` → IC=+0.199 (n=1232)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1413 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.843` → IC=+0.203 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.843 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.0327` → IC=+0.156 (n=1753)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0327 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.179 (n=820)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.5368` → IC=+0.152 (n=860)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5368 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.5068` → IC=+0.164 (n=652)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.5068 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `4737.5945` → IC=+0.190 (n=1328)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 4737.5945 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.158 (n=1932)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 142.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.154 (n=2108)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3953` → IC=+0.144 (n=2107)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3953 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.165 (n=1005)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6846` → IC=+0.186 (n=2107)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6846 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1546` → IC=+0.154 (n=2099)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1546 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.636` → IC=+0.158 (n=518)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.636 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.157 (n=1405)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8585 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2983` → IC=+0.200 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2983 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.8074` → IC=+0.134 (n=1314)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.8074 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4213` → IC=+0.128 (n=1970)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4213 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7721.7079` → IC=+0.188 (n=955)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7721.7079 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `117.0` → IC=+0.131 (n=1690)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 117.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.174 (n=1018)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0103 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4388` → IC=+0.129 (n=1972)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4388 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.4872` → IC=+0.215 (n=2241)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4872 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.195` → IC=+0.190 (n=1320)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.195 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.65` → IC=+0.272 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.65 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1795` → IC=+0.142 (n=2241)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1795 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.135 (n=2273)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4364` → IC=+0.148 (n=725)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 1.4364 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2835.7653` → IC=+0.210 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2835.7653 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.160 (n=701)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 20.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.136 (n=2307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0108 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.170 (n=770)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2340)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.217 (n=2311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.2001` → IC=+0.147 (n=2168)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2001 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.418` → IC=+0.124 (n=464)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 7.418 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.475` → IC=+0.128 (n=2036)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 2.475 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.129 (n=2307)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.1753 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` < `0.1651` → IC=+0.122 (n=2223)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` < 0.1651 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.151 (n=305)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4475` → IC=+0.129 (n=715)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4475 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4248` → IC=+0.136 (n=715)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4248 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2673.3847` → IC=+0.189 (n=1046)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 2673.3847 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.128 (n=1849)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 42.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.245 (n=1849)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1748` → IC=+0.236 (n=911)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1748 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.223 (n=2150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.228 (n=1402)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.6591` → IC=+0.256 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6591 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1888` → IC=+0.225 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1888 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.4877` → IC=+0.222 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4877 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.251 (n=938)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.179` → IC=+0.224 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.179 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.228 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6199 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2306` → IC=+0.263 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2306 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `2.4628` → IC=+0.226 (n=2015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4628 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.8021` → IC=+0.229 (n=1343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8021 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2637.7402` → IC=+0.229 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2637.7402 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.237 (n=937)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.239 (n=966)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.260 (n=710)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.246 (n=1042)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` < `0.4256` → IC=+0.255 (n=2130)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4256 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.2966` → IC=+0.233 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2966 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.326` → IC=+0.252 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.326 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6412` → IC=+0.235 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6412 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2777` → IC=+0.284 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2777 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4374` → IC=+0.230 (n=1977)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4374 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2752)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2384.9953` → IC=+0.229 (n=1903)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2384.9953 (IC base=+0.227)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.208 (n=1378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.192 (n=1042)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0088 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1295` → IC=+0.200 (n=1377)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1295 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.214 (n=1538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.180)

- **PATRÓN** `ibs_20min` > `0.7295` → IC=+0.232 (n=2084)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7295 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.7903` → IC=+0.201 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7903 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.673` → IC=+0.209 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.673 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` < `0.8641` → IC=+0.200 (n=1869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8641 (IC base=+0.180)

- **PATRÓN** `volumen_regimen` > `0.6975` → IC=+0.183 (n=2504)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6975 (IC base=+0.180)

- **PATRÓN** `volumen_pendiente_norm` > `0.1` → IC=+0.192 (n=1131)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` < `1.4337` → IC=+0.197 (n=1013)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4337 (IC base=+0.180)

- **PATRÓN** `volumen_spike_ratio` > `2.5109` → IC=+0.188 (n=1013)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.5109 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=3538)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `2730.6299` → IC=+0.186 (n=2792)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2730.6299 (IC base=+0.180)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.192 (n=2907)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 150.0 (IC base=+0.180)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.136 (n=1113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0037 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.3784` → IC=+0.163 (n=2228)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3784 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.131 (n=1075)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 19.0 (IC base=+0.091)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.213 (n=388)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3265` → IC=+0.194 (n=880)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3265 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.199 (n=795)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.9273` → IC=+0.229 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9273 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.3033` → IC=+0.191 (n=276)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.3033 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.092` → IC=+0.190 (n=375)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.092 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.822` → IC=+0.173 (n=933)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.822 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.198 (n=587)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8753 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` < `0.0916` → IC=+0.172 (n=846)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` < 0.0916 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.071` → IC=+0.176 (n=347)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.071 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.2069` → IC=+0.183 (n=758)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.2069 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.414` → IC=+0.172 (n=861)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.414 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `14802.2575` → IC=+0.185 (n=586)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14802.2575 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.201 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 157.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.141 (n=1045)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0056 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.3447` → IC=+0.138 (n=1044)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3447 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.127 (n=934)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 7.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6382` → IC=+0.167 (n=918)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6382 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.74` → IC=+0.128 (n=202)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 8.74 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `1.0613` → IC=+0.148 (n=473)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` > 1.0613 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.166 (n=276)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.1142` → IC=+0.132 (n=907)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.1142 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `308.0` → IC=+0.146 (n=891)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 308.0 (IC base=+0.118)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.252 (n=638)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0946` → IC=+0.244 (n=319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0946 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=1007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.6866` → IC=+0.276 (n=637)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6866 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.3577` → IC=+0.226 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3577 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2053` → IC=+0.220 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2053 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.948` → IC=+0.240 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.948 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8389` → IC=+0.222 (n=639)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8389 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.1774` → IC=+0.232 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1774 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.1565` → IC=+0.244 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1565 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.254 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.4553` → IC=+0.235 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4553 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.1051` → IC=+0.166 (n=324)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1051 (IC base=+0.065)

- **PATRÓN** `libro_liquidez` > `6887.3567` → IC=+0.133 (n=646)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 6887.3567 (IC base=+0.065)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.178 (n=256)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0108 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.5317` → IC=+0.163 (n=769)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.5317 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.215 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.273 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.9964` → IC=+0.236 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9964 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.204` → IC=+0.230 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.204 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.0551` → IC=+0.180 (n=676)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.0551 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `0.7217` → IC=+0.168 (n=687)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.7217 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1635` → IC=+0.191 (n=218)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1635 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.4569` → IC=+0.167 (n=247)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4569 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.1801` → IC=+0.177 (n=336)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 2.1801 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.167 (n=793)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3060.1971` → IC=+0.194 (n=256)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 3060.1971 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.6591` → IC=+0.124 (n=803)

  - _Acción_: Kelly boost +0.62€ cuando `ibs_20min` < 0.6591 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `2750.9096` → IC=+0.156 (n=364)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2750.9096 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.127 (n=516)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 21.0 (IC base=+0.060)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0234` → IC=+0.160 (n=201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0234 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.186 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.007 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.3919` → IC=+0.165 (n=177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3919 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.192 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.185 (n=179)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.56 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.2178` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.2178 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `1.0805` → IC=+0.159 (n=224)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 1.0805 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.317` → IC=+0.182 (n=171)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.317 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` > `0.635` → IC=+0.170 (n=201)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.635 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.2526` → IC=+0.175 (n=198)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` < 0.2526 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1897` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1897 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.4605` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4605 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.6132` → IC=+0.189 (n=59)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6132 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=201)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `2495.898` → IC=+0.169 (n=134)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2495.898 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.159 (n=206)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.012 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.138 (n=230)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` < 0.61 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `1.1213` → IC=+0.269 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1213 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.151 (n=61)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `0.8919` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` < 0.8919 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `1.0624` → IC=+0.126 (n=105)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` > 1.0624 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1158` → IC=+0.130 (n=209)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1158 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.144 (n=189)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 17.0 (IC base=+0.120)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.182 (n=5349)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0047 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.225 (n=5344)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=16710)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.229 (n=16019)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4483 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9067` → IC=+0.211 (n=2001)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9067 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.311` → IC=+0.253 (n=3921)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.311 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.169 (n=10738)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.2227 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.206 (n=2131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6075` → IC=+0.196 (n=5189)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6075 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1819.3955` → IC=+0.185 (n=16018)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1819.3955 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `114.0` → IC=+0.202 (n=14643)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 114.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.193 (n=9741)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0073 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3808` → IC=+0.191 (n=12858)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.3808 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=5444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.5806` → IC=+0.241 (n=14611)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5806 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.1767` → IC=+0.171 (n=8876)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1767 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.87` → IC=+0.206 (n=2026)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.87 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.609` → IC=+0.190 (n=14109)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.609 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6341` → IC=+0.161 (n=3289)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.6341 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2897` → IC=+0.252 (n=1968)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2897 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.2561` → IC=+0.197 (n=6254)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2561 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.215 (n=9136)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.238 (n=872)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.221)

- **PATRÓN** `drift_60min` |x|≤ `0.3482` → IC=+0.224 (n=2615)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3482 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=1260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.225 (n=1763)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.221)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.327 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.603` → IC=+0.352 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.603 (IC base=+0.221)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.284 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.221)

- **PATRÓN** `volumen_spike_ratio` > `2.2721` → IC=+0.234 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2721 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.238 (n=2757)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `2088.2932` → IC=+0.235 (n=872)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2088.2932 (IC base=+0.221)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.239 (n=1522)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.221)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.267 (n=1497)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=+0.261)

- **PATRÓN** `drift_60min` |x|≤ `0.1212` → IC=+0.279 (n=986)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1212 (IC base=+0.261)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=2047)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.261)

- **PATRÓN** `ibs_20min` < `0.5053` → IC=+0.288 (n=2240)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5053 (IC base=+0.261)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.234` → IC=+0.262 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.234 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` < `0.0949` → IC=+0.261 (n=2001)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0949 (IC base=+0.261)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.279 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.261 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.261)

- **PATRÓN** `volumen_spike_ratio` > `2.6384` → IC=+0.271 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6384 (IC base=+0.261)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.262 (n=2505)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.261)

- **PATRÓN** `libro_liquidez` > `1681.16` → IC=+0.269 (n=2001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1681.16 (IC base=+0.261)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.265 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.261)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.200 (n=865)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1063` → IC=+0.162 (n=1139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1063 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2705)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3769` → IC=+0.226 (n=2313)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3769 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.126` → IC=+0.196 (n=1364)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.126 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.602` → IC=+0.162 (n=427)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.602 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.192` → IC=+0.155 (n=2255)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 3.192 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.175 (n=864)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6288 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0715` → IC=+0.154 (n=2311)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0715 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2713` → IC=+0.179 (n=369)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2713 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1743` → IC=+0.161 (n=2225)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1743 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5289` → IC=+0.154 (n=2259)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5289 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.182 (n=1096)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 267.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.165 (n=2185)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2591` → IC=+0.163 (n=1920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2591 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.170 (n=826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.7006` → IC=+0.198 (n=2182)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7006 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1371` → IC=+0.166 (n=2040)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1371 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.205` → IC=+0.158 (n=363)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 11.205 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.456` → IC=+0.144 (n=2199)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.456 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1856` → IC=+0.154 (n=2182)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1856 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.198 (n=408)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.150 (n=2077)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7717` → IC=+0.155 (n=1385)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7717 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `275.0` → IC=+0.154 (n=874)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 275.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.260 (n=892)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.228 (n=2394)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=993)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.318 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.2094` → IC=+0.226 (n=2717)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2094 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.6973` → IC=+0.239 (n=1173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6973 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=3162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1849.4184` → IC=+0.237 (n=1777)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1849.4184 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.244 (n=2205)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1818` → IC=+0.255 (n=1103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1818 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.264 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0272` → IC=+0.303 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0272 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.03` → IC=+0.293 (n=403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.03 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.298 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1354` → IC=+0.250 (n=1585)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1354 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.241 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2058.44` → IC=+0.260 (n=835)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2058.44 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.250 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.199 (n=1215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4194` → IC=+0.158 (n=2757)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4194 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2515` → IC=+0.194 (n=2757)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2515 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.141` → IC=+0.171 (n=1483)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.141 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.154` → IC=+0.162 (n=1122)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.154 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8691` → IC=+0.165 (n=1838)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8691 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.187 (n=359)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5219` → IC=+0.164 (n=1184)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5219 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1702` → IC=+0.158 (n=1219)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1702 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6661.8302` → IC=+0.241 (n=1250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6661.8302 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.174 (n=1170)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 75.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.149 (n=2291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0074 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4396` → IC=+0.140 (n=2290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4396 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=836)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.7385` → IC=+0.184 (n=2290)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7385 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1496` → IC=+0.144 (n=2071)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1496 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.137` → IC=+0.171 (n=347)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.137 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8737` → IC=+0.141 (n=1527)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8737 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.234 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.138 (n=2201)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4309 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7400.3488` → IC=+0.211 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7400.3488 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.129 (n=1968)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 133.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.146 (n=1850)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0084 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=1012)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.199 (n=2773)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4444 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `1.0677` → IC=+0.207 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0677 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.789` → IC=+0.269 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.789 (IC base=+0.124)

- **PATRÓN** `volumen_regimen` < `1.2241` → IC=+0.136 (n=2769)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2241 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.125 (n=2610)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.124)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.141 (n=357)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` < `1.8314` → IC=+0.127 (n=1804)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 1.8314 (IC base=+0.124)

- **PATRÓN** `volumen_spike_ratio` > `2.1893` → IC=+0.130 (n=1226)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` > 2.1893 (IC base=+0.124)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.129 (n=2856)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `2513.3094` → IC=+0.237 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2513.3094 (IC base=+0.124)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.136 (n=890)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 25.0 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.140 (n=2650)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0111 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1335` → IC=+0.157 (n=884)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1335 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=2735)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6458` → IC=+0.211 (n=2650)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6458 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2159` → IC=+0.138 (n=2268)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2159 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.298` → IC=+0.134 (n=2554)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.298 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6433` → IC=+0.138 (n=884)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6433 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2238` → IC=+0.169 (n=448)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.2238 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4381` → IC=+0.150 (n=826)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4381 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2692.6188` → IC=+0.211 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2692.6188 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.135 (n=2163)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 47.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.246 (n=2345)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=2743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=1752)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.6074` → IC=+0.270 (n=2345)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6074 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1948` → IC=+0.244 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1948 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.748` → IC=+0.270 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.748 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2301` → IC=+0.234 (n=2626)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2301 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6423` → IC=+0.230 (n=2625)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6423 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.249 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.5001` → IC=+0.244 (n=851)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5001 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=3407)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2643.8343` → IC=+0.239 (n=1750)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2643.8343 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0229` → IC=+0.248 (n=1246)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0229 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.236 (n=2585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.264 (n=2747)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` < `0.2938` → IC=+0.233 (n=2638)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2938 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.209` → IC=+0.262 (n=528)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.209 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `1.227` → IC=+0.256 (n=916)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.227 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2799` → IC=+0.298 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2799 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4297` → IC=+0.231 (n=2546)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4297 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2399.323` → IC=+0.229 (n=2454)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.323 (IC base=+0.228)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=4800)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.242 (n=1620)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.5061` → IC=+0.212 (n=4853)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5061 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.219 (n=1743)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.9401` → IC=+0.244 (n=1618)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9401 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.1725` → IC=+0.210 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1725 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.4358` → IC=+0.210 (n=3516)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4358 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.76` → IC=+0.212 (n=1580)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.76 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.634` → IC=+0.204 (n=4324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.634 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `0.7054` → IC=+0.217 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7054 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.8841` → IC=+0.208 (n=2382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8841 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.1664` → IC=+0.218 (n=1363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1664 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.4537` → IC=+0.209 (n=1593)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4537 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.8412` → IC=+0.204 (n=3186)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8412 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=3783)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2972.894` → IC=+0.214 (n=4335)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2972.894 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.237 (n=1206)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.189)

- **PATRÓN** `drift_60min` |x|≤ `0.4923` → IC=+0.205 (n=3612)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4923 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=1208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.205 (n=1620)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.189)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.195 (n=3612)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.7333 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` > `0.6725` → IC=+0.201 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6725 (IC base=+0.189)

- **PATRÓN** `dist_vwap_pct` < `0.4192` → IC=+0.186 (n=3619)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.4192 (IC base=+0.189)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.141` → IC=+0.197 (n=3626)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 6.141 (IC base=+0.189)

- **PATRÓN** `volumen_regimen` < `1.1012` → IC=+0.198 (n=3009)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.1012 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.193 (n=3309)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.189)

- **PATRÓN** `volumen_pendiente_norm` > `0.2222` → IC=+0.190 (n=734)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2222 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.194 (n=1569)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.189)

- **PATRÓN** `volumen_spike_ratio` > `1.8117` → IC=+0.196 (n=2375)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 1.8117 (IC base=+0.189)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=4800)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.189)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.199 (n=3117)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 166.0 (IC base=+0.189)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.260 (n=622)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.247)

- **PATRÓN** `drift_60min` |x|≤ `0.0855` → IC=+0.287 (n=237)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0855 (IC base=+0.247)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.252 (n=748)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.247)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.247)

- **PATRÓN** `ibs_20min` < `0.4907` → IC=+0.270 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4907 (IC base=+0.247)

- **PATRÓN** `dist_vwap_pct` < `0.3329` → IC=+0.259 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3329 (IC base=+0.247)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.051` → IC=+0.264 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.051 (IC base=+0.247)

- **PATRÓN** `volumen_regimen` < `1.2148` → IC=+0.253 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2148 (IC base=+0.247)

- **PATRÓN** `volumen_regimen` > `0.868` → IC=+0.265 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.868 (IC base=+0.247)

- **PATRÓN** `volumen_pendiente_norm` > `0.2866` → IC=+0.342 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2866 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` < `1.8149` → IC=+0.255 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8149 (IC base=+0.247)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.247 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.247)

- **PATRÓN** `libro_liquidez` > `12150.0374` → IC=+0.256 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12150.0374 (IC base=+0.247)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.227 (n=838)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3723` → IC=+0.184 (n=1254)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.3723 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.213 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.196 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.204 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1409 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.6081` → IC=+0.172 (n=568)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.6081 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.6916` → IC=+0.199 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6916 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.38` → IC=+0.189 (n=1236)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 6.38 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `0.8873` → IC=+0.201 (n=836)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8873 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.1525` → IC=+0.192 (n=387)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1525 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `1.4032` → IC=+0.184 (n=416)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` < 1.4032 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `2.1625` → IC=+0.183 (n=566)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.1625 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `13472.9392` → IC=+0.181 (n=835)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 13472.9392 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `699.0` → IC=+0.183 (n=1207)

  - _Acción_: Kelly boost +0.92€ cuando `ballena_activa_n` < 699.0 (IC base=+0.171)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.193 (n=320)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0068 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.5887` → IC=+0.186 (n=727)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.5887 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.237 (n=260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.231 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.51` → IC=+0.220 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.51 (IC base=+0.175)

- **PATRÓN** `volumen_pendiente_norm` > `0.2088` → IC=+0.224 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2088 (IC base=+0.175)

- **PATRÓN** `volumen_spike_ratio` > `2.2445` → IC=+0.183 (n=484)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.2445 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `2520.8066` → IC=+0.223 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2520.8066 (IC base=+0.175)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.233 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.227)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.215 (n=1366)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.4612` → IC=+0.207 (n=1366)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4612 (IC base=+0.199)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.5189` → IC=+0.212 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5189 (IC base=+0.199)

- **PATRÓN** `ibs_20min` > `0.7601` → IC=+0.199 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7601 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.2178` → IC=+0.212 (n=1209)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2178 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.114` → IC=+0.208 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.114 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `0.8778` → IC=+0.202 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8778 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.210 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.1054` → IC=+0.203 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1054 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` > `0.1642` → IC=+0.199 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1642 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` < `2.4554` → IC=+0.206 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4554 (IC base=+0.199)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.201 (n=1400)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.199)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.205 (n=1117)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.211 (n=1117)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.204 (n=437)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.198 (n=747)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.3984` → IC=+0.196 (n=745)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.3984 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.0864` → IC=+0.190 (n=1117)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.0864 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6705` → IC=+0.199 (n=197)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6705 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.2251` → IC=+0.189 (n=1079)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2251 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.74` → IC=+0.193 (n=1143)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.74 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `1.2445` → IC=+0.200 (n=1117)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2445 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0744` → IC=+0.209 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0744 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.198 (n=962)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.5263` → IC=+0.190 (n=366)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5263 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `6859.3179` → IC=+0.194 (n=1117)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 6859.3179 (IC base=+0.188)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.204 (n=639)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.204 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.251 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.7569` → IC=+0.235 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7569 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.236` → IC=+0.203 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.236 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `0.6955` → IC=+0.229 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6955 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.194 (n=652)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.0799` → IC=+0.192 (n=323)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0799 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` < `1.5676` → IC=+0.199 (n=310)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5676 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.4815` → IC=+0.209 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4815 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=845)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `3097.399` → IC=+0.202 (n=648)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3097.399 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.201 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.203 (n=352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.202 (n=176)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.199)

- **PATRÓN** `drift_60min` |x|≤ `0.6144` → IC=+0.220 (n=527)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6144 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.235 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.199)

- **PATRÓN** `ibs_20min` < `0.7259` → IC=+0.222 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7259 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` > `0.5232` → IC=+0.222 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5232 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `1.2199` → IC=+0.202 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.2199 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.926` → IC=+0.209 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.926 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` < `1.3392` → IC=+0.203 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3392 (IC base=+0.199)

- **PATRÓN** `volumen_regimen` > `0.9412` → IC=+0.208 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9412 (IC base=+0.199)

- **PATRÓN** `volumen_pendiente_norm` < `0.1072` → IC=+0.222 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1072 (IC base=+0.199)

- **PATRÓN** `volumen_spike_ratio` > `2.2044` → IC=+0.240 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2044 (IC base=+0.199)

- **PATRÓN** `libro_liquidez` > `2990.7396` → IC=+0.218 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2990.7396 (IC base=+0.199)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.230 (n=516)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.199)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.157 (n=706)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0039 (IC base=+0.067)

- **PATRÓN** `ibs_20min` > `0.5405` → IC=+0.164 (n=1345)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5405 (IC base=+0.067)

- **PATRÓN** `dist_vwap_pct` > `0.3593` → IC=+0.154 (n=533)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.3593 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.193` → IC=+0.170 (n=334)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.193 (IC base=+0.067)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.248 (n=534)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` < `0.1015` → IC=+0.136 (n=779)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1015 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.43` → IC=+0.182 (n=127)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 10.43 (IC base=+0.069)

- **PATRÓN** `volumen_pendiente_norm` > `0.148` → IC=+0.192 (n=219)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.148 (IC base=+0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.4824` → IC=+0.130 (n=322)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4824 (IC base=+0.069)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.4989` → IC=-0.120 (n=222)

  - _Acción_: SKIP cuando `ibs_20min` < 0.4989
  - _Potencial_: sin este filtro IC_bueno=+0.182 (n=451)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.124 (n=536)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0056 (IC base=+0.081)

- **PATRÓN** `ibs_20min` > `0.4989` → IC=+0.182 (n=451)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.4989 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.1218` → IC=+0.154 (n=255)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1218 (IC base=+0.081)

- **PATRÓN** `ibs_20min` < `0.2807` → IC=+0.237 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2807 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.216` → IC=+0.129 (n=397)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.216 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.8276` → IC=+0.121 (n=238)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 0.8276 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.190 (n=69)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `2.1644` → IC=+0.122 (n=294)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_spike_ratio` < 2.1644 (IC base=+0.086)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.131 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0059 (IC base=+0.093)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.123 (n=491)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 7.0 (IC base=+0.093)

- **PATRÓN** `ibs_20min` > `0.6407` → IC=+0.206 (n=437)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6407 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.1258` → IC=+0.198 (n=256)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1258 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.269` → IC=+0.255 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.269 (IC base=+0.093)

- **PATRÓN** `volumen_regimen` < `0.8145` → IC=+0.126 (n=327)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.8145 (IC base=+0.093)

- **PATRÓN** `volumen_pendiente_norm` > `0.2854` → IC=+0.157 (n=68)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` > 0.2854 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.106` → IC=+0.286 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.106 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.836` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.836 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.1379` → IC=+0.167 (n=70)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1379 (IC base=+0.033)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.1429` → IC=-0.219 (n=62)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1429
  - _Potencial_: sin este filtro IC_bueno=+0.245 (n=190)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.164 (n=343)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.75 (IC base=+0.027)

- **PATRÓN** `dist_vwap_pct` > `0.7402` → IC=+0.131 (n=128)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.7402 (IC base=+0.027)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.483` → IC=+0.161 (n=107)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.483 (IC base=+0.027)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.167 (n=220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0103 (IC base=+0.083)

- **PATRÓN** `ibs_20min` < `0.1429` → IC=+0.245 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1429 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` < `0.6741` → IC=+0.153 (n=220)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.6741 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.803` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.803 (IC base=+0.083)

- **PATRÓN** `volumen_regimen` > `1.0831` → IC=+0.238 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0831 (IC base=+0.083)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` < `2.1886` → IC=+0.164 (n=147)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 2.1886 (IC base=+0.083)

- **PATRÓN** `volumen_spike_ratio` > `1.4109` → IC=+0.180 (n=167)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 1.4109 (IC base=+0.083)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.173 (n=160)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.06 (IC base=+0.083)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` < `0.0066` → IC=-0.229 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=102)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.216 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=160)

- **FILTRO** `dist_vwap_pct` > `0.2344` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2344
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=282)

- **FILTRO** `volumen_regimen` < `0.7708` → IC=-0.342 (n=74)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.7708
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=225)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.341 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=185)

- **FILTRO** `dist_vwap_pct` > `0.4388` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4388
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=226)

- **FILTRO** `sigma_ewma_delta_pct` > `10.676` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.676
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=222)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=135)

- **FILTRO** `libro_liquidez` < `1430.0389` → IC=-0.307 (n=81)

  - _Acción_: SKIP cuando `libro_liquidez` < 1430.0389
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=165)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `drift_60min` |x|> `0.1744` → IC=-0.260 (n=23)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1744
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=72)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.273 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=76)

- **FILTRO** `dist_vwap_pct` < `0.0874` → IC=-0.287 (n=73)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0874
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=81)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.441 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=67)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.243 (n=72)

- **FILTRO** `ibs_20min` > `0.538` → IC=-0.375 (n=46)

  - _Acción_: SKIP cuando `ibs_20min` > 0.538
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=48)

- **FILTRO** `volumen_spike_ratio` < `1.4324` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `volumen_spike_ratio` < 1.4324
  - _Potencial_: sin este filtro IC_bueno=-0.255 (n=47)

- **FILTRO** `libro_liquidez` < `1496.9492` → IC=-0.296 (n=47)

  - _Acción_: SKIP cuando `libro_liquidez` < 1496.9492
  - _Potencial_: sin este filtro IC_bueno=-0.255 (n=47)

- **PATRÓN** `ibs_20min` > `0.9464` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.9464 (IC base=-0.173)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0064` → IC=-0.333 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=70)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.395 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.197 (n=87)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.329 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=12)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1644` → IC=-0.123 (n=271)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1644
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=527)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.180 (n=167)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.007 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.142 (n=501)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` > 0.6818 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.7337` → IC=+0.211 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7337 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.6322` → IC=+0.159 (n=168)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.6322 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` < `0.2284` → IC=+0.132 (n=444)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` < 0.2284 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `1.7963` → IC=+0.143 (n=267)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_spike_ratio` < 1.7963 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.1644` → IC=+0.160 (n=527)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1644 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.12` → IC=+0.180 (n=179)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 9.12 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `3247.8769` → IC=+0.143 (n=399)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 3247.8769 (IC base=+0.064)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6623` → IC=-0.217 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6623
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=156)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.216 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.158 (n=191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 12.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.154 (n=105)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 6.0 (IC base=+0.139)

- **PATRÓN** `ibs_20min` < `0.1796` → IC=+0.199 (n=280)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1796 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.0941` → IC=+0.154 (n=284)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.0941 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.216` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 7.216 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.645` → IC=+0.138 (n=222)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 4.645 (IC base=+0.139)

- **PATRÓN** `volumen_regimen` > `1.0304` → IC=+0.190 (n=127)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_regimen` > 1.0304 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` < `0.0701` → IC=+0.158 (n=217)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_pendiente_norm` < 0.0701 (IC base=+0.139)

- **PATRÓN** `volumen_pendiente_norm` > `0.2726` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2726 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` < `2.5184` → IC=+0.172 (n=248)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.5184 (IC base=+0.139)

- **PATRÓN** `volumen_spike_ratio` > `1.5491` → IC=+0.147 (n=222)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` > 1.5491 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4587.7919` → IC=+0.147 (n=250)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 4587.7919 (IC base=+0.139)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1302` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1302
  - _Potencial_: sin este filtro IC_bueno=+0.130 (n=163)

- **FILTRO** `ibs_20min` > `0.1906` → IC=-0.134 (n=99)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1906
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=193)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.120 (n=156)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.005 (IC base=+0.086)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.172 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.086)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.131 (n=158)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.8015 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.015` → IC=+0.131 (n=128)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.015 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `1.0086` → IC=+0.120 (n=156)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_regimen` < 1.0086 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` < `0.1302` → IC=+0.130 (n=163)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.1302 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `1.4416` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4416 (IC base=+0.086)

- **PATRÓN** `ibs_20min` < `0.1906` → IC=+0.120 (n=193)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.1906 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.034)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4118` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4118
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=101)

- **FILTRO** `dist_vwap_pct` > `0.1687` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1687
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=97)

- **FILTRO** `volumen_spike_ratio` > `2.4266` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.4266
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=73)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.300 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.263 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6522 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` < `0.216` → IC=+0.241 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.216 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.331` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.331 (IC base=+0.241)

- **PATRÓN** `volumen_regimen` < `0.5837` → IC=+0.314 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5837 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.11` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.11 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` < `1.5351` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5351 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.240 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.418` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.418 (IC base=-0.081)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.326 (n=67)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.310)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.310)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.310)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.367 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.310)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.310)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.233)

- **PATRÓN** `elapsed_s` > `185.9` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.9 (IC base=+0.233)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.233)

- **PATRÓN** `drift_15min` |x|≤ `1.4315` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4315 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.273 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.233)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.233)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.326 (n=67)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.310)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.383 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.310)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.310)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.367 (n=58)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.310)

- **PATRÓN** `ballena_activa_n` < `1114.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1114.0 (IC base=+0.310)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3488` → IC=+0.263 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3488 (IC base=+0.233)

- **PATRÓN** `elapsed_s` > `185.9` → IC=+0.246 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.9 (IC base=+0.233)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.278 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.233)

- **PATRÓN** `drift_15min` |x|≤ `1.4315` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4315 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.273 (n=64)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.233)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.326 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.233)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2855.9096` → IC=+0.134 (n=553)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2855.9096 (IC base=+0.098)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2855.9096` → IC=+0.134 (n=553)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2855.9096 (IC base=+0.098)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=184)

- **FILTRO** `libro_liquidez` < `2764.5849` → IC=-0.192 (n=50)

  - _Acción_: SKIP cuando `libro_liquidez` < 2764.5849
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=150)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=266)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=66)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.149 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=14)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=25)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `liq_usd_total` < `3561.53` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 3561.53
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=23)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=31)

- **FILTRO** `ballena_activa_n` > `55.0` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `ballena_activa_n` > 55.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### LIQUIDACIONES_15M#SOL#15min
- **FILTRO** `hora_utc` > `4.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.121 (n=85)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3417)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

- **FILTRO** `ballena_activa_n` > `118.0` → IC=-0.217 (n=58)

  - _Acción_: SKIP cuando `ballena_activa_n` > 118.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=29)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1251)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1205)

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
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=713)

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
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=410)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=391)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.137 (n=169)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.495 (IC base=+0.019)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=834)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=834)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.133 (n=257)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=657)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=776)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=776)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=221)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=221)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.132 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=170)

- **FILTRO** `py_entrada` > `0.535` → IC=-0.183 (n=39)

  - _Acción_: SKIP cuando `py_entrada` > 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=215)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=239)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=254)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.123 (n=59)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=213)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=250)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=344)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=344)

- **FILTRO** `libro_liquidez` < `611.7268` → IC=-0.132 (n=123)

  - _Acción_: SKIP cuando `libro_liquidez` < 611.7268
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=251)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=250)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=178)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.122 (n=1266)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3315)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.132 (n=55)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.094 (n=30)

- **FILTRO** `py_entrada` > `0.47` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `restante_min` < `3.95` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `restante_min` < 3.95
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=15)

- **FILTRO** `lag_apertura_s` > `62.87` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `lag_apertura_s` > 62.87
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.157 (n=135)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.46 (IC base=+0.011)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.198 (n=51)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=231)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.152 (n=139)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=156)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.5 (IC base=+0.051)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.128 (n=315)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=114)

- **FILTRO** `profundidad_ratio` < `40.5` → IC=-0.170 (n=107)

  - _Acción_: SKIP cuando `profundidad_ratio` < 40.5
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=322)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.218 (n=69)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.002 (n=309)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `profundidad_ratio` < `20.7` → IC=-0.142 (n=132)

  - _Acción_: SKIP cuando `profundidad_ratio` < 20.7
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=268)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.175 (n=78)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=332)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.131 (n=266)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=285)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=5680)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=17729)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.170 (n=6016)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=18124)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.193 (n=1041)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=3195)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.167 (n=995)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=3326)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.139 (n=1114)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1416.98` → IC=+0.135 (n=2118)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 1416.98 (IC base=+0.037)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.129 (n=2017)

  - _Acción_: Kelly boost +0.65€ cuando `py_entrada` < 0.5 (IC base=+0.015)

- **PATRÓN** `libro_liquidez` > `1527.98` → IC=+0.151 (n=1470)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1527.98 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.155 (n=790)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2664)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.175 (n=839)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2598)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.173 (n=1045)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=3220)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.200 (n=1020)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=3379)

- **PATRÓN** `ibs_20min` > `0.9635` → IC=+0.130 (n=1451)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9635 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1839.6776` → IC=+0.126 (n=1451)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1839.6776 (IC base=+0.037)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.157 (n=1017)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=3227)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2328)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=2749)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=3489)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=436)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.264 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=423)

- **FILTRO** `py_entrada` > `0.595` → IC=-0.234 (n=273)

  - _Acción_: SKIP cuando `py_entrada` > 0.595
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=854)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.102 (n=347)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=875)

- **FILTRO** `libro_liquidez` < `2083.4373` → IC=-0.168 (n=347)

  - _Acción_: SKIP cuando `libro_liquidez` < 2083.4373
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=705)

### MOMENTUM_IBS_15M_FADE#XRP#15min
- **FILTRO** `hora_utc` < `13.0` → IC=-0.238 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=232)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=16146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=36104)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=12734)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=39516)

- **FILTRO** `ibs_7min` < `0.2417` → IC=-0.229 (n=13060)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2417
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=39190)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.152 (n=17586)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=34664)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.238 (n=16084)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=49956)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.180 (n=16318)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=49722)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.145 (n=2599)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6473)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=4489)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=4583)

- **FILTRO** `ibs_7min` < `0.7115` → IC=-0.246 (n=2991)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7115
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=6081)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.177 (n=1996)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7076)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.269 (n=2828)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.001 (n=8623)

- **FILTRO** `ibs_7min` > `0.7703` → IC=-0.210 (n=2862)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7703
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=8589)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2041)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=6807)

- **FILTRO** `ibs_7min` < `0.7285` → IC=-0.197 (n=2212)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7285
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6636)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.189 (n=2202)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6646)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2197)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6788)

- **FILTRO** `ibs_7min` > `0.2677` → IC=-0.196 (n=2244)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2677
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6741)

- **FILTRO** `ballena_activa_n` > `149.0` → IC=-0.182 (n=2246)

  - _Acción_: SKIP cuando `ballena_activa_n` > 149.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6739)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.157 (n=2117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=6516)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.316 (n=2103)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=6530)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.246 (n=2842)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=5791)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.194 (n=2096)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6537)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.252 (n=2808)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9379)

- **FILTRO** `ibs_7min` > `0.7333` → IC=-0.175 (n=3043)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7333
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=9144)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.123 (n=2781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=5739)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=1982)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6538)

- **FILTRO** `ibs_7min` < `0.732` → IC=-0.187 (n=2130)

  - _Acción_: SKIP cuando `ibs_7min` < 0.732
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6390)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.192 (n=2063)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6457)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=1971)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=6886)

- **FILTRO** `ibs_7min` > `0.2749` → IC=-0.179 (n=2214)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2749
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6643)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.174 (n=2212)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6645)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=2035)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=6569)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.232 (n=2150)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=6454)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.218 (n=2080)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6524)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.187 (n=3017)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=9604)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.280 (n=2137)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6436)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.219 (n=2140)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6433)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.198 (n=1943)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=6630)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.211 (n=2897)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9042)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=120)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=981)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1265)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=531)

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
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=830)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.128 (n=151)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=339)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=323)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=440)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=629)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.144 (n=1111)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.72€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.140 (n=517)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.130)

- **PATRÓN** `total_vol_5m` < `3732.187` → IC=+0.148 (n=740)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 3732.187 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `3669.2114` → IC=+0.142 (n=503)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3669.2114 (IC base=+0.130)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.149 (n=368)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 12.0 (IC base=+0.130)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4367` → IC=+0.167 (n=88)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.83€ cuando `delta_ratio` |x|> 0.4367 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.216 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `2585.3133` → IC=+0.222 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2585.3133 (IC base=+0.144)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.135 (n=228)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.142 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 3.0 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.130 (n=271)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.04 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2098.069` → IC=+0.126 (n=204)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 2098.069 (IC base=+0.120)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4156` → IC=+0.185 (n=147)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.4156 (IC base=+0.135)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.155 (n=227)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 4.0 (IC base=+0.135)

- **PATRÓN** `total_vol_5m` < `391.8444` → IC=+0.220 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 391.8444 (IC base=+0.135)

- **PATRÓN** `libro_liquidez` > `7895.7846` → IC=+0.138 (n=147)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 7895.7846 (IC base=+0.135)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.135)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4332` → IC=+0.258 (n=89)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4332 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.150)

- **PATRÓN** `total_vol_5m` < `4970.298` → IC=+0.184 (n=131)

  - _Acción_: Kelly boost +0.92€ cuando `total_vol_5m` < 4970.298 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `3077.3625` → IC=+0.162 (n=196)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3077.3625 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 27.0 (IC base=+0.150)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.140 (n=184)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.70€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.095)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.121 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 14.0 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=124)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.095)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.163 (n=93)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.095)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.4547` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.4547
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=130)

- **FILTRO** `sigma_h` > `0.0051` → IC=-0.267 (n=315)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=317)

- **FILTRO** `T_h` > `129.6211` → IC=-0.203 (n=156)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=476)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.183 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0034 (IC base=-0.079)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9957` → IC=-0.276 (n=47)

  - _Acción_: SKIP cuando `T_h` > 87.9957
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=143)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.300 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.036)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.152 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.237 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=72)

- **FILTRO** `T_h` < `87.7913` → IC=-0.179 (n=54)

  - _Acción_: SKIP cuando `T_h` < 87.7913
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.233 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0054 (IC base=-0.082)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0101` → IC=-0.217 (n=444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0101
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=148)

- **FILTRO** `T_h` > `70.6078` → IC=-0.194 (n=443)

  - _Acción_: SKIP cuando `T_h` > 70.6078
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=149)

- **FILTRO** `sigma_h` > `0.0083` → IC=-0.272 (n=169)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=331)

- **FILTRO** `T_h` > `54.3929` → IC=-0.279 (n=374)

  - _Acción_: SKIP cuando `T_h` > 54.3929
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=126)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0043` → IC=-0.200 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.138 (n=147)

- **FILTRO** `T_h` > `71.43` → IC=-0.182 (n=130)

  - _Acción_: SKIP cuando `T_h` > 71.43
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=65)

- **FILTRO** `T_h` > `72.749` → IC=-0.279 (n=134)

  - _Acción_: SKIP cuando `T_h` > 72.749
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=45)

- **FILTRO** `pct_vs_K` |x|> `3.0008` → IC=-0.432 (n=42)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0008
  - _Potencial_: sin este filtro IC_bueno=-0.219 (n=137)

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
- **FILTRO** `sigma_h` < `0.0091` → IC=-0.316 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=58)

- **FILTRO** `T_h` > `78.4593` → IC=-0.260 (n=127)

  - _Acción_: SKIP cuando `T_h` > 78.4593
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.375 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.130 (n=117)

- **FILTRO** `T_h` > `57.5396` → IC=-0.281 (n=103)

  - _Acción_: SKIP cuando `T_h` > 57.5396
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=52)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.006` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.245 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=109)

- **FILTRO** `T_h` > `94.1391` → IC=-0.218 (n=108)

  - _Acción_: SKIP cuando `T_h` > 94.1391
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=54)

- **FILTRO** `sigma_h` > `0.0153` → IC=-0.362 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0153
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=83)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.263 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=74)

- **FILTRO** `T_h` > `46.6251` → IC=-0.313 (n=73)

  - _Acción_: SKIP cuando `T_h` > 46.6251
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=37)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1221` → IC=+0.464 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1221 (IC base=+0.333)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.349 (n=91)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.333)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.370 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.333)

- **PATRÓN** `T_h` > `0.7719` → IC=+0.387 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7719 (IC base=+0.333)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.333)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.347 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.333)

- **PATRÓN** `edge` > `0.097` → IC=+0.444 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.097 (IC base=+0.416)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.432 (n=190)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.416)

- **PATRÓN** `T_h` < `0.5922` → IC=+0.431 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5922 (IC base=+0.416)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.431 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.3772` → IC=+0.458 (n=213)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3772 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.416)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.418)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.419 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.418)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.423 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.418)

- **PATRÓN** `T_h` < `1.0313` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 1.0313 (IC base=+0.418)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.407 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.418)

- **PATRÓN** `dist_50` > `0.4084` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4084 (IC base=+0.418)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.426 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.418)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.418)

### RESOLUTION_SNIPER#SOL#sniper
- **PATRÓN** `edge` > `0.1885` → IC=+0.482 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1885 (IC base=+0.435)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.465 (n=55)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.435)

- **PATRÓN** `T_h` > `0.4307` → IC=+0.447 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4307 (IC base=+0.435)

- **PATRÓN** `dist_50` > `0.3326` → IC=+0.465 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3326 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.435 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.435)

- **PATRÓN** `edge` > `0.177` → IC=+0.478 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.177 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.478 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.464)

- **PATRÓN** `T_h` > `1.1543` → IC=+0.478 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1543 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4373` → IC=+0.485 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4373 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=300)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=375)

- **FILTRO** `streak_estiramiento` > `0.8469` → IC=-0.182 (n=83)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8469
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=251)

- **PATRÓN** `streak_estiramiento` < `0.8469` → IC=+0.121 (n=251)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.8469 (IC base=+0.043)

- **PATRÓN** `libro_liquidez` > `2790.9544` → IC=+0.147 (n=100)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2790.9544 (IC base=+0.043)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=16)

- **FILTRO** `libro_liquidez` < `2474.7486` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 2474.7486
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=16)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `streak_estiramiento` < `0.2711` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `streak_estiramiento` < 0.2711 (IC base=-0.004)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.140 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 7.0 (IC base=+0.084)

- **PATRÓN** `streak_estiramiento` < `0.5597` → IC=+0.170 (n=107)

  - _Acción_: Kelly boost +0.85€ cuando `streak_estiramiento` < 0.5597 (IC base=+0.084)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 29.0 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `2274.7787` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2274.7787 (IC base=+0.084)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=93)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=44)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=29)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

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

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.024)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=960)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1329)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1105)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1140)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `14.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3879)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=17)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=2130)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.198 (n=1512)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0053 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.194 (n=1146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.012 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1731` → IC=+0.195 (n=3024)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1731 (IC base=+0.180)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1333` → IC=+0.191 (n=1365)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1333 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=3191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=3161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.180)

- **PATRÓN** `ibs_15` > `0.5641` → IC=+0.257 (n=3438)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5641 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1251` → IC=+0.173 (n=1638)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1251 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.6735` → IC=+0.168 (n=3244)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.6735 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.594` → IC=+0.255 (n=899)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.594 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `4870.1814` → IC=+0.201 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4870.1814 (IC base=+0.180)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=1349)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.233 (n=587)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.0582` → IC=+0.263 (n=196)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0582 (IC base=+0.223)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2509` → IC=+0.247 (n=196)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2509 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.241 (n=592)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `ibs_15` > `0.7243` → IC=+0.284 (n=587)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7243 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1354` → IC=+0.246 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1354 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.5198` → IC=+0.226 (n=662)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5198 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.305 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `16220.2116` → IC=+0.253 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16220.2116 (IC base=+0.223)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.192 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0034 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.1497` → IC=+0.150 (n=593)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1497 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1453` → IC=+0.150 (n=449)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio_macro` |x|> 0.1453 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1354` → IC=+0.165 (n=264)

  - _Acción_: Kelly boost +0.83€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1354 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.150 (n=473)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 11.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5476` → IC=+0.245 (n=673)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5476 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1154` → IC=+0.157 (n=423)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1154 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.6102` → IC=+0.147 (n=768)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.6102 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.835` → IC=+0.279 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.835 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3534.509` → IC=+0.153 (n=601)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3534.509 (IC base=+0.145)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `18.005` → IC=-0.184 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.005
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=304)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.140 (n=245)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0061 (IC base=+0.096)

- **PATRÓN** `drift_60min` |x|≤ `0.1666` → IC=+0.140 (n=490)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.1666 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.9` → IC=+0.245 (n=245)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.131 (n=402)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.096)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.013)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0238` → IC=+0.247 (n=267)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0238 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.237 (n=352)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.202)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3374` → IC=+0.233 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3374 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.217 (n=709)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.202)

- **PATRÓN** `ibs_15` > `0.5429` → IC=+0.282 (n=800)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5429 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.1887` → IC=+0.211 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1887 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.825` → IC=+0.225 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.825 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `2969.9944` → IC=+0.299 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2969.9944 (IC base=+0.202)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.157 (n=768)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.368 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.383 (n=203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.385 (n=405)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2268` → IC=+0.383 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2268 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=611)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.400 (n=609)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4165` → IC=+0.392 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4165 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.722` → IC=+0.386 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.722 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3505.1277` → IC=+0.374 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3505.1277 (IC base=+0.364)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.365 (n=280)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.390 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.366)

- **PATRÓN** `drift_15min` |x|≤ `0.5105` → IC=+0.364 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5105 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2136` → IC=+0.390 (n=144)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2136 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.397 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.384 (n=318)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.8057` → IC=+0.391 (n=318)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8057 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.2448` → IC=+0.395 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2448 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.997` → IC=+0.385 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.997 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `15400.5519` → IC=+0.390 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15400.5519 (IC base=+0.366)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.412 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.366)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.363 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.361)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.381 (n=132)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.361)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0903` → IC=+0.374 (n=260)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0903 (IC base=+0.361)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2986` → IC=+0.380 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2986 (IC base=+0.361)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.387 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.361)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.367 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.361)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.411 (n=291)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.380 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.361)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.363 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.361)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.293` → IC=+0.387 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.293 (IC base=+0.361)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.361)

- **PATRÓN** `libro_liquidez` > `3951.6306` → IC=+0.388 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3951.6306 (IC base=+0.361)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.171 (n=2109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=2111)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.210 (n=1652)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2568)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1402` → IC=+0.189 (n=679)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.94€ cuando `delta_ratio_macro` |x|> 0.1402 (IC base=-0.066)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.284 (n=1019)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1081` → IC=+0.210 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1081 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.4242` → IC=+0.204 (n=991)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4242 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2295` → IC=+0.270 (n=1159)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2295 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3589` → IC=+0.282 (n=3477)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3589 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6634` → IC=+0.281 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6634 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0341` → IC=-0.218 (n=1810)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0341
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=607)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.231 (n=604)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1813)

- **FILTRO** `sigma_ewma_delta_pct` > `23.385` → IC=-0.266 (n=348)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.385
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2069)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=2353)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.127 (n=724)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0052 (IC base=+0.101)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.300 (n=148)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.124 (n=726)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.101)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.336 (n=327)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.298 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` < `0.3659` → IC=+0.294 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3659 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.628` → IC=+0.138 (n=365)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 8.628 (IC base=+0.101)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0613` → IC=+0.207 (n=56)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0613 (IC base=-0.194)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0902` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0902 (IC base=-0.194)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.293 (n=56)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.194)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.194)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 381.0 (IC base=-0.194)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.163 (n=662)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.167 (n=449)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.161 (n=340)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0048 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.0714` → IC=+0.192 (n=225)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0714 (IC base=+0.155)

- **PATRÓN** `drift_15min` |x|≤ `0.4004` → IC=+0.157 (n=170)

  - _Acción_: Kelly boost +0.78€ cuando `drift_15min` |x|≤ 0.4004 (IC base=+0.155)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.196 (n=389)

  - _Acción_: Kelly boost +0.98€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.168 (n=471)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.155)

- **PATRÓN** `ibs_15` > `0.6189` → IC=+0.256 (n=510)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6189 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.4589` → IC=+0.164 (n=135)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.4589 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.6525` → IC=+0.155 (n=587)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.6525 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.422` → IC=+0.260 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.422 (IC base=+0.155)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.163 (n=662)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.155)

- **PATRÓN** `libro_liquidez` > `10043.6494` → IC=+0.169 (n=170)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10043.6494 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.251 (n=1229)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.4483` → IC=+0.245 (n=1229)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4483 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7706` → IC=+0.260 (n=1082)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7706 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1578` → IC=+0.259 (n=819)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1578 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.249 (n=473)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3695` → IC=+0.275 (n=1229)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3695 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6027` → IC=+0.274 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6027 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.511` → IC=+0.252 (n=546)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.511 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.498` → IC=+0.250 (n=1286)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.498 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0473` → IC=-0.205 (n=730)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0473
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=244)

- **FILTRO** `drift_60min` |x|> `0.1726` → IC=-0.257 (n=331)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1726
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=643)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.280 (n=243)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=731)

- **FILTRO** `sigma_ewma_delta_pct` > `18.007` → IC=-0.146 (n=509)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.007
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4047)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.0642` → IC=+0.241 (n=546)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0642 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3529` → IC=+0.290 (n=547)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3529 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4499` → IC=+0.247 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4499 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.250 (n=585)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=586)

- **FILTRO** `drift_15min` |x|> `0.482` → IC=-0.227 (n=877)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.482
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=294)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=1152)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.206)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0678` → IC=+0.273 (n=754)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0678 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1154` → IC=+0.296 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1154 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.293 (n=845)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7764` → IC=+0.350 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7764 (IC base=-0.025)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.324 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.068)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.324 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.068)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.299 (n=910)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.319 (n=346)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.304 (n=345)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2247` → IC=+0.308 (n=612)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2247 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=1082)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.321 (n=1034)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.2663` → IC=+0.324 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2663 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.638` → IC=+0.376 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.638 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `14151.592` → IC=+0.313 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 14151.592 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.314 (n=245)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.319 (n=186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2556` → IC=+0.314 (n=186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2556 (IC base=+0.289)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3931` → IC=+0.300 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3931 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=559)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.827` → IC=+0.314 (n=557)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.827 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2523` → IC=+0.322 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2523 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.789` → IC=+0.382 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.789 (IC base=+0.289)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.288 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `16220.2116` → IC=+0.330 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16220.2116 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.304 (n=478)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0515` → IC=+0.315 (n=160)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0515 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.149` → IC=+0.297 (n=318)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.149 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1057` → IC=+0.337 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1057 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.306 (n=492)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.297 (n=431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.293)

- **PATRÓN** `ibs_15` > `0.8527` → IC=+0.325 (n=477)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8527 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.324 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.63` → IC=+0.361 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.63 (IC base=+0.293)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0999` → IC=-0.150 (n=218)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0999
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=74)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.169 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=358)

- **FILTRO** `ballena_activa_n` > `23.0` → IC=-0.206 (n=107)

  - _Acción_: SKIP cuando `ballena_activa_n` > 23.0
  - _Potencial_: sin este filtro IC_bueno=-0.113 (n=109)

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
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=148)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2412` → IC=-0.128 (n=92)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2412
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=93)

- **FILTRO** `drift_60min` |x|> `0.2244` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2244
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=34)

- **FILTRO** `drift_15min` |x|> `0.3481` → IC=-0.278 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3481
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.2021` → IC=-0.241 (n=25)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.2021
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

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3147` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3147
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.075` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.075
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.222 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=19)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0905` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `85.7585` → IC=+0.195 (n=463)

  - _Acción_: Kelly boost +0.97€ cuando `T_h` > 85.7585 (IC base=+0.190)

- **PATRÓN** `ratio` < `0.973` → IC=+0.423 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.190)

- **PATRÓN** `T_h` > `111.9997` → IC=+0.354 (n=2106)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9997 (IC base=+0.338)

- **PATRÓN** `ratio` > `1.0236` → IC=+0.374 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0236 (IC base=+0.338)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `105.6124` → IC=+0.179 (n=191)

  - _Acción_: Kelly boost +0.89€ cuando `T_h` > 105.6124 (IC base=+0.161)

- **PATRÓN** `ratio` < `0.9701` → IC=+0.384 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9701 (IC base=+0.161)

- **PATRÓN** `T_h` > `110.3225` → IC=+0.308 (n=722)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 110.3225 (IC base=+0.296)

- **PATRÓN** `ratio` > `1.0464` → IC=+0.399 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0464 (IC base=+0.296)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.236 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.229)

- **PATRÓN** `ratio` < `0.9849` → IC=+0.432 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.229)

- **PATRÓN** `T_h` > `111.9838` → IC=+0.353 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0372` → IC=+0.402 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0372 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1003` → IC=+0.445 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1003 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5641 sube el IC de +0.180 a +0.257 en UPDOWN_GBM#15min (n=3438). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7243 sube el IC de +0.223 a +0.284 en UPDOWN_GBM#BTC#15min (n=587). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5476 sube el IC de +0.145 a +0.245 en UPDOWN_GBM#ETH#15min (n=673). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9 sube el IC de +0.096 a +0.245 en UPDOWN_GBM#SOL#15min (n=245). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5429 sube el IC de +0.202 a +0.282 en UPDOWN_GBM#XRP#15min (n=800). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.157 en UPDOWN_GBM#XRP#15min (n=768). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.066 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=1019). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3589 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3477). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.101 a +0.336 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=327). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.194 a +0.293 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6189 sube el IC de +0.155 a +0.256 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=510). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3695 sube el IC de +0.244 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1229). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.190 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3529 sube el IC de -0.039 a +0.290 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=547). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.206 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.025 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=845). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.068 a +0.324 en UPDOWN_GBM_ETH_15M_HORA7 (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.068 a +0.324 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.291 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=1034). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.827 sube el IC de +0.289 a +0.314 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=557). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.293 a +0.325 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=477). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.364 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=609). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.366 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=318). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.361 a +0.411 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=291). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1851 | +0.090 | +198.87€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1851 | +0.090 | +198.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1467 | +0.095 | +174.42€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1467 | +0.095 | +174.42€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 280 | +0.067 | +10.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 280 | +0.067 | +10.78€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 73 | +0.100 | +14.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 73 | +0.100 | +14.01€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 542 | -0.020 | +54.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 542 | -0.020 | +54.23€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 391 | -0.044 | +28.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 391 | -0.044 | +28.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 121 | +0.053 | +20.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 121 | +0.053 | +20.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 27 | -0.017 | +2.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 27 | -0.017 | +2.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 39065 | -0.082 | -4897.72€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2139 | +0.030 | -243.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 36926 | -0.089 | -4653.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4437 | -0.116 | -764.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4437 | -0.116 | -764.76€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2139 | +0.030 | -243.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2139 | +0.030 | -243.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4283 | -0.105 | -879.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4283 | -0.105 | -879.15€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10370 | -0.019 | -920.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10370 | -0.019 | -920.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10240 | -0.104 | -782.98€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10240 | -0.104 | -782.98€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7596 | -0.138 | -1306.58€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7596 | -0.138 | -1306.58€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 33320 | -0.016 | +3525.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8623 | +0.005 | +1709.31€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 24697 | -0.023 | +1816.46€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 33320 | -0.016 | +3525.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8623 | +0.005 | +1709.31€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 24697 | -0.023 | +1816.46€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 139669 | +0.115 | -5725.14€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18182 | +0.183 | -518.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 610 | -0.021 | -67.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 112462 | +0.105 | -4840.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8415 | +0.102 | -298.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 18653 | +0.108 | -1139.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 18577 | +0.109 | -1138.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 27150 | +0.129 | -370.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5136 | +0.190 | -155.01€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 18638 | +0.120 | -102.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3334 | +0.084 | -90.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 18706 | +0.097 | -1366.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 71 | -0.116 | -5.63€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 18620 | +0.098 | -1349.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 29695 | +0.124 | -550.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7723 | +0.178 | -119.80€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 18881 | +0.106 | -362.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3079 | +0.100 | -60.29€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 26792 | +0.115 | -1349.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5125 | +0.195 | -253.20€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 513 | +0.013 | -13.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 19152 | +0.094 | -934.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2002 | +0.135 | -147.81€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 18673 | +0.104 | -949.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 66 | -0.088 | +4.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 18594 | +0.104 | -953.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 22422 | +0.196 | -1373.77€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 22422 | +0.196 | -1373.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5118 | +0.177 | -454.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5118 | +0.177 | -454.74€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2774 | +0.203 | -57.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2774 | +0.203 | -57.96€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5059 | +0.181 | -402.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5059 | +0.181 | -402.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4402 | +0.248 | -141.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4402 | +0.248 | -141.27€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4990 | +0.187 | -330.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4990 | +0.187 | -330.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 984 | +0.427 | -33.60€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 984 | +0.427 | -33.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 388 | +0.436 | -5.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 388 | +0.436 | -5.69€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 385 | +0.430 | -9.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 385 | +0.430 | -9.72€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 198 | +0.400 | -15.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 198 | +0.400 | -15.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 78410 | +0.200 | -5716.81€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 78410 | +0.200 | -5716.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 13462 | +0.185 | -1399.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 13462 | +0.185 | -1399.47€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 12665 | +0.224 | -449.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 12665 | +0.224 | -449.70€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 13434 | +0.179 | -1443.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 13434 | +0.179 | -1443.87€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 12734 | +0.220 | -486.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 12734 | +0.220 | -486.80€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13001 | +0.201 | -867.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13001 | +0.201 | -867.34€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13114 | +0.196 | -1069.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13114 | +0.196 | -1069.63€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 29981 | +0.117 | +220.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 29981 | +0.117 | +220.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 14904 | +0.120 | +188.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 14904 | +0.120 | +188.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15077 | +0.114 | +32.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15077 | +0.114 | +32.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2008 | +0.290 | -16.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2008 | +0.290 | -16.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 919 | +0.277 | -28.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 919 | +0.277 | -28.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 970 | +0.294 | +6.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 970 | +0.294 | +6.36€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 926 | +0.441 | +3.06€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 926 | +0.441 | +3.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 449 | +0.436 | -4.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 449 | +0.436 | -4.07€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 431 | +0.447 | +6.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 431 | +0.447 | +6.58€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1578 | +0.071 | -63.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 606 | +0.053 | -49.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 972 | +0.082 | -14.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1214 | +0.079 | -25.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 242 | +0.066 | -10.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 972 | +0.082 | -14.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 292 | +0.027 | -41.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 292 | +0.027 | -41.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 58937 | +0.100 | -1515.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4767 | +0.091 | +56.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 54170 | +0.101 | -1571.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 32467 | +0.105 | -364.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4767 | +0.091 | +56.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 27700 | +0.107 | -420.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12039 | +0.109 | -52.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12039 | +0.109 | -52.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 14431 | +0.081 | -1098.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 14431 | +0.081 | -1098.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 894 | +0.192 | -112.64€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 894 | +0.192 | -112.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 894 | +0.192 | -112.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 894 | +0.192 | -112.64€ | 3 | 4 |
| ✅ GBM_LATE_15M | 40635 | +0.093 | +21004.43€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 40635 | +0.093 | +21004.43€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6786 | +0.213 | +5505.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6786 | +0.213 | +5505.32€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6096 | +0.179 | +4594.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6096 | +0.179 | +4594.90€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 7257 | +0.204 | +5618.84€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7257 | +0.204 | +5618.84€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5677 | +0.040 | +1552.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5677 | +0.040 | +1552.30€ | 1 | 17 |
| ✅ GBM_LATE_15M#SOL | 5739 | -0.031 | +1220.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5739 | -0.031 | +1220.94€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 9080 | -0.032 | +2512.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9080 | -0.032 | +2512.13€ | 4 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 43792 | +0.086 | +23735.12€ | 0 | 18 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 43792 | +0.086 | +23735.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8468 | +0.004 | +4297.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8468 | +0.004 | +4297.18€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9250 | +0.011 | +2164.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9250 | +0.011 | +2164.47€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6086 | +0.276 | +6483.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6086 | +0.276 | +6483.78€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7807 | +0.013 | +1920.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7807 | +0.013 | +1920.94€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7005 | +0.039 | +2869.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7005 | +0.039 | +2869.72€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5176 | +0.299 | +5999.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5176 | +0.299 | +5999.03€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 32249 | +0.179 | +25919.77€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 32249 | +0.179 | +25919.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4894 | +0.226 | +4279.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4894 | +0.226 | +4279.33€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5066 | +0.150 | +3747.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5066 | +0.150 | +3747.12€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5166 | +0.222 | +4423.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5166 | +0.222 | +4423.25€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5464 | +0.138 | +4134.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5464 | +0.138 | +4134.83€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6061 | +0.123 | +4473.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6061 | +0.123 | +4473.75€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5598 | +0.224 | +4861.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5598 | +0.224 | +4861.49€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8618 | +0.134 | +4201.85€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8618 | +0.134 | +4201.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2562 | +0.143 | +1453.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2562 | +0.143 | +1453.18€ | 0 | 23 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2566 | +0.140 | +1218.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2566 | +0.140 | +1218.80€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2094 | +0.109 | +811.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2094 | +0.109 | +811.37€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 573 | +0.135 | +258.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 573 | +0.135 | +258.23€ | 0 | 26 |
| ✅ GBM_LATE_15M_TARDIO | 40838 | +0.184 | +32414.38€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 40838 | +0.184 | +32414.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6472 | +0.239 | +5969.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6472 | +0.239 | +5969.72€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6359 | +0.147 | +4313.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6359 | +0.147 | +4313.06€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6894 | +0.232 | +6131.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6894 | +0.232 | +6131.97€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6728 | +0.138 | +4795.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6728 | +0.138 | +4795.34€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7223 | +0.121 | +4936.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7223 | +0.121 | +4936.53€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7162 | +0.228 | +6267.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7162 | +0.228 | +6267.76€ | 0 | 21 |
| ✅ GBM_LATE_5M | 11285 | +0.197 | +8554.85€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 11285 | +0.197 | +8554.85€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2612 | +0.198 | +2151.95€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2612 | +0.198 | +2151.95€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1044 | +0.179 | +696.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1044 | +0.179 | +696.71€ | 0 | 16 |
| ✅ GBM_LATE_5M#ETH | 3310 | +0.194 | +2345.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3310 | +0.194 | +2345.49€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 1668 | +0.190 | +1256.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1668 | +0.190 | +1256.38€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1732 | +0.200 | +1290.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1732 | +0.200 | +1290.33€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3290 | +0.067 | +1115.69€ | 0 | 9 |
| ✅ GBM_LATE_60M#60min | 3290 | +0.067 | +1115.69€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1221 | +0.083 | +463.82€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1221 | +0.083 | +463.82€ | 1 | 8 |
| ✅ GBM_LATE_60M#ETH | 1055 | +0.072 | +391.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1055 | +0.072 | +391.65€ | 0 | 10 |
| ✅ GBM_LATE_60M#SOL | 1014 | +0.043 | +260.22€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1014 | +0.043 | +260.22€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 545 | -0.246 | -23.88€ | 9 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 545 | -0.246 | -23.88€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 203 | -0.241 | -11.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 203 | -0.241 | -11.96€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 193 | -0.228 | -3.02€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 193 | -0.228 | -3.02€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 149 | -0.268 | -8.90€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 149 | -0.268 | -8.90€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1466 | +0.082 | +390.98€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1466 | +0.082 | +390.98€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 579 | +0.080 | +146.26€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 579 | +0.080 | +146.26€ | 1 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 527 | +0.058 | +84.81€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 527 | +0.058 | +84.81€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 360 | +0.121 | +159.91€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 360 | +0.121 | +159.91€ | 3 | 10 |
| ✅ LATE_WINDOW_5MIN | 161 | +0.273 | +154.25€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 161 | +0.273 | +154.25€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 161 | +0.273 | +154.25€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 161 | +0.273 | +154.25€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3305 | +0.101 | +816.60€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3305 | +0.101 | +816.60€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3305 | +0.101 | +816.60€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3305 | +0.101 | +816.60€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 487 | -0.052 | -23.99€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 487 | -0.052 | -23.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 135 | -0.018 | +0.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 135 | -0.018 | +0.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 87 | -0.073 | -7.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 87 | -0.073 | -7.11€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 184 | -0.005 | -0.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 184 | -0.005 | -0.94€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3623 | +0.016 | +79.12€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3623 | +0.016 | +79.12€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 175 | +0.025 | -1.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 175 | +0.025 | -1.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 750 | +0.012 | +32.91€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 750 | +0.012 | +32.91€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1301 | +0.026 | +30.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1301 | +0.026 | +30.58€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 754 | +0.011 | +0.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 754 | +0.011 | +0.86€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 440 | +0.011 | +21.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 440 | +0.011 | +21.61€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1705 | -0.040 | -26.46€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1705 | -0.040 | -26.46€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 490 | -0.029 | -10.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 490 | -0.029 | -10.06€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 576 | -0.014 | +6.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 576 | -0.014 | +6.58€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 639 | -0.071 | -22.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 639 | -0.071 | -22.98€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8032 | -0.028 | -21.28€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3800 | -0.037 | -89.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4232 | -0.020 | +68.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 234 | -0.042 | -8.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 119 | -0.021 | +0.41€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 115 | -0.064 | -9.04€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2010 | -0.018 | +20.98€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 951 | -0.025 | -6.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1059 | -0.013 | +27.48€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 883 | -0.022 | +15.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 443 | -0.039 | -8.97€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 440 | -0.004 | +24.81€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1739 | -0.043 | -66.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 807 | -0.055 | -59.21€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 932 | -0.032 | -7.65€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1567 | -0.025 | +10.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 745 | -0.038 | -15.83€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 822 | -0.012 | +26.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1599 | -0.030 | +7.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 735 | -0.033 | +0.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 864 | -0.027 | +6.50€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 47549 | -0.001 | +2416.51€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 47549 | -0.001 | +2416.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8557 | +0.026 | +1102.42€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8557 | +0.026 | +1102.42€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6891 | -0.033 | -78.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6891 | -0.033 | -78.08€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 8664 | +0.024 | +898.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 8664 | +0.024 | +898.51€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6726 | -0.047 | -135.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6726 | -0.047 | -135.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8030 | -0.005 | +239.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8030 | -0.005 | +239.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 8681 | +0.014 | +389.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 8681 | +0.014 | +389.76€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6535 | -0.060 | -161.01€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6535 | -0.060 | -161.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1688 | -0.078 | -42.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1688 | -0.078 | -42.51€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 767 | -0.119 | -32.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 767 | -0.119 | -32.24€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1946 | -0.077 | -43.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1946 | -0.077 | -43.03€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 856 | -0.015 | -25.00€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 856 | -0.015 | -25.00€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M | 3367 | +0.004 | -1.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#5min | 3367 | +0.004 | -1.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 131 | -0.034 | -0.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 131 | -0.034 | -0.72€ | 2 | 1 |
| ✅ MOMENTUM_IBS_5M#BTC | 192 | +0.015 | +1.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 192 | +0.015 | +1.02€ | 1 | 1 |
| ✅ MOMENTUM_IBS_5M#DOGE | 139 | -0.004 | -2.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 139 | -0.004 | -2.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 1325 | +0.006 | +6.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 1325 | +0.006 | +6.88€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 1390 | +0.007 | +0.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 1390 | +0.007 | +0.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 190 | -0.010 | -6.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 118290 | -0.075 | +1924.21€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 118290 | -0.075 | +1924.21€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 20523 | -0.076 | +1133.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 20523 | -0.076 | +1133.31€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 17833 | -0.099 | -944.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 17833 | -0.099 | -944.25€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 20820 | -0.067 | +1141.06€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 20820 | -0.067 | +1141.06€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 17377 | -0.096 | -561.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 17377 | -0.096 | -561.27€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 21225 | -0.055 | +371.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 21225 | -0.055 | +371.96€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 20512 | -0.065 | +783.41€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 20512 | -0.065 | +783.41€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8707 | -0.033 | -179.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8707 | -0.033 | -179.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1967 | -0.045 | -23.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1967 | -0.045 | -23.08€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2581 | -0.026 | -41.49€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2581 | -0.026 | -41.49€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1187 | -0.055 | -28.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1187 | -0.055 | -28.62€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 963 | -0.031 | -35.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 963 | -0.031 | -35.02€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1615 | +0.124 | +662.01€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1479 | +0.130 | +649.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 349 | +0.144 | +184.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 349 | +0.144 | +184.49€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 303 | +0.120 | +106.41€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 303 | +0.120 | +106.41€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 294 | +0.135 | +140.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 294 | +0.135 | +140.98€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 261 | +0.150 | +142.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 261 | +0.150 | +142.22€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 272 | +0.095 | +75.32€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 272 | +0.095 | +75.32€ | 0 | 4 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1355 | -0.011 | -1.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1355 | -0.011 | -1.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 265 | +0.006 | +14.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 265 | +0.006 | +14.55€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 234 | -0.004 | +4.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 234 | -0.004 | +4.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 355 | -0.038 | -22.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 355 | -0.038 | -22.44€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 283 | +0.005 | +1.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 283 | +0.005 | +1.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 218 | -0.014 | +0.53€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 218 | -0.014 | +0.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 872 | -0.068 | -36.38€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 406 | -0.110 | -73.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 317 | -0.140 | -64.18€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 310 | -0.029 | +26.51€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 224 | -0.022 | +27.01€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 156 | -0.032 | +11.09€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 126 | -0.039 | +6.19€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 667 | -0.082 | -30.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1092 | -0.207 | -65.69€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 430 | -0.208 | -40.61€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 374 | -0.213 | -40.89€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 371 | -0.216 | -34.19€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 325 | -0.225 | -39.89€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 291 | -0.193 | +9.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 272 | -0.190 | +5.98€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 971 | -0.211 | -74.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 437 | +0.393 | +407.43€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 61 | +0.135 | +49.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 61 | +0.135 | +49.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 107 | +0.362 | +89.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 107 | +0.362 | +89.61€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 269 | +0.459 | +268.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 269 | +0.459 | +268.15€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 437 | +0.393 | +407.43€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 713 | +0.027 | +31.30€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 713 | +0.027 | +31.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 300 | +0.023 | +3.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 300 | +0.023 | +3.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 73 | -0.007 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 73 | -0.007 | +0.78€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 281 | +0.048 | +28.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 281 | +0.048 | +28.80€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3431 | -0.022 | -136.40€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3431 | -0.022 | -136.40€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 589 | -0.028 | -26.63€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 589 | -0.028 | -26.63€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 163 | -0.039 | -13.81€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 163 | -0.039 | -13.81€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1628 | -0.018 | -58.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1628 | -0.018 | -58.44€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 97 | -0.056 | -9.95€ | 4 | 0 |
| ✅ STREAK_FADE_60M#60min | 97 | -0.056 | -9.95€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 40 | -0.071 | -3.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 40 | -0.071 | -3.54€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 57 | -0.042 | -6.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 57 | -0.042 | -6.41€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10624 | +0.017 | +96.67€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10624 | +0.017 | +96.67€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2706 | +0.020 | +27.01€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2706 | +0.020 | +27.01€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2744 | +0.021 | +41.04€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2744 | +0.021 | +41.04€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2887 | +0.009 | -1.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2887 | +0.009 | -1.49€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2287 | +0.019 | +30.11€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2287 | +0.019 | +30.11€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9674 | +0.014 | -43.18€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9674 | +0.014 | -43.18€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3898 | +0.018 | -6.93€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3898 | +0.018 | -6.93€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3612 | +0.011 | -27.24€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3612 | +0.011 | -27.24€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2164 | +0.011 | -9.01€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2164 | +0.011 | -9.01€ | 1 | 0 |
| ✅ UPDOWN_GBM | 73642 | +0.053 | +6468.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 18458 | +0.083 | +4074.78€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2383 | +0.005 | +22.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 48249 | +0.049 | +2289.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4295 | +0.008 | +82.23€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 15474 | +0.055 | +1325.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2344 | +0.090 | +583.01€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 632 | +0.011 | +10.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 10495 | +0.060 | +673.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1910 | +0.004 | +55.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 93 | -0.068 | +3.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8267 | +0.067 | +867.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6634 | +0.049 | +258.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 16668 | +0.044 | +1068.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4308 | +0.064 | +623.91€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 618 | +0.006 | +15.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10164 | +0.043 | +407.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1492 | +0.013 | +19.16€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 86 | -0.102 | +2.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 16187 | +0.032 | +763.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4552 | +0.034 | +371.91€ | 0 | 4 |
| ✅ UPDOWN_GBM#SOL#240min | 590 | -0.007 | -0.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10076 | +0.036 | +389.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 893 | +0.007 | +7.21€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 76 | -0.128 | -4.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10193 | +0.063 | +1370.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4123 | +0.101 | +1186.91€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5682 | +0.038 | +183.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 255 | -0.099 | +1.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 810 | +0.364 | +295.94€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 810 | +0.364 | +295.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 423 | +0.366 | +149.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 423 | +0.366 | +149.18€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 387 | +0.361 | +146.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 387 | +0.361 | +146.76€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19383 | -0.024 | +4610.54€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19383 | -0.024 | +4610.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3381 | -0.110 | +156.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3381 | -0.110 | +156.68€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2317 | +0.218 | +1523.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2317 | +0.218 | +1523.09€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5530 | -0.066 | +666.86€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5530 | -0.066 | +666.86€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5489 | -0.064 | +990.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5489 | -0.064 | +990.64€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 218 | +0.032 | +7.39€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 218 | +0.032 | +7.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 218 | +0.032 | +7.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 218 | +0.032 | +7.39€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1378 | +0.291 | +1170.69€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1378 | +0.291 | +1170.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 742 | +0.289 | +599.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 742 | +0.289 | +599.82€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 636 | +0.293 | +570.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 636 | +0.293 | +570.87€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 811 | -0.111 | -82.42€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#5min | 811 | -0.111 | -82.42€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 247 | -0.078 | -17.59€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 247 | -0.078 | -17.59€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 87 | -0.163 | -9.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 87 | -0.163 | -9.15€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 94 | -0.188 | -6.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 94 | -0.188 | -6.32€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3492 | +0.305 | +1688.36€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1275 | +0.259 | +171.66€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1341 | +0.299 | +608.27€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 876 | +0.379 | +908.42€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.018 n=913 — no justifica filtro, seguir monitorizando
  - _Datos_: n=913 IC=+0.018 PNL=+31.94€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 705 celda(s) pasan gate riguroso completo de 2658 evaluadas (n>=40) y 3686 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=4552 IC=+0.034 PNL=+371.91€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1341/15 IC=+0.299 PNL=+608.27€ | BTC: n=1275/15 IC=+0.259 PNL=+171.66€ | SOL: n=876/15 IC=+0.379 PNL=+908.42€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.137 n=763/60 | contraria IC=+0.191 n=791 | gap=-0.054 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=446, boost estimado=+0.014. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1490/40 IC=+0.012 PNL=+17.74€ | BTC#60min: n=1909/40 IC=+0.003 PNL=+55.12€ | SOL#60min: n=893/40 IC=+0.007 PNL=+7.21€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=533622 | tras_1loss IC=+0.094 n=406398 | tras_2loss IC=+0.063 n=164898/40 | gap=-0.016 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.203 > 0.08 con n=713 PNL=+554.82€
  - _Datos_: n=713 IC=+0.203 PNL=+554.82€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=801 PNL=+474.59€
  - _Datos_: n=801 IC=+0.175 PNL=+474.59€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.177 > 0.08 con n=60 PNL=+33.31€
  - _Datos_: n=60 IC=+0.177 PNL=+33.31€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=2851 PNL=+1610.74€
  - _Datos_: n=2851 IC=+0.335 PNL=+1610.74€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=635 IC=+0.075 PNL=+73.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=635 IC=+0.075 PNL=+73.77€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=80 IC=+0.183 PNL=+53.17€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=80 IC=+0.183 PNL=+53.17€

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
  - _Estado_: n=2891 IC=+0.005 PNL=-3.98€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2891 IC=+0.005 PNL=-3.98€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1401 IC=+0.012 PNL=+84.05€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1401 IC=+0.012 PNL=+84.05€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=913 IC=+0.018 PNL=+31.94€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=913 IC=+0.018 PNL=+31.94€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.1 con n=4579 PNL=+2924.74€
  - _Datos_: n=4579 IC=+0.180 PNL=+2924.74€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2342 IC=+0.090 PNL=+580.72€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2342 IC=+0.090 PNL=+580.72€

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
  - _Estado_: n=945 IC=+0.035 PNL=+91.03€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=945 IC=+0.035 PNL=+91.03€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=113 IC=+0.013 PNL=+1.56€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=113 IC=+0.013 PNL=+1.56€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.273 n=161) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=161 IC=+0.273 PNL=+154.25€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.02 con n=933 PNL=+407.20€
  - _Datos_: n=933 IC=+0.130 PNL=+407.20€

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
  - _Estado_: n=28652 IC=+0.073 PNL=+4152.27€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=28652 IC=+0.073 PNL=+4152.27€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.141 < -0.1 con n=455 PNL=+52.38€
  - _Datos_: n=455 IC=-0.141 PNL=+52.38€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3057 IC=+0.066 PNL=+372.70€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3057 IC=+0.066 PNL=+372.70€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=136 IC=-0.094 PNL=+5.06€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=136 IC=-0.094 PNL=+5.06€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.1 con n=762 PNL=+209.42€
  - _Datos_: n=762 IC=+0.111 PNL=+209.42€

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
  - _Estado_: n=30551 IC=-0.134 PNL=+2348.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=30551 IC=-0.134 PNL=+2348.82€

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
  - _Estado_: n=3084 IC=+0.133 PNL=+1872.00€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3084 IC=+0.133 PNL=+1872.00€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=7555 IC=+0.049 PNL=+587.51€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7555 IC=+0.049 PNL=+587.51€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.092 > 0.08 con n=3314 PNL=+1772.29€
  - _Datos_: n=3314 IC=+0.092 PNL=+1772.29€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.223 < -0.1 con n=3144 PNL=-247.70€
  - _Datos_: n=3144 IC=-0.223 PNL=-247.70€

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
  - _Estado_: n=66 IC=+0.000 PNL=+4.12€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=66 IC=+0.000 PNL=+4.12€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.102 n=1681) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1681 IC=+0.102 PNL=+373.86€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.415 n=560) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=560 IC=+0.415 PNL=+809.80€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=13453 IC=+0.184 PNL=-1401.29€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=13453 IC=+0.184 PNL=-1401.29€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.212 > 0.1 con n=220 PNL=+139.50€
  - _Datos_: n=220 IC=+0.212 PNL=+139.50€
