# Hipótesis automáticas — 2026-10-19 23:51 UTC
_Generado por shadow_postmortem.py sobre 972022 resoluciones (PNL=+126406.97€)_

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
- **FILTRO** `restante_s_al_confirmar` < `142.38` → IC=-0.206 (n=9974)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 142.38
  - _Potencial_: sin este filtro IC_bueno=-0.042 (n=29924)

### BALLENAS_TARDIAS#BNB#5min
- **FILTRO** `restante_s_al_confirmar` < `128.98` → IC=-0.263 (n=1120)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 128.98
  - _Potencial_: sin este filtro IC_bueno=-0.067 (n=3360)

### BALLENAS_TARDIAS#DOGE#5min
- **FILTRO** `restante_s_al_confirmar` < `121.5` → IC=-0.287 (n=1078)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 121.5
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=3237)

### BALLENAS_TARDIAS#SOL#5min
- **FILTRO** `restante_s_al_confirmar` < `167.21` → IC=-0.208 (n=2628)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 167.21
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=7884)

### BALLENAS_TARDIAS#XRP#5min
- **FILTRO** `restante_s_al_confirmar` < `133.32` → IC=-0.279 (n=1945)

  - _Acción_: SKIP cuando `restante_s_al_confirmar` < 133.32
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=5836)

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
- **PATRÓN** `py_entrada` > `0.68` → IC=+0.213 (n=21472)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.68 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.136 (n=4302)

  - _Acción_: Kelly boost +0.68€ cuando `libro_spread` < 0.01 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `9149.9865` → IC=+0.178 (n=1940)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 9149.9865 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.130 (n=18283)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.129 (n=32612)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 11.0 (IC base=+0.126)

- **PATRÓN** `py_entrada` < `0.35` → IC=+0.227 (n=16991)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.35 (IC base=+0.126)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.150 (n=7159)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.01 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7120.5951` → IC=+0.159 (n=2766)

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

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.190 (n=1783)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 7.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.188 (n=1980)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 17.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.340 (n=659)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.184)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.186 (n=2541)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `16148.5591` → IC=+0.194 (n=655)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 16148.5591 (IC base=+0.184)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `py_entrada` > `0.61` → IC=+0.169 (n=469)

  - _Acción_: Kelly boost +0.84€ cuando `py_entrada` > 0.61 (IC base=+0.081)

- **PATRÓN** `libro_liquidez` > `6860.5651` → IC=+0.172 (n=123)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 6860.5651 (IC base=+0.081)

- **PATRÓN** `py_entrada` < `0.44` → IC=+0.139 (n=1109)

  - _Acción_: Kelly boost +0.70€ cuando `py_entrada` < 0.44 (IC base=+0.085)

### FAVORITO_CONFIRMADO#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=171)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.168 (n=4171)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 5.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.161 (n=2838)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 12.0 (IC base=+0.161)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.371 (n=1358)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.220 (n=1852)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` < `0.26` → IC=+0.360 (n=669)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.26 (IC base=+0.212)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=2168)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.212)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=1052)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.149 (n=681)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.67` → IC=+0.263 (n=339)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.67 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.142 (n=826)

  - _Acción_: Kelly boost +0.71€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `1879.9984` → IC=+0.153 (n=670)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1879.9984 (IC base=+0.142)

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

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.206 (n=18150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.202 (n=15336)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.234 (n=7480)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.201)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.337 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `4837.3339` → IC=+0.337 (n=256)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4837.3339 (IC base=+0.201)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.182 (n=3961)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.181 (n=4160)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 18.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` < `0.73` → IC=+0.182 (n=4081)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.73 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.180 (n=3419)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.71 (IC base=+0.179)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.380 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=89)

- **FILTRO** `py_entrada` > `0.805` → IC=-0.417 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.805
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=90)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.224 (n=2129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.228 (n=2224)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.73` → IC=+0.306 (n=747)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.73 (IC base=+0.223)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.188 (n=4116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 5.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.184 (n=3488)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 15.0 (IC base=+0.182)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.187 (n=3224)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.71 (IC base=+0.182)

### FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.258 (n=3573)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.248)

- **PATRÓN** `py_entrada` > `0.79` → IC=+0.361 (n=1142)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.194 (n=4037)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 5.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.191 (n=3439)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 15.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.193 (n=2976)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.71 (IC base=+0.188)

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

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.212 (n=20267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.247 (n=23721)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.202)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.195 (n=3500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.188 (n=7480)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.71` → IC=+0.201 (n=10528)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.71 (IC base=+0.185)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.228 (n=4923)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.226 (n=4801)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.224)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.285 (n=3442)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.224)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.191 (n=4041)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.74` → IC=+0.212 (n=5370)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.74 (IC base=+0.181)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min
- **FILTRO** `py_entrada` < `0.835` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.835
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.232 (n=4960)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=3750)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.278 (n=3347)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.222)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=9024)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.262 (n=3487)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.203)

### FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=3922)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.197)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.199 (n=3919)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 6.0 (IC base=+0.197)

- **PATRÓN** `py_entrada` > `0.75` → IC=+0.248 (n=4082)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.75 (IC base=+0.197)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.191 (n=8523)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.38 (IC base=+0.117)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.140 (n=8363)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` > 4.96 (IC base=+0.117)

- **PATRÓN** `lag_apertura_s` < `3.78` → IC=+0.136 (n=10247)

  - _Acción_: Kelly boost +0.68€ cuando `lag_apertura_s` < 3.78 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=4216)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.120)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.143 (n=4263)

  - _Acción_: Kelly boost +0.72€ cuando `restante_min` > 4.95 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.131 (n=4469)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.120)

- **PATRÓN** `lag_apertura_s` < `2.77` → IC=+0.147 (n=3858)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 2.77 (IC base=+0.120)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.188 (n=4307)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.38 (IC base=+0.114)

- **PATRÓN** `restante_min` > `4.96` → IC=+0.135 (n=4559)

  - _Acción_: Kelly boost +0.67€ cuando `restante_min` > 4.96 (IC base=+0.114)

- **PATRÓN** `lag_apertura_s` < `3.33` → IC=+0.133 (n=5153)

  - _Acción_: Kelly boost +0.67€ cuando `lag_apertura_s` < 3.33 (IC base=+0.114)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.300 (n=1646)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.292 (n=1621)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.292)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.381 (n=569)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.292)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.286 (n=747)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.279)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.354 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.279)

- **PATRÓN** `libro_liquidez` > `5007.5546` → IC=+0.287 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5007.5546 (IC base=+0.279)

### FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.322 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.297)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.300 (n=780)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.297)

- **PATRÓN** `py_entrada` > `0.815` → IC=+0.391 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.815 (IC base=+0.297)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.297 (n=883)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.445 (n=762)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.441)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.442 (n=752)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.441)

- **PATRÓN** `py_entrada` > `0.925` → IC=+0.445 (n=526)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.925 (IC base=+0.441)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.442 (n=865)

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
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.453 (n=359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.449)

- **PATRÓN** `py_entrada` < `0.935` → IC=+0.451 (n=347)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.935 (IC base=+0.449)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.450 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.449)

- **PATRÓN** `libro_liquidez` > `1978.5089` → IC=+0.468 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1978.5089 (IC base=+0.449)

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
- **PATRÓN** `drift_60min` |x|≤ `0.4776` → IC=+0.138 (n=13172)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4776 (IC base=+0.121)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.124 (n=13346)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 6.0 (IC base=+0.121)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=9169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.121)

- **PATRÓN** `ibs_20min` > `0.9808` → IC=+0.248 (n=4391)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9808 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` > `0.783` → IC=+0.267 (n=727)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.783 (IC base=+0.121)

- **PATRÓN** `dist_vwap_pct` < `0.3703` → IC=+0.258 (n=3707)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3703 (IC base=+0.121)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.926` → IC=+0.190 (n=4986)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 5.926 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` < `1.2004` → IC=+0.258 (n=3817)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2004 (IC base=+0.121)

- **PATRÓN** `volumen_regimen` > `0.6206` → IC=+0.263 (n=3816)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6206 (IC base=+0.121)

- **PATRÓN** `volumen_pendiente_norm` > `0.3024` → IC=+0.239 (n=1337)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3024 (IC base=+0.121)

- **PATRÓN** `volumen_spike_ratio` > `2.3416` → IC=+0.227 (n=4244)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.3416 (IC base=+0.121)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.122 (n=16222)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.04 (IC base=+0.121)

- **PATRÓN** `ibs_20min` < `0.6857` → IC=+0.129 (n=18420)

  - _Acción_: Kelly boost +0.64€ cuando `ibs_20min` < 0.6857 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` < `0.1531` → IC=+0.187 (n=5959)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.1531 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` < `0.6961` → IC=+0.185 (n=2773)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_regimen` < 0.6961 (IC base=+0.075)

- **PATRÓN** `volumen_regimen` > `1.0498` → IC=+0.181 (n=2856)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_regimen` > 1.0498 (IC base=+0.075)

- **PATRÓN** `volumen_pendiente_norm` > `0.2958` → IC=+0.231 (n=1572)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2958 (IC base=+0.075)

- **PATRÓN** `volumen_spike_ratio` > `2.6796` → IC=+0.207 (n=3570)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6796 (IC base=+0.075)

- **PATRÓN** `ballena_activa_n` < `106.0` → IC=+0.220 (n=10567)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 106.0 (IC base=+0.075)

### GBM_LATE_15M#BNB#15min
- **PATRÓN** `sigma_h` < `0.005` → IC=+0.213 (n=960)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.005 (IC base=+0.198)

- **PATRÓN** `drift_60min` |x|≤ `0.3473` → IC=+0.202 (n=2869)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3473 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.210 (n=1399)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.198)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.203 (n=1914)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.198)

- **PATRÓN** `ibs_20min` > `0.9803` → IC=+0.280 (n=1301)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9803 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.941` → IC=+0.281 (n=1258)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.941 (IC base=+0.198)

- **PATRÓN** `volumen_pendiente_norm` > `0.2332` → IC=+0.248 (n=506)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2332 (IC base=+0.198)

- **PATRÓN** `volumen_spike_ratio` > `1.4375` → IC=+0.200 (n=2732)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4375 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.213 (n=3066)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `2079.88` → IC=+0.206 (n=956)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2079.88 (IC base=+0.198)

- **PATRÓN** `ballena_activa_n` < `14.0` → IC=+0.216 (n=1705)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 14.0 (IC base=+0.198)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=2399)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.240 (n=1089)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.237)

- **PATRÓN** `drift_60min` |x|≤ `0.0873` → IC=+0.271 (n=803)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0873 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.254 (n=879)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.237)

- **PATRÓN** `ibs_20min` < `0.5263` → IC=+0.258 (n=2399)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5263 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` < `0.0941` → IC=+0.239 (n=2148)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0941 (IC base=+0.237)

- **PATRÓN** `volumen_pendiente_norm` > `0.287` → IC=+0.259 (n=322)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.287 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` < `1.4411` → IC=+0.242 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4411 (IC base=+0.237)

- **PATRÓN** `volumen_spike_ratio` > `2.6588` → IC=+0.246 (n=753)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6588 (IC base=+0.237)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.240 (n=2689)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.237)

- **PATRÓN** `libro_liquidez` > `1650.5605` → IC=+0.244 (n=2142)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1650.5605 (IC base=+0.237)

- **PATRÓN** `ballena_activa_n` < `7.0` → IC=+0.240 (n=791)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 7.0 (IC base=+0.237)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.237 (n=1038)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0031 (IC base=+0.227)

- **PATRÓN** `sigma_h` > `0.005` → IC=+0.230 (n=1068)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.005 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.106` → IC=+0.260 (n=1032)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.106 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.238 (n=2466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.227)

- **PATRÓN** `ibs_20min` > `0.9509` → IC=+0.277 (n=782)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9509 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.1289` → IC=+0.234 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1289 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.355` → IC=+0.265 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.355 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` < `1.231` → IC=+0.230 (n=2346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.231 (IC base=+0.227)

- **PATRÓN** `volumen_regimen` > `0.6226` → IC=+0.232 (n=2346)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6226 (IC base=+0.227)

- **PATRÓN** `volumen_pendiente_norm` > `0.2765` → IC=+0.261 (n=333)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2765 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` < `1.5085` → IC=+0.228 (n=1017)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5085 (IC base=+0.227)

- **PATRÓN** `volumen_spike_ratio` > `2.4423` → IC=+0.253 (n=770)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.4423 (IC base=+0.227)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.151 (n=2385)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0057 (IC base=+0.133)

- **PATRÓN** `drift_60min` |x|≤ `0.0752` → IC=+0.169 (n=795)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.0752 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.146 (n=1588)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 12.0 (IC base=+0.133)

- **PATRÓN** `ibs_20min` < `0.7285` → IC=+0.176 (n=2383)

  - _Acción_: Kelly boost +0.88€ cuando `ibs_20min` < 0.7285 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.038` → IC=+0.147 (n=386)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 11.038 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.197` → IC=+0.141 (n=2176)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 4.197 (IC base=+0.133)

- **PATRÓN** `volumen_regimen` < `1.2032` → IC=+0.140 (n=2383)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 1.2032 (IC base=+0.133)

- **PATRÓN** `volumen_pendiente_norm` > `0.0967` → IC=+0.159 (n=870)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_pendiente_norm` > 0.0967 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` < `2.4538` → IC=+0.142 (n=2263)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_spike_ratio` < 2.4538 (IC base=+0.133)

- **PATRÓN** `volumen_spike_ratio` > `1.4138` → IC=+0.136 (n=2262)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4138 (IC base=+0.133)

- **PATRÓN** `ballena_activa_n` < `218.0` → IC=+0.174 (n=967)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 218.0 (IC base=+0.133)

### GBM_LATE_15M#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.215 (n=1351)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=3132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.195)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.272 (n=1137)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.27` → IC=+0.275 (n=628)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.27 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` < `0.0974` → IC=+0.200 (n=2640)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0974 (IC base=+0.195)

- **PATRÓN** `volumen_pendiente_norm` > `0.352` → IC=+0.210 (n=384)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.352 (IC base=+0.195)

- **PATRÓN** `volumen_spike_ratio` > `2.6919` → IC=+0.210 (n=1310)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6919 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.202 (n=3558)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `1977.9684` → IC=+0.201 (n=1351)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1977.9684 (IC base=+0.195)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.223 (n=2348)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.217)

- **PATRÓN** `drift_60min` |x|≤ `0.6031` → IC=+0.222 (n=2666)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.6031 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.241 (n=1003)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `ibs_20min` < `0.0164` → IC=+0.276 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0164 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.409` → IC=+0.245 (n=324)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.409 (IC base=+0.217)

- **PATRÓN** `volumen_pendiente_norm` > `0.3479` → IC=+0.257 (n=380)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3479 (IC base=+0.217)

- **PATRÓN** `volumen_spike_ratio` > `2.73` → IC=+0.229 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.73 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.218 (n=1393)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2054.498` → IC=+0.224 (n=889)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2054.498 (IC base=+0.217)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.220 (n=2179)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 24.0 (IC base=+0.217)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.140 (n=148)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.042 (n=3613)

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.162 (n=533)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0036 (IC base=+0.053)

