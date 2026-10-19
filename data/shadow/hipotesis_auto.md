# Hipótesis automáticas — 2026-10-19 21:39 UTC
_Generado por shadow_postmortem.py sobre 970759 resoluciones (PNL=+126110.58€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=624)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.238 (n=780)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.515 (IC base=+0.138)

- **PATRÓN** `n_total_lado` > `66.0` → IC=+0.182 (n=278)

  - _Acción_: Kelly boost +0.91€ cuando `n_total_lado` > 66.0 (IC base=+0.138)

- **PATRÓN** `banda_hit_calibrado` > `0.7998` → IC=+0.273 (n=552)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7998 (IC base=+0.138)

- **PATRÓN** `banda_z` > `9.204` → IC=+0.204 (n=278)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.204 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.172 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.154 (n=901)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.138)

- **PATRÓN** `ballena_activa_n` < `98.0` → IC=+0.153 (n=450)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 98.0 (IC base=+0.138)

### BALLENAS_CONFIRMADAS_15M#ETH#15min
- **PATRÓN** `py_entrada` > `0.55` → IC=+0.269 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.55 (IC base=+0.144)

- **PATRÓN** `n_total_lado` > `70.0` → IC=+0.202 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `n_total_lado` > 70.0 (IC base=+0.144)

- **PATRÓN** `banda_hit_calibrado` > `0.6177` → IC=+0.265 (n=466)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.6177 (IC base=+0.144)

- **PATRÓN** `banda_z` > `9.629` → IC=+0.211 (n=233)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 9.629 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.152 (n=802)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.155 (n=412)

  - _Acción_: Kelly boost +0.77€ cuando `ballena_activa_n` < 100.0 (IC base=+0.144)

- **PATRÓN** `libro_liquidez` > `9759.7992` → IC=+0.133 (n=205)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 9759.7992 (IC base=+0.017)

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
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=106)

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

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.120 (n=106)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.495 (IC base=+0.007)

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
- **FILTRO** `restante_s_al_confirmar` < `142.4` → IC=-0.207 (n=9968)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.4
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=29904)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.98` → IC=-0.263 (n=1120)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.98
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3360)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.52` → IC=-0.288 (n=1078)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.52
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3236)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.21` → IC=-0.208 (n=2625)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.21
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7878)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.28` → IC=-0.279 (n=1943)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.28
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=5831)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.213 (n=21452)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=4299)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `9160.5319` → IC=+0.178 (n=1938)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9160.5319 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.131 (n=18185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=32612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 11.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=16955)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.151 (n=7153)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7120.5951` → IC=+0.159 (n=2765)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 7120.5951 (IC base=+0.126)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=2020)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.194 (n=1974)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 17.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` > `0.775` → IC=+0.364 (n=644)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.775 (IC base=+0.193)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=2477)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.193)

- **PATRÓN** `libro_liquidez` > `16394.7121` → IC=+0.203 (n=642)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16394.7121 (IC base=+0.193)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.190 (n=1781)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 7.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=1980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=2539)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `16126.1219` → IC=+0.194 (n=655)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 16126.1219 (IC base=+0.184)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.167 (n=467)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `6860.5651` → IC=+0.172 (n=123)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6860.5651 (IC base=+0.081)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.140 (n=1108)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.086)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4168)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.161 (n=2838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 12.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.372 (n=1356)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` < `0.26` → IC=+0.360 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.26 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=2165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.144 (n=1050)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=681)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.263 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=825)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `1879.9984` → IC=+0.153 (n=669)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1879.9984 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=833)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.83` → IC=+0.418 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.83 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.150 (n=1287)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 7.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.160 (n=677)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 7.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.285 (n=646)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.149)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=853)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.149)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `9.0` → IC=+0.173 (n=310)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 9.0 (IC base=+0.159)

- **PATRÓN** `py_entrada` > `0.76` → IC=+0.342 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.76 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.153 (n=194)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.02 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `1131.3588` → IC=+0.147 (n=242)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 1131.3588 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.135 (n=1133)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 7.0 (IC base=+0.124)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.251 (n=407)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.124)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION
- **FILTRO** `hora_utc` > `11.0` → IC=-0.297 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=18120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=15336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=7468)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.182 (n=3951)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.181 (n=4160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 18.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4074)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=3410)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=2124)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.228 (n=2224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.306 (n=746)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=4111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=3220)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=3569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.361 (n=1139)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=4031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2572)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.194 (n=2972)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.189)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.433 (n=770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.428)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.441 (n=797)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.428)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.432 (n=813)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.428)

- **PATRÓN** `libro_liquidez` > `13089.4142` → IC=+0.445 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 13089.4142 (IC base=+0.428)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.451 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.437)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.449 (n=331)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.437)

- **PATRÓN** `libro_liquidez` > `18390.1556` → IC=+0.442 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 18390.1556 (IC base=+0.437)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.448 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.432)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.443 (n=313)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.432)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.435 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.432)

- **PATRÓN** `libro_liquidez` > `4391.5757` → IC=+0.441 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4391.5757 (IC base=+0.432)

### FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.408 (n=140)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.402)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.401 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.402)

- **PATRÓN** `py_entrada` > `0.915` → IC=+0.416 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.915 (IC base=+0.402)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION
- **FILTRO** `py_entrada` > `0.77` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `py_entrada` > 0.77
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=23493)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=23682)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=3482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=10514)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4908)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=4801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3439)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4021)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.212 (n=5355)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=4945)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=3750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.279 (n=3343)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=9007)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.261 (n=3483)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3905)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=3919)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=4078)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=8510)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=8347)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.78` → IC=+0.136 (n=10228)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.78 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=4210)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.144 (n=4254)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.130 (n=5097)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 7.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.77` → IC=+0.147 (n=3849)

  - _Acción_: Kelly boost +0.74€ cuando `lag_apertura_s` < 2.77 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=4300)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=4552)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.133 (n=5145)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 3.33 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1642)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=1621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=745)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.278)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `5005.426` → IC=+0.287 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5005.426 (IC base=+0.278)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=529)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.296)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.296)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.296)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.296 (n=881)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.296)

- **PATRÓN** `libro_liquidez` > `2114.2422` → IC=+0.309 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2114.2422 (IC base=+0.296)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=761)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=751)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.441)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.437 (n=363)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.435)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.440 (n=247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.435)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.436 (n=373)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.435)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.441 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.435)

### FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.453 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.448)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.451 (n=346)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.448)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.450 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.448)

- **PATRÓN** `libro_liquidez` > `1978.5089` → IC=+0.467 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.5089 (IC base=+0.448)

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
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=93)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=79)

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
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=93)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=79)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4778` → IC=+0.138 (n=13152)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4778 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=13319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.9804` → IC=+0.248 (n=4389)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9804 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.7841` → IC=+0.267 (n=726)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7841 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.3701` → IC=+0.258 (n=3697)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3701 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.927` → IC=+0.190 (n=4977)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.927 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2003` → IC=+0.257 (n=3811)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2003 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6202` → IC=+0.264 (n=3810)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6202 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.239 (n=1335)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3421` → IC=+0.227 (n=4237)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3421 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.122 (n=16195)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6854` → IC=+0.129 (n=18389)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.6854 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1528` → IC=+0.187 (n=5945)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1528 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.185 (n=2769)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6961 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0494` → IC=+0.180 (n=2852)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0494 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.232 (n=1571)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6796` → IC=+0.207 (n=3564)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6796 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.220 (n=10549)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.215 (n=955)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.3473` → IC=+0.201 (n=2863)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3473 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=1392)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=1914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.9802` → IC=+0.279 (n=1298)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9802 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.946` → IC=+0.281 (n=1255)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.946 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.247 (n=505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4375` → IC=+0.200 (n=2727)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4375 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=3059)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2080.07` → IC=+0.206 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2080.07 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.215 (n=1699)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=2397)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.241 (n=1089)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.272 (n=802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=875)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5255` → IC=+0.259 (n=2395)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5255 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.239 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.259 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.242 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6589` → IC=+0.247 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6589 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=2685)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1652.44` → IC=+0.244 (n=2139)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1652.44 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.241 (n=789)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.237 (n=1038)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.228 (n=1062)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1061` → IC=+0.260 (n=1031)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1061 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2462)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9509` → IC=+0.278 (n=781)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9509 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1285` → IC=+0.234 (n=1260)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1285 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.387` → IC=+0.264 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.387 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2306` → IC=+0.230 (n=2343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2306 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6225` → IC=+0.232 (n=2343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6225 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.261 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.5102` → IC=+0.229 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5102 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.252 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.151 (n=2378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0753` → IC=+0.166 (n=794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0753 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=900)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7285` → IC=+0.176 (n=2377)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7285 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.006` → IC=+0.146 (n=385)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 11.006 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.189` → IC=+0.141 (n=2174)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.189 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.1995` → IC=+0.141 (n=2377)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1995 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.160 (n=868)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4537` → IC=+0.142 (n=2257)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4537 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4135` → IC=+0.135 (n=2257)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4135 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.173 (n=964)

  - _Acción_: Kelly boost +0.86€ cuando `ballena_activa_n` < 218.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.218 (n=995)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=3127)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.271 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.274 (n=626)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.200 (n=2636)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.3519` → IC=+0.210 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3519 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.6914` → IC=+0.210 (n=1308)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6914 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=3553)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `1978.4984` → IC=+0.201 (n=1350)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.4984 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.223 (n=2343)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.6053` → IC=+0.223 (n=2661)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6053 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0164` → IC=+0.275 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0164 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.411` → IC=+0.245 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.411 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3479` → IC=+0.257 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3479 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7276` → IC=+0.228 (n=1145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7276 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.218 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2054.9984` → IC=+0.224 (n=887)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2054.9984 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.220 (n=2172)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.144 (n=147)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=3610)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.163 (n=532)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0036 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.9545` → IC=+0.226 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9545 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.329 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.3359` → IC=+0.328 (n=556)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3359 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.111` → IC=+0.186 (n=1144)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.111 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.335 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.2208` → IC=+0.345 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2208 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2985` → IC=+0.348 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2985 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.4107` → IC=+0.346 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4107 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.2171` → IC=+0.326 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2171 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.337 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0932` → IC=+0.173 (n=941)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.0932 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.323` → IC=+0.141 (n=446)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.323 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` < `0.13` → IC=+0.136 (n=1536)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.13 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8417` → IC=+0.147 (n=1113)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8417 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `1.1679` → IC=+0.134 (n=556)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_regimen` > 1.1679 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.200 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7767` → IC=+0.137 (n=1065)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.7767 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.1545` → IC=+0.150 (n=724)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1545 (IC base=+0.035)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=549)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.191 (n=163)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=489)

- **FILTRO** `ibs_20min` > `0.2174` → IC=-0.132 (n=3536)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2174
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=1746)

- **FILTRO** `sigma_ewma_delta_pct` > `8.662` → IC=-0.239 (n=554)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.662
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4728)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.180 (n=223)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.7857 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `1.0156` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0156 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.4892` → IC=+0.262 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4892 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.383` → IC=+0.140 (n=231)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 2.383 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.0155` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0155 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.276 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.5549` → IC=+0.279 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5549 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5481` → IC=+0.258 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5481 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.2174` → IC=+0.148 (n=1746)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2174 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.276 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4355` → IC=+0.276 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4355 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.6968` → IC=+0.301 (n=319)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6968 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.302 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.298 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6139` → IC=-0.179 (n=963)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6139
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2893)

- **FILTRO** `ibs_20min` < `0.748` → IC=-0.150 (n=2544)

  - _Acción_: SKIP cuando `ibs_20min` < 0.748
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=1312)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.161 (n=956)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2900)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.203 (n=1391)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=4179)

- **PATRÓN** `dist_vwap_pct` > `0.7184` → IC=+0.333 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7184 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2486` → IC=+0.305 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2486 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` < `1.1457` → IC=+0.298 (n=667)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1457 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.314 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.302 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0737` → IC=+0.303 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0737 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.4208` → IC=+0.326 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4208 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.8376` → IC=+0.306 (n=430)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8376 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.8102` → IC=+0.274 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8102 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0687` → IC=+0.283 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0687 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1042` → IC=+0.282 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1042 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1851` → IC=+0.262 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1851 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.262 (n=1399)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.207 (n=5775)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.3224` → IC=+0.168 (n=17294)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3224 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.6765` → IC=+0.295 (n=1651)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6765 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.161 (n=7761)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1691` → IC=+0.263 (n=6371)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1691 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6886` → IC=+0.268 (n=5690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6886 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2396` → IC=+0.275 (n=1895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2396 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4596` → IC=+0.261 (n=3393)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4596 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6405` → IC=+0.270 (n=3390)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6405 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.294 (n=9758)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.160 (n=5555)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0093 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.6592` → IC=+0.144 (n=16650)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6592 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.24` → IC=+0.263 (n=5235)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.24 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7058` → IC=+0.259 (n=2313)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7058 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1948` → IC=+0.265 (n=1752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1948 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.316 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5798` → IC=+0.288 (n=3310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5798 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2684` → IC=+0.282 (n=3411)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2684 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.293 (n=7440)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.371` → IC=-0.180 (n=1567)

  - _Acción_: SKIP cuando `ibs_20min` < 0.371
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=3187)

- **FILTRO** `ibs_20min` > `0.7424` → IC=-0.211 (n=996)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7424
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2994)

- **FILTRO** `sigma_ewma_delta_pct` > `4.413` → IC=-0.205 (n=874)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.413
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=3116)

