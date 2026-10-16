# Hipótesis automáticas — 2026-10-16 15:32 UTC
_Generado por shadow_postmortem.py sobre 925431 resoluciones (PNL=+118909.86€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.261 (n=178)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=606)

- **PATRÓN** `py_entrada` > `0.7` → IC=+0.276 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.7 (IC base=+0.139)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.193 (n=265)

  - _Acción_: Kelly boost +0.96€ cuando `n_total_lado` > 67.0 (IC base=+0.139)

- **PATRÓN** `banda_hit_calibrado` > `0.8011` → IC=+0.277 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8011 (IC base=+0.139)

- **PATRÓN** `banda_z` > `9.461` → IC=+0.202 (n=260)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.461 (IC base=+0.139)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.727` → IC=+0.140 (n=697)

  - _Acción_: Kelly boost +0.70€ cuando `ballenas_wallet_edge_medio` > 0.727 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.180 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 17.0 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.157 (n=843)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.139)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.73` → IC=+0.288 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.146)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.212 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.146)

- **PATRÓN** `banda_hit_calibrado` > `0.6183` → IC=+0.272 (n=433)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6183 (IC base=+0.146)

- **PATRÓN** `banda_z` > `9.932` → IC=+0.232 (n=218)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.932 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.198 (n=223)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.146)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=745)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.154 (n=388)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 103.0 (IC base=+0.146)

### BALLENAS_CONFIRMADAS_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.355` → IC=-0.203 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.355
  - _Potencial_: sin este filtro IC_bueno=+0.236 (n=108)

- **FILTRO** `banda_hit_calibrado` < `0.8028` → IC=-0.133 (n=47)

  - _Acción_: SKIP cuando `banda_hit_calibrado` < 0.8028
  - _Potencial_: sin este filtro IC_bueno=+0.255 (n=96)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.186 (n=116)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.353 (n=32)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=102)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.157 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=101)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=117)

- **PATRÓN** `py_entrada` > `0.355` → IC=+0.236 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.355 (IC base=+0.128)

- **PATRÓN** `banda_hit_calibrado` > `0.8028` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8028 (IC base=+0.128)

- **PATRÓN** `banda_z` > `7.17` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `banda_z` > 7.17 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.132 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 4.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.140 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 14.0 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `906.0197` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 906.0197 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `79.0` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 79.0 (IC base=+0.128)

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
- **FILTRO** `restante_s_al_confirmar` < `143.42` → IC=-0.203 (n=9645)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.42
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=28937)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `122.6` → IC=-0.288 (n=1057)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 122.6
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3171)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.44` → IC=-0.208 (n=2515)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.44
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=7547)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `132.99` → IC=-0.283 (n=1877)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 132.99
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=5633)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.211 (n=20518)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=4199)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `9265.6556` → IC=+0.178 (n=1887)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9265.6556 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=17302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=21040)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.225 (n=16063)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=6986)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7220.7864` → IC=+0.160 (n=2693)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7220.7864 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=1990)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.195 (n=1950)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2443)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `libro_liquidez` > `16324.3347` → IC=+0.201 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16324.3347 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.193 (n=1749)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.191 (n=1955)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=2502)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `16119.9456` → IC=+0.196 (n=645)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 16119.9456 (IC base=+0.187)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=451)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.61 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `6869.1866` → IC=+0.175 (n=121)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6869.1866 (IC base=+0.082)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.138 (n=1069)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.44 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.166 (n=3989)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.159 (n=2728)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 12.0 (IC base=+0.159)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.370 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.222 (n=1774)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.360 (n=654)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.217 (n=2077)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.145 (n=857)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 15.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.259 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.139)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.140 (n=781)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `1852.1782` → IC=+0.146 (n=637)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 1852.1782 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4449.086` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4449.086 (IC base=+0.072)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.243 (n=931)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.411 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=1276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=844)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.148)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.160 (n=425)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.256 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.127)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=17238)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=14691)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=7139)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=3996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.178 (n=3792)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 17.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3886)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.176)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **FILTRO** `libro_liquidez` < `9614.35` → IC=-0.328 (n=56)

  - _Acción_: SKIP cuando `libro_liquidez` < 9614.35
  - _Potencial_: sin este filtro IC_bueno=-0.224 (n=56)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.225 (n=1948)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=1300)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.313 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.225)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=3928)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.185 (n=3356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.186 (n=3090)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.181)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3416)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.247)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.351 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.78 (IC base=+0.247)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.306 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.247)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=3851)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=2469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.198 (n=1325)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.432 (n=744)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.431 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `7390.2621` → IC=+0.443 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7390.2621 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.449 (n=194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `18390.1556` → IC=+0.440 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18390.1556 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.446 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `4387.5246` → IC=+0.439 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4387.5246 (IC base=+0.430)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.406 (n=137)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.404)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.404 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.404)

- **PATRÓN** `py_entrada` > `0.91` → IC=+0.410 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.91 (IC base=+0.404)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.77` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.77
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=22159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=22493)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=8867)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.189 (n=7135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=9942)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.225 (n=4579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.284 (n=3247)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.188 (n=3792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=7121)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=9506)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=4667)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=3574)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.276 (n=3178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=8552)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=3679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=3749)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=3867)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=8050)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.137 (n=7947)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.41` → IC=+0.136 (n=7380)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.41 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=3987)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` < `4.19` → IC=+0.127 (n=3689)

  - _Acción_: Kelly boost +0.63€ cuando `restante_min` < 4.19 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.140 (n=4028)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.129 (n=4865)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.8` → IC=+0.144 (n=3665)

  - _Acción_: Kelly boost +0.72€ cuando `lag_apertura_s` < 2.8 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=4063)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=4339)

  - _Acción_: Kelly boost +0.66€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.26` → IC=+0.135 (n=3736)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 2.26 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=1574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.290 (n=1333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.376 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.290)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=712)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.280 (n=616)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.347 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5399.1782` → IC=+0.290 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5399.1782 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.297 (n=751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.386 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `1733.724` → IC=+0.302 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1733.724 (IC base=+0.292)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.444 (n=731)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.440)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.439 (n=606)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.440)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=721)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.440)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.444 (n=498)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.440)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.440)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=348)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.441 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.442 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.451 (n=343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.446)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.446)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.448 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.446)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.447 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.446)

- **PATRÓN** `libro_liquidez` > `2138.537` → IC=+0.454 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2138.537 (IC base=+0.446)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4792` → IC=+0.135 (n=12476)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.67€ cuando `drift_60min` |x|≤ 0.4792 (IC base=+0.118)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.122 (n=8744)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 12.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` > `0.9809` → IC=+0.245 (n=4158)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9809 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` > `0.7924` → IC=+0.266 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7924 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.3721` → IC=+0.253 (n=3416)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3721 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.969` → IC=+0.188 (n=4713)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.969 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.2057` → IC=+0.253 (n=3589)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2057 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.259 (n=3588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.302` → IC=+0.233 (n=1265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.302 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.3388` → IC=+0.224 (n=4011)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3388 (IC base=+0.118)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.121 (n=10655)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.5676` → IC=+0.141 (n=15384)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5676 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1541` → IC=+0.185 (n=5511)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1541 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.179 (n=5934)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` < 1.1913 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.0503` → IC=+0.180 (n=2690)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0503 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.230 (n=1474)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.6645` → IC=+0.204 (n=3365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6645 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `110.0` → IC=+0.218 (n=9947)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 110.0 (IC base=+0.074)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.214 (n=915)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.349` → IC=+0.197 (n=2733)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.349 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=1316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.197 (n=1836)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 11.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `0.9762` → IC=+0.275 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9762 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.076` → IC=+0.283 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.076 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.242 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.2813` → IC=+0.206 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2813 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.205 (n=2888)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `2090.52` → IC=+0.212 (n=911)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2090.52 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.204 (n=2118)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.237 (n=2281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.233)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.236 (n=1039)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.0888` → IC=+0.262 (n=761)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0888 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.258 (n=828)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.5164` → IC=+0.255 (n=2281)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5164 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.764` → IC=+0.234 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.764 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` < `0.0939` → IC=+0.235 (n=2032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0939 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.250 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.234 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.6474` → IC=+0.243 (n=715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6474 (IC base=+0.233)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.236 (n=2534)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `1575.869` → IC=+0.243 (n=2280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1575.869 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.234 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.233)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.240 (n=984)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.224)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.225 (n=1012)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.1081` → IC=+0.256 (n=982)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1081 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=2343)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `0.2936` → IC=+0.240 (n=2231)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2936 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` > `0.1292` → IC=+0.233 (n=1236)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1292 (IC base=+0.224)

- **PATRÓN** `dist_vwap_pct` < `0.341` → IC=+0.225 (n=2133)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.341 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.408` → IC=+0.265 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.408 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` < `1.2347` → IC=+0.226 (n=2231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2347 (IC base=+0.224)

- **PATRÓN** `volumen_regimen` > `0.6225` → IC=+0.229 (n=2231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6225 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.251 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.5114` → IC=+0.225 (n=967)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5114 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.429` → IC=+0.251 (n=733)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.429 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.151 (n=2276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0761` → IC=+0.169 (n=759)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0761 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=861)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7307` → IC=+0.177 (n=2275)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` < 0.7307 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.1323` → IC=+0.156 (n=2101)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1323 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.086` → IC=+0.153 (n=367)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.086 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.229` → IC=+0.141 (n=2085)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.229 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.142 (n=2275)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1913 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.163 (n=618)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4453` → IC=+0.141 (n=2157)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4453 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4152` → IC=+0.137 (n=2157)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4152 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.168 (n=917)

  - _Acción_: Kelly boost +0.84€ cuando `ballena_activa_n` < 220.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.212 (n=1282)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=2963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 5.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=2539)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=1078)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.345` → IC=+0.269 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.345 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.0979` → IC=+0.196 (n=2493)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0979 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.3511` → IC=+0.213 (n=367)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3511 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.6894` → IC=+0.208 (n=1240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6894 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=3352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `1992.72` → IC=+0.202 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1992.72 (IC base=+0.192)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.222 (n=2217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.6073` → IC=+0.220 (n=2518)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6073 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.0095` → IC=+0.272 (n=841)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0095 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.515` → IC=+0.253 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.515 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.3479` → IC=+0.254 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3479 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.7248` → IC=+0.215 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7248 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `2.7242` → IC=+0.226 (n=1081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7242 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2069.52` → IC=+0.229 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2069.52 (IC base=+0.216)

- **PATRÓN** `ballena_activa_n` < `26.0` → IC=+0.216 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 26.0 (IC base=+0.216)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.139 (n=142)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=3419)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.159 (n=508)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0036 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.9552` → IC=+0.224 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9552 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1359` → IC=+0.323 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1359 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.7526` → IC=+0.328 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7526 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.086` → IC=+0.185 (n=1090)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 5.086 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` < `0.8577` → IC=+0.330 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8577 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.347 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2251 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` < `0.1741` → IC=+0.320 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1741 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.2965` → IC=+0.340 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2965 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `1.4081` → IC=+0.337 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4081 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.319 (n=247)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.331 (n=488)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0953` → IC=+0.170 (n=891)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.0953 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.3253` → IC=+0.140 (n=443)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.3253 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1302` → IC=+0.135 (n=1402)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1302 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8486` → IC=+0.146 (n=1035)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8486 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2847` → IC=+0.198 (n=200)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2847 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `1.5114` → IC=+0.145 (n=1326)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.5114 (IC base=+0.034)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.170 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=516)

- **FILTRO** `ibs_20min` < `0.2857` → IC=-0.195 (n=152)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2857
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=456)

- **FILTRO** `ibs_20min` > `0.2203` → IC=-0.132 (n=3372)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2203
  - _Potencial_: sin este filtro IC_bueno=+0.151 (n=1663)

- **FILTRO** `sigma_ewma_delta_pct` > `8.685` → IC=-0.235 (n=522)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.685
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4513)

- **PATRÓN** `ibs_20min` > `0.7913` → IC=+0.189 (n=207)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.7913 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `1.0161` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0161 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` < `0.4558` → IC=+0.253 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4558 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.37` → IC=+0.139 (n=214)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 2.37 (IC base=+0.033)

- **PATRÓN** `volumen_regimen` > `0.9772` → IC=+0.294 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9772 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` < `0.0815` → IC=+0.269 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0815 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.276 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.033)

- **PATRÓN** `volumen_spike_ratio` > `1.5401` → IC=+0.251 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5401 (IC base=+0.033)

- **PATRÓN** `ibs_20min` < `0.2203` → IC=+0.151 (n=1663)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.2203 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.1923` → IC=+0.276 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1923 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4351` → IC=+0.272 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4351 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.7066` → IC=+0.299 (n=301)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7066 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.307 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4034` → IC=+0.299 (n=620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4034 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6259` → IC=-0.179 (n=901)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6259
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=2711)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.161 (n=913)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=2699)

- **FILTRO** `ibs_20min` > `0.7549` → IC=-0.203 (n=1320)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7549
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=3964)

- **PATRÓN** `dist_vwap_pct` > `0.7472` → IC=+0.331 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7472 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` < `0.2594` → IC=+0.298 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2594 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` < `1.1432` → IC=+0.296 (n=600)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1432 (IC base=-0.070)

- **PATRÓN** `volumen_regimen` > `0.7048` → IC=+0.309 (n=536)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7048 (IC base=-0.070)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.299 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.321 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=-0.070)

- **PATRÓN** `volumen_spike_ratio` > `1.8466` → IC=+0.296 (n=386)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8466 (IC base=-0.070)

- **PATRÓN** `dist_vwap_pct` > `0.8089` → IC=+0.274 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8089 (IC base=-0.008)

- **PATRÓN** `volumen_regimen` > `1.0723` → IC=+0.280 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0723 (IC base=-0.008)