- **PATRÓN** `ibs_20min` > `0.9547` → IC=+0.228 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9547 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` > `0.14` → IC=+0.329 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.14 (IC base=+0.053)

- **PATRÓN** `dist_vwap_pct` < `0.19` → IC=+0.329 (n=476)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.19 (IC base=+0.053)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.12` → IC=+0.187 (n=1145)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.12 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` < `0.8561` → IC=+0.335 (n=398)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8561 (IC base=+0.053)

- **PATRÓN** `volumen_regimen` > `1.2207` → IC=+0.346 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2207 (IC base=+0.053)

- **PATRÓN** `volumen_pendiente_norm` > `0.2985` → IC=+0.348 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2985 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` < `1.4099` → IC=+0.346 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4099 (IC base=+0.053)

- **PATRÓN** `volumen_spike_ratio` > `2.2171` → IC=+0.326 (n=263)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2171 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `132.0` → IC=+0.337 (n=514)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 132.0 (IC base=+0.053)

- **PATRÓN** `ibs_20min` < `0.0931` → IC=+0.173 (n=941)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` < 0.0931 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` > `0.3253` → IC=+0.141 (n=446)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.3253 (IC base=+0.035)

- **PATRÓN** `dist_vwap_pct` < `0.13` → IC=+0.136 (n=1538)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.13 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` < `0.8417` → IC=+0.148 (n=1114)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_regimen` < 0.8417 (IC base=+0.035)

- **PATRÓN** `volumen_regimen` > `1.1677` → IC=+0.135 (n=557)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` > 1.1677 (IC base=+0.035)

- **PATRÓN** `volumen_pendiente_norm` > `0.2857` → IC=+0.200 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2857 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` < `1.7767` → IC=+0.138 (n=1066)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_spike_ratio` < 1.7767 (IC base=+0.035)

- **PATRÓN** `volumen_spike_ratio` > `2.1545` → IC=+0.151 (n=725)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` > 2.1545 (IC base=+0.035)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=550)

- **FILTRO** `ibs_20min` < `0.2727` → IC=-0.191 (n=163)

  - _Acción_: SKIP cuando `ibs_20min` < 0.2727
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=490)

- **FILTRO** `ibs_20min` > `0.2174` → IC=-0.132 (n=3539)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2174
  - _Potencial_: sin este filtro IC_bueno=+0.148 (n=1748)

- **FILTRO** `sigma_ewma_delta_pct` > `8.665` → IC=-0.239 (n=554)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.665
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=4733)

- **PATRÓN** `ibs_20min` > `0.7857` → IC=+0.180 (n=223)

  - _Acción_: Kelly boost +0.90€ cuando `ibs_20min` > 0.7857 (IC base=+0.031)

- **PATRÓN** `dist_vwap_pct` > `1.0156` → IC=+0.273 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0156 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.146` → IC=+0.146 (n=207)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 3.146 (IC base=+0.031)

- **PATRÓN** `volumen_regimen` > `1.0155` → IC=+0.303 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0155 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` < `0.1553` → IC=+0.276 (n=230)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1553 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `2.5549` → IC=+0.279 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.5549 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `1.5481` → IC=+0.258 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.5481 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.2174` → IC=+0.148 (n=1748)

  - _Acción_: Kelly boost +0.74€ cuando `ibs_20min` < 0.2174 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` > `0.2659` → IC=+0.276 (n=226)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2659 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4351` → IC=+0.276 (n=814)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4351 (IC base=-0.039)

- **PATRÓN** `volumen_regimen` < `0.7007` → IC=+0.301 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7007 (IC base=-0.039)

- **PATRÓN** `volumen_pendiente_norm` > `0.0806` → IC=+0.302 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0806 (IC base=-0.039)

- **PATRÓN** `volumen_spike_ratio` < `2.4232` → IC=+0.299 (n=661)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4232 (IC base=-0.039)

### GBM_LATE_15M#XRP#15min
- **FILTRO** `drift_60min` |x|> `0.6131` → IC=-0.179 (n=965)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6131
  - _Potencial_: sin este filtro IC_bueno=-0.028 (n=2898)

- **FILTRO** `ibs_20min` < `0.75` → IC=-0.150 (n=2547)

  - _Acción_: SKIP cuando `ibs_20min` < 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=1316)

- **FILTRO** `libro_spread` > `0.03` → IC=-0.161 (n=957)

  - _Acción_: SKIP cuando `libro_spread` > 0.03
  - _Potencial_: sin este filtro IC_bueno=-0.035 (n=2906)

- **FILTRO** `ibs_20min` > `0.75` → IC=-0.203 (n=1393)

  - _Acción_: SKIP cuando `ibs_20min` > 0.75
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=4184)

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

- **PATRÓN** `dist_vwap_pct` > `0.8089` → IC=+0.275 (n=251)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8089 (IC base=-0.006)

- **PATRÓN** `volumen_regimen` > `1.0691` → IC=+0.283 (n=691)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0691 (IC base=-0.006)

- **PATRÓN** `volumen_pendiente_norm` > `0.1044` → IC=+0.282 (n=531)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1044 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` < `2.1859` → IC=+0.261 (n=1233)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.1859 (IC base=-0.006)

- **PATRÓN** `volumen_spike_ratio` > `1.4315` → IC=+0.263 (n=1401)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4315 (IC base=-0.006)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0098` → IC=+0.207 (n=5780)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0098 (IC base=+0.096)

- **PATRÓN** `ibs_20min` > `0.3218` → IC=+0.168 (n=17315)

  - _Acción_: Kelly boost +0.84€ cuando `ibs_20min` > 0.3218 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.953` → IC=+0.297 (n=1262)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.953 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.606` → IC=+0.161 (n=7770)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 3.606 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` < `1.1691` → IC=+0.263 (n=6376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1691 (IC base=+0.096)

- **PATRÓN** `volumen_regimen` > `0.6886` → IC=+0.268 (n=5696)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6886 (IC base=+0.096)

- **PATRÓN** `volumen_pendiente_norm` > `0.2399` → IC=+0.277 (n=1896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2399 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` < `1.4596` → IC=+0.261 (n=3395)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4596 (IC base=+0.096)

- **PATRÓN** `volumen_spike_ratio` > `2.6413` → IC=+0.270 (n=3394)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6413 (IC base=+0.096)

- **PATRÓN** `ballena_activa_n` < `92.0` → IC=+0.294 (n=9767)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 92.0 (IC base=+0.096)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.160 (n=5559)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0093 (IC base=+0.074)

- **PATRÓN** `ibs_20min` < `0.6591` → IC=+0.144 (n=16670)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` < 0.6591 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.24` → IC=+0.263 (n=5242)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.24 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` < `0.7056` → IC=+0.260 (n=2314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7056 (IC base=+0.074)

- **PATRÓN** `volumen_regimen` > `0.6339` → IC=+0.260 (n=5259)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6339 (IC base=+0.074)

- **PATRÓN** `volumen_pendiente_norm` > `0.295` → IC=+0.316 (n=1127)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.295 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` < `1.58` → IC=+0.288 (n=3314)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.58 (IC base=+0.074)

- **PATRÓN** `volumen_spike_ratio` > `2.2682` → IC=+0.282 (n=3415)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2682 (IC base=+0.074)

- **PATRÓN** `ballena_activa_n` < `77.0` → IC=+0.293 (n=7472)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 77.0 (IC base=+0.074)

### GBM_LATE_15M_ESPACIO_ATR#BNB#15min
- **FILTRO** `ibs_20min` < `0.3718` → IC=-0.179 (n=1569)

  - _Acción_: SKIP cuando `ibs_20min` < 0.3718
  - _Potencial_: sin este filtro IC_bueno=+0.134 (n=3190)

- **FILTRO** `ibs_20min` > `0.7424` → IC=-0.212 (n=998)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7424
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=3000)

- **FILTRO** `sigma_ewma_delta_pct` > `4.413` → IC=-0.206 (n=876)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.413
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=3122)

- **PATRÓN** `ibs_20min` > `0.9174` → IC=+0.309 (n=1190)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9174 (IC base=+0.031)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.026` → IC=+0.216 (n=846)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.026 (IC base=+0.031)

- **PATRÓN** `volumen_pendiente_norm` > `0.2294` → IC=+0.301 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2294 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` < `1.4428` → IC=+0.249 (n=519)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4428 (IC base=+0.031)

- **PATRÓN** `volumen_spike_ratio` > `2.2425` → IC=+0.272 (n=705)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2425 (IC base=+0.031)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.279 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.031)

- **PATRÓN** `ibs_20min` < `0.1633` → IC=+0.161 (n=1000)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.1633 (IC base=-0.029)

- **PATRÓN** `volumen_pendiente_norm` < `0.0734` → IC=+0.417 (n=457)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0734 (IC base=-0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.4231` → IC=+0.425 (n=172)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4231 (IC base=-0.029)

- **PATRÓN** `ballena_activa_n` < `10.0` → IC=+0.411 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 10.0 (IC base=-0.029)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.1133` → IC=+0.213 (n=858)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1133 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1937` → IC=+0.192 (n=1688)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_regimen` < 1.1937 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` > `0.6821` → IC=+0.200 (n=1507)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6821 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` < `0.0748` → IC=+0.190 (n=1551)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_pendiente_norm` < 0.0748 (IC base=+0.023)

- **PATRÓN** `volumen_pendiente_norm` > `0.2755` → IC=+0.229 (n=223)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2755 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` < `1.4247` → IC=+0.218 (n=554)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4247 (IC base=+0.023)

- **PATRÓN** `volumen_spike_ratio` > `2.4876` → IC=+0.191 (n=554)

  - _Acción_: Kelly boost +0.95€ cuando `volumen_spike_ratio` > 2.4876 (IC base=+0.023)

- **PATRÓN** `ballena_activa_n` < `274.0` → IC=+0.229 (n=1103)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 274.0 (IC base=+0.023)

- **PATRÓN** `volumen_regimen` < `1.1556` → IC=+0.226 (n=1076)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.1556 (IC base=-0.003)

- **PATRÓN** `volumen_regimen` > `0.6201` → IC=+0.235 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6201 (IC base=-0.003)

- **PATRÓN** `volumen_pendiente_norm` > `0.2731` → IC=+0.286 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2731 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` < `1.5351` → IC=+0.238 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5351 (IC base=-0.003)

- **PATRÓN** `volumen_spike_ratio` > `2.1657` → IC=+0.247 (n=465)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1657 (IC base=-0.003)

- **PATRÓN** `ballena_activa_n` < `201.0` → IC=+0.238 (n=345)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 201.0 (IC base=-0.003)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.308 (n=845)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.266)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.273 (n=2658)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.309 (n=1330)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.266)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.299` → IC=+0.302 (n=623)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.299 (IC base=+0.266)

- **PATRÓN** `volumen_pendiente_norm` < `0.0978` → IC=+0.279 (n=2198)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0978 (IC base=+0.266)

- **PATRÓN** `volumen_spike_ratio` > `1.6104` → IC=+0.272 (n=2442)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.6104 (IC base=+0.266)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.277 (n=3001)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.266)

- **PATRÓN** `libro_liquidez` > `1971.202` → IC=+0.281 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1971.202 (IC base=+0.266)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.280 (n=1500)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.327 (n=991)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1819` → IC=+0.310 (n=961)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1819 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.318 (n=838)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` < `0.3689` → IC=+0.295 (n=2184)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3689 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.2593` → IC=+0.298 (n=990)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.2593 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.584` → IC=+0.311 (n=295)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.584 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` < `0.1976` → IC=+0.290 (n=2134)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1976 (IC base=+0.292)

- **PATRÓN** `volumen_pendiente_norm` > `0.3423` → IC=+0.309 (n=348)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3423 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` < `1.5776` → IC=+0.298 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.5776 (IC base=+0.292)

- **PATRÓN** `volumen_spike_ratio` > `2.6701` → IC=+0.301 (n=945)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6701 (IC base=+0.292)

- **PATRÓN** `libro_liquidez` > `2051.2584` → IC=+0.307 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.2584 (IC base=+0.292)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.292 (n=1390)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 19.0 (IC base=+0.292)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `ibs_20min` > `0.7378` → IC=-0.185 (n=1046)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7378
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=3141)

- **PATRÓN** `ibs_20min` > `0.8799` → IC=+0.173 (n=992)

  - _Acción_: Kelly boost +0.87€ cuando `ibs_20min` > 0.8799 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` > `0.1525` → IC=+0.234 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1525 (IC base=+0.029)

- **PATRÓN** `dist_vwap_pct` < `0.3648` → IC=+0.233 (n=1354)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3648 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` < `1.0074` → IC=+0.244 (n=1217)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.0074 (IC base=+0.029)

- **PATRÓN** `volumen_regimen` > `0.6704` → IC=+0.230 (n=1235)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6704 (IC base=+0.029)

- **PATRÓN** `volumen_pendiente_norm` > `0.1022` → IC=+0.251 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.1022 (IC base=+0.029)

- **PATRÓN** `volumen_spike_ratio` < `1.3994` → IC=+0.248 (n=446)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.3994 (IC base=+0.029)

- **PATRÓN** `ballena_activa_n` < `103.0` → IC=+0.266 (n=1199)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 103.0 (IC base=+0.029)

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
- **FILTRO** `ibs_20min` < `0.76` → IC=-0.213 (n=1822)

  - _Acción_: SKIP cuando `ibs_20min` < 0.76
  - _Potencial_: sin este filtro IC_bueno=+0.304 (n=1829)

- **FILTRO** `ibs_20min` > `0.6486` → IC=-0.233 (n=894)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6486
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=2684)

- **FILTRO** `sigma_ewma_delta_pct` > `8.532` → IC=-0.241 (n=415)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.532
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=3163)

- **PATRÓN** `ibs_20min` > `0.76` → IC=+0.304 (n=1829)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.76 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.2157` → IC=+0.336 (n=808)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2157 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.563` → IC=+0.182 (n=568)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.563 (IC base=+0.046)

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

- **PATRÓN** `ibs_20min` < `0.5493` → IC=+0.145 (n=2362)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` < 0.5493 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.4547` → IC=+0.250 (n=1280)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4547 (IC base=+0.032)

- **PATRÓN** `volumen_regimen` < `0.7014` → IC=+0.263 (n=520)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.7014 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` < `0.2238` → IC=+0.241 (n=1327)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.2238 (IC base=+0.032)

- **PATRÓN** `volumen_pendiente_norm` > `0.0762` → IC=+0.261 (n=449)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.0762 (IC base=+0.032)

- **PATRÓN** `volumen_spike_ratio` < `2.4253` → IC=+0.251 (n=1135)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 2.4253 (IC base=+0.032)

- **PATRÓN** `ballena_activa_n` < `52.0` → IC=+0.270 (n=1149)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 52.0 (IC base=+0.032)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1215` → IC=+0.200 (n=5617)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1215 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.190 (n=13270)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 5.0 (IC base=+0.181)

- **PATRÓN** `ibs_20min` > `0.5585` → IC=+0.234 (n=12762)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5585 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.1637` → IC=+0.208 (n=5148)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1637 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.261` → IC=+0.260 (n=2511)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.261 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` < `1.1862` → IC=+0.169 (n=8466)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.1862 (IC base=+0.181)

- **PATRÓN** `volumen_regimen` > `0.6243` → IC=+0.166 (n=8465)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` > 0.6243 (IC base=+0.181)

- **PATRÓN** `volumen_pendiente_norm` > `0.2935` → IC=+0.205 (n=1855)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2935 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` < `1.5615` → IC=+0.180 (n=5443)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.5615 (IC base=+0.181)

- **PATRÓN** `volumen_spike_ratio` > `2.6084` → IC=+0.191 (n=4123)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_spike_ratio` > 2.6084 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `1982.02` → IC=+0.182 (n=11401)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 1982.02 (IC base=+0.181)

- **PATRÓN** `ballena_activa_n` < `95.0` → IC=+0.199 (n=11684)

  - _Acción_: Kelly boost +0.99€ cuando `ballena_activa_n` < 95.0 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0091` → IC=+0.183 (n=10811)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0091 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.0796` → IC=+0.227 (n=4099)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0796 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.209 (n=5840)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_20min` < `0.5` → IC=+0.236 (n=12295)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.1742` → IC=+0.174 (n=8756)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` < 0.1742 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.035` → IC=+0.197 (n=2010)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.035 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.69` → IC=+0.180 (n=10829)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 2.69 (IC base=+0.179)

- **PATRÓN** `volumen_regimen` < `1.1824` → IC=+0.162 (n=8768)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 1.1824 (IC base=+0.179)

- **PATRÓN** `volumen_pendiente_norm` > `0.2939` → IC=+0.224 (n=1815)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2939 (IC base=+0.179)

- **PATRÓN** `volumen_spike_ratio` > `2.6362` → IC=+0.187 (n=3844)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.6362 (IC base=+0.179)

- **PATRÓN** `ballena_activa_n` < `100.0` → IC=+0.191 (n=11246)

  - _Acción_: Kelly boost +0.96€ cuando `ballena_activa_n` < 100.0 (IC base=+0.179)

### GBM_LATE_15M_MULTIHORIZONTE#BNB#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.234 (n=715)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0052 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.3316` → IC=+0.231 (n=2137)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3316 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=801)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.221 (n=1437)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.9275` → IC=+0.295 (n=1425)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9275 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.983` → IC=+0.332 (n=676)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.983 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2805` → IC=+0.270 (n=320)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2805 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.8394` → IC=+0.209 (n=1347)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.8394 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.4363` → IC=+0.214 (n=2020)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4363 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.227 (n=2305)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.215)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.250 (n=1668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.249)

- **PATRÓN** `sigma_h` > `0.0073` → IC=+0.260 (n=756)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0073 (IC base=+0.249)

- **PATRÓN** `drift_60min` |x|≤ `0.0945` → IC=+0.304 (n=732)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0945 (IC base=+0.249)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.254 (n=1512)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.249)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.253 (n=803)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.249)

