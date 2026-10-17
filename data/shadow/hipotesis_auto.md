# Hipótesis automáticas — 2026-10-17 08:03 UTC
_Generado por shadow_postmortem.py sobre 935252 resoluciones (PNL=+120478.78€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.261 (n=178)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=608)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.241 (n=740)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `67.0` → IC=+0.190 (n=266)

  - _Acción_: Kelly boost +0.95€ cuando `n_total_lado` > 67.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.8017` → IC=+0.273 (n=527)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.8017 (IC base=+0.138)

- **PATRÓN** `banda_z` > `7.948` → IC=+0.190 (n=359)

  - _Acción_: Kelly boost +0.95€ cuando `banda_z` > 7.948 (IC base=+0.138)

- **PATRÓN** `ballenas_wallet_edge_medio` > `0.727` → IC=+0.137 (n=709)

  - _Acción_: Kelly boost +0.69€ cuando `ballenas_wallet_edge_medio` > 0.727 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=284)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.139 (n=532)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 11.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=858)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `99.0` → IC=+0.153 (n=428)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 99.0 (IC base=+0.138)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.555` → IC=+0.274 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.555 (IC base=+0.144)

- **PATRÓN** `n_total_lado` > `71.0` → IC=+0.208 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 71.0 (IC base=+0.144)

- **PATRÓN** `banda_hit_calibrado` > `0.6199` → IC=+0.272 (n=441)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6199 (IC base=+0.144)

- **PATRÓN** `banda_z` > `9.852` → IC=+0.227 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.852 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=233)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=759)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `102.0` → IC=+0.155 (n=389)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 102.0 (IC base=+0.144)

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
- **FILTRO** `restante_s_al_confirmar` < `143.23` → IC=-0.204 (n=9725)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 143.23
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=29175)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.61` → IC=-0.288 (n=1069)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.61
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3209)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.58` → IC=-0.206 (n=2543)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.58
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=7630)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.28` → IC=-0.284 (n=1893)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.28
  - _Potencial_: sin este filtro IC_bueno=-0.089 (n=5680)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.211 (n=20728)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.106)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.138 (n=4220)

  - _Acción_: Kelly boost +0.69€ cuando `libro_spread` < 0.01 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `9221.3679` → IC=+0.178 (n=1898)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9221.3679 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=17540)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=21375)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.226 (n=16236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=7020)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7188.024` → IC=+0.161 (n=2709)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 7188.024 (IC base=+0.125)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=1995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.196 (n=1954)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 17.0 (IC base=+0.195)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.197 (n=2450)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `16325.2152` → IC=+0.203 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16325.2152 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.194 (n=1752)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 7.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.191 (n=1959)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 17.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=2509)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `16122.9185` → IC=+0.198 (n=647)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 16122.9185 (IC base=+0.187)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=455)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `6860.5651` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `libro_liquidez` > 6860.5651 (IC base=+0.081)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1076)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.088)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.167 (n=4023)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.160 (n=2751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 12.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1284)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.222 (n=1785)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.360 (n=655)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.218 (n=2094)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1008)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.146 (n=862)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 15.0 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.262 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.140)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=789)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `1860.6193` → IC=+0.148 (n=643)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1860.6193 (IC base=+0.140)

- **PATRÓN** `libro_liquidez` > `4449.086` → IC=+0.160 (n=151)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 4449.086 (IC base=+0.071)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.242 (n=941)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.82` → IC=+0.411 (n=1157)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.82 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.149 (n=1277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 7.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.158 (n=673)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 7.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.153 (n=845)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.159 (n=429)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.254 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.127)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.205 (n=17398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=14797)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=7210)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.200)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=4029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.179 (n=3816)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 17.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.180 (n=3922)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.73 (IC base=+0.177)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.227 (n=1977)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.232 (n=1321)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.313 (n=703)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.225)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.187 (n=3963)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.185 (n=3378)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=3120)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.257 (n=3447)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.78` → IC=+0.354 (n=1167)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.193 (n=3882)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.193 (n=2490)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.198 (n=1337)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` > 0.73 (IC base=+0.188)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.432 (n=746)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.442 (n=772)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `7390.2621` → IC=+0.443 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7390.2621 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `10.0` → IC=+0.449 (n=195)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.438)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.451 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.438)

- **PATRÓN** `libro_liquidez` > `18390.1556` → IC=+0.440 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18390.1556 (IC base=+0.438)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.446 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.430)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.430)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.433 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.430)

- **PATRÓN** `libro_liquidez` > `4389.547` → IC=+0.439 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4389.547 (IC base=+0.430)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=22527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.246 (n=22747)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.201)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.192 (n=3344)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7207)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=10067)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=4707)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.225 (n=4648)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3294)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.187 (n=3856)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 17.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.180 (n=7189)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 12.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.210 (n=5150)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.180)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` > `0.775` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.775
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=9)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=4741)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=3634)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.276 (n=3209)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.221)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.204 (n=3747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.259 (n=3361)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=3742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.196 (n=3264)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=3917)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.196)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.190 (n=8139)

  - _Acción_: Kelly boost +0.95€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.138 (n=8037)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `2.41` → IC=+0.137 (n=7459)

  - _Acción_: Kelly boost +0.69€ cuando `lag_apertura_s` < 2.41 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.193 (n=4032)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.142 (n=4072)

  - _Acción_: Kelly boost +0.71€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=4940)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.79` → IC=+0.145 (n=3701)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.79 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.187 (n=4107)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.133 (n=4389)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `2.26` → IC=+0.135 (n=3772)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 2.26 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.299 (n=1589)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.291 (n=1575)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.290)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.376 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.290)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.285 (n=720)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.277)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.279 (n=621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.277)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.347 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.277)

- **PATRÓN** `libro_liquidez` > `5416.3978` → IC=+0.288 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5416.3978 (IC base=+0.277)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.320 (n=510)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.297 (n=757)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.293)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.387 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.293)

- **PATRÓN** `libro_liquidez` > `2100.1274` → IC=+0.307 (n=242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2100.1274 (IC base=+0.293)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.440 (n=479)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.441 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=702)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.441 (n=833)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.438 (n=351)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.441 (n=237)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.437 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.442 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.451 (n=347)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.447)

- **PATRÓN** `py_entrada` < `0.93` → IC=+0.452 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.93 (IC base=+0.447)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.447)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.448 (n=382)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4783` → IC=+0.135 (n=12613)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.4783 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.120 (n=13202)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 18.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.245 (n=4208)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` > `0.7962` → IC=+0.266 (n=716)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7962 (IC base=+0.119)

- **PATRÓN** `dist_vwap_pct` < `0.3734` → IC=+0.254 (n=3470)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3734 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.953` → IC=+0.189 (n=4766)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.953 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` < `1.2036` → IC=+0.254 (n=3629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2036 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `0.6188` → IC=+0.260 (n=3629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6188 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.3019` → IC=+0.234 (n=1281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3019 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` > `2.3388` → IC=+0.225 (n=4055)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3388 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.122 (n=10742)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.02 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.5675` → IC=+0.141 (n=15557)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` < 0.5675 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.1543` → IC=+0.184 (n=5628)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1543 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.6958` → IC=+0.181 (n=2649)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6958 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.0501` → IC=+0.180 (n=2729)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0501 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2946` → IC=+0.228 (n=1495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2946 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.6706` → IC=+0.204 (n=3412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6706 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `109.0` → IC=+0.218 (n=10078)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 109.0 (IC base=+0.074)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.213 (n=926)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=+0.193)

- **PATRÓN** `drift_60min` |x|≤ `0.348` → IC=+0.198 (n=2759)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.99€ cuando `drift_60min` |x|≤ 0.348 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.204 (n=1336)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.199 (n=1851)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `0.977` → IC=+0.276 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.977 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.036` → IC=+0.281 (n=1206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.036 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.2324` → IC=+0.243 (n=489)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2324 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.2844` → IC=+0.207 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2844 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.207 (n=2923)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `2088.76` → IC=+0.211 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2088.76 (IC base=+0.193)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.205 (n=2151)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.238 (n=2308)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.238 (n=1047)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.088` → IC=+0.263 (n=770)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.088 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=844)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.5181` → IC=+0.255 (n=2307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5181 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` < `0.0937` → IC=+0.238 (n=2053)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0937 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.2867` → IC=+0.250 (n=310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2867 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.237 (n=724)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.6447` → IC=+0.243 (n=723)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6447 (IC base=+0.234)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2568)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `1567.34` → IC=+0.244 (n=2308)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1567.34 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.237 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.234)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.240 (n=990)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.225)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.225 (n=1021)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.225)

- **PATRÓN** `drift_60min` |x|≤ `0.1777` → IC=+0.249 (n=1500)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1777 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.237 (n=2363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.225)

- **PATRÓN** `ibs_20min` > `0.9577` → IC=+0.273 (n=750)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9577 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` > `0.1301` → IC=+0.233 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1301 (IC base=+0.225)

- **PATRÓN** `dist_vwap_pct` < `0.3432` → IC=+0.226 (n=2162)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3432 (IC base=+0.225)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.434` → IC=+0.267 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.434 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` < `1.2335` → IC=+0.227 (n=2250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2335 (IC base=+0.225)

- **PATRÓN** `volumen_regimen` > `0.6211` → IC=+0.230 (n=2251)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6211 (IC base=+0.225)

- **PATRÓN** `volumen_pendiente_norm` > `0.2763` → IC=+0.254 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2763 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` < `1.5114` → IC=+0.226 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5114 (IC base=+0.225)

- **PATRÓN** `volumen_spike_ratio` > `2.4315` → IC=+0.254 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4315 (IC base=+0.225)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.151 (n=2310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0058 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.165 (n=769)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=879)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.132)

- **PATRÓN** `ibs_20min` < `0.7293` → IC=+0.176 (n=2305)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7293 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` < `0.1328` → IC=+0.154 (n=2141)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1328 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.086` → IC=+0.148 (n=373)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 11.086 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.216` → IC=+0.141 (n=2107)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.216 (IC base=+0.132)

- **PATRÓN** `volumen_regimen` < `1.1913` → IC=+0.140 (n=2305)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1913 (IC base=+0.132)

- **PATRÓN** `volumen_pendiente_norm` > `0.0966` → IC=+0.160 (n=844)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0966 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` < `2.4535` → IC=+0.141 (n=2186)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_spike_ratio` < 2.4535 (IC base=+0.132)

- **PATRÓN** `volumen_spike_ratio` > `1.415` → IC=+0.136 (n=2186)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.415 (IC base=+0.132)

- **PATRÓN** `ballena_activa_n` < `219.0` → IC=+0.170 (n=932)

  - _Acción_: Kelly boost +0.85€ cuando `ballena_activa_n` < 219.0 (IC base=+0.132)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.215 (n=953)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.198 (n=2995)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.196 (n=2560)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 15.0 (IC base=+0.193)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=1091)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.333` → IC=+0.270 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.333 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` < `0.098` → IC=+0.197 (n=2525)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.098 (IC base=+0.193)

- **PATRÓN** `volumen_pendiente_norm` > `0.351` → IC=+0.210 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.351 (IC base=+0.193)

- **PATRÓN** `volumen_spike_ratio` > `2.6919` → IC=+0.209 (n=1254)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6919 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.200 (n=3396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `1855.62` → IC=+0.199 (n=1904)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1855.62 (IC base=+0.193)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.221 (n=2244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.6073` → IC=+0.220 (n=2548)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6073 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.247 (n=956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.0107` → IC=+0.272 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0107 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.494` → IC=+0.254 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.494 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.3473` → IC=+0.255 (n=365)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3473 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.7245` → IC=+0.214 (n=1062)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7245 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `2.726` → IC=+0.227 (n=1095)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.726 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `2068.0889` → IC=+0.231 (n=850)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2068.0889 (IC base=+0.215)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.217 (n=2077)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 25.0 (IC base=+0.215)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.135 (n=143)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=3459)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.160 (n=513)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0036 (IC base=+0.052)

- **PATRÓN** `ibs_20min` > `0.9547` → IC=+0.225 (n=511)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9547 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` > `0.1359` → IC=+0.324 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1359 (IC base=+0.052)

- **PATRÓN** `dist_vwap_pct` < `0.7574` → IC=+0.329 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.7574 (IC base=+0.052)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.086` → IC=+0.185 (n=1098)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.086 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.332 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.052)

- **PATRÓN** `volumen_regimen` > `1.2251` → IC=+0.348 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2251 (IC base=+0.052)

- **PATRÓN** `volumen_pendiente_norm` > `0.2986` → IC=+0.341 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2986 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` < `1.4081` → IC=+0.339 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4081 (IC base=+0.052)

- **PATRÓN** `volumen_spike_ratio` > `2.2427` → IC=+0.321 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2427 (IC base=+0.052)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.332 (n=493)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 133.0 (IC base=+0.052)

- **PATRÓN** `ibs_20min` < `0.0962` → IC=+0.169 (n=901)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.0962 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.3267` → IC=+0.140 (n=443)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.3267 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.1308` → IC=+0.134 (n=1435)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1308 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` < `0.8471` → IC=+0.146 (n=1051)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` < 0.8471 (IC base=+0.034)

- **PATRÓN** `volumen_regimen` > `1.1677` → IC=+0.133 (n=526)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_regimen` > 1.1677 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.2851` → IC=+0.198 (n=203)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_pendiente_norm` > 0.2851 (IC base=+0.034)

- **PATRÓN** `volumen_spike_ratio` > `2.1513` → IC=+0.152 (n=685)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 2.1513 (IC base=+0.034)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.160 (n=95)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=525)

- **FILTRO** `ibs_20min` < `0.2791` → IC=-0.194 (n=155)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2791
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=465)

- **FILTRO** `ibs_20min` > `0.2195` → IC=-0.132 (n=3404)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2195
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=1679)

- **FILTRO** `sigma_ewma_delta_pct` > `8.673` → IC=-0.234 (n=529)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.673
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4554)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.182 (n=212)

  - _Acción_: Kelly boost +0.91€ cuando `ibs_20min` > 0.7857 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `1.0167` → IC=+0.270 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0167 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.6239` → IC=+0.256 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6239 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.37` → IC=+0.141 (n=218)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 2.37 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` > `1.0006` → IC=+0.309 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0006 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.0778` → IC=+0.276 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0778 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.1931` → IC=+0.277 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1931 (IC base=+0.032)

- **PATRÓN** `ibs_20min` < `0.2195` → IC=+0.150 (n=1679)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.2195 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.1921` → IC=+0.276 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1921 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4351` → IC=+0.272 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4351 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.301 (n=305)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0797` → IC=+0.300 (n=298)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0797 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4034` → IC=+0.300 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4034 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6215` → IC=-0.179 (n=915)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6215
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=2754)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.162 (n=920)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=2749)

