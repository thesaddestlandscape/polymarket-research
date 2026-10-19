# Hipótesis automáticas — 2026-10-19 22:46 UTC
_Generado por shadow_postmortem.py sobre 971382 resoluciones (PNL=+126235.14€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **FILTRO** `py_entrada` > `0.495` → IC=-0.255 (n=194)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=625)

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

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 9759.7992 (IC base=+0.018)

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
- **FILTRO** `restante_s_al_confirmar` < `142.4` → IC=-0.207 (n=9971)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.4
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=29914)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.98` → IC=-0.263 (n=1120)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.98
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3360)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.52` → IC=-0.288 (n=1078)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.52
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3236)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.25` → IC=-0.208 (n=2627)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.25
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7882)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.32` → IC=-0.280 (n=1944)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.32
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=5832)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.213 (n=21467)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=4301)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `9157.1008` → IC=+0.178 (n=1939)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9157.1008 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.130 (n=18236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=32612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 11.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=16975)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=7154)

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
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.168 (n=468)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `6860.5651` → IC=+0.172 (n=123)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6860.5651 (IC base=+0.081)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1109)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.085)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.161 (n=2838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 12.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.231 (n=770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` < `0.26` → IC=+0.360 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.26 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=2165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1051)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=681)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.263 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=826)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `1880.1917` → IC=+0.154 (n=669)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1880.1917 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `4424.9893` → IC=+0.162 (n=152)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 4424.9893 (IC base=+0.069)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.253 (n=835)
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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=18134)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=15336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=7475)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.182 (n=3956)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.181 (n=4160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 18.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4078)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=3415)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=2126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.228 (n=2224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.306 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=4114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=3222)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=3571)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.361 (n=1141)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=4033)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.189)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=2572)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.189)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=2973)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=23537)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=23701)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.194 (n=3490)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.200 (n=10520)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=4914)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=4801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3440)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4031)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.212 (n=5363)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=4951)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=3750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.279 (n=3344)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=9014)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.262 (n=3486)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3912)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=3919)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=4080)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.192 (n=8516)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=8357)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.77` → IC=+0.136 (n=10225)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.77 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.195 (n=4212)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=4259)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.131 (n=4469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.77` → IC=+0.147 (n=3854)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.77 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.189 (n=4304)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=4557)

  - _Acción_: Kelly boost +0.68€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.133 (n=5150)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 3.33 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1644)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=1621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=568)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=746)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5005.426` → IC=+0.287 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5005.426 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.321 (n=530)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.296 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.297)

- **PATRÓN** `libro_liquidez` > `2113.1713` → IC=+0.310 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2113.1713 (IC base=+0.297)

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
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=94)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=80)

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
  - _Potencial_: sin este filtro IC_bueno=-0.208 (n=94)

- **FILTRO** `py_entrada` > `0.735` → IC=-0.365 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.735
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=80)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4777` → IC=+0.138 (n=13162)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4777 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=13331)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.9808` → IC=+0.248 (n=4387)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9808 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.783` → IC=+0.267 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.783 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.3701` → IC=+0.258 (n=3702)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3701 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.927` → IC=+0.190 (n=4980)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.927 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2003` → IC=+0.258 (n=3814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2003 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6202` → IC=+0.263 (n=3815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6202 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.239 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3425` → IC=+0.227 (n=4240)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3425 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.122 (n=16207)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6857` → IC=+0.129 (n=18406)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.6857 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1531` → IC=+0.187 (n=5953)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1531 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.185 (n=2773)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6961 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0494` → IC=+0.181 (n=2854)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0494 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2957` → IC=+0.231 (n=1573)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2957 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6792` → IC=+0.207 (n=3568)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6792 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.220 (n=10558)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.215 (n=955)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.3476` → IC=+0.201 (n=2865)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3476 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=1394)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=1914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.9802` → IC=+0.279 (n=1299)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9802 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.946` → IC=+0.281 (n=1256)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.946 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.248 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4388` → IC=+0.200 (n=2728)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4388 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.212 (n=3061)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2080.07` → IC=+0.206 (n=955)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2080.07 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.215 (n=1700)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=2398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.240 (n=1088)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.272 (n=802)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.255 (n=878)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5263` → IC=+0.259 (n=2398)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5263 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.239 (n=2147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.259 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.242 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6588` → IC=+0.246 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6588 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=2688)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1651.1194` → IC=+0.245 (n=2141)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1651.1194 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.241 (n=790)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.237 (n=1038)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.230 (n=1068)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.1061` → IC=+0.260 (n=1032)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1061 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2464)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9509` → IC=+0.277 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9509 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1289` → IC=+0.234 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1289 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.355` → IC=+0.265 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.355 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.2306` → IC=+0.230 (n=2344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2306 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.232 (n=2344)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.261 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.5102` → IC=+0.229 (n=1016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5102 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.253 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.151 (n=2382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0752` → IC=+0.168 (n=794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0752 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.152 (n=904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7285` → IC=+0.176 (n=2380)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7285 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.038` → IC=+0.147 (n=386)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 11.038 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.196` → IC=+0.142 (n=2175)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.196 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.1995` → IC=+0.141 (n=2380)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.1995 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.159 (n=870)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4537` → IC=+0.142 (n=2260)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4537 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4135` → IC=+0.135 (n=2260)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4135 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.174 (n=966)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 218.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0121` → IC=+0.217 (n=996)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0121 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.201 (n=3130)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.274 (n=627)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.200 (n=2638)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.210 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.6928` → IC=+0.210 (n=1309)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6928 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=3556)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `1977.9684` → IC=+0.201 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1977.9684 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.223 (n=2345)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.6047` → IC=+0.222 (n=2663)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6047 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=999)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0164` → IC=+0.275 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0164 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.409` → IC=+0.245 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.409 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3477` → IC=+0.257 (n=381)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3477 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.7276` → IC=+0.228 (n=1146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7276 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.218 (n=1392)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2054.9584` → IC=+0.225 (n=888)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2054.9584 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.220 (n=2175)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=148)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=3612)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.163 (n=532)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0036 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.9547` → IC=+0.227 (n=530)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9547 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.329 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.3359` → IC=+0.328 (n=557)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3359 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.12` → IC=+0.187 (n=1144)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 5.12 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.335 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.346 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2985` → IC=+0.348 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2985 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.4107` → IC=+0.346 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4107 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.2172` → IC=+0.326 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2172 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.337 (n=513)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0932` → IC=+0.173 (n=942)

  - _Acción_: Kelly boost +0.86€ cuando `ibs_20min` < 0.0932 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.323` → IC=+0.141 (n=446)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.323 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` < `0.13` → IC=+0.136 (n=1537)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.13 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8415` → IC=+0.147 (n=1113)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8415 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `1.1677` → IC=+0.135 (n=557)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.1677 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.200 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7767` → IC=+0.138 (n=1066)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.7767 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.151 (n=725)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.035)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=549)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.191 (n=163)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.105 (n=489)

- **FILTRO** `ibs_20min` > `0.2174` → IC=-0.132 (n=3538)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2174
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=1746)

- **FILTRO** `sigma_ewma_delta_pct` > `8.665` → IC=-0.239 (n=554)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.665
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4730)

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
- **FILTRO** `drift_60min` |x|> `0.6131` → IC=-0.179 (n=964)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6131
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2896)

- **FILTRO** `ibs_20min` < `0.75` → IC=-0.149 (n=2546)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1314)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.161 (n=956)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2904)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.203 (n=1393)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4181)

- **PATRÓN** `dist_vwap_pct` > `0.7184` → IC=+0.333 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7184 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` < `0.2486` → IC=+0.304 (n=585)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2486 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` < `1.1506` → IC=+0.297 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1506 (IC base=-0.066)

- **PATRÓN** `volumen_regimen` > `0.704` → IC=+0.313 (n=598)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.704 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.300 (n=629)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=-0.066)

- **PATRÓN** `volumen_pendiente_norm` > `0.0731` → IC=+0.303 (n=262)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0731 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` < `1.42` → IC=+0.321 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.42 (IC base=-0.066)

- **PATRÓN** `volumen_spike_ratio` > `1.8367` → IC=+0.304 (n=431)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8367 (IC base=-0.066)

- **PATRÓN** `dist_vwap_pct` > `0.8102` → IC=+0.274 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8102 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0691` → IC=+0.283 (n=690)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0691 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.282 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1865` → IC=+0.261 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1865 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4313` → IC=+0.263 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4313 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.207 (n=5780)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.3226` → IC=+0.168 (n=17305)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3226 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.953` → IC=+0.297 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.953 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.607` → IC=+0.161 (n=7765)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 3.607 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1691` → IC=+0.264 (n=6374)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1691 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6886` → IC=+0.268 (n=5694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6886 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2397` → IC=+0.277 (n=1897)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2397 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4596` → IC=+0.261 (n=3394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4596 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6413` → IC=+0.270 (n=3392)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6413 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.294 (n=9762)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.160 (n=5558)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0093 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.6593` → IC=+0.144 (n=16659)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6593 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.2405` → IC=+0.263 (n=5238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2405 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.260 (n=2314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `1.1948` → IC=+0.265 (n=1752)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1948 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.316 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.5797` → IC=+0.288 (n=3312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5797 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2682` → IC=+0.282 (n=3413)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2682 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `76.0` → IC=+0.293 (n=7444)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 76.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3718` → IC=-0.179 (n=1569)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3718
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=3187)

- **FILTRO** `ibs_20min` > `0.7424` → IC=-0.212 (n=997)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7424
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=2996)

- **FILTRO** `sigma_ewma_delta_pct` > `4.413` → IC=-0.206 (n=875)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.413
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=3118)

- **PATRÓN** `ibs_20min` > `0.9167` → IC=+0.308 (n=1192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9167 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.029` → IC=+0.216 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.029 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.301 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4427` → IC=+0.250 (n=518)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4427 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.2425` → IC=+0.272 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2425 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.278 (n=1053)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.1633` → IC=+0.161 (n=999)

  - _Acción_: Kelly boost +0.81€ cuando `ibs_20min` < 0.1633 (IC base=-0.028)

- **PATRÓN** `volumen_pendiente_norm` < `0.0734` → IC=+0.417 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0734 (IC base=-0.028)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.425 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=-0.028)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.411 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=-0.028)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1131` → IC=+0.213 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1131 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1937` → IC=+0.193 (n=1687)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.1937 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6821` → IC=+0.200 (n=1506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6821 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0748` → IC=+0.190 (n=1551)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0748 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.229 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.425` → IC=+0.219 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.425 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.4876` → IC=+0.191 (n=554)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.4876 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `274.0` → IC=+0.229 (n=1102)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 274.0 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1556` → IC=+0.226 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1556 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.235 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.273` → IC=+0.286 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.273 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5339` → IC=+0.237 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5339 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1651` → IC=+0.247 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1651 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.238 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.308 (n=845)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.273 (n=2657)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.287` → IC=+0.300 (n=624)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.287 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.279 (n=2197)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.272 (n=2441)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.277 (n=3000)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1971.202` → IC=+0.281 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1971.202 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.280 (n=1499)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.327 (n=991)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.291)