- **PATRÓN** `ibs_20min` < `0.2931` → IC=+0.272 (n=1464)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2931 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` < `0.1003` → IC=+0.251 (n=1455)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1003 (IC base=+0.249)

- **PATRÓN** `volumen_pendiente_norm` > `0.2973` → IC=+0.286 (n=250)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2973 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` < `1.4319` → IC=+0.270 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4319 (IC base=+0.249)

- **PATRÓN** `volumen_spike_ratio` > `2.679` → IC=+0.253 (n=525)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.679 (IC base=+0.249)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.254 (n=1870)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.249)

- **PATRÓN** `libro_liquidez` > `1528.1906` → IC=+0.259 (n=1663)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1528.1906 (IC base=+0.249)

- **PATRÓN** `ballena_activa_n` < `8.0` → IC=+0.254 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 8.0 (IC base=+0.249)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0027` → IC=+0.218 (n=641)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0027 (IC base=+0.155)

- **PATRÓN** `drift_60min` |x|≤ `0.1596` → IC=+0.184 (n=1282)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1596 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.170 (n=2029)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 5.0 (IC base=+0.155)

- **PATRÓN** `ibs_20min` > `0.3409` → IC=+0.224 (n=1922)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3409 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.1342` → IC=+0.215 (n=1147)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1342 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.332` → IC=+0.225 (n=361)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.332 (IC base=+0.155)

- **PATRÓN** `volumen_regimen` < `0.6895` → IC=+0.164 (n=846)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_regimen` < 0.6895 (IC base=+0.155)

- **PATRÓN** `volumen_pendiente_norm` > `0.2814` → IC=+0.196 (n=307)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2814 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` < `1.4131` → IC=+0.181 (n=628)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_spike_ratio` < 1.4131 (IC base=+0.155)

- **PATRÓN** `volumen_spike_ratio` > `2.5038` → IC=+0.162 (n=628)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_spike_ratio` > 2.5038 (IC base=+0.155)

- **PATRÓN** `ballena_activa_n` < `422.0` → IC=+0.159 (n=1844)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 422.0 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.168 (n=2018)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.234` → IC=+0.173 (n=1776)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.234 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=974)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.6184` → IC=+0.204 (n=2018)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6184 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.48` → IC=+0.194 (n=383)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.48 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.2053` → IC=+0.159 (n=2018)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.2053 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` < `0.0938` → IC=+0.147 (n=1708)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_pendiente_norm` < 0.0938 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4999` → IC=+0.152 (n=1898)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_spike_ratio` < 2.4999 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.4236` → IC=+0.146 (n=1898)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_spike_ratio` > 1.4236 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `202.0` → IC=+0.181 (n=612)

  - _Acción_: Kelly boost +0.90€ cuando `ballena_activa_n` < 202.0 (IC base=+0.144)

### GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.237 (n=980)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.213)

- **PATRÓN** `drift_60min` |x|≤ `0.3996` → IC=+0.225 (n=1902)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3996 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=797)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1115)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.213)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.441` → IC=+0.299 (n=501)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.441 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` < `0.0988` → IC=+0.213 (n=1849)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0988 (IC base=+0.213)

- **PATRÓN** `volumen_pendiente_norm` > `0.3549` → IC=+0.232 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3549 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` < `1.767` → IC=+0.215 (n=922)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.767 (IC base=+0.213)

- **PATRÓN** `volumen_spike_ratio` > `2.7088` → IC=+0.227 (n=949)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.7088 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.220 (n=2577)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `1963.5896` → IC=+0.226 (n=980)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1963.5896 (IC base=+0.213)

- **PATRÓN** `sigma_h` < `0.0104` → IC=+0.246 (n=1630)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0104 (IC base=+0.234)

- **PATRÓN** `drift_60min` |x|≤ `0.1428` → IC=+0.274 (n=815)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1428 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.280 (n=706)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.234)

- **PATRÓN** `ibs_20min` < `0.0083` → IC=+0.301 (n=816)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0083 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.514` → IC=+0.273 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.514 (IC base=+0.234)

- **PATRÓN** `volumen_pendiente_norm` > `0.3558` → IC=+0.278 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3558 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` < `1.7477` → IC=+0.235 (n=778)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.7477 (IC base=+0.234)

- **PATRÓN** `volumen_spike_ratio` > `2.1533` → IC=+0.238 (n=1178)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1533 (IC base=+0.234)

- **PATRÓN** `libro_liquidez` > `2051.2584` → IC=+0.241 (n=617)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2051.2584 (IC base=+0.234)

- **PATRÓN** `ballena_activa_n` < `16.0` → IC=+0.235 (n=1160)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 16.0 (IC base=+0.234)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.174 (n=2072)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0074 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.4062` → IC=+0.168 (n=2072)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.4062 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=2153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3118` → IC=+0.214 (n=2071)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3118 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1414` → IC=+0.200 (n=1259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1414 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.752` → IC=+0.201 (n=359)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.752 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `1.0223` → IC=+0.159 (n=1823)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` < 1.0223 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.103` → IC=+0.180 (n=846)

  - _Acción_: Kelly boost +0.90€ cuando `volumen_pendiente_norm` > 0.103 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `1.8174` → IC=+0.150 (n=1354)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.8174 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `2.5053` → IC=+0.167 (n=677)

  - _Acción_: Kelly boost +0.84€ cuando `volumen_spike_ratio` > 2.5053 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `4612.7985` → IC=+0.188 (n=1381)

  - _Acción_: Kelly boost +0.94€ cuando `libro_liquidez` > 4612.7985 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `139.0` → IC=+0.160 (n=2007)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 139.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.153 (n=2179)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0072 (IC base=+0.126)

- **PATRÓN** `drift_60min` |x|≤ `0.3953` → IC=+0.143 (n=2179)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.72€ cuando `drift_60min` |x|≤ 0.3953 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.166 (n=1039)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `ibs_20min` < `0.6854` → IC=+0.185 (n=2179)

  - _Acción_: Kelly boost +0.93€ cuando `ibs_20min` < 0.6854 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.1533` → IC=+0.155 (n=2183)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1533 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.826` → IC=+0.157 (n=764)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 6.826 (IC base=+0.126)

- **PATRÓN** `volumen_regimen` < `0.8557` → IC=+0.154 (n=1453)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 0.8557 (IC base=+0.126)

- **PATRÓN** `volumen_pendiente_norm` > `0.2997` → IC=+0.196 (n=330)

  - _Acción_: Kelly boost +0.98€ cuando `volumen_pendiente_norm` > 0.2997 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` < `1.81` → IC=+0.135 (n=1361)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 1.81 (IC base=+0.126)

- **PATRÓN** `volumen_spike_ratio` > `2.5482` → IC=+0.128 (n=680)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` > 2.5482 (IC base=+0.126)

- **PATRÓN** `libro_liquidez` > `7562.5057` → IC=+0.193 (n=988)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 7562.5057 (IC base=+0.126)

- **PATRÓN** `ballena_activa_n` < `68.0` → IC=+0.146 (n=882)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 68.0 (IC base=+0.126)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.178 (n=1056)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0103 (IC base=+0.129)

- **PATRÓN** `drift_60min` |x|≤ `0.4428` → IC=+0.130 (n=2048)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.4428 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=1117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.129)

- **PATRÓN** `ibs_20min` > `0.4915` → IC=+0.215 (n=2328)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4915 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `1.0682` → IC=+0.218 (n=462)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0682 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.599` → IC=+0.278 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.599 (IC base=+0.129)

- **PATRÓN** `volumen_regimen` < `1.1741` → IC=+0.143 (n=2328)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 1.1741 (IC base=+0.129)

- **PATRÓN** `volumen_pendiente_norm` < `0.1612` → IC=+0.136 (n=2364)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` < 0.1612 (IC base=+0.129)

- **PATRÓN** `volumen_spike_ratio` < `1.4387` → IC=+0.150 (n=753)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 1.4387 (IC base=+0.129)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2433)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.129)

- **PATRÓN** `libro_liquidez` > `2792.8737` → IC=+0.206 (n=1056)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2792.8737 (IC base=+0.129)

- **PATRÓN** `ballena_activa_n` < `20.0` → IC=+0.167 (n=745)

  - _Acción_: Kelly boost +0.83€ cuando `ballena_activa_n` < 20.0 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.138 (n=2380)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0108 (IC base=+0.120)

- **PATRÓN** `drift_60min` |x|≤ `0.108` → IC=+0.174 (n=795)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.87€ cuando `drift_60min` |x|≤ 0.108 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.139 (n=2427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 5.0 (IC base=+0.120)

- **PATRÓN** `ibs_20min` < `0.6` → IC=+0.217 (n=2387)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.1986` → IC=+0.147 (n=2252)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1986 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.461` → IC=+0.131 (n=2101)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 2.461 (IC base=+0.120)

- **PATRÓN** `volumen_regimen` < `1.1756` → IC=+0.130 (n=2380)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_regimen` < 1.1756 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` < `0.1654` → IC=+0.123 (n=2303)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` < 0.1654 (IC base=+0.120)

- **PATRÓN** `volumen_pendiente_norm` > `0.275` → IC=+0.150 (n=318)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_pendiente_norm` > 0.275 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` < `1.4461` → IC=+0.136 (n=740)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` < 1.4461 (IC base=+0.120)

- **PATRÓN** `volumen_spike_ratio` > `2.4234` → IC=+0.137 (n=739)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 2.4234 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `2654.4448` → IC=+0.192 (n=1079)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 2654.4448 (IC base=+0.120)

- **PATRÓN** `ballena_activa_n` < `42.0` → IC=+0.130 (n=1928)

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

- **PATRÓN** `drift_60min` |x|≤ `0.0884` → IC=+0.261 (n=731)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0884 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.247 (n=1074)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.228)

- **PATRÓN** `ibs_20min` < `0.4267` → IC=+0.256 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4267 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.2961` → IC=+0.234 (n=576)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2961 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.331` → IC=+0.257 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.331 (IC base=+0.228)

- **PATRÓN** `volumen_regimen` > `0.641` → IC=+0.235 (n=2193)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.641 (IC base=+0.228)

- **PATRÓN** `volumen_pendiente_norm` > `0.2804` → IC=+0.285 (n=296)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2804 (IC base=+0.228)

- **PATRÓN** `volumen_spike_ratio` > `1.4406` → IC=+0.231 (n=2039)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.4406 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `2591.6802` → IC=+0.228 (n=1462)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2591.6802 (IC base=+0.228)

### GBM_LATE_15M_PYCONFIRMADO
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.208 (n=1431)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.182)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.191 (n=1087)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0089 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.129` → IC=+0.204 (n=1431)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.129 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.216 (n=1623)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.182)

- **PATRÓN** `ibs_20min` > `0.7224` → IC=+0.232 (n=2168)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.7224 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.7907` → IC=+0.204 (n=481)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7907 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.626` → IC=+0.212 (n=1404)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.626 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` < `0.8616` → IC=+0.204 (n=1954)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8616 (IC base=+0.182)

- **PATRÓN** `volumen_regimen` > `0.6952` → IC=+0.185 (n=2617)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_regimen` > 0.6952 (IC base=+0.182)

- **PATRÓN** `volumen_pendiente_norm` > `0.0999` → IC=+0.192 (n=1168)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.0999 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` < `1.4308` → IC=+0.199 (n=1054)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` < 1.4308 (IC base=+0.182)

- **PATRÓN** `volumen_spike_ratio` > `2.1943` → IC=+0.186 (n=1433)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_spike_ratio` > 2.1943 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=3675)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.02 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `2695.8014` → IC=+0.189 (n=2905)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2695.8014 (IC base=+0.182)