- **PATRÓN** `ibs_20min` > `0.9167` → IC=+0.308 (n=1191)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9167 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.026` → IC=+0.215 (n=845)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.026 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2292` → IC=+0.300 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2292 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.250 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.2425` → IC=+0.272 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2425 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.278 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.1633` → IC=+0.161 (n=999)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1633 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0733` → IC=+0.417 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0733 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4225` → IC=+0.425 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4225 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.411 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1131` → IC=+0.213 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1131 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1936` → IC=+0.192 (n=1684)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.1936 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6821` → IC=+0.201 (n=1505)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6821 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0748` → IC=+0.190 (n=1551)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0748 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.228 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.425` → IC=+0.219 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.425 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.4876` → IC=+0.190 (n=553)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.4876 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `274.0` → IC=+0.229 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 274.0 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1556` → IC=+0.226 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1556 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.235 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6206 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2731` → IC=+0.286 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2731 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5351` → IC=+0.237 (n=450)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5351 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1657` → IC=+0.247 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1657 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.237 (n=344)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.308 (n=845)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.272 (n=2656)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=1329)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.300 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.279 (n=2197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.272 (n=2440)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.277 (n=2999)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1971.3584` → IC=+0.282 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1971.3584 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.279 (n=1498)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.329 (n=989)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.311 (n=960)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.318 (n=834)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` < `0.3689` → IC=+0.295 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3689 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.2581` → IC=+0.299 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2581 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.584` → IC=+0.311 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.584 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` < `0.1976` → IC=+0.290 (n=2130)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1976 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.3423` → IC=+0.309 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3423 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `1.5758` → IC=+0.297 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5758 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.6774` → IC=+0.301 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6774 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `2051.6413` → IC=+0.308 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.6413 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.292 (n=1386)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.292)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7378` → IC=-0.186 (n=1045)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7378
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=3137)

- **PATRÓN** `ibs_20min` > `0.8799` → IC=+0.173 (n=991)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` > 0.8799 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.234 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3648` → IC=+0.233 (n=1352)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3648 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `1.0074` → IC=+0.245 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0074 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.6703` → IC=+0.231 (n=1234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6703 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1021` → IC=+0.250 (n=434)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1021 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.3994` → IC=+0.248 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3994 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.267 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3309` → IC=+0.231 (n=1049)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3309 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.1965` → IC=+0.230 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1965 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.246 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.101 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2862` → IC=+0.292 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2862 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.7982` → IC=+0.268 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7982 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4427` → IC=+0.250 (n=302)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4427 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.256 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7619` → IC=-0.212 (n=1822)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7619
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=1823)

- **FILTRO** `ibs_20min` > `0.6486` → IC=-0.233 (n=893)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6486
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=2682)

- **FILTRO** `sigma_ewma_delta_pct` > `8.511` → IC=-0.240 (n=414)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.511
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=3161)

- **PATRÓN** `ibs_20min` > `0.7619` → IC=+0.304 (n=1823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7619 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.336 (n=807)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.527` → IC=+0.182 (n=568)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.527 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8453` → IC=+0.333 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8453 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7033` → IC=+0.324 (n=1223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7033 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1583` → IC=+0.323 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1583 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2752` → IC=+0.349 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2752 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.343 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.340 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.5493` → IC=+0.145 (n=2360)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.5493 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.4547` → IC=+0.250 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4547 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.263 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.2238` → IC=+0.241 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2238 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.261 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.251 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.270 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.032)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.345 (n=1731)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.301)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.304 (n=754)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.312 (n=925)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.301)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.335 (n=1938)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.301)

- **PATRÓN** `dist_vwap_pct` > `0.2054` → IC=+0.327 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2054 (IC base=+0.301)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.792` → IC=+0.322 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.792 (IC base=+0.301)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.310 (n=1936)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.301)

- **PATRÓN** `volumen_pendiente_norm` > `0.2797` → IC=+0.343 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2797 (IC base=+0.301)

- **PATRÓN** `volumen_spike_ratio` > `1.425` → IC=+0.312 (n=1854)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.425 (IC base=+0.301)

- **PATRÓN** `libro_liquidez` > `2634.3588` → IC=+0.313 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2634.3588 (IC base=+0.301)

- **PATRÓN** `ballena_activa_n` < `41.0` → IC=+0.335 (n=1658)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 41.0 (IC base=+0.301)

- **PATRÓN** `sigma_h` > `0.0152` → IC=+0.333 (n=1363)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0152 (IC base=+0.302)

- **PATRÓN** `drift_60min` |x|≤ `0.1867` → IC=+0.305 (n=901)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1867 (IC base=+0.302)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.314 (n=793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.302)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.303 (n=1001)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.302)

- **PATRÓN** `ibs_20min` < `0.3676` → IC=+0.327 (n=2045)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3676 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.345` → IC=+0.317 (n=385)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.345 (IC base=+0.302)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.085` → IC=+0.303 (n=2432)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.085 (IC base=+0.302)

- **PATRÓN** `volumen_regimen` < `0.7186` → IC=+0.308 (n=900)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7186 (IC base=+0.302)

- **PATRÓN** `volumen_regimen` > `1.2242` → IC=+0.332 (n=682)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2242 (IC base=+0.302)

- **PATRÓN** `volumen_pendiente_norm` > `0.2838` → IC=+0.351 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2838 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` < `1.4161` → IC=+0.310 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4161 (IC base=+0.302)

- **PATRÓN** `volumen_spike_ratio` > `2.1353` → IC=+0.305 (n=849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1353 (IC base=+0.302)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.225 (n=4255)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.1214` → IC=+0.200 (n=5610)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1214 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=13247)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.5581` → IC=+0.234 (n=12747)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5581 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1637` → IC=+0.208 (n=5148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1637 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.262` → IC=+0.259 (n=2508)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.262 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1861` → IC=+0.169 (n=8456)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 1.1861 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.624` → IC=+0.166 (n=8456)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.624 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.205 (n=1853)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.179 (n=5437)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6076` → IC=+0.191 (n=4118)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.6076 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1982.2507` → IC=+0.182 (n=11386)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1982.2507 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.198 (n=11666)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 95.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.183 (n=10796)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0091 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.227 (n=4091)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=5821)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.236 (n=12282)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.174` → IC=+0.174 (n=8741)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.174 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.035` → IC=+0.197 (n=2005)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.035 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.69` → IC=+0.181 (n=10819)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 2.69 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.162 (n=8758)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1823 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.225 (n=1813)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6367` → IC=+0.187 (n=3839)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` > 2.6367 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.191 (n=11234)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.234 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3319` → IC=+0.230 (n=2132)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3319 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=2234)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.221 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.295 (n=1421)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.983` → IC=+0.331 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.983 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.270 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.213 (n=2015)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=2298)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.250 (n=1668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.249)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.261 (n=755)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.0951` → IC=+0.305 (n=732)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0951 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.255 (n=1511)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=803)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.0158` → IC=+0.294 (n=732)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0158 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.251 (n=1454)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.2973` → IC=+0.286 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2973 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` < `1.4319` → IC=+0.270 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4319 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.6805` → IC=+0.253 (n=524)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6805 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=1869)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `1528.1906` → IC=+0.259 (n=1662)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1528.1906 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.255 (n=594)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.249)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.218 (n=641)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1596` → IC=+0.183 (n=1280)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1596 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=2025)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3409` → IC=+0.224 (n=1919)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3409 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1341` → IC=+0.215 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1341 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.364` → IC=+0.225 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.364 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.164 (n=845)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6895 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.195 (n=306)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4131` → IC=+0.180 (n=627)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4131 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.5038` → IC=+0.161 (n=627)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5038 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `421.0` → IC=+0.159 (n=1840)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 421.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=2016)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.2342` → IC=+0.172 (n=1772)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.2342 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6188` → IC=+0.204 (n=2014)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6188 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.49` → IC=+0.192 (n=381)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.49 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.159 (n=2014)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.204 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.146 (n=1704)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.5032` → IC=+0.152 (n=1894)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.5032 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.146 (n=1893)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4236 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.180 (n=611)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 202.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.238 (n=979)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3996` → IC=+0.225 (n=1900)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3996 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.235 (n=793)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1113)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.441` → IC=+0.299 (n=500)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.441 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.214 (n=1846)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3544` → IC=+0.226 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3544 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.766` → IC=+0.216 (n=920)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.766 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7073` → IC=+0.227 (n=948)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7073 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2573)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1964.0432` → IC=+0.226 (n=979)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1964.0432 (IC base=+0.214)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.246 (n=1628)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.235)

- **PATRÓN** `drift_60min` |x|≤ `0.1428` → IC=+0.273 (n=814)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1428 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.281 (n=704)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.235)

- **PATRÓN** `ibs_20min` < `0.0082` → IC=+0.300 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0082 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.514` → IC=+0.273 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.514 (IC base=+0.235)

- **PATRÓN** `volumen_pendiente_norm` > `0.3557` → IC=+0.278 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3557 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` < `1.7474` → IC=+0.236 (n=777)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7474 (IC base=+0.235)

- **PATRÓN** `volumen_spike_ratio` > `2.1531` → IC=+0.238 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1531 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `2051.2584` → IC=+0.241 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.2584 (IC base=+0.235)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.235 (n=1158)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.235)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.175 (n=2069)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0074 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4062` → IC=+0.168 (n=2069)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4062 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3118` → IC=+0.214 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3118 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1413` → IC=+0.200 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1413 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.752` → IC=+0.200 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.752 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.0223` → IC=+0.159 (n=1821)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0223 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.180 (n=845)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.8174` → IC=+0.150 (n=1353)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.8174 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.167 (n=676)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4612.7985` → IC=+0.187 (n=1379)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 4612.7985 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.160 (n=2005)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 139.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.153 (n=2178)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0072 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3955` → IC=+0.143 (n=2177)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.3955 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1036)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6858` → IC=+0.186 (n=2177)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6858 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.156 (n=2179)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.609` → IC=+0.159 (n=538)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.609 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8557` → IC=+0.155 (n=1452)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8557 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2997` → IC=+0.196 (n=330)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2997 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.81` → IC=+0.135 (n=1359)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.81 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4246` → IC=+0.126 (n=2038)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4246 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7579.1069` → IC=+0.193 (n=987)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7579.1069 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.147 (n=881)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 68.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.177 (n=1054)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0103 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4428` → IC=+0.130 (n=2047)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4428 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.143 (n=2374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.4915` → IC=+0.215 (n=2325)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4915 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1961` → IC=+0.188 (n=1351)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1961 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.599` → IC=+0.277 (n=496)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.599 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.175` → IC=+0.142 (n=2326)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.175 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.136 (n=2361)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4385` → IC=+0.150 (n=752)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4385 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2431)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2794.4942` → IC=+0.205 (n=1054)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2794.4942 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.167 (n=745)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 20.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.139 (n=2376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0108 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.173 (n=794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2422)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.5968` → IC=+0.219 (n=2376)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5968 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.199` → IC=+0.148 (n=2249)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.199 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.46` → IC=+0.131 (n=2097)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 2.46 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.130 (n=2376)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1753 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1654` → IC=+0.124 (n=2299)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1654 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.152 (n=317)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.136 (n=739)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4234` → IC=+0.138 (n=738)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4234 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2655.6964` → IC=+0.191 (n=1077)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2655.6964 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.130 (n=1924)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.246 (n=1917)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1287` → IC=+0.239 (n=715)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1287 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2226)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=1923)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.259 (n=2148)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1837` → IC=+0.227 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1837 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.4782` → IC=+0.224 (n=1924)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4782 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.61` → IC=+0.251 (n=974)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.61 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.1768` → IC=+0.225 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1768 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6184` → IC=+0.231 (n=2144)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6184 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.269 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.4668` → IC=+0.228 (n=2086)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4668 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.8078` → IC=+0.230 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8078 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2615.934` → IC=+0.227 (n=1429)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.934 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.234 (n=731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.240 (n=995)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.0888` → IC=+0.261 (n=731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0888 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1072)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.4267` → IC=+0.256 (n=2191)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4267 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.2956` → IC=+0.234 (n=577)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2956 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.33` → IC=+0.257 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.33 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.641` → IC=+0.235 (n=2191)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.641 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.285 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.230 (n=2037)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4406 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2591.9144` → IC=+0.229 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2591.9144 (IC base=+0.228)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.207 (n=1434)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.190 (n=1083)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0089 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1292` → IC=+0.203 (n=1430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1292 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.216 (n=1616)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.7231` → IC=+0.232 (n=2164)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7231 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.7935` → IC=+0.205 (n=479)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7935 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.637` → IC=+0.211 (n=1402)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.637 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.204 (n=1950)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.6953` → IC=+0.186 (n=2612)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6953 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.193 (n=1166)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4312` → IC=+0.199 (n=1052)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4312 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.1945` → IC=+0.186 (n=1430)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.1945 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=3668)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2693.0919` → IC=+0.189 (n=2900)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2693.0919 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.194 (n=3028)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 150.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.133 (n=1168)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0038 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.3818` → IC=+0.160 (n=2335)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.3818 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.128 (n=1139)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 19.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.203 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.3269` → IC=+0.200 (n=920)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3269 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=841)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.177)

- **PATRÓN** `ibs_20min` > `0.6334` → IC=+0.233 (n=613)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6334 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.3084` → IC=+0.198 (n=273)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3084 (IC base=+0.177)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.069` → IC=+0.196 (n=393)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.069 (IC base=+0.177)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.203 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8725 (IC base=+0.177)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.182 (n=363)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` < `2.2069` → IC=+0.188 (n=792)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.2069 (IC base=+0.177)

- **PATRÓN** `volumen_spike_ratio` > `1.4107` → IC=+0.178 (n=900)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4107 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `14647.5968` → IC=+0.183 (n=613)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 14647.5968 (IC base=+0.177)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.206 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.177)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.184 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0028 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.3402` → IC=+0.136 (n=1090)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.3402 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=990)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6327` → IC=+0.168 (n=959)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` < 0.6327 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.694` → IC=+0.128 (n=216)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 8.694 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `1.0616` → IC=+0.145 (n=494)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0616 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.1613` → IC=+0.166 (n=288)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1613 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.132 (n=947)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.161 (n=706)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 217.0 (IC base=+0.119)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.247 (n=658)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.243 (n=329)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=1036)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.6836` → IC=+0.274 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6836 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.3563` → IC=+0.222 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3563 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.2051` → IC=+0.222 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2051 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.882` → IC=+0.245 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.882 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.8344` → IC=+0.226 (n=658)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8344 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `1.1625` → IC=+0.222 (n=329)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1625 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.1583` → IC=+0.248 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1583 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.249 (n=325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.230 (n=649)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=1104)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.1073` → IC=+0.161 (n=337)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1073 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `6658.8999` → IC=+0.135 (n=672)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 6658.8999 (IC base=+0.059)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.177 (n=363)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0097 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.5352` → IC=+0.165 (n=800)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.5352 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.219 (n=390)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.274 (n=370)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `1.0116` → IC=+0.236 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0116 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.0` → IC=+0.249 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.0 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.0604` → IC=+0.181 (n=704)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.0604 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.7162` → IC=+0.171 (n=715)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.7162 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4478` → IC=+0.179 (n=257)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4478 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.1798` → IC=+0.171 (n=350)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.1798 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.171 (n=825)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3044.5069` → IC=+0.191 (n=267)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3044.5069 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.132 (n=756)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5417 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `2721.3379` → IC=+0.142 (n=389)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2721.3379 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.130 (n=554)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 21.0 (IC base=+0.053)

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