- **PATRÓN** `drift_60min` |x|≤ `0.1816` → IC=+0.310 (n=960)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1816 (IC base=+0.291)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.317 (n=836)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.291)

- **PATRÓN** `ibs_20min` < `0.3689` → IC=+0.295 (n=2182)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3689 (IC base=+0.291)

- **PATRÓN** `ibs_20min` > `0.2593` → IC=+0.298 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2593 (IC base=+0.291)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.567` → IC=+0.311 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.567 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` < `0.1976` → IC=+0.290 (n=2132)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1976 (IC base=+0.291)

- **PATRÓN** `volumen_pendiente_norm` > `0.3426` → IC=+0.311 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3426 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` < `1.5758` → IC=+0.297 (n=694)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5758 (IC base=+0.291)

- **PATRÓN** `volumen_spike_ratio` > `2.6774` → IC=+0.301 (n=944)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6774 (IC base=+0.291)

- **PATRÓN** `libro_liquidez` > `2051.2584` → IC=+0.307 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.2584 (IC base=+0.291)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.291 (n=1388)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.291)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7378` → IC=-0.185 (n=1046)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7378
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=3139)

- **PATRÓN** `ibs_20min` > `0.8799` → IC=+0.173 (n=992)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8799 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.234 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3648` → IC=+0.234 (n=1353)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3648 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` < `1.0074` → IC=+0.245 (n=1216)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0074 (IC base=+0.030)

- **PATRÓN** `volumen_regimen` > `0.6703` → IC=+0.231 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6703 (IC base=+0.030)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.251 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.030)

- **PATRÓN** `volumen_spike_ratio` < `1.3994` → IC=+0.248 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3994 (IC base=+0.030)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.267 (n=1198)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3309` → IC=+0.231 (n=1050)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3309 (IC base=-0.002)

- **PATRÓN** `volumen_regimen` < `1.1951` → IC=+0.231 (n=958)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1951 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` < `0.101` → IC=+0.246 (n=885)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.101 (IC base=-0.002)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.294 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` < `1.7961` → IC=+0.268 (n=605)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7961 (IC base=-0.002)

- **PATRÓN** `volumen_spike_ratio` > `2.4416` → IC=+0.251 (n=303)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4416 (IC base=-0.002)

- **PATRÓN** `ballena_activa_n` < `125.0` → IC=+0.257 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 125.0 (IC base=-0.002)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `ibs_20min` < `0.7606` → IC=-0.212 (n=1824)

  - _Acción_: SKIP cuando `ibs_20min` < 0.7606
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=1825)

- **FILTRO** `ibs_20min` > `0.6489` → IC=-0.234 (n=893)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6489
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=2683)

- **FILTRO** `sigma_ewma_delta_pct` > `8.532` → IC=-0.241 (n=415)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.532
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=3161)

- **PATRÓN** `ibs_20min` > `0.7606` → IC=+0.304 (n=1825)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7606 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.336 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.527` → IC=+0.183 (n=569)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 9.527 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` < `0.8456` → IC=+0.332 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8456 (IC base=+0.046)

- **PATRÓN** `volumen_regimen` > `0.7033` → IC=+0.324 (n=1224)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.7033 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` < `0.1585` → IC=+0.323 (n=1419)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1585 (IC base=+0.046)

- **PATRÓN** `volumen_pendiente_norm` > `0.2757` → IC=+0.349 (n=177)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2757 (IC base=+0.046)

- **PATRÓN** `volumen_spike_ratio` < `1.4415` → IC=+0.343 (n=444)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4415 (IC base=+0.046)

- **PATRÓN** `ballena_activa_n` < `49.0` → IC=+0.340 (n=1177)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 49.0 (IC base=+0.046)

- **PATRÓN** `ibs_20min` < `0.55` → IC=+0.144 (n=2365)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.55 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` < `0.4547` → IC=+0.250 (n=1278)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4547 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.263 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.2238` → IC=+0.241 (n=1325)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2238 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.261 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.251 (n=1133)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.270 (n=1148)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.031)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.345 (n=1730)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.301)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.304 (n=755)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.312 (n=925)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.301)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.335 (n=1939)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.301)

- **PATRÓN** `dist_vwap_pct` > `0.2054` → IC=+0.327 (n=1085)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2054 (IC base=+0.301)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.795` → IC=+0.322 (n=940)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.795 (IC base=+0.301)

- **PATRÓN** `volumen_regimen` > `0.6266` → IC=+0.310 (n=1937)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6266 (IC base=+0.301)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.343 (n=279)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.301)

- **PATRÓN** `volumen_spike_ratio` > `1.4247` → IC=+0.313 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4247 (IC base=+0.301)

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
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.225 (n=4258)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.181)

- **PATRÓN** `drift_60min` |x|≤ `0.0871` → IC=+0.202 (n=4255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0871 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=13259)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.5588` → IC=+0.234 (n=12754)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5588 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1637` → IC=+0.208 (n=5148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1637 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.264` → IC=+0.260 (n=2511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.264 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1861` → IC=+0.169 (n=8461)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1861 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.6242` → IC=+0.166 (n=8462)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6242 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2933` → IC=+0.205 (n=1856)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2933 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.179 (n=5439)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6086` → IC=+0.191 (n=4121)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6086 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1982.1859` → IC=+0.182 (n=11394)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1982.1859 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.199 (n=11675)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 95.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.183 (n=10801)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0091 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.227 (n=4095)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=5829)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.236 (n=12285)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.1743` → IC=+0.174 (n=8749)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1743 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.035` → IC=+0.197 (n=2007)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.035 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.69` → IC=+0.181 (n=10821)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 2.69 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1823` → IC=+0.162 (n=8763)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1823 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.224 (n=1814)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6363` → IC=+0.187 (n=3841)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6363 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.191 (n=11237)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.234 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3321` → IC=+0.229 (n=2134)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3321 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.218 (n=2236)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.221 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.295 (n=1422)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.986` → IC=+0.331 (n=674)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.986 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.270 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `1.4364` → IC=+0.214 (n=2016)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4364 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.226 (n=2300)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1596` → IC=+0.184 (n=1281)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1596 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=2027)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3422` → IC=+0.223 (n=1920)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3422 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1342` → IC=+0.215 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1342 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.364` → IC=+0.225 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.364 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6893` → IC=+0.164 (n=845)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6893 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.196 (n=307)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4131` → IC=+0.180 (n=627)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4131 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.5048` → IC=+0.163 (n=627)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5048 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `422.0` → IC=+0.159 (n=1843)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 422.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.169 (n=2020)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.234` → IC=+0.172 (n=1775)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.234 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.184 (n=972)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6188` → IC=+0.205 (n=2017)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6188 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.49` → IC=+0.193 (n=382)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 11.49 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.243` → IC=+0.144 (n=1755)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.243 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.204` → IC=+0.159 (n=2017)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.204 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.094` → IC=+0.147 (n=1708)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.094 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.5004` → IC=+0.152 (n=1897)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.5004 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.146 (n=1896)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4236 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.181 (n=612)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 202.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.237 (n=980)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.214)

- **PATRÓN** `drift_60min` |x|≤ `0.3996` → IC=+0.225 (n=1901)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3996 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.234 (n=796)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.214)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.442` → IC=+0.299 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.442 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.213 (n=1848)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.214)

- **PATRÓN** `volumen_pendiente_norm` > `0.3545` → IC=+0.229 (n=312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3545 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` < `1.7667` → IC=+0.216 (n=921)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7667 (IC base=+0.214)

- **PATRÓN** `volumen_spike_ratio` > `2.7088` → IC=+0.227 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7088 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.221 (n=2576)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `1963.5896` → IC=+0.226 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1963.5896 (IC base=+0.214)

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
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.175 (n=2070)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0074 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4062` → IC=+0.168 (n=2070)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4062 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2151)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3118` → IC=+0.214 (n=2070)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3118 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1413` → IC=+0.200 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1413 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.766` → IC=+0.201 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.766 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.0223` → IC=+0.159 (n=1821)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0223 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.1029` → IC=+0.180 (n=846)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.1029 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.8174` → IC=+0.150 (n=1353)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.8174 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5051` → IC=+0.167 (n=677)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5051 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4612.7985` → IC=+0.187 (n=1380)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 4612.7985 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.160 (n=2005)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 139.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.153 (n=2179)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0072 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3955` → IC=+0.143 (n=2178)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3955 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6858` → IC=+0.186 (n=2178)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6858 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1526` → IC=+0.156 (n=2180)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1526 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.609` → IC=+0.160 (n=539)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 9.609 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8557` → IC=+0.155 (n=1452)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8557 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2997` → IC=+0.196 (n=330)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2997 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.81` → IC=+0.135 (n=1360)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.81 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `1.4244` → IC=+0.126 (n=2039)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4244 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7562.5057` → IC=+0.193 (n=988)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7562.5057 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.147 (n=881)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 68.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.178 (n=1056)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0103 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4428` → IC=+0.130 (n=2048)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4428 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=1116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.4915` → IC=+0.215 (n=2327)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4915 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1959` → IC=+0.188 (n=1351)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.1959 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.599` → IC=+0.278 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.599 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.143 (n=2327)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1741 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.161` → IC=+0.136 (n=2362)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.161 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4387` → IC=+0.150 (n=753)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4387 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2433)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2793.361` → IC=+0.206 (n=1055)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2793.361 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.167 (n=745)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 20.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.139 (n=2377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0108 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.173 (n=794)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.140 (n=2424)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.218 (n=2384)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1993` → IC=+0.148 (n=2251)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1993 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.461` → IC=+0.131 (n=2098)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 2.461 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1753` → IC=+0.130 (n=2377)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1753 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1653` → IC=+0.123 (n=2298)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1653 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.2749` → IC=+0.152 (n=317)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_pendiente_norm` > 0.2749 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.446` → IC=+0.135 (n=738)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.446 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4234` → IC=+0.138 (n=738)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` > 2.4234 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2655.5302` → IC=+0.192 (n=1078)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2655.5302 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.130 (n=1925)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 42.0 (IC base=+0.120)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.246 (n=1919)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0129 (IC base=+0.222)

- **PATRÓN** `drift_60min` |x|≤ `0.1289` → IC=+0.240 (n=716)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1289 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.226 (n=2228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=1923)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.222)