- **PATRÓN** `ballena_activa_n` < `150.0` → IC=+0.194 (n=3033)

  - _Acción_: Kelly boost +0.97€ cuando `ballena_activa_n` < 150.0 (IC base=+0.182)

- **PATRÓN** `sigma_h` < `0.0038` → IC=+0.134 (n=1172)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0038 (IC base=+0.088)

- **PATRÓN** `ibs_20min` < `0.381` → IC=+0.160 (n=2340)

  - _Acción_: Kelly boost +0.80€ cuando `ibs_20min` < 0.381 (IC base=+0.088)

- **PATRÓN** `ballena_activa_n` < `19.0` → IC=+0.128 (n=1142)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 19.0 (IC base=+0.088)

### GBM_LATE_15M_PYCONFIRMADO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.203 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.178)

- **PATRÓN** `drift_60min` |x|≤ `0.3269` → IC=+0.200 (n=922)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3269 (IC base=+0.178)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.206 (n=843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.178)

- **PATRÓN** `ibs_20min` > `0.6334` → IC=+0.234 (n=614)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.6334 (IC base=+0.178)

- **PATRÓN** `dist_vwap_pct` > `0.3086` → IC=+0.197 (n=272)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.3086 (IC base=+0.178)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.068` → IC=+0.197 (n=394)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 3.068 (IC base=+0.178)

- **PATRÓN** `volumen_regimen` < `0.8725` → IC=+0.203 (n=615)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8725 (IC base=+0.178)

- **PATRÓN** `volumen_pendiente_norm` > `0.0718` → IC=+0.183 (n=364)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.0718 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` < `2.2054` → IC=+0.188 (n=793)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_spike_ratio` < 2.2054 (IC base=+0.178)

- **PATRÓN** `volumen_spike_ratio` > `1.4107` → IC=+0.179 (n=901)

  - _Acción_: Kelly boost +0.89€ cuando `volumen_spike_ratio` > 1.4107 (IC base=+0.178)

- **PATRÓN** `libro_liquidez` > `14647.5968` → IC=+0.183 (n=614)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 14647.5968 (IC base=+0.178)

- **PATRÓN** `ballena_activa_n` < `158.0` → IC=+0.206 (n=396)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 158.0 (IC base=+0.178)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.184 (n=368)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0028 (IC base=+0.119)

- **PATRÓN** `drift_60min` |x|≤ `0.2682` → IC=+0.142 (n=963)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.71€ cuando `drift_60min` |x|≤ 0.2682 (IC base=+0.119)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=996)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.119)

- **PATRÓN** `ibs_20min` < `0.6326` → IC=+0.169 (n=963)

  - _Acción_: Kelly boost +0.85€ cuando `ibs_20min` < 0.6326 (IC base=+0.119)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.713` → IC=+0.135 (n=217)

  - _Acción_: Kelly boost +0.67€ cuando `sigma_ewma_delta_pct` > 8.713 (IC base=+0.119)

- **PATRÓN** `volumen_regimen` > `1.0617` → IC=+0.147 (n=496)

  - _Acción_: Kelly boost +0.73€ cuando `volumen_regimen` > 1.0617 (IC base=+0.119)

- **PATRÓN** `volumen_pendiente_norm` > `0.1613` → IC=+0.166 (n=291)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_pendiente_norm` > 0.1613 (IC base=+0.119)

- **PATRÓN** `volumen_spike_ratio` < `2.1209` → IC=+0.134 (n=951)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_spike_ratio` < 2.1209 (IC base=+0.119)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=1416)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.119)

- **PATRÓN** `ballena_activa_n` < `217.0` → IC=+0.162 (n=708)

  - _Acción_: Kelly boost +0.81€ cuando `ballena_activa_n` < 217.0 (IC base=+0.119)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.247 (n=661)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.215)

- **PATRÓN** `drift_60min` |x|≤ `0.0934` → IC=+0.241 (n=330)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0934 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.231 (n=1040)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.215)

- **PATRÓN** `ibs_20min` > `0.3764` → IC=+0.257 (n=884)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3764 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` > `0.3567` → IC=+0.221 (n=299)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3567 (IC base=+0.215)

- **PATRÓN** `dist_vwap_pct` < `0.2053` → IC=+0.221 (n=893)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2053 (IC base=+0.215)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.874` → IC=+0.246 (n=399)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.874 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` < `0.8344` → IC=+0.227 (n=660)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.8344 (IC base=+0.215)

- **PATRÓN** `volumen_regimen` > `1.1625` → IC=+0.220 (n=330)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.1625 (IC base=+0.215)

- **PATRÓN** `volumen_pendiente_norm` > `0.2672` → IC=+0.250 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2672 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` < `1.4216` → IC=+0.247 (n=326)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4216 (IC base=+0.215)

- **PATRÓN** `volumen_spike_ratio` > `1.7751` → IC=+0.229 (n=651)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 1.7751 (IC base=+0.215)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.216 (n=1107)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.215)

- **PATRÓN** `ibs_20min` < `0.1053` → IC=+0.167 (n=337)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` < 0.1053 (IC base=+0.060)

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

- **PATRÓN** `ibs_20min` < `0.5455` → IC=+0.132 (n=761)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` < 0.5455 (IC base=+0.053)

- **PATRÓN** `libro_liquidez` > `2719.8549` → IC=+0.143 (n=390)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2719.8549 (IC base=+0.053)

- **PATRÓN** `ballena_activa_n` < `21.0` → IC=+0.127 (n=556)

  - _Acción_: Kelly boost +0.64€ cuando `ballena_activa_n` < 21.0 (IC base=+0.053)

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
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.226 (n=5548)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.192 (n=17353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 5.0 (IC base=+0.183)

- **PATRÓN** `ibs_20min` > `0.4483` → IC=+0.231 (n=16626)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4483 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.9` → IC=+0.209 (n=2024)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.272` → IC=+0.255 (n=4063)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.272 (IC base=+0.183)

- **PATRÓN** `volumen_regimen` < `1.2206` → IC=+0.170 (n=11144)

  - _Acción_: Kelly boost +0.85€ cuando `volumen_regimen` < 1.2206 (IC base=+0.183)

- **PATRÓN** `volumen_pendiente_norm` > `0.2905` → IC=+0.207 (n=2209)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2905 (IC base=+0.183)

- **PATRÓN** `volumen_spike_ratio` > `2.6123` → IC=+0.197 (n=5389)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6123 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `1973.596` → IC=+0.185 (n=14852)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1973.596 (IC base=+0.183)

- **PATRÓN** `ballena_activa_n` < `112.0` → IC=+0.204 (n=15247)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 112.0 (IC base=+0.183)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.193 (n=10059)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0073 (IC base=+0.188)

- **PATRÓN** `drift_60min` |x|≤ `0.3797` → IC=+0.193 (n=13276)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.3797 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.209 (n=5640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.188)

- **PATRÓN** `ibs_20min` < `0.5833` → IC=+0.242 (n=15097)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5833 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.1752` → IC=+0.171 (n=9237)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 0.1752 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.842` → IC=+0.205 (n=2093)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.842 (IC base=+0.188)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.578` → IC=+0.191 (n=14580)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 3.578 (IC base=+0.188)

- **PATRÓN** `volumen_regimen` < `0.705` → IC=+0.162 (n=4482)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_regimen` < 0.705 (IC base=+0.188)

- **PATRÓN** `volumen_pendiente_norm` > `0.2906` → IC=+0.253 (n=2040)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2906 (IC base=+0.188)

- **PATRÓN** `volumen_spike_ratio` > `2.6149` → IC=+0.197 (n=4753)

  - _Acción_: Kelly boost +0.99€ cuando `volumen_spike_ratio` > 2.6149 (IC base=+0.188)

- **PATRÓN** `ballena_activa_n` < `40.0` → IC=+0.216 (n=9383)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 40.0 (IC base=+0.188)

### GBM_LATE_15M_TARDIO#BNB#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.236 (n=916)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.224)

- **PATRÓN** `drift_60min` |x|≤ `0.3478` → IC=+0.227 (n=2715)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3478 (IC base=+0.224)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.238 (n=1321)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.224)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.227 (n=1821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.224)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.330 (n=1071)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.224)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.529` → IC=+0.354 (n=635)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.529 (IC base=+0.224)

- **PATRÓN** `volumen_pendiente_norm` > `0.2318` → IC=+0.280 (n=485)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2318 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` < `1.4457` → IC=+0.221 (n=869)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4457 (IC base=+0.224)

- **PATRÓN** `volumen_spike_ratio` > `2.2767` → IC=+0.236 (n=1182)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.2767 (IC base=+0.224)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.242 (n=2887)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.224)

- **PATRÓN** `libro_liquidez` > `2001.6602` → IC=+0.229 (n=1231)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2001.6602 (IC base=+0.224)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.251 (n=1111)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.224)

- **PATRÓN** `sigma_h` < `0.0084` → IC=+0.266 (n=2310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0084 (IC base=+0.262)

- **PATRÓN** `drift_60min` |x|≤ `0.1194` → IC=+0.286 (n=1017)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1194 (IC base=+0.262)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.268 (n=2117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.262)

- **PATRÓN** `ibs_20min` < `0.5093` → IC=+0.288 (n=2311)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5093 (IC base=+0.262)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.171` → IC=+0.266 (n=459)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.171 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` < `0.0953` → IC=+0.262 (n=2074)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.0953 (IC base=+0.262)

- **PATRÓN** `volumen_pendiente_norm` > `0.286` → IC=+0.288 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.286 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` < `1.4431` → IC=+0.264 (n=730)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` < 1.4431 (IC base=+0.262)

- **PATRÓN** `volumen_spike_ratio` > `2.6447` → IC=+0.273 (n=729)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.6447 (IC base=+0.262)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.264 (n=2597)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.262)

- **PATRÓN** `libro_liquidez` > `1649.7388` → IC=+0.269 (n=2063)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1649.7388 (IC base=+0.262)

- **PATRÓN** `ballena_activa_n` < `12.0` → IC=+0.266 (n=1034)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 12.0 (IC base=+0.262)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.198 (n=899)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0028 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.1043` → IC=+0.166 (n=1184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.1043 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=2812)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.3706` → IC=+0.225 (n=2403)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3706 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.1252` → IC=+0.197 (n=1389)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1252 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.553` → IC=+0.162 (n=445)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.553 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.174` → IC=+0.154 (n=2344)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` < 3.174 (IC base=+0.151)

- **PATRÓN** `volumen_regimen` < `0.6302` → IC=+0.175 (n=897)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_regimen` < 0.6302 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` < `0.0725` → IC=+0.155 (n=2398)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_pendiente_norm` < 0.0725 (IC base=+0.151)

- **PATRÓN** `volumen_pendiente_norm` > `0.2717` → IC=+0.185 (n=385)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_pendiente_norm` > 0.2717 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` < `2.1861` → IC=+0.160 (n=2314)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_spike_ratio` < 2.1861 (IC base=+0.151)

- **PATRÓN** `volumen_spike_ratio` > `1.5289` → IC=+0.155 (n=2349)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_spike_ratio` > 1.5289 (IC base=+0.151)

- **PATRÓN** `ballena_activa_n` < `266.0` → IC=+0.185 (n=1139)

  - _Acción_: Kelly boost +0.93€ cuando `ballena_activa_n` < 266.0 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.164 (n=2241)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0058 (IC base=+0.144)

- **PATRÓN** `drift_60min` |x|≤ `0.256` → IC=+0.164 (n=1971)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.256 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.171 (n=848)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 17.0 (IC base=+0.144)

- **PATRÓN** `ibs_20min` < `0.698` → IC=+0.198 (n=2240)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` < 0.698 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.194` → IC=+0.155 (n=372)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 11.194 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.254` → IC=+0.144 (n=2017)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` < 4.254 (IC base=+0.144)

- **PATRÓN** `volumen_regimen` < `1.1895` → IC=+0.155 (n=2240)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_regimen` < 1.1895 (IC base=+0.144)

- **PATRÓN** `volumen_pendiente_norm` > `0.2182` → IC=+0.193 (n=422)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_pendiente_norm` > 0.2182 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` < `2.4321` → IC=+0.149 (n=2135)

  - _Acción_: Kelly boost +0.75€ cuando `volumen_spike_ratio` < 2.4321 (IC base=+0.144)

- **PATRÓN** `volumen_spike_ratio` > `1.7752` → IC=+0.155 (n=1423)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 1.7752 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.144 (n=2907)

  - _Acción_: Kelly boost +0.72€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `ballena_activa_n` < `275.0` → IC=+0.159 (n=902)

  - _Acción_: Kelly boost +0.80€ cuando `ballena_activa_n` < 275.0 (IC base=+0.144)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.260 (n=924)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.234 (n=2897)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.226)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.227 (n=2472)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.226)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.303 (n=1026)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.303` → IC=+0.322 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.303 (IC base=+0.226)

- **PATRÓN** `volumen_pendiente_norm` < `0.1319` → IC=+0.230 (n=2587)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` < 0.1319 (IC base=+0.226)

- **PATRÓN** `volumen_spike_ratio` > `3.1891` → IC=+0.239 (n=896)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 3.1891 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.235 (n=3296)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1831.0032` → IC=+0.235 (n=1845)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1831.0032 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.245 (n=2282)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0106 (IC base=+0.241)

- **PATRÓN** `drift_60min` |x|≤ `0.1818` → IC=+0.258 (n=1141)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1818 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.262 (n=979)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.241)

- **PATRÓN** `ibs_20min` < `0.0303` → IC=+0.307 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0303 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.96` → IC=+0.293 (n=413)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.96 (IC base=+0.241)

- **PATRÓN** `volumen_pendiente_norm` > `0.3452` → IC=+0.300 (n=383)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.3452 (IC base=+0.241)

- **PATRÓN** `volumen_spike_ratio` > `2.1354` → IC=+0.250 (n=1643)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.1354 (IC base=+0.241)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.243 (n=1366)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.241)

- **PATRÓN** `libro_liquidez` > `2050.141` → IC=+0.256 (n=865)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2050.141 (IC base=+0.241)

- **PATRÓN** `ballena_activa_n` < `11.0` → IC=+0.256 (n=1077)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 11.0 (IC base=+0.241)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.197 (n=1262)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0039 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.4207` → IC=+0.159 (n=2859)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.4207 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.160 (n=2973)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 5.0 (IC base=+0.146)

- **PATRÓN** `ibs_20min` > `0.2479` → IC=+0.194 (n=2859)

  - _Acción_: Kelly boost +0.97€ cuando `ibs_20min` > 0.2479 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.1417` → IC=+0.172 (n=1511)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.1417 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.141` → IC=+0.160 (n=1160)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 4.141 (IC base=+0.146)

- **PATRÓN** `volumen_regimen` < `0.8651` → IC=+0.166 (n=1907)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_regimen` < 0.8651 (IC base=+0.146)