- **PATRÓN** `ibs_20min` > `0.56` → IC=+0.183 (n=197)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` > 0.56 (IC base=+0.152)

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

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.149 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0125 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.135 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 10.0 (IC base=+0.117)

- **PATRÓN** `ibs_20min` < `0.61` → IC=+0.130 (n=252)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` < 0.61 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `1.1964` → IC=+0.318 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.1964 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.225` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.225 (IC base=+0.117)

- **PATRÓN** `volumen_regimen` < `0.8919` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8919 (IC base=+0.117)

- **PATRÓN** `volumen_pendiente_norm` > `0.2383` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2383 (IC base=+0.117)

- **PATRÓN** `volumen_spike_ratio` > `2.3392` → IC=+0.136 (n=108)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.3392 (IC base=+0.117)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.130 (n=233)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 19.0 (IC base=+0.117)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.226 (n=5536)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=17323)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.231 (n=16602)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4483 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.9006` → IC=+0.210 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9006 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.272` → IC=+0.255 (n=4058)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.272 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.2206` → IC=+0.170 (n=11131)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2206 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2904` → IC=+0.206 (n=2204)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2904 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6123` → IC=+0.197 (n=5382)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6123 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1974.0184` → IC=+0.185 (n=14832)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1974.0184 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.204 (n=15243)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.191 (n=13264)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0096 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.3798` → IC=+0.192 (n=13255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3798 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=5610)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.583` → IC=+0.242 (n=15062)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.583 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.1752` → IC=+0.171 (n=9218)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1752 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.838` → IC=+0.204 (n=2090)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.838 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.581` → IC=+0.190 (n=14560)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.581 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.7049` → IC=+0.163 (n=4475)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7049 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.253 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.6156` → IC=+0.197 (n=4745)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6156 (IC base=+0.187)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.216 (n=9365)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.187)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.235 (n=904)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.3479` → IC=+0.226 (n=2710)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3479 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.236 (n=1314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=1066)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.529` → IC=+0.353 (n=633)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.529 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2318` → IC=+0.280 (n=484)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2318 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.220 (n=867)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.2779` → IC=+0.236 (n=1179)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2779 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=2880)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2001.8802` → IC=+0.229 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2001.8802 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.250 (n=1105)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.267 (n=2307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.286 (n=1015)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=2113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5087` → IC=+0.288 (n=2307)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5087 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.173` → IC=+0.265 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.173 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0952` → IC=+0.262 (n=2069)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0952 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.288 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.4431` → IC=+0.265 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4431 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6455` → IC=+0.273 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6455 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2593)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1651.1194` → IC=+0.269 (n=2061)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1651.1194 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.268 (n=1031)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.198 (n=899)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1044` → IC=+0.167 (n=1182)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1044 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2806)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3709` → IC=+0.225 (n=2399)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3709 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1252` → IC=+0.197 (n=1389)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1252 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.568` → IC=+0.164 (n=444)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 11.568 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.167` → IC=+0.154 (n=2465)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.167 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6302` → IC=+0.175 (n=896)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6302 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0724` → IC=+0.154 (n=2394)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0724 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2717` → IC=+0.184 (n=384)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2717 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1861` → IC=+0.161 (n=2310)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1861 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5299` → IC=+0.155 (n=2345)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5299 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `266.0` → IC=+0.186 (n=1137)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 266.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=2239)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.143)

- **PATRÓN** `drift_60min` |x|≤ `0.2565` → IC=+0.163 (n=1967)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.2565 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.169 (n=842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.143)

- **PATRÓN** `ibs_20min` < `0.7006` → IC=+0.198 (n=2236)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7006 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.194` → IC=+0.154 (n=371)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.194 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.443` → IC=+0.144 (n=2251)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.443 (IC base=+0.143)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.154 (n=2236)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1894 (IC base=+0.143)

- **PATRÓN** `volumen_pendiente_norm` > `0.2182` → IC=+0.193 (n=421)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2182 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` < `2.434` → IC=+0.149 (n=2131)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_spike_ratio` < 2.434 (IC base=+0.143)

- **PATRÓN** `volumen_spike_ratio` > `1.7755` → IC=+0.155 (n=1420)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.7755 (IC base=+0.143)

- **PATRÓN** `ballena_activa_n` < `275.0` → IC=+0.159 (n=900)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 275.0 (IC base=+0.143)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.261 (n=923)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2892)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1025)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.309` → IC=+0.322 (n=588)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.309 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.1319` → IC=+0.230 (n=2583)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1319 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `3.1891` → IC=+0.240 (n=894)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1891 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3291)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1833.5188` → IC=+0.235 (n=1842)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1833.5188 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.245 (n=2279)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1818` → IC=+0.258 (n=1139)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1818 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0303` → IC=+0.307 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0303 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.961` → IC=+0.293 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.961 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3454` → IC=+0.299 (n=382)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3454 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1351` → IC=+0.250 (n=1640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1351 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.242 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2051.2032` → IC=+0.255 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.2032 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.256 (n=1073)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.197 (n=1259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4209` → IC=+0.158 (n=2855)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4209 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2968)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2479` → IC=+0.194 (n=2856)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2479 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.172 (n=1511)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1412 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.136` → IC=+0.160 (n=1158)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.136 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8651` → IC=+0.166 (n=1905)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8651 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.192 (n=371)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5231` → IC=+0.163 (n=1226)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5231 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1656` → IC=+0.157 (n=1263)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1656 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6295.0353` → IC=+0.244 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6295.0353 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.175 (n=1215)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 74.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.149 (n=2379)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0075 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4405` → IC=+0.139 (n=2377)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4405 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.154 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.7373` → IC=+0.183 (n=2376)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.7373 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1476` → IC=+0.144 (n=2163)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1476 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.113` → IC=+0.171 (n=363)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.113 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8687` → IC=+0.138 (n=1584)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8687 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2971` → IC=+0.222 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2971 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.2242` → IC=+0.130 (n=2011)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.2242 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4309` → IC=+0.135 (n=2283)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4309 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7243.2915` → IC=+0.213 (n=792)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7243.2915 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.130 (n=776)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 67.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.155 (n=1303)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0103 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=1059)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.199 (n=2874)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4444 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.0671` → IC=+0.207 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0671 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.748` → IC=+0.265 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.748 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2208` → IC=+0.136 (n=2874)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2208 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.126 (n=2989)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.135 (n=371)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8314` → IC=+0.128 (n=1873)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8314 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4627` → IC=+0.126 (n=2807)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4627 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=1965)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2496.5462` → IC=+0.230 (n=1303)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2496.5462 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.146 (n=897)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 24.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.152 (n=2410)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.156 (n=914)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=2823)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6458` → IC=+0.212 (n=2735)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6458 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2146` → IC=+0.136 (n=2358)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2146 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.259` → IC=+0.135 (n=2634)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.259 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.7104` → IC=+0.141 (n=1204)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7104 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.174 (n=468)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4404` → IC=+0.155 (n=853)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.4404 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2673.3847` → IC=+0.209 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2673.3847 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.134 (n=2246)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 47.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.250 (n=2430)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=2840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.235 (n=1962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `0.61` → IC=+0.272 (n=2431)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.61 (IC base=+0.230)

- **PATRÓN** `dist_vwap_pct` > `0.1902` → IC=+0.246 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1902 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.270 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` < `1.2287` → IC=+0.238 (n=2718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2287 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` > `0.6398` → IC=+0.233 (n=2718)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6398 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.253 (n=342)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.5041` → IC=+0.250 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5041 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3530)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `2620.2181` → IC=+0.236 (n=1812)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2620.2181 (IC base=+0.230)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.251 (n=941)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.236 (n=2659)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.264 (n=2823)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.196` → IC=+0.266 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.196 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.258 (n=941)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.299 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.232 (n=2620)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.229)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.193 (n=4910)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.246 (n=1681)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.504` → IC=+0.219 (n=5043)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.504 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=1835)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9401` → IC=+0.248 (n=1682)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9401 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.1709` → IC=+0.208 (n=1861)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1709 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.9444` → IC=+0.211 (n=4228)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9444 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.018` → IC=+0.215 (n=824)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.018 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.615` → IC=+0.210 (n=4490)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.615 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.221 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.1063` → IC=+0.209 (n=4709)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1063 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1666` → IC=+0.222 (n=1417)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1666 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.455` → IC=+0.215 (n=1655)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.455 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.8457` → IC=+0.210 (n=3310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8457 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=3879)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2928.3292` → IC=+0.216 (n=4505)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2928.3292 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.239 (n=1234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.4893` → IC=+0.208 (n=3694)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4893 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.207 (n=1643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.7312` → IC=+0.199 (n=3694)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7312 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.675` → IC=+0.199 (n=622)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.675 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.4216` → IC=+0.191 (n=3733)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.4216 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.843` → IC=+0.203 (n=3312)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.843 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `1.0969` → IC=+0.202 (n=3081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0969 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.0975` → IC=+0.196 (n=3388)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0975 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.194 (n=746)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.197 (n=1603)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.1885` → IC=+0.201 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1885 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=4910)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.203 (n=2416)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.192)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.273 (n=672)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.259)

- **PATRÓN** `drift_60min` |x|≤ `0.0854` → IC=+0.294 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0854 (IC base=+0.259)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.265 (n=765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.259)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.260 (n=765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.259)

- **PATRÓN** `ibs_20min` < `0.489` → IC=+0.279 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.489 (IC base=+0.259)

- **PATRÓN** `dist_vwap_pct` < `0.3378` → IC=+0.274 (n=769)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3378 (IC base=+0.259)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.585` → IC=+0.272 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.585 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` < `1.2183` → IC=+0.267 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2183 (IC base=+0.259)

- **PATRÓN** `volumen_regimen` > `0.868` → IC=+0.273 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.868 (IC base=+0.259)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.350 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.259)