- **FILTRO** `ibs_20min` > `0.7531` → IC=-0.204 (n=1334)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7531
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=4009)

- **PATRÓN** `dist_vwap_pct` > `0.749` → IC=+0.330 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.749 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` < `0.2587` → IC=+0.296 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2587 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` < `1.1432` → IC=+0.292 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1432 (IC base=-0.069)

- **PATRÓN** `volumen_regimen` > `0.7047` → IC=+0.309 (n=549)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7047 (IC base=-0.069)

- **PATRÓN** `volumen_pendiente_norm` < `0.1006` → IC=+0.298 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1006 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` < `1.4142` → IC=+0.320 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4142 (IC base=-0.069)

- **PATRÓN** `volumen_spike_ratio` > `1.8376` → IC=+0.294 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8376 (IC base=-0.069)

- **PATRÓN** `dist_vwap_pct` > `0.8152` → IC=+0.272 (n=248)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8152 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0712` → IC=+0.280 (n=657)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0712 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1019` → IC=+0.277 (n=504)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1019 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1737` → IC=+0.260 (n=1169)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1737 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.424` → IC=+0.258 (n=1328)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.424 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.206 (n=5549)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0097 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.3257` → IC=+0.168 (n=16644)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3257 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.9747` → IC=+0.300 (n=1239)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9747 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.63` → IC=+0.160 (n=7463)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.63 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1724` → IC=+0.259 (n=6118)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1724 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6887` → IC=+0.264 (n=5466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6887 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.273 (n=1824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.2664` → IC=+0.266 (n=4439)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2664 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.290 (n=9368)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.162 (n=5353)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0092 (IC base=+0.075)

- **PATRÓN** `ibs_20min` < `0.6609` → IC=+0.144 (n=16033)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6609 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.2426` → IC=+0.260 (n=4974)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2426 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.1939` → IC=+0.263 (n=1680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1939 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2934` → IC=+0.313 (n=1059)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2934 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` < `1.4557` → IC=+0.288 (n=2395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4557 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.2637` → IC=+0.281 (n=3257)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2637 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.290 (n=7103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.075)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3707` → IC=-0.172 (n=1515)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3707
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=3080)

- **FILTRO** `ibs_20min` > `0.7451` → IC=-0.208 (n=959)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7451
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2879)

- **FILTRO** `sigma_ewma_delta_pct` > `4.495` → IC=-0.202 (n=839)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.495
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=2999)

- **PATRÓN** `ibs_20min` > `0.9142` → IC=+0.302 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9142 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.059` → IC=+0.214 (n=812)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.059 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.294 (n=290)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4469` → IC=+0.235 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4469 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.2496` → IC=+0.267 (n=680)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2496 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.269 (n=1009)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.1597` → IC=+0.160 (n=960)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1597 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0738` → IC=+0.411 (n=415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0738 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `2.5483` → IC=+0.402 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5483 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `22.0` → IC=+0.395 (n=426)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 22.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1138` → IC=+0.210 (n=839)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1138 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.186 (n=1614)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` < 1.1951 (IC base=+0.024)

- **PATRÓN** `volumen_regimen` > `0.6813` → IC=+0.195 (n=1442)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_regimen` > 0.6813 (IC base=+0.024)

- **PATRÓN** `volumen_pendiente_norm` > `0.2738` → IC=+0.219 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2738 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` < `1.425` → IC=+0.212 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.425 (IC base=+0.024)

- **PATRÓN** `volumen_spike_ratio` > `2.4515` → IC=+0.194 (n=530)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` > 2.4515 (IC base=+0.024)

- **PATRÓN** `ballena_activa_n` < `220.0` → IC=+0.237 (n=697)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 220.0 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.1124` → IC=+0.231 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1124 (IC base=-0.000)

- **PATRÓN** `volumen_regimen` > `0.6194` → IC=+0.234 (n=1032)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6194 (IC base=-0.000)

- **PATRÓN** `volumen_pendiente_norm` > `0.272` → IC=+0.289 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.272 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` < `1.5333` → IC=+0.233 (n=432)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5333 (IC base=-0.000)

- **PATRÓN** `volumen_spike_ratio` > `2.1657` → IC=+0.249 (n=445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1657 (IC base=-0.000)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.304 (n=816)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.263)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.269 (n=2569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.263)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.308 (n=1282)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.263)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.297 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.263)

- **PATRÓN** `volumen_pendiente_norm` < `0.0981` → IC=+0.275 (n=2122)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0981 (IC base=+0.263)

- **PATRÓN** `volumen_spike_ratio` > `1.6102` → IC=+0.269 (n=2360)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6102 (IC base=+0.263)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.274 (n=2892)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.263)

- **PATRÓN** `libro_liquidez` > `1979.81` → IC=+0.285 (n=1110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.81 (IC base=+0.263)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.327 (n=951)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.1822` → IC=+0.305 (n=923)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1822 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.321 (n=808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.290)

- **PATRÓN** `ibs_20min` < `0.3659` → IC=+0.293 (n=2098)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3659 (IC base=+0.290)

- **PATRÓN** `ibs_20min` > `0.1124` → IC=+0.294 (n=1398)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1124 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.647` → IC=+0.313 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.647 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` < `0.1968` → IC=+0.289 (n=2042)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1968 (IC base=+0.290)

- **PATRÓN** `volumen_pendiente_norm` > `0.3403` → IC=+0.309 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3403 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` < `1.7224` → IC=+0.299 (n=879)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7224 (IC base=+0.290)

- **PATRÓN** `volumen_spike_ratio` > `2.6522` → IC=+0.300 (n=906)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6522 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `2060.32` → IC=+0.313 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2060.32 (IC base=+0.290)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.286 (n=1331)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 20.0 (IC base=+0.290)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7391` → IC=-0.182 (n=997)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7391
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=2993)

- **PATRÓN** `ibs_20min` > `0.8828` → IC=+0.170 (n=940)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.8828 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.1516` → IC=+0.229 (n=710)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1516 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3691` → IC=+0.228 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3691 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `1.0108` → IC=+0.242 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0108 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.249 (n=412)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.3969` → IC=+0.246 (n=420)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3969 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.261 (n=1129)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3327` → IC=+0.226 (n=971)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3327 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.0399` → IC=+0.230 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0399 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.1025` → IC=+0.243 (n=831)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1025 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.286 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.262 (n=564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7982 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4393` → IC=+0.257 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4393 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.251 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7619` → IC=-0.207 (n=1756)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.302 (n=1760)

- **FILTRO** `ibs_20min` > `0.6512` → IC=-0.236 (n=864)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6512
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=2597)

- **FILTRO** `sigma_ewma_delta_pct` > `8.544` → IC=-0.239 (n=397)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.544
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=3064)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.302 (n=1760)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.336 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.607` → IC=+0.176 (n=550)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.607 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` < `0.8456` → IC=+0.331 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8456 (IC base=+0.048)

- **PATRÓN** `volumen_regimen` > `0.6274` → IC=+0.319 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6274 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` < `0.159` → IC=+0.318 (n=1373)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.159 (IC base=+0.048)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.356 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.048)

- **PATRÓN** `volumen_spike_ratio` < `1.4421` → IC=+0.341 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4421 (IC base=+0.048)

- **PATRÓN** `ballena_activa_n` < `57.0` → IC=+0.335 (n=1288)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 57.0 (IC base=+0.048)

- **PATRÓN** `ibs_20min` < `0.55` → IC=+0.141 (n=2288)

  - _Acción_: Kelly boost +0.71€ cuando `ibs_20min` < 0.55 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.4629` → IC=+0.246 (n=1204)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4629 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `0.7052` → IC=+0.261 (n=495)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7052 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` < `0.1001` → IC=+0.241 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1001 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.0753` → IC=+0.254 (n=424)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0753 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `2.4125` → IC=+0.250 (n=1079)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4125 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `53.0` → IC=+0.267 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 53.0 (IC base=+0.030)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.344 (n=1678)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.298 (n=722)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.312 (n=903)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.298)

- **PATRÓN** `ibs_20min` > `0.6516` → IC=+0.330 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6516 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.209` → IC=+0.326 (n=1069)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.209 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.787` → IC=+0.319 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.787 (IC base=+0.298)

- **PATRÓN** `volumen_regimen` > `0.6276` → IC=+0.307 (n=1878)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6276 (IC base=+0.298)

- **PATRÓN** `volumen_pendiente_norm` > `0.28` → IC=+0.340 (n=273)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.28 (IC base=+0.298)

- **PATRÓN** `volumen_spike_ratio` > `1.4247` → IC=+0.310 (n=1799)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4247 (IC base=+0.298)

- **PATRÓN** `libro_liquidez` > `2654.5546` → IC=+0.316 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2654.5546 (IC base=+0.298)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.332 (n=1607)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 42.0 (IC base=+0.298)

- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.332 (n=1327)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0151 (IC base=+0.300)

- **PATRÓN** `drift_60min` |x|≤ `0.1879` → IC=+0.303 (n=876)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1879 (IC base=+0.300)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.312 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.300)

- **PATRÓN** `ibs_20min` < `0.3696` → IC=+0.324 (n=1990)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3696 (IC base=+0.300)

- **PATRÓN** `dist_vwap_pct` > `0.3121` → IC=+0.300 (n=687)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3121 (IC base=+0.300)

- **PATRÓN** `dist_vwap_pct` < `0.2281` → IC=+0.304 (n=1873)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2281 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.54` → IC=+0.312 (n=737)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.54 (IC base=+0.300)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.065` → IC=+0.301 (n=2367)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.065 (IC base=+0.300)

- **PATRÓN** `volumen_regimen` < `0.7186` → IC=+0.304 (n=876)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7186 (IC base=+0.300)

- **PATRÓN** `volumen_regimen` > `1.224` → IC=+0.329 (n=664)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.224 (IC base=+0.300)

- **PATRÓN** `volumen_pendiente_norm` > `0.2816` → IC=+0.351 (n=274)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2816 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` < `1.4133` → IC=+0.309 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4133 (IC base=+0.300)

- **PATRÓN** `volumen_spike_ratio` > `2.1346` → IC=+0.303 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1346 (IC base=+0.300)

- **PATRÓN** `libro_liquidez` > `2423.752` → IC=+0.302 (n=1778)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2423.752 (IC base=+0.300)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.182 (n=4086)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0048 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.222 (n=4086)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0869` → IC=+0.200 (n=4083)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0869 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=12708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.5585` → IC=+0.233 (n=12234)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5585 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1663` → IC=+0.208 (n=5031)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1663 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.328` → IC=+0.258 (n=2414)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.328 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1915` → IC=+0.168 (n=8115)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1915 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.6261` → IC=+0.163 (n=8115)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` > 0.6261 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.203 (n=1783)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6003` → IC=+0.188 (n=3950)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6003 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2004.3184` → IC=+0.183 (n=10929)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 2004.3184 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `96.0` → IC=+0.196 (n=11141)

  - _Acción_: Kelly boost +0.98€ cuando `ballena_activa_n` < 96.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.186 (n=7879)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0069 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.08` → IC=+0.223 (n=3938)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.08 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=4440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.234 (n=11860)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` < `0.1751` → IC=+0.173 (n=8339)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` < 0.1751 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.086` → IC=+0.195 (n=1941)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.086 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.727` → IC=+0.178 (n=10387)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 2.727 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `1.1787` → IC=+0.162 (n=8428)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1787 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.2922` → IC=+0.224 (n=1735)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2922 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `2.626` → IC=+0.186 (n=3688)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.626 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `66.0` → IC=+0.195 (n=9506)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 66.0 (IC base=+0.177)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.233 (n=690)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.209)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.228 (n=2050)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.213 (n=2149)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=1385)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.209)

- **PATRÓN** `ibs_20min` > `0.9259` → IC=+0.291 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9259 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.07` → IC=+0.332 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.07 (IC base=+0.209)

- **PATRÓN** `volumen_pendiente_norm` > `0.2807` → IC=+0.267 (n=307)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2807 (IC base=+0.209)

- **PATRÓN** `volumen_spike_ratio` > `1.4398` → IC=+0.209 (n=1933)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4398 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2015.02` → IC=+0.216 (n=929)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2015.02 (IC base=+0.209)

- **PATRÓN** `sigma_h` < `0.008` → IC=+0.246 (n=1603)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.245)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.252 (n=729)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.245)

- **PATRÓN** `drift_60min` |x|≤ `0.0967` → IC=+0.298 (n=707)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0967 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.248 (n=1632)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=786)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.245)

- **PATRÓN** `ibs_20min` < `0.2824` → IC=+0.270 (n=1411)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2824 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` < `0.0995` → IC=+0.246 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0995 (IC base=+0.245)

- **PATRÓN** `volumen_pendiente_norm` > `0.2967` → IC=+0.278 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2967 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` < `1.4302` → IC=+0.263 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4302 (IC base=+0.245)

- **PATRÓN** `volumen_spike_ratio` > `2.6638` → IC=+0.246 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6638 (IC base=+0.245)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.249 (n=1791)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.245)

- **PATRÓN** `libro_liquidez` > `1553.364` → IC=+0.256 (n=1603)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1553.364 (IC base=+0.245)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.246 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.245)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.218 (n=616)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1615` → IC=+0.184 (n=1228)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1615 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.172 (n=1943)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3437` → IC=+0.224 (n=1840)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3437 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1371` → IC=+0.217 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1371 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.433` → IC=+0.227 (n=349)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.433 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6901` → IC=+0.168 (n=810)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6901 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2815` → IC=+0.184 (n=292)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2815 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.413` → IC=+0.177 (n=602)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` < 1.413 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.4971` → IC=+0.162 (n=601)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.4971 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `423.0` → IC=+0.160 (n=1763)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 423.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.169 (n=1946)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0059 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2348` → IC=+0.171 (n=1711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2348 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=742)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6154` → IC=+0.203 (n=1944)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6154 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.563` → IC=+0.199 (n=373)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 11.563 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2024` → IC=+0.159 (n=1944)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2024 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0934` → IC=+0.145 (n=1636)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0934 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.1586` → IC=+0.146 (n=599)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.1586 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4963` → IC=+0.150 (n=1825)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4963 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4225` → IC=+0.146 (n=1824)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4225 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `204.0` → IC=+0.173 (n=591)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 204.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.234 (n=941)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3956` → IC=+0.225 (n=1824)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3956 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.302 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.5` → IC=+0.297 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.5 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0999` → IC=+0.212 (n=1767)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0999 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.228 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.213 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.6989` → IC=+0.227 (n=909)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6989 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=2457)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1979.26` → IC=+0.223 (n=939)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1979.26 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.244 (n=1562)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0103 (IC base=+0.233)