- **PATRÓN** `volumen_pendiente_norm` > `0.2802` → IC=+0.193 (n=372)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_pendiente_norm` > 0.2802 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` < `1.5231` → IC=+0.163 (n=1227)

  - _Acción_: Kelly boost +0.82€ cuando `volumen_spike_ratio` < 1.5231 (IC base=+0.146)

- **PATRÓN** `volumen_spike_ratio` > `2.1656` → IC=+0.157 (n=1265)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` > 2.1656 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `6294.9447` → IC=+0.244 (n=1296)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6294.9447 (IC base=+0.146)

- **PATRÓN** `ballena_activa_n` < `74.0` → IC=+0.173 (n=1217)

  - _Acción_: Kelly boost +0.87€ cuando `ballena_activa_n` < 74.0 (IC base=+0.146)

- **PATRÓN** `sigma_h` < `0.0075` → IC=+0.150 (n=2378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0075 (IC base=+0.128)

- **PATRÓN** `drift_60min` |x|≤ `0.4396` → IC=+0.139 (n=2378)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.4396 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.155 (n=871)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 17.0 (IC base=+0.128)

- **PATRÓN** `ibs_20min` < `0.737` → IC=+0.184 (n=2378)

  - _Acción_: Kelly boost +0.92€ cuando `ibs_20min` < 0.737 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1485` → IC=+0.144 (n=2167)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1485 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.113` → IC=+0.172 (n=364)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 11.113 (IC base=+0.128)

- **PATRÓN** `volumen_regimen` < `0.869` → IC=+0.139 (n=1586)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_regimen` < 0.869 (IC base=+0.128)

- **PATRÓN** `volumen_pendiente_norm` > `0.2969` → IC=+0.222 (n=300)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2969 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` < `2.2242` → IC=+0.131 (n=2013)

  - _Acción_: Kelly boost +0.65€ cuando `volumen_spike_ratio` < 2.2242 (IC base=+0.128)

- **PATRÓN** `volumen_spike_ratio` > `1.4297` → IC=+0.136 (n=2286)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_spike_ratio` > 1.4297 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `7242.0685` → IC=+0.212 (n=793)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7242.0685 (IC base=+0.128)

- **PATRÓN** `ballena_activa_n` < `67.0` → IC=+0.130 (n=777)

  - _Acción_: Kelly boost +0.65€ cuando `ballena_activa_n` < 67.0 (IC base=+0.128)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.156 (n=1304)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0103 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=1063)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.125)

- **PATRÓN** `ibs_20min` > `0.4444` → IC=+0.199 (n=2878)

  - _Acción_: Kelly boost +0.99€ cuando `ibs_20min` > 0.4444 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `1.067` → IC=+0.207 (n=497)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.067 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.748` → IC=+0.266 (n=728)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.748 (IC base=+0.125)

- **PATRÓN** `volumen_regimen` < `1.2204` → IC=+0.136 (n=2877)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_regimen` < 1.2204 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` < `0.1618` → IC=+0.126 (n=2991)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_pendiente_norm` < 0.1618 (IC base=+0.125)

- **PATRÓN** `volumen_pendiente_norm` > `0.2791` → IC=+0.137 (n=370)

  - _Acción_: Kelly boost +0.69€ cuando `volumen_pendiente_norm` > 0.2791 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` < `1.8314` → IC=+0.128 (n=1874)

  - _Acción_: Kelly boost +0.64€ cuando `volumen_spike_ratio` < 1.8314 (IC base=+0.125)

- **PATRÓN** `volumen_spike_ratio` > `1.4628` → IC=+0.127 (n=2810)

  - _Acción_: Kelly boost +0.63€ cuando `volumen_spike_ratio` > 1.4628 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.130 (n=2983)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.02 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2496.5462` → IC=+0.231 (n=1304)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2496.5462 (IC base=+0.125)

- **PATRÓN** `ballena_activa_n` < `24.0` → IC=+0.146 (n=897)

  - _Acción_: Kelly boost +0.73€ cuando `ballena_activa_n` < 24.0 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.151 (n=2411)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.01 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.1341` → IC=+0.155 (n=915)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.1341 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.131 (n=2830)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 5.0 (IC base=+0.118)

- **PATRÓN** `ibs_20min` < `0.6463` → IC=+0.212 (n=2740)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.6463 (IC base=+0.118)

- **PATRÓN** `dist_vwap_pct` < `0.2141` → IC=+0.136 (n=2364)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.2141 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.259` → IC=+0.135 (n=2640)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 3.259 (IC base=+0.118)

- **PATRÓN** `volumen_regimen` < `0.7104` → IC=+0.141 (n=1206)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.7104 (IC base=+0.118)

- **PATRÓN** `volumen_pendiente_norm` > `0.2248` → IC=+0.173 (n=469)

  - _Acción_: Kelly boost +0.87€ cuando `volumen_pendiente_norm` > 0.2248 (IC base=+0.118)

- **PATRÓN** `volumen_spike_ratio` < `1.4414` → IC=+0.156 (n=855)

  - _Acción_: Kelly boost +0.78€ cuando `volumen_spike_ratio` < 1.4414 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `2673.057` → IC=+0.208 (n=914)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2673.057 (IC base=+0.118)

- **PATRÓN** `ballena_activa_n` < `47.0` → IC=+0.134 (n=2250)

  - _Acción_: Kelly boost +0.67€ cuando `ballena_activa_n` < 47.0 (IC base=+0.118)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.249 (n=2430)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.236 (n=2843)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.235 (n=1962)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.230)

- **PATRÓN** `ibs_20min` > `0.61` → IC=+0.271 (n=2434)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.61 (IC base=+0.230)

- **PATRÓN** `dist_vwap_pct` > `0.1902` → IC=+0.246 (n=1467)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1902 (IC base=+0.230)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.737` → IC=+0.270 (n=912)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.737 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` < `1.2301` → IC=+0.238 (n=2720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2301 (IC base=+0.230)

- **PATRÓN** `volumen_regimen` > `0.6399` → IC=+0.233 (n=2720)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 0.6399 (IC base=+0.230)

- **PATRÓN** `volumen_pendiente_norm` > `0.2874` → IC=+0.254 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2874 (IC base=+0.230)

- **PATRÓN** `volumen_spike_ratio` > `2.5002` → IC=+0.250 (n=883)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_spike_ratio` > 2.5002 (IC base=+0.230)

- **PATRÓN** `libro_spread` < `0.04` → IC=+0.232 (n=3533)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.04 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `2963.6442` → IC=+0.239 (n=907)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2963.6442 (IC base=+0.230)

- **PATRÓN** `sigma_h` > `0.0255` → IC=+0.251 (n=942)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0255 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.237 (n=2663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.229)

- **PATRÓN** `ibs_20min` < `0.5146` → IC=+0.264 (n=2826)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5146 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.201` → IC=+0.266 (n=541)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.201 (IC base=+0.229)

- **PATRÓN** `volumen_regimen` > `1.2298` → IC=+0.259 (n=942)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.2298 (IC base=+0.229)

- **PATRÓN** `volumen_pendiente_norm` > `0.2819` → IC=+0.299 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2819 (IC base=+0.229)

- **PATRÓN** `volumen_spike_ratio` > `1.4316` → IC=+0.232 (n=2623)

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
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.156 (n=728)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.004 (IC base=+0.071)

- **PATRÓN** `ibs_20min` > `0.3889` → IC=+0.145 (n=1562)

  - _Acción_: Kelly boost +0.73€ cuando `ibs_20min` > 0.3889 (IC base=+0.071)

- **PATRÓN** `dist_vwap_pct` > `0.1483` → IC=+0.142 (n=812)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1483 (IC base=+0.071)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.999` → IC=+0.163 (n=455)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 8.999 (IC base=+0.071)

- **PATRÓN** `volumen_pendiente_norm` > `0.2761` → IC=+0.148 (n=217)

  - _Acción_: Kelly boost +0.74€ cuando `volumen_pendiente_norm` > 0.2761 (IC base=+0.071)

- **PATRÓN** `ibs_20min` < `0.2` → IC=+0.230 (n=573)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.358` → IC=+0.174 (n=133)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 10.358 (IC base=+0.056)

- **PATRÓN** `volumen_pendiente_norm` > `0.1467` → IC=+0.172 (n=233)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_pendiente_norm` > 0.1467 (IC base=+0.056)

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

- **PATRÓN** `ibs_20min` < `0.0468` → IC=+0.275 (n=167)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0468 (IC base=+0.072)

- **PATRÓN** `volumen_pendiente_norm` > `0.2164` → IC=+0.203 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_pendiente_norm` > 0.2164 (IC base=+0.072)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `ibs_20min` > `0.7041` → IC=-0.185 (n=90)

  - _Acción_: SKIP cuando `ibs_20min` > 0.7041
  - _Potencial_: sin este filtro IC_bueno=+0.120 (n=272)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.133 (n=475)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0059 (IC base=+0.095)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.157 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 17.0 (IC base=+0.095)

- **PATRÓN** `ibs_20min` > `0.616` → IC=+0.207 (n=455)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.616 (IC base=+0.095)

- **PATRÓN** `dist_vwap_pct` > `0.1247` → IC=+0.198 (n=263)

  - _Acción_: Kelly boost +0.99€ cuando `dist_vwap_pct` > 0.1247 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.194` → IC=+0.257 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.194 (IC base=+0.095)

- **PATRÓN** `volumen_regimen` < `0.5804` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `volumen_regimen` < 0.5804 (IC base=+0.095)

- **PATRÓN** `volumen_pendiente_norm` > `0.2854` → IC=+0.176 (n=72)

  - _Acción_: Kelly boost +0.88€ cuando `volumen_pendiente_norm` > 0.2854 (IC base=+0.095)

- **PATRÓN** `ibs_20min` < `0.0289` → IC=+0.296 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0289 (IC base=+0.017)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.686` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.686 (IC base=+0.017)

### GBM_LATE_60M#SOL#60min
- **PATRÓN** `ibs_20min` > `0.75` → IC=+0.167 (n=358)

  - _Acción_: Kelly boost +0.83€ cuando `ibs_20min` > 0.75 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.7377` → IC=+0.136 (n=130)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.7377 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.36` → IC=+0.172 (n=114)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 9.36 (IC base=+0.033)

- **PATRÓN** `volumen_pendiente_norm` > `0.279` → IC=+0.136 (n=75)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.279 (IC base=+0.033)

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

- **FILTRO** `drift_60min` |x|> `0.1933` → IC=-0.315 (n=63)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1933
  - _Potencial_: sin este filtro IC_bueno=-0.268 (n=192)

- **FILTRO** `ibs_20min` > `0.5429` → IC=-0.333 (n=130)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5429
  - _Potencial_: sin este filtro IC_bueno=-0.237 (n=131)

- **FILTRO** `dist_vwap_pct` > `0.4614` → IC=-0.405 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.4614
  - _Potencial_: sin este filtro IC_bueno=-0.275 (n=242)

- **FILTRO** `sigma_ewma_delta_pct` > `10.371` → IC=-0.321 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.371
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=235)

- **FILTRO** `volumen_pendiente_norm` > `0.0465` → IC=-0.371 (n=29)

  - _Acción_: SKIP cuando `volumen_pendiente_norm` > 0.0465
  - _Potencial_: sin este filtro IC_bueno=-0.270 (n=146)

### GBM_LATE_60M_FADE#BTC#60min
- **FILTRO** `hora_utc` < `6.0` → IC=-0.271 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=51)

- **FILTRO** `volumen_regimen` < `0.8402` → IC=-0.308 (n=24)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.8402
  - _Potencial_: sin este filtro IC_bueno=-0.193 (n=73)

- **FILTRO** `volumen_spike_ratio` > `2.3966` → IC=-0.237 (n=36)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.3966
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=38)

- **FILTRO** `sigma_h` > `0.0042` → IC=-0.300 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0042
  - _Potencial_: sin este filtro IC_bueno=-0.242 (n=87)

- **FILTRO** `volumen_regimen` > `0.8213` → IC=-0.333 (n=28)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8213
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=87)

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
- **FILTRO** `ibs_20min` > `0.1597` → IC=-0.124 (n=277)

  - _Acción_: SKIP cuando `ibs_20min` > 0.1597
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=538)

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

- **PATRÓN** `ibs_20min` < `0.1597` → IC=+0.150 (n=538)

  - _Acción_: Kelly boost +0.75€ cuando `ibs_20min` < 0.1597 (IC base=+0.057)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.069` → IC=+0.186 (n=183)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.069 (IC base=+0.057)

- **PATRÓN** `volumen_pendiente_norm` > `0.2227` → IC=+0.124 (n=123)

  - _Acción_: Kelly boost +0.62€ cuando `volumen_pendiente_norm` > 0.2227 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `3230.7051` → IC=+0.134 (n=408)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3230.7051 (IC base=+0.057)

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
  - _Potencial_: sin este filtro IC_bueno=+0.110 (n=198)

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

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.957 (IC base=+0.025)

- **PATRÓN** `volumen_pendiente_norm` > `0.2823` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `volumen_pendiente_norm` > 0.2823 (IC base=+0.025)

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

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.276 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.239)

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

- **PATRÓN** `elapsed_s` > `186.2` → IC=+0.250 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` > 186.2 (IC base=+0.239)

- **PATRÓN** `elapsed_s` < `202.5` → IC=+0.283 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `elapsed_s` < 202.5 (IC base=+0.239)

- **PATRÓN** `drift_15min` |x|≤ `2.3607` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 2.3607 (IC base=+0.239)

- **PATRÓN** `drift_60min` |x|≤ `0.947` → IC=+0.276 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.947 (IC base=+0.239)

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
- **FILTRO** `py_entrada` < `0.4` → IC=-0.122 (n=1362)

  - _Acción_: SKIP cuando `py_entrada` < 0.4
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=3547)

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
  - _Potencial_: sin este filtro IC_bueno=+0.055 (n=171)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.151 (n=41)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.5 (IC base=+0.058)

### LIQUIDACIONES_DEPTH_FASE0#ETH#15min
- **FILTRO** `py_entrada` < `0.53` → IC=-0.127 (n=344)

  - _Acción_: SKIP cuando `py_entrada` < 0.53
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=120)

- **FILTRO** `profundidad_ratio` < `56.8` → IC=-0.158 (n=153)

  - _Acción_: SKIP cuando `profundidad_ratio` < 56.8
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=311)

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
  - _Potencial_: sin este filtro IC_bueno=+0.039 (n=304)

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
- **FILTRO** `py_entrada` < `0.47` → IC=-0.165 (n=5940)

  - _Acción_: SKIP cuando `py_entrada` < 0.47
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=18442)

- **FILTRO** `py_entrada` > `0.59` → IC=-0.175 (n=6036)

  - _Acción_: SKIP cuando `py_entrada` > 0.59
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=19008)