- **PATRÓN** `volumen_spike_ratio` < `1.8249` → IC=+0.266 (n=507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8249 (IC base=+0.259)

- **PATRÓN** `libro_liquidez` > `16333.2471` → IC=+0.277 (n=254)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16333.2471 (IC base=+0.259)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.253 (n=582)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0034 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.369` → IC=+0.194 (n=1320)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.369 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=481)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.178)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.201 (n=480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` < `0.1382` → IC=+0.207 (n=581)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1382 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.6078` → IC=+0.180 (n=599)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.6078 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.7048` → IC=+0.186 (n=116)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.7048 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.385` → IC=+0.197 (n=1302)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 6.385 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `1.2212` → IC=+0.193 (n=1320)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.2212 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.2183` → IC=+0.200 (n=265)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2183 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `1.4018` → IC=+0.196 (n=438)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.4018 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `2.1651` → IC=+0.190 (n=595)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.1651 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `14901.4739` → IC=+0.191 (n=599)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 14901.4739 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `692.0` → IC=+0.190 (n=1274)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 692.0 (IC base=+0.178)

### GBM_LATE_5M#DOGE#5min
- **PATRÓN** `sigma_h` < `0.007` → IC=+0.198 (n=342)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.007 (IC base=+0.191)

- **PATRÓN** `sigma_h` > `0.0104` → IC=+0.220 (n=352)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0104 (IC base=+0.191)

- **PATRÓN** `drift_60min` |x|≤ `0.5854` → IC=+0.202 (n=777)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5854 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.245 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `ibs_20min` < `0.7037` → IC=+0.195 (n=519)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` < 0.7037 (IC base=+0.191)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.239 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.191)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.488` → IC=+0.229 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.488 (IC base=+0.191)

- **PATRÓN** `volumen_pendiente_norm` > `0.2102` → IC=+0.244 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2102 (IC base=+0.191)

- **PATRÓN** `volumen_spike_ratio` > `2.2501` → IC=+0.201 (n=517)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2501 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `2469.0708` → IC=+0.223 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2469.0708 (IC base=+0.191)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.193 (n=558)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 11.0 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.229 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.011 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.250 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.01 (IC base=+0.227)

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
- **PATRÓN** `sigma_h` < `0.008` → IC=+0.213 (n=1376)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.008 (IC base=+0.197)

- **PATRÓN** `drift_60min` |x|≤ `0.4596` → IC=+0.205 (n=1376)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4596 (IC base=+0.197)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.215 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `ibs_20min` < `0.519` → IC=+0.209 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.519 (IC base=+0.197)

- **PATRÓN** `ibs_20min` > `0.8776` → IC=+0.199 (n=459)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.8776 (IC base=+0.197)

- **PATRÓN** `dist_vwap_pct` < `0.4062` → IC=+0.211 (n=1374)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4062 (IC base=+0.197)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.114` → IC=+0.205 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.114 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` < `0.8782` → IC=+0.200 (n=918)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8782 (IC base=+0.197)

- **PATRÓN** `volumen_regimen` > `1.2314` → IC=+0.203 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2314 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` < `0.1047` → IC=+0.200 (n=1264)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1047 (IC base=+0.197)

- **PATRÓN** `volumen_pendiente_norm` > `0.1638` → IC=+0.197 (n=410)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.1638 (IC base=+0.197)

- **PATRÓN** `volumen_spike_ratio` < `2.4554` → IC=+0.205 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4554 (IC base=+0.197)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=1412)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.197)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.245 (n=375)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.187)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.210 (n=1124)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.202 (n=438)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.198 (n=752)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.187)

- **PATRÓN** `ibs_20min` < `0.3986` → IC=+0.196 (n=750)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.3986 (IC base=+0.187)

- **PATRÓN** `ibs_20min` > `0.0867` → IC=+0.190 (n=1124)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.0867 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` > `0.6705` → IC=+0.199 (n=197)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6705 (IC base=+0.187)

- **PATRÓN** `dist_vwap_pct` < `0.2251` → IC=+0.189 (n=1087)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2251 (IC base=+0.187)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.36` → IC=+0.195 (n=1021)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 4.36 (IC base=+0.187)

- **PATRÓN** `volumen_regimen` < `0.6394` → IC=+0.224 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6394 (IC base=+0.187)

- **PATRÓN** `volumen_pendiente_norm` > `0.0742` → IC=+0.207 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0742 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` < `2.1925` → IC=+0.197 (n=968)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 2.1925 (IC base=+0.187)

- **PATRÓN** `volumen_spike_ratio` > `2.5255` → IC=+0.191 (n=367)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5255 (IC base=+0.187)

- **PATRÓN** `libro_liquidez` > `6781.2899` → IC=+0.195 (n=1124)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6781.2899 (IC base=+0.187)

### GBM_LATE_5M#SOL#5min
- **PATRÓN** `sigma_h` < `0.0107` → IC=+0.202 (n=646)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0107 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `3.0` → IC=+0.202 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 3.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.925` → IC=+0.246 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.925 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.743` → IC=+0.238 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.743 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.204` → IC=+0.212 (n=182)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.204 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `0.6978` → IC=+0.229 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6978 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` < `0.1062` → IC=+0.191 (n=662)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` < 0.1062 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.079` → IC=+0.191 (n=328)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` > 0.079 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.5672` → IC=+0.196 (n=314)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5672 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.4918` → IC=+0.204 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4918 (IC base=+0.181)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.186 (n=855)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.02 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `3085.5096` → IC=+0.201 (n=656)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3085.5096 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.198 (n=717)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 52.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.206 (n=355)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0091 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.209 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0125 (IC base=+0.201)

- **PATRÓN** `drift_60min` |x|≤ `0.6144` → IC=+0.223 (n=532)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6144 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.238 (n=361)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.201)

- **PATRÓN** `ibs_20min` < `0.7249` → IC=+0.225 (n=532)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.7249 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.5172` → IC=+0.222 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5172 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` < `1.2157` → IC=+0.205 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 1.2157 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.868` → IC=+0.211 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.868 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` < `1.3392` → IC=+0.206 (n=533)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.3392 (IC base=+0.201)

- **PATRÓN** `volumen_regimen` > `0.9368` → IC=+0.211 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.9368 (IC base=+0.201)

- **PATRÓN** `volumen_pendiente_norm` < `0.1071` → IC=+0.224 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1071 (IC base=+0.201)

- **PATRÓN** `volumen_spike_ratio` > `2.2044` → IC=+0.243 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2044 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `2981.8939` → IC=+0.221 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2981.8939 (IC base=+0.201)

- **PATRÓN** `ballena_activa_n` < `46.0` → IC=+0.232 (n=521)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 46.0 (IC base=+0.201)

### GBM_LATE_60M
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.156 (n=727)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.004 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.3889` → IC=+0.145 (n=1561)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 0.3889 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.3636` → IC=+0.157 (n=540)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3636 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.999` → IC=+0.163 (n=455)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 8.999 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2764` → IC=+0.147 (n=216)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` > 0.2764 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.237 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.374` → IC=+0.174 (n=133)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 10.374 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.172 (n=233)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=+0.059)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.5136` → IC=-0.120 (n=227)

  - _Acción_: SKIP cuando `ibs_20min` < 0.5136
  - _Potencial_: sin este filtro IC_bueno=+0.190 (n=463)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.133 (n=549)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0056 (IC base=+0.087)

- **PATRÓN** `ibs_20min` > `0.5136` → IC=+0.190 (n=463)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.5136 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.1227` → IC=+0.155 (n=259)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.1227 (IC base=+0.087)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.126 (n=271)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0037 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.0544` → IC=+0.287 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0544 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.074)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7058` → IC=-0.181 (n=89)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7058
  - _Potencial_: sin este filtro IC_bueno=+0.123 (n=271)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.132 (n=474)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0059 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.6175` → IC=+0.208 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6175 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.198 (n=263)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.204` → IC=+0.254 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.204 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.8141` → IC=+0.128 (n=339)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_regimen` < 0.8141 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` > `0.2854` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2854 (IC base=+0.094)

- **PATRÓN** `ibs_20min` < `0.0314` → IC=+0.306 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0314 (IC base=+0.019)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.019)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.167 (n=358)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.75 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` > `0.475` → IC=+0.124 (n=187)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.475 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.362` → IC=+0.170 (n=113)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 9.362 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.2296` → IC=+0.131 (n=101)

  - _Acción_: Kelly boost +0.66€ cuando `volumen_pendiente_norm` > 0.2296 (IC base=+0.032)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.155 (n=233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0103 (IC base=+0.080)

- **PATRÓN** `ibs_20min` < `0.1379` → IC=+0.226 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1379 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.1772` → IC=+0.155 (n=192)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1772 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.715` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.715 (IC base=+0.080)

- **PATRÓN** `volumen_regimen` > `1.0779` → IC=+0.229 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0779 (IC base=+0.080)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` < `2.1557` → IC=+0.156 (n=158)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 2.1557 (IC base=+0.080)

- **PATRÓN** `volumen_spike_ratio` > `1.4056` → IC=+0.170 (n=180)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4056 (IC base=+0.080)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.161 (n=175)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.06 (IC base=+0.080)

### GBM_LATE_60M_FADE
- **FILTRO** `hora_utc` > `8.0` → IC=-0.333 (n=64)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=241)

- **FILTRO** `dist_vwap_pct` > `0.2321` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2321
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=288)

- **FILTRO** `libro_liquidez` < `887.0104` → IC=-0.218 (n=76)

  - _Acción_: SKIP cuando `libro_liquidez` < 887.0104
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=229)

- **FILTRO** `drift_60min` |x|> `0.1933` → IC=-0.315 (n=63)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1933
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=190)

- **FILTRO** `ibs_20min` > `0.5495` → IC=-0.332 (n=129)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5495
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=130)

- **FILTRO** `dist_vwap_pct` > `0.4497` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4497
  - _Potencial_: sin este filtro IC_bueno=-0.273 (n=240)

- **FILTRO** `volumen_pendiente_norm` > `0.0465` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0465
  - _Potencial_: sin este filtro IC_bueno=-0.267 (n=144)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

- **FILTRO** `ibs_20min` > `0.3071` → IC=-0.240 (n=48)

  - _Acción_: SKIP cuando `ibs_20min` > 0.3071
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=49)

- **FILTRO** `volumen_regimen` < `0.8402` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8402
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `sigma_h` > `0.0042` → IC=-0.300 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=86)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=86)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `drift_60min` |x|> `0.149` → IC=-0.315 (n=25)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.149
  - _Potencial_: sin este filtro IC_bueno=-0.103 (n=76)

- **FILTRO** `hora_utc` < `5.0` → IC=-0.160 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=53)

- **FILTRO** `sigma_h` > `0.0048` → IC=-0.346 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.266 (n=75)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.260 (n=77)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.279 (n=84)

- **FILTRO** `libro_liquidez` < `1541.8747` → IC=-0.304 (n=49)

  - _Acción_: SKIP cuando `libro_liquidez` < 1541.8747
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=50)

- **PATRÓN** `ibs_20min` > `0.941` → IC=+0.149 (n=35)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` > 0.941 (IC base=-0.160)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.395 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=90)

- **FILTRO** `sigma_h` < `0.006` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=31)

- **FILTRO** `hora_utc` > `11.0` → IC=-0.441 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.227 (n=31)

- **FILTRO** `dist_vwap_pct` < `0.2328` → IC=-0.352 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2328
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=21)

- **FILTRO** `sigma_ewma_delta_pct` > `3.164` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.164
  - _Potencial_: sin este filtro IC_bueno=-0.293 (n=27)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.1613` → IC=-0.126 (n=276)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1613
  - _Potencial_: sin este filtro IC_bueno=+0.154 (n=536)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.188 (n=235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.006 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.175 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.6818` → IC=+0.150 (n=518)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.6818 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.741` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.741 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6249` → IC=+0.169 (n=173)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_regimen` < 0.6249 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` < `0.2267` → IC=+0.144 (n=465)

  - _Acción_: Kelly boost +0.72€ cuando `volumen_pendiente_norm` < 0.2267 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.155 (n=279)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.1613` → IC=+0.154 (n=536)

  - _Acción_: Kelly boost +0.77€ cuando `ibs_20min` < 0.1613 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.085` → IC=+0.185 (n=182)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 9.085 (IC base=+0.059)

- **PATRÓN** `volumen_pendiente_norm` > `0.2222` → IC=+0.124 (n=123)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.2222 (IC base=+0.059)

- **PATRÓN** `libro_liquidez` > `3239.2397` → IC=+0.137 (n=406)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 3239.2397 (IC base=+0.059)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **FILTRO** `ibs_20min` < `0.6889` → IC=-0.209 (n=53)

  - _Acción_: SKIP cuando `ibs_20min` < 0.6889
  - _Potencial_: sin este filtro IC_bueno=+0.047 (n=159)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.201 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.155 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 12.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.148 (n=106)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.138)

- **PATRÓN** `ibs_20min` < `0.1761` → IC=+0.198 (n=283)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.1761 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.216` → IC=+0.169 (n=122)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 7.216 (IC base=+0.138)

- **PATRÓN** `volumen_regimen` > `1.0304` → IC=+0.185 (n=128)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` > 1.0304 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` < `0.0706` → IC=+0.152 (n=219)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` < 0.0706 (IC base=+0.138)

- **PATRÓN** `volumen_pendiente_norm` > `0.2723` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2723 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` < `2.5184` → IC=+0.172 (n=251)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_spike_ratio` < 2.5184 (IC base=+0.138)

- **PATRÓN** `volumen_spike_ratio` > `1.4429` → IC=+0.152 (n=251)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` > 1.4429 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4588.7853` → IC=+0.150 (n=252)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 4588.7853 (IC base=+0.138)

### GBM_LATE_60M_PYCONFIRMADO#ETH#60min
- **FILTRO** `volumen_pendiente_norm` > `0.1263` → IC=-0.149 (n=35)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.1263
  - _Potencial_: sin este filtro IC_bueno=+0.140 (n=170)

- **FILTRO** `ibs_20min` > `0.1892` → IC=-0.137 (n=100)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1892
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=197)

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.140 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0039 (IC base=+0.094)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.191 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 18.0 (IC base=+0.094)

- **PATRÓN** `ibs_20min` > `0.8015` → IC=+0.136 (n=163)

  - _Acción_: Kelly boost +0.68€ cuando `ibs_20min` > 0.8015 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` < `0.0943` → IC=+0.135 (n=154)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.0943 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.217` → IC=+0.126 (n=188)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 9.217 (IC base=+0.094)

- **PATRÓN** `volumen_regimen` < `0.6229` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 0.6229 (IC base=+0.094)

- **PATRÓN** `volumen_pendiente_norm` < `0.1263` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_pendiente_norm` < 0.1263 (IC base=+0.094)

- **PATRÓN** `volumen_spike_ratio` < `1.7943` → IC=+0.167 (n=103)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_spike_ratio` < 1.7943 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.957` → IC=+0.232 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.028)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4` → IC=-0.278 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=105)

- **FILTRO** `volumen_spike_ratio` > `2.1066` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.1066
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=68)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.310 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.248)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.272 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6522 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.386 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` < `0.2335` → IC=+0.255 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2335 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.248)

- **PATRÓN** `volumen_regimen` < `0.5821` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5821 (IC base=+0.248)

- **PATRÓN** `volumen_pendiente_norm` > `0.1057` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1057 (IC base=+0.248)

- **PATRÓN** `volumen_spike_ratio` < `1.4907` → IC=+0.395 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4907 (IC base=+0.248)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.248 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.089)

### LATE_WINDOW_5MIN
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.331 (n=69)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.315)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.387 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.315)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.315)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.371 (n=60)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `1107.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1107.0 (IC base=+0.315)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3366` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3366 (IC base=+0.239)

- **PATRÓN** `elapsed_s` > `226.1` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 226.1 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.304 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.331 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.239)

### LATE_WINDOW_5MIN#BTC#5min
- **FILTRO** `es_ntm_5min` < `1.0` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `es_ntm_5min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.331 (n=69)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3349` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3349 (IC base=+0.315)

- **PATRÓN** `elapsed_s` > `184.3` → IC=+0.387 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 184.3 (IC base=+0.315)

- **PATRÓN** `drift_15min` |x|≤ `1.0295` → IC=+0.455 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.0295 (IC base=+0.315)

- **PATRÓN** `drift_60min` |x|≤ `0.969` → IC=+0.371 (n=60)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.969 (IC base=+0.315)

- **PATRÓN** `ballena_activa_n` < `1107.0` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1107.0 (IC base=+0.315)

- **PATRÓN** `drift_ventana_pct` |x|> `0.3366` → IC=+0.261 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `drift_ventana_pct` |x|> 0.3366 (IC base=+0.239)

- **PATRÓN** `elapsed_s` > `226.1` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 226.1 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `1.4538` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 1.4538 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.6421` → IC=+0.304 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6421 (IC base=+0.239)

- **PATRÓN** `es_ntm_5min` > `1.0` → IC=+0.331 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `es_ntm_5min` > 1.0 (IC base=+0.239)

- **PATRÓN** `ballena_activa_n` < `1854.0` → IC=+0.291 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 1854.0 (IC base=+0.239)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `libro_liquidez` > `2848.3664` → IC=+0.131 (n=564)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2848.3664 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2848.3664` → IC=+0.131 (n=564)

  - _Acción_: Kelly boost +0.65€ cuando `libro_liquidez` > 2848.3664 (IC base=+0.101)

### LIQUIDACIONES_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=191)

- **FILTRO** `libro_liquidez` < `2842.6585` → IC=-0.198 (n=51)

  - _Acción_: SKIP cuando `libro_liquidez` < 2842.6585
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=156)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=298)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `libro_liquidez` < `10724.0239` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `libro_liquidez` < 10724.0239
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=69)