- **PATRÓN** `ibs_20min` > `0.66` → IC=+0.258 (n=2150)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.66 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` > `0.1837` → IC=+0.227 (n=1380)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1837 (IC base=+0.222)

- **PATRÓN** `dist_vwap_pct` < `0.4781` → IC=+0.224 (n=1926)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4781 (IC base=+0.222)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.250 (n=975)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` < `1.178` → IC=+0.225 (n=2146)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.178 (IC base=+0.222)

- **PATRÓN** `volumen_regimen` > `0.6187` → IC=+0.231 (n=2145)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6187 (IC base=+0.222)

- **PATRÓN** `volumen_pendiente_norm` > `0.2832` → IC=+0.269 (n=297)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2832 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` < `2.4668` → IC=+0.228 (n=2087)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4668 (IC base=+0.222)

- **PATRÓN** `volumen_spike_ratio` > `1.8078` → IC=+0.230 (n=1391)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8078 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `2615.829` → IC=+0.227 (n=1430)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2615.829 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.234 (n=731)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.01 (IC base=+0.228)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.240 (n=995)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0225 (IC base=+0.228)

- **PATRÓN** `drift_60min` |x|≤ `0.0887` → IC=+0.261 (n=731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0887 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1073)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.4267` → IC=+0.256 (n=2192)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4267 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.2961` → IC=+0.234 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2961 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.33` → IC=+0.257 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.33 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.641` → IC=+0.235 (n=2192)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.641 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.281` → IC=+0.285 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.281 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.230 (n=2038)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4406 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2591.9144` → IC=+0.229 (n=1461)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2591.9144 (IC base=+0.228)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.208 (n=1435)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.190 (n=1083)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0089 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.1291` → IC=+0.204 (n=1430)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1291 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.216 (n=1620)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.7231` → IC=+0.232 (n=2166)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7231 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.7932` → IC=+0.203 (n=480)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7932 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.635` → IC=+0.212 (n=1403)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.635 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.204 (n=1953)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.6952` → IC=+0.185 (n=2615)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6952 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.192 (n=1168)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4308` → IC=+0.199 (n=1053)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4308 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.1943` → IC=+0.186 (n=1432)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.1943 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=3672)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2693.0919` → IC=+0.189 (n=2903)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2693.0919 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.194 (n=3031)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 150.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.134 (n=1170)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0038 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.3818` → IC=+0.160 (n=2338)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.3818 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.129 (n=1140)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 19.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.203 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3269` → IC=+0.200 (n=921)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3269 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.6304` → IC=+0.234 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6304 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.3084` → IC=+0.198 (n=273)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3084 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.068` → IC=+0.197 (n=394)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.068 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `0.871` → IC=+0.204 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.871 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.0723` → IC=+0.182 (n=363)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.0723 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `2.2069` → IC=+0.188 (n=793)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.2069 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `14622.535` → IC=+0.183 (n=614)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14622.535 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.206 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.184 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0028 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.2682` → IC=+0.143 (n=961)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.2682 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.131 (n=994)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6326` → IC=+0.170 (n=961)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6326 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.694` → IC=+0.130 (n=217)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 8.694 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `1.0613` → IC=+0.147 (n=496)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0613 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.1616` → IC=+0.166 (n=291)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1616 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.133 (n=950)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.120 (n=1415)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.162 (n=708)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 217.0 (IC base=+0.119)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.247 (n=659)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.216)

- **PATRÓN** `drift_60min` |x|≤ `0.0935` → IC=+0.244 (n=330)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0935 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.232 (n=1038)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.216)

- **PATRÓN** `ibs_20min` > `0.3764` → IC=+0.257 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3764 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` > `0.3563` → IC=+0.222 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3563 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.2052` → IC=+0.221 (n=891)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2052 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.882` → IC=+0.245 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.882 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` < `0.8344` → IC=+0.226 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8344 (IC base=+0.216)

- **PATRÓN** `volumen_regimen` > `0.6827` → IC=+0.217 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6827 (IC base=+0.216)

- **PATRÓN** `volumen_pendiente_norm` > `0.2672` → IC=+0.250 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2672 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.247 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.216)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.230 (n=650)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.216)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=1106)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.216)

- **PATRÓN** `ibs_20min` < `0.106` → IC=+0.164 (n=337)

  - _Acción_: Kelly boost +0.82€ cuando `ibs_20min` < 0.106 (IC base=+0.060)

- **PATRÓN** `libro_liquidez` > `6610.7915` → IC=+0.136 (n=673)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 6610.7915 (IC base=+0.060)

### GBM_LATE_15M_PYCONFIRMADO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0097` → IC=+0.177 (n=363)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0097 (IC base=+0.164)

- **PATRÓN** `drift_60min` |x|≤ `0.5352` → IC=+0.165 (n=801)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.5352 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.220 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.164)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.275 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `1.0116` → IC=+0.236 (n=142)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0116 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.0` → IC=+0.249 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.0 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` < `1.0604` → IC=+0.182 (n=705)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_regimen` < 1.0604 (IC base=+0.164)

- **PATRÓN** `volumen_regimen` > `0.7162` → IC=+0.171 (n=715)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` > 0.7162 (IC base=+0.164)

- **PATRÓN** `volumen_pendiente_norm` > `0.1641` → IC=+0.182 (n=221)

  - _Acción_: Kelly boost +0.91€ cuando `volumen_pendiente_norm` > 0.1641 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` < `1.4478` → IC=+0.181 (n=258)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4478 (IC base=+0.164)

- **PATRÓN** `volumen_spike_ratio` > `2.1798` → IC=+0.171 (n=350)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 2.1798 (IC base=+0.164)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=826)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `3044.5069` → IC=+0.191 (n=267)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3044.5069 (IC base=+0.164)

- **PATRÓN** `ibs_20min` < `0.5417` → IC=+0.132 (n=756)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5417 (IC base=+0.054)

- **PATRÓN** `libro_liquidez` > `2719.8549` → IC=+0.143 (n=390)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2719.8549 (IC base=+0.054)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.130 (n=554)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 21.0 (IC base=+0.054)

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
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.226 (n=5539)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=17335)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.231 (n=16614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4483 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.9004` → IC=+0.210 (n=2023)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9004 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.272` → IC=+0.255 (n=4061)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.272 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.2208` → IC=+0.170 (n=11136)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2208 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.207 (n=2208)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.613` → IC=+0.197 (n=5384)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.613 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1973.7124` → IC=+0.185 (n=14840)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1973.7124 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `113.0` → IC=+0.204 (n=15252)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 113.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.191 (n=13274)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0096 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3798` → IC=+0.192 (n=13267)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3798 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=5627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.242 (n=15086)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.1752` → IC=+0.171 (n=9228)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1752 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.838` → IC=+0.204 (n=2092)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.838 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.578` → IC=+0.191 (n=14571)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.578 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.7048` → IC=+0.163 (n=4478)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.7048 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.253 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.6149` → IC=+0.198 (n=4750)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6149 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.216 (n=9376)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.235 (n=904)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.3479` → IC=+0.227 (n=2711)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3479 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.237 (n=1316)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.329 (n=1068)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.529` → IC=+0.354 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.529 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2318` → IC=+0.280 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2318 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.221 (n=868)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.2767` → IC=+0.235 (n=1181)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2767 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.241 (n=2882)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2001.8802` → IC=+0.229 (n=1229)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2001.8802 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.250 (n=1106)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.266 (n=2309)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1192` → IC=+0.286 (n=1016)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1192 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.269 (n=2116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5093` → IC=+0.288 (n=2310)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5093 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.173` → IC=+0.265 (n=458)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.173 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0953` → IC=+0.262 (n=2073)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0953 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.288 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.4431` → IC=+0.265 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4431 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6447` → IC=+0.273 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6447 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2596)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1649.7388` → IC=+0.269 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1649.7388 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.267 (n=1033)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.198 (n=899)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1045` → IC=+0.168 (n=1183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.1045 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3714` → IC=+0.225 (n=2400)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3714 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1252` → IC=+0.197 (n=1389)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1252 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.609` → IC=+0.162 (n=572)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 9.609 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.167` → IC=+0.154 (n=2467)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 4.167 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6301` → IC=+0.176 (n=896)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6301 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.155 (n=2395)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2717` → IC=+0.185 (n=385)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2717 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1861` → IC=+0.160 (n=2311)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1861 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5312` → IC=+0.155 (n=2346)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.5312 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `266.0` → IC=+0.186 (n=1137)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 266.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=2238)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.164 (n=1969)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6986` → IC=+0.198 (n=2238)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.6986 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.198` → IC=+0.154 (n=371)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 11.198 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.443` → IC=+0.144 (n=2253)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 6.443 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1894` → IC=+0.154 (n=2238)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1894 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2182` → IC=+0.193 (n=422)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2182 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4323` → IC=+0.149 (n=2133)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4323 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.155 (n=1422)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `275.0` → IC=+0.159 (n=902)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 275.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.260 (n=924)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2895)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.304` → IC=+0.322 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.304 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.0966` → IC=+0.231 (n=2445)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0966 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `3.1929` → IC=+0.239 (n=895)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1929 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3294)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1831.6886` → IC=+0.235 (n=1844)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1831.6886 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.245 (n=2281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.240)

- **PATRÓN** `drift_60min` |x|≤ `0.1818` → IC=+0.257 (n=1140)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1818 (IC base=+0.240)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.261 (n=976)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.240)