### MOMENTUM_IBS_15M_BALLENA#BNB#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.195 (n=1088)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.117 (n=3343)

- **FILTRO** `py_entrada` > `0.64` → IC=-0.174 (n=1035)

  - _Acción_: SKIP cuando `py_entrada` > 0.64
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=3442)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.144 (n=1167)

  - _Acción_: Kelly boost +0.72€ cuando `ibs_20min` > 1.0 (IC base=+0.040)

- **PATRÓN** `libro_liquidez` > `1317.92` → IC=+0.138 (n=2216)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 1317.92 (IC base=+0.040)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.127 (n=2092)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.5 (IC base=+0.011)

- **PATRÓN** `libro_liquidez` > `1504.5254` → IC=+0.153 (n=1523)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 1504.5254 (IC base=+0.011)

### MOMENTUM_IBS_15M_BALLENA#BTC#15min
- **FILTRO** `py_entrada` < `0.45` → IC=-0.159 (n=825)

  - _Acción_: SKIP cuando `py_entrada` < 0.45
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=2746)

- **FILTRO** `py_entrada` > `0.57` → IC=-0.177 (n=875)

  - _Acción_: SKIP cuando `py_entrada` > 0.57
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2678)

### MOMENTUM_IBS_15M_BALLENA#DOGE#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.175 (n=1083)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.106 (n=3360)

- **FILTRO** `py_entrada` > `0.62` → IC=-0.202 (n=1067)

  - _Acción_: SKIP cuando `py_entrada` > 0.62
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=3505)

- **PATRÓN** `ibs_20min` > `0.9643` → IC=+0.131 (n=1515)

  - _Acción_: Kelly boost +0.65€ cuando `ibs_20min` > 0.9643 (IC base=+0.038)

- **PATRÓN** `libro_liquidez` > `1817.3772` → IC=+0.125 (n=1511)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 1817.3772 (IC base=+0.038)

### MOMENTUM_IBS_15M_BALLENA#XRP#15min
- **FILTRO** `py_entrada` < `0.49` → IC=-0.158 (n=1080)

  - _Acción_: SKIP cuando `py_entrada` < 0.49
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=3357)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.485` → IC=-0.171 (n=697)

  - _Acción_: SKIP cuando `py_entrada` < 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=2368)

- **FILTRO** `ballena_activa_n` > `11.0` → IC=-0.162 (n=758)

  - _Acción_: SKIP cuando `ballena_activa_n` > 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2306)

- **FILTRO** `py_entrada` > `0.585` → IC=-0.208 (n=761)

  - _Acción_: SKIP cuando `py_entrada` > 0.585
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=2796)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=3536)

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
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=875)

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
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=37590)

- **FILTRO** `py_entrada` < `0.33` → IC=-0.285 (n=13346)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.039 (n=40964)

- **FILTRO** `ibs_7min` < `0.2381` → IC=-0.229 (n=13563)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2381
  - _Potencial_: sin este filtro IC_bueno=-0.057 (n=40747)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.153 (n=18119)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=36191)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.242 (n=16749)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=+0.003 (n=51576)

- **FILTRO** `ibs_7min` > `0.2857` → IC=-0.182 (n=16911)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2857
  - _Potencial_: sin este filtro IC_bueno=-0.016 (n=51414)

### MOMENTUM_IBS_5M_BALLENA#BNB#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.146 (n=2696)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6779)

- **FILTRO** `py_entrada` < `0.46` → IC=-0.235 (n=4679)

  - _Acción_: SKIP cuando `py_entrada` < 0.46
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=4796)

- **FILTRO** `ibs_7min` < `0.7125` → IC=-0.244 (n=3126)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7125
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=6349)

- **FILTRO** `ballena_activa_n` > `6.0` → IC=-0.178 (n=2022)

  - _Acción_: SKIP cuando `ballena_activa_n` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=7453)

- **FILTRO** `py_entrada` > `0.71` → IC=-0.271 (n=2940)

  - _Acción_: SKIP cuando `py_entrada` > 0.71
  - _Potencial_: sin este filtro IC_bueno=-0.001 (n=8907)

- **FILTRO** `ibs_7min` > `0.7714` → IC=-0.210 (n=2961)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7714
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=8886)

### MOMENTUM_IBS_5M_BALLENA#BTC#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.265 (n=2140)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=7027)

- **FILTRO** `ibs_7min` < `0.7265` → IC=-0.200 (n=2289)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7265
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=6878)

- **FILTRO** `ballena_activa_n` > `154.0` → IC=-0.192 (n=2283)

  - _Acción_: SKIP cuando `ballena_activa_n` > 154.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=6884)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.263 (n=2296)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=7012)

- **FILTRO** `ibs_7min` > `0.268` → IC=-0.196 (n=2326)

  - _Acción_: SKIP cuando `ibs_7min` > 0.268
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6982)

- **FILTRO** `ballena_activa_n` > `151.0` → IC=-0.183 (n=2316)

  - _Acción_: SKIP cuando `ballena_activa_n` > 151.0
  - _Potencial_: sin este filtro IC_bueno=-0.069 (n=6992)

### MOMENTUM_IBS_5M_BALLENA#DOGE#5min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.159 (n=2200)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=6812)

- **FILTRO** `py_entrada` < `0.31` → IC=-0.314 (n=2215)

  - _Acción_: SKIP cuando `py_entrada` < 0.31
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=6797)

- **FILTRO** `ibs_7min` < `0.297` → IC=-0.245 (n=2973)

  - _Acción_: SKIP cuando `ibs_7min` < 0.297
  - _Potencial_: sin este filtro IC_bueno=-0.030 (n=6039)

- **FILTRO** `ballena_activa_n` > `5.0` → IC=-0.195 (n=2146)

  - _Acción_: SKIP cuando `ballena_activa_n` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.072 (n=6866)

- **FILTRO** `py_entrada` > `0.7` → IC=-0.256 (n=2939)

  - _Acción_: SKIP cuando `py_entrada` > 0.7
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=9674)

- **FILTRO** `ibs_7min` > `0.7347` → IC=-0.178 (n=3153)

  - _Acción_: SKIP cuando `ibs_7min` > 0.7347
  - _Potencial_: sin este filtro IC_bueno=+0.002 (n=9460)

### MOMENTUM_IBS_5M_BALLENA#ETH#5min
- **FILTRO** `py_entrada` < `0.34` → IC=-0.262 (n=2073)

  - _Acción_: SKIP cuando `py_entrada` < 0.34
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=6773)

- **FILTRO** `ibs_7min` < `0.7293` → IC=-0.186 (n=2211)

  - _Acción_: SKIP cuando `ibs_7min` < 0.7293
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6635)

- **FILTRO** `ballena_activa_n` > `27.0` → IC=-0.189 (n=2191)

  - _Acción_: SKIP cuando `ballena_activa_n` > 27.0
  - _Potencial_: sin este filtro IC_bueno=-0.073 (n=6655)

- **FILTRO** `py_entrada` > `0.67` → IC=-0.269 (n=2059)

  - _Acción_: SKIP cuando `py_entrada` > 0.67
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=7113)

- **FILTRO** `ibs_7min` > `0.2748` → IC=-0.180 (n=2292)

  - _Acción_: SKIP cuando `ibs_7min` > 0.2748
  - _Potencial_: sin este filtro IC_bueno=-0.063 (n=6880)

- **FILTRO** `ballena_activa_n` > `26.0` → IC=-0.176 (n=2258)

  - _Acción_: SKIP cuando `ballena_activa_n` > 26.0
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=6914)

### MOMENTUM_IBS_5M_BALLENA#SOL#5min
- **FILTRO** `py_entrada` < `0.33` → IC=-0.283 (n=2130)

  - _Acción_: SKIP cuando `py_entrada` < 0.33
  - _Potencial_: sin este filtro IC_bueno=-0.044 (n=6783)

- **FILTRO** `ibs_7min` < `0.2143` → IC=-0.232 (n=2218)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2143
  - _Potencial_: sin este filtro IC_bueno=-0.058 (n=6695)

- **FILTRO** `ballena_activa_n` > `13.0` → IC=-0.219 (n=2146)

  - _Acción_: SKIP cuando `ballena_activa_n` > 13.0
  - _Potencial_: sin este filtro IC_bueno=-0.064 (n=6767)

- **FILTRO** `py_entrada` > `0.61` → IC=-0.191 (n=3157)

  - _Acción_: SKIP cuando `py_entrada` > 0.61
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=9889)

### MOMENTUM_IBS_5M_BALLENA#XRP#5min
- **FILTRO** `py_entrada` < `0.32` → IC=-0.291 (n=2094)

  - _Acción_: SKIP cuando `py_entrada` < 0.32
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=6803)

- **FILTRO** `ibs_7min` < `0.2029` → IC=-0.221 (n=2224)

  - _Acción_: SKIP cuando `ibs_7min` < 0.2029
  - _Potencial_: sin este filtro IC_bueno=-0.066 (n=6673)

- **FILTRO** `ballena_activa_n` > `10.0` → IC=-0.202 (n=1987)

  - _Acción_: SKIP cuando `ballena_activa_n` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.077 (n=6910)

- **FILTRO** `py_entrada` > `0.66` → IC=-0.217 (n=3014)

  - _Acción_: SKIP cuando `py_entrada` > 0.66
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=9325)

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

- **FILTRO** `T_h` > `129.5932` → IC=-0.189 (n=162)

  - _Acción_: SKIP cuando `T_h` > 129.5932
  - _Potencial_: sin este filtro IC_bueno=-0.040 (n=487)

- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.185 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0034 (IC base=-0.078)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0069` → IC=-0.340 (n=48)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0069
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=145)

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
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=303)

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
- **PATRÓN** `streak_estiramiento` < `0.2662` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `streak_estiramiento` < 0.2662 (IC base=+0.000)

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
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=990)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.128 (n=41)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.004 (n=1330)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=1134)

- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=1183)

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
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=3984)

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
  - _Potencial_: sin este filtro IC_bueno=+0.012 (n=2190)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.199 (n=1184)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` < 0.0047 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.197 (n=1184)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0119 (IC base=+0.179)

- **PATRÓN** `drift_60min` |x|≤ `0.1749` → IC=+0.195 (n=3126)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.98€ cuando `drift_60min` |x|≤ 0.1749 (IC base=+0.179)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1333` → IC=+0.189 (n=1416)

  - _Acción_: Kelly boost +0.94€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1333 (IC base=+0.179)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=3301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.182 (n=3255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 15.0 (IC base=+0.179)

- **PATRÓN** `ibs_15` > `0.5593` → IC=+0.255 (n=3552)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5593 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` > `0.128` → IC=+0.169 (n=1687)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.128 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.4914` → IC=+0.167 (n=3180)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.4914 (IC base=+0.179)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.542` → IC=+0.254 (n=925)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.542 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `4721.7851` → IC=+0.198 (n=1184)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 4721.7851 (IC base=+0.179)

### UPDOWN_GBM#60min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.007 (n=1410)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.252 (n=268)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.219)

- **PATRÓN** `drift_60min` |x|≤ `0.0585` → IC=+0.267 (n=204)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0585 (IC base=+0.219)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2526` → IC=+0.246 (n=203)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2526 (IC base=+0.219)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2298` → IC=+0.232 (n=353)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2298 (IC base=+0.219)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.240 (n=609)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.219)

- **PATRÓN** `ibs_15` > `0.7199` → IC=+0.285 (n=608)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7199 (IC base=+0.219)

- **PATRÓN** `dist_vwap_pct` > `0.2443` → IC=+0.243 (n=259)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2443 (IC base=+0.219)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.96` → IC=+0.302 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.96 (IC base=+0.219)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.220 (n=788)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.219)

- **PATRÓN** `libro_liquidez` > `8959.7753` → IC=+0.230 (n=608)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8959.7753 (IC base=+0.219)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0034` → IC=+0.189 (n=236)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0034 (IC base=+0.145)

- **PATRÓN** `drift_60min` |x|≤ `0.0668` → IC=+0.158 (n=311)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.79€ cuando `drift_60min` |x|≤ 0.0668 (IC base=+0.145)

- **PATRÓN** `drift_15min` |x|≤ `0.3955` → IC=+0.147 (n=236)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 0.3955 (IC base=+0.145)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1438` → IC=+0.150 (n=470)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio_macro` |x|> 0.1438 (IC base=+0.145)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1315` → IC=+0.161 (n=278)

  - _Acción_: Kelly boost +0.80€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1315 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=649)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.150 (n=733)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 17.0 (IC base=+0.145)

- **PATRÓN** `ibs_15` > `0.5456` → IC=+0.244 (n=705)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5456 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.1194` → IC=+0.158 (n=434)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1194 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.835` → IC=+0.269 (n=132)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.835 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `3215.6409` → IC=+0.153 (n=705)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 3215.6409 (IC base=+0.145)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` > `17.774` → IC=-0.192 (n=37)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.774
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=329)

### UPDOWN_GBM#SOL#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1744` → IC=+0.139 (n=524)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.1744 (IC base=+0.096)

- **PATRÓN** `ibs_15` > `0.8947` → IC=+0.251 (n=263)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8947 (IC base=+0.096)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.132 (n=433)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.01 (IC base=+0.096)

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
- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.392 (n=210)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0056 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1501` → IC=+0.384 (n=419)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1501 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1413` → IC=+0.384 (n=239)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1413 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.379 (n=633)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.788` → IC=+0.400 (n=629)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.788 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.4158` → IC=+0.393 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4158 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.239` → IC=+0.385 (n=206)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 19.239 (IC base=+0.365)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.370 (n=766)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `10357.0212` → IC=+0.385 (n=285)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 10357.0212 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.368 (n=218)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0036 (IC base=+0.365)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.401 (n=109)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.365)

- **PATRÓN** `drift_60min` |x|≤ `0.0547` → IC=+0.365 (n=109)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0547 (IC base=+0.365)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1537` → IC=+0.381 (n=217)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.1537 (IC base=+0.365)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1356` → IC=+0.392 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1356 (IC base=+0.365)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.385 (n=327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.365)

- **PATRÓN** `ibs_15` > `0.8066` → IC=+0.391 (n=327)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8066 (IC base=+0.365)

- **PATRÓN** `dist_vwap_pct` > `0.2458` → IC=+0.397 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2458 (IC base=+0.365)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.617` → IC=+0.379 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 20.617 (IC base=+0.365)

- **PATRÓN** `libro_liquidez` > `15415.1121` → IC=+0.393 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 15415.1121 (IC base=+0.365)

- **PATRÓN** `ballena_activa_n` < `493.0` → IC=+0.411 (n=245)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 493.0 (IC base=+0.365)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.367 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.364)

- **PATRÓN** `sigma_h` > `0.0058` → IC=+0.386 (n=138)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0058 (IC base=+0.364)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0897` → IC=+0.379 (n=271)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0897 (IC base=+0.364)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.298` → IC=+0.381 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.298 (IC base=+0.364)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.392 (n=146)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.364)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.372 (n=139)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.364)