- **FILTRO** `liq_n` < `5.0` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `liq_n` < 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=31)

### LIQUIDACIONES_15M#ETH#15min
- **FILTRO** `ballena_activa_n` > `66.0` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ballena_activa_n` > 66.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

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
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=3495)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=104)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.160 (n=104)

### LIQUIDACIONES_5M#BNB#5min
- **FILTRO** `hora_utc` > `14.0` → IC=-0.146 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=129)

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
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=1281)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=62)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=1235)

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
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=715)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=415)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=396)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.142 (n=174)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.495 (IC base=+0.022)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=839)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.122 (n=80)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=839)

- **FILTRO** `py_entrada` < `0.44` → IC=-0.132 (n=259)

  - _Acción_: SKIP cuando `py_entrada` < 0.44
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=660)

- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=807)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=807)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=226)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=250)

### LIQUIDACIONES_60M#ETH#60min
- **FILTRO** `py_entrada` < `0.445` → IC=-0.135 (n=50)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=254)

### LIQUIDACIONES_60M#SOL#60min
- **FILTRO** `liq_imbalance` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=349)

- **FILTRO** `liq_imbalance_15min` |x|≤ `1.0` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `liq_imbalance_15min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=349)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.120 (n=185)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=194)

- **FILTRO** `libro_liquidez` < `625.8426` → IC=-0.138 (n=125)

  - _Acción_: SKIP cuando `libro_liquidez` < 625.8426
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=254)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=256)

- **FILTRO** `hora_utc` > `15.0` → IC=-0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.027 (n=184)

### LIQUIDACIONES_DEPTH_FASE0
- **FILTRO** `py_entrada` < `0.4` → IC=-0.121 (n=1361)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3544)

### LIQUIDACIONES_DEPTH_FASE0#BNB#15min
- **FILTRO** `py_entrada` > `0.57` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.081 (n=29)

### LIQUIDACIONES_DEPTH_FASE0#BNB#5min
- **FILTRO** `py_entrada` < `0.47` → IC=-0.145 (n=60)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=34)

- **FILTRO** `hora_utc` < `13.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 13.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

### LIQUIDACIONES_DEPTH_FASE0#BTC#5min
- **PATRÓN** `py_entrada` < `0.46` → IC=+0.176 (n=143)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.46 (IC base=+0.012)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=249)

### LIQUIDACIONES_DEPTH_FASE0#DOGE#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.142 (n=149)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.052 (n=170)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.5 (IC base=+0.058)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.126 (n=343)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=120)

- **FILTRO** `profundidad_ratio` < `56.1` → IC=-0.162 (n=152)

  - _Acción_: SKIP cuando `profundidad_ratio` < 56.1
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=311)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.142 (n=191)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=216)

### LIQUIDACIONES_DEPTH_FASE0#ETH#5min
- **FILTRO** `profundidad_ratio` < `21.2` → IC=-0.139 (n=142)

  - _Acción_: SKIP cuando `profundidad_ratio` < 21.2
  - _Potencial_: sin este filtro IC_bueno=+0.046 (n=289)

### LIQUIDACIONES_DEPTH_FASE0#SOL#15min
- **FILTRO** `py_entrada` < `0.39` → IC=-0.171 (n=83)

  - _Acción_: SKIP cuando `py_entrada` < 0.39
  - _Potencial_: sin este filtro IC_bueno=-0.003 (n=356)

### LIQUIDACIONES_DEPTH_FASE0#XRP#5min
- **FILTRO** `py_entrada` < `0.43` → IC=-0.122 (n=281)

  - _Acción_: SKIP cuando `py_entrada` < 0.43
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=303)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.165 (n=5929)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=18415)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.175 (n=6028)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=18976)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.195 (n=1087)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=3335)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.174 (n=1034)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3437)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.145 (n=1164)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `1317.92` → IC=+0.137 (n=2211)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1317.92 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.128 (n=2089)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.012)

- **PATRÓN** `libro_liquidez` > `1504.5254` → IC=+0.153 (n=1521)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1504.5254 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.159 (n=822)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=2745)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=874)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2673)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.174 (n=1082)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=3354)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.201 (n=1065)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=3500)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.131 (n=1512)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1817.9984` → IC=+0.125 (n=1509)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1817.9984 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.158 (n=1079)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.084 (n=3352)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2367)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=758)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2305)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2793)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3533)

### MOMENTUM_IBS_15M_FADE#BTC#15min
- **FILTRO** `hora_utc` > `20.0` → IC=-0.146 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.094 (n=436)

- **FILTRO** `py_entrada` < `0.445` → IC=-0.264 (n=138)

  - _Acción_: SKIP cuando `py_entrada` < 0.445
  - _Potencial_: sin este filtro IC_bueno=-0.053 (n=423)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.234 (n=287)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=872)

### MOMENTUM_IBS_15M_FADE#ETH#15min
- **FILTRO** `py_entrada` < `0.395` → IC=-0.230 (n=72)

  - _Acción_: SKIP cuando `py_entrada` < 0.395
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=262)

- **FILTRO** `libro_liquidez` < `3613.7014` → IC=-0.152 (n=110)

  - _Acción_: SKIP cuando `libro_liquidez` < 3613.7014
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=224)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.190 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=297)

- **FILTRO** `ibs_20min` > `0.9803` → IC=-0.194 (n=109)

  - _Acción_: SKIP cuando `ibs_20min` > 0.9803
  - _Potencial_: sin este filtro IC_bueno=-0.104 (n=331)

- **FILTRO** `libro_liquidez` < `3728.8927` → IC=-0.167 (n=220)

  - _Acción_: SKIP cuando `libro_liquidez` < 3728.8927
  - _Potencial_: sin este filtro IC_bueno=-0.086 (n=220)

### MOMENTUM_IBS_15M_FADE#SOL#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=914)

- **FILTRO** `libro_liquidez` < `1760.3335` → IC=-0.164 (n=233)

  - _Acción_: SKIP cuando `libro_liquidez` < 1760.3335
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=700)

- **FILTRO** `libro_liquidez` < `2083.7972` → IC=-0.169 (n=348)

  - _Acción_: SKIP cuando `libro_liquidez` < 2083.7972
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=707)

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

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.037)

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
- **FILTRO** `hora_utc` < `8.0` → IC=-0.128 (n=16720)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=37497)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13318)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=40899)

- **FILTRO** `ibs_7min` < `0.2381` → IC=-0.230 (n=13535)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=40682)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=18098)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=36119)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.241 (n=16727)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=51510)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.182 (n=16893)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=51344)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6761)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=4674)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4783)

- **FILTRO** `ibs_7min` < `0.7123` → IC=-0.243 (n=3120)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7123
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6337)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.178 (n=2019)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7438)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.270 (n=2933)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=8899)

- **FILTRO** `ibs_7min` > `0.7714` → IC=-0.210 (n=2956)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7714
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=8876)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=2133)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7019)

- **FILTRO** `ibs_7min` < `0.7268` → IC=-0.200 (n=2287)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7268
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6865)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.192 (n=2275)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6877)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2294)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7002)

- **FILTRO** `ibs_7min` > `0.2682` → IC=-0.196 (n=2323)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2682
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6973)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.183 (n=2312)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6984)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=2200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6793)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=2211)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6782)

- **FILTRO** `ibs_7min` < `0.2969` → IC=-0.246 (n=2965)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2969
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6028)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2144)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6849)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.256 (n=2935)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9659)

- **FILTRO** `ibs_7min` > `0.7342` → IC=-0.178 (n=3148)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7342
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=9446)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2068)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6767)

- **FILTRO** `ibs_7min` < `0.7296` → IC=-0.187 (n=2208)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7296
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6627)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.189 (n=2190)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6645)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=2057)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7100)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.181 (n=2288)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6869)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.175 (n=2256)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6901)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=2125)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6773)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.233 (n=2214)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=6684)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.220 (n=2144)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6754)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.190 (n=3151)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=9880)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.292 (n=2090)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=6792)

- **FILTRO** `ibs_7min` < `0.2029` → IC=-0.222 (n=2219)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2029
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6663)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.202 (n=1987)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=6895)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.216 (n=3010)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9317)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `drift_7min_pct` |x|> `0.1046` → IC=-0.135 (n=61)

  - _Acción_: SKIP cuando `drift_7min_pct` |x|> 0.1046
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=120)

### MOMENTUM_IBS_5M_FADE#BTC#5min
- **FILTRO** `py_entrada` < `0.455` → IC=-0.158 (n=299)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=984)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=1268)

- **FILTRO** `hora_utc` < `8.0` → IC=-0.121 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=495)

- **FILTRO** `py_entrada` > `0.545` → IC=-0.152 (n=156)

  - _Acción_: SKIP cuando `py_entrada` > 0.545
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=548)

### MOMENTUM_IBS_5M_FADE#ETH#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.129 (n=33)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=1458)

- **FILTRO** `py_entrada` > `0.565` → IC=-0.172 (n=260)

  - _Acción_: SKIP cuando `py_entrada` > 0.565
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=849)

### MOMENTUM_IBS_5M_FADE#SOL#5min
- **FILTRO** `py_entrada` < `0.475` → IC=-0.122 (n=162)

  - _Acción_: SKIP cuando `py_entrada` < 0.475
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=330)

- **FILTRO** `ballena_activa_n` > `3.0` → IC=-0.143 (n=166)

  - _Acción_: SKIP cuando `ballena_activa_n` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.008 (n=325)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.231 (n=50)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=442)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.134 (n=69)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=631)

### MOMENTUM_IBS_5M_FADE#XRP#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=387)

### ORDER_FLOW_5M
- **PATRÓN** `delta_ratio` |x|> `0.3981` → IC=+0.139 (n=1153)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio` |x|> 0.3981 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.131 (n=545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 14.0 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.133 (n=431)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.129)

- **PATRÓN** `total_vol_5m` < `126584.0` → IC=+0.142 (n=1014)

  - _Acción_: Kelly boost +0.71€ cuando `total_vol_5m` < 126584.0 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `3650.3048` → IC=+0.147 (n=522)

  - _Acción_: Kelly boost +0.73€ cuando `libro_liquidez` > 3650.3048 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.148 (n=373)

  - _Acción_: Kelly boost +0.74€ cuando `ballena_activa_n` < 11.0 (IC base=+0.129)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `delta_ratio` |x|> `0.4374` → IC=+0.152 (n=90)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio` |x|> 0.4374 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.204 (n=130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.139)

- **PATRÓN** `total_vol_5m` < `292.267` → IC=+0.148 (n=180)

  - _Acción_: Kelly boost +0.74€ cuando `total_vol_5m` < 292.267 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `2576.9482` → IC=+0.206 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2576.9482 (IC base=+0.139)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.167 (n=97)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 7.0 (IC base=+0.139)

### ORDER_FLOW_5M#DOGE#5min
- **PATRÓN** `delta_ratio` |x|> `0.3992` → IC=+0.129 (n=235)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio` |x|> 0.3992 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.127 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 14.0 (IC base=+0.113)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.122 (n=281)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.113)

- **PATRÓN** `libro_liquidez` > `2323.3188` → IC=+0.135 (n=157)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2323.3188 (IC base=+0.113)

### ORDER_FLOW_5M#ETH#5min
- **PATRÓN** `delta_ratio` |x|> `0.416` → IC=+0.173 (n=154)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.87€ cuando `delta_ratio` |x|> 0.416 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.153 (n=240)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 4.0 (IC base=+0.136)

- **PATRÓN** `total_vol_5m` < `384.339` → IC=+0.211 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 384.339 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `7711.1521` → IC=+0.141 (n=154)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 7711.1521 (IC base=+0.136)

- **PATRÓN** `ballena_activa_n` < `69.0` → IC=+0.189 (n=101)

  - _Acción_: Kelly boost +0.95€ cuando `ballena_activa_n` < 69.0 (IC base=+0.136)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `delta_ratio` |x|> `0.4324` → IC=+0.247 (n=93)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio` |x|> 0.4324 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.191 (n=150)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 12.0 (IC base=+0.153)

- **PATRÓN** `total_vol_5m` < `4950.202` → IC=+0.183 (n=137)

  - _Acción_: Kelly boost +0.92€ cuando `total_vol_5m` < 4950.202 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `3257.229` → IC=+0.165 (n=183)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 3257.229 (IC base=+0.153)

- **PATRÓN** `ballena_activa_n` < `27.0` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `ballena_activa_n` < 27.0 (IC base=+0.153)

### ORDER_FLOW_5M#XRP#5min
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.122 (n=194)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 14.0 (IC base=+0.098)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=130)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.098)

- **PATRÓN** `libro_liquidez` > `3584.1484` → IC=+0.157 (n=97)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3584.1484 (IC base=+0.098)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.9794` → IC=-0.266 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.9794
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=139)

- **FILTRO** `T_h` > `129.5932` → IC=-0.189 (n=162)

  - _Acción_: SKIP cuando `T_h` > 129.5932
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=487)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.185 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0034 (IC base=-0.078)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `T_h` > `87.9952` → IC=-0.260 (n=48)

  - _Acción_: SKIP cuando `T_h` > 87.9952
  - _Potencial_: sin este filtro IC_bueno=+0.051 (n=145)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.304 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=-0.028)

### PRICE_TARGET_GBM#ETH#reach
- **FILTRO** `pct_vs_K` |x|> `9.8932` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 9.8932
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=49)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.013` → IC=-0.267 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=85)

- **FILTRO** `T_h` < `87.7913` → IC=-0.190 (n=56)

  - _Acción_: SKIP cuando `T_h` < 87.7913
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=57)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.242 (n=29)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=-0.091)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0103` → IC=-0.221 (n=456)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0103
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=152)

- **FILTRO** `T_h` > `70.3333` → IC=-0.202 (n=455)

  - _Acción_: SKIP cuando `T_h` > 70.3333
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=153)

- **FILTRO** `sigma_h` > `0.0084` → IC=-0.251 (n=175)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.215 (n=342)

- **FILTRO** `sigma_h` < `0.0049` → IC=-0.248 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0049
  - _Potencial_: sin este filtro IC_bueno=-0.221 (n=388)

- **FILTRO** `T_h` > `54.8663` → IC=-0.266 (n=387)

  - _Acción_: SKIP cuando `T_h` > 54.8663
  - _Potencial_: sin este filtro IC_bueno=-0.114 (n=130)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` < `0.0044` → IC=-0.206 (n=49)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0044
  - _Potencial_: sin este filtro IC_bueno=-0.142 (n=149)