- **PATRÓN** `volumen_pendiente_norm` > `0.1027` → IC=+0.274 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1027 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` < `2.1684` → IC=+0.260 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1684 (IC base=-0.008)

- **PATRÓN** `volumen_spike_ratio` > `1.424` → IC=+0.257 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.424 (IC base=-0.008)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.207 (n=5495)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.097)

- **PATRÓN** `ibs_20min` > `0.884` → IC=+0.279 (n=7467)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.884 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.9631` → IC=+0.299 (n=1248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9631 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.645` → IC=+0.159 (n=7382)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.645 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` < `1.1729` → IC=+0.258 (n=6066)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1729 (IC base=+0.097)

- **PATRÓN** `volumen_regimen` > `0.6894` → IC=+0.263 (n=5417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6894 (IC base=+0.097)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.272 (n=1812)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.097)

- **PATRÓN** `volumen_spike_ratio` > `2.2649` → IC=+0.265 (n=4399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2649 (IC base=+0.097)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.289 (n=9274)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.162 (n=5299)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0092 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.6613` → IC=+0.144 (n=15879)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6613 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2425` → IC=+0.261 (n=4888)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2425 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1947` → IC=+0.265 (n=1659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1947 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.293` → IC=+0.314 (n=1047)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.293 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.4547` → IC=+0.287 (n=2363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4547 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2619` → IC=+0.280 (n=3214)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2619 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.290 (n=7001)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3707` → IC=-0.171 (n=1501)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3707
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=3050)

- **FILTRO** `ibs_20min` > `0.7455` → IC=-0.206 (n=950)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7455
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=2851)

- **FILTRO** `sigma_ewma_delta_pct` > `4.508` → IC=-0.200 (n=830)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.508
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2971)

- **PATRÓN** `ibs_20min` > `0.9124` → IC=+0.299 (n=1138)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9124 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.07` → IC=+0.211 (n=804)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.07 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.294 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `1.4484` → IC=+0.231 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4484 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` > `2.2425` → IC=+0.266 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2425 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.267 (n=998)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.1596` → IC=+0.160 (n=951)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1596 (IC base=-0.027)

- **PATRÓN** `volumen_pendiente_norm` < `0.0733` → IC=+0.411 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0733 (IC base=-0.027)

- **PATRÓN** `volumen_spike_ratio` < `2.4877` → IC=+0.401 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4877 (IC base=-0.027)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.398 (n=409)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.027)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1138` → IC=+0.210 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1138 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` < `1.1952` → IC=+0.184 (n=1600)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 1.1952 (IC base=+0.025)

- **PATRÓN** `volumen_regimen` > `0.6821` → IC=+0.194 (n=1430)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_regimen` > 0.6821 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2732` → IC=+0.216 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2732 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` < `1.425` → IC=+0.210 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.425 (IC base=+0.025)

- **PATRÓN** `volumen_spike_ratio` > `2.4515` → IC=+0.191 (n=526)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.4515 (IC base=+0.025)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.234 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 220.0 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.1112` → IC=+0.231 (n=1008)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1112 (IC base=+0.001)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.235 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=+0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2701` → IC=+0.303 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2701 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5351` → IC=+0.231 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5351 (IC base=+0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.1623` → IC=+0.250 (n=438)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1623 (IC base=+0.001)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.303 (n=810)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.267 (n=2549)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.262)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.262 (n=2183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.308 (n=1267)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.296 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.274 (n=2102)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `1.6102` → IC=+0.268 (n=2338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6102 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.273 (n=2863)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1982.0608` → IC=+0.284 (n=1100)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.0608 (IC base=+0.262)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.329 (n=945)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.1824` → IC=+0.306 (n=915)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1824 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.323 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.3659` → IC=+0.293 (n=2078)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3659 (IC base=+0.290)

- **PATRÓN** `ibs_20min` > `0.1124` → IC=+0.294 (n=1385)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1124 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.67` → IC=+0.310 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.67 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.1965` → IC=+0.288 (n=2022)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1965 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.3399` → IC=+0.310 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3399 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.7195` → IC=+0.298 (n=871)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7195 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` > `2.6449` → IC=+0.296 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6449 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `2061.7984` → IC=+0.313 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2061.7984 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.286 (n=1305)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.290)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7408` → IC=-0.183 (n=984)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7408
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=2953)

- **PATRÓN** `ibs_20min` > `0.8855` → IC=+0.172 (n=927)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8855 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.229 (n=706)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3691` → IC=+0.227 (n=1238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3691 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `1.0113` → IC=+0.242 (n=1130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0113 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.1635` → IC=+0.232 (n=1361)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1635 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1024` → IC=+0.246 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1024 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.3944` → IC=+0.245 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3944 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` > `2.134` → IC=+0.233 (n=563)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.134 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.261 (n=1109)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3327` → IC=+0.229 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3327 (IC base=-0.001)

- **PATRÓN** `volumen_regimen` < `1.041` → IC=+0.234 (n=771)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.041 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.246 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=-0.001)

- **PATRÓN** `volumen_pendiente_norm` > `0.2887` → IC=+0.286 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2887 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` < `1.5259` → IC=+0.271 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5259 (IC base=-0.001)

- **PATRÓN** `volumen_spike_ratio` > `2.4508` → IC=+0.259 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4508 (IC base=-0.001)

- **PATRÓN** `ballena_activa_n` < `126.0` → IC=+0.254 (n=838)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 126.0 (IC base=-0.001)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7632` → IC=-0.206 (n=1740)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7632
  - _Potencial_: sin este filtro IC_bueno=+0.302 (n=1743)

- **FILTRO** `ibs_20min` > `0.6522` → IC=-0.237 (n=855)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6522
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=2582)

- **FILTRO** `sigma_ewma_delta_pct` > `8.569` → IC=-0.242 (n=393)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.569
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=3044)

- **PATRÓN** `ibs_20min` > `0.7632` → IC=+0.302 (n=1743)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7632 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.336 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.608` → IC=+0.172 (n=544)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.608 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.331 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8471 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `0.6283` → IC=+0.319 (n=1316)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6283 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.318 (n=1362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.355 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.342 (n=428)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.334 (n=1277)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.5517` → IC=+0.142 (n=2269)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.5517 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.4547` → IC=+0.250 (n=1184)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4547 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.7092` → IC=+0.262 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7092 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.242 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.0733` → IC=+0.260 (n=418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0733 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.4223` → IC=+0.253 (n=1065)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4223 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.271 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.030)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.342 (n=1665)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.312 (n=895)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.297)

- **PATRÓN** `ibs_20min` > `0.6511` → IC=+0.329 (n=1864)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6511 (IC base=+0.297)

- **PATRÓN** `dist_vwap_pct` > `0.2113` → IC=+0.326 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2113 (IC base=+0.297)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.795` → IC=+0.318 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.795 (IC base=+0.297)

- **PATRÓN** `volumen_regimen` > `0.6279` → IC=+0.307 (n=1865)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6279 (IC base=+0.297)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.343 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.297)

- **PATRÓN** `volumen_spike_ratio` > `1.4235` → IC=+0.309 (n=1785)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4235 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `2473.0926` → IC=+0.310 (n=1665)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2473.0926 (IC base=+0.297)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.331 (n=1589)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.297)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.331 (n=1317)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.298)

- **PATRÓN** `drift_60min` |x|≤ `0.1888` → IC=+0.301 (n=869)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.312 (n=768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.298)

- **PATRÓN** `ibs_20min` < `0.3679` → IC=+0.324 (n=1975)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3679 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.3125` → IC=+0.300 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3125 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` < `0.2282` → IC=+0.302 (n=1853)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2282 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.541` → IC=+0.310 (n=731)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.541 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.039` → IC=+0.300 (n=2349)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.039 (IC base=+0.298)

- **PATRÓN** `volumen_regimen` < `0.7186` → IC=+0.302 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7186 (IC base=+0.298)

- **PATRÓN** `volumen_regimen` > `1.2246` → IC=+0.329 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2246 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` > `0.2304` → IC=+0.348 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2304 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.308 (n=602)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` > `2.1317` → IC=+0.300 (n=818)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1317 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `2428.9954` → IC=+0.301 (n=1765)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2428.9954 (IC base=+0.298)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.183 (n=4043)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0048 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.222 (n=4037)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.3477` → IC=+0.189 (n=10646)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.3477 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.189 (n=12574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.233 (n=12099)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.56 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1667` → IC=+0.208 (n=5025)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1667 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.353` → IC=+0.257 (n=2388)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.353 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1944` → IC=+0.169 (n=8026)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1944 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.203 (n=1768)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.5976` → IC=+0.189 (n=3906)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.5976 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2009.7484` → IC=+0.184 (n=10806)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2009.7484 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `97.0` → IC=+0.196 (n=11013)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 97.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.186 (n=7792)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0069 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.0804` → IC=+0.223 (n=3890)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0804 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=4369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.234 (n=11735)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.1753` → IC=+0.173 (n=8212)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1753 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.114` → IC=+0.196 (n=1919)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.114 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.734` → IC=+0.178 (n=10265)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 2.734 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1804` → IC=+0.162 (n=8329)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1804 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2919` → IC=+0.226 (n=1715)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2919 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.6217` → IC=+0.186 (n=3643)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6217 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.189 (n=10649)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 102.0 (IC base=+0.177)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.234 (n=678)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.3326` → IC=+0.226 (n=2026)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3326 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=2129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.217 (n=1371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.9247` → IC=+0.291 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9247 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.138` → IC=+0.332 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.138 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2806` → IC=+0.270 (n=306)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2806 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `2.2559` → IC=+0.219 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2559 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=2160)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2092.77` → IC=+0.221 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2092.77 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.0079` → IC=+0.245 (n=1585)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0079 (IC base=+0.243)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.248 (n=720)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.0973` → IC=+0.291 (n=697)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0973 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.247 (n=1612)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.247 (n=777)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.0105` → IC=+0.295 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0105 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` < `0.1002` → IC=+0.244 (n=1376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1002 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2973` → IC=+0.279 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2973 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.4351` → IC=+0.263 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4351 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `2.67` → IC=+0.246 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.67 (IC base=+0.243)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.247 (n=1766)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `1557.0938` → IC=+0.254 (n=1584)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1557.0938 (IC base=+0.243)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.243 (n=539)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.243)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.220 (n=608)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.157)

- **PATRÓN** `drift_60min` |x|≤ `0.1622` → IC=+0.186 (n=1215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.1622 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.173 (n=1923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.157)

- **PATRÓN** `ibs_20min` > `0.3506` → IC=+0.225 (n=1822)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3506 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` > `0.1368` → IC=+0.217 (n=1124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1368 (IC base=+0.157)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.442` → IC=+0.228 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.442 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` < `0.6929` → IC=+0.172 (n=802)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_regimen` < 0.6929 (IC base=+0.157)

- **PATRÓN** `volumen_regimen` > `1.0696` → IC=+0.158 (n=826)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` > 1.0696 (IC base=+0.157)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.185 (n=290)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` < `1.5121` → IC=+0.173 (n=785)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 1.5121 (IC base=+0.157)

- **PATRÓN** `volumen_spike_ratio` > `2.4856` → IC=+0.163 (n=595)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` > 2.4856 (IC base=+0.157)

- **PATRÓN** `ballena_activa_n` < `424.0` → IC=+0.161 (n=1745)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 424.0 (IC base=+0.157)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=1921)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.3016` → IC=+0.164 (n=1918)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.3016 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.186 (n=728)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6113` → IC=+0.204 (n=1918)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6113 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.581` → IC=+0.203 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.581 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.160 (n=1918)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2024 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0933` → IC=+0.145 (n=1614)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.0933 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1578` → IC=+0.147 (n=590)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1578 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4911` → IC=+0.150 (n=1799)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4911 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.146 (n=1799)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4236 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.173 (n=579)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 204.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0106` → IC=+0.237 (n=930)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0106 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3972` → IC=+0.224 (n=1800)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3972 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1058)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.514` → IC=+0.296 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.514 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.230 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.7699` → IC=+0.213 (n=870)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7699 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.6928` → IC=+0.228 (n=897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6928 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=2423)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1982.8952` → IC=+0.223 (n=927)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1982.8952 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.246 (n=1544)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.2545` → IC=+0.260 (n=1171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2545 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.282 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.3548` → IC=+0.251 (n=1755)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3548 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.616` → IC=+0.276 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.616 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3546` → IC=+0.272 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3546 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7279` → IC=+0.237 (n=735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7279 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.7347` → IC=+0.239 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7347 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2066.3805` → IC=+0.248 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2066.3805 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.228 (n=741)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.233)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.173 (n=1957)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0075 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.4075` → IC=+0.167 (n=1957)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4075 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.163 (n=2034)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3126` → IC=+0.210 (n=1956)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3126 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.1409` → IC=+0.197 (n=1224)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1409 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.884` → IC=+0.201 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.884 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `1.0344` → IC=+0.156 (n=1722)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0344 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.1017` → IC=+0.177 (n=807)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1017 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `1.5337` → IC=+0.152 (n=844)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5337 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `2.5011` → IC=+0.165 (n=640)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5011 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `4796.7576` → IC=+0.195 (n=1304)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 4796.7576 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `143.0` → IC=+0.159 (n=1905)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 143.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0071` → IC=+0.155 (n=2061)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0071 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3957` → IC=+0.145 (n=2061)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.3957 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=778)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6846` → IC=+0.187 (n=2061)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6846 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1544` → IC=+0.154 (n=2042)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1544 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.865` → IC=+0.156 (n=718)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 6.865 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8585` → IC=+0.158 (n=1374)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8585 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.198 (n=309)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.134 (n=1284)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.7982 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5302` → IC=+0.132 (n=642)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` > 2.5302 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7857.911` → IC=+0.187 (n=934)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 7857.911 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `119.0` → IC=+0.130 (n=1655)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 119.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.129 (n=739)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.006 (IC base=+0.127)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.171 (n=1002)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0102 (IC base=+0.127)

- **PATRÓN** `drift_60min` |x|≤ `0.4428` → IC=+0.129 (n=1944)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4428 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.127)

- **PATRÓN** `ibs_20min` > `0.4889` → IC=+0.215 (n=2209)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4889 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1964` → IC=+0.191 (n=1313)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1964 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.679` → IC=+0.270 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.679 (IC base=+0.127)

- **PATRÓN** `volumen_regimen` < `1.1842` → IC=+0.142 (n=2209)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1842 (IC base=+0.127)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.136 (n=2242)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.127)

- **PATRÓN** `volumen_spike_ratio` < `1.4354` → IC=+0.146 (n=716)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4354 (IC base=+0.127)

- **PATRÓN** `libro_liquidez` > `2849.939` → IC=+0.211 (n=1002)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2849.939 (IC base=+0.127)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.157 (n=684)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 20.0 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.138 (n=2260)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0107 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.171 (n=754)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5918` → IC=+0.219 (n=2259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5918 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.2006` → IC=+0.148 (n=2109)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2006 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.964` → IC=+0.125 (n=347)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 8.964 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.51` → IC=+0.127 (n=1991)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 2.51 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.174` → IC=+0.129 (n=2259)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.174 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2744` → IC=+0.153 (n=298)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` > 0.2744 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4479` → IC=+0.129 (n=699)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4479 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.4234` → IC=+0.138 (n=699)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4234 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2693.1185` → IC=+0.191 (n=1024)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2693.1185 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.126 (n=2065)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 50.0 (IC base=+0.119)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.243 (n=1822)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.1289` → IC=+0.235 (n=680)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1289 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=2117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.226 (n=1384)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.219)