- **PATRÓN** `ibs_20min` < `0.0303` → IC=+0.307 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0303 (IC base=+0.240)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.96` → IC=+0.293 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.96 (IC base=+0.240)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.300 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.240)

- **PATRÓN** `volumen_spike_ratio` > `2.1336` → IC=+0.249 (n=1642)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1336 (IC base=+0.240)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.242 (n=1365)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.240)

- **PATRÓN** `libro_liquidez` > `2051.1091` → IC=+0.255 (n=864)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.1091 (IC base=+0.240)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.256 (n=1075)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.240)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.197 (n=1259)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4209` → IC=+0.159 (n=2856)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4209 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2969)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2479` → IC=+0.194 (n=2857)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2479 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.172 (n=1511)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1412 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.141` → IC=+0.161 (n=1159)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.141 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8651` → IC=+0.166 (n=1905)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8651 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2803` → IC=+0.193 (n=372)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2803 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5231` → IC=+0.163 (n=1226)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` < 1.5231 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1659` → IC=+0.158 (n=1263)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` > 2.1659 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6295.0353` → IC=+0.244 (n=1295)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6295.0353 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.175 (n=1215)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 74.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.149 (n=2377)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0075 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4396` → IC=+0.139 (n=2377)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4396 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=870)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.737` → IC=+0.183 (n=2377)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.737 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.144 (n=2166)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.109` → IC=+0.171 (n=363)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.109 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.8687` → IC=+0.138 (n=1585)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.8687 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.222 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.2238` → IC=+0.130 (n=2011)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.2238 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4297` → IC=+0.135 (n=2285)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4297 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7242.0685` → IC=+0.212 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7242.0685 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.130 (n=777)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 67.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.156 (n=1304)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0103 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.178 (n=1061)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.199 (n=2876)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4444 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.067` → IC=+0.207 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.067 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.748` → IC=+0.266 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.748 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2204` → IC=+0.136 (n=2875)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2204 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1615` → IC=+0.126 (n=2990)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1615 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2785` → IC=+0.136 (n=372)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2785 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8314` → IC=+0.128 (n=1874)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8314 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4628` → IC=+0.126 (n=2808)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4628 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2982)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2496.5462` → IC=+0.231 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2496.5462 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.146 (n=897)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 24.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.152 (n=2412)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.156 (n=914)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=2826)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6463` → IC=+0.212 (n=2737)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6463 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2146` → IC=+0.136 (n=2360)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2146 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.259` → IC=+0.135 (n=2637)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.259 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.7102` → IC=+0.140 (n=1205)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7102 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2245` → IC=+0.174 (n=468)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2245 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4404` → IC=+0.155 (n=854)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4404 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2673.0949` → IC=+0.208 (n=913)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2673.0949 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.134 (n=2247)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 47.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.249 (n=2429)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=2842)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.235 (n=1962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `0.61` → IC=+0.271 (n=2433)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.61 (IC base=+0.230)

- **PATRÓN** `dist_vwap_pct` > `0.1902` → IC=+0.246 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1902 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.270 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` < `1.2301` → IC=+0.238 (n=2719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2301 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` > `0.6399` → IC=+0.233 (n=2719)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6399 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.254 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.5041` → IC=+0.250 (n=882)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5041 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3532)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `2963.6442` → IC=+0.239 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2963.6442 (IC base=+0.230)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.251 (n=942)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.236 (n=2662)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.264 (n=2825)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.196` → IC=+0.266 (n=540)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.196 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `1.2292` → IC=+0.259 (n=943)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2292 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.282` → IC=+0.299 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.282 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.232 (n=2622)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4316 (IC base=+0.229)

### GBM_LATE_5M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.194 (n=4911)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.246 (n=1682)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.208)

- **PATRÓN** `drift_60min` |x|≤ `0.5039` → IC=+0.219 (n=5046)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.5039 (IC base=+0.208)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.225 (n=1839)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `ibs_20min` > `0.9401` → IC=+0.248 (n=1684)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9401 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.1709` → IC=+0.208 (n=1861)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1709 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.9438` → IC=+0.211 (n=4232)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.9438 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.02` → IC=+0.215 (n=823)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.02 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.615` → IC=+0.210 (n=4494)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.615 (IC base=+0.208)

- **PATRÓN** `volumen_regimen` < `0.7051` → IC=+0.221 (n=1615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7051 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` < `0.1063` → IC=+0.208 (n=4711)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1063 (IC base=+0.208)

- **PATRÓN** `volumen_pendiente_norm` > `0.1666` → IC=+0.223 (n=1418)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1666 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` < `1.455` → IC=+0.215 (n=1656)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.455 (IC base=+0.208)

- **PATRÓN** `volumen_spike_ratio` > `1.8456` → IC=+0.210 (n=3312)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.8456 (IC base=+0.208)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=3881)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `2928.3635` → IC=+0.216 (n=4508)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2928.3635 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.239 (n=1234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.192)

- **PATRÓN** `drift_60min` |x|≤ `0.4893` → IC=+0.208 (n=3695)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4893 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=1254)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.207 (n=1643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.192)

- **PATRÓN** `ibs_20min` < `0.7325` → IC=+0.199 (n=3695)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.7325 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` > `0.6749` → IC=+0.199 (n=622)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6749 (IC base=+0.192)

- **PATRÓN** `dist_vwap_pct` < `0.4216` → IC=+0.191 (n=3734)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.4216 (IC base=+0.192)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.843` → IC=+0.203 (n=3313)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.843 (IC base=+0.192)

- **PATRÓN** `volumen_regimen` < `1.0969` → IC=+0.202 (n=3081)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0969 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.196 (n=3389)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.192)

- **PATRÓN** `volumen_pendiente_norm` > `0.2229` → IC=+0.194 (n=746)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2229 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` < `1.5329` → IC=+0.197 (n=1604)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_spike_ratio` < 1.5329 (IC base=+0.192)

- **PATRÓN** `volumen_spike_ratio` > `2.1885` → IC=+0.201 (n=1652)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1885 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=4911)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `ballena_activa_n` < `72.0` → IC=+0.204 (n=2417)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 72.0 (IC base=+0.192)

### GBM_LATE_5M#BTC#5min
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.273 (n=673)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.260)

- **PATRÓN** `drift_60min` |x|≤ `0.0853` → IC=+0.294 (n=255)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0853 (IC base=+0.260)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.266 (n=766)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.260)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.260 (n=765)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.260)

- **PATRÓN** `ibs_20min` < `0.489` → IC=+0.279 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.489 (IC base=+0.260)

- **PATRÓN** `dist_vwap_pct` < `0.3378` → IC=+0.275 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3378 (IC base=+0.260)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.054` → IC=+0.274 (n=179)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.054 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` < `1.2151` → IC=+0.267 (n=763)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2151 (IC base=+0.260)

- **PATRÓN** `volumen_regimen` > `0.868` → IC=+0.273 (n=509)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.868 (IC base=+0.260)

- **PATRÓN** `volumen_pendiente_norm` > `0.2875` → IC=+0.350 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2875 (IC base=+0.260)

- **PATRÓN** `volumen_spike_ratio` < `1.8249` → IC=+0.267 (n=508)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8249 (IC base=+0.260)

- **PATRÓN** `libro_liquidez` > `16321.2566` → IC=+0.274 (n=255)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16321.2566 (IC base=+0.260)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.4924` → IC=+0.211 (n=1125)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4924 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.203 (n=439)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.198 (n=752)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 10.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.3986` → IC=+0.196 (n=750)

  - _Acción_: Kelly boost +0.98€ cuando `ibs_20min` < 0.3986 (IC base=+0.188)

- **PATRÓN** `ibs_20min` > `0.0867` → IC=+0.190 (n=1125)

  - _Acción_: Kelly boost +0.95€ cuando `ibs_20min` > 0.0867 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` > `0.6705` → IC=+0.199 (n=197)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.6705 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.2251` → IC=+0.189 (n=1088)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.2251 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.36` → IC=+0.195 (n=1022)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 4.36 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.6394` → IC=+0.224 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6394 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.0741` → IC=+0.207 (n=473)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0741 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` < `2.1925` → IC=+0.197 (n=969)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 2.1925 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.5255` → IC=+0.191 (n=367)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.5255 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `6777.6409` → IC=+0.196 (n=1125)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 6777.6409 (IC base=+0.188)

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

- **PATRÓN** `volumen_regimen` < `0.7551` → IC=+0.212 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7551 (IC base=+0.201)

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

- **PATRÓN** `ibs_20min` > `0.3924` → IC=+0.145 (n=1560)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.3924 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.3636` → IC=+0.157 (n=540)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3636 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.999` → IC=+0.163 (n=455)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 8.999 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2761` → IC=+0.148 (n=217)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2761 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.233 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.358` → IC=+0.174 (n=133)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 10.358 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.1466` → IC=+0.170 (n=234)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_pendiente_norm` > 0.1466 (IC base=+0.057)

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

- **PATRÓN** `ibs_20min` < `0.0493` → IC=+0.281 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0493 (IC base=+0.073)

- **PATRÓN** `volumen_pendiente_norm` > `0.2162` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2162 (IC base=+0.073)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7041` → IC=-0.185 (n=90)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7041
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

- **PATRÓN** `ibs_20min` < `0.0289` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0289 (IC base=+0.018)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.018)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.167 (n=358)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.75 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.475` → IC=+0.124 (n=187)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.475 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.36` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.36 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.2291` → IC=+0.135 (n=102)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_pendiente_norm` > 0.2291 (IC base=+0.033)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.152 (n=234)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0103 (IC base=+0.078)

- **PATRÓN** `ibs_20min` < `0.1379` → IC=+0.222 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.1379 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` > `0.2251` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.2251 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.1772` → IC=+0.151 (n=193)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1772 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.715` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.715 (IC base=+0.078)

- **PATRÓN** `volumen_regimen` > `1.0779` → IC=+0.229 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0779 (IC base=+0.078)

- **PATRÓN** `volumen_pendiente_norm` > `0.1518` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1518 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` < `2.1557` → IC=+0.152 (n=159)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.1557 (IC base=+0.078)

- **PATRÓN** `volumen_spike_ratio` > `1.4056` → IC=+0.170 (n=180)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_spike_ratio` > 1.4056 (IC base=+0.078)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.157 (n=176)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.06 (IC base=+0.078)

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

- **FILTRO** `sigma_h` > `0.0052` → IC=-0.333 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=196)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.274 (n=241)

- **FILTRO** `volumen_pendiente_norm` > `0.0465` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0465
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=145)

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
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=76)

- **FILTRO** `hora_utc` < `6.0` → IC=-0.375 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.263 (n=78)

- **FILTRO** `libro_spread` > `0.02` → IC=-0.324 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.02
  - _Potencial_: sin este filtro IC_bueno=-0.282 (n=85)

- **FILTRO** `libro_liquidez` < `1582.3345` → IC=-0.308 (n=50)

  - _Acción_: SKIP cuando `libro_liquidez` < 1582.3345
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
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=538)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.189 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.006 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.113)

- **PATRÓN** `ibs_20min` > `0.68` → IC=+0.151 (n=519)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` > 0.68 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.741` → IC=+0.207 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.741 (IC base=+0.113)

- **PATRÓN** `volumen_regimen` < `0.6242` → IC=+0.174 (n=173)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_regimen` < 0.6242 (IC base=+0.113)