- **PATRÓN** `drift_60min` |x|≤ `0.1424` → IC=+0.268 (n=783)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1424 (IC base=+0.233)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=684)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.233)

- **PATRÓN** `ibs_20min` < `0.3558` → IC=+0.252 (n=1775)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3558 (IC base=+0.233)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.566` → IC=+0.277 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.566 (IC base=+0.233)

- **PATRÓN** `volumen_pendiente_norm` > `0.3534` → IC=+0.275 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3534 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` < `1.7377` → IC=+0.234 (n=745)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7377 (IC base=+0.233)

- **PATRÓN** `volumen_spike_ratio` > `2.1509` → IC=+0.236 (n=1128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1509 (IC base=+0.233)

- **PATRÓN** `libro_liquidez` > `2060.075` → IC=+0.247 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2060.075 (IC base=+0.233)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.227 (n=1112)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 17.0 (IC base=+0.233)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.172 (n=1985)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0075 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.4065` → IC=+0.166 (n=1983)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.4065 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=1333)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 11.0 (IC base=+0.149)

- **PATRÓN** `ibs_20min` > `0.3116` → IC=+0.211 (n=1983)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3116 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.1409` → IC=+0.197 (n=1228)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1409 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.863` → IC=+0.202 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.863 (IC base=+0.149)

- **PATRÓN** `volumen_regimen` < `1.0327` → IC=+0.155 (n=1745)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_regimen` < 1.0327 (IC base=+0.149)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.178 (n=817)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` < `1.5364` → IC=+0.153 (n=856)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 1.5364 (IC base=+0.149)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.162 (n=648)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `4763.2061` → IC=+0.190 (n=1322)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 4763.2061 (IC base=+0.149)

- **PATRÓN** `ballena_activa_n` < `142.0` → IC=+0.158 (n=1920)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 142.0 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.153 (n=2086)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3957` → IC=+0.144 (n=2086)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3957 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6837` → IC=+0.185 (n=2086)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.6837 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1546` → IC=+0.153 (n=2073)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1546 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.639` → IC=+0.158 (n=515)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 9.639 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8571` → IC=+0.158 (n=1391)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_regimen` < 0.8571 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.203 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.8013` → IC=+0.132 (n=1300)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 1.8013 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4171` → IC=+0.128 (n=1950)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 1.4171 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7821.8386` → IC=+0.189 (n=946)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 7821.8386 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.135 (n=1267)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 92.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.173 (n=1015)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.0103 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4413` → IC=+0.129 (n=1965)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.4413 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` > `0.4878` → IC=+0.215 (n=2232)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4878 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.1959` → IC=+0.190 (n=1316)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.1959 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.679` → IC=+0.272 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.679 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `1.182` → IC=+0.142 (n=2233)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.182 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` < `0.1609` → IC=+0.135 (n=2265)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` < 0.1609 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `1.4359` → IC=+0.146 (n=722)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4359 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `2839.7087` → IC=+0.211 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2839.7087 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.159 (n=699)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 20.0 (IC base=+0.128)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.136 (n=2287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0108 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1079` → IC=+0.171 (n=763)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.85€ cuando `drift_60min` |x|≤ 0.1079 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=2314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.217 (n=2293)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2002` → IC=+0.146 (n=2142)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.2002 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.445` → IC=+0.124 (n=461)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 7.445 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.51` → IC=+0.126 (n=2017)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 2.51 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `1.174` → IC=+0.128 (n=2287)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 1.174 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.149 (n=303)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` > `2.4249` → IC=+0.138 (n=708)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4249 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2685.1916` → IC=+0.190 (n=1037)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2685.1916 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `50.0` → IC=+0.125 (n=2098)

  - _Acción_: Kelly boost +0.62€ cuando `ballena_activa_n` < 50.0 (IC base=+0.118)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.245 (n=1841)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.1748` → IC=+0.235 (n=908)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1748 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.222 (n=2138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1397)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `0.6583` → IC=+0.256 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6583 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` > `0.1892` → IC=+0.226 (n=1355)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1892 (IC base=+0.220)

- **PATRÓN** `dist_vwap_pct` < `0.488` → IC=+0.221 (n=1831)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.488 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.252 (n=936)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` < `1.179` → IC=+0.223 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.179 (IC base=+0.220)

- **PATRÓN** `volumen_regimen` > `0.6199` → IC=+0.227 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6199 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2306` → IC=+0.262 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2306 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` < `2.4575` → IC=+0.225 (n=2006)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4575 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `1.7999` → IC=+0.229 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7999 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2642.1228` → IC=+0.230 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2642.1228 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.236 (n=930)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0124 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.235 (n=962)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.226)

- **PATRÓN** `drift_60min` |x|≤ `0.0897` → IC=+0.260 (n=705)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0897 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` < `0.4252` → IC=+0.254 (n=2114)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4252 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.2956` → IC=+0.234 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2956 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.33` → IC=+0.249 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.33 (IC base=+0.226)

- **PATRÓN** `volumen_regimen` > `0.6411` → IC=+0.234 (n=2114)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6411 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` > `0.2772` → IC=+0.282 (n=287)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2772 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `1.4361` → IC=+0.229 (n=1962)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4361 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `2392.7369` → IC=+0.229 (n=1889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2392.7369 (IC base=+0.226)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.207 (n=1376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.188 (n=1041)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0088 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1297` → IC=+0.201 (n=1370)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1297 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.213 (n=1535)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` > `0.7296` → IC=+0.231 (n=2075)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7296 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.7906` → IC=+0.203 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7906 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.675` → IC=+0.208 (n=1349)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.675 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `0.8638` → IC=+0.200 (n=1860)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8638 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` > `0.6971` → IC=+0.182 (n=2492)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` > 0.6971 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.1` → IC=+0.192 (n=1126)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.1 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` < `1.4332` → IC=+0.196 (n=1009)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4332 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.1972` → IC=+0.183 (n=1372)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` > 2.1972 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=3522)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `2731.7891` → IC=+0.185 (n=2780)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 2731.7891 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.192 (n=2894)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 150.0 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.134 (n=1107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0037 (IC base=+0.091)

- **PATRÓN** `ibs_20min` < `0.3774` → IC=+0.162 (n=2209)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.3774 (IC base=+0.091)

- **PATRÓN** `ballena_activa_n` < `28.0` → IC=+0.125 (n=1405)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 28.0 (IC base=+0.091)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.212 (n=387)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.3272` → IC=+0.193 (n=875)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.3272 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.199 (n=789)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.171)

- **PATRÓN** `ibs_20min` > `0.9273` → IC=+0.228 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9273 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.3049` → IC=+0.196 (n=274)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.3049 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.092` → IC=+0.191 (n=373)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 3.092 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.822` → IC=+0.172 (n=929)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 6.822 (IC base=+0.171)

- **PATRÓN** `volumen_regimen` < `0.8753` → IC=+0.200 (n=584)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8753 (IC base=+0.171)

- **PATRÓN** `volumen_pendiente_norm` > `0.0705` → IC=+0.178 (n=343)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_pendiente_norm` > 0.0705 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` < `2.2078` → IC=+0.182 (n=754)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 2.2078 (IC base=+0.171)

- **PATRÓN** `volumen_spike_ratio` > `1.4133` → IC=+0.173 (n=857)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` > 1.4133 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `14845.767` → IC=+0.185 (n=583)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 14845.767 (IC base=+0.171)

- **PATRÓN** `ballena_activa_n` < `157.0` → IC=+0.202 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 157.0 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.140 (n=1037)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0056 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.3449` → IC=+0.137 (n=1037)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.3449 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=926)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6416` → IC=+0.167 (n=913)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.6416 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.1865` → IC=+0.141 (n=1050)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1865 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` > `1.0596` → IC=+0.146 (n=470)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0596 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.1595` → IC=+0.164 (n=275)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_pendiente_norm` > 0.1595 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `2.1137` → IC=+0.131 (n=901)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.1137 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `308.0` → IC=+0.146 (n=886)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 308.0 (IC base=+0.118)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.250 (n=638)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.2048` → IC=+0.232 (n=636)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2048 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.230 (n=1003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.6852` → IC=+0.274 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6852 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.3578` → IC=+0.226 (n=294)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3578 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2068` → IC=+0.219 (n=855)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2068 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.93` → IC=+0.239 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.93 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8389` → IC=+0.221 (n=636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8389 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.1774` → IC=+0.231 (n=318)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1774 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.1565` → IC=+0.244 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1565 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4137` → IC=+0.253 (n=314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4137 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.7708` → IC=+0.225 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7708 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=1064)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.1034` → IC=+0.169 (n=321)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.1034 (IC base=+0.066)

- **PATRÓN** `libro_liquidez` > `6929.9156` → IC=+0.132 (n=642)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 6929.9156 (IC base=+0.066)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.177 (n=255)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0108 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.5317` → IC=+0.164 (n=766)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.5317 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.214 (n=369)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=357)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `1.0116` → IC=+0.236 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0116 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.222` → IC=+0.232 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.222 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` < `1.0551` → IC=+0.182 (n=674)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.0551 (IC base=+0.161)

- **PATRÓN** `volumen_regimen` > `0.7177` → IC=+0.168 (n=684)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` > 0.7177 (IC base=+0.161)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.190 (n=217)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` < `1.4543` → IC=+0.165 (n=246)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.4543 (IC base=+0.161)

- **PATRÓN** `volumen_spike_ratio` > `2.1799` → IC=+0.174 (n=335)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_spike_ratio` > 2.1799 (IC base=+0.161)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.168 (n=789)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.02 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `3060.3888` → IC=+0.193 (n=255)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3060.3888 (IC base=+0.161)

- **PATRÓN** `ibs_20min` < `0.52` → IC=+0.143 (n=696)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.52 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `2760.3927` → IC=+0.157 (n=359)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2760.3927 (IC base=+0.060)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.127 (n=510)

  - _Acción_: Kelly boost +0.63€ cuando `ballena_activa_n` < 21.0 (IC base=+0.060)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0234` → IC=+0.155 (n=198)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0234 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.180 (n=198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.007 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.254` → IC=+0.164 (n=132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.254 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.181 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 16.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.192 (n=89)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 7.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.5556` → IC=+0.178 (n=178)

  - _Acción_: Kelly boost +0.89€ cuando `ibs_20min` > 0.5556 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.2304` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.2304 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `1.103` → IC=+0.153 (n=220)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 1.103 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.301` → IC=+0.175 (n=167)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` < 3.301 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` > `0.6289` → IC=+0.165 (n=198)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6289 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` < `0.2526` → IC=+0.168 (n=194)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_pendiente_norm` < 0.2526 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.1897` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1897 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.4483` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4483 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.6057` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.6057 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.182 (n=199)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `2499.3184` → IC=+0.172 (n=132)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 2499.3184 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.154 (n=203)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.012 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.115)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.133 (n=227)

  - _Acción_: Kelly boost +0.67€ cuando `ibs_20min` < 0.61 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `1.1297` → IC=+0.269 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1297 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.115)

- **PATRÓN** `volumen_regimen` < `0.8919` → IC=+0.130 (n=152)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 0.8919 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` < `0.1158` → IC=+0.125 (n=206)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1158 (IC base=+0.115)

- **PATRÓN** `volumen_pendiente_norm` > `0.2293` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` > 0.2293 (IC base=+0.115)

- **PATRÓN** `ballena_activa_n` < `17.0` → IC=+0.136 (n=185)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 17.0 (IC base=+0.115)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.181 (n=5319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0047 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.224 (n=5318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=16607)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.229 (n=15945)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4483 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.9104` → IC=+0.212 (n=1995)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9104 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.322` → IC=+0.254 (n=3902)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.322 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.2227` → IC=+0.169 (n=10687)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2227 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.206 (n=2121)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.607` → IC=+0.195 (n=5163)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.607 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1824.0348` → IC=+0.185 (n=15941)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1824.0348 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `115.0` → IC=+0.202 (n=14577)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 115.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.194 (n=6397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0055 (IC base=+0.186)

- **PATRÓN** `drift_60min` |x|≤ `0.4959` → IC=+0.189 (n=14505)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.4959 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=5426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `ibs_20min` < `0.58` → IC=+0.241 (n=14507)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.58 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` < `0.1766` → IC=+0.170 (n=8788)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1766 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.88` → IC=+0.205 (n=2009)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.88 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.628` → IC=+0.189 (n=14010)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 3.628 (IC base=+0.186)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.161 (n=4313)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 0.7049 (IC base=+0.186)

- **PATRÓN** `volumen_pendiente_norm` > `0.2895` → IC=+0.250 (n=1949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2895 (IC base=+0.186)

- **PATRÓN** `volumen_spike_ratio` > `2.2544` → IC=+0.197 (n=6206)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` > 2.2544 (IC base=+0.186)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.214 (n=9039)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.186)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.239 (n=869)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.220)

- **PATRÓN** `drift_60min` |x|≤ `0.3486` → IC=+0.223 (n=2606)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3486 (IC base=+0.220)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=1259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.224 (n=1758)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.220)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.326 (n=1012)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.220)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.612` → IC=+0.351 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.612 (IC base=+0.220)

- **PATRÓN** `volumen_pendiente_norm` > `0.2793` → IC=+0.283 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2793 (IC base=+0.220)

- **PATRÓN** `volumen_spike_ratio` > `2.2767` → IC=+0.234 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2767 (IC base=+0.220)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.237 (n=2745)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `2088.76` → IC=+0.234 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2088.76 (IC base=+0.220)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.239 (n=1018)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.263 (n=2224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.1214` → IC=+0.278 (n=979)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1214 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.277 (n=817)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.5048` → IC=+0.287 (n=2225)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5048 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.365` → IC=+0.262 (n=692)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.365 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` < `0.0949` → IC=+0.260 (n=1984)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0949 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.278 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.5569` → IC=+0.258 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5569 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` > `2.6384` → IC=+0.271 (n=701)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6384 (IC base=+0.259)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.261 (n=2483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `1567.2992` → IC=+0.268 (n=2223)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1567.2992 (IC base=+0.259)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.261 (n=957)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.259)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.201 (n=862)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1769` → IC=+0.160 (n=1720)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.80€ cuando `drift_60min` |x|≤ 0.1769 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2691)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `ibs_20min` > `0.3774` → IC=+0.226 (n=2304)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3774 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.126` → IC=+0.196 (n=1364)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.126 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.602` → IC=+0.165 (n=425)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.602 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.194` → IC=+0.155 (n=2246)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.194 (IC base=+0.150)

- **PATRÓN** `volumen_regimen` < `0.6288` → IC=+0.176 (n=861)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6288 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` < `0.0718` → IC=+0.154 (n=2304)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0718 (IC base=+0.150)

- **PATRÓN** `volumen_pendiente_norm` > `0.2719` → IC=+0.179 (n=369)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.2719 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` < `2.1761` → IC=+0.161 (n=2216)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1761 (IC base=+0.150)

- **PATRÓN** `volumen_spike_ratio` > `1.5299` → IC=+0.154 (n=2250)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5299 (IC base=+0.150)

- **PATRÓN** `ballena_activa_n` < `267.0` → IC=+0.183 (n=1088)

  - _Acción_: Kelly boost +0.91€ cuando `ballena_activa_n` < 267.0 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=2170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2605` → IC=+0.163 (n=1910)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2605 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.7006` → IC=+0.198 (n=2170)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7006 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.135` → IC=+0.165 (n=2024)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.135 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.205` → IC=+0.156 (n=361)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.205 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.454` → IC=+0.144 (n=2189)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.454 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1817` → IC=+0.153 (n=2171)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1817 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2172` → IC=+0.195 (n=405)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2172 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.4315` → IC=+0.149 (n=2066)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4315 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7707` → IC=+0.155 (n=1377)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7707 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `276.0` → IC=+0.154 (n=871)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 276.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.258 (n=885)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2768)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=2377)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.304 (n=987)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.349` → IC=+0.319 (n=560)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.349 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` < `0.2097` → IC=+0.226 (n=2700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2097 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `3.1929` → IC=+0.240 (n=857)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1929 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.233 (n=3143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `1852.8886` → IC=+0.238 (n=1767)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1852.8886 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.243 (n=2186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.1813` → IC=+0.253 (n=1093)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1813 (IC base=+0.239)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.265 (n=938)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.239)

- **PATRÓN** `ibs_20min` < `0.0263` → IC=+0.302 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0263 (IC base=+0.239)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.047` → IC=+0.292 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.047 (IC base=+0.239)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.296 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.239)

- **PATRÓN** `volumen_spike_ratio` > `2.1351` → IC=+0.249 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1351 (IC base=+0.239)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.240 (n=1317)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.239)

- **PATRÓN** `libro_liquidez` > `2060.32` → IC=+0.260 (n=828)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2060.32 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.247 (n=1037)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.239)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.199 (n=1210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0039 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.4206` → IC=+0.158 (n=2743)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4206 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=2850)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.145)

- **PATRÓN** `ibs_20min` > `0.2515` → IC=+0.193 (n=2743)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2515 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1408` → IC=+0.171 (n=1476)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1408 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.165` → IC=+0.162 (n=1118)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 4.165 (IC base=+0.145)

- **PATRÓN** `volumen_regimen` < `0.869` → IC=+0.164 (n=1830)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.869 (IC base=+0.145)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.188 (n=357)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` < `1.5216` → IC=+0.164 (n=1178)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5216 (IC base=+0.145)

- **PATRÓN** `volumen_spike_ratio` > `2.1677` → IC=+0.156 (n=1213)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1677 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `6697.2205` → IC=+0.240 (n=1244)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6697.2205 (IC base=+0.145)

- **PATRÓN** `ballena_activa_n` < `75.0` → IC=+0.172 (n=1161)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 75.0 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0033` → IC=+0.190 (n=758)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0033 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4436` → IC=+0.140 (n=2271)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.4436 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.156 (n=833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` < `0.7385` → IC=+0.184 (n=2271)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7385 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` < `0.1494` → IC=+0.144 (n=2047)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1494 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.138` → IC=+0.171 (n=344)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 11.138 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `0.8727` → IC=+0.140 (n=1514)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.8727 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` > `0.2956` → IC=+0.231 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2956 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` > `1.4282` → IC=+0.138 (n=2182)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 1.4282 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `7431.4548` → IC=+0.211 (n=757)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7431.4548 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `133.0` → IC=+0.129 (n=1945)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 133.0 (IC base=+0.129)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.148 (n=1838)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0084 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=1010)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.200 (n=2760)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4444 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0689` → IC=+0.207 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0689 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.822` → IC=+0.269 (n=699)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.822 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2242` → IC=+0.136 (n=2754)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2242 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.0984` → IC=+0.125 (n=2598)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.0984 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2794` → IC=+0.140 (n=356)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` > 0.2794 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8314` → IC=+0.128 (n=1794)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8314 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4631` → IC=+0.126 (n=2688)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4631 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2836)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2516.937` → IC=+0.236 (n=1249)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2516.937 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `25.0` → IC=+0.136 (n=882)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 25.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.141 (n=2629)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0111 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1334` → IC=+0.158 (n=877)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.1334 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=2708)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6444` → IC=+0.213 (n=2629)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6444 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2159` → IC=+0.138 (n=2241)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2159 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.3` → IC=+0.133 (n=2536)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` < 3.3 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.6414` → IC=+0.137 (n=877)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.6414 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2238` → IC=+0.167 (n=445)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.2238 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4348` → IC=+0.147 (n=819)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` < 1.4348 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2697.8048` → IC=+0.210 (n=877)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2697.8048 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `48.0` → IC=+0.135 (n=2186)

  - _Acción_: Kelly boost +0.68€ cuando `ballena_activa_n` < 48.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.245 (n=2335)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=2725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.234 (n=1745)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.607` → IC=+0.270 (n=2333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.607 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1948` → IC=+0.244 (n=1441)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1948 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.744` → IC=+0.271 (n=874)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.744 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2284` → IC=+0.234 (n=2612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2284 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6419` → IC=+0.229 (n=2612)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6419 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2358` → IC=+0.248 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2358 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.5487` → IC=+0.234 (n=2269)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5487 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.228 (n=3389)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2646.5003` → IC=+0.239 (n=1741)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2646.5003 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.0229` → IC=+0.248 (n=1238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0229 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.235 (n=2562)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` < `0.51` → IC=+0.263 (n=2731)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.51 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` < `0.2927` → IC=+0.231 (n=2614)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2927 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.944` → IC=+0.262 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.944 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `1.2268` → IC=+0.257 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2268 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2796` → IC=+0.297 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2796 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `1.4285` → IC=+0.230 (n=2530)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4285 (IC base=+0.227)

- **PATRÓN** `libro_liquidez` > `2407.4896` → IC=+0.229 (n=2439)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2407.4896 (IC base=+0.227)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=4783)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.240 (n=1617)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.5084` → IC=+0.211 (n=4838)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5084 (IC base=+0.203)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.218 (n=1740)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `ibs_20min` > `0.9404` → IC=+0.244 (n=1613)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9404 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.1725` → IC=+0.210 (n=1847)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1725 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` < `0.4364` → IC=+0.210 (n=3503)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4364 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.76` → IC=+0.212 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.76 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.634` → IC=+0.203 (n=4312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.634 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.217 (n=1568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.203)

- **PATRÓN** `volumen_regimen` > `0.8832` → IC=+0.209 (n=2376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8832 (IC base=+0.203)

- **PATRÓN** `volumen_pendiente_norm` > `0.166` → IC=+0.218 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.166 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` < `1.4537` → IC=+0.208 (n=1588)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4537 (IC base=+0.203)

- **PATRÓN** `volumen_spike_ratio` > `1.8412` → IC=+0.204 (n=3176)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8412 (IC base=+0.203)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.211 (n=3769)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2974.0304` → IC=+0.214 (n=4322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2974.0304 (IC base=+0.203)

- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.235 (n=1200)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4933` → IC=+0.204 (n=3600)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4933 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=1206)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.205 (n=1620)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.7335` → IC=+0.195 (n=3599)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.7335 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6749` → IC=+0.199 (n=622)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6749 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.4194` → IC=+0.185 (n=3603)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.4194 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.15` → IC=+0.196 (n=3614)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 6.15 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `1.0986` → IC=+0.198 (n=2997)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_regimen` < 1.0986 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.192 (n=3298)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2222` → IC=+0.189 (n=732)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.2222 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.193 (n=1563)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.1885` → IC=+0.198 (n=1611)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.1885 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.190 (n=4783)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `165.0` → IC=+0.199 (n=3105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 165.0 (IC base=+0.188)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.256 (n=616)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.0869` → IC=+0.281 (n=235)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0869 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.249 (n=738)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.250 (n=322)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` < `0.4908` → IC=+0.268 (n=467)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4908 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` < `0.5497` → IC=+0.253 (n=762)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5497 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.054` → IC=+0.260 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.054 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `1.2117` → IC=+0.251 (n=700)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2117 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` > `0.8668` → IC=+0.259 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.8668 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.337 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.8179` → IC=+0.252 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8179 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` > `1.4288` → IC=+0.244 (n=698)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4288 (IC base=+0.244)