- **FILTRO** `T_h` > `71.1632` → IC=-0.184 (n=131)

  - _Acción_: SKIP cuando `T_h` > 71.1632
  - _Potencial_: sin este filtro IC_bueno=-0.109 (n=67)

- **FILTRO** `T_h` > `144.2373` → IC=-0.287 (n=45)

  - _Acción_: SKIP cuando `T_h` > 144.2373
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=138)

- **FILTRO** `pct_vs_K` |x|> `2.9891` → IC=-0.436 (n=45)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.9891
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=138)

### PRICE_TARGET_GBM_FADE#BTC#reach
- **FILTRO** `sigma_h` > `0.0042` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

- **FILTRO** `T_h` < `139.5329` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `T_h` < 139.5329
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `sigma_h` < `0.0078` → IC=-0.262 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0078
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `sigma_h` < `0.0097` → IC=-0.304 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0097
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=45)

- **FILTRO** `T_h` > `74.6449` → IC=-0.267 (n=131)

  - _Acción_: SKIP cuando `T_h` > 74.6449
  - _Potencial_: sin este filtro IC_bueno=-0.223 (n=45)

- **FILTRO** `sigma_h` > `0.0089` → IC=-0.357 (n=40)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0089
  - _Potencial_: sin este filtro IC_bueno=-0.118 (n=121)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.214 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=121)

- **FILTRO** `T_h` > `57.7851` → IC=-0.271 (n=107)

  - _Acción_: SKIP cuando `T_h` > 57.7851
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=54)

### PRICE_TARGET_GBM_FADE#ETH#reach
- **FILTRO** `T_h` < `145.7969` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `T_h` < 145.7969
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `sigma_h` < `0.0098` → IC=-0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0098
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

### PRICE_TARGET_GBM_FADE#SOL#atexpiry
- **FILTRO** `sigma_h` < `0.0079` → IC=-0.267 (n=41)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0079
  - _Potencial_: sin este filtro IC_bueno=-0.117 (n=126)

- **FILTRO** `T_h` > `95.5744` → IC=-0.234 (n=111)

  - _Acción_: SKIP cuando `T_h` > 95.5744
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=56)

- **FILTRO** `sigma_h` > `0.0153` → IC=-0.367 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0153
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=86)

- **FILTRO** `sigma_h` < `0.0085` → IC=-0.269 (n=37)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0085
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=77)

- **FILTRO** `T_h` > `46.7258` → IC=-0.308 (n=76)

  - _Acción_: SKIP cuando `T_h` > 46.7258
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=38)

### RESOLUTION_SNIPER
- **PATRÓN** `edge` > `0.1224` → IC=+0.477 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1224 (IC base=+0.338)

- **PATRÓN** `sigma_h` < `0.0135` → IC=+0.354 (n=94)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0135 (IC base=+0.338)

- **PATRÓN** `sigma_h` > `0.0099` → IC=+0.377 (n=63)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0099 (IC base=+0.338)

- **PATRÓN** `T_h` > `0.7719` → IC=+0.391 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.7719 (IC base=+0.338)

- **PATRÓN** `dist_50` > `0.47` → IC=+0.478 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.338)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.352 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.338)

- **PATRÓN** `edge` > `0.099` → IC=+0.442 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.099 (IC base=+0.416)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.435 (n=198)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.416)

- **PATRÓN** `T_h` < `0.5922` → IC=+0.434 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 0.5922 (IC base=+0.416)

- **PATRÓN** `T_h` > `1.484` → IC=+0.422 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 1.484 (IC base=+0.416)

- **PATRÓN** `dist_50` > `0.3772` → IC=+0.455 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.3772 (IC base=+0.416)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.478 (n=136)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.416)

### RESOLUTION_SNIPER#BTC#sniper
- **PATRÓN** `dist_50` > `0.47` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.47 (IC base=+0.180)

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
- **PATRÓN** `edge` > `0.1885` → IC=+0.483 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1885 (IC base=+0.438)

- **PATRÓN** `sigma_h` < `0.016` → IC=+0.467 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.016 (IC base=+0.438)

- **PATRÓN** `T_h` > `0.4307` → IC=+0.449 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.4307 (IC base=+0.438)

- **PATRÓN** `dist_50` > `0.354` → IC=+0.466 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.354 (IC base=+0.438)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.438)

- **PATRÓN** `edge` > `0.1961` → IC=+0.479 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `edge` > 0.1961 (IC base=+0.465)

- **PATRÓN** `sigma_h` < `0.0155` → IC=+0.479 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0155 (IC base=+0.465)

- **PATRÓN** `T_h` > `0.8576` → IC=+0.468 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 0.8576 (IC base=+0.465)

- **PATRÓN** `dist_50` > `0.4659` → IC=+0.492 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `dist_50` > 0.4659 (IC base=+0.465)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.472 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.465)

### STREAK_FADE_15M
- **FILTRO** `streak_len` > `5.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=302)

- **FILTRO** `py_entrada` < `0.495` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=381)

- **PATRÓN** `streak_estiramiento` < `0.8382` → IC=+0.120 (n=256)

  - _Acción_: Kelly boost +0.60€ cuando `streak_estiramiento` < 0.8382 (IC base=+0.044)

- **PATRÓN** `libro_liquidez` > `2756.3002` → IC=+0.150 (n=101)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2756.3002 (IC base=+0.044)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.120 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 5.0 (IC base=+0.087)

- **PATRÓN** `streak_estiramiento` < `0.4496` → IC=+0.187 (n=97)

  - _Acción_: Kelly boost +0.93€ cuando `streak_estiramiento` < 0.4496 (IC base=+0.087)

- **PATRÓN** `ballena_activa_n` < `35.0` → IC=+0.151 (n=107)

  - _Acción_: Kelly boost +0.76€ cuando `ballena_activa_n` < 35.0 (IC base=+0.087)

- **PATRÓN** `libro_liquidez` > `2414.7926` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 2414.7926 (IC base=+0.087)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.019 (n=102)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.5` → IC=-0.157 (n=33)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=71)

- **FILTRO** `libro_liquidez` < `3678.6572` → IC=-0.214 (n=26)

  - _Acción_: SKIP cuando `libro_liquidez` < 3678.6572
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=78)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=46)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

### STREAK_FADE_5M#XRP#5min
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

- **FILTRO** `streak_estiramiento` > `1.1496` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `streak_estiramiento` > 1.1496
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=41)

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
- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.035)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=989)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1330)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1133)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=1181)

### STRUCT_NO_15M
- **FILTRO** `hora_utc` < `15.0` → IC=-0.250 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=22)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3978)

### STRUCT_NO_15M#ETH#15min
- **FILTRO** `hora_utc` < `15.0` → IC=-0.250 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `py_entrada` < `0.455` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.455
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=22)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2187)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.199 (n=1181)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.197 (n=1181)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0119 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1746` → IC=+0.195 (n=3118)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1746 (IC base=+0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1339` → IC=+0.188 (n=1411)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1339 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.187 (n=3288)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=3255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_15` > `0.56` → IC=+0.255 (n=3542)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.56 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.128` → IC=+0.169 (n=1686)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` > 0.128 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.4927` → IC=+0.167 (n=3169)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.4927 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.518` → IC=+0.254 (n=924)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.518 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `4692.4102` → IC=+0.197 (n=1181)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 4692.4102 (IC base=+0.179)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=1406)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.244 (n=404)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0038 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.266 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.219)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2541` → IC=+0.250 (n=202)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2541 (IC base=+0.219)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2303` → IC=+0.231 (n=351)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2303 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=606)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `ibs_15` > `0.7184` → IC=+0.286 (n=606)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7184 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.2399` → IC=+0.243 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2399 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.108` → IC=+0.302 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.108 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.221 (n=785)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `8997.0825` → IC=+0.229 (n=606)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8997.0825 (IC base=+0.219)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.188 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0667` → IC=+0.156 (n=309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0667 (IC base=+0.146)

- **PATRÓN** `drift_15min` |x|≤ `0.3955` → IC=+0.150 (n=235)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.3955 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.145` → IC=+0.153 (n=468)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.77€ cuando `delta_ratio_macro` |x|> 0.145 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1315` → IC=+0.160 (n=277)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1315 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.155 (n=645)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 6.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5467` → IC=+0.244 (n=702)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5467 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.159 (n=435)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.835` → IC=+0.269 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.835 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3210.7419` → IC=+0.155 (n=702)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3210.7419 (IC base=+0.146)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.763` → IC=-0.175 (n=38)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.763
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=327)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1727` → IC=+0.137 (n=521)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.1727 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.8947` → IC=+0.250 (n=262)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8947 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.134 (n=432)

  - _Acción_: Kelly boost +0.67€ cuando `libro_spread` < 0.01 (IC base=+0.095)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.524` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 8.524 (IC base=+0.009)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.0238` → IC=+0.246 (n=270)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0238 (IC base=+0.203)

- **PATRÓN** `drift_60min` |x|≤ `0.0862` → IC=+0.238 (n=357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0862 (IC base=+0.203)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3374` → IC=+0.233 (n=713)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3374 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.217 (n=718)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 14.0 (IC base=+0.203)

- **PATRÓN** `ibs_15` > `0.5417` → IC=+0.280 (n=811)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5417 (IC base=+0.203)

- **PATRÓN** `dist_vwap_pct` > `0.1903` → IC=+0.212 (n=408)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1903 (IC base=+0.203)

- **PATRÓN** `sigma_ewma_delta_pct` > `17.081` → IC=+0.226 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 17.081 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `2966.2693` → IC=+0.301 (n=270)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2966.2693 (IC base=+0.203)

- **PATRÓN** `ibs_15` < `0.1111` → IC=+0.157 (n=773)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.1111 (IC base=+0.066)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.391 (n=209)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0703` → IC=+0.375 (n=624)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0703 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.387 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.379 (n=628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.401 (n=625)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.393 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.454` → IC=+0.385 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.454 (IC base=+0.366)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=761)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `3851.736` → IC=+0.375 (n=559)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3851.736 (IC base=+0.366)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.368 (n=286)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.366)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.400 (n=108)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.366)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.365 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.366)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2147` → IC=+0.393 (n=147)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2147 (IC base=+0.366)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1371` → IC=+0.399 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1371 (IC base=+0.366)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.387 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.366)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.393 (n=324)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.366)

- **PATRÓN** `dist_vwap_pct` > `0.2456` → IC=+0.397 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2456 (IC base=+0.366)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.742` → IC=+0.378 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.742 (IC base=+0.366)

- **PATRÓN** `libro_liquidez` > `15403.697` → IC=+0.393 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15403.697 (IC base=+0.366)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.414 (n=243)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.366)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.367 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.363)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.385 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.363)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0901` → IC=+0.378 (n=269)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0901 (IC base=+0.363)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.380 (n=240)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.363)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.390 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.363)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.363)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.411 (n=301)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.380 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.363)

- **PATRÓN** `dist_vwap_pct` < `0.2918` → IC=+0.365 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2918 (IC base=+0.363)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.861` → IC=+0.390 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.861 (IC base=+0.363)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=338)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.363)

- **PATRÓN** `libro_liquidez` > `3954.5881` → IC=+0.392 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3954.5881 (IC base=+0.363)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.366 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=+0.363)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.172 (n=2143)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2145)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.211 (n=1671)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2617)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1402` → IC=+0.187 (n=691)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.1402 (IC base=-0.067)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.282 (n=1037)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1113` → IC=+0.209 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1113 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.266` → IC=+0.198 (n=882)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.266 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2302` → IC=+0.267 (n=1184)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2302 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.361` → IC=+0.282 (n=3552)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.361 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6631` → IC=+0.281 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6631 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.217 (n=624)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=1874)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.228 (n=624)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1874)

- **FILTRO** `sigma_ewma_delta_pct` > `23.271` → IC=-0.265 (n=360)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.271
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=2138)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=65)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.195 (n=2433)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.169 (n=249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0028 (IC base=+0.097)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2081` → IC=+0.292 (n=152)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2081 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.275 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.135 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.7566` → IC=+0.334 (n=336)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7566 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1047` → IC=+0.292 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1047 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.58` → IC=+0.130 (n=376)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.58 (IC base=+0.097)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0659` → IC=+0.205 (n=59)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0659 (IC base=-0.195)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.159` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.159 (IC base=-0.195)

- **PATRÓN** `ibs_15` < `0.618` → IC=+0.287 (n=59)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.618 (IC base=-0.195)

- **PATRÓN** `dist_vwap_pct` < `0.0474` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0474 (IC base=-0.195)

- **PATRÓN** `ballena_activa_n` < `291.0` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 291.0 (IC base=-0.195)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.160 (n=674)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.163 (n=458)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.161 (n=346)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0048 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.0704` → IC=+0.193 (n=229)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0704 (IC base=+0.152)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3021` → IC=+0.192 (n=397)

  - _Acción_: Kelly boost +0.96€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3021 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.152 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.152)

- **PATRÓN** `ibs_15` > `0.6098` → IC=+0.251 (n=519)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6098 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.167 (n=133)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` < `0.1598` → IC=+0.154 (n=408)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1598 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.422` → IC=+0.245 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.422 (IC base=+0.152)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=674)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.152)