- **PATRÓN** `volumen_pendiente_norm` < `0.2267` → IC=+0.145 (n=466)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.2267 (IC base=+0.113)

- **PATRÓN** `volumen_spike_ratio` < `1.7926` → IC=+0.157 (n=278)

  - _Acción_: Kelly boost +0.79€ cuando `volumen_spike_ratio` < 1.7926 (IC base=+0.113)

- **PATRÓN** `ibs_20min` < `0.1613` → IC=+0.152 (n=538)

  - _Acción_: Kelly boost +0.76€ cuando `ibs_20min` < 0.1613 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.085` → IC=+0.185 (n=182)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 9.085 (IC base=+0.058)

- **PATRÓN** `volumen_pendiente_norm` > `0.2227` → IC=+0.124 (n=123)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.2227 (IC base=+0.058)

- **PATRÓN** `libro_liquidez` > `3239.2397` → IC=+0.136 (n=407)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 3239.2397 (IC base=+0.058)

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

- **FILTRO** `ibs_20min` > `0.1832` → IC=-0.141 (n=101)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1832
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

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.027)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.027)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `ibs_20min` > `0.4` → IC=-0.278 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=106)

- **FILTRO** `dist_vwap_pct` > `0.1699` → IC=-0.150 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1699
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=102)

- **FILTRO** `volumen_spike_ratio` > `2.3635` → IC=-0.204 (n=25)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3635
  - _Potencial_: sin este filtro IC_bueno=-0.037 (n=78)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.311 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 13.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` > `0.6522` → IC=+0.272 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6522 (IC base=+0.249)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.386 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.249)

- **PATRÓN** `dist_vwap_pct` < `0.2335` → IC=+0.257 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2335 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.317 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.249)

- **PATRÓN** `volumen_regimen` < `0.5804` → IC=+0.323 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.5804 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.1048` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1048 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` < `1.4854` → IC=+0.395 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4854 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.06` → IC=+0.250 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.06 (IC base=+0.249)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.321` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.321 (IC base=-0.091)

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
- **PATRÓN** `libro_liquidez` > `2847.7662` → IC=+0.131 (n=565)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2847.7662 (IC base=+0.101)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `libro_liquidez` > `2847.7662` → IC=+0.131 (n=565)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 2847.7662 (IC base=+0.101)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=3496)

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
  - _Potencial_: sin este filtro IC_bueno=+0.034 (n=416)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.122 (n=35)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.036 (n=397)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.144 (n=175)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.495 (IC base=+0.023)

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

- **FILTRO** `py_entrada` > `0.57` → IC=-0.139 (n=192)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.165 (n=5933)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=18434)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.175 (n=6036)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=18985)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.195 (n=1088)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.116 (n=3339)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.174 (n=1035)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3440)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.144 (n=1167)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `1317.92` → IC=+0.137 (n=2214)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1317.92 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.127 (n=2091)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.012)

- **PATRÓN** `libro_liquidez` > `1504.9852` → IC=+0.153 (n=1522)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 1504.9852 (IC base=+0.012)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.159 (n=823)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2746)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=875)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2674)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.174 (n=1082)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=3358)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=1067)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=3501)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.131 (n=1514)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1817.4014` → IC=+0.125 (n=1510)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 1817.4014 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.158 (n=1079)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=3356)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2368)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=758)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2306)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2794)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=3534)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=873)

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
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=915)

- **FILTRO** `libro_liquidez` < `1760.3335` → IC=-0.164 (n=233)

  - _Acción_: SKIP cuando `libro_liquidez` < 1760.3335
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=701)

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
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=37541)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13334)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=40927)

- **FILTRO** `ibs_7min` < `0.2381` → IC=-0.230 (n=13551)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=40710)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=18110)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=36151)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=16741)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=51541)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.182 (n=16906)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=51376)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6770)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.236 (n=4677)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4789)

- **FILTRO** `ibs_7min` < `0.7123` → IC=-0.243 (n=3123)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7123
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6343)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.178 (n=2020)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7446)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.270 (n=2937)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=8902)

- **FILTRO** `ibs_7min` > `0.7714` → IC=-0.210 (n=2959)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7714
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=8880)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=2136)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7023)

- **FILTRO** `ibs_7min` < `0.7268` → IC=-0.200 (n=2289)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7268
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6870)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.192 (n=2278)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6881)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2295)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7007)

- **FILTRO** `ibs_7min` > `0.2682` → IC=-0.196 (n=2324)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2682
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6978)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.183 (n=2315)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=6987)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=2200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6800)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.315 (n=2214)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6786)

- **FILTRO** `ibs_7min` < `0.2969` → IC=-0.246 (n=2968)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2969
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6032)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.196 (n=2144)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6856)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.256 (n=2939)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9666)

- **FILTRO** `ibs_7min` > `0.7347` → IC=-0.178 (n=3151)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7347
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=9454)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2071)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6771)

- **FILTRO** `ibs_7min` < `0.7296` → IC=-0.187 (n=2210)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7296
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6632)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.189 (n=2191)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6651)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=2058)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7105)

- **FILTRO** `ibs_7min` > `0.275` → IC=-0.180 (n=2289)

  - _Acción_: SKIP cuando `ibs_7min` > 0.275
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=6874)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.175 (n=2257)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6906)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=2128)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6777)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.233 (n=2216)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=6689)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.219 (n=2146)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6759)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.191 (n=3155)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=9884)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.292 (n=2092)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=6797)

- **FILTRO** `ibs_7min` < `0.2029` → IC=-0.222 (n=2222)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2029
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6667)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.202 (n=1987)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=6902)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.217 (n=3012)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9322)

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

- **FILTRO** `sigma_h` > `0.006` → IC=-0.296 (n=219)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=430)

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
- **FILTRO** `hora_utc` > `9.0` → IC=-0.219 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=93)

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
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1182)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=3981)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2189)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.198 (n=1184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0047 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.197 (n=1183)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0119 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1748` → IC=+0.195 (n=3123)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.1748 (IC base=+0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1333` → IC=+0.189 (n=1414)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1333 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=3295)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=3255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_15` > `0.56` → IC=+0.255 (n=3547)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.56 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.1276` → IC=+0.169 (n=1687)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1276 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.4914` → IC=+0.167 (n=3174)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.4914 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.542` → IC=+0.254 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.542 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `4706.5295` → IC=+0.197 (n=1183)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 4706.5295 (IC base=+0.179)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1409)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.251 (n=267)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.266 (n=203)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.219)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2541` → IC=+0.250 (n=202)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2541 (IC base=+0.219)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2298` → IC=+0.232 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2298 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.239 (n=608)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.285 (n=607)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.2432` → IC=+0.243 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2432 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.96` → IC=+0.302 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.96 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.220 (n=787)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `8997.0825` → IC=+0.229 (n=607)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8997.0825 (IC base=+0.219)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.188 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0034 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.157 (n=310)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.146)

- **PATRÓN** `drift_15min` |x|≤ `0.3955` → IC=+0.150 (n=235)

  - _Acción_: Kelly boost +0.75€ cuando `drift_15min` |x|≤ 0.3955 (IC base=+0.146)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.152 (n=469)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.146)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1315` → IC=+0.160 (n=277)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1315 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.156 (n=646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 6.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.146)

- **PATRÓN** `ibs_15` > `0.5467` → IC=+0.245 (n=703)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5467 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.159 (n=435)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.827` → IC=+0.263 (n=133)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.827 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `3210.7419` → IC=+0.155 (n=703)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 3210.7419 (IC base=+0.146)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.774` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.774
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=329)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1728` → IC=+0.138 (n=523)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1728 (IC base=+0.095)

- **PATRÓN** `ibs_15` > `0.8947` → IC=+0.251 (n=263)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8947 (IC base=+0.095)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=433)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.095)

### UPDOWN_GBM#SOL#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.524` → IC=+0.140 (n=73)

  - _Acción_: Kelly boost +0.70€ cuando `sigma_ewma_delta_pct` > 8.524 (IC base=+0.007)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.384 (n=419)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1403` → IC=+0.383 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1403 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.378 (n=631)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.400 (n=628)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.1455` → IC=+0.382 (n=362)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1455 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.385 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.369 (n=764)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `10317.9078` → IC=+0.385 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10317.9078 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.365 (n=287)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0043 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.401 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.0553` → IC=+0.365 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0553 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1537` → IC=+0.381 (n=217)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1537 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.392 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.384 (n=326)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.8077` → IC=+0.390 (n=326)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8077 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.2458` → IC=+0.397 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2458 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.617` → IC=+0.379 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.617 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `15403.697` → IC=+0.393 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15403.697 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `489.0` → IC=+0.411 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 489.0 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.367 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.385 (n=137)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.379 (n=271)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.381 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.391 (n=145)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.411 (n=302)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4542` → IC=+0.380 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4542 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.365 (n=280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.861` → IC=+0.390 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.861 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3987.1822` → IC=+0.392 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3987.1822 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.366 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0068` → IC=-0.172 (n=2146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0068
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=2147)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.211 (n=1673)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2620)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.282 (n=1039)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.209 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2663` → IC=+0.198 (n=884)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` < 0.2663 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.268 (n=1186)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.361` → IC=+0.282 (n=3555)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.361 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6627` → IC=+0.281 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6627 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.217 (n=624)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1876)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.227 (n=625)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1875)

- **FILTRO** `sigma_ewma_delta_pct` > `23.271` → IC=-0.265 (n=360)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.271
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=2140)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=65)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2435)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.121 (n=748)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0052 (IC base=+0.097)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2051` → IC=+0.293 (n=153)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2051 (IC base=+0.097)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1079` → IC=+0.277 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1079 (IC base=+0.097)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.134 (n=367)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 15.0 (IC base=+0.097)

- **PATRÓN** `ibs_15` > `0.7572` → IC=+0.335 (n=337)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7572 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1051` → IC=+0.291 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1051 (IC base=+0.097)

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

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=1275)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.7675` → IC=+0.259 (n=1121)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.7675 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1581` → IC=+0.258 (n=849)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1581 (IC base=+0.245)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2768` → IC=+0.245 (n=1086)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2768 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.249 (n=913)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.247 (n=1135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3696` → IC=+0.275 (n=1274)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3696 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.6087` → IC=+0.274 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6087 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.449` → IC=+0.257 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.449 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.257 (n=335)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=656)