- **PATRÓN** `libro_liquidez` > `12227.9612` → IC=+0.258 (n=625)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12227.9612 (IC base=+0.244)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.223 (n=829)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0044 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.374` → IC=+0.182 (n=1243)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.91€ cuando `drift_60min` |x|≤ 0.374 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=442)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.196 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 5.0 (IC base=+0.169)

- **PATRÓN** `ibs_20min` < `0.1386` → IC=+0.201 (n=547)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1386 (IC base=+0.169)

- **PATRÓN** `ibs_20min` > `0.6084` → IC=+0.170 (n=564)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` > 0.6084 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.6926` → IC=+0.194 (n=119)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6926 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.186 (n=1226)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.169)

- **PATRÓN** `volumen_regimen` < `0.8855` → IC=+0.202 (n=829)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8855 (IC base=+0.169)

- **PATRÓN** `volumen_pendiente_norm` > `0.1523` → IC=+0.191 (n=386)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.1523 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` < `1.4032` → IC=+0.182 (n=413)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_spike_ratio` < 1.4032 (IC base=+0.169)

- **PATRÓN** `volumen_spike_ratio` > `2.1644` → IC=+0.180 (n=561)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` > 2.1644 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `13519.2976` → IC=+0.180 (n=829)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 13519.2976 (IC base=+0.169)

- **PATRÓN** `ballena_activa_n` < `701.0` → IC=+0.180 (n=1200)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 701.0 (IC base=+0.169)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.192 (n=319)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0067 (IC base=+0.173)

- **PATRÓN** `drift_60min` |x|≤ `0.5907` → IC=+0.183 (n=724)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.5907 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=258)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.173)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.231 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.173)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.556` → IC=+0.218 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.556 (IC base=+0.173)

- **PATRÓN** `volumen_pendiente_norm` > `0.2088` → IC=+0.221 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2088 (IC base=+0.173)

- **PATRÓN** `volumen_spike_ratio` > `2.2523` → IC=+0.183 (n=481)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_spike_ratio` > 2.2523 (IC base=+0.173)

- **PATRÓN** `libro_liquidez` > `2523.314` → IC=+0.224 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2523.314 (IC base=+0.173)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.216 (n=1364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.200)

- **PATRÓN** `drift_60min` |x|≤ `0.4614` → IC=+0.208 (n=1364)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4614 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=497)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.200)

- **PATRÓN** `ibs_20min` < `0.519` → IC=+0.212 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.519 (IC base=+0.200)

- **PATRÓN** `ibs_20min` > `0.7601` → IC=+0.201 (n=619)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7601 (IC base=+0.200)

- **PATRÓN** `dist_vwap_pct` < `0.2178` → IC=+0.212 (n=1207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2178 (IC base=+0.200)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.114` → IC=+0.207 (n=1228)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.114 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` < `0.8778` → IC=+0.202 (n=910)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8778 (IC base=+0.200)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.210 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` < `0.1054` → IC=+0.203 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1054 (IC base=+0.200)

- **PATRÓN** `volumen_pendiente_norm` > `0.164` → IC=+0.203 (n=405)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.164 (IC base=+0.200)

- **PATRÓN** `volumen_spike_ratio` < `2.4495` → IC=+0.206 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4495 (IC base=+0.200)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=1397)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.200)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.205 (n=1115)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.212 (n=1115)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.203 (n=436)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.199 (n=746)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.3984` → IC=+0.196 (n=744)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.3984 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.0863` → IC=+0.189 (n=1116)

  - _Acción_: Kelly boost +0.94€ cuando `ibs_20min` > 0.0863 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6705` → IC=+0.199 (n=197)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6705 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.2251` → IC=+0.189 (n=1076)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.2251 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.747` → IC=+0.193 (n=1141)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 6.747 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `1.2449` → IC=+0.200 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2449 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.207 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.1949` → IC=+0.199 (n=961)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1949 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.5301` → IC=+0.191 (n=364)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5301 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `6896.289` → IC=+0.194 (n=1115)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 6896.289 (IC base=+0.188)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.203 (n=638)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.203 (n=746)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.251 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.7569` → IC=+0.235 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7569 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.236` → IC=+0.202 (n=391)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.236 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.6955` → IC=+0.229 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6955 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` < `0.1066` → IC=+0.194 (n=652)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` < 0.1066 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0799` → IC=+0.191 (n=322)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0799 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.5676` → IC=+0.199 (n=310)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.5676 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.4815` → IC=+0.209 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4815 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.187 (n=844)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `3097.623` → IC=+0.201 (n=647)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3097.623 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.200 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.182)

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
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.161 (n=700)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0039 (IC base=+0.069)

- **PATRÓN** `ibs_20min` > `0.5517` → IC=+0.163 (n=1332)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` > 0.5517 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.3615` → IC=+0.153 (n=531)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.3615 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.207` → IC=+0.169 (n=330)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 11.207 (IC base=+0.069)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.249 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` < `0.1007` → IC=+0.139 (n=765)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1007 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.433` → IC=+0.185 (n=125)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 10.433 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.148` → IC=+0.194 (n=214)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.148 (IC base=+0.071)

- **PATRÓN** `volumen_spike_ratio` < `1.4839` → IC=+0.130 (n=317)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 1.4839 (IC base=+0.071)

### GBM_LATE_60M#BTC#60min
- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.131 (n=532)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0057 (IC base=+0.085)