- **PATRÓN** `ibs_20min` > `0.656` → IC=+0.255 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.656 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.1903` → IC=+0.226 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1903 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` < `0.4878` → IC=+0.221 (n=1802)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4878 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.611` → IC=+0.251 (n=928)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.611 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` < `1.1809` → IC=+0.222 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1809 (IC base=+0.219)

- **PATRÓN** `volumen_regimen` > `0.6223` → IC=+0.225 (n=2041)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6223 (IC base=+0.219)

- **PATRÓN** `volumen_pendiente_norm` > `0.2826` → IC=+0.268 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2826 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` < `2.461` → IC=+0.226 (n=1987)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.461 (IC base=+0.219)

- **PATRÓN** `volumen_spike_ratio` > `1.7991` → IC=+0.230 (n=1324)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7991 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2653)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `2645.2402` → IC=+0.229 (n=1360)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2645.2402 (IC base=+0.219)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.236 (n=921)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.236 (n=951)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.0902` → IC=+0.260 (n=698)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0902 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1018)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` < `0.425` → IC=+0.254 (n=2094)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.425 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.2961` → IC=+0.234 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2961 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.33` → IC=+0.251 (n=400)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.33 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6412` → IC=+0.234 (n=2094)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6412 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.280 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `1.434` → IC=+0.226 (n=1942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.434 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `2399.3806` → IC=+0.230 (n=1870)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2399.3806 (IC base=+0.225)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.207 (n=1368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.178)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.187 (n=1034)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0088 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.13` → IC=+0.200 (n=1365)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.13 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.211 (n=1524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.7297` → IC=+0.230 (n=2066)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7297 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.7895` → IC=+0.202 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7895 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.676` → IC=+0.208 (n=1342)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.676 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `0.8639` → IC=+0.199 (n=1852)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8639 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` > `0.6971` → IC=+0.181 (n=2481)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6971 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.1002` → IC=+0.191 (n=1122)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1002 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.4324` → IC=+0.196 (n=1005)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4324 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.5094` → IC=+0.183 (n=1004)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.5094 (IC base=+0.178)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.183 (n=3505)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `2733.5431` → IC=+0.184 (n=2769)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 2733.5431 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.191 (n=2881)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 150.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.138 (n=1095)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0037 (IC base=+0.093)

- **PATRÓN** `ibs_20min` < `0.3758` → IC=+0.162 (n=2186)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3758 (IC base=+0.093)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.132 (n=1054)

  - _Acción_: Kelly boost +0.66€ cuando `ballena_activa_n` < 19.0 (IC base=+0.093)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.210 (n=384)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0997` → IC=+0.223 (n=384)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0997 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.198 (n=786)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.170)

- **PATRÓN** `ibs_20min` > `0.9273` → IC=+0.227 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9273 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.3035` → IC=+0.193 (n=275)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.3035 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.109` → IC=+0.190 (n=372)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.109 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.828` → IC=+0.171 (n=924)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 6.828 (IC base=+0.170)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.198 (n=581)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 0.8753 (IC base=+0.170)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.178 (n=343)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` < `2.2086` → IC=+0.181 (n=751)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.2086 (IC base=+0.170)

- **PATRÓN** `volumen_spike_ratio` > `1.413` → IC=+0.171 (n=853)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.413 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `14802.2575` → IC=+0.184 (n=581)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14802.2575 (IC base=+0.170)

- **PATRÓN** `ballena_activa_n` < `156.0` → IC=+0.202 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 156.0 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.190 (n=343)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0028 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.3449` → IC=+0.140 (n=1027)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.3449 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.129 (n=920)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.7755` → IC=+0.155 (n=1027)

  - _Acción_: Kelly boost +0.78€ cuando `ibs_20min` < 0.7755 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1877` → IC=+0.144 (n=1038)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1877 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.162` → IC=+0.123 (n=929)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 3.162 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` > `1.0609` → IC=+0.150 (n=466)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_regimen` > 1.0609 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.168 (n=272)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.133 (n=894)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=1331)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `308.0` → IC=+0.149 (n=878)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 308.0 (IC base=+0.120)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.250 (n=634)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.2048` → IC=+0.231 (n=634)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2048 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.229 (n=999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.6864` → IC=+0.275 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6864 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` > `0.3573` → IC=+0.227 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3573 (IC base=+0.214)

- **PATRÓN** `dist_vwap_pct` < `0.2052` → IC=+0.217 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2052 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.93` → IC=+0.239 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.93 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` < `0.8392` → IC=+0.219 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8392 (IC base=+0.214)

- **PATRÓN** `volumen_regimen` > `1.1791` → IC=+0.230 (n=317)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1791 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.1569` → IC=+0.244 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1569 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.4127` → IC=+0.252 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4127 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.4505` → IC=+0.230 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4505 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=1060)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

- **PATRÓN** `ibs_20min` < `0.1034` → IC=+0.172 (n=318)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.1034 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `7013.633` → IC=+0.133 (n=635)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7013.633 (IC base=+0.068)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.174 (n=507)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0079 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.5352` → IC=+0.160 (n=760)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.5352 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.186 (n=680)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 8.0 (IC base=+0.159)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.9916` → IC=+0.238 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9916 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.204` → IC=+0.226 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.204 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` < `1.0509` → IC=+0.183 (n=669)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.0509 (IC base=+0.159)

- **PATRÓN** `volumen_regimen` > `0.7177` → IC=+0.165 (n=679)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.7177 (IC base=+0.159)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.188 (n=216)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` < `1.4569` → IC=+0.164 (n=245)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.4569 (IC base=+0.159)

- **PATRÓN** `volumen_spike_ratio` > `2.1801` → IC=+0.174 (n=332)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1801 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.165 (n=782)

  - _Acción_: Kelly boost +0.82€ cuando `libro_spread` < 0.02 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `3062.644` → IC=+0.195 (n=254)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3062.644 (IC base=+0.159)

- **PATRÓN** `ibs_20min` < `0.5152` → IC=+0.146 (n=688)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5152 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `2768.8884` → IC=+0.160 (n=354)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2768.8884 (IC base=+0.064)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.134 (n=503)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 21.0 (IC base=+0.064)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0234` → IC=+0.158 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0234 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.183 (n=197)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.007 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2552` → IC=+0.172 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2552 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.200 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.180 (n=176)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.56 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.2304` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.2304 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `1.103` → IC=+0.156 (n=219)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 1.103 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.705` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 7.705 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.301` → IC=+0.175 (n=167)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 3.301 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.6289` → IC=+0.168 (n=197)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.6289 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.2537` → IC=+0.173 (n=194)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` < 0.2537 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.1897` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1897 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `1.4605` → IC=+0.233 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4605 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `2.6057` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6057 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=198)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2499.5335` → IC=+0.169 (n=131)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 2499.5335 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.149 (n=223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0097 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.163 (n=78)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 17.0 (IC base=+0.112)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.131 (n=223)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.61 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `1.1297` → IC=+0.269 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1297 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.17` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 5.17 (IC base=+0.112)

- **PATRÓN** `volumen_regimen` > `1.2191` → IC=+0.123 (n=75)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` > 1.2191 (IC base=+0.112)

- **PATRÓN** `volumen_pendiente_norm` > `0.2295` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2295 (IC base=+0.112)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.136 (n=182)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 17.0 (IC base=+0.112)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.182 (n=5259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0047 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.223 (n=5262)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=16448)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.5562` → IC=+0.241 (n=14088)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5562 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9044` → IC=+0.210 (n=2008)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9044 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.334` → IC=+0.254 (n=3860)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.334 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2244` → IC=+0.170 (n=10571)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2244 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2906` → IC=+0.206 (n=2103)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2906 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6048` → IC=+0.196 (n=5106)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.6048 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1828.14` → IC=+0.186 (n=15769)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1828.14 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `116.0` → IC=+0.202 (n=14407)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 116.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.194 (n=6319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0054 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.4961` → IC=+0.189 (n=14339)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.94€ cuando `drift_60min` |x|≤ 0.4961 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.5798` → IC=+0.241 (n=14338)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5798 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1767` → IC=+0.171 (n=8641)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1767 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.9` → IC=+0.206 (n=1988)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.9 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.639` → IC=+0.188 (n=13853)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.639 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.7053` → IC=+0.160 (n=4262)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7053 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2894` → IC=+0.251 (n=1927)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2894 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.254` → IC=+0.197 (n=6133)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.254 (IC base=+0.186)

- **PATRÓN** `libro_liquidez` > `1765.8062` → IC=+0.187 (n=14338)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1765.8062 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.213 (n=8894)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.186)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.239 (n=863)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.218)

- **PATRÓN** `drift_60min` |x|≤ `0.3504` → IC=+0.221 (n=2581)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3504 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=1241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.223 (n=1742)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.218)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.325 (n=999)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.634` → IC=+0.350 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.634 (IC base=+0.218)

- **PATRÓN** `volumen_pendiente_norm` > `0.2786` → IC=+0.285 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2786 (IC base=+0.218)

- **PATRÓN** `volumen_spike_ratio` > `2.2721` → IC=+0.233 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2721 (IC base=+0.218)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=2711)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.218)

- **PATRÓN** `libro_liquidez` > `2091.27` → IC=+0.233 (n=860)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2091.27 (IC base=+0.218)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.237 (n=994)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.218)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.264 (n=2201)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.258)

- **PATRÓN** `drift_60min` |x|≤ `0.1217` → IC=+0.275 (n=968)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1217 (IC base=+0.258)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.266 (n=2004)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.258)