- **FILTRO** `drift_15min` |x|> `0.888` → IC=-0.283 (n=247)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.888
  - _Potencial_: sin este filtro IC_bueno=-0.158 (n=744)

- **FILTRO** `sigma_ewma_delta_pct` > `6.572` → IC=-0.201 (n=232)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.572
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=759)

- **FILTRO** `sigma_ewma_delta_pct` > `17.981` → IC=-0.145 (n=517)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.981
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4118)

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

- **PATRÓN** `delta_ratio_macro` |x|> `0.082` → IC=+0.236 (n=506)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.082 (IC base=-0.040)

- **PATRÓN** `ibs_15` < `0.3556` → IC=+0.290 (n=566)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3556 (IC base=-0.040)

- **PATRÓN** `dist_vwap_pct` < `0.4491` → IC=+0.242 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4491 (IC base=-0.040)

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
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.298 (n=936)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.321 (n=355)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2423` → IC=+0.309 (n=355)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2423 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2247` → IC=+0.308 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2247 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=1111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8389` → IC=+0.321 (n=1064)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8389 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2698` → IC=+0.327 (n=454)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2698 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.378 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `12348.3168` → IC=+0.312 (n=483)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 12348.3168 (IC base=+0.292)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.315 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.289)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.298 (n=260)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0046 (IC base=+0.289)

- **PATRÓN** `drift_60min` |x|≤ `0.0571` → IC=+0.314 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0571 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.314 (n=191)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.315 (n=572)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.829 (IC base=+0.289)

- **PATRÓN** `dist_vwap_pct` > `0.2552` → IC=+0.330 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2552 (IC base=+0.289)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.497` → IC=+0.383 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.497 (IC base=+0.289)

- **PATRÓN** `libro_liquidez` > `16201.6469` → IC=+0.329 (n=191)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 16201.6469 (IC base=+0.289)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0065` → IC=+0.306 (n=493)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0065 (IC base=+0.295)

- **PATRÓN** `drift_60min` |x|≤ `0.0523` → IC=+0.320 (n=165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0523 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0676` → IC=+0.298 (n=492)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0676 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2213` → IC=+0.318 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2213 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.324 (n=492)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.285` → IC=+0.328 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.285 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.52` → IC=+0.363 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.52 (IC base=+0.295)

### UPDOWN_OU_5M
- **FILTRO** `delta_ratio_macro` |x|≤ `0.1226` → IC=-0.151 (n=84)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1226
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=253)