- **PATRÓN** `ibs_20min` > `0.5149` → IC=+0.184 (n=448)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.5149 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.152 (n=254)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.085)

- **PATRÓN** `ibs_20min` < `0.2807` → IC=+0.234 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2807 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.216` → IC=+0.131 (n=391)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.216 (IC base=+0.086)

- **PATRÓN** `volumen_regimen` < `0.825` → IC=+0.124 (n=235)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.825 (IC base=+0.086)

- **PATRÓN** `volumen_pendiente_norm` > `0.0709` → IC=+0.167 (n=145)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.0709 (IC base=+0.086)

- **PATRÓN** `volumen_spike_ratio` < `2.17` → IC=+0.123 (n=290)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_spike_ratio` < 2.17 (IC base=+0.086)

### GBM_LATE_60M#ETH#60min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.149 (n=348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0047 (IC base=+0.092)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.122 (n=487)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 7.0 (IC base=+0.092)

- **PATRÓN** `ibs_20min` > `0.6407` → IC=+0.205 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6407 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.1258` → IC=+0.197 (n=255)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.1258 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.269` → IC=+0.252 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.269 (IC base=+0.092)

- **PATRÓN** `volumen_regimen` < `0.8145` → IC=+0.124 (n=325)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_regimen` < 0.8145 (IC base=+0.092)

- **PATRÓN** `volumen_pendiente_norm` > `0.2835` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.2835 (IC base=+0.092)

- **PATRÓN** `libro_liquidez` > `1667.8655` → IC=+0.142 (n=219)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 1667.8655 (IC base=+0.092)

- **PATRÓN** `ibs_20min` < `0.106` → IC=+0.291 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.106 (IC base=+0.036)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.991` → IC=+0.256 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.991 (IC base=+0.036)

- **PATRÓN** `volumen_pendiente_norm` > `0.1379` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1379 (IC base=+0.036)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `ibs_20min` > `0.15` → IC=-0.230 (n=61)

  - _Acción_: SKIP cuando `ibs_20min` > 0.15
  - _Potencial_: sin este filtro IC_bueno=+0.251 (n=187)

- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.162 (n=341)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` > 0.75 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.7402` → IC=+0.131 (n=128)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.7402 (IC base=+0.029)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.817` → IC=+0.148 (n=143)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` > 7.817 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.2369` → IC=+0.146 (n=97)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2369 (IC base=+0.029)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.167 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0103 (IC base=+0.084)

- **PATRÓN** `ibs_20min` < `0.15` → IC=+0.251 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.15 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` < `0.6636` → IC=+0.156 (n=216)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.6636 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.803` → IC=+0.295 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.803 (IC base=+0.084)

- **PATRÓN** `volumen_regimen` > `1.0818` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0818 (IC base=+0.084)

- **PATRÓN** `volumen_pendiente_norm` > `0.1517` → IC=+0.272 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1517 (IC base=+0.084)

- **PATRÓN** `volumen_spike_ratio` > `2.4899` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4899 (IC base=+0.084)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.175 (n=158)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.06 (IC base=+0.084)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.333 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=234)

- **FILTRO** `dist_vwap_pct` > `0.2344` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2344
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=281)

- **FILTRO** `volumen_spike_ratio` > `2.5112` → IC=-0.218 (n=76)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.5112
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=148)

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.341 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.258 (n=184)

- **FILTRO** `dist_vwap_pct` > `0.4388` → IC=-0.409 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4388
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=225)

- **FILTRO** `sigma_ewma_delta_pct` > `10.676` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.676
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=221)

- **FILTRO** `volumen_pendiente_norm` > `0.0538` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0538
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=134)

- **FILTRO** `libro_liquidez` < `1289.4538` → IC=-0.309 (n=61)

  - _Acción_: SKIP cuando `libro_liquidez` < 1289.4538
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=184)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.173 (n=50)

- **FILTRO** `volumen_regimen` < `1.2175` → IC=-0.280 (n=48)

  - _Acción_: SKIP cuando `volumen_regimen` < 1.2175
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=48)

- **FILTRO** `dist_vwap_pct` < `0.0874` → IC=-0.287 (n=73)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0874
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=34)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=81)

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
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=71)

- **FILTRO** `dist_vwap_pct` > `0.1206` → IC=-0.328 (n=27)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1206
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=66)

- **FILTRO** `libro_liquidez` < `1483.7101` → IC=-0.292 (n=46)

  - _Acción_: SKIP cuando `libro_liquidez` < 1483.7101
  - _Potencial_: sin este filtro IC_bueno=-0.255 (n=47)

- **PATRÓN** `ibs_20min` > `0.9464` → IC=+0.167 (n=34)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.9464 (IC base=-0.173)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_h` < `0.0063` → IC=-0.329 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0063
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=70)

- **FILTRO** `drift_60min` |x|> `0.2367` → IC=-0.389 (n=25)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2367
  - _Potencial_: sin este filtro IC_bueno=-0.171 (n=77)

- **FILTRO** `dist_vwap_pct` > `0.0933` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.0933
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=84)

- **FILTRO** `dist_vwap_pct` < `0.219` → IC=-0.346 (n=24)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.219
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=21)

- **FILTRO** `volumen_regimen` < `0.9792` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.9792
  - _Potencial_: sin este filtro IC_bueno=-0.180 (n=23)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1653` → IC=-0.125 (n=270)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1653
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=526)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.179 (n=166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0069 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.104)

- **PATRÓN** `ibs_20min` > `0.6842` → IC=+0.139 (n=497)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 0.6842 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.7249` → IC=+0.202 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7249 (IC base=+0.104)

- **PATRÓN** `volumen_regimen` < `0.6301` → IC=+0.155 (n=166)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.6301 (IC base=+0.104)

- **PATRÓN** `volumen_pendiente_norm` < `0.2806` → IC=+0.130 (n=460)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_pendiente_norm` < 0.2806 (IC base=+0.104)

- **PATRÓN** `volumen_spike_ratio` < `2.5028` → IC=+0.130 (n=395)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.5028 (IC base=+0.104)

- **PATRÓN** `ibs_20min` < `0.1653` → IC=+0.161 (n=526)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1653 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.159` → IC=+0.186 (n=138)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 11.159 (IC base=+0.064)

- **PATRÓN** `volumen_pendiente_norm` > `0.2251` → IC=+0.123 (n=120)

  - _Acción_: Kelly boost +0.61€ cuando `volumen_pendiente_norm` > 0.2251 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `3253.1348` → IC=+0.142 (n=398)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3253.1348 (IC base=+0.064)

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
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.128 (n=162)

- **FILTRO** `ibs_20min` > `0.1906` → IC=-0.134 (n=99)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1906
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=193)

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

- **PATRÓN** `ibs_20min` < `0.1906` → IC=+0.120 (n=193)

  - _Acción_: Kelly boost +0.60€ cuando `ibs_20min` < 0.1906 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.059` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.059 (IC base=+0.034)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.034)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4194` → IC=-0.265 (n=32)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4194
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=100)

- **FILTRO** `dist_vwap_pct` > `0.1687` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1687
  - _Potencial_: sin este filtro IC_bueno=-0.046 (n=95)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.281 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.244)

- **PATRÓN** `ibs_20min` > `0.6667` → IC=+0.257 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6667 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6475` → IC=+0.384 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6475 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.401` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.401 (IC base=+0.244)

- **PATRÓN** `volumen_regimen` < `0.5837` → IC=+0.310 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5837 (IC base=+0.244)

- **PATRÓN** `volumen_pendiente_norm` > `0.0887` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0887 (IC base=+0.244)

- **PATRÓN** `volumen_spike_ratio` < `1.4958` → IC=+0.385 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4958 (IC base=+0.244)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.245 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.445` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.445 (IC base=-0.082)

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
- **PATRÓN** `libro_liquidez` > `2857.3954` → IC=+0.134 (n=550)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2857.3954 (IC base=+0.100)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2857.3954` → IC=+0.134 (n=550)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2857.3954 (IC base=+0.100)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=184)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=261)

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
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=3403)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.127 (n=234)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.495 (IC base=+0.025)

### LIQUIDACIONES_5M#ETH#5min
- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1248)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=1202)

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
  - _Potencial_: sin este filtro IC_bueno=+0.030 (n=409)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=390)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.020)

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
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=769)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=769)

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
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=212)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=236)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=254)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.133 (n=58)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=+0.061 (n=212)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=248)

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
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=248)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=176)

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
  - _Potencial_: sin este filtro IC_bueno=+0.053 (n=45)

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

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` < 0.46 (IC base=+0.009)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.186 (n=49)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=222)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **PATRÓN** `py_entrada` < `0.5` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.5 (IC base=+0.048)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.128 (n=310)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=110)

- **FILTRO** `restante_min` < `10.42` → IC=-0.136 (n=138)

  - _Acción_: SKIP cuando `restante_min` < 10.42
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=282)

- **FILTRO** `lag_apertura_s` > `255.13` → IC=-0.139 (n=142)

  - _Acción_: SKIP cuando `lag_apertura_s` > 255.13
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=278)

- **FILTRO** `profundidad_ratio` < `40.5` → IC=-0.173 (n=105)

  - _Acción_: SKIP cuando `profundidad_ratio` < 40.5
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=315)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.229 (n=68)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=306)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `profundidad_ratio` < `21.2` → IC=-0.144 (n=130)

  - _Acción_: SKIP cuando `profundidad_ratio` < 21.2
  - _Potencial_: sin este filtro IC_bueno=+0.054 (n=265)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.175 (n=75)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=324)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.131 (n=261)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=281)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.164 (n=5633)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=17613)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.170 (n=5978)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=+0.044 (n=17971)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.193 (n=1033)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=3170)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.168 (n=989)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3302)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.140 (n=1110)

  - _Acción_: Kelly boost +0.70€ cuando `ibs_20min` > 1.0 (IC base=+0.037)

- **PATRÓN** `libro_liquidez` > `1422.418` → IC=+0.134 (n=2102)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 1422.418 (IC base=+0.037)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.128 (n=2002)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.014)

- **PATRÓN** `libro_liquidez` > `1539.8007` → IC=+0.150 (n=1459)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 1539.8007 (IC base=+0.014)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.156 (n=781)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2653)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.176 (n=835)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2575)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.171 (n=1034)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=3200)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.201 (n=1013)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=3354)

- **PATRÓN** `ibs_20min` > `0.9635` → IC=+0.130 (n=1440)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9635 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1842.8556` → IC=+0.125 (n=1440)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1842.8556 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.155 (n=1010)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=3203)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=2327)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=2730)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3470)

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
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=839)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `py_entrada` > `0.615` → IC=-0.216 (n=86)

  - _Acción_: SKIP cuando `py_entrada` > 0.615
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=343)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=874)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=16142)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=35734)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.284 (n=12627)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=39249)

- **FILTRO** `ibs_7min` < `0.2421` → IC=-0.229 (n=12968)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2421
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=38908)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.152 (n=17491)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=34385)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.238 (n=15973)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=49620)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.180 (n=16240)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=49353)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2597)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6394)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=4457)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=4534)

- **FILTRO** `ibs_7min` < `0.7111` → IC=-0.245 (n=2967)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7111
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6024)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.176 (n=1986)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7005)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.269 (n=2810)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8570)

- **FILTRO** `ibs_7min` > `0.7722` → IC=-0.210 (n=2844)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7722
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=8536)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2020)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.055 (n=6772)

- **FILTRO** `ibs_7min` < `0.7289` → IC=-0.197 (n=2198)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7289
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6594)

- **FILTRO** `ballena_activa_n` > `153.0` → IC=-0.188 (n=2189)

  - _Acción_: SKIP cuando `ballena_activa_n` > 153.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6603)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.264 (n=2176)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=6744)

- **FILTRO** `ibs_7min` > `0.267` → IC=-0.195 (n=2229)

  - _Acción_: SKIP cuando `ibs_7min` > 0.267
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6691)

- **FILTRO** `ballena_activa_n` > `149.0` → IC=-0.182 (n=2225)

  - _Acción_: SKIP cuando `ballena_activa_n` > 149.0
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=6695)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.157 (n=2117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=6446)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=2085)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=6478)

- **FILTRO** `ibs_7min` < `0.7` → IC=-0.246 (n=2823)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=5740)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.193 (n=2090)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6473)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.251 (n=2789)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9316)

- **FILTRO** `ibs_7min` > `0.7338` → IC=-0.175 (n=3026)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7338
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=9079)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.123 (n=2781)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.090 (n=5689)

- **FILTRO** `py_entrada` < `0.34` → IC=-0.263 (n=1965)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6505)

- **FILTRO** `ibs_7min` < `0.732` → IC=-0.186 (n=2116)

  - _Acción_: SKIP cuando `ibs_7min` < 0.732
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6354)

- **FILTRO** `ballena_activa_n` > `28.0` → IC=-0.191 (n=2059)

  - _Acción_: SKIP cuando `ballena_activa_n` > 28.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6411)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.268 (n=1953)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=6831)

- **FILTRO** `ibs_7min` > `0.2751` → IC=-0.179 (n=2195)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2751
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=6589)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.175 (n=2195)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6589)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.282 (n=2020)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=6532)

- **FILTRO** `ibs_7min` < `0.2222` → IC=-0.232 (n=2127)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2222
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=6425)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.186 (n=2998)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=9543)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.281 (n=2118)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=6390)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.219 (n=2127)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6381)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.199 (n=1931)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.075 (n=6577)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.211 (n=2879)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=8984)

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
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=825)

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
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=628)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3982` → IC=+0.146 (n=1104)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.73€ cuando `delta_ratio` |x|> 0.3982 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.143 (n=513)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 14.0 (IC base=+0.131)

- **PATRÓN** `total_vol_5m` < `441.7389` → IC=+0.160 (n=369)

  - _Acción_: Kelly boost +0.80€ cuando `total_vol_5m` < 441.7389 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `3672.897` → IC=+0.142 (n=501)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 3672.897 (IC base=+0.131)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.149 (n=363)

  - _Acción_: Kelly boost +0.75€ cuando `ballena_activa_n` < 12.0 (IC base=+0.131)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4367` → IC=+0.163 (n=87)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4367 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.222 (n=124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `2587.5138` → IC=+0.219 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2587.5138 (IC base=+0.147)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3994` → IC=+0.136 (n=226)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio` |x|> 0.3994 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.142 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 3.0 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.131 (n=269)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.04 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2365.7446` → IC=+0.134 (n=151)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2365.7446 (IC base=+0.120)

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
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4332 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.185 (n=144)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 12.0 (IC base=+0.153)

- **PATRÓN** `total_vol_5m` < `5032.488` → IC=+0.192 (n=131)

  - _Acción_: Kelly boost +0.96€ cuando `total_vol_5m` < 5032.488 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `3079.8442` → IC=+0.160 (n=195)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3079.8442 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 27.0 (IC base=+0.153)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `delta_ratio` |x|> `0.401` → IC=+0.138 (n=183)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.401 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=124)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `3599.4239` → IC=+0.163 (n=93)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3599.4239 (IC base=+0.093)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `8.4547` → IC=-0.256 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 8.4547
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=130)

- **FILTRO** `sigma_h` > `0.005` → IC=-0.267 (n=311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=313)

- **FILTRO** `T_h` > `129.6211` → IC=-0.205 (n=154)

  - _Acción_: SKIP cuando `T_h` > 129.6211
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=470)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.185 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0034 (IC base=-0.078)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0054` → IC=-0.268 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0054
  - _Potencial_: sin este filtro IC_bueno=+0.191 (n=95)

- **FILTRO** `T_h` > `87.9981` → IC=-0.271 (n=46)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=142)