- **PATRÓN** `libro_liquidez` > `9906.9054` → IC=+0.163 (n=173)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 9906.9054 (IC base=+0.152)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=1274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.7686` → IC=+0.259 (n=1122)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7686 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1581` → IC=+0.258 (n=849)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1581 (IC base=+0.245)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2771` → IC=+0.245 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2771 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.248 (n=912)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.247 (n=1135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.275 (n=1273)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.6087` → IC=+0.274 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6087 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.498` → IC=+0.257 (n=565)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.498 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.256 (n=334)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=654)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.282 (n=246)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=742)

- **FILTRO** `sigma_ewma_delta_pct` > `6.572` → IC=-0.204 (n=231)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.572
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=757)

- **FILTRO** `sigma_ewma_delta_pct` > `17.972` → IC=-0.147 (n=516)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.972
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4114)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.082` → IC=+0.237 (n=504)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.082 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3556` → IC=+0.290 (n=564)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3556 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.4496` → IC=+0.243 (n=593)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4496 (IC base=-0.040)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` > `0.0197` → IC=-0.250 (n=590)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0197
  - _Potencial_: sin este filtro IC_bueno=-0.162 (n=592)

- **FILTRO** `sigma_ewma_delta_pct` > `7.426` → IC=-0.212 (n=370)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.426
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=812)

- **FILTRO** `libro_spread` > `0.04` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.04
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=1163)

- **PATRÓN** `delta_ratio_macro` |x|> `0.132` → IC=+0.196 (n=21)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.98€ cuando `delta_ratio_macro` |x|> 0.132 (IC base=-0.206)

- **PATRÓN** `ibs_15` > `0.5856` → IC=+0.326 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5856 (IC base=-0.206)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0685` → IC=+0.272 (n=762)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0685 (IC base=-0.026)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1155` → IC=+0.296 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1155 (IC base=-0.026)

- **PATRÓN** `ibs_15` < `0.3333` → IC=+0.292 (n=856)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3333 (IC base=-0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7759` → IC=+0.350 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7759 (IC base=-0.026)

### UPDOWN_GBM_ETH_15M_HORA7
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.074)

### UPDOWN_GBM_ETH_15M_HORA7#ETH#15min
- **PATRÓN** `ibs_15` > `0.8434` → IC=+0.333 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8434 (IC base=+0.074)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.299 (n=934)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.321 (n=355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2427` → IC=+0.309 (n=354)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2427 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2248` → IC=+0.309 (n=631)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2248 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=1108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8388` → IC=+0.321 (n=1062)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8388 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2686` → IC=+0.327 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2686 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.378 (n=235)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12348.3168` → IC=+0.312 (n=482)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12348.3168 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.314 (n=251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.290)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.297 (n=259)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.290)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.314 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.290)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2603` → IC=+0.318 (n=190)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2603 (IC base=+0.290)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.308 (n=571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.290)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.316 (n=570)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.290)

- **PATRÓN** `dist_vwap_pct` > `0.2546` → IC=+0.330 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2546 (IC base=+0.290)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.589` → IC=+0.383 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.589 (IC base=+0.290)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.328 (n=190)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.290)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.306 (n=492)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.294)

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.319 (n=164)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.294)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.298 (n=492)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.294)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.221` → IC=+0.317 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.221 (IC base=+0.294)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=506)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.294)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.294)

- **PATRÓN** `ibs_15` > `0.8503` → IC=+0.324 (n=492)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8503 (IC base=+0.294)

- **PATRÓN** `dist_vwap_pct` > `0.2815` → IC=+0.328 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2815 (IC base=+0.294)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.363 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.294)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.151 (n=84)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.098 (n=252)

- **FILTRO** `ballena_activa_n` > `47.0` → IC=-0.136 (n=226)

  - _Acción_: SKIP cuando `ballena_activa_n` > 47.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=78)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.214 (n=117)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.076 (n=361)

- **FILTRO** `sigma_h` > `0.007` → IC=-0.186 (n=119)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.007
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=359)

- **FILTRO** `drift_15min` |x|> `0.4407` → IC=-0.152 (n=162)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4407
  - _Potencial_: sin este filtro IC_bueno=-0.088 (n=316)

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
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=149)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.2412` → IC=-0.128 (n=92)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.2412
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=94)

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
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1254` → IC=-0.200 (n=18)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1254
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=37)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.3147` → IC=-0.385 (n=24)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.3147
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.0623` → IC=-0.286 (n=26)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.0623
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `sigma_h` < `0.0051` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=37)

- **FILTRO** `divergencia_cvd_spot_perp` |x|> `0.138` → IC=-0.227 (n=20)

  - _Acción_: SKIP cuando `divergencia_cvd_spot_perp` |x|> 0.138
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `86.3225` → IC=+0.185 (n=480)

  - _Acción_: Kelly boost +0.92€ cuando `T_h` > 86.3225 (IC base=+0.185)

- **PATRÓN** `ratio` < `0.973` → IC=+0.406 (n=284)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.973 (IC base=+0.185)

- **PATRÓN** `T_h` > `113.2461` → IC=+0.353 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 113.2461 (IC base=+0.336)

- **PATRÓN** `ratio` > `1.0229` → IC=+0.374 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0229 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `109.3643` → IC=+0.170 (n=198)

  - _Acción_: Kelly boost +0.85€ cuando `T_h` > 109.3643 (IC base=+0.153)

- **PATRÓN** `ratio` < `0.983` → IC=+0.327 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.983 (IC base=+0.153)

- **PATRÓN** `T_h` > `111.8714` → IC=+0.304 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.8714 (IC base=+0.292)

- **PATRÓN** `ratio` > `1.0455` → IC=+0.403 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0455 (IC base=+0.292)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `83.3501` → IC=+0.228 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 83.3501 (IC base=+0.226)