- **PATRÓN** `ibs_20min` < `0.5036` → IC=+0.286 (n=2200)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5036 (IC base=+0.258)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.37` → IC=+0.266 (n=685)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.37 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.258 (n=1965)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.258)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.278 (n=309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.258)

- **PATRÓN** `volumen_spike_ratio` > `2.2714` → IC=+0.269 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2714 (IC base=+0.258)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.259 (n=2451)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.258)

- **PATRÓN** `libro_liquidez` > `1570.482` → IC=+0.268 (n=2199)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1570.482 (IC base=+0.258)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.263 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=+0.258)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.202 (n=856)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1773` → IC=+0.162 (n=1701)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.1773 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2666)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.2563` → IC=+0.209 (n=2551)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2563 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1246` → IC=+0.196 (n=1365)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1246 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.62` → IC=+0.167 (n=418)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.62 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.169` → IC=+0.156 (n=2340)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 4.169 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6305` → IC=+0.177 (n=852)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6305 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0712` → IC=+0.155 (n=2278)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_pendiente_norm` < 0.0712 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2706` → IC=+0.177 (n=363)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2706 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1714` → IC=+0.161 (n=2192)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1714 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.528` → IC=+0.157 (n=2227)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.528 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `10307.2247` → IC=+0.152 (n=2551)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 10307.2247 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `268.0` → IC=+0.185 (n=1082)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 268.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=2145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.3322` → IC=+0.158 (n=2143)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.3322 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.7033` → IC=+0.200 (n=2143)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7033 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.1344` → IC=+0.166 (n=1988)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1344 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.218` → IC=+0.160 (n=474)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.218 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1835` → IC=+0.154 (n=2143)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1835 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2167` → IC=+0.194 (n=400)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2167 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4236` → IC=+0.150 (n=2039)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4236 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7717` → IC=+0.158 (n=1359)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 1.7717 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `338.0` → IC=+0.148 (n=1304)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 338.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.257 (n=873)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.305 (n=976)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.391` → IC=+0.318 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.391 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.2094` → IC=+0.226 (n=2667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2094 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `3.1781` → IC=+0.241 (n=847)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1781 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3102)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1856.6724` → IC=+0.237 (n=1746)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1856.6724 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0105` → IC=+0.243 (n=2163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0105 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1809` → IC=+0.253 (n=1081)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1809 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.266 (n=924)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0261` → IC=+0.301 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0261 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.071` → IC=+0.291 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.071 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3451` → IC=+0.294 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3451 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.128` → IC=+0.247 (n=1553)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.128 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `2061.827` → IC=+0.261 (n=819)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2061.827 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.246 (n=1004)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.239)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.200 (n=1195)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4224` → IC=+0.159 (n=2710)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4224 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=2820)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2532` → IC=+0.194 (n=2711)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2532 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1411` → IC=+0.171 (n=1471)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1411 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.181` → IC=+0.163 (n=1104)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.181 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8719` → IC=+0.164 (n=1808)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.8719 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.188 (n=357)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5208` → IC=+0.165 (n=1164)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5208 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1702` → IC=+0.159 (n=1198)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` > 2.1702 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6820.9392` → IC=+0.240 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6820.9392 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.173 (n=1155)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 76.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.191 (n=748)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0033 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4436` → IC=+0.140 (n=2242)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4436 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.158 (n=819)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.7425` → IC=+0.185 (n=2242)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.7425 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.145 (n=2009)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.146` → IC=+0.174 (n=339)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.146 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.6998` → IC=+0.143 (n=987)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_regimen` < 0.6998 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2959` → IC=+0.233 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2959 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4265` → IC=+0.137 (n=2154)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4265 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7453.3789` → IC=+0.213 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7453.3789 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.130 (n=1910)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 133.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.149 (n=1816)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0083 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.200 (n=2732)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4444 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0632` → IC=+0.209 (n=499)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0632 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.838` → IC=+0.267 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.838 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2241` → IC=+0.137 (n=2724)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 1.2241 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1621` → IC=+0.127 (n=2830)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1621 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2801` → IC=+0.138 (n=352)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2801 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `2.4762` → IC=+0.126 (n=2659)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` < 2.4762 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4632` → IC=+0.127 (n=2659)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4632 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2801)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2875.1364` → IC=+0.251 (n=908)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2875.1364 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.135 (n=867)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 25.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.141 (n=2599)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0111 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.159 (n=868)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.132 (n=2677)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6429` → IC=+0.213 (n=2599)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6429 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.4927` → IC=+0.132 (n=2646)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.4927 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.312` → IC=+0.134 (n=2505)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.312 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `0.6439` → IC=+0.139 (n=867)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6439 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.2239` → IC=+0.171 (n=438)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.2239 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `1.4341` → IC=+0.146 (n=809)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4341 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2710.726` → IC=+0.212 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2710.726 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.137 (n=2153)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 48.0 (IC base=+0.119)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.245 (n=2311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2701)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.235 (n=1728)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.6058` → IC=+0.270 (n=2312)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6058 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.197` → IC=+0.244 (n=1437)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.197 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.756` → IC=+0.271 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.756 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2308` → IC=+0.234 (n=2587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2308 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6427` → IC=+0.229 (n=2587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6427 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2353` → IC=+0.251 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2353 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4995` → IC=+0.244 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4995 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=3356)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2652.5528` → IC=+0.238 (n=1725)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2652.5528 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0229` → IC=+0.247 (n=1226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0229 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.234 (n=2540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.263 (n=2708)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` < `0.2934` → IC=+0.230 (n=2577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2934 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.218` → IC=+0.259 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.218 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `1.2298` → IC=+0.258 (n=901)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2298 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.294 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.427` → IC=+0.229 (n=2504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.427 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2413.8398` → IC=+0.229 (n=2414)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2413.8398 (IC base=+0.226)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=4742)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.242 (n=1597)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.5079` → IC=+0.211 (n=4781)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5079 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.218 (n=1692)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.9405` → IC=+0.246 (n=1594)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9405 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.1719` → IC=+0.209 (n=1845)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1719 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.4327` → IC=+0.210 (n=3422)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4327 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.766` → IC=+0.212 (n=1562)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.766 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.65` → IC=+0.203 (n=4258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.65 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `0.7068` → IC=+0.219 (n=1543)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7068 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.8852` → IC=+0.206 (n=2338)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8852 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.220 (n=1339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.4537` → IC=+0.208 (n=1570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4537 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.8414` → IC=+0.204 (n=3140)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8414 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=3723)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2608.7215` → IC=+0.210 (n=4781)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2608.7215 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.235 (n=1190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4913` → IC=+0.203 (n=3568)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4913 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.198 (n=1382)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 16.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.204 (n=1608)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.7333` → IC=+0.194 (n=3570)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.7333 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.6713` → IC=+0.200 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6713 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.4174` → IC=+0.184 (n=3559)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.4174 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.168` → IC=+0.195 (n=3576)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` < 6.168 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `1.101` → IC=+0.197 (n=2970)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.101 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.192 (n=3265)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `1.5326` → IC=+0.194 (n=1549)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.5326 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.1885` → IC=+0.195 (n=1597)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.1885 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=4742)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `166.0` → IC=+0.198 (n=3081)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 166.0 (IC base=+0.187)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.258 (n=609)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.243)

- **PATRÓN** `drift_60min` |x|≤ `0.0866` → IC=+0.281 (n=231)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0866 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.248 (n=727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.243)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.249 (n=321)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.243)

- **PATRÓN** `ibs_20min` < `0.5013` → IC=+0.269 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5013 (IC base=+0.243)

- **PATRÓN** `dist_vwap_pct` < `0.539` → IC=+0.252 (n=748)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.539 (IC base=+0.243)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.979` → IC=+0.260 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.979 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` < `1.2051` → IC=+0.252 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2051 (IC base=+0.243)

- **PATRÓN** `volumen_regimen` > `0.8637` → IC=+0.256 (n=461)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8637 (IC base=+0.243)

- **PATRÓN** `volumen_pendiente_norm` > `0.2861` → IC=+0.333 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2861 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` < `1.8148` → IC=+0.251 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8148 (IC base=+0.243)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.243 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `12241.3325` → IC=+0.255 (n=618)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12241.3325 (IC base=+0.243)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.222 (n=826)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.168)

- **PATRÓN** `drift_60min` |x|≤ `0.3728` → IC=+0.181 (n=1235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.90€ cuando `drift_60min` |x|≤ 0.3728 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.196 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.168)

- **PATRÓN** `ibs_20min` < `0.1409` → IC=+0.200 (n=545)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1409 (IC base=+0.168)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.171 (n=560)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6084 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` > `0.6887` → IC=+0.199 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6887 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.407` → IC=+0.186 (n=1217)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 6.407 (IC base=+0.168)

- **PATRÓN** `volumen_regimen` < `0.8865` → IC=+0.202 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8865 (IC base=+0.168)

- **PATRÓN** `volumen_pendiente_norm` > `0.1514` → IC=+0.186 (n=386)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_pendiente_norm` > 0.1514 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` < `1.4014` → IC=+0.182 (n=410)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4014 (IC base=+0.168)

- **PATRÓN** `volumen_spike_ratio` > `1.7953` → IC=+0.176 (n=820)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_spike_ratio` > 1.7953 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `13509.9946` → IC=+0.180 (n=823)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 13509.9946 (IC base=+0.168)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.180 (n=1191)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 701.0 (IC base=+0.168)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.194 (n=318)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0067 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0102` → IC=+0.206 (n=328)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0102 (IC base=+0.174)

- **PATRÓN** `drift_60min` |x|≤ `0.5907` → IC=+0.185 (n=722)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.93€ cuando `drift_60min` |x|≤ 0.5907 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.174)

- **PATRÓN** `ibs_20min` < `0.3898` → IC=+0.175 (n=241)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.3898 (IC base=+0.174)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.234 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.56` → IC=+0.225 (n=136)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.56 (IC base=+0.174)

- **PATRÓN** `volumen_pendiente_norm` > `0.2088` → IC=+0.225 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2088 (IC base=+0.174)

- **PATRÓN** `volumen_spike_ratio` > `2.2523` → IC=+0.185 (n=480)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.2523 (IC base=+0.174)

- **PATRÓN** `libro_liquidez` > `2523.314` → IC=+0.224 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2523.314 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.217 (n=1355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.4616` → IC=+0.210 (n=1355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4616 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.220 (n=487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.5182` → IC=+0.213 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5182 (IC base=+0.201)

- **PATRÓN** `ibs_20min` > `0.8776` → IC=+0.205 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8776 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `0.2171` → IC=+0.215 (n=1193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2171 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.152` → IC=+0.210 (n=1218)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.152 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `0.8809` → IC=+0.204 (n=904)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8809 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `1.2334` → IC=+0.209 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2334 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.1056` → IC=+0.204 (n=1246)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1056 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` > `0.1645` → IC=+0.205 (n=402)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1645 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` < `2.4554` → IC=+0.208 (n=1326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4554 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.204 (n=1387)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.244 (n=369)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4923` → IC=+0.210 (n=1105)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4923 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.199 (n=741)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.3952` → IC=+0.194 (n=737)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.3952 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.0864` → IC=+0.189 (n=1105)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.0864 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.6607` → IC=+0.200 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6607 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.2251` → IC=+0.188 (n=1063)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2251 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.748` → IC=+0.192 (n=1130)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.748 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6419` → IC=+0.222 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6419 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.206 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.198 (n=952)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.5301` → IC=+0.192 (n=361)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5301 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `6959.7194` → IC=+0.193 (n=1105)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6959.7194 (IC base=+0.187)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.219 (n=471)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0087 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.205 (n=727)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.257 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.184)

- **PATRÓN** `dist_vwap_pct` > `0.7405` → IC=+0.234 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7405 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.307` → IC=+0.213 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.307 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.6985` → IC=+0.235 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6985 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.194 (n=635)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.184)

- **PATRÓN** `volumen_pendiente_norm` > `0.0795` → IC=+0.197 (n=318)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.0795 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` < `1.5676` → IC=+0.192 (n=303)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.5676 (IC base=+0.184)

- **PATRÓN** `volumen_spike_ratio` > `2.4815` → IC=+0.214 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4815 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=821)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `3551.9496` → IC=+0.208 (n=471)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3551.9496 (IC base=+0.184)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.204 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.184)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.201 (n=346)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.197)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.197 (n=173)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0124 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.6119` → IC=+0.220 (n=519)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6119 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.234 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.7241` → IC=+0.220 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7241 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` > `0.5172` → IC=+0.222 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5172 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.3104` → IC=+0.197 (n=433)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.3104 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.952` → IC=+0.205 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.952 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.929` → IC=+0.204 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.929 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.7624` → IC=+0.206 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7624 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `0.9427` → IC=+0.204 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9427 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.1073` → IC=+0.220 (n=448)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1073 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` > `2.1983` → IC=+0.233 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1983 (IC base=+0.197)

- **PATRÓN** `libro_liquidez` > `2981.5842` → IC=+0.218 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2981.5842 (IC base=+0.197)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.231 (n=515)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 47.0 (IC base=+0.197)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.162 (n=691)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0039 (IC base=+0.070)

- **PATRÓN** `ibs_20min` > `0.5578` → IC=+0.165 (n=1318)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.5578 (IC base=+0.070)

- **PATRÓN** `dist_vwap_pct` > `0.1457` → IC=+0.139 (n=785)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1457 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.222` → IC=+0.175 (n=327)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 11.222 (IC base=+0.070)

- **PATRÓN** `ibs_20min` < `0.1926` → IC=+0.264 (n=510)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1926 (IC base=+0.073)

- **PATRÓN** `dist_vwap_pct` < `0.0992` → IC=+0.145 (n=738)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.0992 (IC base=+0.073)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.469` → IC=+0.180 (n=123)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 10.469 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.1468` → IC=+0.200 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1468 (IC base=+0.073)

- **PATRÓN** `volumen_spike_ratio` < `1.4844` → IC=+0.132 (n=308)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.4844 (IC base=+0.073)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.133 (n=527)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0057 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.5161` → IC=+0.185 (n=443)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` > 0.5161 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1218` → IC=+0.154 (n=255)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.1218 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.2794` → IC=+0.245 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2794 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.1146` → IC=+0.144 (n=349)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1146 (IC base=+0.088)

- **PATRÓN** `volumen_regimen` < `1.0279` → IC=+0.127 (n=301)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.0279 (IC base=+0.088)

- **PATRÓN** `volumen_pendiente_norm` > `0.0693` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.0693 (IC base=+0.088)

- **PATRÓN** `volumen_spike_ratio` < `2.5247` → IC=+0.123 (n=319)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.5247 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `5062.7919` → IC=+0.137 (n=111)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 5062.7919 (IC base=+0.088)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.151 (n=342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0047 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.125 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 7.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.649` → IC=+0.209 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.649 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.197 (n=255)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.269` → IC=+0.259 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.269 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.8145` → IC=+0.127 (n=322)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_regimen` < 0.8145 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.283` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.283 (IC base=+0.094)

- **PATRÓN** `libro_liquidez` > `1646.1464` → IC=+0.148 (n=217)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1646.1464 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.1058` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1058 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.025` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.025 (IC base=+0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.1363` → IC=+0.167 (n=67)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1363 (IC base=+0.039)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.15` → IC=-0.230 (n=61)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.258 (n=184)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.160 (n=339)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` > 0.75 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.817` → IC=+0.146 (n=142)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 7.817 (IC base=+0.028)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.168 (n=215)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0103 (IC base=+0.087)

- **PATRÓN** `ibs_20min` < `0.15` → IC=+0.258 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.15 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.6473` → IC=+0.161 (n=213)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` < 0.6473 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.807` → IC=+0.309 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.807 (IC base=+0.087)

- **PATRÓN** `volumen_regimen` > `1.0818` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0818 (IC base=+0.087)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` < `2.1886` → IC=+0.174 (n=142)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` < 2.1886 (IC base=+0.087)

- **PATRÓN** `volumen_spike_ratio` > `2.5298` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5298 (IC base=+0.087)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.183 (n=156)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.06 (IC base=+0.087)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.333 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=231)

- **FILTRO** `dist_vwap_pct` > `0.2348` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2348
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=278)

- **FILTRO** `volumen_spike_ratio` > `2.5231` → IC=-0.214 (n=75)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.5231
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=146)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.355 (n=60)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.255 (n=182)

- **FILTRO** `dist_vwap_pct` > `0.4185` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4185
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=221)

- **FILTRO** `sigma_ewma_delta_pct` > `10.676` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.676
  - _Potencial_: sin este filtro IC_bueno=-0.277 (n=218)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.259 (n=131)

- **FILTRO** `libro_liquidez` < `1287.125` → IC=-0.306 (n=60)

  - _Acción_: SKIP cuando `libro_liquidez` < 1287.125
  - _Potencial_: sin este filtro IC_bueno=-0.272 (n=182)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=50)

- **FILTRO** `volumen_regimen` < `1.2175` → IC=-0.280 (n=48)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2175
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=48)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.300 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.191 (n=53)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=80)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `hora_utc` < `5.0` → IC=-0.173 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=52)

- **FILTRO** `ibs_20min` < `0.6568` → IC=-0.441 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6568
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=67)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.246 (n=69)

- **FILTRO** `ibs_20min` > `0.538` → IC=-0.372 (n=45)

  - _Acción_: SKIP cuando `ibs_20min` > 0.538
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=46)

- **FILTRO** `libro_liquidez` < `1269.5074` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `libro_liquidez` < 1269.5074
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=69)

- **PATRÓN** `ibs_20min` > `0.9464` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.9464 (IC base=-0.173)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.329 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=67)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.389 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.198 (n=84)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=30)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1653` → IC=-0.120 (n=264)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1653
  - _Potencial_: sin este filtro IC_bueno=+0.169 (n=515)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.167 (n=223)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0059 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.147 (n=182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 17.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.6875` → IC=+0.139 (n=491)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 0.6875 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.7218` → IC=+0.194 (n=83)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.7218 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.8504` → IC=+0.136 (n=328)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 0.8504 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` < `0.2776` → IC=+0.129 (n=453)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.2776 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `2.4758` → IC=+0.132 (n=389)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.4758 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.1653` → IC=+0.169 (n=515)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.1653 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.198` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 11.198 (IC base=+0.071)

- **PATRÓN** `libro_liquidez` > `3256.3999` → IC=+0.150 (n=390)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 3256.3999 (IC base=+0.071)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6623` → IC=-0.217 (n=51)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6623
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=155)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.213 (n=92)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.170 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 12.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.1667` → IC=+0.210 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1667 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.0941` → IC=+0.167 (n=277)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.0941 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.216` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 7.216 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.678` → IC=+0.154 (n=215)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.678 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.163 (n=274)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6211 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` < `0.07` → IC=+0.167 (n=211)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` < 0.07 (IC base=+0.148)

- **PATRÓN** `volumen_pendiente_norm` > `0.2728` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2728 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` < `2.5184` → IC=+0.182 (n=243)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.5184 (IC base=+0.148)

- **PATRÓN** `volumen_spike_ratio` > `1.4429` → IC=+0.161 (n=243)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 1.4429 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.148 (n=325)

  - _Acción_: Kelly boost +0.74€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5309.1442` → IC=+0.154 (n=183)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 5309.1442 (IC base=+0.148)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=162)

- **FILTRO** `ibs_20min` > `0.2038` → IC=-0.136 (n=97)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2038
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=189)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.133 (n=118)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0038 (IC base=+0.085)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.172 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.129 (n=157)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` > 0.8015 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.015` → IC=+0.131 (n=128)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.015 (IC base=+0.085)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.128 (n=162)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.085)

- **PATRÓN** `volumen_spike_ratio` < `1.4416` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` < 1.4416 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.2038` → IC=+0.134 (n=189)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.2038 (IC base=+0.042)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.042)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4444` → IC=-0.281 (n=30)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4444
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=98)

- **FILTRO** `volumen_spike_ratio` > `2.1493` → IC=-0.188 (n=30)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.1493
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=61)

- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.357 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.276 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.250 (n=162)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.250)