- **PATRÓN** `sigma_h` < `0.0054` → IC=+0.191 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0054 (IC base=-0.037)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `sigma_h` > `0.0055` → IC=-0.152 (n=44)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `pct_vs_K` |x|> `7.7861` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.7861
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=40)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `T_h` < `87.7913` → IC=-0.167 (n=52)

  - _Acción_: SKIP cuando `T_h` < 87.7913
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=54)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.224 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=-0.074)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.01` → IC=-0.217 (n=437)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=146)

- **FILTRO** `T_h` > `70.6078` → IC=-0.190 (n=437)

  - _Acción_: SKIP cuando `T_h` > 70.6078
  - _Potencial_: sin este filtro IC_bueno=-0.135 (n=146)

- **FILTRO** `pct_vs_K` |x|> `3.3681` → IC=-0.435 (n=121)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.3681
  - _Potencial_: sin este filtro IC_bueno=-0.178 (n=371)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `T_h` > `71.6618` → IC=-0.187 (n=129)

  - _Acción_: SKIP cuando `T_h` > 71.6618
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=64)

- **FILTRO** `pct_vs_K` |x|> `2.7876` → IC=-0.360 (n=48)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.7876
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=145)

- **FILTRO** `T_h` > `72.749` → IC=-0.284 (n=132)

  - _Acción_: SKIP cuando `T_h` > 72.749
  - _Potencial_: sin este filtro IC_bueno=-0.245 (n=45)

- **FILTRO** `pct_vs_K` |x|> `3.0008` → IC=-0.432 (n=42)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.0008
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=135)

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
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.309 (n=124)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=42)

- **FILTRO** `T_h` > `135.9836` → IC=-0.267 (n=41)

  - _Acción_: SKIP cuando `T_h` > 135.9836
  - _Potencial_: sin este filtro IC_bueno=-0.240 (n=125)

- **FILTRO** `pct_vs_K` |x|> `3.1362` → IC=-0.443 (n=51)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.1362
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=101)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `sigma_h` > `0.006` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0083` → IC=-0.259 (n=52)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0083
  - _Potencial_: sin este filtro IC_bueno=-0.078 (n=107)

- **FILTRO** `T_h` > `94.0115` → IC=-0.204 (n=106)

  - _Acción_: SKIP cuando `T_h` > 94.0115
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=53)

- **FILTRO** `sigma_h` > `0.0156` → IC=-0.357 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0156
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=81)

- **FILTRO** `T_h` > `41.2641` → IC=-0.322 (n=71)

  - _Acción_: SKIP cuando `T_h` > 41.2641
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=36)

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

- **PATRÓN** `edge` > `0.097` → IC=+0.444 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.097 (IC base=+0.416)

- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.432 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.416)

- **PATRÓN** `T_h` < `0.5922` → IC=+0.431 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5922 (IC base=+0.416)

- **PATRÓN** `T_h` > `1.4829` → IC=+0.431 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.4829 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.3772` → IC=+0.458 (n=212)

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

- **PATRÓN** `T_h` < `0.6978` → IC=+0.444 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.6978 (IC base=+0.418)

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

- **PATRÓN** `edge` > `0.1961` → IC=+0.478 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.464)

- **PATRÓN** `sigma_h` < `0.0157` → IC=+0.478 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0157 (IC base=+0.464)

- **PATRÓN** `T_h` > `1.1834` → IC=+0.478 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.1834 (IC base=+0.464)

- **PATRÓN** `dist_50` > `0.4384` → IC=+0.485 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4384 (IC base=+0.464)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.464)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=298)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=374)

- **FILTRO** `streak_estiramiento` > `0.8469` → IC=-0.182 (n=83)

  - _Acción_: SKIP cuando `streak_estiramiento` > 0.8469
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=250)

- **PATRÓN** `streak_estiramiento` < `0.5606` → IC=+0.186 (n=167)

  - _Acción_: Kelly boost +0.93€ cuando `streak_estiramiento` < 0.5606 (IC base=+0.041)

- **PATRÓN** `libro_liquidez` > `2756.3002` → IC=+0.147 (n=100)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2756.3002 (IC base=+0.041)

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
- **PATRÓN** `volumen_racha` < `945898.4` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_racha` < 945898.4 (IC base=+0.004)

- **PATRÓN** `streak_estiramiento` < `0.2292` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `streak_estiramiento` < 0.2292 (IC base=+0.004)

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

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.024)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=953)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=1329)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.011 (n=1099)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.037 (n=1131)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `14.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3864)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `14.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=2123)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.197 (n=1509)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0053 (IC base=+0.180)

- **PATRÓN** `sigma_h` > `0.012` → IC=+0.195 (n=1143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.012 (IC base=+0.180)

- **PATRÓN** `drift_60min` |x|≤ `0.1731` → IC=+0.195 (n=3018)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1731 (IC base=+0.180)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1333` → IC=+0.191 (n=1362)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1333 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=3182)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.183 (n=3155)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.180)

- **PATRÓN** `ibs_15` > `0.5645` → IC=+0.257 (n=3430)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5645 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.1251` → IC=+0.172 (n=1636)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1251 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` < `0.6735` → IC=+0.167 (n=3235)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.6735 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.61` → IC=+0.254 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.61 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `4887.7162` → IC=+0.202 (n=1143)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4887.7162 (IC base=+0.180)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=1345)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.231 (n=586)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.223)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.264 (n=197)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.223)

- **PATRÓN** `delta_ratio_macro` |x|> `0.25` → IC=+0.241 (n=195)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.25 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.243 (n=547)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `ibs_15` > `0.7243` → IC=+0.284 (n=585)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7243 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` > `0.1354` → IC=+0.246 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1354 (IC base=+0.223)

- **PATRÓN** `dist_vwap_pct` < `0.5214` → IC=+0.224 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5214 (IC base=+0.223)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.305 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.224 (n=759)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `16272.4583` → IC=+0.256 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16272.4583 (IC base=+0.223)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.190 (n=224)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0034 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.1497` → IC=+0.149 (n=591)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.75€ cuando `drift_60min` |x|≤ 0.1497 (IC base=+0.144)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1455` → IC=+0.148 (n=447)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.74€ cuando `delta_ratio_macro` |x|> 0.1455 (IC base=+0.144)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1354` → IC=+0.164 (n=263)

  - _Acción_: Kelly boost +0.82€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1354 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.152 (n=613)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.150 (n=472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 11.0 (IC base=+0.144)

- **PATRÓN** `ibs_15` > `0.5476` → IC=+0.244 (n=671)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5476 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.1154` → IC=+0.156 (n=422)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1154 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` < `0.6102` → IC=+0.145 (n=765)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.6102 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.851` → IC=+0.285 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.851 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `3537.6258` → IC=+0.154 (n=599)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3537.6258 (IC base=+0.144)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `18.005` → IC=-0.184 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.005
  - _Potencial_: sin este filtro IC_bueno=+0.058 (n=301)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.138 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0061 (IC base=+0.094)

- **PATRÓN** `drift_60min` |x|≤ `0.1666` → IC=+0.139 (n=488)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1666 (IC base=+0.094)

- **PATRÓN** `ibs_15` > `0.9` → IC=+0.245 (n=245)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.9 (IC base=+0.094)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.130 (n=401)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.094)

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
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.367 (n=405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0041 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.387 (n=202)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.364)

- **PATRÓN** `drift_15min` |x|≤ `0.4004` → IC=+0.363 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4004 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1505` → IC=+0.384 (n=404)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1505 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2297` → IC=+0.383 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2297 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.377 (n=609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.400 (n=608)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4165` → IC=+0.392 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4165 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.772` → IC=+0.386 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.772 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3507.1457` → IC=+0.373 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3507.1457 (IC base=+0.364)

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
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.361 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.360)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.380 (n=131)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.360)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0903` → IC=+0.373 (n=258)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0903 (IC base=+0.360)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2995` → IC=+0.379 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2995 (IC base=+0.360)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.387 (n=139)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.360)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.367 (n=133)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.360)

- **PATRÓN** `ibs_15` > `0.7504` → IC=+0.411 (n=289)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7504 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.380 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.360)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.362 (n=266)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.360)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.352` → IC=+0.387 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.352 (IC base=+0.360)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.365 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.360)

- **PATRÓN** `libro_liquidez` > `3951.8446` → IC=+0.395 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3951.8446 (IC base=+0.360)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0124` → IC=-0.223 (n=1053)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0124
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3161)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.210 (n=1649)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=2565)

- **FILTRO** `libro_liquidez` < `4174.6285` → IC=-0.152 (n=2781)

  - _Acción_: SKIP cuando `libro_liquidez` < 4174.6285
  - _Potencial_: sin este filtro IC_bueno=+0.101 (n=1433)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.284 (n=1017)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.1092` → IC=+0.210 (n=587)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1092 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.4242` → IC=+0.203 (n=989)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4242 (IC base=-0.066)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2291` → IC=+0.270 (n=1156)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2291 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3584` → IC=+0.282 (n=3467)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3584 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6637` → IC=+0.281 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6637 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0341` → IC=-0.218 (n=1807)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0341
  - _Potencial_: sin este filtro IC_bueno=-0.123 (n=603)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.233 (n=602)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.181 (n=1808)

- **FILTRO** `sigma_ewma_delta_pct` > `23.489` → IC=-0.267 (n=346)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.489
  - _Potencial_: sin este filtro IC_bueno=-0.182 (n=2064)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.212 (n=64)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2346)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.126 (n=723)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0052 (IC base=+0.101)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2033` → IC=+0.300 (n=148)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2033 (IC base=+0.101)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.101)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.336 (n=327)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.102` → IC=+0.298 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.102 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` < `0.3659` → IC=+0.294 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3659 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.617` → IC=+0.137 (n=364)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 8.617 (IC base=+0.101)

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
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=660)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.166 (n=447)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0058 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.165 (n=454)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0038 (IC base=+0.154)

- **PATRÓN** `drift_60min` |x|≤ `0.0712` → IC=+0.190 (n=224)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.95€ cuando `drift_60min` |x|≤ 0.0712 (IC base=+0.154)

- **PATRÓN** `drift_15min` |x|≤ `0.4004` → IC=+0.157 (n=170)

  - _Acción_: Kelly boost +0.78€ cuando `drift_15min` |x|≤ 0.4004 (IC base=+0.154)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.194 (n=387)

  - _Acción_: Kelly boost +0.97€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.167 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 6.0 (IC base=+0.154)

- **PATRÓN** `ibs_15` > `0.6189` → IC=+0.255 (n=508)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6189 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.456` → IC=+0.167 (n=136)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.456 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` < `0.6448` → IC=+0.154 (n=585)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.6448 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.422` → IC=+0.260 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.422 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=660)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `10043.6494` → IC=+0.169 (n=170)

  - _Acción_: Kelly boost +0.84€ cuando `libro_liquidez` > 10043.6494 (IC base=+0.154)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.248 (n=1222)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.244)

- **PATRÓN** `drift_60min` |x|≤ `0.4483` → IC=+0.244 (n=1222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4483 (IC base=+0.244)

- **PATRÓN** `drift_15min` |x|≤ `0.7706` → IC=+0.260 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7706 (IC base=+0.244)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2158` → IC=+0.263 (n=554)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2158 (IC base=+0.244)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.253 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.244)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.249 (n=473)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.244)

- **PATRÓN** `ibs_15` < `0.3703` → IC=+0.274 (n=1222)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3703 (IC base=+0.244)

- **PATRÓN** `dist_vwap_pct` > `0.6027` → IC=+0.274 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6027 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.522` → IC=+0.251 (n=544)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.522 (IC base=+0.244)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.548` → IC=+0.248 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.548 (IC base=+0.244)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1726` → IC=-0.256 (n=330)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1726
  - _Potencial_: sin este filtro IC_bueno=-0.153 (n=641)

- **FILTRO** `drift_15min` |x|> `0.8922` → IC=-0.279 (n=242)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.8922
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=729)

- **FILTRO** `sigma_ewma_delta_pct` > `6.585` → IC=-0.200 (n=228)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.585
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=743)

- **FILTRO** `sigma_ewma_delta_pct` > `18.012` → IC=-0.146 (n=509)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 18.012
  - _Potencial_: sin este filtro IC_bueno=-0.025 (n=4038)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1478` → IC=+0.181 (n=45)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.1478 (IC base=-0.189)

- **PATRÓN** `ibs_15` > `0.5625` → IC=+0.234 (n=62)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5625 (IC base=-0.189)

- **PATRÓN** `dist_vwap_pct` < `0.4298` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.4298 (IC base=-0.189)

- **PATRÓN** `ballena_activa_n` < `44.0` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 44.0 (IC base=-0.189)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0646` → IC=+0.245 (n=543)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0646 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.35` → IC=+0.290 (n=545)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.35 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4499` → IC=+0.251 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4499 (IC base=-0.039)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.250 (n=585)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=586)

- **FILTRO** `sigma_ewma_delta_pct` > `7.379` → IC=-0.208 (n=364)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.379
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=807)

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
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.298 (n=908)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.053` → IC=+0.318 (n=344)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.053 (IC base=+0.291)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2395` → IC=+0.303 (n=344)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2395 (IC base=+0.291)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2248` → IC=+0.307 (n=611)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2248 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.307 (n=1079)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.291)

- **PATRÓN** `ibs_15` > `0.8382` → IC=+0.321 (n=1032)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8382 (IC base=+0.291)