- **FILTRO** `ballena_activa_n` > `46.0` → IC=-0.135 (n=228)

  - _Acción_: SKIP cuando `ballena_activa_n` > 46.0
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=77)

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
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.56 sube el IC de +0.179 a +0.255 en UPDOWN_GBM#15min (n=3547). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.219 a +0.285 en UPDOWN_GBM#BTC#15min (n=607). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5467 sube el IC de +0.146 a +0.245 en UPDOWN_GBM#ETH#15min (n=703). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8947 sube el IC de +0.095 a +0.251 en UPDOWN_GBM#SOL#15min (n=263). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.203 a +0.280 en UPDOWN_GBM#XRP#15min (n=811). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.157 en UPDOWN_GBM#XRP#15min (n=773). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.067 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=1039). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.361 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3555). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.097 a +0.335 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=337). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.195 a +0.287 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6098 sube el IC de +0.152 a +0.251 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=519). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3696 sube el IC de +0.245 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1274). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.190 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3556 sube el IC de -0.040 a +0.290 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=566). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.206 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=856). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.074 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.074 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8389 sube el IC de +0.292 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=1064). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.289 a +0.315 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=572). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.295 a +0.324 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=492). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.365 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=628). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8077 sube el IC de +0.365 a +0.390 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=326). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.364 a +0.411 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=302). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1923 | +0.091 | +216.55€ | 1 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1923 | +0.091 | +216.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 31 | +0.045 | -0.33€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 1533 | +0.095 | +187.60€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 1533 | +0.095 | +187.60€ | 0 | 8 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 282 | +0.070 | +11.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 282 | +0.070 | +11.51€ | 4 | 9 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 77 | +0.108 | +17.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 77 | +0.108 | +17.77€ | 0 | 7 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 628 | -0.003 | +71.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 628 | -0.003 | +71.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 457 | -0.027 | +40.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 457 | -0.027 | +40.32€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 133 | +0.070 | +23.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 133 | +0.070 | +23.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 35 | +0.013 | +3.73€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 35 | +0.013 | +3.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 39885 | -0.084 | -5025.51€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2183 | +0.031 | -251.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 37702 | -0.090 | -4774.13€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4480 | -0.116 | -773.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4480 | -0.116 | -773.00€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2183 | +0.031 | -251.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2183 | +0.031 | -251.38€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4314 | -0.105 | -874.01€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4314 | -0.105 | -874.01€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10623 | -0.024 | -995.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10623 | -0.024 | -995.41€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10509 | -0.106 | -813.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10509 | -0.106 | -813.73€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7776 | -0.136 | -1317.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7776 | -0.136 | -1317.97€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 34700 | -0.016 | +3378.74€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8977 | +0.005 | +1684.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 25723 | -0.023 | +1693.81€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 34700 | -0.016 | +3378.74€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8977 | +0.005 | +1684.93€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 25723 | -0.023 | +1693.81€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 144109 | +0.115 | -5775.19€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18538 | +0.183 | -544.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 634 | -0.019 | -69.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 116294 | +0.106 | -4837.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8643 | +0.101 | -324.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19287 | +0.108 | -1183.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19211 | +0.109 | -1183.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 27931 | +0.129 | -383.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5185 | +0.189 | -165.90€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19273 | +0.121 | -94.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3431 | +0.083 | -99.98€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19339 | +0.100 | -1346.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 72 | -0.122 | -6.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19252 | +0.101 | -1328.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 30646 | +0.125 | -555.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7940 | +0.178 | -133.81€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 19527 | +0.107 | -355.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3167 | +0.100 | -57.61€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 27599 | +0.115 | -1381.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5213 | +0.195 | -255.92€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 537 | +0.014 | -15.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 19804 | +0.095 | -943.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2045 | +0.132 | -166.73€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19307 | +0.105 | -924.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 67 | -0.080 | +6.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19227 | +0.106 | -930.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23178 | +0.197 | -1392.84€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23178 | +0.197 | -1392.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5277 | +0.179 | -449.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5277 | +0.179 | -449.66€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2930 | +0.203 | -63.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2930 | +0.203 | -63.64€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5218 | +0.181 | -412.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5218 | +0.181 | -412.39€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4528 | +0.248 | -148.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4528 | +0.248 | -148.33€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5146 | +0.188 | -332.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5146 | +0.188 | -332.57€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 81008 | +0.201 | -5777.90€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 81008 | +0.201 | -5777.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 13918 | +0.185 | -1437.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 13918 | +0.185 | -1437.37€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13085 | +0.224 | -451.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13085 | +0.224 | -451.35€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 13876 | +0.181 | -1451.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 13876 | +0.181 | -1451.84€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13156 | +0.221 | -483.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13156 | +0.221 | -483.26€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13435 | +0.202 | -875.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13435 | +0.202 | -875.13€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13538 | +0.197 | -1078.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13538 | +0.197 | -1078.95€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 30984 | +0.117 | +221.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 30984 | +0.117 | +221.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15400 | +0.120 | +182.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15400 | +0.120 | +182.67€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15584 | +0.114 | +38.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15584 | +0.114 | +38.92€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2066 | +0.292 | -10.12€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2066 | +0.292 | -10.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 946 | +0.279 | -28.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 946 | +0.279 | -28.03€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1001 | +0.297 | +12.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1001 | +0.297 | +12.60€ | 0 | 5 |
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
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 61154 | +0.100 | -1541.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4943 | +0.091 | +47.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 56211 | +0.101 | -1589.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 33654 | +0.105 | -373.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4943 | +0.091 | +47.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 28711 | +0.108 | -421.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12550 | +0.109 | -60.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12550 | +0.109 | -60.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 14950 | +0.082 | -1107.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 14950 | +0.082 | -1107.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 896 | +0.193 | -110.33€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 896 | +0.193 | -110.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 896 | +0.193 | -110.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 896 | +0.193 | -110.33€ | 2 | 4 |
| ✅ GBM_LATE_15M | 42083 | +0.094 | +21981.22€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 42083 | +0.094 | +21981.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7014 | +0.216 | +5769.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7014 | +0.216 | +5769.92€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6298 | +0.180 | +4817.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6298 | +0.180 | +4817.22€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 7521 | +0.205 | +5852.36€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7521 | +0.205 | +5852.36€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 5880 | +0.042 | +1645.86€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5880 | +0.042 | +1645.86€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 5936 | -0.032 | +1251.41€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5936 | -0.032 | +1251.41€ | 4 | 14 |
| ✅ GBM_LATE_15M#XRP | 9434 | -0.030 | +2644.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9434 | -0.030 | +2644.45€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 45284 | +0.085 | +24619.08€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 45284 | +0.085 | +24619.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8749 | +0.004 | +4417.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8749 | +0.004 | +4417.30€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9575 | +0.010 | +2265.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9575 | +0.010 | +2265.72€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6280 | +0.278 | +6732.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6280 | +0.278 | +6732.09€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8147 | +0.013 | +2014.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8147 | +0.013 | +2014.36€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7225 | +0.039 | +2977.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7225 | +0.039 | +2977.63€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5308 | +0.302 | +6211.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5308 | +0.302 | +6211.98€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 33369 | +0.180 | +27032.79€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 33369 | +0.180 | +27032.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5060 | +0.230 | +4498.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5060 | +0.230 | +4498.83€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5248 | +0.149 | +3890.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5248 | +0.149 | +3890.38€ | 0 | 22 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5346 | +0.223 | +4601.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5346 | +0.223 | +4601.59€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5662 | +0.138 | +4307.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5662 | +0.138 | +4307.19€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6271 | +0.124 | +4683.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6271 | +0.124 | +4683.09€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5782 | +0.225 | +5051.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5782 | +0.225 | +5051.72€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9006 | +0.134 | +4407.81€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9006 | +0.134 | +4407.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2683 | +0.146 | +1556.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2683 | +0.146 | +1556.63€ | 0 | 21 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2662 | +0.137 | +1259.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2662 | +0.137 | +1259.28€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2212 | +0.107 | +847.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2212 | +0.107 | +847.97€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 626 | +0.134 | +283.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 626 | +0.134 | +283.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 42247 | +0.185 | +33830.82€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 42247 | +0.185 | +33830.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6692 | +0.242 | +6242.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6692 | +0.242 | +6242.76€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6565 | +0.148 | +4509.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6565 | +0.148 | +4509.46€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7141 | +0.233 | +6383.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7141 | +0.233 | +6383.02€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6976 | +0.138 | +4983.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6976 | +0.138 | +4983.99€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7482 | +0.122 | +5182.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7482 | +0.122 | +5182.53€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7391 | +0.230 | +6529.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7391 | +0.230 | +6529.06€ | 0 | 19 |
| ✅ GBM_LATE_5M | 11653 | +0.202 | +9034.78€ | 1 | 30 |
| ✅ GBM_LATE_5M#5min | 11653 | +0.202 | +9034.78€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BNB#5min | 984 | +0.242 | +916.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 2776 | +0.208 | +2384.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 2776 | +0.208 | +2384.37€ | 0 | 26 |
| ✅ GBM_LATE_5M#DOGE | 1110 | +0.193 | +808.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#DOGE#5min | 1110 | +0.193 | +808.37€ | 0 | 19 |
| ✅ GBM_LATE_5M#ETH | 3333 | +0.193 | +2337.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 3333 | +0.193 | +2337.55€ | 0 | 27 |
| ✅ GBM_LATE_5M#SOL | 1686 | +0.190 | +1266.01€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 1686 | +0.190 | +1266.01€ | 0 | 27 |
| ✅ GBM_LATE_5M#XRP | 1764 | +0.201 | +1322.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 1764 | +0.201 | +1322.38€ | 0 | 0 |
| ✅ GBM_LATE_60M | 3440 | +0.066 | +1125.08€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3440 | +0.066 | +1125.08€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1268 | +0.081 | +463.47€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1268 | +0.081 | +463.47€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1108 | +0.068 | +387.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1108 | +0.068 | +387.75€ | 1 | 9 |
| ✅ GBM_LATE_60M#SOL | 1064 | +0.046 | +273.87€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1064 | +0.046 | +273.87€ | 0 | 14 |
| 🚫 GBM_LATE_60M_FADE | 565 | -0.246 | -25.77€ | 6 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 565 | -0.246 | -25.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 211 | -0.246 | -14.55€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 211 | -0.246 | -14.55€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 201 | -0.229 | -3.50€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 201 | -0.229 | -3.50€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 153 | -0.261 | -7.72€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 153 | -0.261 | -7.72€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1505 | +0.083 | +386.63€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1505 | +0.083 | +386.63€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 588 | +0.081 | +144.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 588 | +0.081 | +144.52€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 540 | +0.057 | +81.70€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 540 | +0.057 | +81.70€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 377 | +0.123 | +160.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 377 | +0.123 | +160.41€ | 3 | 10 |
| ✅ LATE_WINDOW_5MIN | 165 | +0.278 | +162.71€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 165 | +0.278 | +162.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 165 | +0.278 | +162.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 165 | +0.278 | +162.71€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3376 | +0.100 | +829.77€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3376 | +0.100 | +829.77€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3376 | +0.100 | +829.77€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3376 | +0.100 | +829.77€ | 0 | 1 |
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
| ✅ LIQUIDACIONES_5M | 3706 | +0.016 | +84.19€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 3706 | +0.016 | +84.19€ | 0 | 0 |
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
| ✅ LIQUIDACIONES_5M#XRP | 446 | +0.016 | +26.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 446 | +0.016 | +26.57€ | 2 | 1 |
| ✅ LIQUIDACIONES_60M | 1741 | -0.040 | -27.56€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 1741 | -0.040 | -27.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 501 | -0.029 | -10.57€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 501 | -0.029 | -10.57€ | 5 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 590 | -0.015 | +5.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 590 | -0.015 | +5.75€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 650 | -0.071 | -22.74€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 650 | -0.071 | -22.74€ | 6 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8610 | -0.028 | -7.17€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4089 | -0.036 | -83.19€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4521 | -0.020 | +76.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 260 | -0.042 | -10.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 133 | -0.026 | -1.52€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 127 | -0.058 | -9.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2142 | -0.019 | +16.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1023 | -0.024 | -3.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1119 | -0.015 | +19.78€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 949 | -0.025 | +11.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 476 | -0.042 | -12.45€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 473 | -0.007 | +24.19€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1871 | -0.043 | -66.23€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 871 | -0.054 | -58.32€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1000 | -0.033 | -7.90€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1689 | -0.020 | +27.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 803 | -0.033 | -6.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 886 | -0.009 | +33.97€ | 0 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 49388 | -0.001 | +2430.10€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 49388 | -0.001 | +2430.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8902 | +0.026 | +1124.95€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8902 | +0.026 | +1124.95€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7118 | -0.034 | -108.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7118 | -0.034 | -108.59€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9008 | +0.024 | +932.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9008 | +0.024 | +932.33€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6964 | -0.048 | -152.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6964 | -0.048 | -152.48€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8350 | -0.005 | +232.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8350 | -0.005 | +232.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9046 | +0.015 | +401.40€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9046 | +0.015 | +401.40€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6620 | -0.060 | -163.28€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6620 | -0.060 | -163.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1721 | -0.079 | -46.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1721 | -0.079 | -46.32€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 54 | -0.054 | -2.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 54 | -0.054 | -2.38€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 774 | -0.120 | -33.46€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 774 | -0.120 | -33.46€ | 5 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 1989 | -0.075 | -40.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 1989 | -0.075 | -40.31€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 122543 | -0.076 | +1599.37€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 122543 | -0.076 | +1599.37€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 21305 | -0.077 | +1084.56€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 21305 | -0.077 | +1084.56€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18461 | -0.100 | -985.23€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18461 | -0.100 | -985.23€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 21605 | -0.067 | +1141.04€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 21605 | -0.067 | +1141.04€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 18005 | -0.097 | -620.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 18005 | -0.097 | -620.69€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 21944 | -0.057 | +311.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 21944 | -0.057 | +311.82€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21223 | -0.066 | +667.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21223 | -0.066 | +667.86€ | 4 | 0 |
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
| ✅ ORDER_FLOW_5M_REACTIVO | 1436 | -0.012 | -9.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1436 | -0.012 | -9.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 282 | +0.000 | +9.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 282 | +0.000 | +9.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 243 | -0.010 | +3.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 243 | -0.010 | +3.13€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 372 | -0.043 | -27.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 372 | -0.043 | -27.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 306 | +0.013 | +4.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 306 | +0.013 | +4.70€ | 0 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE | 1125 | -0.207 | -69.66€ | 4 | 0 |
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
| ✅ STREAK_MOM_5M | 10838 | +0.017 | +94.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10838 | +0.017 | +94.48€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2772 | +0.021 | +28.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2772 | +0.021 | +28.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2821 | +0.019 | +38.17€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2821 | +0.019 | +38.17€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2357 | +0.018 | +28.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2357 | +0.018 | +28.46€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9839 | +0.013 | -49.59€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9839 | +0.013 | -49.59€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4000 | +0.017 | -9.10€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4000 | +0.017 | -9.10€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3616 | +0.011 | -27.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3616 | +0.011 | -27.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2223 | +0.009 | -13.36€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2223 | +0.009 | -13.36€ | 1 | 0 |
| ✅ UPDOWN_GBM | 75985 | +0.053 | +6689.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 18896 | +0.083 | +4144.30€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2445 | +0.004 | +23.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 49908 | +0.050 | +2436.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4470 | +0.007 | +86.32€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 16300 | +0.055 | +1391.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2441 | +0.089 | +591.59€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 655 | +0.010 | +10.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11116 | +0.061 | +726.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1992 | +0.004 | +60.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 96 | -0.071 | +2.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8387 | +0.069 | +885.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6754 | +0.051 | +276.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 17405 | +0.044 | +1126.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4471 | +0.065 | +653.17€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 639 | +0.005 | +16.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10639 | +0.044 | +435.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1567 | +0.012 | +18.86€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 89 | -0.104 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 16646 | +0.032 | +802.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4695 | +0.034 | +386.86€ | 0 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 608 | -0.008 | +0.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10353 | +0.037 | +413.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 911 | +0.006 | +6.76€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 79 | -0.130 | -4.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10394 | +0.064 | +1409.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4158 | +0.101 | +1203.64€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5848 | +0.041 | +205.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 264 | -0.102 | +1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 836 | +0.365 | +308.53€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 836 | +0.365 | +308.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 434 | +0.365 | +153.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 434 | +0.365 | +153.12€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 402 | +0.364 | +155.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 402 | +0.364 | +155.41€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19712 | -0.025 | +4628.65€ | 2 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19712 | -0.025 | +4628.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3497 | -0.112 | +136.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3497 | -0.112 | +136.29€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2389 | +0.218 | +1564.30€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2389 | +0.218 | +1564.30€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5626 | -0.066 | +671.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5626 | -0.066 | +671.77€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5534 | -0.065 | +983.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5534 | -0.065 | +983.03€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 227 | +0.042 | +9.93€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 227 | +0.042 | +9.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 227 | +0.042 | +9.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 227 | +0.042 | +9.93€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1418 | +0.292 | +1213.35€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1418 | +0.292 | +1213.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 762 | +0.289 | +616.78€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 762 | +0.289 | +616.78€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 656 | +0.295 | +596.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 656 | +0.295 | +596.57€ | 0 | 9 |
| ✅ UPDOWN_OU_5M | 815 | -0.112 | -83.16€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#5min | 815 | -0.112 | -83.16€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 311 | -0.078 | -35.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 311 | -0.078 | -35.51€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 248 | -0.080 | -18.10€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 248 | -0.080 | -18.10€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 34 | -0.194 | -7.23€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 34 | -0.194 | -7.23€ | 5 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 87 | -0.163 | -9.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 87 | -0.163 | -9.15€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 97 | -0.187 | -6.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 97 | -0.187 | -6.55€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 38 | -0.175 | -6.61€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 3610 | +0.303 | +1706.47€ | 0 | 4 |
| ✅ WEEKLY_PRICE#BTC | 1328 | +0.255 | +162.57€ | 0 | 4 |
| ✅ WEEKLY_PRICE#ETH | 1388 | +0.298 | +621.15€ | 0 | 4 |
| ✅ WEEKLY_PRICE#SOL | 894 | +0.380 | +922.75€ | 0 | 1 |
## Hipótesis pendientes — tracking automático


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.043) — sin ventaja clara. oversold(IBS<0.3): IC=+0.064 n=26398 | neutral: IC=+0.057 n=28023 | overbought(IBS>0.7): IC=+0.099 n=26886
  - _Datos_: n=84520 IC=+0.074 PNL=+12554.81€

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 710 celda(s) pasan gate riguroso completo de 2685 evaluadas (n>=40) y 3733 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.034 < 0.08 — monitorear
  - _Datos_: n=4695 IC=+0.034 PNL=+386.86€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=1388/15 IC=+0.298 PNL=+621.15€ | BTC: n=1328/15 IC=+0.255 PNL=+162.57€ | SOL: n=894/15 IC=+0.380 PNL=+922.75€

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 31 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH#60min, UPDOWN_GBM#ETH, UPDOWN_GBM#60min, UPDOWN_GBM#BTC#60min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: 15
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Falta 11 ops más en GBM@18h (IC actual=-0.067)
  - _Datos_: n=4 IC=-0.067 PNL=-3.02€