- **PATRÓN** `ibs_20min` > `0.6757` → IC=+0.267 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6757 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` < `0.224` → IC=+0.248 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.224 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.333` → IC=+0.303 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.333 (IC base=+0.250)

- **PATRÓN** `volumen_regimen` < `0.9999` → IC=+0.285 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.9999 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` < `0.3005` → IC=+0.309 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.3005 (IC base=+0.250)

- **PATRÓN** `volumen_pendiente_norm` > `0.089` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.089 (IC base=+0.250)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.380 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.250)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.253 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.250)

- **PATRÓN** `libro_liquidez` > `667.907` → IC=+0.253 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 667.907 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.614` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.614 (IC base=-0.085)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.324 (n=66)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3369` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3369 (IC base=+0.229)

- **PATRÓN** `elapsed_s` > `185.9` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.9 (IC base=+0.229)

- **PATRÓN** `elapsed_s` < `202.0` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.0 (IC base=+0.229)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.269 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.229)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.324 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.229)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.324 (n=66)

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

- **PATRÓN** `drift_ventana_pct` |x|> `0.3369` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3369 (IC base=+0.229)

- **PATRÓN** `elapsed_s` > `185.9` → IC=+0.241 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 185.9 (IC base=+0.229)

- **PATRÓN** `elapsed_s` < `202.0` → IC=+0.273 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.0 (IC base=+0.229)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.333 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.9999` → IC=+0.269 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.9999 (IC base=+0.229)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.324 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.229)

- **PATRÓN** `ballena_activa_n` < `1862.0` → IC=+0.285 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1862.0 (IC base=+0.229)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2859.5654` → IC=+0.132 (n=544)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2859.5654 (IC base=+0.102)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2859.5654` → IC=+0.132 (n=544)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2859.5654 (IC base=+0.102)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=182)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=259)

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
- **FILTRO** `hora_utc` < `17.0` → IC=-0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3375)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.176 (n=100)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.128 (n=232)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1238)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=1192)

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
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=705)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=407)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.031 (n=388)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.137 (n=166)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.495 (IC base=+0.018)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=832)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=832)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=256)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=656)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=757)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=757)

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
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=206)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=230)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=254)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.121 (n=56)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=208)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=242)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=342)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=342)

- **FILTRO** `libro_liquidez` < `599.5589` → IC=-0.129 (n=122)

  - _Acción_: SKIP cuando `libro_liquidez` < 599.5589
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=250)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=248)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=176)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.122 (n=1213)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=3154)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=24)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.179 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.42` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` < 0.42
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=44)

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
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.164 (n=132)

  - _Acción_: Kelly boost +0.82€ cuando `py_entrada` < 0.46 (IC base=+0.008)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.186 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=218)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.5 (IC base=+0.048)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `restante_min` < `10.35` → IC=-0.150 (n=135)

  - _Acción_: SKIP cuando `restante_min` < 10.35
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=277)

- **FILTRO** `lag_apertura_s` > `255.13` → IC=-0.148 (n=140)

  - _Acción_: SKIP cuando `lag_apertura_s` > 255.13
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=272)

- **FILTRO** `profundidad_ratio` < `39.0` → IC=-0.176 (n=103)

  - _Acción_: SKIP cuando `profundidad_ratio` < 39.0
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=309)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.246 (n=65)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=294)

- **FILTRO** `profundidad_ratio` < `20.4` → IC=-0.152 (n=116)

  - _Acción_: SKIP cuando `profundidad_ratio` < 20.4
  - _Potencial_: sin este filtro IC_bueno=+0.006 (n=243)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `profundidad_ratio` < `22.3` → IC=-0.136 (n=127)

  - _Acción_: SKIP cuando `profundidad_ratio` < 22.3
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=258)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=312)

### LIQUIDACIONES_DEPTH_FASE0#SOL#5min
- **PATRÓN** `py_entrada` > `0.48` → IC=+0.124 (n=155)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` > 0.48 (IC base=-0.015)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.4` → IC=-0.184 (n=112)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.005 (n=418)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.163 (n=5558)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=17410)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.170 (n=5885)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=17779)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.192 (n=1020)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=3125)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.165 (n=975)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3267)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.138 (n=1093)

  - _Acción_: Kelly boost +0.69€ cuando `ibs_20min` > 1.0 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1420.26` → IC=+0.133 (n=2073)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1420.26 (IC base=+0.037)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.128 (n=1983)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.015)

- **PATRÓN** `libro_liquidez` > `1542.3486` → IC=+0.149 (n=1443)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1542.3486 (IC base=+0.015)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.155 (n=770)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2631)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=824)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2548)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.169 (n=1023)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=3160)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.182 (n=1078)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=3238)

- **PATRÓN** `ibs_20min` > `0.9632` → IC=+0.131 (n=1424)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 0.9632 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1847.6396` → IC=+0.126 (n=1423)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1847.6396 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.153 (n=995)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=3162)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=2311)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2718)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3458)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=430)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.264 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=417)

- **FILTRO** `py_entrada` > `0.595` → IC=-0.234 (n=273)

  - _Acción_: SKIP cuando `py_entrada` > 0.595
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=834)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `ibs_20min` < `0.1975` → IC=-0.223 (n=110)

  - _Acción_: SKIP cuando `ibs_20min` < 0.1975
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=224)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.193 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=286)

- **FILTRO** `libro_liquidez` < `3742.1782` → IC=-0.168 (n=212)

  - _Acción_: SKIP cuando `libro_liquidez` < 3742.1782
  - _Potencial_: sin este filtro IC_bueno=-0.084 (n=212)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.070 (n=864)

- **FILTRO** `libro_liquidez` < `2083.3312` → IC=-0.167 (n=346)

  - _Acción_: SKIP cuando `libro_liquidez` < 2083.3312
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=704)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=15866)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=35434)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=12479)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=38821)

- **FILTRO** `ibs_7min` < `0.2421` → IC=-0.228 (n=12824)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2421
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=38476)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.152 (n=17333)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=33967)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.238 (n=15746)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=49112)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.180 (n=16049)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=48809)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2561)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6324)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=4403)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4482)

- **FILTRO** `ibs_7min` < `0.7105` → IC=-0.246 (n=2930)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7105
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=5955)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.176 (n=1974)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6911)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.270 (n=2770)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8480)

- **FILTRO** `ibs_7min` > `0.773` → IC=-0.211 (n=2812)

  - _Acción_: SKIP cuando `ibs_7min` > 0.773
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=8438)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=1996)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=6699)

- **FILTRO** `ibs_7min` < `0.7289` → IC=-0.196 (n=2171)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7289
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6524)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.188 (n=2165)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6530)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2144)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6677)

- **FILTRO** `ibs_7min` > `0.2665` → IC=-0.195 (n=2205)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2665
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6616)

- **FILTRO** `ballena_activa_n` > `149.0` → IC=-0.182 (n=2201)

  - _Acción_: SKIP cuando `ballena_activa_n` > 149.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6620)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.156 (n=2083)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=6383)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=2064)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=6402)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.244 (n=2791)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=5675)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.192 (n=2082)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6384)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.250 (n=2747)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9218)

- **FILTRO** `ibs_7min` > `0.7341` → IC=-0.176 (n=2991)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7341
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=8974)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.261 (n=1943)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6433)

- **FILTRO** `ibs_7min` < `0.732` → IC=-0.184 (n=2092)

  - _Acción_: SKIP cuando `ibs_7min` < 0.732
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6284)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.190 (n=2046)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6330)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=1928)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=6752)

- **FILTRO** `ibs_7min` > `0.2755` → IC=-0.180 (n=2168)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2755
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6512)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.178 (n=2094)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6586)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=1993)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6478)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.230 (n=2105)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=6366)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.185 (n=2949)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=9457)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.281 (n=2089)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=6318)

- **FILTRO** `ibs_7min` < `0.2115` → IC=-0.219 (n=2101)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2115
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6306)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.200 (n=1910)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=6497)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.210 (n=2843)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=8893)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=120)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=980)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=1264)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=528)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=822)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.128 (n=151)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=338)

- **FILTRO** `ballena_activa_n` > `4.0` → IC=-0.141 (n=165)

  - _Acción_: SKIP cuando `ballena_activa_n` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=323)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.031 (n=439)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.129 (n=68)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=625)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.143 (n=1096)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.141 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 14.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `3732.187` → IC=+0.150 (n=729)

  - _Acción_: Kelly boost +0.75€ cuando `total_vol_5m` < 3732.187 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3685.1446` → IC=+0.141 (n=496)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3685.1446 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.143 (n=354)

  - _Acción_: Kelly boost +0.72€ cuando `ballena_activa_n` < 12.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4367` → IC=+0.159 (n=86)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.4367 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.226 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2589.8389` → IC=+0.227 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2589.8389 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `9.0` → IC=+0.175 (n=118)

  - _Acción_: Kelly boost +0.88€ cuando `ballena_activa_n` < 9.0 (IC base=+0.145)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.134 (n=225)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.142 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 3.0 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.130 (n=268)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.04 (IC base=+0.119)

- **PATRÓN** `libro_liquidez` > `2365.7446` → IC=+0.132 (n=150)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2365.7446 (IC base=+0.119)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.4153` → IC=+0.185 (n=147)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.92€ cuando `delta_ratio` |x|> 0.4153 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.153 (n=226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 4.0 (IC base=+0.134)

- **PATRÓN** `total_vol_5m` < `391.8444` → IC=+0.217 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 391.8444 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `7895.7846` → IC=+0.138 (n=147)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 7895.7846 (IC base=+0.134)

- **PATRÓN** `ballena_activa_n` < `71.0` → IC=+0.210 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 71.0 (IC base=+0.134)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4332` → IC=+0.256 (n=88)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4332 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 12.0 (IC base=+0.152)

- **PATRÓN** `total_vol_5m` < `5064.531` → IC=+0.195 (n=129)

  - _Acción_: Kelly boost +0.97€ cuando `total_vol_5m` < 5064.531 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `3077.3625` → IC=+0.162 (n=193)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3077.3625 (IC base=+0.152)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `ballena_activa_n` < 27.0 (IC base=+0.152)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.180 (n=123)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.088)

- **PATRÓN** `libro_liquidez` > `3635.4092` → IC=+0.167 (n=91)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3635.4092 (IC base=+0.088)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.4547` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.4547
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=130)

- **FILTRO** `T_h` > `129.6211` → IC=-0.214 (n=152)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.034 (n=464)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.181 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0034 (IC base=-0.079)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.354 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=140)