- **PATRÓN** `dist_vwap_pct` > `0.266` → IC=+0.322 (n=447)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.266 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.656` → IC=+0.376 (n=231)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.656 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `12471.9662` → IC=+0.311 (n=468)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12471.9662 (IC base=+0.291)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.314 (n=245)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.288)

- **PATRÓN** `drift_60min` |x|≤ `0.0574` → IC=+0.314 (n=186)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0574 (IC base=+0.288)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2522` → IC=+0.313 (n=185)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2522 (IC base=+0.288)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3961` → IC=+0.300 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3961 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=557)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `ibs_15` > `0.827` → IC=+0.313 (n=555)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.827 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.2523` → IC=+0.322 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2523 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.837` → IC=+0.382 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.837 (IC base=+0.288)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.288 (n=719)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.288)

- **PATRÓN** `libro_liquidez` > `16294.6642` → IC=+0.334 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16294.6642 (IC base=+0.288)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.304 (n=477)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.293)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.292 (n=426)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0039 (IC base=+0.293)

- **PATRÓN** `drift_60min` |x|≤ `0.0506` → IC=+0.314 (n=159)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0506 (IC base=+0.293)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1481` → IC=+0.297 (n=318)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1481 (IC base=+0.293)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1057` → IC=+0.337 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1057 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.305 (n=491)
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
- **PATRÓN** `T_h` > `83.5733` → IC=+0.196 (n=458)

  - _Acción_: Kelly boost +0.98€ cuando `T_h` > 83.5733 (IC base=+0.191)

- **PATRÓN** `ratio` < `0.973` → IC=+0.422 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.191)

- **PATRÓN** `T_h` > `111.9969` → IC=+0.353 (n=2083)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.337)

- **PATRÓN** `ratio` > `1.0236` → IC=+0.373 (n=328)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0236 (IC base=+0.337)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `103.5964` → IC=+0.184 (n=188)

  - _Acción_: Kelly boost +0.92€ cuando `T_h` > 103.5964 (IC base=+0.163)

- **PATRÓN** `ratio` < `0.9943` → IC=+0.288 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9943 (IC base=+0.163)

- **PATRÓN** `T_h` > `109.882` → IC=+0.307 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 109.882 (IC base=+0.294)

- **PATRÓN** `ratio` > `1.0464` → IC=+0.398 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0464 (IC base=+0.294)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.237 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.230)

- **PATRÓN** `ratio` < `0.9849` → IC=+0.432 (n=188)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9849 (IC base=+0.230)

- **PATRÓN** `T_h` > `111.9836` → IC=+0.353 (n=758)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9836 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0372` → IC=+0.401 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0372 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1038` → IC=+0.448 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1038 (IC base=+0.400)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5645 sube el IC de +0.180 a +0.257 en UPDOWN_GBM#15min (n=3430). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7243 sube el IC de +0.223 a +0.284 en UPDOWN_GBM#BTC#15min (n=585). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5476 sube el IC de +0.144 a +0.244 en UPDOWN_GBM#ETH#15min (n=671). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.9 sube el IC de +0.094 a +0.245 en UPDOWN_GBM#SOL#15min (n=245). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5429 sube el IC de +0.202 a +0.282 en UPDOWN_GBM#XRP#15min (n=800). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.157 en UPDOWN_GBM#XRP#15min (n=768). Ya aplicado como kelly_boost=+0.79€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.066 a +0.284 en UPDOWN_GBM_15M_TARDIO (n=1017). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3584 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3467). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.101 a +0.336 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=327). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.194 a +0.293 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=56). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6189 sube el IC de +0.154 a +0.255 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=508). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3703 sube el IC de +0.244 a +0.274 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1222). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.189 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.35 sube el IC de -0.039 a +0.290 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=545). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.206 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.025 a +0.293 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=845). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.068 a +0.324 en UPDOWN_GBM_ETH_15M_HORA7 (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.068 a +0.324 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=15). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8382 sube el IC de +0.291 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=1032). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.827 sube el IC de +0.288 a +0.313 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=555). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8527 sube el IC de +0.293 a +0.325 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=477). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.364 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=608). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8057 sube el IC de +0.366 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=318). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7504 sube el IC de +0.360 a +0.411 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=289). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1840 | +0.091 | +202.19€ | 1 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1840 | +0.091 | +202.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1456 | +0.095 | +177.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1456 | +0.095 | +177.74€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 280 | +0.067 | +10.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 280 | +0.067 | +10.78€ | 5 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 73 | +0.100 | +14.01€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 73 | +0.100 | +14.01€ | 0 | 6 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 531 | -0.020 | +52.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 531 | -0.020 | +52.22€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 380 | -0.044 | +26.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 380 | -0.044 | +26.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 121 | +0.053 | +20.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 121 | +0.053 | +20.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 27 | -0.017 | +2.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 27 | -0.017 | +2.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 38900 | -0.082 | -4891.09€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2123 | +0.031 | -236.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 36777 | -0.088 | -4654.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4437 | -0.116 | -764.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4437 | -0.116 | -764.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2123 | +0.031 | -236.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2123 | +0.031 | -236.43€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4278 | -0.105 | -878.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4278 | -0.105 | -878.06€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10316 | -0.017 | -914.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10316 | -0.017 | -914.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10173 | -0.103 | -786.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10173 | -0.103 | -786.36€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7573 | -0.138 | -1311.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7573 | -0.138 | -1311.05€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 33043 | -0.016 | +3532.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8550 | +0.005 | +1711.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 24493 | -0.024 | +1820.91€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 33043 | -0.016 | +3532.87€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8550 | +0.005 | +1711.96€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 24493 | -0.024 | +1820.91€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 138815 | +0.115 | -5728.07€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18121 | +0.183 | -516.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 606 | -0.023 | -67.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 111720 | +0.105 | -4854.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8368 | +0.102 | -288.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 18532 | +0.107 | -1154.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 18456 | +0.108 | -1153.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 26998 | +0.128 | -366.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5126 | +0.191 | -147.81€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 18516 | +0.120 | -108.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3314 | +0.084 | -87.30€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 18583 | +0.097 | -1364.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 71 | -0.116 | -5.63€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 18497 | +0.098 | -1347.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 29512 | +0.124 | -552.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7684 | +0.178 | -123.25€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 18754 | +0.106 | -365.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3062 | +0.100 | -55.52€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 26638 | +0.115 | -1358.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5113 | +0.195 | -254.88€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 509 | +0.011 | -13.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 19024 | +0.094 | -944.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 1992 | +0.135 | -145.99€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 18552 | +0.104 | -931.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 66 | -0.088 | +4.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 18473 | +0.105 | -935.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 22290 | +0.196 | -1354.99€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 22290 | +0.196 | -1354.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5092 | +0.177 | -451.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5092 | +0.177 | -451.58€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2743 | +0.204 | -52.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2743 | +0.204 | -52.26€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5035 | +0.181 | -400.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5035 | +0.181 | -400.53€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4379 | +0.248 | -138.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4379 | +0.248 | -138.22€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 4962 | +0.187 | -326.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 4962 | +0.187 | -326.17€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 979 | +0.428 | -32.15€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 979 | +0.428 | -32.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 385 | +0.438 | -3.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 385 | +0.438 | -3.94€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 383 | +0.430 | -10.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 383 | +0.430 | -10.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 198 | +0.400 | -15.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 198 | +0.400 | -15.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 77877 | +0.200 | -5662.21€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 77877 | +0.200 | -5662.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 13373 | +0.185 | -1379.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 13373 | +0.185 | -1379.75€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 12576 | +0.224 | -446.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 12576 | +0.224 | -446.85€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 13345 | +0.180 | -1431.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 13345 | +0.180 | -1431.44€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 12647 | +0.220 | -480.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 12647 | +0.220 | -480.20€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 12912 | +0.201 | -864.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 12912 | +0.201 | -864.20€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13024 | +0.196 | -1059.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13024 | +0.196 | -1059.76€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 29777 | +0.117 | +228.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 29777 | +0.117 | +228.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 14801 | +0.120 | +188.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 14801 | +0.120 | +188.41€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 14976 | +0.114 | +40.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 14976 | +0.114 | +40.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2001 | +0.290 | -20.02€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2001 | +0.290 | -20.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 916 | +0.277 | -29.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 916 | +0.277 | -29.56€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 966 | +0.293 | +4.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 966 | +0.293 | +4.23€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 922 | +0.441 | +2.52€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 922 | +0.441 | +2.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 446 | +0.435 | -4.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 446 | +0.435 | -4.49€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 430 | +0.447 | +6.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 430 | +0.447 | +6.45€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1568 | +0.071 | -62.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 602 | +0.055 | -46.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 966 | +0.082 | -15.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 72 | +0.108 | +2.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1207 | +0.079 | -25.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 241 | +0.068 | -9.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 966 | +0.082 | -15.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 289 | +0.029 | -39.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 289 | +0.029 | -39.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 58508 | +0.100 | -1513.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4730 | +0.091 | +56.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 53778 | +0.101 | -1569.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 32238 | +0.105 | -361.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4730 | +0.091 | +56.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 27508 | +0.107 | -418.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 11942 | +0.109 | -51.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 11942 | +0.109 | -51.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 14328 | +0.081 | -1099.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 14328 | +0.081 | -1099.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 894 | +0.192 | -112.64€ | 3 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 894 | +0.192 | -112.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 894 | +0.192 | -112.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 894 | +0.192 | -112.64€ | 3 | 4 |
| ✅ GBM_LATE_15M | 40387 | +0.093 | +20793.03€ | 0 | 18 |
| ✅ GBM_LATE_15M#15min | 40387 | +0.093 | +20793.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 6752 | +0.212 | +5446.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 6752 | +0.212 | +5446.99€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6071 | +0.178 | +4554.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6071 | +0.178 | +4554.49€ | 0 | 25 |
| ✅ GBM_LATE_15M#DOGE | 7205 | +0.204 | +5560.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7205 | +0.204 | +5560.83€ | 0 | 20 |
| ✅ GBM_LATE_15M#ETH | 5644 | +0.040 | +1542.74€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5644 | +0.040 | +1542.74€ | 1 | 18 |
| ✅ GBM_LATE_15M#SOL | 5703 | -0.031 | +1205.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5703 | -0.031 | +1205.78€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 9012 | -0.032 | +2482.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9012 | -0.032 | +2482.21€ | 3 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 43565 | +0.086 | +23597.61€ | 0 | 17 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 43565 | +0.086 | +23597.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8433 | +0.005 | +4296.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8433 | +0.005 | +4296.54€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9193 | +0.012 | +2131.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9193 | +0.012 | +2131.12€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6059 | +0.276 | +6442.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6059 | +0.276 | +6442.60€ | 0 | 20 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 7746 | +0.013 | +1896.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 7746 | +0.013 | +1896.89€ | 1 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 6977 | +0.039 | +2860.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 6977 | +0.039 | +2860.89€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5157 | +0.299 | +5969.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5157 | +0.299 | +5969.57€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 32051 | +0.178 | +25690.51€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 32051 | +0.178 | +25690.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 4868 | +0.225 | +4236.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 4868 | +0.225 | +4236.60€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5044 | +0.149 | +3722.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5044 | +0.149 | +3722.07€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5127 | +0.222 | +4382.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5127 | +0.222 | +4382.48€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5423 | +0.137 | +4093.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5423 | +0.137 | +4093.66€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6024 | +0.123 | +4439.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6024 | +0.123 | +4439.36€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5565 | +0.223 | +4816.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5565 | +0.223 | +4816.34€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8563 | +0.134 | +4151.96€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8563 | +0.134 | +4151.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2548 | +0.142 | +1439.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2548 | +0.142 | +1439.77€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2553 | +0.140 | +1203.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2553 | +0.140 | +1203.91€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2074 | +0.110 | +805.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2074 | +0.110 | +805.09€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 565 | +0.130 | +242.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 565 | +0.130 | +242.93€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO | 40593 | +0.184 | +32131.91€ | 0 | 22 |
| ✅ GBM_LATE_15M_TARDIO#15min | 40593 | +0.184 | +32131.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6438 | +0.238 | +5911.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6438 | +0.238 | +5911.39€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6330 | +0.147 | +4271.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6330 | +0.147 | +4271.06€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 6844 | +0.231 | +6073.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 6844 | +0.231 | +6073.83€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6684 | +0.138 | +4751.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6684 | +0.138 | +4751.21€ | 0 | 23 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7176 | +0.121 | +4909.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7176 | +0.121 | +4909.46€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7121 | +0.227 | +6214.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7121 | +0.227 | +6214.97€ | 0 | 21 |
| ✅ GBM_LATE_5M | 11248 | +0.197 | +8490.58€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 11248 | +0.197 | +8490.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 919 | +0.232 | +813.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2589 | +0.196 | +2110.44€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2589 | +0.196 | +2110.44€ | 0 | 27 |
| ✅ GBM_LATE_5M#DOGE | 1039 | +0.177 | +686.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1039 | +0.177 | +686.71€ | 0 | 15 |
| ✅ GBM_LATE_5M#ETH | 3304 | +0.194 | +2340.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3304 | +0.194 | +2340.33€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 1667 | +0.190 | +1248.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1667 | +0.190 | +1248.66€ | 0 | 26 |
| ✅ GBM_LATE_5M#XRP | 1730 | +0.200 | +1290.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1730 | +0.200 | +1290.45€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3256 | +0.069 | +1128.71€ | 0 | 9 |
| ✅ GBM_LATE_60M#60min | 3256 | +0.069 | +1128.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1210 | +0.086 | +474.22€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1210 | +0.086 | +474.22€ | 0 | 8 |
| ✅ GBM_LATE_60M#ETH | 1045 | +0.073 | +388.58€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1045 | +0.073 | +388.58€ | 0 | 11 |
| ✅ GBM_LATE_60M#SOL | 1001 | +0.045 | +265.91€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1001 | +0.045 | +265.91€ | 1 | 12 |
| 🚫 GBM_LATE_60M_FADE | 543 | -0.245 | -22.86€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 543 | -0.245 | -22.86€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 203 | -0.241 | -11.96€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 203 | -0.241 | -11.96€ | 4 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 192 | -0.227 | -2.51€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 192 | -0.227 | -2.51€ | 5 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 148 | -0.267 | -8.39€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 148 | -0.267 | -8.39€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1458 | +0.082 | +388.58€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1458 | +0.082 | +388.58€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 579 | +0.080 | +146.26€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 579 | +0.080 | +146.26€ | 1 | 13 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 526 | +0.057 | +84.38€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 526 | +0.057 | +84.38€ | 2 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 353 | +0.122 | +157.94€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 353 | +0.122 | +157.94€ | 2 | 9 |
| ✅ LATE_WINDOW_5MIN | 161 | +0.273 | +154.25€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 161 | +0.273 | +154.25€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 161 | +0.273 | +154.25€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 161 | +0.273 | +154.25€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3285 | +0.101 | +814.76€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3285 | +0.101 | +814.76€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3285 | +0.101 | +814.76€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3285 | +0.101 | +814.76€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 482 | -0.056 | -25.78€ | 2 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 482 | -0.056 | -25.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 135 | -0.018 | +0.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 135 | -0.018 | +0.92€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 87 | -0.073 | -7.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 87 | -0.073 | -7.11€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 179 | -0.014 | -2.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 179 | -0.014 | -2.73€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3609 | +0.016 | +81.68€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3609 | +0.016 | +81.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 174 | +0.023 | -2.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 174 | +0.023 | -2.27€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 741 | +0.015 | +35.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 741 | +0.015 | +35.52€ | 4 | 1 |
| ✅ LIQUIDACIONES_5M#DOGE | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 203 | -0.017 | -5.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1298 | +0.025 | +29.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1298 | +0.025 | +29.80€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 754 | +0.011 | +0.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 754 | +0.011 | +0.86€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 439 | +0.013 | +22.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 439 | +0.013 | +22.85€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1698 | -0.039 | -26.14€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1698 | -0.039 | -26.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 487 | -0.030 | -10.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 487 | -0.030 | -10.66€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 574 | -0.014 | +6.48€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 574 | -0.014 | +6.48€ | 3 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 637 | -0.070 | -21.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 637 | -0.070 | -21.96€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 7898 | -0.028 | -3.44€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 3735 | -0.036 | -82.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4163 | -0.019 | +79.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 225 | -0.024 | +1.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 115 | -0.004 | +4.69€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 110 | -0.045 | -3.69€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 1982 | -0.018 | +22.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 937 | -0.023 | -2.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1045 | -0.014 | +25.05€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 860 | -0.022 | +17.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 431 | -0.040 | -8.29€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 429 | -0.004 | +25.79€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1710 | -0.044 | -71.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 794 | -0.059 | -64.90€ | 5 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 916 | -0.032 | -6.15€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1542 | -0.022 | +19.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 733 | -0.036 | -13.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 809 | -0.009 | +32.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1579 | -0.029 | +7.22€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 725 | -0.032 | +1.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 854 | -0.027 | +5.83€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 47195 | -0.001 | +2394.53€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 47195 | -0.001 | +2394.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8494 | +0.025 | +1088.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8494 | +0.025 | +1088.70€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 6844 | -0.033 | -84.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 6844 | -0.033 | -84.23€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 8601 | +0.024 | +891.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 8601 | +0.024 | +891.34€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6682 | -0.047 | -136.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6682 | -0.047 | -136.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 7963 | -0.005 | +238.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 7963 | -0.005 | +238.92€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 8611 | +0.015 | +396.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 8611 | +0.015 | +396.32€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6515 | -0.061 | -166.03€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6515 | -0.061 | -166.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1673 | -0.081 | -46.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1673 | -0.081 | -46.70€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 53 | -0.064 | -2.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 763 | -0.120 | -32.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 763 | -0.120 | -32.55€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1945 | -0.078 | -43.55€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1945 | -0.078 | -43.55€ | 2 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 117469 | -0.075 | +1881.28€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 117469 | -0.075 | +1881.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 20371 | -0.076 | +1100.43€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 20371 | -0.076 | +1100.43€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 17712 | -0.099 | -937.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 17712 | -0.099 | -937.17€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 20668 | -0.067 | +1145.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 20668 | -0.067 | +1145.52€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 17254 | -0.096 | -551.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 17254 | -0.096 | -551.52€ | 7 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 21093 | -0.055 | +372.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 21093 | -0.055 | +372.07€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 20371 | -0.065 | +751.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 20371 | -0.065 | +751.95€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8700 | -0.033 | -179.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8700 | -0.033 | -179.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1967 | -0.045 | -23.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1967 | -0.045 | -23.08€ | 3 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2576 | -0.026 | -41.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2576 | -0.026 | -41.14€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1186 | -0.055 | -28.11€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1186 | -0.055 | -28.11€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 962 | -0.031 | -35.57€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 962 | -0.031 | -35.57€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1608 | +0.125 | +664.56€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#5min | 1472 | +0.131 | +651.97€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 346 | +0.147 | +186.57€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 346 | +0.147 | +186.57€ | 0 | 3 |
| ✅ ORDER_FLOW_5M#DOGE | 301 | +0.120 | +106.50€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 301 | +0.120 | +106.50€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 294 | +0.135 | +140.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 294 | +0.135 | +140.98€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 260 | +0.153 | +144.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 260 | +0.153 | +144.26€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 271 | +0.093 | +73.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 271 | +0.093 | +73.67€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1338 | -0.010 | +1.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1338 | -0.010 | +1.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 261 | +0.006 | +14.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 261 | +0.006 | +14.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 233 | -0.006 | +2.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 233 | -0.006 | +2.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 349 | -0.036 | -20.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 349 | -0.036 | -20.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 279 | +0.009 | +3.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 279 | +0.009 | +3.74€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 216 | -0.014 | +0.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 216 | -0.014 | +0.65€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 864 | -0.067 | -36.27€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 402 | -0.111 | -74.75€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 313 | -0.141 | -64.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 89 | -0.005 | -9.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 308 | -0.029 | +26.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 222 | -0.022 | +26.87€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 86 | -0.045 | -0.50€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 154 | -0.026 | +12.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 124 | -0.032 | +7.21€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 30 | +0.000 | +4.90€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 659 | -0.081 | -30.87€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 205 | -0.022 | -5.40€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1075 | -0.207 | -63.63€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 426 | -0.208 | -40.36€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 370 | -0.212 | -40.64€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 56 | -0.172 | +0.28€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 364 | -0.216 | -32.83€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 318 | -0.225 | -38.52€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 46 | -0.146 | +5.69€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 285 | -0.193 | +9.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 266 | -0.190 | +6.42€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 19 | -0.204 | +3.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 954 | -0.211 | -72.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 121 | -0.175 | +9.11€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 436 | +0.393 | +406.93€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 61 | +0.135 | +49.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 61 | +0.135 | +49.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 107 | +0.362 | +89.61€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 107 | +0.362 | +89.61€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 268 | +0.459 | +267.65€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 268 | +0.459 | +267.65€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 436 | +0.393 | +406.93€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 710 | +0.028 | +32.92€ | 3 | 2 |
| ✅ STREAK_FADE_15M#15min | 710 | +0.028 | +32.92€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 300 | +0.023 | +3.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 300 | +0.023 | +3.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 58 | -0.017 | -3.08€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 58 | -0.017 | -3.08€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 73 | -0.007 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 73 | -0.007 | +0.78€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 279 | +0.052 | +31.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 279 | +0.052 | +31.86€ | 0 | 6 |
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
| ✅ STREAK_FADE_60M | 97 | -0.056 | -9.95€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 97 | -0.056 | -9.95€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 40 | -0.071 | -3.54€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 40 | -0.071 | -3.54€ | 2 | 0 |
| ✅ STREAK_FADE_60M#SOL | 57 | -0.042 | -6.41€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 57 | -0.042 | -6.41€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10591 | +0.018 | +99.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10591 | +0.018 | +99.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2704 | +0.020 | +26.01€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2704 | +0.020 | +26.01€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2728 | +0.021 | +41.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2728 | +0.021 | +41.17€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2887 | +0.009 | -1.49€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2887 | +0.009 | -1.49€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2272 | +0.021 | +33.80€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2272 | +0.021 | +33.80€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9651 | +0.013 | -46.39€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9651 | +0.013 | -46.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3883 | +0.017 | -8.17€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3883 | +0.017 | -8.17€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3611 | +0.011 | -27.83€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3611 | +0.011 | -27.83€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2157 | +0.010 | -10.39€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2157 | +0.010 | -10.39€ | 1 | 0 |
| ✅ UPDOWN_GBM | 73274 | +0.053 | +6417.32€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 18416 | +0.083 | +4055.92€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2369 | +0.005 | +19.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 47963 | +0.048 | +2259.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4272 | +0.008 | +83.06€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 15327 | +0.055 | +1317.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2339 | +0.090 | +578.06€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 627 | +0.012 | +11.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 10369 | +0.060 | +666.10€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1900 | +0.005 | +57.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 92 | -0.064 | +3.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8261 | +0.067 | +866.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6628 | +0.049 | +257.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 16538 | +0.043 | +1050.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4282 | +0.063 | +616.30€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 612 | +0.006 | +11.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10081 | +0.043 | +402.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1479 | +0.013 | +18.14€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 84 | -0.105 | +2.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 16131 | +0.031 | +742.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4541 | +0.033 | +365.62€ | 0 | 4 |
| ✅ UPDOWN_GBM#SOL#240min | 587 | -0.006 | -0.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10034 | +0.035 | +375.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 893 | +0.007 | +7.21€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 76 | -0.128 | -4.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10164 | +0.063 | +1366.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4123 | +0.101 | +1186.91€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5653 | +0.038 | +179.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 252 | -0.098 | +1.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 808 | +0.364 | +294.07€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 808 | +0.364 | +294.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 423 | +0.366 | +149.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 423 | +0.366 | +149.18€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 385 | +0.360 | +144.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 385 | +0.360 | +144.89€ | 0 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19351 | -0.024 | +4600.68€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19351 | -0.024 | +4600.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3373 | -0.110 | +153.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3373 | -0.110 | +153.81€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2305 | +0.217 | +1509.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2305 | +0.217 | +1509.14€ | 1 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5518 | -0.065 | +673.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5518 | -0.065 | +673.82€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5489 | -0.064 | +990.64€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5489 | -0.064 | +990.64€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 218 | +0.032 | +7.39€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 218 | +0.032 | +7.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 218 | +0.032 | +7.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 218 | +0.032 | +7.39€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1375 | +0.291 | +1166.38€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1375 | +0.291 | +1166.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 740 | +0.288 | +596.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 740 | +0.288 | +596.35€ | 0 | 10 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 635 | +0.293 | +570.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 635 | +0.293 | +570.03€ | 0 | 10 |
| ✅ UPDOWN_OU_5M | 810 | -0.111 | -81.91€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 810 | -0.111 | -81.91€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 247 | -0.078 | -17.59€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 247 | -0.078 | -17.59€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 86 | -0.159 | -8.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 86 | -0.159 | -8.64€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 94 | -0.188 | -6.32€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 94 | -0.188 | -6.32€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3450 | +0.304 | +1668.47€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1258 | +0.258 | +168.96€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1325 | +0.299 | +599.85€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 867 | +0.379 | +899.66€ | 0 | 1 |
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
  - _Estado_: 696 celda(s) pasan gate riguroso completo de 2651 evaluadas (n>=40) y 3680 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.033 < 0.08 — monitorear
  - _Datos_: n=4539 IC=+0.033 PNL=+367.17€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1325/15 IC=+0.299 PNL=+599.85€ | BTC: n=1258/15 IC=+0.258 PNL=+168.96€ | SOL: n=867/15 IC=+0.379 PNL=+899.66€

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
  - _Estado_: alineada_con_outcome_prev IC=+0.136 n=762/60 | contraria IC=+0.191 n=790 | gap=-0.055 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=445, boost estimado=+0.015. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 0/50 ops con delta_ratio feature

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1478/40 IC=+0.012 PNL=+17.64€ | BTC#60min: n=1900/40 IC=+0.005 PNL=+57.71€ | SOL#60min: n=893/40 IC=+0.007 PNL=+7.21€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.047 n=530390 | tras_1loss IC=+0.094 n=404041 | tras_2loss IC=+0.064 n=163921/40 | gap=-0.016 (umbral 0.05)

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.204 > 0.08 con n=710 PNL=+547.96€
  - _Datos_: n=710 IC=+0.204 PNL=+547.96€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.175 > 0.08 con n=800 PNL=+474.07€
  - _Datos_: n=800 IC=+0.175 PNL=+474.07€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.334 > 0.1 con n=2816 PNL=+1585.97€
  - _Datos_: n=2816 IC=+0.334 PNL=+1585.97€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=629 IC=+0.077 PNL=+74.14€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=629 IC=+0.077 PNL=+74.14€

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
  - _Estado_: n=2872 IC=+0.006 PNL=-1.33€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=2872 IC=+0.006 PNL=-1.33€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1399 IC=+0.012 PNL=+83.89€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1399 IC=+0.012 PNL=+83.89€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.180 > 0.1 con n=4569 PNL=+2906.75€
  - _Datos_: n=4569 IC=+0.180 PNL=+2906.75€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2337 IC=+0.090 PNL=+578.24€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2337 IC=+0.090 PNL=+578.24€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.130 > 0.02 con n=930 PNL=+405.32€
  - _Datos_: n=930 IC=+0.130 PNL=+405.32€

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
  - _Estado_: n=28482 IC=+0.073 PNL=+4122.49€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=28482 IC=+0.073 PNL=+4122.49€

**⏳ H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: 120
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: 0/120 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.140 < -0.1 con n=451 PNL=+52.46€
  - _Datos_: n=451 IC=-0.140 PNL=+52.46€

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
  - _Estado_: n=134 IC=-0.096 PNL=+4.38€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=134 IC=-0.096 PNL=+4.38€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.1 con n=761 PNL=+207.97€
  - _Datos_: n=761 IC=+0.111 PNL=+207.97€

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
  - _Estado_: n=30343 IC=-0.134 PNL=+2404.05€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=30343 IC=-0.134 PNL=+2404.05€

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
  - _Estado_: n=3071 IC=+0.133 PNL=+1841.92€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3071 IC=+0.133 PNL=+1841.92€

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
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.221 < -0.1 con n=3121 PNL=-233.59€
  - _Datos_: n=3121 IC=-0.221 PNL=-233.59€

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
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.101 n=1669) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1669 IC=+0.101 PNL=+367.83€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=555) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=555 IC=+0.414 PNL=+800.50€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=13365 IC=+0.185 PNL=-1381.33€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=13365 IC=+0.185 PNL=-1381.33€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.212 > 0.1 con n=220 PNL=+139.50€
  - _Datos_: n=220 IC=+0.212 PNL=+139.50€