**⏳ H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: 75923 ops, 22 horas distintas. Sin hora con n≥15 y IC extremo aún.

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.139 n=779/60 | contraria IC=+0.191 n=807 | gap=-0.052 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=465, boost estimado=+0.016. Necesita 0 más y boost>0.05

**⏳ H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 0/50 ops con delta_ratio feature | SOL: 272 ops con delta_ratio

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=1567/40 IC=+0.012 PNL=+18.86€ | BTC#60min: n=1992/40 IC=+0.004 PNL=+60.71€ | SOL#60min: n=911/40 IC=+0.006 PNL=+6.76€

**⏳ H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.048 n=551644 | tras_1loss IC=+0.095 n=419437 | tras_2loss IC=+0.064 n=169859/40 | gap=-0.016 (umbral 0.05)

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.036 n=10602 | contrario_BTC IC=+0.052 n=9292/40 | gap=+0.016 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.205 > 0.08 con n=738 PNL=+573.26€
  - _Datos_: n=738 IC=+0.205 PNL=+573.26€

**🟡 H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.171 > 0.08 con n=834 PNL=+479.60€
  - _Datos_: n=834 IC=+0.171 PNL=+479.60€

**🟡 H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.182 > 0.08 con n=61 PNL=+35.11€
  - _Datos_: n=61 IC=+0.182 PNL=+35.11€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.333 > 0.1 con n=2947 PNL=+1641.30€
  - _Datos_: n=2947 IC=+0.333 PNL=+1641.30€

**〰️ H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: n=687 IC=+0.073 PNL=+79.19€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=687 IC=+0.073 PNL=+79.19€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=84 IC=+0.198 PNL=+61.01€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=84 IC=+0.198 PNL=+61.01€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=71993 IC=+0.053 PNL=+6396.74€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=71993 IC=+0.053 PNL=+6396.74€

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
  - _Estado_: n=3007 IC=+0.009 PNL=+9.44€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=3007 IC=+0.009 PNL=+9.44€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=1463 IC=+0.003 PNL=+76.88€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=1463 IC=+0.003 PNL=+76.88€

**〰️ H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: n=949 IC=+0.019 PNL=+33.50€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=949 IC=+0.019 PNL=+33.50€

**🟡 H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.1 con n=4729 PNL=+2983.27€
  - _Datos_: n=4729 IC=+0.179 PNL=+2983.27€

**〰️ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: n=2912 IC=+0.068 PNL=+220.16€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2912 IC=+0.068 PNL=+220.16€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=2441 IC=+0.089 PNL=+591.59€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=2441 IC=+0.089 PNL=+591.59€

**⏳ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: 50
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: 0/50 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)
  - _Bloqueante_: FILTRO_YA_IMPLEMENTADO: confirmada 2026-07-01 (IC=-0.037 n=52) e implementada en shadow_predict.py (skip si drift_15min∈[-0.3,0.3)) -- verificado 26-Ago con 2177 filas post-TWAP reales, 0 caen en la zona filtrada. Frozen by design, no falta n

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.098 > 0.08 con n=10881 PNL=+3066.87€
  - _Datos_: n=10881 IC=+0.098 PNL=+3066.87€

**〰️ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: n=349 IC=-0.227 PNL=-0.07€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=349 IC=-0.227 PNL=-0.07€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=429 IC=-0.024 PNL=-9.53€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=429 IC=-0.024 PNL=-9.53€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=973 IC=+0.038 PNL=+92.91€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=973 IC=+0.038 PNL=+92.91€

**〰️ H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: n=118 IC=+0.017 PNL=+1.99€ — sin señal clara aún (umbral IC: min=None max=-0.08)
  - _Datos_: n=118 IC=+0.017 PNL=+1.99€

**〰️ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: n=8338 IC=+0.019 PNL=+197.47€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=8338 IC=+0.019 PNL=+197.47€

**🟡 H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=347 PNL=+77.46€
  - _Datos_: n=347 IC=+0.122 PNL=+77.46€

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.278 n=165) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=165 IC=+0.278 PNL=+162.71€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=12568 IC=+0.051 PNL=+1050.79€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=12568 IC=+0.051 PNL=+1050.79€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=4516 IC=+0.064 PNL=+662.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4516 IC=+0.064 PNL=+662.28€

**🟡 H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.106 > 0.08 con n=539 PNL=+165.78€
  - _Datos_: n=539 IC=+0.106 PNL=+165.78€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.150 > 0.08 con n=1139 PNL=+322.70€
  - _Datos_: n=1139 IC=+0.150 PNL=+322.70€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.104 > 0.08 con n=889 PNL=+451.98€
  - _Datos_: n=889 IC=+0.104 PNL=+451.98€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=64364 IC=+0.118 PNL=+23936.47€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=64364 IC=+0.118 PNL=+23936.47€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=1792 IC=+0.109 PNL=+195.82€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=1792 IC=+0.109 PNL=+195.82€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=11416 IC=+0.057 PNL=+1119.80€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=11416 IC=+0.057 PNL=+1119.80€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.125 > 0.02 con n=964 PNL=+404.19€
  - _Datos_: n=964 IC=+0.125 PNL=+404.19€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=213 IC=-0.091 PNL=+19.65€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=213 IC=-0.091 PNL=+19.65€

**〰️ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: n≥25 y IC<-0.10 para confirmar (evidencia inicial es de solo 3 ops)
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: n=81 IC=-0.030 PNL=+3.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=81 IC=-0.030 PNL=+3.88€

**🟡 H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: n≥25 y IC>+0.10 para confirmar
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.449 > 0.1 con n=1647 PNL=+1599.92€
  - _Datos_: n=1647 IC=+0.449 PNL=+1599.92€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=29790 IC=+0.074 PNL=+4329.47€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=29790 IC=+0.074 PNL=+4329.47€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.209 > 0.1 con n=6701 PNL=+4021.21€
  - _Datos_: n=6701 IC=+0.209 PNL=+4021.21€

**🔴 H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.141 < -0.1 con n=480 PNL=+55.02€
  - _Datos_: n=480 IC=-0.141 PNL=+55.02€

**〰️ H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: n=3078 IC=+0.066 PNL=+373.70€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=3078 IC=+0.066 PNL=+373.70€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=142 IC=-0.090 PNL=+6.55€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=142 IC=-0.090 PNL=+6.55€

**🟡 H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.111 > 0.1 con n=798 PNL=+214.28€
  - _Datos_: n=798 IC=+0.111 PNL=+214.28€

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
  - _Estado_: n=31740 IC=-0.134 PNL=+2520.11€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=31740 IC=-0.134 PNL=+2520.11€

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
  - _Estado_: n=3173 IC=+0.133 PNL=+1946.80€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=3173 IC=+0.133 PNL=+1946.80€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.207 > 0.08 con n=4078 PNL=+3000.65€
  - _Datos_: n=4078 IC=+0.207 PNL=+3000.65€

**〰️ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: n=7800 IC=+0.048 PNL=+591.17€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=7800 IC=+0.048 PNL=+591.17€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.095 > 0.08 con n=3421 PNL=+1866.76€
  - _Datos_: n=3421 IC=+0.095 PNL=+1866.76€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.218 > 0.08 con n=807 PNL=+477.29€
  - _Datos_: n=807 IC=+0.218 PNL=+477.29€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.222 < -0.1 con n=3296 PNL=-252.36€
  - _Datos_: n=3296 IC=-0.222 PNL=-252.36€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.209 > 0.2 con n=8662 PNL=+6834.80€
  - _Datos_: n=8662 IC=+0.209 PNL=+6834.80€

**🟡 H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: n≥40 en cada rama (contrario y alineado) para separar señal de ruido
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.124 > 0.08 con n=123 PNL=+55.78€
  - _Datos_: n=123 IC=+0.124 PNL=+55.78€

**🟡 H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.080 > 0.08 con n=3168 PNL=+1101.13€
  - _Datos_: n=3168 IC=+0.080 PNL=+1101.13€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.179 > 0.08 con n=2921 PNL=+2225.72€
  - _Datos_: n=2921 IC=+0.179 PNL=+2225.72€

**〰️ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: n=4932 IC=-0.025 PNL=+1389.10€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=4932 IC=-0.025 PNL=+1389.10€

**〰️ H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: n=678 IC=+0.079 PNL=-45.33€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=678 IC=+0.079 PNL=-45.33€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.243 > 0.08 con n=4765 PNL=-375.65€
  - _Datos_: n=4765 IC=+0.243 PNL=-375.65€

**〰️ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: n>=40 y IC>0.08
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: n=67 IC=+0.007 PNL=+4.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=67 IC=+0.007 PNL=+4.82€

**🔶 H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: SEÑAL POSITIVA en XRP (IC=+0.100 n=1716) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=1716 IC=+0.100 PNL=+372.84€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.313 > 0.08 con n=448 PNL=+131.39€
  - _Datos_: n=448 IC=+0.313 PNL=+131.39€

**🔶 H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: bucket [0.45,0.55) con n>=200 y split-half consistente en ambas mitades antes de considerar promocion
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: SEÑAL POSITIVA en SOL (IC=+0.414 n=566) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=566 IC=+0.414 PNL=+816.00€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=13918 IC=+0.185 PNL=-1437.37€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=13918 IC=+0.185 PNL=-1437.37€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.217 > 0.1 con n=228 PNL=+149.22€
  - _Datos_: n=228 IC=+0.217 PNL=+149.22€