- **PATRÓN** `ratio` < `0.9854` → IC=+0.397 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` < 0.9854 (IC base=+0.226)

- **PATRÓN** `T_h` > `111.9838` → IC=+0.353 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.325)

- **PATRÓN** `ratio` > `1.0347` → IC=+0.395 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `ratio` > 1.0347 (IC base=+0.325)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `146.1003` → IC=+0.445 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1003 (IC base=+0.399)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.56 sube el IC de +0.179 a +0.255 en UPDOWN_GBM#15min (n=3542). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7184 sube el IC de +0.219 a +0.286 en UPDOWN_GBM#BTC#15min (n=606). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5467 sube el IC de +0.146 a +0.244 en UPDOWN_GBM#ETH#15min (n=702). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8947 sube el IC de +0.095 a +0.250 en UPDOWN_GBM#SOL#15min (n=262). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.203 a +0.280 en UPDOWN_GBM#XRP#15min (n=811). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.157 en UPDOWN_GBM#XRP#15min (n=773). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.067 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=1037). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.361 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3552). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7566 sube el IC de +0.097 a +0.334 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=336). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.195 a +0.287 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6098 sube el IC de +0.152 a +0.251 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=519). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.245 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1273). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.190 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3556 sube el IC de -0.040 a +0.290 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=564). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.206 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=856). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.074 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.074 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8388 sube el IC de +0.292 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=1062). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.290 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=570). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8503 sube el IC de +0.294 a +0.324 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=492). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.366 a +0.401 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=625). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.366 a +0.393 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=324). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.363 a +0.411 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=301). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1922 | +0.091 | +216.12€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1922 | +0.091 | +216.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1532 | +0.095 | +187.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1532 | +0.095 | +187.18€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 282 | +0.070 | +11.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 282 | +0.070 | +11.51€ | 4 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 627 | -0.004 | +68.95€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 627 | -0.004 | +68.95€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 456 | -0.028 | +38.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 456 | -0.028 | +38.11€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 133 | +0.070 | +23.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 133 | +0.070 | +23.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 35 | +0.013 | +3.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 35 | +0.013 | +3.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 39872 | -0.084 | -5025.88€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2181 | +0.031 | -250.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 37691 | -0.090 | -4775.07€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4480 | -0.116 | -773.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4480 | -0.116 | -773.00€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2181 | +0.031 | -250.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2181 | +0.031 | -250.81€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4314 | -0.105 | -874.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4314 | -0.105 | -874.01€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10620 | -0.024 | -992.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10620 | -0.024 | -992.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10503 | -0.106 | -815.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10503 | -0.106 | -815.08€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7774 | -0.136 | -1320.78€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7774 | -0.136 | -1320.78€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 34670 | -0.015 | +3385.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8969 | +0.005 | +1687.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 25701 | -0.023 | +1697.94€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 34670 | -0.015 | +3385.72€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8969 | +0.005 | +1687.77€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 25701 | -0.023 | +1697.94€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 144018 | +0.115 | -5764.18€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18534 | +0.183 | -542.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 634 | -0.019 | -69.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 116211 | +0.106 | -4828.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8639 | +0.101 | -323.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19274 | +0.108 | -1180.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19198 | +0.109 | -1180.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 27916 | +0.129 | -379.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5185 | +0.189 | -165.90€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19260 | +0.121 | -92.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3429 | +0.083 | -99.29€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19325 | +0.099 | -1345.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 72 | -0.122 | -6.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19238 | +0.101 | -1327.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 30627 | +0.125 | -551.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7938 | +0.178 | -132.79€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 19512 | +0.107 | -351.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3165 | +0.100 | -57.80€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 27582 | +0.115 | -1381.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5211 | +0.195 | -255.19€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 537 | +0.014 | -15.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 19789 | +0.095 | -943.94€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2045 | +0.132 | -166.73€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19294 | +0.105 | -926.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 67 | -0.080 | +6.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19214 | +0.106 | -932.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23164 | +0.197 | -1388.98€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23164 | +0.197 | -1388.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5272 | +0.179 | -448.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5272 | +0.179 | -448.48€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2928 | +0.203 | -62.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2928 | +0.203 | -62.88€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5215 | +0.181 | -412.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5215 | +0.181 | -412.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4526 | +0.248 | -147.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4526 | +0.248 | -147.31€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5144 | +0.188 | -331.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5144 | +0.188 | -331.93€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 1009 | +0.428 | -32.16€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 1009 | +0.428 | -32.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 396 | +0.437 | -4.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 396 | +0.437 | -4.81€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#DOGE#15min | 5 | +0.089 | +0.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 396 | +0.432 | -8.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 396 | +0.432 | -8.23€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 203 | +0.402 | -15.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 203 | +0.402 | -15.25€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#XRP#15min | 5 | +0.018 | -2.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 80964 | +0.201 | -5782.72€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 80964 | +0.201 | -5782.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 13910 | +0.185 | -1438.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 13910 | +0.185 | -1438.52€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13079 | +0.224 | -452.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13079 | +0.224 | -452.18€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 13866 | +0.181 | -1452.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 13866 | +0.181 | -1452.12€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13150 | +0.221 | -484.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13150 | +0.221 | -484.04€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13428 | +0.202 | -877.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13428 | +0.202 | -877.31€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13531 | +0.197 | -1078.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13531 | +0.197 | -1078.56€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 30963 | +0.117 | +219.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 30963 | +0.117 | +219.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15390 | +0.120 | +182.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15390 | +0.120 | +182.89€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15573 | +0.114 | +36.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15573 | +0.114 | +36.77€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2064 | +0.292 | -11.27€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2064 | +0.292 | -11.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 945 | +0.278 | -28.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 945 | +0.278 | -28.61€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1000 | +0.296 | +12.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1000 | +0.296 | +12.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 953 | +0.441 | +3.88€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 953 | +0.441 | +3.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 463 | +0.435 | -4.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 463 | +0.435 | -4.68€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 444 | +0.448 | +8.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 444 | +0.448 | +8.01€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1631 | +0.072 | -62.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 629 | +0.051 | -51.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1002 | +0.085 | -10.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 73 | +0.113 | +3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 73 | +0.113 | +3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1254 | +0.080 | -22.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 252 | +0.063 | -12.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1002 | +0.085 | -10.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 304 | +0.026 | -43.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 304 | +0.026 | -43.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 61112 | +0.100 | -1549.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4940 | +0.090 | +45.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 56172 | +0.101 | -1594.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 33630 | +0.105 | -375.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4940 | +0.090 | +45.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 28690 | +0.108 | -421.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12539 | +0.109 | -61.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12539 | +0.109 | -61.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 14943 | +0.082 | -1111.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 14943 | +0.082 | -1111.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 895 | +0.192 | -111.46€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 895 | +0.192 | -111.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 895 | +0.192 | -111.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 895 | +0.192 | -111.46€ | 2 | 4 |
| ✅ GBM_LATE_15M | 42052 | +0.094 | +21949.60€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 42052 | +0.094 | +21949.60€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7009 | +0.216 | +5763.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7009 | +0.216 | +5763.96€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6292 | +0.180 | +4805.43€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6292 | +0.180 | +4805.43€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 7515 | +0.205 | +5848.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7515 | +0.205 | +5848.71€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 5876 | +0.041 | +1641.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5876 | +0.041 | +1641.48€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 5934 | -0.032 | +1249.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5934 | -0.032 | +1249.67€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 9426 | -0.030 | +2640.36€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9426 | -0.030 | +2640.36€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 45256 | +0.086 | +24610.47€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 45256 | +0.086 | +24610.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8744 | +0.004 | +4417.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8744 | +0.004 | +4417.45€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9567 | +0.010 | +2263.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9567 | +0.010 | +2263.74€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6277 | +0.278 | +6730.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6277 | +0.278 | +6730.20€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8141 | +0.013 | +2012.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8141 | +0.013 | +2012.13€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7220 | +0.039 | +2976.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7220 | +0.039 | +2976.97€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5307 | +0.302 | +6209.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5307 | +0.302 | +6209.98€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 33349 | +0.180 | +26995.93€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 33349 | +0.180 | +26995.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5058 | +0.230 | +4494.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5058 | +0.230 | +4494.70€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5242 | +0.149 | +3878.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5242 | +0.149 | +3878.58€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5343 | +0.224 | +4599.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5343 | +0.224 | +4599.66€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5660 | +0.138 | +4296.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5660 | +0.138 | +4296.79€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6267 | +0.124 | +4676.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6267 | +0.124 | +4676.35€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5779 | +0.225 | +5049.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5779 | +0.225 | +5049.84€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 8996 | +0.133 | +4388.47€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 8996 | +0.133 | +4388.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2678 | +0.146 | +1541.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2678 | +0.146 | +1541.72€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2659 | +0.137 | +1258.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2659 | +0.137 | +1258.01€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2210 | +0.107 | +844.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2210 | +0.107 | +844.81€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 626 | +0.134 | +283.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 626 | +0.134 | +283.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 42218 | +0.185 | +33782.08€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 42218 | +0.185 | +33782.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6687 | +0.242 | +6236.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6687 | +0.242 | +6236.80€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6560 | +0.148 | +4495.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6560 | +0.148 | +4495.62€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7135 | +0.233 | +6379.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7135 | +0.233 | +6379.37€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6973 | +0.138 | +4971.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6973 | +0.138 | +4971.58€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7477 | +0.121 | +5175.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7477 | +0.121 | +5175.41€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7386 | +0.230 | +6523.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7386 | +0.230 | +6523.30€ | 0 | 19 |
| ✅ GBM_LATE_5M | 11648 | +0.202 | +9030.58€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 11648 | +0.202 | +9030.58€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2775 | +0.208 | +2383.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2775 | +0.208 | +2383.94€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1110 | +0.193 | +808.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1110 | +0.193 | +808.37€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3332 | +0.193 | +2335.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3332 | +0.193 | +2335.78€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 1686 | +0.190 | +1266.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1686 | +0.190 | +1266.01€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1761 | +0.201 | +1320.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1761 | +0.201 | +1320.37€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3436 | +0.066 | +1129.96€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3436 | +0.066 | +1129.96€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1267 | +0.082 | +465.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1267 | +0.082 | +465.25€ | 1 | 6 |
| ✅ GBM_LATE_60M#ETH | 1107 | +0.068 | +389.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1107 | +0.068 | +389.28€ | 1 | 9 |
| ✅ GBM_LATE_60M#SOL | 1062 | +0.046 | +275.44€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1062 | +0.046 | +275.44€ | 0 | 13 |
| 🚫 GBM_LATE_60M_FADE | 564 | -0.246 | -25.26€ | 7 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 564 | -0.246 | -25.26€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 211 | -0.246 | -14.55€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 211 | -0.246 | -14.55€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 200 | -0.228 | -2.99€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 200 | -0.228 | -2.99€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 153 | -0.261 | -7.72€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 153 | -0.261 | -7.72€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1502 | +0.084 | +388.79€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1502 | +0.084 | +388.79€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 588 | +0.081 | +144.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 588 | +0.081 | +144.52€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 539 | +0.058 | +82.99€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 539 | +0.058 | +82.99€ | 2 | 9 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 375 | +0.123 | +161.28€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 375 | +0.123 | +161.28€ | 2 | 10 |
| ✅ LATE_WINDOW_5MIN | 165 | +0.278 | +162.71€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 165 | +0.278 | +162.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 165 | +0.278 | +162.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 165 | +0.278 | +162.71€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3374 | +0.100 | +829.80€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3374 | +0.100 | +829.80€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3374 | +0.100 | +829.80€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3374 | +0.100 | +829.80€ | 0 | 1 |
| ✅ LIQUIDACIONES_15M | 526 | -0.047 | -21.58€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 526 | -0.047 | -21.58€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 146 | -0.020 | +1.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 146 | -0.020 | +1.33€ | 3 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#DOGE#15min | 24 | -0.192 | -5.34€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 101 | -0.044 | -4.54€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 101 | -0.044 | -4.54€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 198 | -0.010 | -1.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 198 | -0.010 | -1.50€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 52 | -0.167 | -9.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 52 | -0.167 | -9.92€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 3705 | +0.016 | +82.95€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3705 | +0.016 | +82.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB | 181 | +0.019 | -2.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BNB#5min | 181 | +0.019 | -2.82€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 785 | +0.011 | +32.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 785 | +0.011 | +32.02€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 207 | -0.012 | -4.18€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 1331 | +0.025 | +30.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 1331 | +0.025 | +30.61€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#SOL | 756 | +0.012 | +1.99€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#SOL#5min | 756 | +0.012 | +1.99€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 445 | +0.015 | +25.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 445 | +0.015 | +25.33€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1741 | -0.040 | -27.56€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1741 | -0.040 | -27.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 501 | -0.029 | -10.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 501 | -0.029 | -10.57€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 590 | -0.015 | +5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 590 | -0.015 | +5.75€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 650 | -0.071 | -22.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 650 | -0.071 | -22.74€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8605 | -0.028 | -10.11€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4085 | -0.037 | -87.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4520 | -0.020 | +77.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 260 | -0.042 | -10.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 133 | -0.026 | -1.52€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 127 | -0.058 | -9.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2141 | -0.019 | +15.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1022 | -0.024 | -4.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1119 | -0.015 | +19.78€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 949 | -0.025 | +11.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 476 | -0.042 | -12.45€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 473 | -0.007 | +24.19€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1870 | -0.043 | -67.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 870 | -0.055 | -60.02€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1000 | -0.033 | -7.90€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1686 | -0.020 | +27.50€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 801 | -0.033 | -7.54€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 885 | -0.009 | +35.04€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1699 | -0.029 | +14.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 783 | -0.035 | -0.93€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 916 | -0.023 | +15.23€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 49348 | -0.001 | +2440.63€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 49348 | -0.001 | +2440.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8893 | +0.026 | +1124.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8893 | +0.026 | +1124.65€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7114 | -0.034 | -106.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7114 | -0.034 | -106.40€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9001 | +0.024 | +934.03€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9001 | +0.024 | +934.03€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6960 | -0.047 | -148.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6960 | -0.047 | -148.76€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8342 | -0.005 | +235.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8342 | -0.005 | +235.25€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9038 | +0.015 | +401.85€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9038 | +0.015 | +401.85€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6618 | -0.060 | -164.35€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6618 | -0.060 | -164.35€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1720 | -0.080 | -46.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1720 | -0.080 | -46.86€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 54 | -0.054 | -2.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 54 | -0.054 | -2.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 774 | -0.120 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 774 | -0.120 | -33.46€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1988 | -0.075 | -40.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1988 | -0.075 | -40.83€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 857 | -0.016 | -25.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 857 | -0.016 | -25.51€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 122454 | -0.076 | +1614.88€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 122454 | -0.076 | +1614.88€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 21289 | -0.077 | +1092.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 21289 | -0.077 | +1092.95€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18448 | -0.100 | -984.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18448 | -0.100 | -984.77€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 21587 | -0.067 | +1141.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 21587 | -0.067 | +1141.91€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 17992 | -0.097 | -625.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 17992 | -0.097 | -625.58€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 21929 | -0.056 | +316.64€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 21929 | -0.056 | +316.64€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21209 | -0.066 | +673.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21209 | -0.066 | +673.73€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 8758 | -0.034 | -183.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 8758 | -0.034 | -183.08€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 1001 | -0.017 | -18.91€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 1001 | -0.017 | -18.91€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 1987 | -0.046 | -24.71€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 1987 | -0.046 | -24.71€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 1008 | -0.022 | -32.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 2600 | -0.026 | -42.34€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 2600 | -0.026 | -42.34€ | 2 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 1192 | -0.055 | -28.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 1192 | -0.055 | -28.89€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 970 | -0.031 | -35.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 970 | -0.031 | -35.44€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1671 | +0.123 | +678.18€ | 0 | 6 |
| ✅ ORDER_FLOW_5M#5min | 1535 | +0.129 | +665.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 358 | +0.139 | +181.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 358 | +0.139 | +181.89€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#DOGE | 313 | +0.113 | +102.27€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 313 | +0.113 | +102.27€ | 0 | 4 |
| ✅ ORDER_FLOW_5M#ETH | 308 | +0.136 | +148.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 308 | +0.136 | +148.62€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#SOL | 272 | +0.153 | +151.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 272 | +0.153 | +151.81€ | 0 | 5 |
| ✅ ORDER_FLOW_5M#XRP | 284 | +0.098 | +80.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 284 | +0.098 | +80.99€ | 0 | 3 |
| ✅ ORDER_FLOW_5M_REACTIVO | 1433 | -0.011 | -6.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1433 | -0.011 | -6.58€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 282 | +0.000 | +9.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 282 | +0.000 | +9.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 243 | -0.010 | +3.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 243 | -0.010 | +3.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 370 | -0.040 | -25.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 370 | -0.040 | -25.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 305 | +0.015 | +5.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 305 | +0.015 | +5.77€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 233 | -0.011 | +0.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 233 | -0.011 | +0.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 900 | -0.069 | -41.12€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 420 | -0.109 | -76.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 324 | -0.138 | -64.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 318 | -0.028 | +26.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 227 | -0.015 | +28.93€ | 1 | 1 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 91 | -0.059 | -2.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 162 | -0.043 | +9.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 131 | -0.049 | +4.73€ | 2 | 1 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 31 | -0.015 | +4.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 682 | -0.080 | -30.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 218 | -0.032 | -10.67€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 1125 | -0.207 | -69.66€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 438 | -0.209 | -41.88€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 381 | -0.213 | -41.65€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#reach | 57 | -0.178 | -0.23€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 385 | -0.211 | -33.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 337 | -0.223 | -41.00€ | 5 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#ETH#reach | 48 | -0.120 | +7.01€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 302 | -0.197 | +6.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 281 | -0.193 | +4.09€ | 5 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#reach | 21 | -0.239 | +2.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 999 | -0.211 | -78.56€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 126 | -0.172 | +8.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 453 | +0.395 | +433.28€ | 0 | 12 |
| ✅ RESOLUTION_SNIPER#BTC | 67 | +0.152 | +54.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 67 | +0.152 | +54.00€ | 0 | 1 |
| ✅ RESOLUTION_SNIPER#ETH | 110 | +0.366 | +102.82€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 110 | +0.366 | +102.82€ | 0 | 8 |
| ✅ RESOLUTION_SNIPER#SOL | 276 | +0.460 | +276.46€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 276 | +0.460 | +276.46€ | 0 | 10 |
| ✅ RESOLUTION_SNIPER#sniper | 453 | +0.395 | +433.28€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 721 | +0.028 | +34.36€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 721 | +0.028 | +34.36€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 302 | +0.023 | +3.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 302 | +0.023 | +3.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 73 | -0.007 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 73 | -0.007 | +0.78€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 287 | +0.050 | +31.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 287 | +0.050 | +31.88€ | 0 | 5 |
| ✅ STREAK_FADE_5M | 3442 | -0.021 | -133.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 3442 | -0.021 | -133.79€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 1059 | -0.020 | -35.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 1059 | -0.020 | -35.48€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 590 | -0.027 | -26.08€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 590 | -0.027 | -26.08€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 165 | -0.039 | -13.80€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 165 | -0.039 | -13.80€ | 4 | 0 |
| ✅ STREAK_FADE_5M#XRP | 1628 | -0.018 | -58.44€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 1628 | -0.018 | -58.44€ | 2 | 0 |
| ✅ STREAK_FADE_60M | 101 | -0.063 | -11.04€ | 5 | 0 |
| ✅ STREAK_FADE_60M#60min | 101 | -0.063 | -11.04€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 43 | -0.100 | -5.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 43 | -0.100 | -5.07€ | 4 | 0 |
| ✅ STREAK_FADE_60M#SOL | 58 | -0.033 | -5.97€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 58 | -0.033 | -5.97€ | 0 | 1 |
| ✅ STREAK_MOM_5M | 10833 | +0.017 | +95.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10833 | +0.017 | +95.00€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2769 | +0.020 | +28.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2769 | +0.020 | +28.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2820 | +0.019 | +38.68€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2820 | +0.019 | +38.68€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2356 | +0.019 | +28.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2356 | +0.019 | +28.97€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9834 | +0.013 | -49.99€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9834 | +0.013 | -49.99€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 3997 | +0.017 | -9.53€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 3997 | +0.017 | -9.53€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3616 | +0.011 | -27.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3616 | +0.011 | -27.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2221 | +0.009 | -13.33€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2221 | +0.009 | -13.33€ | 1 | 0 |
| ✅ UPDOWN_GBM | 75925 | +0.053 | +6684.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 18880 | +0.083 | +4142.23€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2445 | +0.004 | +23.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 49869 | +0.050 | +2432.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4465 | +0.007 | +86.85€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 16277 | +0.055 | +1390.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2437 | +0.089 | +592.77€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 655 | +0.010 | +10.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11099 | +0.061 | +723.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1990 | +0.004 | +60.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 96 | -0.071 | +2.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8384 | +0.068 | +884.40€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6751 | +0.051 | +275.23€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 17389 | +0.044 | +1124.55€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4467 | +0.065 | +651.38€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 639 | +0.005 | +16.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10629 | +0.044 | +435.47€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1565 | +0.012 | +18.88€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 89 | -0.104 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 16631 | +0.032 | +802.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4687 | +0.034 | +385.40€ | 0 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 608 | -0.008 | +0.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10347 | +0.037 | +414.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 910 | +0.007 | +7.27€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 79 | -0.130 | -4.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10391 | +0.064 | +1408.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4158 | +0.101 | +1203.64€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5845 | +0.040 | +205.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 264 | -0.102 | +1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 833 | +0.366 | +309.40€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 833 | +0.366 | +309.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 432 | +0.366 | +154.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 432 | +0.366 | +154.32€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 401 | +0.363 | +155.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 401 | +0.363 | +155.09€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19699 | -0.025 | +4622.05€ | 2 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19699 | -0.025 | +4622.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3493 | -0.112 | +135.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3493 | -0.112 | +135.59€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2388 | +0.218 | +1562.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2388 | +0.218 | +1562.60€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5618 | -0.066 | +667.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5618 | -0.066 | +667.55€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5534 | -0.065 | +983.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5534 | -0.065 | +983.03€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 227 | +0.042 | +9.93€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 227 | +0.042 | +9.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 227 | +0.042 | +9.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 227 | +0.042 | +9.93€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1415 | +0.292 | +1214.22€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1415 | +0.292 | +1214.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 760 | +0.290 | +617.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 760 | +0.290 | +617.98€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 655 | +0.294 | +596.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 655 | +0.294 | +596.24€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 814 | -0.112 | -82.65€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 814 | -0.112 | -82.65€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 248 | -0.080 | -18.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 248 | -0.080 | -18.10€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 87 | -0.163 | -9.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 87 | -0.163 | -9.15€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 96 | -0.184 | -6.04€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 96 | -0.184 | -6.04€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3610 | +0.303 | +1706.47€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1328 | +0.255 | +162.57€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1388 | +0.298 | +621.15€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 894 | +0.380 | +922.75€ | 0 | 1 |