- **FILTRO** `T_h` > `87.9981` → IC=-0.271 (n=46)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=140)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.316 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=-0.037)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.152 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `87.7913` → IC=-0.160 (n=51)

  - _Acción_: SKIP cuando `T_h` < 87.7913
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.070)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0099` → IC=-0.222 (n=430)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0099
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=144)

- **FILTRO** `T_h` > `71.1632` → IC=-0.188 (n=428)

  - _Acción_: SKIP cuando `T_h` > 71.1632
  - _Potencial_: sin este filtro IC_bueno=-0.128 (n=146)

- **FILTRO** `pct_vs_K` |x|> `3.3706` → IC=-0.434 (n=120)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3706
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=364)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `pct_vs_K` |x|> `2.7876` → IC=-0.357 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7876
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=144)

- **FILTRO** `T_h` > `71.1632` → IC=-0.289 (n=131)

  - _Acción_: SKIP cuando `T_h` > 71.1632
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=44)

- **FILTRO** `pct_vs_K` |x|> `3.0008` → IC=-0.432 (n=42)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0008
  - _Potencial_: sin este filtro IC_bueno=-0.226 (n=133)

### PRICE_TARGET_GBM_FADE#BTC#reach
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
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.323 (n=122)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=41)

- **FILTRO** `T_h` > `135.9851` → IC=-0.281 (n=39)

  - _Acción_: SKIP cuando `T_h` > 135.9851
  - _Potencial_: sin este filtro IC_bueno=-0.238 (n=124)

- **FILTRO** `sigma_h` > `0.0088` → IC=-0.346 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0088
  - _Potencial_: sin este filtro IC_bueno=-0.140 (n=112)

- **FILTRO** `T_h` > `57.2342` → IC=-0.292 (n=99)

  - _Acción_: SKIP cuando `T_h` > 57.2342
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=50)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.255 (n=51)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=104)

- **FILTRO** `T_h` > `94.0115` → IC=-0.195 (n=103)

  - _Acción_: SKIP cuando `T_h` > 94.0115
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=52)

- **FILTRO** `sigma_h` > `0.0156` → IC=-0.352 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0156
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=79)

- **FILTRO** `T_h` > `33.8406` → IC=-0.323 (n=77)

  - _Acción_: SKIP cuando `T_h` > 33.8406
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=27)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1224` → IC=+0.476 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1224 (IC base=+0.340)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.359 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.340)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.380 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0072 (IC base=+0.340)

- **PATRÓN** `T_h` > `0.7719` → IC=+0.387 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7719 (IC base=+0.340)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.477 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.340)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.357 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.340)

- **PATRÓN** `edge` > `0.096` → IC=+0.448 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.096 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.430 (n=69)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0075 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.436 (n=138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.417)

- **PATRÓN** `T_h` < `0.5883` → IC=+0.430 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5883 (IC base=+0.417)

- **PATRÓN** `T_h` > `1.4813` → IC=+0.444 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4813 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.482 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

### RESOLUTION_SNIPER#ETH#sniper
- **PATRÓN** `edge` > `0.1023` → IC=+0.457 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1023 (IC base=+0.417)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.419 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.417)

- **PATRÓN** `sigma_h` > `0.0094` → IC=+0.420 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0094 (IC base=+0.417)

- **PATRÓN** `T_h` < `0.6978` → IC=+0.444 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6978 (IC base=+0.417)

- **PATRÓN** `T_h` > `0.4508` → IC=+0.406 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4508 (IC base=+0.417)

- **PATRÓN** `dist_50` > `0.4077` → IC=+0.479 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4077 (IC base=+0.417)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.423 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.417)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.441 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.417)

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

- **PATRÓN** `edge` > `0.1961` → IC=+0.478 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0156` → IC=+0.478 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0156 (IC base=+0.464)

- **PATRÓN** `T_h` > `1.1968` → IC=+0.478 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1968 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4373` → IC=+0.485 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4373 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=294)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=371)

- **FILTRO** `streak_estiramiento` > `0.8486` → IC=-0.179 (n=82)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8486
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=248)

- **PATRÓN** `streak_estiramiento` < `0.5614` → IC=+0.184 (n=166)

  - _Acción_: Kelly boost +0.92€ cuando `streak_estiramiento` < 0.5614 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `2756.3002` → IC=+0.144 (n=99)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2756.3002 (IC base=+0.040)

### STREAK_FADE_15M#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=27)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=15)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.000)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.495 (IC base=+0.000)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `volumen_racha` < `945898.4` → IC=+0.121 (n=56)

  - _Acción_: Kelly boost +0.60€ cuando `volumen_racha` < 945898.4 (IC base=+0.004)

- **PATRÓN** `streak_estiramiento` < `0.2292` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `streak_estiramiento` < 0.2292 (IC base=+0.004)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.137 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.082)

- **PATRÓN** `streak_estiramiento` < `0.5597` → IC=+0.167 (n=106)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.5597 (IC base=+0.082)

- **PATRÓN** `ballena_activa_n` < `29.0` → IC=+0.159 (n=80)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 29.0 (IC base=+0.082)

- **PATRÓN** `libro_liquidez` > `2274.7787` → IC=+0.148 (n=123)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2274.7787 (IC base=+0.082)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=92)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.190 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=43)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=820)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=826)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=734)

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

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.037)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=946)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1327)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=1092)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=1114)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `12.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3839)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `12.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2102)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.196 (n=1489)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.199 (n=1128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0119 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1721` → IC=+0.195 (n=2978)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1721 (IC base=+0.181)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1329` → IC=+0.192 (n=1343)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1329 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.188 (n=3139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.181)

- **PATRÓN** `ibs_15` > `0.5671` → IC=+0.259 (n=3384)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5671 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.174 (n=1629)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` < `0.6597` → IC=+0.169 (n=3165)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.6597 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.61` → IC=+0.257 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.61 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `4960.9554` → IC=+0.203 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4960.9554 (IC base=+0.181)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=1320)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.231 (n=581)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.0584` → IC=+0.260 (n=194)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0584 (IC base=+0.220)

- **PATRÓN** `delta_ratio_macro` |x|> `0.25` → IC=+0.240 (n=194)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.25 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=585)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `ibs_15` > `0.7231` → IC=+0.282 (n=581)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7231 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1354` → IC=+0.245 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1354 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.114` → IC=+0.303 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.114 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `16272.4583` → IC=+0.255 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16272.4583 (IC base=+0.220)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_ewma_delta_pct` > `28.269` → IC=-0.190 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 28.269
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=739)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.189 (n=220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0034 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.154 (n=290)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.151 (n=439)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1315` → IC=+0.162 (n=258)

  - _Acción_: Kelly boost +0.81€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1315 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.152 (n=605)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.152 (n=463)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5559` → IC=+0.246 (n=659)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5559 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1154` → IC=+0.156 (n=417)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1154 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.607` → IC=+0.146 (n=747)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.607 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.973` → IC=+0.289 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.973 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3558.8831` → IC=+0.153 (n=589)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3558.8831 (IC base=+0.145)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `18.347` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.347
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=291)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.131 (n=315)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0069 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.9024` → IC=+0.254 (n=238)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9024 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=392)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.096)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.407` → IC=+0.149 (n=72)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 8.407 (IC base=+0.017)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0237` → IC=+0.251 (n=263)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0237 (IC base=+0.205)

- **PATRÓN** `drift_60min` |x|≤ `0.0846` → IC=+0.234 (n=348)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0846 (IC base=+0.205)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3374` → IC=+0.236 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3374 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.205 (n=717)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.217 (n=709)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.205)

- **PATRÓN** `ibs_15` > `0.5488` → IC=+0.285 (n=789)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5488 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` > `0.1857` → IC=+0.209 (n=410)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1857 (IC base=+0.205)

- **PATRÓN** `dist_vwap_pct` < `0.3267` → IC=+0.206 (n=754)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3267 (IC base=+0.205)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.783` → IC=+0.231 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.783 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `2975.4354` → IC=+0.296 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2975.4354 (IC base=+0.205)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.158 (n=764)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` < 0.1111 (IC base=+0.065)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.369 (n=402)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.371 (n=603)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.384 (n=402)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.382 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.377 (n=606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.399 (n=604)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4165` → IC=+0.392 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4165 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.679` → IC=+0.386 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.679 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=734)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `3507.1457` → IC=+0.373 (n=603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3507.1457 (IC base=+0.363)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.364 (n=278)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.389 (n=106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0047 (IC base=+0.365)

- **PATRÓN** `drift_15min` |x|≤ `0.5105` → IC=+0.364 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.5105 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2146` → IC=+0.390 (n=143)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2146 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.397 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.384 (n=316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.390 (n=316)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.2448` → IC=+0.395 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2448 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.742` → IC=+0.376 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.742 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `15286.8558` → IC=+0.390 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15286.8558 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.411 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.361 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.359)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.379 (n=130)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.359)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0902` → IC=+0.372 (n=256)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0902 (IC base=+0.359)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2986` → IC=+0.378 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2986 (IC base=+0.359)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.387 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.359)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.364 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.359)

- **PATRÓN** `ibs_15` > `0.7485` → IC=+0.410 (n=287)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7485 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.378 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.359)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.360 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.359)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.352` → IC=+0.387 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.352 (IC base=+0.359)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.364 (n=321)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.359)

- **PATRÓN** `libro_liquidez` > `3951.8446` → IC=+0.394 (n=130)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3951.8446 (IC base=+0.359)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.222 (n=1043)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=3135)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.208 (n=1632)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2546)

- **FILTRO** `libro_liquidez` < `4171.7267` → IC=-0.151 (n=2757)

  - _Acción_: SKIP cuando `libro_liquidez` < 4171.7267
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1421)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.283 (n=1011)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1081` → IC=+0.209 (n=586)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1081 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.4229` → IC=+0.202 (n=978)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4229 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2289` → IC=+0.270 (n=1145)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2289 (IC base=-0.013)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3304` → IC=+0.254 (n=3370)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3304 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3571` → IC=+0.281 (n=3433)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3571 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6579` → IC=+0.279 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6579 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0342` → IC=-0.217 (n=1786)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0342
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=596)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.232 (n=595)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=1787)

- **FILTRO** `sigma_ewma_delta_pct` > `23.552` → IC=-0.267 (n=345)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.552
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=2037)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.127 (n=716)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0052 (IC base=+0.100)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.299 (n=147)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.100)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.122 (n=718)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 5.0 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.331 (n=324)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.1039` → IC=+0.297 (n=220)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1039 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.3651` → IC=+0.291 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3651 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.58` → IC=+0.135 (n=360)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 8.58 (IC base=+0.100)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0613` → IC=+0.207 (n=56)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0613 (IC base=-0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.0902` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.0902 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.293 (n=56)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.0459` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0459 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `381.0` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 381.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=655)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.166 (n=444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.167 (n=451)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0038 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.0711` → IC=+0.192 (n=222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0711 (IC base=+0.154)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.192 (n=384)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.168 (n=465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` > `0.622` → IC=+0.255 (n=505)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.622 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.455` → IC=+0.162 (n=137)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.455 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.6448` → IC=+0.155 (n=580)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.6448 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.268 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=655)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `10408.2229` → IC=+0.171 (n=168)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 10408.2229 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.248 (n=1207)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.242)

- **PATRÓN** `drift_15min` |x|≤ `0.7694` → IC=+0.257 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7694 (IC base=+0.242)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.260 (n=547)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.242)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3302` → IC=+0.243 (n=1168)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3302 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.249 (n=444)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.242)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.246 (n=466)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.242)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.272 (n=1207)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.6007` → IC=+0.268 (n=196)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6007 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.527` → IC=+0.252 (n=538)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.527 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.53` → IC=+0.246 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.53 (IC base=+0.242)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_h` > `0.0102` → IC=-0.243 (n=239)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0102
  - _Potencial_: sin este filtro IC_bueno=-0.168 (n=718)

- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.255 (n=324)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=633)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.280 (n=239)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.156 (n=718)

- **FILTRO** `sigma_ewma_delta_pct` > `6.57` → IC=-0.197 (n=226)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.57
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=731)

- **FILTRO** `sigma_ewma_delta_pct` > `18.076` → IC=-0.145 (n=503)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.076
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4001)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.187)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.187)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.187)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.187)

- **PATRÓN** `delta_ratio_macro` |x|> `0.082` → IC=+0.246 (n=479)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.082 (IC base=-0.038)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.290 (n=536)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.038)

- **PATRÓN** `dist_vwap_pct` < `0.4491` → IC=+0.253 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4491 (IC base=-0.038)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.248 (n=582)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=583)

- **FILTRO** `sigma_ewma_delta_pct` > `7.349` → IC=-0.204 (n=363)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.349
  - _Potencial_: sin este filtro IC_bueno=-0.204 (n=802)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=1146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.204)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.204)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0678` → IC=+0.271 (n=748)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0678 (IC base=-0.025)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1154` → IC=+0.298 (n=364)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1154 (IC base=-0.025)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.294 (n=841)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7702` → IC=+0.351 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7702 (IC base=-0.025)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.297 (n=899)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.319 (n=341)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2402` → IC=+0.301 (n=340)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2402 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2257` → IC=+0.307 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2257 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=1069)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8389` → IC=+0.320 (n=1021)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8389 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.4335` → IC=+0.328 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4335 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.706` → IC=+0.374 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.706 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `12635.0591` → IC=+0.311 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12635.0591 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.312 (n=243)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.287)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.312 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.287)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.312 (n=184)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.287)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.298 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.287)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.305 (n=553)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.287)

- **PATRÓN** `ibs_15` > `0.8279` → IC=+0.314 (n=552)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8279 (IC base=+0.287)

- **PATRÓN** `dist_vwap_pct` > `0.2516` → IC=+0.322 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2516 (IC base=+0.287)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.865` → IC=+0.381 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.865 (IC base=+0.287)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.286 (n=714)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.287)

- **PATRÓN** `libro_liquidez` > `16294.6642` → IC=+0.333 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16294.6642 (IC base=+0.287)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.307 (n=470)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.295)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.297 (n=470)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.318 (n=157)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.297 (n=470)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1055` → IC=+0.336 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1055 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.313 (n=421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.297 (n=427)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8745` → IC=+0.334 (n=420)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8745 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.324 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.360 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.103` → IC=-0.148 (n=217)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.103
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=73)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.212 (n=116)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=360)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.183 (n=118)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=358)

- **FILTRO** `drift_15min` |x|> `0.4407` → IC=-0.150 (n=161)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4407
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=315)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.1682` → IC=-0.191 (n=40)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.1682
  - _Potencial_: sin este filtro IC_bueno=-0.081 (n=41)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.160 (n=48)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