- **PATRÓN** `ibs_15` > `0.7479` → IC=+0.411 (n=303)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7479 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` > `0.4536` → IC=+0.381 (n=82)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4536 (IC base=+0.364)

- **PATRÓN** `dist_vwap_pct` < `0.2936` → IC=+0.366 (n=281)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2936 (IC base=+0.364)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.861` → IC=+0.390 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.861 (IC base=+0.364)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.368 (n=340)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.364)

- **PATRÓN** `libro_liquidez` > `3987.1822` → IC=+0.393 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3987.1822 (IC base=+0.364)

- **PATRÓN** `ballena_activa_n` < `137.0` → IC=+0.367 (n=246)

  - _Acción_: Kelly boost +1.00€ cuando `ballena_activa_n` < 137.0 (IC base=+0.364)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` > `0.0123` → IC=-0.224 (n=1074)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0123
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=3223)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.211 (n=1673)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=2624)

- **FILTRO** `libro_liquidez` < `4198.4937` → IC=-0.153 (n=2836)

  - _Acción_: SKIP cuando `libro_liquidez` < 4198.4937
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=1461)

- **PATRÓN** `ibs_15` > `0.6341` → IC=+0.282 (n=1040)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6341 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` > `0.1122` → IC=+0.209 (n=592)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1122 (IC base=-0.067)

- **PATRÓN** `dist_vwap_pct` < `0.2664` → IC=+0.197 (n=888)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.2664 (IC base=-0.067)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2301` → IC=+0.268 (n=1187)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2301 (IC base=-0.013)

- **PATRÓN** `ibs_15` < `0.3605` → IC=+0.282 (n=3558)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3605 (IC base=-0.013)

- **PATRÓN** `dist_vwap_pct` > `0.6621` → IC=+0.281 (n=451)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6621 (IC base=-0.013)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.218 (n=625)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=-0.187 (n=1876)

- **FILTRO** `sigma_h` < `0.0034` → IC=-0.229 (n=625)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=1876)

- **FILTRO** `sigma_ewma_delta_pct` > `23.202` → IC=-0.266 (n=361)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 23.202
  - _Potencial_: sin este filtro IC_bueno=-0.183 (n=2140)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.216 (n=65)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=2436)

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
  - _Potencial_: sin este filtro IC_bueno=+0.158 (n=677)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.162 (n=459)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0058 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.156 (n=347)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0049 (IC base=+0.151)

- **PATRÓN** `drift_60min` |x|≤ `0.0704` → IC=+0.194 (n=230)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.0704 (IC base=+0.151)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.3006` → IC=+0.190 (n=398)

  - _Acción_: Kelly boost +0.95€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.3006 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=524)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.152 (n=352)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.151)

- **PATRÓN** `ibs_15` > `0.6076` → IC=+0.251 (n=521)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6076 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.4658` → IC=+0.167 (n=133)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4658 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` < `0.1604` → IC=+0.151 (n=411)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1604 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.422` → IC=+0.245 (n=100)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.422 (IC base=+0.151)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.158 (n=677)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `9861.0594` → IC=+0.165 (n=174)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 9861.0594 (IC base=+0.151)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.250 (n=1276)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.245)

- **PATRÓN** `drift_15min` |x|≤ `0.766` → IC=+0.258 (n=1123)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.766 (IC base=+0.245)

- **PATRÓN** `delta_ratio_macro` |x|> `0.158` → IC=+0.257 (n=851)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.158 (IC base=+0.245)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2768` → IC=+0.246 (n=1088)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2768 (IC base=+0.245)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.248 (n=916)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.245)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.247 (n=1135)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.245)

- **PATRÓN** `ibs_15` < `0.3695` → IC=+0.275 (n=1276)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3695 (IC base=+0.245)

- **PATRÓN** `dist_vwap_pct` > `0.6047` → IC=+0.274 (n=193)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6047 (IC base=+0.245)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.498` → IC=+0.257 (n=566)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.498 (IC base=+0.245)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1729` → IC=-0.257 (n=336)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1729
  - _Potencial_: sin este filtro IC_bueno=-0.155 (n=656)

- **FILTRO** `drift_15min` |x|> `0.89` → IC=-0.283 (n=247)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.89
  - _Potencial_: sin este filtro IC_bueno=-0.159 (n=745)

- **FILTRO** `sigma_ewma_delta_pct` > `6.57` → IC=-0.201 (n=232)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.57
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=760)

- **FILTRO** `sigma_ewma_delta_pct` > `17.981` → IC=-0.145 (n=517)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.981
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=4121)

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
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.082 (IC base=-0.039)

- **PATRÓN** `ibs_15` < `0.3556` → IC=+0.291 (n=567)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3556 (IC base=-0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4456` → IC=+0.243 (n=597)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.4456 (IC base=-0.039)

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
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.299 (n=938)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0053 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.0531` → IC=+0.322 (n=357)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0531 (IC base=+0.292)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2423` → IC=+0.309 (n=355)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.2423 (IC base=+0.292)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.2247` → IC=+0.308 (n=634)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.2247 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.309 (n=1113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.292)

- **PATRÓN** `ibs_15` > `0.8393` → IC=+0.321 (n=1065)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8393 (IC base=+0.292)

- **PATRÓN** `dist_vwap_pct` > `0.2713` → IC=+0.329 (n=453)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2713 (IC base=+0.292)

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

- **PATRÓN** `drift_60min` |x|≤ `0.0569` → IC=+0.319 (n=191)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0569 (IC base=+0.289)

- **PATRÓN** `delta_ratio_macro` |x|> `0.26` → IC=+0.314 (n=191)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.26 (IC base=+0.289)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.289)

- **PATRÓN** `ibs_15` > `0.829` → IC=+0.316 (n=573)
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

- **PATRÓN** `drift_60min` |x|≤ `0.0518` → IC=+0.320 (n=165)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0518 (IC base=+0.295)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0673` → IC=+0.298 (n=493)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +1.00€ cuando `delta_ratio_macro` |x|> 0.0673 (IC base=+0.295)

- **PATRÓN** `divergencia_cvd_spot_perp` |x|≤ `0.1055` → IC=+0.330 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `divergencia_cvd_spot_perp` |x|≤ 0.1055 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.310 (n=508)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.296 (n=445)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `ibs_15` > `0.8516` → IC=+0.324 (n=493)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.8516 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` > `0.285` → IC=+0.328 (n=207)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.285 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.513` → IC=+0.364 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 23.513 (IC base=+0.295)

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

- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5593 sube el IC de +0.179 a +0.255 en UPDOWN_GBM#15min (n=3552). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.7199 sube el IC de +0.219 a +0.285 en UPDOWN_GBM#BTC#15min (n=608). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.5456 sube el IC de +0.145 a +0.244 en UPDOWN_GBM#ETH#15min (n=705). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#SOL#15min**: dentro de BUY_YES, IBS > 0.8947 sube el IC de +0.096 a +0.251 en UPDOWN_GBM#SOL#15min (n=263). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_YES, IBS > 0.5417 sube el IC de +0.203 a +0.280 en UPDOWN_GBM#XRP#15min (n=811). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.1111 sube el IC de +0.066 a +0.157 en UPDOWN_GBM#XRP#15min (n=773). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.6341 sube el IC de -0.067 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=1040). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3605 sube el IC de -0.013 a +0.282 en UPDOWN_GBM_15M_TARDIO (n=3558). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7572 sube el IC de +0.097 a +0.335 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=337). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_NO, IBS < 0.618 sube el IC de -0.195 a +0.287 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=59). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.6076 sube el IC de +0.151 a +0.251 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=521). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.3695 sube el IC de +0.245 a +0.275 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=1276). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.5625 sube el IC de -0.190 a +0.234 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=62). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.3556 sube el IC de -0.039 a +0.291 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=567). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5856 sube el IC de -0.206 a +0.326 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=21). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3333 sube el IC de -0.026 a +0.292 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=856). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.074 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7 (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_ETH_15M_HORA7#ETH#15min**: dentro de BUY_YES, IBS > 0.8434 sube el IC de +0.074 a +0.333 en UPDOWN_GBM_ETH_15M_HORA7#ETH#15min (n=16). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO**: dentro de BUY_YES, IBS > 0.8393 sube el IC de +0.292 a +0.321 en UPDOWN_GBM_IBS_ALTO (n=1065). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#BTC#15min**: dentro de BUY_YES, IBS > 0.829 sube el IC de +0.289 a +0.316 en UPDOWN_GBM_IBS_ALTO#BTC#15min (n=573). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_IBS_ALTO#ETH#15min**: dentro de BUY_YES, IBS > 0.8516 sube el IC de +0.295 a +0.324 en UPDOWN_GBM_IBS_ALTO#ETH#15min (n=493). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD**: dentro de BUY_YES, IBS > 0.788 sube el IC de +0.365 a +0.400 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD (n=629). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min**: dentro de BUY_YES, IBS > 0.8066 sube el IC de +0.365 a +0.391 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min (n=327). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min**: dentro de BUY_YES, IBS > 0.7479 sube el IC de +0.364 a +0.411 en UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min (n=303). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.

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
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0 | 631 | -0.001 | +73.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#15min | 631 | -0.001 | +73.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH | 459 | -0.025 | +41.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#ETH#15min | 459 | -0.025 | +41.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL | 133 | +0.070 | +23.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#SOL#15min | 133 | +0.070 | +23.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M_BUYNO_DEPTH_FASE0#XRP#15min | 36 | +0.026 | +4.76€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 39898 | -0.083 | -5016.83€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 2184 | +0.031 | -252.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 37714 | -0.090 | -4764.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 4480 | -0.116 | -773.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 4480 | -0.116 | -773.00€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 2184 | +0.031 | -252.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 2184 | +0.031 | -252.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 4315 | -0.105 | -873.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 4315 | -0.105 | -873.20€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 10626 | -0.024 | -994.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 10626 | -0.024 | -994.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 10512 | -0.106 | -814.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 10512 | -0.106 | -814.26€ | 1 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 7781 | -0.135 | -1309.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 7781 | -0.135 | -1309.39€ | 1 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA | 34730 | -0.015 | +3374.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#15min | 8986 | +0.005 | +1683.64€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#5min | 25744 | -0.023 | +1691.34€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC | 34730 | -0.015 | +3374.98€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#15min | 8986 | +0.005 | +1683.64€ | 0 | 0 |
| ✅ CANDIDATA10_CONFIRMACION_CRUZADA#BTC#5min | 25744 | -0.023 | +1691.34€ | 0 | 0 |
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
| ✅ FAVORITO_CONFIRMADO | 144199 | +0.116 | -5761.20€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 18544 | +0.183 | -547.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 634 | -0.019 | -69.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 116376 | +0.107 | -4821.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 8645 | +0.101 | -322.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 19300 | +0.108 | -1181.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 61 | -0.151 | +10.95€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BNB#240min | 15 | -0.243 | -11.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 19224 | +0.109 | -1180.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 27948 | +0.129 | -379.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 5187 | +0.189 | -166.44€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 42 | -0.114 | -22.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 19287 | +0.121 | -90.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 3432 | +0.083 | -99.59€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 19353 | +0.100 | -1345.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 72 | -0.122 | -6.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#DOGE#240min | 15 | -0.243 | -11.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 19266 | +0.101 | -1328.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 30665 | +0.125 | -550.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 7944 | +0.178 | -136.02€ | 1 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 19541 | +0.107 | -349.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 3168 | +0.100 | -56.59€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL | 27613 | +0.115 | -1377.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 5213 | +0.195 | -255.92€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 537 | +0.014 | -15.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 19818 | +0.095 | -939.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 2045 | +0.132 | -166.73€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 19320 | +0.105 | -927.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 67 | -0.080 | +6.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#240min | 13 | -0.022 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 19240 | +0.106 | -933.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 23194 | +0.197 | -1394.07€ | 1 | 5 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 23194 | +0.197 | -1394.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 5282 | +0.179 | -447.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 5282 | +0.179 | -447.76€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 2933 | +0.203 | -63.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 2933 | +0.203 | -63.89€ | 2 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 5220 | +0.181 | -413.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 5220 | +0.181 | -413.13€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 4530 | +0.248 | -147.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 4530 | +0.248 | -147.67€ | 0 | 3 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 3 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 5150 | +0.188 | -335.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 5150 | +0.188 | -335.38€ | 0 | 3 |
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
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 81066 | +0.202 | -5768.42€ | 2 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 81066 | +0.202 | -5768.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 13928 | +0.185 | -1434.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 13928 | +0.185 | -1434.01€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 13094 | +0.224 | -447.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 13094 | +0.224 | -447.90€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 13886 | +0.181 | -1452.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 13886 | +0.181 | -1452.81€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 13165 | +0.221 | -481.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 13165 | +0.221 | -481.35€ | 1 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 13445 | +0.202 | -874.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 13445 | +0.202 | -874.28€ | 0 | 2 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 13548 | +0.197 | -1078.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 13548 | +0.197 | -1078.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 31010 | +0.117 | +215.67€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 31010 | +0.117 | +215.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 15414 | +0.120 | +180.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 15414 | +0.120 | +180.47€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 15596 | +0.114 | +35.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 15596 | +0.114 | +35.20€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 2068 | +0.292 | -9.08€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 2068 | +0.292 | -9.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 947 | +0.279 | -27.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 947 | +0.279 | -27.23€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 1002 | +0.297 | +12.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 1002 | +0.297 | +12.85€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 119 | +0.351 | +5.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 119 | +0.351 | +5.31€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 954 | +0.441 | +4.00€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 954 | +0.441 | +4.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 463 | +0.435 | -4.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 463 | +0.435 | -4.68€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 445 | +0.449 | +8.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 445 | +0.449 | +8.13€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 46 | +0.396 | +0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 46 | +0.396 | +0.55€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0 | 1632 | +0.072 | -61.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#240min | 629 | +0.051 | -51.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#60min | 1003 | +0.085 | -9.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC | 73 | +0.113 | +3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#BTC#240min | 73 | +0.113 | +3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH | 1255 | +0.081 | -22.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#240min | 252 | +0.063 | -12.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#ETH#60min | 1003 | +0.085 | -9.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL | 304 | +0.026 | -43.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60_240MIN_DEPTH_FASE0#SOL#240min | 304 | +0.026 | -43.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0 | 61201 | +0.101 | -1539.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#15min | 4948 | +0.091 | +48.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#5min | 56253 | +0.101 | -1587.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC | 33680 | +0.105 | -372.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#15min | 4948 | +0.091 | +48.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#BTC#5min | 28732 | +0.108 | -420.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH | 12560 | +0.109 | -62.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#ETH#5min | 12560 | +0.109 | -62.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL | 14961 | +0.082 | -1105.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_DEPTH_FASE0#SOL#5min | 14961 | +0.082 | -1105.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 896 | +0.193 | -110.33€ | 2 | 4 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 896 | +0.193 | -110.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 896 | +0.193 | -110.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 896 | +0.193 | -110.33€ | 2 | 4 |
| ✅ GBM_LATE_15M | 42113 | +0.094 | +22009.73€ | 0 | 19 |
| ✅ GBM_LATE_15M#15min | 42113 | +0.094 | +22009.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 7020 | +0.216 | +5777.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 7020 | +0.216 | +5777.76€ | 0 | 23 |
| ✅ GBM_LATE_15M#BTC | 6303 | +0.180 | +4820.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 6303 | +0.180 | +4820.53€ | 0 | 23 |
| ✅ GBM_LATE_15M#DOGE | 7527 | +0.205 | +5856.08€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 7527 | +0.205 | +5856.08€ | 0 | 19 |
| ✅ GBM_LATE_15M#ETH | 5883 | +0.042 | +1649.94€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 5883 | +0.042 | +1649.94€ | 1 | 19 |
| ✅ GBM_LATE_15M#SOL | 5940 | -0.032 | +1255.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 5940 | -0.032 | +1255.46€ | 4 | 13 |
| ✅ GBM_LATE_15M#XRP | 9440 | -0.030 | +2649.96€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 9440 | -0.030 | +2649.96€ | 4 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 45312 | +0.085 | +24631.71€ | 0 | 19 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 45312 | +0.085 | +24631.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 8757 | +0.004 | +4416.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 8757 | +0.004 | +4416.39€ | 3 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 9582 | +0.010 | +2268.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 9582 | +0.010 | +2268.81€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 6283 | +0.278 | +6737.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 6283 | +0.278 | +6737.89€ | 0 | 21 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 8153 | +0.013 | +2015.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 8153 | +0.013 | +2015.54€ | 1 | 15 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 7229 | +0.039 | +2981.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 7229 | +0.039 | +2981.10€ | 3 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 5308 | +0.302 | +6211.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 5308 | +0.302 | +6211.98€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 33391 | +0.180 | +27054.95€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 33391 | +0.180 | +27054.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 5066 | +0.230 | +4506.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 5066 | +0.230 | +4506.67€ | 0 | 23 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 5252 | +0.150 | +3901.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 5252 | +0.150 | +3901.06€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 5349 | +0.223 | +4599.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 5349 | +0.223 | +4599.47€ | 0 | 21 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5666 | +0.138 | +4309.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5666 | +0.138 | +4309.89€ | 0 | 24 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 6275 | +0.124 | +4684.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 6275 | +0.124 | +4684.18€ | 0 | 25 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 5783 | +0.225 | +5053.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 5783 | +0.225 | +5053.68€ | 0 | 25 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 9014 | +0.133 | +4410.43€ | 0 | 18 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 9014 | +0.133 | +4410.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BNB#15min | 405 | +0.154 | +252.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 2686 | +0.146 | +1557.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 2686 | +0.146 | +1557.73€ | 0 | 22 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#DOGE#15min | 418 | +0.148 | +207.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 2665 | +0.137 | +1263.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 2665 | +0.137 | +1263.36€ | 0 | 15 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 2214 | +0.106 | +845.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 2214 | +0.106 | +845.40€ | 0 | 16 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 626 | +0.134 | +283.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 626 | +0.134 | +283.67€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO | 42278 | +0.185 | +33865.78€ | 0 | 21 |
| ✅ GBM_LATE_15M_TARDIO#15min | 42278 | +0.185 | +33865.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 6698 | +0.242 | +6250.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 6698 | +0.242 | +6250.61€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 6572 | +0.148 | +4516.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 6572 | +0.148 | +4516.94€ | 0 | 25 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 7146 | +0.233 | +6388.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 7146 | +0.233 | +6388.78€ | 0 | 19 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 6981 | +0.138 | +4987.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 6981 | +0.138 | +4987.90€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 7488 | +0.122 | +5188.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 7488 | +0.122 | +5188.66€ | 0 | 24 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 7393 | +0.230 | +6532.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 7393 | +0.230 | +6532.90€ | 0 | 19 |
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
| ✅ GBM_LATE_60M | 3444 | +0.066 | +1121.88€ | 0 | 8 |
| ✅ GBM_LATE_60M#60min | 3444 | +0.066 | +1121.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 1269 | +0.081 | +461.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 1269 | +0.081 | +461.71€ | 1 | 5 |
| ✅ GBM_LATE_60M#ETH | 1110 | +0.067 | +386.28€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 1110 | +0.067 | +386.28€ | 1 | 9 |
| ✅ GBM_LATE_60M#SOL | 1065 | +0.046 | +273.89€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 1065 | +0.046 | +273.89€ | 0 | 14 |
| 🚫 GBM_LATE_60M_FADE | 566 | -0.246 | -26.28€ | 8 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 566 | -0.246 | -26.28€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 212 | -0.248 | -15.06€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 212 | -0.248 | -15.06€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 201 | -0.229 | -3.50€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 201 | -0.229 | -3.50€ | 6 | 1 |
| 🚫 GBM_LATE_60M_FADE#SOL | 153 | -0.261 | -7.72€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 153 | -0.261 | -7.72€ | 5 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 1506 | +0.083 | +385.34€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 1506 | +0.083 | +385.34€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 588 | +0.081 | +144.52€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 588 | +0.081 | +144.52€ | 1 | 11 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 541 | +0.056 | +80.40€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 541 | +0.056 | +80.40€ | 2 | 10 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 377 | +0.123 | +160.41€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 377 | +0.123 | +160.41€ | 3 | 10 |
| ✅ LATE_WINDOW_5MIN | 165 | +0.278 | +162.71€ | 1 | 12 |
| ✅ LATE_WINDOW_5MIN#5min | 165 | +0.278 | +162.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 165 | +0.278 | +162.71€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 165 | +0.278 | +162.71€ | 1 | 12 |
| ✅ LEADLAG_BTC_XRP_15M | 3380 | +0.101 | +833.65€ | 0 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 3380 | +0.101 | +833.65€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 3380 | +0.101 | +833.65€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 3380 | +0.101 | +833.65€ | 0 | 1 |
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
| ✅ LIQUIDACIONES_DEPTH_FASE0 | 8614 | -0.028 | -7.47€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#15min | 4091 | -0.037 | -85.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#5min | 4523 | -0.020 | +77.85€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB | 260 | -0.042 | -10.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#15min | 133 | -0.026 | -1.52€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BNB#5min | 127 | -0.058 | -9.26€ | 2 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC | 2142 | -0.019 | +16.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#15min | 1023 | -0.024 | -3.05€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#BTC#5min | 1119 | -0.015 | +19.78€ | 0 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE | 950 | -0.024 | +12.43€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#15min | 476 | -0.042 | -12.45€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#DOGE#5min | 474 | -0.006 | +24.87€ | 1 | 1 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH | 1872 | -0.043 | -67.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#15min | 872 | -0.055 | -59.39€ | 3 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#ETH#5min | 1000 | -0.033 | -7.90€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL | 1689 | -0.020 | +27.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#15min | 803 | -0.033 | -6.91€ | 1 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#SOL#5min | 886 | -0.009 | +33.97€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP | 1701 | -0.029 | +14.39€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#15min | 784 | -0.036 | -2.00€ | 0 | 0 |
| ✅ LIQUIDACIONES_DEPTH_FASE0#XRP#5min | 917 | -0.022 | +16.40€ | 1 | 0 |
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
| ✅ MOMENTUM_IBS_15M_BALLENA | 49426 | -0.001 | +2438.77€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 49426 | -0.001 | +2438.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 8908 | +0.026 | +1127.27€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 8908 | +0.026 | +1127.27€ | 2 | 4 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 7124 | -0.034 | -106.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 7124 | -0.034 | -106.31€ | 2 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 9015 | +0.024 | +934.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 9015 | +0.024 | +934.17€ | 2 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 6970 | -0.048 | -150.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 6970 | -0.048 | -150.10€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 8356 | -0.005 | +230.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 8356 | -0.005 | +230.28€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 9053 | +0.015 | +403.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 9053 | +0.015 | +403.45€ | 1 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 6622 | -0.059 | -162.15€ | 4 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 6622 | -0.059 | -162.15€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 1225 | -0.000 | -15.31€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 1723 | -0.079 | -45.19€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 1723 | -0.079 | -45.19€ | 3 | 0 |
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
| ✅ MOMENTUM_IBS_5M_BALLENA | 122635 | -0.076 | +1608.58€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 122635 | -0.076 | +1608.58€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 21322 | -0.077 | +1086.14€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 21322 | -0.077 | +1086.14€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 18475 | -0.100 | -985.70€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 18475 | -0.100 | -985.70€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 21625 | -0.067 | +1144.18€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 21625 | -0.067 | +1144.18€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 18018 | -0.097 | -622.83€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 18018 | -0.097 | -622.83€ | 6 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 21959 | -0.057 | +311.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 21959 | -0.057 | +311.86€ | 4 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 21236 | -0.066 | +674.93€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 21236 | -0.066 | +674.93€ | 4 | 0 |
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
| ✅ ORDER_FLOW_5M_REACTIVO | 1437 | -0.012 | -10.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#5min | 1437 | -0.012 | -10.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB | 282 | +0.000 | +9.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#BNB#5min | 282 | +0.000 | +9.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE | 244 | -0.012 | +2.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#DOGE#5min | 244 | -0.012 | +2.06€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH | 372 | -0.043 | -27.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#ETH#5min | 372 | -0.043 | -27.87€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL | 306 | +0.013 | +4.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#SOL#5min | 306 | +0.013 | +4.70€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP | 233 | -0.011 | +0.38€ | 0 | 0 |
| ✅ ORDER_FLOW_5M_REACTIVO#XRP#5min | 233 | -0.011 | +0.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 900 | -0.069 | -41.12€ | 3 | 1 |
| ✅ PRICE_TARGET_GBM#BTC | 420 | -0.109 | -76.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 324 | -0.138 | -64.11€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 96 | -0.010 | -12.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 318 | -0.028 | +26.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 227 | -0.015 | +28.93€ | 2 | 1 |
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
| ✅ STREAK_FADE_15M | 722 | +0.029 | +35.50€ | 2 | 2 |
| ✅ STREAK_FADE_15M#15min | 722 | +0.029 | +35.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 302 | +0.023 | +3.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 302 | +0.023 | +3.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 59 | -0.008 | -1.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 73 | -0.007 | +0.78€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 73 | -0.007 | +0.78€ | 3 | 1 |
| ✅ STREAK_FADE_15M#XRP | 288 | +0.052 | +33.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 288 | +0.052 | +33.02€ | 0 | 5 |
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
| ✅ STREAK_MOM_5M | 10841 | +0.017 | +92.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 10841 | +0.017 | +92.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 2772 | +0.021 | +28.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 2772 | +0.021 | +28.81€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 2822 | +0.019 | +37.66€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 2822 | +0.019 | +37.66€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 2888 | +0.009 | -0.95€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 2888 | +0.009 | -0.95€ | 1 | 0 |
| ✅ STREAK_MOM_5M#XRP | 2359 | +0.018 | +27.44€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 2359 | +0.018 | +27.44€ | 2 | 0 |
| ✅ STRUCT_NO_15M | 9843 | +0.013 | -47.70€ | 2 | 0 |
| ✅ STRUCT_NO_15M#15min | 9843 | +0.013 | -47.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 4003 | +0.018 | -7.69€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 4003 | +0.018 | -7.69€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 3616 | +0.011 | -27.14€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 3616 | +0.011 | -27.14€ | 2 | 0 |
| ✅ STRUCT_NO_15M#SOL | 2224 | +0.009 | -12.88€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 2224 | +0.009 | -12.88€ | 1 | 0 |
| ✅ UPDOWN_GBM | 76049 | +0.053 | +6704.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 18909 | +0.083 | +4151.76€ | 0 | 11 |
| ✅ UPDOWN_GBM#240min | 2445 | +0.004 | +23.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 49956 | +0.050 | +2443.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 4473 | +0.007 | +86.77€ | 1 | 0 |
| ✅ UPDOWN_GBM#BNB | 6851 | +0.089 | +1075.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 1576 | +0.156 | +698.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#240min | 77 | -0.006 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5198 | +0.070 | +378.49€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 16322 | +0.055 | +1395.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 2443 | +0.089 | +594.89€ | 0 | 10 |
| ✅ UPDOWN_GBM#BTC#240min | 655 | +0.010 | +10.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 11134 | +0.061 | +726.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 1994 | +0.004 | +60.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 96 | -0.071 | +2.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 8393 | +0.069 | +886.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 1555 | +0.147 | +610.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#240min | 78 | +0.013 | -1.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 6760 | +0.051 | +277.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 17427 | +0.044 | +1129.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 4477 | +0.065 | +654.14€ | 0 | 11 |
| ✅ UPDOWN_GBM#ETH#240min | 639 | +0.005 | +16.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 10654 | +0.044 | +436.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 1568 | +0.012 | +19.34€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 89 | -0.104 | +2.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 16659 | +0.032 | +810.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 4700 | +0.035 | +390.05€ | 0 | 3 |
| ✅ UPDOWN_GBM#SOL#240min | 608 | -0.008 | +0.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 10361 | +0.037 | +418.43€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 911 | +0.006 | +6.76€ | 0 | 1 |
| ✅ UPDOWN_GBM#SOL#daily | 79 | -0.130 | -4.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 10395 | +0.064 | +1408.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 4158 | +0.101 | +1203.64€ | 0 | 9 |
| ✅ UPDOWN_GBM#XRP#240min | 388 | +0.010 | -0.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 5849 | +0.040 | +205.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 264 | -0.102 | +1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 838 | +0.365 | +310.48€ | 0 | 9 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 838 | +0.365 | +310.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 435 | +0.365 | +154.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 435 | +0.365 | +154.08€ | 0 | 11 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 403 | +0.364 | +156.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 403 | +0.364 | +156.40€ | 0 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO | 19723 | -0.025 | +4630.40€ | 3 | 6 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 19723 | -0.025 | +4630.40€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 1718 | -0.056 | +502.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 3498 | -0.112 | +135.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 3498 | -0.112 | +135.22€ | 4 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 948 | +0.216 | +770.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 2395 | +0.218 | +1566.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 2395 | +0.218 | +1566.80€ | 1 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 5630 | -0.066 | +672.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 5630 | -0.066 | +672.08€ | 4 | 7 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 5534 | -0.065 | +983.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 5534 | -0.065 | +983.03€ | 3 | 6 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 227 | +0.042 | +9.93€ | 0 | 1 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 227 | +0.042 | +9.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 227 | +0.042 | +9.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 227 | +0.042 | +9.93€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO | 1420 | +0.292 | +1219.98€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 1420 | +0.292 | +1219.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 763 | +0.289 | +619.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 763 | +0.289 | +619.58€ | 0 | 9 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 657 | +0.295 | +600.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 657 | +0.295 | +600.41€ | 0 | 9 |
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