### UPDOWN_OU_5M#BTC#5min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1326` → IC=-0.160 (n=48)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1326
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=147)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2443` → IC=-0.134 (n=91)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2443
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=92)

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

- **FILTRO** `delta_ratio_macro` |x|≤ `0.306` → IC=-0.380 (n=23)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.306
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.075` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.075
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0063` → IC=-0.222 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=19)

- **FILTRO** `ballena_activa_n` > `18.0` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `ballena_activa_n` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `83.3501` → IC=+0.200 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.193)

- **PATRÓN** `ratio` < `0.973` → IC=+0.421 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.193)

- **PATRÓN** `T_h` > `111.9966` → IC=+0.353 (n=2051)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9966 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0236` → IC=+0.371 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0236 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.5964` → IC=+0.190 (n=185)

  - _Acción_: Kelly boost +0.95€ cuando `T_h` > 103.5964 (IC base=+0.166)

- **PATRÓN** `ratio` < `0.9943` → IC=+0.290 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9943 (IC base=+0.166)

- **PATRÓN** `T_h` > `109.882` → IC=+0.306 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.882 (IC base=+0.292)

- **PATRÓN** `ratio` > `1.0464` → IC=+0.397 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0464 (IC base=+0.292)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.238 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.230)

- **PATRÓN** `ratio` < `0.9849` → IC=+0.431 (n=186)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.230)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.352 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0093` → IC=+0.343 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0093 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1038` → IC=+0.448 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1038 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5671 sube el IC de +0.181 a +0.259 en UPDOWN_GBM#15min (n=3384). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7231 sube el IC de +0.220 a +0.282 en UPDOWN_GBM#BTC#15min (n=581). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5559 sube el IC de +0.145 a +0.246 en UPDOWN_GBM#ETH#15min (n=659). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9024 sube el IC de +0.096 a +0.254 en UPDOWN_GBM#SOL#15min (n=238). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5488 sube el IC de +0.205 a +0.285 en UPDOWN_GBM#XRP#15min (n=789). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.065 a +0.158 en UPDOWN_GBM#XRP#15min (n=764). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.066 a +0.283 en UPDOWN_GBM_15M_TARDIO (n=1011). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3571 sube el IC de -0.013 a +0.281 en UPDOWN_GBM_15M_TARDIO (n=3433). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.100 a +0.331 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=324). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.195 a +0.293 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.622 sube el IC de +0.154 a +0.255 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=505). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.242 a +0.272 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1207). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.187 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.038 a +0.290 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=536). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.204 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.025 a +0.294 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=841). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8389 sube el IC de +0.291 a +0.320 en UPDOWN_GBM_IBS_ALTO (n=1021). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.8279 sube el IC de +0.287 a +0.314 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=552). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8745 sube el IC de +0.295 a +0.334 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=420). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.363 a +0.399 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=604). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.365 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=316). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7485 sube el IC de +0.359 a +0.410 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=287). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1822 | +0.091 | +208.22€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1822 | +0.091 | +208.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1441 | +0.096 | +184.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1441 | +0.096 | +184.22€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 277 | +0.066 | +10.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 277 | +0.066 | +10.33€ | 6 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 73 | +0.100 | +14.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 73 | +0.100 | +14.01€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 506 | -0.014 | +59.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 506 | -0.014 | +59.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 365 | -0.037 | +30.80€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 365 | -0.037 | +30.80€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 114 | +0.060 | +22.95€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 114 | +0.060 | +22.95€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 24 | -0.038 | +2.10€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 24 | -0.038 | +2.10€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 38582 | -0.081 | -4844.79€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2099 | +0.028 | -237.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 36483 | -0.087 | -4606.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4437 | -0.116 | -764.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4437 | -0.116 | -764.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2099 | +0.028 | -237.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2099 | +0.028 | -237.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4228 | -0.105 | -852.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4228 | -0.105 | -852.91€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10246 | -0.015 | -928.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10246 | -0.015 | -928.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10062 | -0.102 | -759.15€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10062 | -0.102 | -759.15€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7510 | -0.138 | -1301.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7510 | -0.138 | -1301.19€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 32600 | -0.016 | +3560.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8433 | +0.004 | +1722.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 24167 | -0.024 | +1838.09€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 32600 | -0.016 | +3560.50€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8433 | +0.004 | +1722.41€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 24167 | -0.024 | +1838.09€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 137422 | +0.114 | -5778.02€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18010 | +0.183 | -541.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 600 | -0.025 | -67.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 110512 | +0.105 | -4888.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8300 | +0.102 | -280.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 18334 | +0.107 | -1136.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 60 | -0.145 | +11.46€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 18259 | +0.108 | -1136.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 26754 | +0.128 | -411.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5112 | +0.191 | -160.06€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 18317 | +0.118 | -147.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3283 | +0.085 | -81.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 18385 | +0.096 | -1374.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 70 | -0.111 | -5.12€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 18300 | +0.098 | -1357.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 29217 | +0.123 | -567.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7619 | +0.177 | -133.65€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 18550 | +0.106 | -368.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3036 | +0.100 | -56.09€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 26379 | +0.114 | -1366.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5084 | +0.195 | -258.52€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 503 | +0.009 | -13.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 18811 | +0.093 | -951.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1981 | +0.135 | -142.71€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 18353 | +0.104 | -922.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 65 | -0.082 | +4.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 18275 | +0.105 | -926.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 22070 | +0.196 | -1350.46€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 22070 | +0.196 | -1350.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5047 | +0.176 | -451.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5047 | +0.176 | -451.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2699 | +0.204 | -52.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2699 | +0.204 | -52.12€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 4988 | +0.181 | -400.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 4988 | +0.181 | -400.19€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4339 | +0.247 | -138.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4339 | +0.247 | -138.82€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4918 | +0.188 | -321.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4918 | +0.188 | -321.51€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 975 | +0.428 | -30.50€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 975 | +0.428 | -30.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 384 | +0.438 | -4.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 384 | +0.438 | -4.09€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 382 | +0.430 | -10.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 382 | +0.430 | -10.09€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 196 | +0.404 | -13.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 196 | +0.404 | -13.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 77010 | +0.201 | -5575.15€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 77010 | +0.201 | -5575.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 13227 | +0.185 | -1360.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 13227 | +0.185 | -1360.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 12433 | +0.224 | -435.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 12433 | +0.224 | -435.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 13197 | +0.180 | -1413.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 13197 | +0.180 | -1413.84€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 12505 | +0.220 | -470.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 12505 | +0.220 | -470.97€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 12770 | +0.202 | -848.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 12770 | +0.202 | -848.68€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 12878 | +0.196 | -1045.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 12878 | +0.196 | -1045.72€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 29465 | +0.117 | +219.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 29465 | +0.117 | +219.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 14649 | +0.120 | +180.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 14649 | +0.120 | +180.30€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 14816 | +0.114 | +39.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 14816 | +0.114 | +39.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 1981 | +0.290 | -18.33€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 1981 | +0.290 | -18.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 905 | +0.278 | -25.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 905 | +0.278 | -25.58€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 957 | +0.292 | +1.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 957 | +0.292 | +1.93€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 913 | +0.440 | +1.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 913 | +0.440 | +1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 442 | +0.435 | -5.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 442 | +0.435 | -5.02€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 425 | +0.446 | +5.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 425 | +0.446 | +5.78€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1551 | +0.070 | -63.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 595 | +0.054 | -46.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 956 | +0.080 | -17.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1194 | +0.078 | -27.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 238 | +0.067 | -10.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 956 | +0.080 | -17.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 285 | +0.030 | -39.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 285 | +0.030 | -39.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 57803 | +0.100 | -1492.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4675 | +0.091 | +53.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 53128 | +0.100 | -1545.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 31868 | +0.105 | -367.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4675 | +0.091 | +53.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 27193 | +0.107 | -420.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 11786 | +0.109 | -55.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 11786 | +0.109 | -55.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 14149 | +0.081 | -1069.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 14149 | +0.081 | -1069.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 894 | +0.192 | -112.64€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 894 | +0.192 | -112.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 894 | +0.192 | -112.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 894 | +0.192 | -112.64€ | 3 | 4 |
| ✅ GBM_LATE_15M | 39941 | +0.092 | +20484.49€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 39941 | +0.092 | +20484.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6683 | +0.210 | +5355.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6683 | +0.210 | +5355.48€ | 0 | 24 |
| ✅ GBM_LATE_15M#BTC | 6007 | +0.178 | +4489.47€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6007 | +0.178 | +4489.47€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 7120 | +0.203 | +5485.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7120 | +0.203 | +5485.61€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5592 | +0.041 | +1513.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5592 | +0.041 | +1513.55€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 5643 | -0.031 | +1201.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5643 | -0.031 | +1201.13€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 8896 | -0.033 | +2439.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 8896 | -0.033 | +2439.26€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 43126 | +0.086 | +23325.27€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 43126 | +0.086 | +23325.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8352 | +0.005 | +4273.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8352 | +0.005 | +4273.83€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9094 | +0.013 | +2099.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9094 | +0.013 | +2099.27€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6004 | +0.275 | +6366.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6004 | +0.275 | +6366.28€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7638 | +0.014 | +1851.75€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7638 | +0.014 | +1851.75€ | 1 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6920 | +0.039 | +2833.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6920 | +0.039 | +2833.40€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5118 | +0.298 | +5900.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5118 | +0.298 | +5900.74€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 31683 | +0.178 | +25331.12€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 31683 | +0.178 | +25331.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4813 | +0.224 | +4168.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4813 | +0.224 | +4168.42€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 4986 | +0.150 | +3666.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 4986 | +0.150 | +3666.71€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5064 | +0.222 | +4329.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5064 | +0.222 | +4329.96€ | 0 | 20 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5355 | +0.138 | +4038.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5355 | +0.138 | +4038.76€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 5956 | +0.123 | +4373.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 5956 | +0.123 | +4373.54€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5509 | +0.222 | +4753.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5509 | +0.222 | +4753.74€ | 0 | 26 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8502 | +0.135 | +4120.67€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8502 | +0.135 | +4120.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2530 | +0.143 | +1423.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2530 | +0.143 | +1423.88€ | 0 | 24 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2536 | +0.141 | +1195.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2536 | +0.141 | +1195.53€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2054 | +0.111 | +801.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2054 | +0.111 | +801.81€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 559 | +0.129 | +239.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 559 | +0.129 | +239.17€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 40142 | +0.184 | +31725.04€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#15min | 40142 | +0.184 | +31725.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6372 | +0.237 | +5817.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6372 | +0.237 | +5817.68€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6258 | +0.148 | +4235.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6258 | +0.148 | +4235.51€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6764 | +0.231 | +5992.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6764 | +0.231 | +5992.45€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6602 | +0.139 | +4694.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6602 | +0.139 | +4694.59€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7095 | +0.122 | +4847.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7095 | +0.122 | +4847.61€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7051 | +0.227 | +6137.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7051 | +0.227 | +6137.20€ | 0 | 21 |
| ✅ GBM_LATE_5M | 11131 | +0.196 | +8382.55€ | 1 | 29 |
| ✅ GBM_LATE_5M#5min | 11131 | +0.196 | +8382.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2567 | +0.195 | +2075.92€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2567 | +0.195 | +2075.92€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1037 | +0.178 | +690.79€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1037 | +0.178 | +690.79€ | 0 | 17 |
| ✅ GBM_LATE_5M#ETH | 3279 | +0.195 | +2329.20€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3279 | +0.195 | +2329.20€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 1632 | +0.190 | +1223.67€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1632 | +0.190 | +1223.67€ | 0 | 28 |
| ✅ GBM_LATE_5M#XRP | 1697 | +0.198 | +1248.97€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1697 | +0.198 | +1248.97€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3210 | +0.071 | +1121.66€ | 0 | 9 |
| ✅ GBM_LATE_60M#60min | 3210 | +0.071 | +1121.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1190 | +0.087 | +470.23€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1190 | +0.087 | +470.23€ | 0 | 9 |
| ✅ GBM_LATE_60M#ETH | 1030 | +0.076 | +387.64€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1030 | +0.076 | +387.64€ | 0 | 11 |
| ✅ GBM_LATE_60M#SOL | 990 | +0.045 | +263.79€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 990 | +0.045 | +263.79€ | 1 | 11 |
| 🚫 GBM_LATE_60M_FADE | 537 | -0.246 | -23.84€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 537 | -0.246 | -23.84€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 202 | -0.240 | -11.45€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 202 | -0.240 | -11.45€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 190 | -0.229 | -4.06€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 190 | -0.229 | -4.06€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 145 | -0.269 | -8.33€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 145 | -0.269 | -8.33€ | 4 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1433 | +0.086 | +392.49€ | 1 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1433 | +0.086 | +392.49€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 571 | +0.085 | +150.88€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 571 | +0.085 | +150.88€ | 1 | 14 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 520 | +0.061 | +85.51€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 520 | +0.061 | +85.51€ | 2 | 8 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 342 | +0.125 | +156.11€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 342 | +0.125 | +156.11€ | 2 | 14 |
| ✅ LATE_WINDOW_5MIN | 160 | +0.272 | +152.25€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 160 | +0.272 | +152.25€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 160 | +0.272 | +152.25€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 160 | +0.272 | +152.25€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3250 | +0.102 | +812.63€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3250 | +0.102 | +812.63€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3250 | +0.102 | +812.63€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3250 | +0.102 | +812.63€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 478 | -0.056 | -25.92€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 478 | -0.056 | -25.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 135 | -0.018 | +0.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 135 | -0.018 | +0.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 85 | -0.075 | -7.25€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 85 | -0.075 | -7.25€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 177 | -0.014 | -2.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 177 | -0.014 | -2.73€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3581 | +0.015 | +76.54€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3581 | +0.015 | +76.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 173 | +0.020 | -2.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 173 | +0.020 | -2.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 726 | +0.015 | +34.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 726 | +0.015 | +34.23€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1288 | +0.025 | +28.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1288 | +0.025 | +28.93€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 754 | +0.011 | +0.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 754 | +0.011 | +0.86€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 437 | +0.010 | +20.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 437 | +0.010 | +20.39€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1684 | -0.039 | -25.24€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1684 | -0.039 | -25.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 481 | -0.030 | -10.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 481 | -0.030 | -10.72€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 568 | -0.014 | +6.41€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 568 | -0.014 | +6.41€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 635 | -0.068 | -20.94€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 635 | -0.068 | -20.94€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 7736 | -0.028 | -11.51€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3657 | -0.038 | -89.10€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4079 | -0.019 | +77.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 223 | -0.029 | -1.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 114 | -0.009 | +3.48€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 109 | -0.050 | -4.85€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1943 | -0.019 | +18.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 919 | -0.024 | -2.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1024 | -0.015 | +21.74€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 848 | -0.024 | +12.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 424 | -0.042 | -10.43€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 424 | -0.005 | +23.33€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1666 | -0.047 | -79.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 771 | -0.060 | -66.77€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 895 | -0.035 | -13.13€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1505 | -0.019 | +30.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 717 | -0.035 | -11.25€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 788 | -0.004 | +41.75€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1551 | -0.030 | +7.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 712 | -0.035 | -1.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 839 | -0.026 | +8.74€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 46632 | -0.001 | +2386.66€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 46632 | -0.001 | +2386.66€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8387 | +0.026 | +1082.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8387 | +0.026 | +1082.88€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6773 | -0.033 | -77.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6773 | -0.033 | -77.51€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 8499 | +0.024 | +882.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 8499 | +0.024 | +882.25€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6608 | -0.047 | -136.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6608 | -0.047 | -136.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7866 | -0.004 | +245.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7866 | -0.004 | +245.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 8499 | +0.014 | +390.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 8499 | +0.014 | +390.17€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6487 | -0.060 | -160.24€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6487 | -0.060 | -160.24€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1662 | -0.079 | -42.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1662 | -0.079 | -42.11€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 758 | -0.120 | -32.30€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 758 | -0.120 | -32.30€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1933 | -0.078 | -42.60€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1933 | -0.078 | -42.60€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 116158 | -0.075 | +1908.04€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 116158 | -0.075 | +1908.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 20135 | -0.076 | +1048.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 20135 | -0.076 | +1048.73€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 17516 | -0.099 | -943.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 17516 | -0.099 | -943.38€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 20431 | -0.067 | +1164.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 20431 | -0.067 | +1164.19€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 17056 | -0.095 | -516.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 17056 | -0.095 | -516.29€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 20877 | -0.054 | +392.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 20877 | -0.054 | +392.62€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 20143 | -0.065 | +762.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 20143 | -0.065 | +762.17€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8685 | -0.033 | -177.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8685 | -0.033 | -177.54€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1963 | -0.045 | -22.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1963 | -0.045 | -22.09€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2573 | -0.026 | -41.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2573 | -0.026 | -41.88€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1182 | -0.054 | -27.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1182 | -0.054 | -27.28€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 958 | -0.030 | -34.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 958 | -0.030 | -34.58€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1593 | +0.123 | +648.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1457 | +0.129 | +636.03€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 342 | +0.145 | +182.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 342 | +0.145 | +182.81€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#DOGE | 300 | +0.119 | +104.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 300 | +0.119 | +104.66€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 293 | +0.134 | +138.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 293 | +0.134 | +138.98€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 257 | +0.152 | +142.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 257 | +0.152 | +142.42€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 265 | +0.088 | +67.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 265 | +0.088 | +67.16€ | 0 | 2 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1309 | -0.015 | -16.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1309 | -0.015 | -16.16€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 253 | +0.002 | +9.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 253 | +0.002 | +9.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 229 | -0.011 | +0.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 229 | -0.011 | +0.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 344 | -0.038 | -22.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 344 | -0.038 | -22.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 273 | +0.002 | -0.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 273 | +0.002 | -0.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 210 | -0.024 | -4.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 210 | -0.024 | -4.07€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 856 | -0.068 | -38.70€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 397 | -0.114 | -77.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 308 | -0.145 | -67.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 306 | -0.029 | +26.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 220 | -0.022 | +26.74€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 153 | -0.023 | +12.62€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 123 | -0.028 | +7.72€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 651 | -0.082 | -33.30€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1058 | -0.207 | -61.32€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 422 | -0.207 | -39.74€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 366 | -0.212 | -40.02€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 358 | -0.217 | -32.06€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 312 | -0.226 | -37.75€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 278 | -0.193 | +10.48€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 259 | -0.190 | +7.34€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 937 | -0.211 | -70.44€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 428 | +0.395 | +404.32€ | 0 | 13 |
| ✅ RESOLUTION_SNIPER#BTC | 56 | +0.138 | +48.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 56 | +0.138 | +48.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 106 | +0.361 | +89.36€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 106 | +0.361 | +89.36€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 266 | +0.459 | +266.69€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 266 | +0.459 | +266.69€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 428 | +0.395 | +404.32€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 703 | +0.028 | +29.74€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 703 | +0.028 | +29.74€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 300 | +0.023 | +3.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 300 | +0.023 | +3.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 57 | -0.025 | -4.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 57 | -0.025 | -4.51€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 72 | +0.000 | +1.29€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 72 | +0.000 | +1.29€ | 2 | 2 |
| ✅ STREAK_FADE_15M#XRP | 274 | +0.051 | +29.60€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 274 | +0.051 | +29.60€ | 0 | 6 |
| ✅ STREAK_FADE_5M | 3415 | -0.021 | -132.25€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3415 | -0.021 | -132.25€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1051 | -0.022 | -37.52€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 588 | -0.027 | -26.12€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 588 | -0.027 | -26.12€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 162 | -0.043 | -14.36€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 162 | -0.043 | -14.36€ | 3 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1614 | -0.016 | -54.26€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1614 | -0.016 | -54.26€ | 3 | 0 |
| ✅ STREAK_FADE_60M | 96 | -0.051 | -9.44€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 96 | -0.051 | -9.44€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 40 | -0.071 | -3.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 40 | -0.071 | -3.54€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 56 | -0.035 | -5.90€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 56 | -0.035 | -5.90€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10529 | +0.018 | +98.70€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10529 | +0.018 | +98.70€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2684 | +0.019 | +24.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2684 | +0.019 | +24.09€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2712 | +0.020 | +39.14€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2712 | +0.020 | +39.14€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2885 | +0.009 | -1.53€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2885 | +0.009 | -1.53€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2248 | +0.023 | +37.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2248 | +0.023 | +37.00€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9604 | +0.013 | -49.15€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9604 | +0.013 | -49.15€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3858 | +0.017 | -9.11€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3858 | +0.017 | -9.11€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3610 | +0.011 | -28.48€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3610 | +0.011 | -28.48€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2136 | +0.010 | -11.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2136 | +0.010 | -11.56€ | 1 | 0 |
| ✅ UPDOWN_GBM | 72360 | +0.052 | +6309.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 18233 | +0.083 | +4018.40€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2350 | +0.005 | +20.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 47316 | +0.048 | +2188.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4213 | +0.009 | +83.02€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6844 | +0.089 | +1077.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1569 | +0.157 | +699.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 15043 | +0.055 | +1285.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2307 | +0.090 | +565.20€ | 0 | 9 |
| ✅ UPDOWN_GBM#BTC#240min | 619 | +0.012 | +11.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 10154 | +0.060 | +647.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1873 | +0.006 | +56.95€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 90 | -0.065 | +3.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8197 | +0.066 | +852.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1550 | +0.147 | +609.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6569 | +0.048 | +244.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 16270 | +0.043 | +1028.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4226 | +0.063 | +603.60€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 606 | +0.007 | +11.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 9905 | +0.042 | +392.99€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1451 | +0.013 | +17.80€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 82 | -0.107 | +2.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 15950 | +0.030 | +715.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4488 | +0.034 | +357.00€ | 0 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 582 | -0.005 | +0.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 9917 | +0.034 | +354.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 889 | +0.008 | +8.28€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 74 | -0.132 | -4.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10054 | +0.062 | +1353.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4093 | +0.101 | +1183.34€ | 0 | 11 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5573 | +0.037 | +169.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 246 | -0.101 | +1.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 803 | +0.363 | +290.13€ | 0 | 10 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 803 | +0.363 | +290.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 421 | +0.365 | +148.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 421 | +0.365 | +148.49€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 382 | +0.359 | +141.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 382 | +0.359 | +141.63€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19193 | -0.024 | +4562.27€ | 3 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19193 | -0.024 | +4562.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1711 | -0.056 | +506.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1711 | -0.056 | +506.13€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3336 | -0.111 | +140.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3336 | -0.111 | +140.06€ | 3 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 944 | +0.216 | +766.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 944 | +0.216 | +766.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2280 | +0.216 | +1474.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2280 | +0.216 | +1474.11€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5461 | -0.065 | +688.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5461 | -0.065 | +688.37€ | 5 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5461 | -0.064 | +986.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5461 | -0.064 | +986.78€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 216 | +0.032 | +5.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 216 | +0.032 | +5.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 216 | +0.032 | +5.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 216 | +0.032 | +5.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1361 | +0.291 | +1149.46€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1361 | +0.291 | +1149.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 735 | +0.287 | +583.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 735 | +0.287 | +583.82€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 626 | +0.295 | +565.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 626 | +0.295 | +565.64€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 808 | -0.110 | -80.89€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 808 | -0.110 | -80.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 245 | -0.075 | -16.57€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 245 | -0.075 | -16.57€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 86 | -0.159 | -8.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 86 | -0.159 | -8.64€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 94 | -0.188 | -6.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 94 | -0.188 | -6.32€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3405 | +0.304 | +1645.36€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1238 | +0.257 | +165.44€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1309 | +0.299 | +589.06€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 858 | +0.379 | +890.86€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**✅ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: IC=+0.017 n=891 — no justifica filtro, seguir monitorizando
  - _Datos_: n=891 IC=+0.017 PNL=+31.91€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 695 celda(s) pasan gate riguroso completo de 2645 evaluadas (n>=40) y 3672 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=4481 IC=+0.034 PNL=+357.16€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1309/15 IC=+0.299 PNL=+589.06€ | BTC: n=1238/15 IC=+0.257 PNL=+165.44€ | SOL: n=858/15 IC=+0.379 PNL=+890.86€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.135 n=755/60 | contraria IC=+0.193 n=783 | gap=-0.058 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=440, boost estimado=+0.014. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1449/40 IC=+0.013 PNL=+17.85€ | BTC#60min: n=1871/40 IC=+0.006 PNL=+56.93€ | SOL#60min: n=887/40 IC=+0.008 PNL=+7.71€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.047 n=524728 | tras_1loss IC=+0.094 n=399835 | tras_2loss IC=+0.063 n=162287/40 | gap=-0.016 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.08 con n=704 PNL=+534.92€
  - _Datos_: n=704 IC=+0.204 PNL=+534.92€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.08 con n=777 PNL=+473.27€
  - _Datos_: n=777 IC=+0.180 PNL=+473.27€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=2778 PNL=+1558.09€
  - _Datos_: n=2778 IC=+0.334 PNL=+1558.09€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=620 IC=+0.076 PNL=+72.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=620 IC=+0.076 PNL=+72.79€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=77 IC=+0.183 PNL=+51.33€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=77 IC=+0.183 PNL=+51.33€

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
  - _Estado_: n=2836 IC=+0.006 PNL=+0.34€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2836 IC=+0.006 PNL=+0.34€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1371 IC=+0.013 PNL=+82.16€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1371 IC=+0.013 PNL=+82.16€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=891 IC=+0.017 PNL=+31.91€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=891 IC=+0.017 PNL=+31.91€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.181 > 0.1 con n=4506 PNL=+2877.43€
  - _Datos_: n=4506 IC=+0.181 PNL=+2877.43€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2306 IC=+0.090 PNL=+564.70€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2306 IC=+0.090 PNL=+564.70€

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
  - _Estado_: n=932 IC=+0.036 PNL=+87.77€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=932 IC=+0.036 PNL=+87.77€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=111 IC=+0.013 PNL=+1.55€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=111 IC=+0.013 PNL=+1.55€

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
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.270 n=159) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=159 IC=+0.270 PNL=+150.25€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.128 > 0.02 con n=918 PNL=+394.65€
  - _Datos_: n=918 IC=+0.128 PNL=+394.65€

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
  - _Estado_: n=28039 IC=+0.073 PNL=+4074.74€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=28039 IC=+0.073 PNL=+4074.74€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.137 < -0.1 con n=444 PNL=+53.99€
  - _Datos_: n=444 IC=-0.137 PNL=+53.99€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3038 IC=+0.065 PNL=+365.85€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3038 IC=+0.065 PNL=+365.85€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=131 IC=-0.109 PNL=+3.02€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=131 IC=-0.109 PNL=+3.02€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.113 > 0.1 con n=743 PNL=+200.62€
  - _Datos_: n=743 IC=+0.113 PNL=+200.62€

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
  - _Estado_: n=29953 IC=-0.133 PNL=+2431.53€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=29953 IC=-0.133 PNL=+2431.53€

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
  - _Estado_: n=3029 IC=+0.133 PNL=+1818.47€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3029 IC=+0.133 PNL=+1818.47€

**⏳ H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: 40
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=7431 IC=+0.048 PNL=+573.62€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7431 IC=+0.048 PNL=+573.62€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.091 > 0.08 con n=3264 PNL=+1732.29€
  - _Datos_: n=3264 IC=+0.091 PNL=+1732.29€

**⏳ H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: 80
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: 0/80 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.222 < -0.1 con n=3069 PNL=-227.40€
  - _Datos_: n=3069 IC=-0.222 PNL=-227.40€

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
  - _Estado_: n=64 IC=+0.000 PNL=+5.04€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=64 IC=+0.000 PNL=+5.04€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.100 n=1649) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1649 IC=+0.100 PNL=+360.22€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.413 n=550) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=550 IC=+0.413 PNL=+791.24€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=13221 IC=+0.185 PNL=-1357.97€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=13221 IC=+0.185 PNL=-1357.97€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.210 > 0.1 con n=219 PNL=+137.71€
  - _Datos_: n=219 IC=+0.210 PNL=+137.71€
